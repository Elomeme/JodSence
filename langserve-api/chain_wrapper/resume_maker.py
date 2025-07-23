from dotenv import load_dotenv,find_dotenv
from langchain_community.chat_models.tongyi import ChatTongyi
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time

_ = load_dotenv(find_dotenv())

model = ChatTongyi(
    streaming=True,
    name="qwen-turbo"
)

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","""
        你是一位专业的简历生成专家，负责根据用户提供的信息生成专业、有吸引力的简历内容。
        
        请根据用户提供的以下信息，生成一份完整、专业的简历内容：
        - 基本信息（姓名、求职意向、联系方式等）
        - 教育背景
        - 工作经历
        - 技能专长
        - 项目经验
        
        生成的简历内容应该：
        1. 突出用户的核心优势和专业技能
        2. 使用专业、简洁的语言描述工作经历和项目经验
        3. 强调成就和贡献，尽可能使用数据和具体例子
        4. 针对求职意向进行适当的内容优化
        5. 保持整体结构清晰、逻辑连贯
        
        请使用markdown格式输出结果，确保内容专业、有吸引力且易于阅读。
        不要包含评估或建议，只需生成简历内容本身。
        
        输出格式示例：
        
        # 姓名
        
        ## 求职意向
        
        **联系方式**：电话 | 邮箱 | 地址
        
        ## 教育背景
        
        **学校名称** | 学历 | 专业 | 时间段
        
        ## 工作经历
        
        ### 公司名称 | 职位 | 时间段
        
        - 工作职责和成就1
        - 工作职责和成就2
        
        ## 技能专长
        
        - 技能1
        - 技能2
        
        ## 项目经验
        
        ### 项目名称
        
        - 项目描述
        - 个人职责和贡献
        """),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

def call_model(state: MessagesState):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {
    "configurable":{
        "session_id":time.time(),
        "thread_id":time.time()
    }
}
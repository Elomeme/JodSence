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
        你是一位专业的简历评估专家，负责分析求职者的简历并提供详细评估。
        请按以下步骤分析提供的简历内容：
        
        1. 简历打分：根据简历的完整性、专业性和匹配度，给出0-100的分数评估。
        
        2. 技能分析：
           - 提取简历中提到的技术技能和软技能
           - 评估技能的熟练度和相关性
           - 指出技能优势和不足
        
        3. 工作经历评估：
           - 分析工作经历的连贯性和进步性
           - 评估职责描述的专业性和成就导向
           - 指出经历中的亮点和可改进之处
        
        4. 教育背景评估：
           - 评估教育背景与求职方向的匹配度
           - 分析学术成就和相关课程的价值
        
        5. 简历优势：列出简历的3-5个主要优势
        
        6. 改进建议：提供3-5条具体的改进建议
        
        7. 适合岗位推荐：根据简历内容，推荐2-3个最适合的职位类型
        
        请使用markdown格式输出结果，确保分析专业、客观且有建设性。
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
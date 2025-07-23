# JodSence
欢迎了解 JobSense ——您的一站式智能求职伙伴！
# JobSense - 您的AI智能求职助手


**JobSense** 是一个集成了大型语言模型（LLM）的智能求职辅助平台，旨在为求职者提供从简历创建、评估、求职咨询到面试模拟的全流程AI支持。

## 🚀 产品简介

在求职的每个阶段，JobSense都与您同行。我们利用AI技术，将复杂的求职准备工作变得简单、高效和智能。我们的平台能够：

- **解答您的困惑**：提供关于行业趋势、薪资水平、公司文化的即时问答。
- **优化您的简历**：一键生成专业简历，并提供深度评估与改进建议。
- **提升您的面试技巧**：通过模拟真实面试场景，帮助您从容应对挑战。

## ✨ 主要功能

- **🤖 智能职业咨询**
  - **7x24小时在线**：随时解答您的职业发展、技能要求、薪资待遇等问题。
  - **多源信息整合**：结合本地知识库（如大厂面经、岗位要求）与实时网络搜索，提供全面、准确的答复。
  - **上下文记忆**：支持多轮对话，理解上下文，提供连贯的咨询体验。

- **🗣️ AI面试模拟**
  - **动态问题生成**：根据您的简历和目标岗位，智能生成高度相关的面试问题（技术问题、行为问题等）。
  - **实时回答评估**：对您的回答进行实时分析，从内容、逻辑、表达等多个维度提供反馈和改进建议。
  - **结构化流程**：采用先进的LangGraph工作流引擎，模拟真实面试的逻辑，实现智能化的工具选择和流程控制。

- **📄 智能简历评估**
  - **多维度分析**：从简历完整性、技能匹配度、工作经历、项目经验等多个维度进行综合打分。
  - **深度反馈**：精准识别简历中的优势与不足，并提供具体、可行的修改建议。
  - **岗位匹配推荐**：根据简历内容，为您推荐最适合的职位类型。

- **📝 一键简历生成与模板市场**
  - **表单化填写**：通过简单的表单填写个人信息，即可一键生成专业、排版精美的简历。
  - **AI内容优化**：利用AI润色工作经历和项目描述，使其更具吸引力。
  - **丰富模板选择**：提供多种风格的简历模板，满足不同行业和岗位的需求。

## 🛠️ 技术栈

- **后端 (`langserve-api`)**
  - **框架**: `Python`, `FastAPI`
  - **AI与工作流**: `LangChain`, `LangGraph`
  - **大语言模型**: `Tongyi Qwen (通义千问)`
  - **API服务**: `LangServe`

- **前端 (`node-site`)**
  - **框架**: `Node.js`, `Express`
  - **语言**: `HTML`, `CSS`, `JavaScript`
  - **UI交互**: `Marked.js` (用于Markdown渲染), 动态DOM操作

## 📁 项目结构
LLM_project/
├── langserve-api/         # 后端 FastAPI & LangChain 服务
│   ├── chain_wrapper/     # 核心AI链和工作流逻辑
│   │   ├── chat.py        # 职业咨询
│   │   ├── chat_reason.py # 面试模拟
│   │   ├── resume_evaluation.py # 简历评估
│   │   └── resume_maker.py      # 简历生成
│   ├── data/            # 本地知识库数据
│   ├── main.py          # FastAPI 应用入口
│   └── router_api.py    # API 路由
└── node-site/             # 前端 Node.js & 静态文件
├── static/            # HTML, CSS, JS 文件
│   ├── chat.html
│   ├── resume-evaluation.html
│   └── resume-maker.html
├── main.js            # Express 服务器入口
└── users.db           # 本地用户数据库 (SQLite)


## ⚡ 快速开始

请确保您的系统已安装 `Python 3.10+` 和 `Node.js 16+`。

### 1. 环境准备

- **获取API密钥**: 在 `langserve-api` 目录下创建 `.env` 文件，并填入您的通义千问和SerpAPI（如果使用）的API密钥。

  ```.env
  DASHSCOPE_API_KEY="sk-your-key"
  SERPAPI_API_KEY="your-serpapi-key"
  ```

### 2. 后端 (`langserve-api`) 设置

```bash
# 1. 进入后端目录
cd d:\HuaweiMoveData\Users\20105\Documents\xinan\shixishixun\myweb\LLM_project\langserve-api

# 2. 创建并激活虚拟环境 (推荐)
python -m venv venv
.\venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动后端服务 (默认运行在 http://127.0.0.1:8000)
uvicorn main:app --reload
```

### 3. 前端 (`node-site`) 设置

```bash
# 1. 打开一个新的终端，进入前端目录
cd d:\HuaweiMoveData\Users\20105\Documents\xinan\shixishixun\myweb\LLM_project\node-site

# 2. 安装依赖
npm install

# 3. 启动前端服务器 (通常运行在 http://127.0.0.1:3000)
node main.js
```

### 4. 访问应用

打开浏览器，访问前端服务器地址（例如 `http://127.0.0.1:3000` 或 `main.js` 中配置的端口），即可开始使用JobSense！

## 📖 使用指南

1.  **简历制作**: 访问 `简历制作` 页面，填写表单信息，选择模板，点击“生成简历”即可在右侧预览。
2.  **简历评估**: 访问 `简历评估` 页面，上传或粘贴您的简历内容，点击“开始分析”，AI将为您提供详细的评估报告。
3.  **求职助手**: 访问 `求职助手` 页面，在聊天框中输入您的问题，与AI顾问进行互动。
4.  **面试模拟**: （功能集成在求职助手中）您可以上传简历并发起面试请求，AI将扮演面试官与您进行模拟面试。

## 🤝 贡献

我们欢迎任何形式的贡献！如果您有好的想法或发现了Bug，请随时提交 `Pull Request` 或 `Issue`。

## 📄 许可证

本项目采用 [MIT](https://opensource.org/licenses/MIT) 许可证。

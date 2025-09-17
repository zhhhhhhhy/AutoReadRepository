import os
import asyncio
from openai import AsyncOpenAI
from Readfile import read_file
from dotenv import load_dotenv

load_dotenv()

agent_prompt = (
    "你是一名资深程序员技术助手，请用简洁、准确的中文"
    "对用户给出的文件内容进行总结，控制在 3~5 条要点内。"
)
async def getFileConclusion(file_content: str) -> str:
    """调用大模型对 file_content 进行中文总结，返回总结文本。"""
    client = AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE")
    )
    model_name = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

    messages = [
        {"role": "system", "content": agent_prompt},
        {"role": "user",   "content": f"文件内容如下：</file>\n{file_content}\n</file>"}
    ]

    response = await client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return response.choices[0].message.content.strip()

# async def getFileConclusion(filecontent):

#     client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"), 
#                          base_url=os.getenv("OPENAI_API_BASE"))
    
#     model_name = os.getenv('MODEL_NAME')

#     agent_messages = [
#         {"role": "system", "content": agent_prompt},
#     ]

#     response = await self.client.chat.completions.create(
#         model= model_name,
#         messages=agent_messages
#     )
#     messages = [
#         {"role": "user", "content": f"Problem: {problem_text}"}
#     ]

if __name__ == "__main__":
    text = read_file("README.md")
    summary = asyncio.run(getFileConclusion(text))
    print("=== 文件总结 ===")
    print(summary)

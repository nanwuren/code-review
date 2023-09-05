from zhipuai_sse import chat_with_assistant
from prompts_template import translate
from pypdf import PdfReader
import time

reader = PdfReader("C:/Users/T480/Desktop/EJ1078990.pdf")

pages = reader.pages
for page in pages:
    start = time.time()
    print("共{}页，当前第{}页".format(len(pages), page.page_number + 1))
    text = page.extract_text()
    conversation_prompt = [
        {"role": "user", "content": translate.format(source_language="英语", target_language="中文", content=text)},
    ]

    chat_with_assistant(conversation_prompt)
    end = time.time()
    print("翻译时长：{}秒".format(end - start))

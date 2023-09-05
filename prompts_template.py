from langchain.prompts import ChatPromptTemplate

translate = ChatPromptTemplate.from_messages([
    ("human", '''
    我有一段文本来自PDF文档，但其中包含了一些无关的页头和页脚信息。
    先去除这些页头和页脚内容，然后将剩余的文本从{source_language}翻译成{target_language}。如果可能，请尽量保持翻译的准确性和流畅性。只需回复翻译好的内容即可。需要翻译的内容如下：
    {content}.'''),
])

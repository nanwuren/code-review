import zhipuai

output_file = "sse_output.txt"

def chat_with_assistant(prompt):
    zhipuai.api_key = "56c56de2d2598775976bd548bad9d88b.bzHUZ1dOZHPWJCMr"
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=prompt,
        temperature=0.95,
        top_p=0.7,
    )

    with open(output_file, 'a', encoding='utf-8') as f:
        # 先清空文件
        # f.truncate(0)
        for event in response.events():
            if event.event == "add":
                # print(event.data)
                f.write(event.data)
            elif event.event == "error" or event.event == "interrupted":
                print(event.data, end="")
            elif event.event == "finish":
                print(event.data, end="")
                print(event.meta, end="")
            else:
                print(event.data, end="")

import csv
from transformers import AutoTokenizer, AutoModel


def load_prompt(prompt_file):
    with open(prompt_file, "r", newline='', encoding='utf-8') as file:
        prompt = file.read()
    return prompt

def llm_initialize():
    model_path = "model\chatglm-6b-int4"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    # 按需修改，目前只支持 4/8 bit 量化
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True).quantize(4).half().cuda()
    model = model.eval()

    return model, tokenizer


def read_csv_to_list(csv_filename):
    lines = 0
    # 从 CSV 文件中读取内容到列表
    content_list = []
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        for line in csvfile:
            lines += 1
            content_list.append(line.strip())  # 每行是一段话，直接添加到列表中
    return content_list, lines


def llm_response(prompt, model, tokenizer):
    # 加载模型
    # # 使用 IPython.display 流式打印模型输出
    # for response, history in model.stream_chat(
    #         tokenizer, prompt, history=[]):
    #     clear_output(wait=True)
    #     display(Markdown(response))
    response, history = model.chat(tokenizer, prompt, history=[])
    return response


def summarize_texts(texts):
    summarized_text = ""
    combine_prompt = load_prompt("Prompt_list/combine_res.txt")
    gpt_result = llm_response(combine_prompt + "\n" + texts, model, tokenizer)  # 调用你的 GPT 函数处理文本
    summarized_text += gpt_result

    # 在这里可以添加其他算法来进一步处理和总结文本

    return summarized_text


# 初始化模型
model, tokenizer = llm_initialize()

# 假设你的 CSV 文件名为 'processed_content.csv'
csv_filename = 'result/background.csv'

# 从 CSV 文件中读取内容到列表
content_list, lines = read_csv_to_list(csv_filename)

# 进入循环
output_text = ""
result = ""
for texts in content_list:
    output_text += texts
    # 对每段文本进行处理和总结
    result += summarize_texts(output_text)
    output_text = result
    result = ""

# 输出最终的总结结果
print(output_text)

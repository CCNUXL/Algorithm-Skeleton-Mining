from paper_splitter import Splitter


def load_prompt(prompt_file):
    with open(prompt_file, "r", newline='', encoding='utf-8') as file:
        prompt = file.read()
    return prompt

def LLM_response(prompt):
    response = prompt + '\n' + "OK"
    return response

def Structured_Mining(texts):
    # 六个层次的结构化挖掘
    # Background Aspect Scope Approach Model Dataset
    Structure_Info = {
        "Background": "",
        "Aspect": "",
        "Scope": "",
        "Approach": "",
        "Model": "",
        "Dataset": ""
    }
    Background = ""
    for i in range(0, len(texts)):
        # 动态存储六个维度的信息
        Dynamic_res_list = []  # 动态存储每个片段的结果（容量大小为10）
        res_list = [] # 每10个片段的结果总结后存入每个单元（容量大小为chunk_num/10)
        Dynamic_num = 0 # 动态存储块中的片段数量
        # prompt模版
        Prompt = load_prompt("项目代码/Algorithm_Skeleton/Hierarchical_Prompt_list/Background.txt")
        res = LLM_response(Prompt)
        Dynamic_res_list.append(res)
        Dynamic_num += 1
        if Dynamic_num == 10:
            Prompt = load_prompt("项目代码/Algorithm_Skeleton/Prompt_list/combine_res.txt")
            res = LLM_response(Prompt)
            res_list.append(res)
            Dynamic_num = 0
            Dynamic_res_list = []
        if i == len(texts)-1:
            Prompt = load_prompt("项目代码/Algorithm_Skeleton/Prompt_list/combine_res.txt")
            res = LLM_response(Prompt)
            Background = res

    print(Background)
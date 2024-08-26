import json
import os
import random

# 输入 gradio 的 style name 输出 json 格式
def load_json_data(name):
    json_name = f"{name}.json"
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 定位 ../workflow_api 中名为 json_name 的json
    json_path = os.path.join(current_dir, '..', 'workflow_api', json_name)

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

# “无” 风格
class change_file():
     
    def change_无(seed, width, height, prompt):
        data = load_json_data("无")
        if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
        data["3"]["inputs"]["seed"] = int(seed)
        data["5"]["inputs"]["width"] = int(width)
        data["5"]["inputs"]["height"] = int(height)
        data["6"]["inputs"]["text"] = str(prompt)

        return data


if __name__ == "__main__":
    data = change_file.change_无(1, 1920, 1080, "4")
    # data = json.dumps(data, indent=4)
    print(data)
    
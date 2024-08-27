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
        if prompt == "":
            bais_prompt = data["6"]["inputs"]["text"]
            data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
        else:
            data["6"]["inputs"]["text"] = prompt

        return data
    
    def change_经典渲染(seed, width, height, prompt):
         data = load_json_data("经典渲染")
         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["3"]["inputs"]["seed"] = int(seed)
         data["5"]["inputs"]["width"] = int(width)
         data["5"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data
    
    def change_绚丽鲜橙(seed, width, height, prompt):
         data = load_json_data("绚丽鲜橙")
         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["3"]["inputs"]["seed"] = int(seed)
         data["5"]["inputs"]["width"] = int(width)
         data["5"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data
    
    def change_真实照片(seed, width, height, prompt):
         data = load_json_data("真实照片")
         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["3"]["inputs"]["seed"] = int(seed)
         data["5"]["inputs"]["width"] = int(width)
         data["5"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data
    
    def change_马克笔手绘(seed, width, height, prompt):
         data = load_json_data("马克笔手绘")
         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["3"]["inputs"]["seed"] = int(seed)
         data["5"]["inputs"]["width"] = int(width)
         data["5"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data
    
    def change_真实内饰(seed, width, height, prompt):
         data = load_json_data("真实内饰")
         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["25"]["inputs"]["noise_seed"] = int(seed)
         data["27"]["inputs"]["width"] = int(width)
         data["27"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data


if __name__ == "__main__":
    data = change_file.change_无(1, 1920, 1080, "4")
    # data = json.dumps(data, indent=4)
    print(data)
    
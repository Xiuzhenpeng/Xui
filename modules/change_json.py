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
     
    def change_无(seed, width, height, prompt, cn_img_name, strength=1, start=0, end=1,):
        if cn_img_name == "":
            data = load_json_data("无")
        else:
             data = load_json_data("无_controlnet")
             data["10"]["inputs"]["image"] = cn_img_name
             data["13"]["inputs"]["image_gen_width"] = width
             data["13"]["inputs"]["image_gen_height"] = height
             data["9"]["inputs"]["strength"] = f"{strength}"
             data["9"]["inputs"]["start_percent"] = f"{start}"
             data["9"]["inputs"]["end_percent"] = f"{end}"

        if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
        data["3"]["inputs"]["seed"] = int(seed)
        data["5"]["inputs"]["width"] = int(width)
        data["5"]["inputs"]["height"] = int(height)

        # 在无style的情况下，用户的输入会完全生效，没有基础提示词
        if prompt == "":
            bais_prompt = data["6"]["inputs"]["text"]
            data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
        else:
            data["6"]["inputs"]["text"] = prompt

        return data
    
    def change_经典渲染(seed, width, height, prompt, cn_img_name, strength=1, start=0, end=1,):
         if cn_img_name == "":
             data = load_json_data("经典渲染")
         else:
            data = load_json_data("经典渲染_controlnet")
            data["10"]["inputs"]["image"] = cn_img_name
            data["13"]["inputs"]["image_gen_width"] = width
            data["13"]["inputs"]["image_gen_height"] = height
            data["9"]["inputs"]["strength"] = f"{strength}"
            data["9"]["inputs"]["start_percent"] = f"{start}"
            data["9"]["inputs"]["end_percent"] = f"{end}"

         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["3"]["inputs"]["seed"] = int(seed)
         data["5"]["inputs"]["width"] = int(width)
         data["5"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data
    
    def change_绚丽鲜橙(seed, width, height, prompt, cn_img_name, strength=1, start=0, end=1,):
         if cn_img_name == "":
             data = load_json_data("绚丽鲜橙")
         else:
            data = load_json_data("绚丽鲜橙_controlnet")
            data["10"]["inputs"]["image"] = cn_img_name
            data["13"]["inputs"]["image_gen_width"] = width
            data["13"]["inputs"]["image_gen_height"] = height
            data["9"]["inputs"]["strength"] = f"{strength}"
            data["9"]["inputs"]["start_percent"] = f"{start}"
            data["9"]["inputs"]["end_percent"] = f"{end}"

         if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
         data["3"]["inputs"]["seed"] = int(seed)
         data["5"]["inputs"]["width"] = int(width)
         data["5"]["inputs"]["height"] = int(height)
         bais_prompt = data["6"]["inputs"]["text"]
         data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
         return data
    
    def change_真实照片(seed, width, height, prompt, cn_img_name, strength=1, start=0, end=1,):
        if cn_img_name == "":
            data = load_json_data("真实照片")
        else:
             data = load_json_data("真实照片_controlnet")
             data["10"]["inputs"]["image"] = cn_img_name
             data["13"]["inputs"]["image_gen_width"] = width
             data["13"]["inputs"]["image_gen_height"] = height
             data["9"]["inputs"]["strength"] = f"{strength}"
             data["9"]["inputs"]["start_percent"] = f"{start}"
             data["9"]["inputs"]["end_percent"] = f"{end}"

        if seed == -1:
                seed = random.randint(1, 2 ** 32 - 1)
        data["3"]["inputs"]["seed"] = int(seed)
        data["5"]["inputs"]["width"] = int(width)
        data["5"]["inputs"]["height"] = int(height)
        bais_prompt = data["6"]["inputs"]["text"]
        data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
        return data
    
    def change_马克笔手绘(seed, width, height, prompt, cn_img_name, strength=1, start=0, end=1,):
        if cn_img_name == "":
            data = load_json_data("马克笔手绘")
        else:
             data = load_json_data("马克笔手绘_controlnet")
             data["10"]["inputs"]["image"] = cn_img_name
             data["13"]["inputs"]["image_gen_width"] = width
             data["13"]["inputs"]["image_gen_height"] = height
             data["9"]["inputs"]["strength"] = f"{strength}"
             data["9"]["inputs"]["start_percent"] = f"{start}"
             data["9"]["inputs"]["end_percent"] = f"{end}"

        if seed == -1:
            seed = random.randint(1, 2 ** 32 - 1)
        data["3"]["inputs"]["seed"] = int(seed)
        data["5"]["inputs"]["width"] = int(width)
        data["5"]["inputs"]["height"] = int(height)
        bais_prompt = data["6"]["inputs"]["text"]
        data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"
         
        return data
    
    def change_真实内饰(seed, width, height, prompt, cn_img_name, strength=1, start=0, end=1,):
        if seed == -1:
            seed = random.randint(1, 2 ** 32 - 1)

        if cn_img_name == "":
            data = load_json_data("真实内饰")
            data["25"]["inputs"]["noise_seed"] = int(seed)
            data["27"]["inputs"]["width"] = int(width)
            data["27"]["inputs"]["height"] = int(height)
            bais_prompt = data["6"]["inputs"]["text"]
            data["6"]["inputs"]["text"] = f"{prompt}, {bais_prompt}"

        else:
            data = load_json_data("真实内饰_controlnet")
            data["3"]["inputs"]["noise_seed"] = int(seed)
            data["6"]["inputs"]["width"] = int(width)
            data["6"]["inputs"]["height"] = int(height)
            bais_prompt = data["5"]["inputs"]["clip_l"]
            data["5"]["inputs"]["clip_l"] = f"{prompt}, {bais_prompt}"
            data["5"]["inputs"]["t5xxl"] = f"{prompt}, {bais_prompt}"
            data["16"]["inputs"]["image"] = cn_img_name

            data["49"]["inputs"]["image_gen_width"] = width
            data["49"]["inputs"]["image_gen_height"] = height
            data["14"]["inputs"]["strength"] = strength * 0.7
        
        return data


if __name__ == "__main__":
    data = change_file.change_无(1, 1920, 1080, "4")
    # data = json.dumps(data, indent=4)
    print(data)
    
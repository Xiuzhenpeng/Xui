class change_file():
    def change_无(seed, width, height, prompt, img, strength=1, start=0, end=1,):
        base_prompt = "a sport car <random:running|parking> on <random:road|grass>, <random:winter,snow|sunshine>, <random:front|side|front side|rear>"
        if prompt == "":
            prompt = base_prompt
        else:
            prompt = prompt
        # No Controlnet
        if img is None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"realvisxlV40_v40Bakedvae.safetensors",
                "gridgenpresets":"无",
                "comfyuicustomworkflow": "无",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":prompt,
            }
        else:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"realvisxlV40_v40Bakedvae.safetensors",
                "gridgenpresets":"无_controlnet",
                "comfyuicustomworkflow": "无_controlnet",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":prompt,
                "initimage":img,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":strength,
                "comfyrawworkflowinputdecimalpositivepromptnodestartpercentm":start,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":end,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthn":width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightn":height
            }
        return prompt_data
    
    def change_真实内饰(seed, width, height, prompt, img, strength=1, start=0, end=1,):
        base_prompt = "<random:aion|arcfox|avatr|baic|byd|changan|chery|denza|exeed|gac|geely|hozon|jetour|leap|li|lixiang|lynk|nio|rivian|voyah|xpeng|zeekr>, the interior of a car, specifically the driver's seat and the dashboard, The car has a <random:beige|black|blue|white> leather interior with a touch screen display in the center console, The dashboard is made of <random:wood|leather|fabric> and has a modern design with <random:a|two> large touch screen in the middle, The steering wheel is leather-wrapped and the gear shift is located on the <random:right|left> side of the console, There are two side mirrors on the left side and a rearview mirror on the top right corner, The seats are upholstered in a <random:light beige|black|blue|white> color and appear to be made of <random:leather|fabric>, The background shows a <random:beautiful,ocean|mountains|studio,light|simple,background>, The overall aesthetic of the car is luxurious and modern,"
        controlnet_base_prompt = "the interior of a car, specifically the driver's seat and the dashboard, The interior of the interior is clean and modern, with a sleek design,"

        if img == None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "gridgenpresets":"真实内饰",
                "comfyuicustomworkflow": "真实内饰",
                "comfyrawworkflowinputseedrandomnoisenodenoiseseedz":seed,
                "comfyrawworkflowinputintegeremptysdlatentimagenodewidthbb":width,
                "comfyrawworkflowinputintegeremptysdlatentimagenodeheightbb":height,
                "comfyrawworkflowinputtextcliptextencodepositivepromptnodetextg":f"{prompt}, {base_prompt}"
            }
            
        else:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "gridgenpresets":"真实内饰_controlnet",
                "comfyuicustomworkflow": "真实内饰_controlnet",
                "comfyrawworkflowinputtextunetloadernodeunetnamebg": "flux1-dev.safetensors",
                "comfyrawworkflowinputseedxlabssamplernodenoiseseedd":seed,
                "width":width,
                "height":height,
                "initimage":img,
                "comfyrawworkflowinputdecimalapplyfluxcontrolnetnodestrengtho":0.75 * strength,
                "comfyrawworkflowinputtextcliptextencodefluxnodecliplf":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputtextcliptextencodefluxnodetxxlf":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthbx": width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightbx": height
            }
        return prompt_data
    
    def change_经典渲染(seed, width, height, prompt, img, strength=1, start=0, end=1,):
        base_prompt = "car, electric car, futuristic design, aerodynamic, modern, luxury car, automotive design, studio lighting,"
        
        if img is None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"protovisionXLHighFidelity3D_releaseV660Bakedvae.safetensors",
                "gridgenpresets":"无",
                "comfyuicustomworkflow": "无",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}"
            }
        else:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"protovisionXLHighFidelity3D_releaseV660Bakedvae.safetensors",
                "gridgenpresets":"无_controlnet",
                "comfyuicustomworkflow": "无_controlnet",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}",
                "initimage":img,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":strength,
                "comfyrawworkflowinputdecimalpositivepromptnodestartpercentm":start,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":end,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthn":width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightn":height
            }
        return prompt_data

    def change_马克笔手绘(seed, width, height, prompt, img, strength=1, start=0, end=1,):
        base_prompt = "car sketch, concept design, automotive design, sport utility vehicle, simple background, modern, futuristic, dynamic lines, aggressive styling, large wheels, alloy rims, automotive illustration, hand-drawn, design concept, side view, rendered image, art, transportation design, vehicle concept"

        if img is None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"realvisxlV40_v40Bakedvae.safetensors",
                "gridgenpresets":"无",
                "comfyuicustomworkflow": "无",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}"
            }
        else:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"realvisxlV40_v40Bakedvae.safetensors",
                "gridgenpresets":"无_controlnet",
                "comfyuicustomworkflow": "无_controlnet",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}",
                "initimage":img,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":strength,
                "comfyrawworkflowinputdecimalpositivepromptnodestartpercentm":start,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":end,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthn":width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightn":height
            }
        return prompt_data

    def change_真实照片(seed, width, height, prompt, img, strength=1, start=0, end=1,):
        base_prompt = "car, modern, luxury car, automotive design, simple background, high-resolution image, real photo, HDR,"
        
        if img is None:        
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"realvisxlV40_v40Bakedvae.safetensors",
                "gridgenpresets":"无",
                "comfyuicustomworkflow": "无",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}"
            }
        else:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"realvisxlV40_v40Bakedvae.safetensors",
                "gridgenpresets":"无_controlnet",
                "comfyuicustomworkflow": "无_controlnet",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}",
                "initimage":img,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":strength,
                "comfyrawworkflowinputdecimalpositivepromptnodestartpercentm":start,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":end,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthn":width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightn":height
            }
        return prompt_data

    def change_绚丽鲜橙(seed, width, height, prompt, img, strength=1, start=0, end=1,):
        base_prompt = "car, electric car, futuristic design, vehicle front view, grille, aerodynamic, modern, luxury car, automotive design, orange light source, orange background, studio lighting, high-resolution image,"

        if img is None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"protovisionXLHighFidelity3D_releaseV660Bakedvae.safetensors",
                "gridgenpresets":"无",
                "comfyuicustomworkflow": "无",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}"
            }
        else:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "model":"protovisionXLHighFidelity3D_releaseV660Bakedvae.safetensors",
                "gridgenpresets":"无_controlnet",
                "comfyuicustomworkflow": "无_controlnet",
                "seed":seed,
                "width":width,
                "height":height,
                "prompt":f"{prompt}, {base_prompt}",
                "initimage":img,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":strength,
                "comfyrawworkflowinputdecimalpositivepromptnodestartpercentm":start,
                "comfyrawworkflowinputdecimalpositivepromptnodeendpercentm":end,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthn":width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightn":height
            }
        return prompt_data
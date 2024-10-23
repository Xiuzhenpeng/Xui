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
                "session_id":"",
                "images": 1,
                "cfgscale": 1,
                "steps": 20,
                "model":"flux1-dev-fp8.safetensors",
                "comfyuicustomworkflow":"真实内饰_controlnet",
                "seed":seed,
                "initimage":img,
                "comfyrawworkflowinputdecimalpositivepromptnodestrengtho": 0.5 * strength,
                "comfyrawworkflowinputtextcliptextencodepositivepromptnodetextx":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputintegeremptysdlatentimagenodeheightbc": height,
                "comfyrawworkflowinputintegeremptysdlatentimagenodewidthbc": width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightbg":height,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthbg":width,
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

    def change_Toyota(seed, width, height, prompt, img, strength=1, start=0, end=1,): 
        base_prompt = "a car, a toyota car, <random:toyota_porte, toyota_sera, toyota_tacoma_trd_off-road_double_cab, toyota_ts030_hybrid_test_car, toyota_proace_city_van_electric, toyota_raize_hybrid_z> a toyota car <random:running on road, parking in room, studio light>"
        controlnet_base_prompt = "a car, toyota car, toyota exterior design"

        if img == None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "gridgenpresets":"Toyota",
                "comfyuicustomworkflow": "Toyota",
                "comfyrawworkflowinputseedrandomnoisenodenoiseseedz":seed,
                "comfyrawworkflowinputintegeremptysdlatentimagenodewidthbb":width,
                "comfyrawworkflowinputintegeremptysdlatentimagenodeheightbb":height,
                "comfyrawworkflowinputtextcliptextencodepositivepromptnodetextg":f"{prompt}, {base_prompt}",
            }

        else:
            prompt_data = {
                "session_id":"",
                "images": 1,
                "cfgscale": 1,
                "steps": 20,
                "model":"flux1-dev-fp8.safetensors",
                "comfyuicustomworkflow":"Toyota_controlnet_2",
                # "seed":seed,
                "comfyrawworkflowinputseedxlabssamplernodenoiseseedd":seed,
                "width":width,
                "height":height,
                "initimage":img,
                "comfyrawworkflowinputdecimalapplyfluxcontrolnetnodestrengtho": 0.7 * strength,
                "comfyrawworkflowinputtextcliptextencodefluxnodecliplf":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputtextcliptextencodefluxnodetxxlf":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputintegeremptysdlatentimagenodeheightbc": height,
                "comfyrawworkflowinputintegeremptysdlatentimagenodewidthbc": width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightby":height,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthby":width,
            }

        return prompt_data

    def change_Volkswagen(seed, width, height, prompt, img, strength=1, start=0, end=1,): 
        base_prompt = "a car, a Volkswagen car, <random:volkswagen_polo, volkswagen_golf, volkswagen_tiguan, volkswagen_passat, volkswagen_jetta, volkswagen_touareg>, the car <random:running on road, parking in room, running in city, studio light>"
        controlnet_base_prompt = "a car, volkswagen car, volkswagen exterior design"

        if img == None:
            prompt_data = {
                "session_id": "",
                "images": 1,
                "gridgenpresets":"Toyota",
                "comfyuicustomworkflow": "Toyota",
                "comfyrawworkflowinputseedrandomnoisenodenoiseseedz":seed,
                "comfyrawworkflowinputintegeremptysdlatentimagenodewidthbb":width,
                "comfyrawworkflowinputintegeremptysdlatentimagenodeheightbb":height,
                "comfyrawworkflowinputtextcliptextencodepositivepromptnodetextg":f"{prompt}, {base_prompt}",
            }

        else:
            prompt_data = {
                "session_id":"",
                "images": 1,
                "cfgscale": 1,
                "steps": 20,
                "model":"flux1-dev-fp8.safetensors",
                "comfyuicustomworkflow":"Toyota_controlnet_2",
                # "seed":seed,
                "comfyrawworkflowinputseedxlabssamplernodenoiseseedd":seed,
                "width":width,
                "height":height,
                "initimage":img,
                "comfyrawworkflowinputdecimalapplyfluxcontrolnetnodestrengtho": 0.7 * strength,
                "comfyrawworkflowinputtextcliptextencodefluxnodecliplf":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputtextcliptextencodefluxnodetxxlf":f"{prompt}, {controlnet_base_prompt}",
                "comfyrawworkflowinputintegeremptysdlatentimagenodeheightbc": height,
                "comfyrawworkflowinputintegeremptysdlatentimagenodewidthbc": width,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenheightby":height,
                "comfyrawworkflowinputintegerhintimageenchancenodeimagegenwidthby":width,
            }

        return prompt_data
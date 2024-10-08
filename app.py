import random
import argparse
import requests

import gradio as gr

from modules.websockets_api_example_ws_images import inference_image
from modules.change_json import load_json_data
from modules.change_json import change_file


# 添加参数
parser = argparse.ArgumentParser(description="An example script.")

parser.add_argument("--port", type=int, default="8016", help="This app running on this port")
parser.add_argument("--comfy_port",type=int, default="8188", help="Comfyui running on this port")

args = parser.parse_args()

if __name__ == "__main__":

    # address = f"127.0.0.1:{args.comfy_port}"

    comfyurls = [
    "127.0.0.1:8160",
    "127.0.0.1:8161",
    "127.0.0.1:8162",
    "127.0.0.1:8163",
    # 添加更多URL...
    ]

css = """
#aspect-ratio-label .label-wrap {
    font-size: 3em;
    font-weight: bold;
}
#user_prompt-textbox {
    height: 143px !important;
}
"""
js_func = """
function refresh() {
    const url = new URL(window.location);

    const theme = url.searchParams.get('__theme');
    if (theme !== 'dark' && theme !== 'light') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

theme = gr.themes.Soft(
    primary_hue="sky",
)

# 获取less busy url
def get_least_busy_url(monitor_service_url="http://localhost:5000"):
    try:
        response = requests.get(f"{monitor_service_url}/least_busy_url")
        data = response.json()
        return data["least_busy_url"]
    except requests.RequestException as e:
        print(f"Error connecting to monitor service: {e}")
        return comfyurls[0]


# 对进行推理的 gradio 界面的参数进行预处理返回image
def inference_image_preprocess(style_name, random_seed: bool, seed_number, image_aspect_ratio, user_prompt, 
                               cn_img_name, strength, start, end):    
    
    # address = get_least_busy_url()
    address = comfyurls[0]

    # return json 格式
    json_file = load_json_data(style_name)

    # def seed
    if random_seed == True:
        seed = -1
    if random_seed == False:
        seed = seed_number

    # def width heigh
    if image_aspect_ratio == '1:1':
        width = 1024
        heigh = 1024
    if image_aspect_ratio == '16:9':
        width = 1344
        heigh = 756
    if image_aspect_ratio == '18:9':
        width = 1600
        heigh = 800
    
    # def prompt
    prompt = user_prompt

    change_method_name = f"change_{style_name}"
    change_method = getattr(change_file, change_method_name)
    if cn_img_name == "":
        json_file = change_method(seed, width, heigh, prompt, cn_img_name)
    else:
        json_file = change_method(seed, width, heigh, prompt, cn_img_name, strength, start, end)

    image = inference_image(json_file, address)

    return image


with gr.Blocks(css=css, js=js_func, theme=theme, title="IAT Design") as demo:
    gr.Markdown(
        """
        # IAT Design
        ##### 此页面目前处于Alpha阶段。仅用于效果展示，不保证图片质量
        默认深色主题，点击切换[浅色主题](https://192.168.58.22:8016/?__theme=light)，[深色主题](https://192.168.58.22:8016/?__theme=dark) ❗️切换主题会导致界面刷新，丢失当前界面信息
        """)
    with gr.Row(equal_height=False):
        with gr.Column(scale=2, ):
            image_show = gr.Image(label="展示图片", height=500, show_label=False, interactive=False, format="png")
            gr.Markdown("### ⚙️ 基础设置")
            with gr.Row(equal_height=False):
                with gr.Column(scale=1, min_width=300):
                    with gr.Column():
                        image_aspect_ratio = gr.Radio(value='16:9', label="✅ 图片比例", choices=['1:1', '16:9', '18:9'],
                                                    container=True, interactive=True, min_width=10,)
                    with gr.Row():
                        seed = random.randint(1, 2 ** 32 - 1)

                        random_seed = gr.Checkbox(label="🎲随机种子", min_width=10, scale=1, value=True,
                                                interactive=True)
                        seed_number = gr.Number(value=seed, minimum=1, maximum=2 ** 32, label="种子",
                                                min_width=10, container=False, scale=1, visible=False, interactive=True)

                        random_seed.input(lambda show: gr.update(visible=not show), random_seed, seed_number, show_progress=False)

                with gr.Column(scale=4):
                    user_prompt = gr.Textbox(label="提示词", placeholder="⌨️输入你的提示词", lines=6, show_label=False, container=False,
                                            elem_id="user_prompt-textbox")
            with gr.Column(min_width=200):
                generate = gr.Button(value="生成图片", size='lg', variant='primary')
                
        with gr.Column(scale=1,):
                with gr.Tab("🎨Style"):
                    images = [
                        ("./style_pics/a1.png", "无"),
                        ("./style_pics/20240821_090405.png", "真实内饰"),
                        ("./style_pics/00131-1676567236.png", "经典渲染"),
                        ("./style_pics/00213-636703613.png", "绚丽鲜橙"),
                        ("./style_pics/00021-1676567236.png", "真实照片"),
                        ("./style_pics/00052-1493661434.png", "马克笔手绘"),                        
                    ]                    
                    
                    style_pics = gr.Gallery(value=images, object_fit="contain", show_download_button=False, 
                            label="风格展示", interactive=False, format="png", allow_preview=False, height=660,
                            container=False, selected_index=0)
                    style_name = gr.Text(visible=False, value="无")

                    def on_select(evt: gr.SelectData):
                        return f"{images[evt.index][1]}"
                    style_pics.select(on_select, inputs=[], outputs=[style_name])

                # Controlnet
                with gr.Tab("🔧ControlNet", visible=True):

                    # from comfyui.upload_image import upload_image

                    user_image = gr.Image(height=360, type="pil", label="Controlnet图片", sources=('upload', 'clipboard'))
                    controlnet_image_name = gr.Textbox(visible=False)

                    from modules.upload_image import upload_image
                    address = comfyurls[0]
                    user_image.change(lambda img: upload_image(img, address), user_image, outputs=controlnet_image_name)
                    user_image.clear(fn=lambda: "", outputs=controlnet_image_name)
                    
                    gr.Radio(value="Lineart", choices=["Lineart",], label="选择ControlNet种类")

                    with gr.Accordion(label="⚙️高级设置",open=False,) as accordion:
                        controlnet_strength = gr.Slider(0, 1, label="Controlnet权重", value=1,
                                                        info="权重数值越大和Controlnet图片相似度越高", interactive=True)
                        with gr.Row():
                            def controlnet_number_waring (numb1, numb2):
                                if numb1 > numb2:
                                    gr.Warning('介入时机要小于终止时机')

                            controlnet_start = gr.Slider(0, 1, label="介入时机", interactive=True)
                            controlnet_end = gr.Slider(0, 1, label="终止时机", value=1, interactive=True)

                            controlnet_start.change(controlnet_number_waring, inputs=[controlnet_start, controlnet_end])
                            controlnet_end.change(controlnet_number_waring, inputs=[controlnet_start, controlnet_end])

                # 用户建议
                with gr.Tab("🎤意见与建议"):
                    
                    gr.Markdown("""#### 如果你觉得有什么使用上的不便
                                #### 或有其他方面的建议或意见
                                #### 欢迎在下面留言""")
                    
                    user_flag = gr.Textbox(container=False, placeholder="在这里写下留言，确认提交")
                    btn = gr.Button("提交")
                    
                    callback = gr.CSVLogger()
                    callback.setup([user_flag], "flagged_data_points")

                    def suggest(*args):
                        
                        if args[0] == "":
                            gr.Warning('你输入内容了吗')
                            
                        else:                            
                            gr.Info("成功提交")
                            return callback.flag(list(args))

                    btn.click(suggest, inputs=user_flag, outputs=None)

    generate.click(inference_image_preprocess, 
                   inputs=[style_name, random_seed, seed_number, image_aspect_ratio, user_prompt, 
                           controlnet_image_name, controlnet_strength, controlnet_start, controlnet_end,],
                   outputs=image_show,
                   concurrency_limit=2
                   )
    
# Example
    def select_image_by_description(image_show, image_aspect_ratio, seed_number, user_image, user_prompt, description):
        for index, (image_path, desc) in enumerate(images):
            if desc == description:
                return image_show, image_aspect_ratio, gr.update(value=seed_number, visible=True), gr.update(value=False), user_image, user_prompt, gr.update(selected_index=index)
            
    examples = [
        ["./examples/1.webp", "16:9", 20000816, "./examples/1.jpg", "simple background, yellow car", "马克笔手绘",],
        ["./examples/3.png", "16:9", 357378276, "./examples/2.png", "the interior of a car, sunshine, The car has a black leather steering wheel, The dashboard has a large touch screen display, The seats are upholstered in white leather and there are two side mirrors on either side of the steering wheel. The windows are tinted and provide a view of the outside, mountains out of windows, white seats", "真实内饰",],
    ]
    gr.Examples(label="样图", examples=examples, fn=select_image_by_description,
                inputs=[image_show, image_aspect_ratio, seed_number, user_image, user_prompt,
                        gr.Textbox(visible=False, label="风格预设")],
                outputs=[image_show, image_aspect_ratio, seed_number, random_seed, user_image, user_prompt, style_pics],
                run_on_click=True,
                )

demo.launch(server_name="0.0.0.0",share=False, server_port=args.port, max_file_size="5mb",
            ssl_keyfile="./mydomain.key", ssl_certfile="./mydomain.crt", ssl_verify=False,
            show_api=False)

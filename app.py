import random
import argparse

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

    address = f"127.0.0.1:{args.comfy_port}"


# 对进行推理的 gradio 界面的参数进行预处理返回image
def inference_image_preprocess(style_name, random_seed: bool, seed_number, image_aspect_ratio, user_prompt, 
                               cn_img_name, strength, start, end):
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
        width = 1456
        heigh = 816
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


with gr.Blocks() as demo:
    with gr.Row(equal_height=False):
        with gr.Column(scale=2, ):
            image_show = gr.Image(height=500, show_label=False, interactive=False)
            gr.Markdown("### ⚙️ 基础设置")
            with gr.Row(equal_height=False):
                with gr.Column(scale=1, min_width=300):
                    with gr.Column():
                        image_aspect_ratio = gr.Radio(value='1:1', label="✅ 图片比例", choices=['1:1', '16:9', '18:9'],
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
                # comfy_server_address = gr.Textbox(value=address, visible=False)
                
        with gr.Column(scale=1,):
                # Controlnet
                with gr.Tab("🔧ControlNet", visible=True):

                    # from comfyui.upload_image import upload_image

                    user_image = gr.Image(height=360, type="pil", label="Controlnet图片", sources=('upload', 'clipboard'))
                    controlnet_image_name = gr.Textbox(visible=True)

                    from modules.upload_image import upload_image
                    user_image.upload(lambda img: upload_image(img, address), user_image, outputs=controlnet_image_name)
                    user_image.clear(fn=lambda: "", outputs=controlnet_image_name)
                    
                    
                    # controlnetimagename = user_image.change(lambda img: upload_image(img, address), user_image, outputs=[controlnet_image_name])

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

                with gr.Tab("🎨Style"):
                    images = [
                        ("./style_pics/00131-1676567236.png", "经典渲染"),
                        ("./style_pics/00213-636703613.png", "绚丽鲜橙"),
                        ("./style_pics/00021-1676567236.png", "真实照片"),
                        ("./style_pics/00052-1493661434.png", "马克笔手绘"),
                        ("./style_pics/20240821_090405.png", "真实内饰"),
                    ]

                    images_labels = ["无"] + [lable for _, lable in images]

                    def display_gallery():
                        return images

                    gr.Gallery(value=display_gallery, object_fit="contain", show_download_button=False, 
                            label="风格展示", interactive=False, format="png", allow_preview=False)
                    style_name = gr.Radio(value="无", choices=images_labels, label="风格选择", interactive=True)

    generate.click(inference_image_preprocess, 
                   inputs=[
                       style_name, random_seed, seed_number, image_aspect_ratio, user_prompt, 
                       controlnet_image_name, controlnet_strength, controlnet_start, controlnet_end],
                   outputs=image_show)

demo.launch(share=False, server_port=args.port, max_file_size="5mb")

import gradio as gr

def greet(name, is_shouting):
    greeting = f"Hello, {name}!"
    if is_shouting:
        greeting = greeting.upper()
    return greeting

def count_chars(name):
    return f"Your name has {len(name)} characters."

with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Enter your name")
    shouting_checkbox = gr.Checkbox(label="Shout?")
    greet_button = gr.Button("Greet")
    output = gr.Textbox(label="Greeting")
    char_count = gr.Textbox(label="Character Count")

    greet_button.click(
        fn=greet,
        inputs=[name_input, shouting_checkbox],
        outputs=output,
        api_name="greet"
    )

    name_input.change(
        fn=count_chars,
        inputs=name_input,
        outputs=char_count
    )

# 启动 Gradio 应用
demo.launch()

# 像函数一样使用 Gradio Blocks 应用
result = demo("Alice", True, api_name="greet")
print("Greeting result:", result)

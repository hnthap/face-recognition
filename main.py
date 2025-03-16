import gradio as gr

from haarcascade import detect_faces_haarcascade


with gr.Blocks(css='''
h1 {
    text-align: center;
}
.my-group {
    max-width: 600px !important;
    max-height: 600px !important;
}
.my-column {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}
''') as demo:
    gr.Markdown('# Real-Time Face Recognition')
    with gr.Column(elem_classes=['my-column']):
        with gr.Group(elem_classes=['my-group']):
            image = gr.Image(
                sources=['webcam'],
                type='numpy',
                image_mode='RGB',
                label='Stream',
                show_label=False,
            )
            with gr.Column(variant='compact'):
                gr.Markdown('**OpenCV Frontal Face Haar Cascade**')
                with gr.Row(variant='compact'):
                    scale_factor = gr.Slider(
                        1.0, 5.0, 1.8, step=0.05, label='Scale Factor',
                        visible=True, 
                    )
                    min_neighbors = gr.Slider(
                        1, 10, 5, step=1, label='Min Neighbors', visible=True,
                    )
                    min_size = gr.Slider(
                        50, 200, 100, step=10, label='Min Size', visible=True,
                    )
            image.stream(
                detect_faces_haarcascade, 
                [image, scale_factor, min_neighbors, min_size],
                [image], 
                time_limit=30, 
                stream_every=0.2, 
                concurrency_limit=5,
            )


if __name__ == '__main__':
    demo.launch(node_port=7860)

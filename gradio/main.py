
import cv2
import gradio as gr
import numpy as np


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml',
)


def detect_faces_haarcascade(image: np.ndarray, scale_factor, min_neighbors, min_size):
    image = cv2.resize(image, (image.shape[1] * 500 // image.shape[0], 500))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(min_size, min_size),
    )
    for (x, y, w, h) in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image


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

# Real-Time Face Recognition

![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
![OpenCV](https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat-square&logo=OpenCV&logoColor=white)
![Gradio](https://img.shields.io/badge/-Gradio-orange?style=flat-square&logo=gradio&logoColor=white)
![Python 3.11.7](https://img.shields.io/badge/-Python%203.11.7-3776AB?style=flat-square&logo=python&logoColor=white)

![Screenshot](image.png)

## Requirements

Docker is required.

## Installation

### Build from source

```bash
# May take a few minutes to install the dependencies
docker build -t face-recognition .
```

## Usage

```bash
# Start the container
docker run -p -d 7860:7860 face-recognition
```

After starting the container, go to <http://localhost:7860>.

```bash
# Stop the container
docker stop -v face-recognition
```

## To-Dos

* [x] Use OpenCV Haar Cascade
* [x] Use Gradio
* [ ] Isolate frontend and backend into different images
* [ ] Try other face recognition techniques (e.g., DeepFace)
* [ ] Make a Live Demo for this

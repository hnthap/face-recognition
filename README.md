# Real-Time Face Recognition

![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
![OpenCV](https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat-square&logo=OpenCV&logoColor=white)
![Gradio](https://img.shields.io/badge/-Gradio-orange?style=flat-square&logo=gradio&logoColor=white)
![Python 3.11](https://img.shields.io/badge/-Python%203.11-3776AB?style=flat-square&logo=python&logoColor=white)

![Screenshot](image.png)

## Requirements

Docker (Docker Compose) is required.

## Installation

You can pull the image from Docker Hub:

```bash
docker-compose pull
```

Or, you can build the image from source by yourself, but it may take a few minutes to download and install the dependencies:

```bash
docker-compose build
```

## Usage

Start the containers:

```bash
docker-compose up -d
```

Then, go to <http://localhost:7860>.

To stop the containers, run:

```bash
docker-compose down -v
```

## To-Dos

* [x] Use OpenCV Haar Cascade
* [x] Use Gradio
* [ ] Isolate frontend and backend into different images
* [ ] Try other face recognition techniques (e.g., DeepFace)
* [ ] Make a Live Demo

# Real-Time Face Recognition

<div align="center">

  [![Stars](https://img.shields.io/github/stars/hnthap/face-recognition?color=yellow&style=flat&label=%E2%AD%90%20stars)](https://github.com/hnthap/face-recognition/stargazers)
  [![Pulls](https://img.shields.io/docker/pulls/joseph40/face-recognition-gradio?logo=docker)](https://hub.docker.com/r/joseph40/face-recognition-gradio)
  [![License](http://img.shields.io/:license-MIT-green.svg?style=flat)](LICENSE)
  
  <img alt="Screenshot" src="image.png" height="360px" />

</div>

## Requirements

<div align="center">

  ![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
  ![OpenCV](https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat-square&logo=OpenCV&logoColor=white)
  ![Gradio](https://img.shields.io/badge/-Gradio-orange?style=flat-square&logo=gradio&logoColor=white)

</div>

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
* [ ] Try other face recognition techniques (e.g., [deepface](https://github.com/serengil/deepface))
* [ ] Make a Live Demo

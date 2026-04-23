# AI/ML Engineering Assessment – Vision & Deployment

## 📌 Overview

This project implements a multi-stage AI/ML pipeline as part of a technical assessment. It demonstrates:

* REST API development using FastAPI
* AI-based image background removal
* Docker-based deployment with GPU support
* Multi-model orchestration using a vision model (Ollama)

---

# 🧩 Project Structure

```
ai-ml-assessment/
│
├── task1/   # Basic FastAPI background removal API
├── task2/   # Dockerized GPU-enabled API
├── task3/   # Vision + Background Removal pipeline
│
├── README.md
```

---

# ✅ Task 1 – Background Removal API

## 🔹 Description

A FastAPI-based REST API that removes the background from an uploaded image using the **rembg** library.

## 🔹 Features

* Endpoint: `POST /remove-bg`
* Accepts image file upload
* Returns transparent PNG
* Efficient processing with model loaded once

## 🔹 Tech Stack

* FastAPI
* rembg (U2Net model)
* Pillow

## 🔹 Run Instructions

```bash
cd task1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🔹 Test

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Task 2 – Dockerized GPU API

## 🔹 Description

A containerized version of the background removal API designed to run on **NVIDIA GPU using CUDA**.

## 🔹 Features

* GPU-ready Docker environment
* Model loaded at container startup
* Same `/remove-bg` endpoint
* Production-style deployment

## 🔹 Tech Stack

* FastAPI
* Docker
* NVIDIA CUDA
* PyTorch base image

## 🔹 Dockerfile Highlights

* Uses `pytorch/pytorch` CUDA runtime
* Installs dependencies inside container
* Runs API via Uvicorn

## 🔹 Build & Run

```bash
cd task2
docker build -t bg-removal-app .
```

### ▶️ Run with GPU

```bash
docker run --gpus all -p 8000:8000 bg-removal-app
```

### ▶️ Run without GPU (CPU fallback)

```bash
docker run -p 8000:8000 bg-removal-app
```

## 🔹 Note on GPU Usage

This project is configured for GPU acceleration using CUDA.
Since a GPU was not available locally, the application was tested on CPU.
However, the Docker setup is fully compatible with GPU-enabled systems.

---

# 🧠 Task 3 – Image Processing Pipeline

## 🔹 Description

An advanced API that:

1. Generates an image caption using a vision model via Ollama
2. Removes background using rembg
3. Returns both results in a single response

## 🔹 Features

* Endpoint: `POST /process`
* Async processing for performance
* Multi-model pipeline
* Base64 encoded output image

## 🔹 Tech Stack

* FastAPI
* Ollama (moondream vision model)
* rembg (CPU)
* asyncio

---

## 🔹 Setup Ollama

Install: Ollama

Run model:

```bash
ollama pull moondream
ollama run moondream
```

---

## 🔹 Run API

```bash
cd task3
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🔹 Test Endpoint

Open:

```
http://127.0.0.1:8000/docs
```

Use:

```
POST /process
```

---

## 🔹 Sample Output

```json
{
  "description": "A person standing outdoors with trees in the background.",
  "image": "base64_encoded_string"
}
```

---




---

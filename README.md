# Smoker Classifier

Smoking persons classification using pretrained ResNet50

By team 8:
* Svetlana Lukina
* Lyudmila Zavadskaya
* Pavel Gurevich
* Nikita Vybornov


## Overview
This project uses a pretrained ResNet model to classify images of smokers. 

From images to probabilities of smoking persons:

* prob: 0.02

  <img width="252" alt="image" src="https://github.com/user-attachments/assets/aa629c36-15bf-42b2-94c2-10b7ff25bff3">

* prob: 0.78

  <img width="247" alt="image" src="https://github.com/user-attachments/assets/13b5c12e-bed4-4863-a5f0-1a143e290f17">
  

## Requirements
- Python 3.9
- torch
- torchvision
- Pillow

## Setup Instruction

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Owling797/FSE_final_project.git
   git checkout main
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd FSE_final_project
   ```

3. **Place your images into some directory:**

### Setup using Docker 

4. **Build the Docker Image:**
   ```bash
   docker build -t clasdss .
   ```
   <img width="862" alt="image" src="https://github.com/user-attachments/assets/ec5d2bd2-0af7-4e66-a9fe-e3ce96ba4398">


5. **Run the Docker Container:**

   First:
   * Find the path to your image (you can find some examples in the "image" directory)
   * Decide where to place the converted image
   * Decide where to place json result
   
   All your paths must be relative to directory "entrypoint"

   
   ```bash
   docker run -t -v <Your full path to FSE_final_project>/FSE_final_project/out/:/app/out/ clasdss input=<path to your image> output=<path to converted image> input_dir=<path to stored converted images directory> result_file=<path to json result>
   ```
   ![alt text](screenshots/image-build.png)


6. **Check the result**
   ```bash
   cat <path to your json result>
   ```
   ![alt text](screenshots/image-cat.jpg)

   The entire process:
   ![alt text](screenshots/image-all.jpg)



### Setup using Makefiles

If you're using Ubuntu, you're able to build and run this project without Docker. Here is the instruction how to do it

4. **Build the project**
   ```bash
   make prereqs
   make build
   make test
   ```

5. **Run the software**

   First:
   * Find the path to your image (you can find some examples in the "image" directory)
   * Decide where to place the converted image
   * Decide where to place json result
   
   All your paths must be relative to directory "entrypoint"

   
   ```bash
   make all input=<path to your image> output=<path to converted image> input_dir=<path to stored converted images> result_file=<path to json result>
   ```

6. **Check the result**
   ```bash
   cat <path to your json result>
   ```


## Auxilary options

1. **To Prerocess data:**

All paths must be relative to directory entrypoint
   ```bash
   make preprocessing input=<path to your image> output=<path to the result>
   ```
   or outside the container:
   ```bash
   docker run -it clasdss preprocessing input=<path to your image> output=<path to the result>
   ``` 
   ![alt text](screenshots/image-2.png)


2. **To Process data:**
   ```bash
   make processing input_dir<path to stored converted images>
   ```
   or outside the container:
   ```bash
   docker run -it clasdss processing input_dir<path to stored converted images>
   ``` 
   ![alt text](screenshots/image-3.png)

   Runs the neural network model on the images.

3. **To Postprocess data:**
   ```bash
   make postprocessing result_file=<path to json result>
   ```
   or outside the container:
   ```bash
   docker run -it clasdss postprocessing result_file=<path to json result>
   ```
   ![alt text](screenshots/image-4.png)
   
  Analyzes the output from the neural network 

4. **Run tests**:
   ```bash
   python -m unittest test_main_model.py
   ```
   ![alt text](screenshots/image-1.png)
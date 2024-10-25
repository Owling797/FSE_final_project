# Prject Smoker Classifier

# Smoking persons classification using pretrained ResNet50

## Overview
This project uses a pretrained ResNet model to classify images of smokers. 


Team 8:
* Svetlana Lukina
* Lyudmila Zavadskaya
* Pavel Gurevich
* Nikita Vybornov
  

## Requirements
- Python 3.9
- torch
- torchvision
- Pillow

## Setup Instruction

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Owling797/FSE_final_project.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd FSE_final_project
   ```

3. **Build the Docker Image:**
   ```bash
   docker build -t clasdss .
   ```

4. **Run the Docker Container:**
   ```bash
   docker run -it clasdss
   ```

5. **To Prerocess data:**
   ```bash
   make Preprocessing
   ```

6. **To Process data:**
   ```bash
   make Processing
   ```
   Runs the neural network model on the images.

7. **To Postprocess data:**
   ```bash
   make Postprocessing
   ```
  Analyzes the output from the neural network 

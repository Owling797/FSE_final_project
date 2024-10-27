PYTHON=python3
PIP=$(PYTHON) -m pip
VENV=my-venv
REQUIREMENTS=requirements.txt




CXX = g++
CXXFLAGS = -std=c++11 -I./libs/CImg-master -lm -Wall

prereqs:
	@echo "Installing system dependencies..."
	sudo apt-get update && apt-get install -y python3 python3-pip python3-venv
	#

	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)

	@echo "Installing Python packages from $(REQUIREMENTS)..."
	. $(VENV)/bin/activate; pip install --no-cache-dir -Ur $(REQUIREMENTS)



	# @if [ ! -d $(OPENCV_DIR) ]; then \
    #             echo "Cloning OpenCV repository..."; \
    #             git clone https://github.com/opencv/opencv.git; \
    #     else \
    #             echo "OpenCV repository already exists."; \
    #     fi
	# @if [ ! -d $(OPENCV_CONTRIB_DIR) ]; then \
	# 		echo "Cloning OpenCV contrib repository..."; \
	# 		git clone https://github.com/opencv/opencv_contrib.git; \
	# else \
	# 		echo "OpenCV contrib repository already exists."; \
	# fi



build:
	@echo "Current directory is: $(shell pwd)"
	@ls -l
	$(CXX) -o image_converter ./src/image_converter.cpp $(CXXFLAGS)


test: #pavel need to make this


clean:
	@echo "Cleaning up..."
	rm -f $(TARGET)
	rm -rf $(BUILD_DIR)
	rm -rf $(OPENCV_DIR)
	rm -rf $(OPENCV_CONTRIB_DIR)
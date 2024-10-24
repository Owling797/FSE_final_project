PYTHON=python3
PIP=$(PYTHON) -m pip
VENV=my-venv
REQUIREMENTS=requirements.txt



OPENCV_DIR=opencv
OPENCV_CONTRIB_DIR=opencv_contrib
BUILD_DIR=build
CXX=g++
CXXFLAGS=`pkg-config --cflags opencv4`
LDFLAGS=`pkg-config --libs opencv4`
TARGET=image_converter
SRC=image_converter.cpp

prereqs:
	@echo "Installing system dependencies..."
	apt-get update && apt-get install -y python3 python3-pip python3-venv

	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)

	@echo "Installing Python packages from $(REQUIREMENTS)..."
	$(VENV)/bin/$(PIP) install --no-cache-dir -r $(REQUIREMENTS)



	@if [ ! -d $(OPENCV_DIR) ]; then \
                echo "Cloning OpenCV repository..."; \
                git clone https://github.com/opencv/opencv.git; \
        else \
                echo "OpenCV repository already exists."; \
        fi
	@if [ ! -d $(OPENCV_CONTRIB_DIR) ]; then \
			echo "Cloning OpenCV contrib repository..."; \
			git clone https://github.com/opencv/opencv_contrib.git; \
	else \
			echo "OpenCV contrib repository already exists."; \
	fi




build:
	@echo "Building OpenCV..."
	@if [ ! -d $(BUILD_DIR) ]; then \
			mkdir $(BUILD_DIR); \
	fi
	cd $(BUILD_DIR) && cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../$(OPENCV_CONTRIB_DIR)/modules ../$(OPENCV_DIR) && \
	make -j$(nproc) && \
	sudo make install


	$(TARGET): $(SRC)
			@echo "Building the C++ image converter..."
			$(CXX) -o $(TARGET) $(SRC) $(CXXFLAGS) $(LDFLAGS)


test: #pavel need to make this


clean:
	@echo "Cleaning up..."
	rm -f $(TARGET)
	rm -rf $(BUILD_DIR)
	rm -rf $(OPENCV_DIR)
	rm -rf $(OPENCV_CONTRIB_DIR)
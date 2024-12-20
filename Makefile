PYTHON=python3
PIP=$(PYTHON) -m pip
VENV=my-venv
REQUIREMENTS=requirements.txt


prereqs:
	@echo "Installing system dependencies..."
	apt-get update && apt-get install -y python3 python3-pip python3-venv golang-go


	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)


	ls -l $(VENV)
	chmod +x $(VENV)/bin/activate
	ls -l $(VENV)

	@echo "Installing Python packages from $(REQUIREMENTS)..."
	. $(VENV)/bin/activate; pip install --no-cache-dir -Ur $(REQUIREMENTS)




build:
	go build -o image_converter src/image_converter.go
	go build -o pkl_converter src/pkl_converter.go



test: #pavel need to make this
	@echo testing image converter
	./image_converter test.png test.jpg
	. $(VENV)/bin/activate; python3 -m test_preproc
	@echo testing model
	. $(VENV)/bin/activate; python3 -m unittest test_main_model.py
	@echo testing postprocessing
	cd ./src && . ../$(VENV)/bin/activate; python3 -m unittest test_decoder && cd ..

clean:
	@echo "Cleaning up..."
	rm -f $(TARGET)
	rm -rf $(BUILD_DIR)
	rm -rf $(OPENCV_DIR)
	rm -rf $(OPENCV_CONTRIB_DIR)
IMG_CONV_EXE=../image_converter
PKL_CONV_EXE=../pkl_converter
MODEL=../model.py
PYTHON=python3
MODEL_OUT=../out/out.pkl
VENV=my-venv

all: preprocessing processing postprocessing

preprocessing:
	@echo "Running the image converter..."
		@if [ -z "$(input)" ] || [ -z "$(output)" ]; then \
				echo "Error: 'input' and 'output' variables are required."; \
				echo "Usage: make preprocessing input=<.png or .jpg or .gif> output=<.jpg>"; \
				echo "By default dir is '/app/entrypoint' !"; \
				exit 1; \
		else \
				echo "Using input: $(input)"; \
				echo "Using output: $(output)"; \
				./$(IMG_CONV_EXE) $(input) $(output); \
				ls -l $(output); \
        fi



processing:
	 @echo "Running processing"
		@if [ -z "$(input_dir)" ]; then \
				echo "Error: 'input' variable is required."; \
				echo "Usage: make processing input=<.jpg> output=<.pkl>"; \
				echo "By default dir is '/app/entrypoint' !"; \
				exit 1; \
		else \
				echo "Using input: $(input_dir)"; \
				echo "Using output: $(MODEL_OUT)"; \
				mkdir -p ../out; \
				. ../$(VENV)/bin/activate; $(PYTHON) $(MODEL) $(input_dir) $(MODEL_OUT) ../ft_resnet_10e.pt; \
        fi
  



postprocessing:
	@echo "Running the output converter..."
		@if [ -z "$(MODEL_OUT)" ] || [ -z "$(result_file)" ]; then \
				echo "Error: 'input' and 'output' variables are required."; \
				echo "Usage: make postprocessing input=<.pkl> output=<.json>" ; \
				echo "By default dir is '/app/entrypoint' !"; \
				exit 1; \
		else \
				echo "Using input: $(MODEL_OUT)"; \
				echo "Using output: $(result_file)"; \
				. ../$(VENV)/bin/activate; python3 ../src/decoder.py $(MODEL_OUT) $(result_file); \
				./$(PKL_CONV_EXE) $(result_file) ; \
        fi


help:
	@echo "help"
	@echo "bash"
	@echo "preprocessing input=<.png or .jpg or .gif> output=<.jpg>"
	@echo "processing input=<.jpg> output=<.pkl>"
	@echo "postprocessing input=<.pkl> output=<.json>"

bash:
	@/bin/bash

clean:

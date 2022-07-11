setup: requirements.txt
	python3 -m venv venv
	. ./venv/bin/activate; \
	pip install -r ./requirements.txt
run: venv/bin/activate
	python3 main.py $(ARGS)
build: venv/bin/activate
	pyinstaller main.py --clean -F --add-data '.env:.' --add-data 'graphql/:./graphql/'
clean:
	find . -type d -name __pycache__  -prune -exec rm -rf {} \;
	rm -rf build dist main.spec
reset:
	rm -rf venv
	$(MAKE) clean

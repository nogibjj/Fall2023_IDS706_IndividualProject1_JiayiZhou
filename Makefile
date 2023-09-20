install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval mylib/*.ipynb
	python -m pytest -vv --cov=mylib.lib

format:	
	black mylib/*.py
	nbqa black mylib/*.ipynb 

lint:
	nbqa ruff mylib/*.ipynb
	ruff check mylib/*.py
		
all: install lint test format

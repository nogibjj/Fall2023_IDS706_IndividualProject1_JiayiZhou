install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval mylib/*.ipynb
	python -m pytest -vv --cov=mylib.lib --cov=mylib.script

format:	
	black mylib/*.py
	nbqa black mylib/*.ipynb 

lint:
	nbqa ruff mylib/*.ipynb
	ruff check mylib/*.py
		
all: install lint test format

generate_and_push:
	# Create the markdown file (assuming it's generated from the plot)
	python mylib/script.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

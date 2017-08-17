clean:
	find . -name "*.py" -exec autopep8 -i "{}" ";"
	find . -name "*.pyc" -delete

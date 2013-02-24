clean:
	@find . -name "*.pyc" -delete
	
run: clean
	@python headball.py
	
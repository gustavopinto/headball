clean:
	@find . -name "*.pyc" -delete
	@find . -name "*~" -delete

	
run: clean
	@python headball.py
	
install :
	pip install -r requirements.txt

test:
	pytest -vv test_fibn.py
	pytest -vv test_class_fibn.py
	pytest -vv test_fibparam.py

lint:
	pylint fibn.py

format:
	black fibn.py
  
setup:
	# Create python virtualenv & source
	python3 -m venv ~/.haensel-ams &&\
			source ~\.haensel-ams\bin\activate

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
			pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

#Testing will be done later
#test:
	# Additional, optional, tests could go here
	#python -m pytest test/pytest.py

all: install
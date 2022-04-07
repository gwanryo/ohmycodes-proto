run:
	sudo docker run -d -p 0.0.0.0:5000:5000/tcp --name ohmycodes ohmycodes:latest

build:
	sudo docker build -t ohmycodes:latest .

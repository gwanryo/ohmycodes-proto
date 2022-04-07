run:
	-sudo docker kill ohmycodes
	-sudo docker rm ohmycodes
	sudo docker run -d -p 127.0.0.1:5000:5000/tcp --name ohmycodes ohmycodes:latest

build:
	sudo docker build -t ohmycodes:latest .

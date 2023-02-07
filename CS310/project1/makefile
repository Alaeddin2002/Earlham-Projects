CXX=gcc -Wall -Werror -std=c99

all: image imagestack

image: image.c
	$(CXX) image.c -o image

imagestack: imagestack.c
	$(CXX) imagestack.c -o imagestack

clean: 
	rm -f image imagestack

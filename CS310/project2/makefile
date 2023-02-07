CXX=gcc -Wall -Werror -std=c99 -lm

all: detective demo

demo: mysterysorts.o mysterysorts.h demo.c
	$(CXX) demo.c mysterysorts.o -o demo

detective: mysterysorts.o mysterysorts.h detective.c
	$(CXX) detective.c mysterysorts.o -o detective

clean:
	rm -f detective demo

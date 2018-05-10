all: test
test: pytest.o
	gcc -L/usr/lib/python3.5/config-3.5m-arm-linux-gnueabihf/ -lpython3.5 -ldl pytest.o -o test
pytest.o: pytest.c
	gcc -g -std=gnu99 -Wall -c  pytest.c -I/usr/include/python3.5/
clean:
	@rm -rf *.o *.pyc test
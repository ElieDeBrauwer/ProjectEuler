problem0001: problem0001.o
	ld -o $@  $^

problem0001.o: problem0001.s
	as -o $@ -g $^ 

clean:
	rm -f problem0001.o
	rm -f problem0001
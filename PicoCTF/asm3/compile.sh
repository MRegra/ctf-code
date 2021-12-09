
gcc -masm=intel -m32 -c test.S -o test.o
gcc -m32 -c solve.c -o solve.o
gcc -m32 test.o solve.o -o solve
./solve

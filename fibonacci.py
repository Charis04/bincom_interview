"""
9. Write a program to sum the first 50 fibonacci sequence.
"""

def fib_sum(n):
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print(sum(fib))

if __name__ == "__main__":
    fib_sum(50)

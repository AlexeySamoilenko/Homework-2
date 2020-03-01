from concurrent.futures import ProcessPoolExecutor, as_completed


def function(arg, a):
    for _ in range(arg):
        a += 1
    return a


def main():
    a = 0
    with ProcessPoolExecutor(max_workers=5) as executor:
        future_a = [
            executor.submit(function, 1000000, a) for i in range(5)
        ]
        for i in as_completed(future_a):
            a += i.result()

    print("----------------------", a)  # ???


main()

''' with args=(10000000,) avr for 5 time
    without lock      5.983 seconds
    with lock         6.895 seconds
    with Rlock        6.068 seconds
    without for: a+=1 0.018 seconds
    without threads   4.310 seconds'''

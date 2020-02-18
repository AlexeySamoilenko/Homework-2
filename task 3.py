from concurrent.futures import ProcessPoolExecutor as PoolExecutor


def function(arg):
    a = 0
    for _ in range(arg):
       a += 1
    return a
    
def main():
    a = 0
    threads = []
    with PoolExecutor(max_workers=5) as executor:
        #for _ in executor.map(function(1000000,),range(5)):
        for _ in range(5):
            a += function(1000000,)
        
    #[t.join() for t in threads]
    print("----------------------", a) # ???


main()

''' with args=(10000000,) avr for 5 time
    withPoolExecutor  4.031 seconds
    without lock      5.983 seconds
    with lock         6.895 seconds
    with Rlock        6.068 seconds
    without for: a+=1 0.018 seconds
    without threads   4.310 seconds'''


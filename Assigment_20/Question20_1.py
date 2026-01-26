import threading

def Even():   
 
    for i in range(0,20,2):
        print(i)

def Odd(): 

   
    for i in range(1,20,2):
        print(i)


def main():
    print("Even") 

    t1 = threading.Thread(target=Even)   
    t1.start()
    print("Odd") 

    t2 = threading.Thread(target=Odd)   
    t2.start()

    t1.join()
    t2.join()

  

if __name__ == "__main__":
    main()
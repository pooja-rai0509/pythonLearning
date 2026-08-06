import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

# create threads
orderthread = threading.Thread(target=take_orders)
brewthread = threading.Thread(target=brew_chai)

orderthread.start()
brewthread.start()

# wait for both to finish
orderthread.join()
brewthread.join()

print('A orders taken & chai brewed')
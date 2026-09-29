import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
#asyncio → asynchronous programming/event loop
#time → we're using time.sleep()
#ThreadPoolExecutor → creates/manages worker threads

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)   #Blocking operation
    return f"{item} stock: 42"

#main() is a coroutine.
#It doesn't immediately execute when you call it. asyncio.run() will execute it.
async def main():
    loop = asyncio.get_running_loop()   #This gets the currently running asyncio event loop.
    with ThreadPoolExecutor() as pool:  #This creates a pool of worker threads.The with block also ensures the executor is properly shut down afterward.
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")   #run_in_executor() moves that blocking function to a separate thread, so it doesn't block the asyncio event loop.
        print(result)

asyncio.run(main())
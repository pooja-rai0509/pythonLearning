import asyncio
import threading
import time

def bg_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health")

async def fetch_order():
    await asyncio.sleep(3)
    print(f"Order fetched")

threading.Thread(target=bg_worker, daemon=True).start()

asyncio.run(fetch_order())
import asyncio
import time

async def brew(name):
    print(f"Brewing {name}...")
    #await asyncio.sleep(3)     # does all in once, don't block the others call
    time.sleep(3)   # does 1 by 1 completion
    print(f"{name} is ready.")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai")
    )

asyncio.run(main())
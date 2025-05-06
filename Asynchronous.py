
import asyncio
#pomt here is that you can pause taks to let other tasks run

async def say_hello():
    print("Hello")
    await asyncio.sleep(5)
    print("World")

def main():
       return say_hello()
    
main()
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(2)  # Simulating being blocked and yeilding control
    print("World!")

async def say_goodbye():
    print("Goodbye!")
    await asyncio.sleep(1)
    print("for now!")

# Running the async function
async def main1():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_goodbye())

    await task1
    await task2

#########################################################################
import random

async def download_data(n):
    print(f"Downloading data {n}...")
    await asyncio.sleep(random.randint(1,5))  # Simulate different download times
    print(f"Download {n} complete")
    return f"Data {n}"

async def main2():
    results = await asyncio.gather(download_data(2), download_data(3), download_data(1))
    print("All downloads finished:", results)

#########################################################################
async def unreliable_task(n):
    await asyncio.sleep(n)
    if n == 3:
        raise RuntimeError("Random failure!")
    return f"Task {n} completed"

async def main3():
    tasks = [unreliable_task(n) for n in range(1, 5)]

    print("Starting tasks...")
    try:
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=4)
        print("All tasks finished:", results)
    except asyncio.TimeoutError:
        print("Some tasks took too long!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Cleaning up...")

#########################################################################
import aiohttp

async def fetch_data(session, url):
    """Fetch data asynchronously from a given URL."""
    try:
        async with session.get(url) as response:
            data = await response.json()
            return data  # Assuming the API returns JSON
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def main4():
    """Fetch data from multiple APIs concurrently."""
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for i, result in enumerate(results, 1):
        if result:
            print(f"Data from API {i}: {result}")

#########################################################################
# Run the async event loop
            
# asyncio.run(main1())
print("main1 finished")

# asyncio.run(main2())
print("main2 finished")

# asyncio.run(main3())
print("main3 finished")

asyncio.run(main4())
print("main4 finished")

import os
import pandas as pd
import requests

curr_dir = os.getcwd()
print(curr_dir)

todo = 1

url = f"https://jsonplaceholder.typicode.com/todos/{todo}"

response = requests.get(url)
data = response.json()

print(data)
import requests
import time

'''
your localhost url. If running on port 5000
'''
url = "http://localhost:5000/process"
# Path to image file
filess = {"img": open("../img.jpg", "rb")}
starttime = time.time()
results = requests.post(url, files=filess)
print("time taken:", time.time() - starttime)
print(results.text)

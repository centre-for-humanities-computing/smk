import pandas as pd
import os
import concurrent.futures
from threading import Lock

lock = Lock()
THREADS = 10

# import a CSV into Pyhton with Panda
data_url = "sub_smk.csv"
df1 = pd.read_csv(data_url)

dfList = df1['medium_image_url'].tolist()
print("size", len(dfList))
print(dfList[1])
print(type(dfList[1])) 


# method for downloading by a wget-call
def download(url,name):
    cmd = "wget --output-document=images/"+name+".jpg " + url #{url}"#.format(url=url)
    #with lock:
    print("command: \n")
    print(cmd)
    os.system(cmd)

### Running through it as a list: 
count_lines = 0
for x in dfList:
    if isinstance(x, str):
        image_url = x
        file_name = "image"+str(count_lines)
        download(str(image_url), str(file_name))
        print("count ", count_lines)
    count_lines += 1

'''
# Threaded method
def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=THREADS) as ex:
        count_lines = 0
        for x in dfList:
            #print(row['medium_image_url'])
            image_url = x
            file_name = "image"+str(count_lines)
            ex.submit(download, image_url, file_name)
            print("count ", count_lines)
            count_lines += 1

          

def download(url,name):
    #cmd = "wget -q {url}".format(url=url)
    #print(file_name)
    cmd = "wget --output-document=images/"+name+".jpg " + url #{url}"#.format(url=url)
    with lock:
        print("command: \n")
        print(cmd)
    os.system(cmd)


##########


if __name__ == "__main__":
    main()
'''

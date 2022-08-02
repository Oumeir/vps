
from urlextract import URLExtract
extractor = URLExtract()



import os
all_urls=[]
for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
        data = str(f.readlines())
        urls = extractor.find_urls(data)
        all_urls += urls


        


for s in set(all_urls):
    if 'https' in s :
        l =s.split('https://')[1].replace('/','').replace('www.','')
    elif 'http' in s:
        l = s.split('http://')[1].replace('/','').replace('www.','')

    print(l)
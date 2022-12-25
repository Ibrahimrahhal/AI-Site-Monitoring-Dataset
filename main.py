from browser import controller
from time import sleep
import logging
from multiprocessing import Pool
from os.path import exists

file = open("10-million-site.csv")

traversed = 0
starting_point = 100

def traverse_url(url):
    if(exists('./dataset/non-broken/site' + str(url['traversed']) + '.png')):
        print("Skipping: " + url['url'])
        return
    temp_browser = controller()
    print("Starting: " + url['url'])
    temp_browser.get(url['url'])
    sleep(12)
    temp_browser.take_screenshot('./dataset/non-broken/', 'site' + str(url['traversed']))
    temp_browser.remove_styles_from_page()
    temp_browser.take_screenshot('./dataset/broken/', 'site' + str(url['traversed']))
    temp_browser.abort()
    print("Done: " + url['url'])

sites = []
for i in file:
    url = "https://{0}".format(i.split(",")[1].replace('"', ''))
    if(traversed > 10000):
        break
    if(traversed == 0 or traversed < starting_point):
        traversed=traversed+1
        continue
    traversed=traversed+1
    sites.append({"url": url, "traversed": traversed})


def pool_handler(url):
    try:
        traverse_url(url)
    except:
        pass
if __name__ == '__main__':
    with Pool(processes=10) as pool:
        result = pool.map(pool_handler, sites)


    
#! python3
# Downloads XKCD comics using mutiple threads.

import requests, os, bs4, threading, time

os.makedirs('xkcd-201-250', exist_ok=True) #store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' %(urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text,features="html.parser")

        # Find the URL of the comic imag.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src').strip("http://")
            comicUrl = "http://"+comicUrl
            if 'xkcd' not in comicUrl:
                comicUrl=comicUrl[:7]+'xkcd.com/'+comicUrl[7:]
            print ("comic url",comicUrl)

            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

startTime = time.time()
downloadXkcd(201,250)
endTime = time.time()
print('Took %s seconds to download.' % (endTime - startTime))




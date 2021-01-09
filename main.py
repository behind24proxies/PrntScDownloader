from bs4 import BeautifulSoup
import requests
import random
import string
import time
import sys
from createFolder import createFolder

def main():
    createFolder()
    while True:
        randomExtension = (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6)))
        baseUrl = "https://prnt.sc/" + randomExtension
        removedUrl = "//st.prntscr.com/2020/12/09/2233/img/0_173a7b_211be8ff.png"
        time.sleep(0.2)
        response = requests.get(baseUrl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'})
        soup = BeautifulSoup(response.text, 'lxml')
        imageSource = soup.find_all("img", id="screenshot-image")

        for img in imageSource:
            url = img['src']
            if url == removedUrl:
                print("This screenshot has been removed...")
            else:
                r = requests.head(url, allow_redirects=True)
                if r.url.split("/")[-1] == "removed.png":
                    print("This screenshot has been removed...")
                try:
                    with requests.get(url, stream=True) as r:
                        if r.status_code == 200:
                            with open("images/" + randomExtension + ".png", 'wb') as f:
                                for chunk in r.iter_content(chunk_size=8192): 
                                    f.write(chunk)
                        else:
                            print("Receiving status code: " + str(r.status_code))
                    print("Downloaded: " + url)
                except Exception as e:
                    print("Error downloading url: " + url + "\nDue to error: " + str(e))


if __name__ == "__main__":
    main()

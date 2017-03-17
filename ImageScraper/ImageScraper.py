import attr, re, os
import urllib.request
from PIL import Image
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

@attr.s
class ImageScraper(object):
    def scrape_n_image_for_phrase(self, phrase, n):
        print("Scraping {n} images from Google for phrase: \"{phrase}\"".format(n=n, phrase=phrase))
        img_urls = self.fetch_img_urls(phrase, n)

        safe_name = phrase.replace(" ", "_")
        file_path = "data/training/images/raw/{dirname}".format(dirname=safe_name)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        saved_images = []
        for i, url in enumerate(img_urls):
            img_name = url.split('/')[-1]
            full_image_path =  "{file_path}/{filename}-{i}.jpg".format(file_path=file_path, filename=safe_name, i=i)
            r = urllib.request.urlretrieve(url, full_image_path)

            saved_images.append(full_image_path)

        return saved_images

    def fetch_img_urls(self, phrase, n):
        startIndex = 0
        phrase = phrase.replace(" ", "+")
        search_url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch" % phrase
        header = {'User-Agent': 'Mozilla/5.0'}
        webpage = urlopen(Request(search_url, headers=header)).read()
        soup = self.get_soup(webpage)
        images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
        return images[:n]

    def get_soup(self,webpage):
      return BeautifulSoup(webpage, "html.parser")

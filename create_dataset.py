import argparse
from ImageScraper import ImageScraper

scraper = ImageScraper()

parser = argparse.ArgumentParser(description='Collect and curate a dataset of images.')
parser.add_argument('phrase', nargs=1)
parser.add_argument('--count', nargs=1, type=int)

args = parser.parse_args()
phrase = args.phrase[0]
count = args.count[0]

scraper.scrape_n_image_for_phrase(phrase, count)
# print(args.phrase[0])

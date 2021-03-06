import argparse
from ImageScraper import ImageScraper, ImageNormalizer

scraper = ImageScraper()
imageNorm = ImageNormalizer()

parser = argparse.ArgumentParser(description='Collect and curate a dataset of images.')
parser.add_argument('phrase', nargs=1)
parser.add_argument('--count', nargs=1, type=int)
parser.add_argument('--size', nargs=2, type=int)
parser.add_argument('--cRange', nargs=1, type=int)

args = parser.parse_args()
phrase = args.phrase[0]
width, height = args.size
count = args.count[0]
cRange = args.cRange[0]

downloaded_paths = scraper.scrape_n_image_for_phrase(phrase, count)

for path in downloaded_paths:
    print(path)
    imageNorm.standardize(path, width, height, cRange)
print("paths:", downloaded_paths)

import argparse, os, pickle
from PIL import Image
from Trainer import DataTrainer, ImageSequencer
from Stepper import Stepper


trainer = DataTrainer()
stepper = Stepper()
img_sequencer = ImageSequencer()

parser = argparse.ArgumentParser(description='Collect and curate a dataset of images.')
parser.add_argument('directory', nargs=1)
parser.add_argument('--size', nargs=2, type=int)
parser.add_argument('--norder', nargs=1, type=int)
parser.add_argument('--pickle', nargs=1, type=bool)

args = parser.parse_args()
directory = args.directory[0]
im_width, im_height = args.size
norder = args.norder[0]
try:
    should_pickle = args.pickle[0]
except:
    should_pickle = False

pickle_file_name = "{width}-{height}-{norder}.pickle".format(width=im_width, height=im_height, norder=norder)
pickled_data = {}

#  checks for and loads pickle
if should_pickle:
    print('checking for pickle..')

    has_pickle = os.path.isfile(directory + pickle_file_name)
    print(has_pickle)
    if has_pickle:
        with open(directory + pickle_file_name, 'rb') as pickle_file:
            pickled_data = pickle.load(pickle_file)

if pickled_data:
    trained_data = pickled_data
else:
    image_set = []
    for fn in os.listdir(directory):
        if fn[0] != '.' and fn[-7:] !=".pickle":
            image_set.append(directory + fn)

    concat_text = ""
    for image in image_set:
        image = Image.open(image)
        image_as_text = img_sequencer.sequence_image_to_text(image)
        concat_text = concat_text + ' ' + image_as_text

    concat_text.strip()


    trained_data = trainer.train_text_data(
            raw_text = concat_text,
            order = norder,
            )

# saves pickeled data
if should_pickle:
    with open(directory + pickle_file_name, 'wb+') as pickle_file:
        pickle.dump(trained_data, pickle_file)
        pickle_file.close()

gen_seq = stepper.new_set_length_sequence(
        model = trained_data,
        steps = im_width * im_height
        )

image = img_sequencer.convert_text_to_image(gen_seq, im_width, im_height)

image.save("data/processed/images/sample.png")
# print(gen_seq)

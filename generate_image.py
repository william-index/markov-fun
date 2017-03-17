from PIL import Image
from Trainer import DataTrainer, ImageSequencer
from Stepper import Stepper


trainer = DataTrainer()
stepper = Stepper()
img_sequencer = ImageSequencer()

image_set = []
phrase = "dia_de_los_meurtos"
for i in range(0, 20):
    image_set.append('{phrase}/{phrase}-{i}.jpg'.format(phrase=phrase, i=i))

concat_text = ""
for image in image_set:
    image = Image.open("data/training/images/cropped_and_reduced/{image}".format(image=image))
    image_as_text = img_sequencer.sequence_image_to_text(image)
    concat_text = concat_text + ' ' + image_as_text

concat_text.strip()


trained_data = trainer.train_text_data(
        raw_text = concat_text,
        order = 2,
        )

gen_seq = stepper.new_set_length_sequence(
        model = trained_data,
        steps = 100 * 100
        )

image = img_sequencer.convert_text_to_image(gen_seq, 100, 100)

image.save("data/processed/images/sample.png")
# print(gen_seq)

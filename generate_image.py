from PIL import Image
from Trainer import DataTrainer, ImageSequencer
from Stepper import Stepper


trainer = DataTrainer()
stepper = Stepper()
img_sequencer = ImageSequencer()

bauhaus_images = ['bauhaus1.png', 'bauhaus2.png', 'bauhaus3.png', 'bauhaus4.png']
concat_text = ""
for image in bauhaus_images:
    image = Image.open("data/training/images/cropped_and_reduced/{image}".format(image=image))
    image_as_text = img_sequencer.sequence_image_to_text(image)
    concat_text = concat_text + ' ' + image_as_text

concat_text.strip()


trained_data = trainer.train_text_data(
        raw_text = concat_text,
        order = 100,
        )

gen_seq = stepper.new_set_length_sequence(
        model = trained_data,
        steps = 200 * 200
        )

image = img_sequencer.convert_text_to_image(gen_seq, 200, 200)

image.save("data/processed/images/bauhaus5.png")
# print(gen_seq)

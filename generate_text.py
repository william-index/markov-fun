from PIL import Image
from Trainer import DataTrainer, ImageSequencer
from Stepper import Stepper


trainer = DataTrainer()
stepper = Stepper()

raw_file = open("data/training/wikipedia_cassettes.txt", 'r')
raw_data = raw_file.read()
raw_file.close()

x = trainer.train_text_data(
        raw_text = raw_data,
        order = 2,
        )

phrase = stepper.new_phrase(
            model = x,
            eol = 'EOL',
            punc = ['!', '.', '?'])

print(phrase)

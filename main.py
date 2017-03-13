from Trainer import DataTrainer
from Stepper import Stepper

trainer = DataTrainer()
stepper = Stepper()

x = trainer.train_text_data(
        filename = "data/training/wikipedia_cassettes.txt",
        order = 2
        )

phrase = stepper.new_phrase(
            model = x,
            eol = 'EOL',
            punc = ['!', '.', '?'])

print(phrase)

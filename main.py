from Trainer import DataTrainer

trainer = DataTrainer()

x = trainer.train_text_data(
        filename = "data/training/william-blog-training-raw.txt",
        order = 1
        )

print(x)

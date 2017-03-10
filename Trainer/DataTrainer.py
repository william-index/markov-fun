import attr

@attr.s
class DataTrainer(object):
    foo = attr.ib()


    """
    Sample method
    """
    def sample(self, bat):
        print("Called sample method")
        myfile = open('data/training/william-blog-training-raw.txt', 'r')
        data = myfile.read()
        myfile.close()

        newfile = open('data/processed/sample.txt', 'w')
        newfile.write(data)
        newfile.close()

        print(data)

        return self.foo + bat

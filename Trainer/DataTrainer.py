import attr

@attr.s
class DataTrainer(object):
    foo = attr.ib()


    """
    Sample method
    """
    def sample(self, bat):
        print("Called sample method")

        return self.foo + bat

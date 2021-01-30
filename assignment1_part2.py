
class Book:
    def __init__(self, author='', title=''):
        self.author = author
        self.title = title
        pass

    def display(self):
        print(self.title + ' written by ' + self.author)
        pass


Book('John Steinbeck', 'Of Mice and Men').display()
Book('Harper Lee', 'To Kill a Mockingbird').display()

if __name__ == "__main__":
    pass

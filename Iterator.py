class RemoteControlTV():
    def __init__(self):
        self.channels = ["Discovery", "STV", "Cartoon", "Animal Kingdom"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


MyTVRemote = RemoteControlTV()
iter = iter(MyTVRemote)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

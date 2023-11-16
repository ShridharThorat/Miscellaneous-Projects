from data_structures import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]

    # Key is assumed to be a string
    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for list in list_at_array:  # list = [key, value]
            if key == list[0]:
                list[1] = value
        # if the key wasn't found
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        list_at_index = self.array[array_index]
        for list in list_at_index:  # list = [key, value]
            if list[0] == key:
                return list[1]
        return None  # not found


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def assign(self, k, v):
        array_index = self.compressor(self.hash(k))
        current_array_value = self.array[array_index]

        # Add code below
        if current_array_value is None:
            self.array[array_index] = [k, v]
            return
        if current_array_value[0] == k:
            self.array[array_index] = [k, v]
            return
        

        # Collision!
        number_collisions = 1

        while (current_array_value[0] != k):
            new_hash_code = self.hash(k, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [k, v]
                return

            if current_array_value[0] == k:
                self.array[new_array_index] = [k, v]
                return

            number_collisions += 1

        return

    def retrieve(self, k):
        array_index = self.compressor(self.hash(k))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == k:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != k):
            new_hash_code = self.hash(k, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == k:
                return possible_return_value[1]

            retrieval_collisions += 1

        return

    def hash(self, k, count_collisions=0):
        k_bytes = k.encode()
        hash_code = sum(k_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size


# Testing code
hm = HashMap(5)
print("HashMap created with 5 indices.")
hm.assign('a', 1)
hm.assign('b', 2)
print("Added key/value pairs a:1 and b:2.")
print("HashMap: " + str(hm.array))
hm.assign('a', 3)
print("Added key/value pair a:3.")
print("HashMap: " + str(hm.array))

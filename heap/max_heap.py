class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1) # adding -1 because if not, the if condition would hit out of bounds on index

    def delete(self):
        self.swap(0, len(self.storage) - 1)
        value_deleted = self.storage.pop()
        self._sift_down(0)
        return value_deleted

    def get_max(self):
        if not self.storage:
            return "Heap is empty"
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # Loop until node is shifted to correct position in tree and node(s) traded are in correct position
        while True:
            p_index = (index - 1) // 2 # parent node (formula from lambda video)
            if self.storage[index] > self.storage[p_index]:
                self.swap(index, p_index)
            index = p_index # child becomes parent
            if p_index <= 0: # node has been shifted to the top-most place, no reason to keep looping
                break


    def _sift_down(self, index):
        # following logic from video...
        p_index = index
        # Loop until index(parent) is greater than both child nodes
        #   or, parent has no children
        while True:
            left = 2 * p_index + 1 # left child node of parent node
            right = 2 * p_index + 2 # right child node of parent node

            # parent has two children
            if len(self.storage) > left and len(self.storage) > right:

                # parent is less than both children
                if self.storage[p_index] < self.storage[left] and self.storage[p_index] < self.storage[right]:

                    # if left child is greater than right child
                    if self.storage[left] > self.storage[right]:
                        self.swap(p_index, left)
                        p_index = left
                    else:
                        self.swap(p_index, right)
                        p_index = right

                # parent is less than left child
                elif self.storage[p_index] < self.storage[left]:
                    self.swap(p_index, left)
                    p_index = left

                # parent is less than right child
                elif self.storage[p_index] < self.storage[right]:
                    self.swap(p_index, right)
                    p_index = right
                else:
                    break

            # parent has 1 child
            elif len(self.storage) > left:

                # if parent is less than child(always left if just 1 child)
                if self.storage[p_index] < self.storage[left]:
                    self.swap(p_index, left)
                    break

            else:
                break

    def swap(self, i, j):
        tmp = self.storage[i]
        self.storage[i] = self.storage[j]
        self.storage[j] = tmp
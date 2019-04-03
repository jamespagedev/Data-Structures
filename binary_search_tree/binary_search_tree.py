class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.value < value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)


    def contains(self, target):
        if self.value is None:
            return False
        elif self.value == target:
            return True
        else:
            if self.value < target:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
            else:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)

    def get_max(self):
        if self.value is None:
            return None
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        value = self.value
        left = self.left
        right = self.right
        if value is None:
            return cb(value)
        elif left is None and right is None:
            cb(value)
        if left is not None:
            self.left.for_each(cb)
            cb(value)
        if right is not None:
            self.right.for_each(cb)
            cb(value)

    # Use this if you want to pass an empty array and fill it
    # def for_each(self, arr):
    #     value = self.value
    #     left = self.left
    #     right = self.right
    #     if value is None:
    #         return arr
    #     elif left is None and right is None:
    #         arr.append(value)
    #         return arr
    #     if left is not None:
    #         self.left.for_each(arr)
    #         arr.append(value)
    #     if right is not None:
    #         self.right.for_each(arr)
    #         arr.append(value)
    #     return arr
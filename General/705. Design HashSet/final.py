class MyHashSet(object):

    def __init__(self):
        self.hashset = list()

    def findIndex(self, key):
        """
        :rtype: key if found else None
        """
        i = 0
        for val in self.hashset:
            if val == key:
                return i
            i += 1

        return None

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        contains = self.findIndex(key)
        if contains is None:
            self.hashset.append(key)
        return None

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        contains = self.findIndex(key)
        if contains is not None:
            self.hashset.pop(contains)
        return None

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        contains = self.findIndex(key)
        if contains is not None:
            return True
        else:
            return False


if __name__ == '__main__':
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    a = obj.contains(1)
    obj.add(2)
    b = obj.contains(2)
    obj.remove(2)
    c = obj.contains(2)


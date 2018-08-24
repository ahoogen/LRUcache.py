class KeyNotFoundError(Exception):
    pass

class CacheSizeError(Exception):
    pass

class CacheElem():
    """CacheElem is a node in a doubly-linked list"""
    def __init__(self):
        self.prev = None
        self.next = None
        self.key = None
        self.val = None
        self.inserted = False

class LRUCache():

    """LRUCache maintains a Least Recently Used cache of items maintained in
    a doubly-linked list. Most recently used elements are at the front of the
    list, while more stale elements get pushed down towards the tail of the list.
    The last element in the list is always the least recently used element, with
    the exception of a list containing a single element.

    LRUCache uses a hash-table lookup for cache items to provide constant lookup
    time. Link updates are also performed in constant time while the doubly-
    linked list structure provides a natural way for older elements to be pushed
    towards the end of the structure.
    """

    def __init__(self):
        self.lookup = dict()
        self.head = None
        self.tail = None
        self.max_size = 0
        self.cur_size = 0
        self.size_set = False

    def setCacheSize(self, size):
        """Sets the max number of cache elements that this cache will store.
        Only allows cache size to be set once.
        """
        if not type(size) == type(int()):
            raise CacheSizeError("SIZE must be an integer")

        if self.size_set:
            raise CacheSizeError("Cache SIZE already set")

        self.max_size = size
        self.size_set = True

    def update(self, elem):
        """Updates the linked list pushing element to the head of the list,
        and all other elements towards the tail of the list.

        Update will allow the linked list to grow to a maximum of self.max_size
        elements. Once self.max_size elements are reached, update raises an
        exception when trying to insert new elements. Freeing and re-using the
        least-used element is handled by the put() method.
        """
        if not elem.prev and not elem.next and not elem.inserted and self.cur_size < self.max_size:
            # If we're a new link element
            elem.inserted = True
            elem.next = self.head
            self.head = elem
            if not elem.next:
                # only element
                self.tail = elem
            self.lookup[elem.key] = elem
            self.cur_size += 1
        elif elem.prev and elem.next:
            # Elem is in the middle, relink list
            prev = elem.prev
            next = elem.next
            prev.next = next
            next.prev = prev
            elem.prev = None
            elem.next = self.head
            self.head = elem
        elif elem == self.head:
            # Element is already at head, no need to update
            pass
        elif elem == self.tail:
            # Element is at tail
            prev = elem.prev
            elem.prev = None
            self.tail = prev
            elem.next = self.head
            self.head = elem
        else:
            raise CacheSizeError("Cache size exceeded")

    def get(self, key=None):
        """Gets cache value for key, or raises KeyNotFoundError otherwise."""
        elem = self.lookup.get(key, None)
        if elem == None:
            raise KeyNotFoundError("Key '{}' not found".format(key))

        self.update(elem)
        return elem

    def put(self, key=None, value=None):
        """Updates key element to value. If key is not found in the lookup table
        either a new element is created an inserted into the list, or the least-
        recently used element is freed from the cache and resued to store the new
        key/value pair.
        """
        elem = self.lookup.get(key, None)
        if elem == None:
            if self.cur_size < self.max_size:
                elem = CacheElem()
                elem.key = key
                elem.val = value
            else:
                elem = self.tail
                del(self.lookup[elem.key])
                elem.key = key
                self.lookup[key] = elem

        elem.val = value
        self.update(elem)

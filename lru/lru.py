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

    def link(self, b):
        """Links B to self so that self <==> B"""
        self.next = b
        b.prev = self
        return self

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
        self.size_set = False

    def setCacheSize(self, size):
        """Initializes LRUCache with a continuous block of memory to improve
        locality. Can only initialize cache once.
        """
        if not type(size) == type(int()):
            raise CacheSizeError("SIZE must be an integer")

        if self.size_set:
            raise CacheSizeError("Cache SIZE already set")

        # Initialize LRU cache
        cache = CacheElem()
        last = cache
        for i in range(1, size):
            elem = CacheElem()
            last.link(elem)
            last = elem

        self.head = cache
        self.size_set = True

    def isInitialized(self):
        return self.size_set

    def update(self, elem):
        """Updates the linked list pushing element to the head of the list,
        and all other elements towards the tail of the list.
        """
        if elem.prev and elem.next:
            # Elem is in the middle, relink list
            elem.prev.link(elem.next)
            # Update floating tail while populating
            if elem == self.tail:
                self.tail = elem.prev
            # update elem to head
            self.head = elem.link(self.head)
            self.head.prev = None
        elif elem == self.head:
            pass
        elif not elem.next:
            # Element is at tail
            self.tail = elem.prev
            self.tail.next = None
            self.head = elem.link(self.head)
            self.head.prev = None

    def get(self, key=None):
        """Gets cache value for key, or raises KeyNotFoundError otherwise."""
        if not self.size_set:
            raise CacheSizeError("Cache is uninitialized")

        if not key:
            raise KeyNotFoundError("Key can't be None type for get()")
            
        elem = self.lookup.get(key, None)
        if elem == None:
            raise KeyNotFoundError("Key '{}' not found".format(key))

        self.update(elem)
        return elem

    def put(self, key=None, value=None):
        """Updates key element to value. If key is not found in the lookup table
        either the floating tail pointer is incremented to accommodate a new
        element, or the least-recently used element is freed from the cache and
        resued to store the new key/value pair.
        """
        if not self.size_set:
            raise CacheSizeError("Cache is uninitialized")

        if not key:
            raise KeyNotFoundError("Key can't be None type for put()")

        elem = self.lookup.get(key, None)
        if elem == None:
            # First insert
            if not self.tail:
                elem = self.head
                self.tail = elem
            # Still populating cache
            elif self.tail.next:
                elem = self.tail.next
                self.tail = elem
            # Evict LRU
            else:
                elem = self.tail
                del(self.lookup[elem.key])

            elem.key = key
            self.lookup[key] = elem

        elem.val = value
        self.update(elem)

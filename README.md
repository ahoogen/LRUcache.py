# LRUcache.py
Python implementation of a Least Recently Used cache.

LRUCache provides O(c) growth complexity on all cache reads, writes and updates.

Constant access time is provided by a lookup hash table for accessing cache elements.

Constant LRU ordering is achieved by using a doubly-linked list to maintain cache order. Elements at the head of the list are most-recently accessed. Any accessed element is extracted from its current position in the list and prepended to the front of the list, pushing all remaining (and now less used) elements towards the tail of the list.

When a new cache element is added to the cache, exceeding LRUCache[MAXLEN], the tail of the linked list is guaranteed to be the least-recently used element, and is removed from the cache lookup table. The element is repurposed for the new cache element and prepended to the linked list.

## Running LRUCache
```
> cd LRUCache.py
> python lru
```

## Known Issues
There are currently no known issues, however there are shortcomings that I would have addressed if more time were allowed:
- There are no tests written
- LRUCache class properties are exposed and used directly by __main__
- __main__ isn't very maintainable, I would move handling code into individual functions

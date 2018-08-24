# LRUcache.py
Python implementation of a Least Recently Used cache.

LRUCache has an initialization cost of O(n), and a cost of O(1) for all cache get, put and LRU shifts.

Constant-time LRU ordering is achieved by using a doubly-linked list to maintain cache order. Elements at the head of the list are most-recently accessed. Elements are accessed by a hash table giving constant-time access to the element's position in the linked list. The element is then extracted from its current position in the list and prepended to the front of the list, pushing all remaining (and now less used) elements towards the tail of the list.

When a new cache element is added to the cache, exceeding LRUCache[MAXLEN], the tail of the linked list is guaranteed to be the least-recently used element, and is removed from the cache lookup table. The element is re-purposed for the new cache element and prepended to the linked list.

LRUCache initializes the linked list to ensure that memory usage is as localized as possible to reduce paging cycles. The LRU element is held in a floating list tail pointer until LRUCache[MAXLEN] equals the tail pointer.

## Running LRUCache
```
> cd /path/to/LRUCache.py
> python lru
```
The following commands are accepted:
- __SIZE *n*__: Initializes the cache to *n* elements
- __GET *n*__: Prints value of cache element *n* or returns __NOTFOUND__
- __SET *n x*__: Sets cache element *n* to value *x*
- __EXIT__: Quits LRUCache

## Running LRUCache With Test Data
```
> cd /path/to/LRUCache.py
> cat input| python lru
```
to see the output of LRUCache, or:
```
> cat input| python lru| diff output -
```
to diff LRUCache output with expected output.

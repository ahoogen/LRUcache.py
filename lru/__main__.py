import sys
import lru

class CommandError(Exception):
    pass

def parseline(line):
    args = line.strip().split(' ')
    cmd = args[0].upper()
    ar1 = ar2 = None
    if cmd not in ['GET', 'SET', 'SIZE', 'EXIT']:
        raise CommandError()

    if len(args) >= 2:
        ar1 = args[1]

    if len(args) == 3:
        ar2 = args[2]

    return (cmd, ar1, ar2)

if __name__ == '__main__':
    l = lru.LRUCache()

    while(1):
        line = raw_input()
        try:
            args = parseline(line)
        except CommandError:
            print('ERROR')
            continue

        if args[0] == 'EXIT':
            exit(0)
        elif args[0] == 'SIZE':
            if l.size_set:
                print('ERROR')
                continue
            try:
                l.setCacheSize(int(args[1]))
                print('SIZE OK')
            except lru.CacheSizeError:
                print('ERROR')
        elif not l.size_set:
            print('ERROR')
            continue
        elif args[0] == 'GET':
            if args[2]:
                print('ERROR')
                continue
            try:
                elem = l.get(args[1])
            except lru.KeyNotFoundError:
                print('NOTFOUND')
                continue
            print("GOT {}".format(elem.val))
        elif args[0] == 'SET':
            if not args[2]:
                print('ERROR')
                continue
            l.put(args[1], args[2])
            print('SET OK')

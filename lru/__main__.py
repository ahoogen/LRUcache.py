import lru

class CommandError(Exception):
    pass

def parseline(line):
    args = line.strip().split(' ')
    # Strip empty elements caused by extra spacing
    args = [i for i in args if i]
    cmd = args[0].upper()
    ar1 = ar2 = None
    if cmd not in ['GET', 'SET', 'SIZE', 'EXIT']:
        raise CommandError()

    # EXIT has no arguments
    if len(args) >= 2:
        ar1 = args[1]

    # SET has only one argument
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

        # Handle EXIT
        if args[0] == 'EXIT':
            exit(0)

        # Handle SIZE n
        elif args[0] == 'SIZE':
            if l.isInitialized():
                print('ERROR')
                continue
            try:
                l.setCacheSize(int(args[1]))
                print('SIZE OK')
            except lru.CacheSizeError:
                print('ERROR')

        # Error on all commands until SIZE OK
        elif not l.isInitialized():
            print('ERROR')
            continue

        # Handle GET
        elif args[0] == 'GET':
            # GET only accepts one argument
            if args[2] or not args[1]:
                print('ERROR')
                continue
            try:
                elem = l.get(args[1])
            except lru.KeyNotFoundError:
                print('NOTFOUND')
                continue
            print("GOT {}".format(elem.val))

        # Handle SET
        elif args[0] == 'SET':
            # SET requires 2 arguments
            if not args[2] or not args[1]:
                print('ERROR')
                continue
            l.put(args[1], args[2])
            print('SET OK')

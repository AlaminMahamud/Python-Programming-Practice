#pretty printing
import pprint
message = 'A quick brown fox jumps over the lazy dog'
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] += 1

pprint.pprint(count)

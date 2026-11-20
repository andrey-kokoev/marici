"""Keep all 27 old addresses. Add five as a positive cycle. Exact check of result."""
from ramsey_39_from_27 import ind,rows
from random import Random
from itertools import combinations
rng=Random(39); opts=[x for x in ind if x.bit_count()==7];seven=opts[:]; miss=[sum(1<<i for i,s in enumerate(seven) if not x&s) for x in opts]
n=len(opts);adj=[{j for j in range(n) if not opts[i]&opts[j]} for i in range(n)];far=[{j for j in range(n) if not miss[i]&miss[j]} for i in range(n)]
def seek(path):
    if len(path)==5:return path
    d=len(path); choices=set(range(n))
    for i,v in enumerate(path):choices &= (adj if d-i in (1,4) else far)[v]
    choices=sorted(choices);rng.shuffle(choices)
    for w in choices:
        sol=seek(path+[w])
        if sol:return sol
sol=seek([])
if sol:
    independent=list(ind);oldrows=rows[:]
    for i,v in enumerate(sol):
        p=opts[v]|sum(1<<(27+j) for j in range(i) if i-j in (1,4));assert p in independent
        independent += [s|1<<len(oldrows) for s in independent if not s&p];oldrows.append(p)
        print(len(oldrows),[j+1 for j in range(len(oldrows)-1) if p>>j&1])
    assert max(s.bit_count() for s in independent)==8
else:print('no such cycle with all five old neighborhoods of size 7')

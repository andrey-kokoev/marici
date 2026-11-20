"""Input: ONLY first 276 adjacency bits of McKay r38_27.g6.gz record 1.
Enumerate column multisets (including repeated types) and internal sign choices.
"""
from itertools import combinations_with_replacement, product
from collections import Counter
bits=''.join(f'{ord(c)-63:06b}' for c in r'GoXI_J?Ec@JScg@sa@o_OG\CP?IOd?KCQ?LA?WlH_@AC?i');assert len(bits)==276
ind=[0]; rows=[];off=0
for j in range(24):
    p=sum(1<<i for i in range(j) if bits[off+i]=='1');off+=j
    assert all(not rows[i]&p for i in range(j) if p>>i&1)
    rows.append(p);ind += [s|1<<j for s in ind if not s&p]
assert max(s.bit_count() for s in ind)==7
sets=lambda k:[s for s in ind if s.bit_count()==k]
seven,six,five=map(sets,(7,6,5));opts=sorted(p for p in ind if all(p&s for s in seven));n=len(opts)
links={};partners=[0]*n;wins=set();solutions=[]
for i,j in combinations_with_replacement(range(n),2):
    p,q=opts[i],opts[j];a=[]
    if all(s&(p|q) for s in six):a.append(0)
    if not p&q:a.append(1)
    links[i,j]=a
    if a:
        for k in {i,j}:partners[k]+=1
for i,j,k in combinations_with_replacement(range(n),3):
    for signs in product(links[i,j],links[i,k],links[j,k]):
        if sum(signs)==3:continue
        if sum(signs)==0 and any(not s&(opts[i]|opts[j]|opts[k]) for s in five):continue
        wins.update((i,j,k));solutions.append((i,j,k,signs))
print('partners, succeeds:',sorted(Counter((partners[i],i in wins) for i in range(n)).items()));print('solutions',len(solutions))
for i,j,k,signs in solutions[:1]:print([[x+1 for x in range(24) if opts[v]>>x&1] for v in (i,j,k)],signs)

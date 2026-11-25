"""Audit every supplied K7 for a forced-blue triple, record witnesses and minimum additional deletion transversals for individual triples."""
from ramsey312_google_two_step import *
from functools import lru_cache
from itertools import combinations
from collections import Counter
@lru_cache(maxsize=200000)
def witness(p,k):
 if not k:return 0
 while p.bit_count()>=k:
    b=p&-p;p-=b;t=witness(p&~adj[b.bit_length()-1],k-1)
    if t is not None:return b|t
 return None

def main():
 out=[];hist=Counter();seeds=Counter();D0=(3,17,36,40,42,44)
 for f in sys.argv[1:]:
    for l in open(f):
        tag,d,*s=l.split();assert tag=='K';d=int(d);s=list(map(int,s));h=F^d;assert len(set(s))==len(s)==7 and all(witness(h&~x,11) is None and not x&d and all(not x&adj[i] for i in bits(x)) for x in s);assert all(not x&y or witness(h&~(x|y),10) is None for x,y in combinations(s,2));bad=[]
        for i,j,k in combinations(range(7),3):
            x,y,z=s[i],s[j],s[k];
            if x&y and y&z and x&z and (t:=witness(h&~(x|y|z),9)) is not None:bad.append([i,j,k,t])
        hist[len(bad)]+=1;seeds[tuple(bits(d))]+=1;out.append(dict(d=d,s=s,n=len(bad),certificate=bad[0] if bad else None))
 print('counts',hist,'cores',len(seeds));print('positive cores',sorted(seeds.items()));(D/'ramsey312_sample6_triples.json').write_text(json.dumps(out))
if __name__=='__main__':main()

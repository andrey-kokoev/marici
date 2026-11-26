"""Self-contained induced witness replay. Only discovery needs catalogue files.\nUsage: python ramsey_retention_slice.py collect <r39_35.g6> <r45_24.g6>; or no args for replay."""
import gzip,itertools,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];D=R/'voevodsky/results/ramsey_retention_slice.json';CAT=R/'chatgpt/ramsey/pauli-realization-catalogues'
def decode(s):
    n=ord(s[0])-63;assert 0<n<63;a=[0]*n;t=0
    for j in range(n):
        for i in range(j):
            if (ord(s[1+t//6])-63)>>(5-t%6)&1:a[i]|=1<<j;a[j]|=1<<i
            t+=1
    return a

def has(a,p,r):
    if r==0:return True
    while p.bit_count()>=r:
        b=p&-p;p^=b
        if has(a,p&a[b.bit_length()-1],r-1):return True
    return False

def check(a,p,l,k):return not has(a,p,l) and not has([~x for x in a],p,k)
def pentagon(a,p):
    for idx in itertools.combinations([i for i in range(len(a)) if p>>i&1],5):
        q=sum(1<<i for i in idx)
        if all((a[i]&q).bit_count()==2 for i in idx):return q
    raise ValueError('no pentagon')

def collect():
    rows=[]
    for k,n in [(4,8),(5,13),(6,17),(7,22),(8,27),(9,35),(5,24)]:
        l=4 if n==24 else 3;fn=Path(sys.argv[3]) if l==4 else Path(sys.argv[2]) if k==9 else next(CAT.glob(f'r3{k}_{n}.g6*'));row=91 if l==4 else 1
        with (gzip.open if fn.suffix=='.gz' else open)(fn,'rt') as f:s=next(itertools.islice(f,row-1,None)).strip()
        a=decode(s);assert len(a)==n;p=6288881 if l==4 else (1<<n)-1;rows.append(dict(l=l,k=k,graph6=s,row=row,seed17=p if l==4 else None,seed5=pentagon(a,p)))
    D.write_text(json.dumps(rows,indent=1)+'\n')

def replay():
    for r in json.loads(D.read_text()):
        a=decode(r['graph6']);p=(1<<len(a))-1;q=r['seed5'];assert check(a,p,r['l'],r['k']);assert q.bit_count()==5 and check(a,q,3,3)
        if r['seed17'] is not None:
            u=r['seed17'];assert u&p==u and q&u==q and u.bit_count()==17 and check(a,u,4,4)
        print(r['l'],r['k'],len(a),'verified')
if __name__=='__main__':
    if len(sys.argv)>1:collect()
    replay()

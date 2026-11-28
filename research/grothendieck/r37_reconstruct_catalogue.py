"""Relabel all catalogue equality cases and test each completion fibre."""
from r37_exchange_falsifier import p,n
from r37_reconstruct_sat import models

def all_six(a,p,s):
    if s.bit_count()==6:yield s;return
    while p.bit_count()>=6-s.bit_count():
        b=p&-p;p^=b;yield from all_six(a,p&~a[b.bit_length()-1],s|b)

def equality_cases(sizes=(10,)):
    for idx,line in enumerate(p.read_text().splitlines()):
        bits=''.join(f'{ord(c)-63:06b}' for c in line[1:]);a=[0]*n
        for b,(j,i) in zip(bits,((j,i) for j in range(n) for i in range(j))):
            if b=='1':a[i]|=1<<j;a[j]|=1<<i
        six=list(all_six(a,(1<<n)-1,0))
        for s in six:
            missed=[t for t in six if not s&t]
            if len(missed) not in sizes:continue
            order=sorted(range(n),key=lambda i:not(s>>i&1));h=[sum((a[i]>>j&1)<<k for k,j in enumerate(order)) for i in order]; B={frozenset(k for k,j in enumerate(order) if t>>j&1) for t in missed}
            yield idx,order,h,B

if __name__=='__main__':
    total=0
    for idx,order,h,B in equality_cases():
            alt=next(models(h,B),None);total+=1
            if alt:print('alternative to classify',idx,order[:6],alt);quit()
    print('all rooted equality cases labelled-unique:',total)

"""Count off-diagonal departures from a fixed + background under symmetric switching."""
import csv
from pathlib import Path
from itertools import combinations


def main():
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:
        h,*rows=csv.reader(f)
    n=len(rows); labels=list(map(int,h[1:])); full=(1<<n)-1
    neg=[sum(1<<j for j in range(n) if j!=i and row[j+1]=='0') for i,row in enumerate(rows)]
    def count(mask):return sum(((row^(mask if not mask>>i&1 else full^mask))&~(1<<i)).bit_count() for i,row in enumerate(neg))//2
    start=count(0);val=start;mask=0;best=val;win=0;ties=1
    for t in range(1,1<<(n-1)):
        flip=(t&-t)<<1;i=flip.bit_length()-1
        before=((neg[i]^(full^mask if mask&flip else mask))&~flip).bit_count();val+=n-1-2*before;mask^=flip
        if val<best:best,win,ties=val,mask,1
        elif val==best:ties+=1
    assert count(win)==best
    print('unit',start,'alternate',count(sum(1<<j for j in range(1,n,2))),'best',best,'ties',ties,'negative labels',[labels[j] for j in range(n) if win>>j&1])

if __name__=='__main__':main()

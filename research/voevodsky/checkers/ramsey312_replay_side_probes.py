"""Verify one-bit split proofs by SAT implication, not by trusting a list of supports or any pair edges."""
from ramsey312_google_two_step import *
import csv

def main():
 elev=list(sets(F,11));r=csv.reader((D/'ramsey312_side_probes.csv').open());checked=queries=0
 for l in r:
    u,v,nrows,old,dia,wd,ok,p,q,m0,t0,m1,t1,bit,oldedge=map(int,l);assert ok and bit<52
    h=F^(1<<u)^(1<<v);lo=sum(1<<j for j in bits(h) if (adj[j]&h).bit_count()<11)
    with Solver(name='g4') as sl:
        for i in bits(h):
            if not (lo>>i)&1:sl.add_clause([-1-i]);continue
            for j in bits(adj[i]&lo&((1<<i)-1)):sl.add_clause([-1-i,-1-j])
        for s in {s&lo for s in elev if not s&~h}:sl.add_clause([j+1 for j in bits(s)])
        for sign,m,t in [(-1,m0,t0),(1,m1,t1)]:
            assert m.bit_count()==1 and t.bit_count()==10 and not (t|m)&~h and not t&m and all(not adj[i]&t for i in bits(t));b=sign*(bit+1);assert sl.solve(assumptions=[b]);
            for goal in [-m.bit_length(),*[i+1 for i in bits(t)]]:
                assert not sl.solve(assumptions=[b,goal]);queries+=1
    checked+=1
 print('verified nonempty sides',2*checked,'impossible violations',queries)
if __name__=='__main__':main()

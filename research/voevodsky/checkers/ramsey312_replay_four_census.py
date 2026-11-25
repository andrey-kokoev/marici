"""Independent SAT challenge to compressed four-class certificates. --all verifies every core; default checks all exact repairs plus a fixed stride control."""
from ramsey312_google_two_step import *
import csv,gzip,collections

def main():
 el=list(sets(F,11));counts=collections.Counter()
 with gzip.open(D/'ramsey312_all_four_covers.csv.gz','rt') as f:
    rd=csv.reader(f);next(rd)
    for i,row in enumerate(rd):
        a,b,c,d,n,rep,*cert=map(int,row)
        if '--all' not in sys.argv and not rep and i%997:continue
        h=F^sum(1<<v for v in (a,b,c,d));lo=sum(1<<v for v in bits(h) if (adj[v]&h).bit_count()<11)
        with Solver(name='g4') as sl:
            for v in bits(lo):
                for j in bits(adj[v]&lo&((1<<v)-1)):sl.add_clause([-1-v,-1-j])
            for s in {x&lo for x in el if not x&~h}:sl.add_clause([v+1 for v in bits(s)])
            for b,t in zip(cert[::2],cert[1::2]):
                assert b.bit_count()==1 and b&lo and not b&t and not t&~h and t.bit_count()==10 and all(not adj[v]&t for v in bits(t));sl.add_clause([-b.bit_length(),*[v+1 for v in bits(t&lo)]])
            assert not sl.solve();counts[rep]+=1
 print('SAT replays, ordinary and repaired',counts)
if __name__=='__main__':main()

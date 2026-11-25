"""SAT challenge to class cover: require a legal support outside all three classes. Pass --all for all cores; default deterministic stratified sample."""
from ramsey312_google_two_step import *
import csv

def main():
 rows=[tuple(map(int,r)) for r in csv.reader((D/'ramsey312_three_deletions.csv').open())];assert len({r[:3] for r in rows})==22100
 picked=rows if '--all' in sys.argv else list(dict.fromkeys(rows[::100]+[max(rows,key=lambda r:r[3])]))
 el=tuple(sets(F,11));checked=0
 for u,v,w,count,*cert in picked:
    h=F^(1<<u)^(1<<v)^(1<<w);lo=sum(1<<i for i in bits(h) if (adj[i]&h).bit_count()<11)
    with Solver(name='g4') as sl:
        for i in bits(lo):
            for j in bits(adj[i]&lo&((1<<i)-1)):sl.add_clause([-1-i,-1-j])
        for s in {s&lo for s in el if not s&~h}:sl.add_clause([i+1 for i in bits(s)])
        for b,t in zip(cert[::2],cert[1::2]):
            assert b.bit_count()==1 and b&lo and t.bit_count()==10 and not t&~h and not b&t and all(not adj[i]&t for i in bits(t));sl.add_clause([-b.bit_length(),*[i+1 for i in bits(t&lo)]])
        assert not sl.solve();checked+=1
 print('cores verified',checked)
if __name__=='__main__':main()

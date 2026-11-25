"""Replay the strict-majority sixth class without loading either the six-coloring, support lists or compatibility graph."""
from ramsey312_google_two_step import *
from itertools import combinations

def main():
 d=[10,37,39,41,43,47];h=F^sum(1<<i for i in d);z=next(r for r in json.loads((D/'ramsey312_flexible_multicerts.json').read_text()) if r['f']==0);red=[b.bit_length()-1 for b,w in z['red']['majority']];ts=[t for t,w in z['blue']['majority']];assert len(set(red))==3 and len(set(ts))==5
 clause=[[-i-1,-j-1] for i in bits(h) for j in bits(h&adj[i]&((1<<i)-1))]+[[v+1 for v in bits(e)] for e in sets(h,11)];
 for b,t in z['rect']:assert b.bit_count()==1 and b&h;clause.append([-b.bit_length(),*[v+1 for v in bits(t)]])
 for t in [*ts,*[t for b,t in z['rect']]]:assert not t&~h and t.bit_count()==10 and all(not adj[i]&t for i in bits(t))
 for i,j in combinations(red,2):
    with Solver(name='g4',bootstrap_with=clause+[[-i-1],[-j-1]]) as sl:assert not sl.solve()
 for tt in combinations(ts,3):
    with Solver(name='g4',bootstrap_with=clause+[[i+1 for i in bits(t)] for t in tt]) as sl:assert not sl.solve()
 print('verified unconditionally on all legal residual supports: 2 of',red,'and miss 3 of 5 tens');(D/'ramsey312_majority_certificate.json').write_text(json.dumps(dict(deletions=d,rect=z['rect'],residual_red_vertices=red,residual_tens=[list(bits(t)) for t in ts])))
if __name__=='__main__':main()

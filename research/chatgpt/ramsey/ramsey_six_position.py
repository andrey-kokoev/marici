"""Uniform within-cube readout, exact SAT search for fixed raw probes."""
from ramsey_six_boundary_moves import ws,A,B,R,E,P,D,json,seed,product,combinations,Counter,G
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType

def states(w):return {(i,j,k):(R if k else ident)[(B if j else ident)[(A if i else ident)[w]]] for i,j,k in product(range(2),repeat=3)}
ident={w:w for w in ws};left=ws.copy();O=[]
while left:
    o=set(states(min(left)).values());O.append(o);left-=o
pairs=[u^v for o in O for u,v in combinations(o,2)];edges=sorted(set(pairs),key=int.bit_count);small=[]
for d in edges:
    if not any(d&s==s for s in small):small.append(d)
C=[[i+1 for i in range(45) if s>>i&1] for s in small];hist=Counter();
for t in combinations(range(45),3):
    mask=sum(1<<i for i in t);hist[sum(len({w&mask for w in o})==8 for o in O)]+=1

def exact(k):
    with Solver(name='g4',bootstrap_with=C+CardEnc.atmost(lits=list(range(1,46)),bound=k,encoding=EncType.seqcounter).clauses) as solver:
        if not solver.solve():return None
        return [v-1 for v in solver.get_model() if 0<v<=45]
for k in range(4,15):
    t=exact(k);print('bound',k,t,flush=True)
    if t is not None:break
assert t and len(t)==k and max(hist)<36;mask=sum(1<<i for i in t);addr=lambda i:'-'.join(''.join(map(str,P[j])) for j in E[i]);codes={};costs=Counter();
for o in O:
    assert len({w&mask for w in o})==8;base=min(o,key=lambda w:w&mask);tab=states(base);codes.update({w:b for b,w in tab.items()});
    for bits,w in tab.items():assert {tab[b] for b in tab if sum(i!=j for i,j in zip(b,bits))==1}=={g[w] for g in (A,B,R)}
r=dict(cubes=len(O),triple_hist=dict(hist),minimum_raw_probes=k,probes=[addr(i) for i in t],indices=t,comparisons=len(pairs),clauses=len(C),seed_coords=codes[seed],mate_coords=codes[R[seed]],codes_checked=len(codes));closure=set(t)
while True:
    more=closure|{g[i] for g in G for i in closure}
    if more==closure:break
    closure=more
comp=json.loads((D/'ramsey_six_component_label.json').read_text());J={i for v in comp['greedy_counts'] for m in v['masks'] for i in range(45) if m>>i&1};r.update(raw_reads_for_canonical_comparisons=len(closure),overlap_with_component=len(J&set(t)),joint_label_raw_reads=len(J|set(t)),joint_canonical_raw_reads=len(J|closure));print(r);(D/'ramsey_six_position.json').write_text(json.dumps(r,indent=2)+'\n')

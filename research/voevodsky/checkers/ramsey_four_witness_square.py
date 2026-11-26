"""Glue the retained catalogue (4,5) side and its colour reverse over a common Paley17. Only the 7x7 cross bits are new. Test every seed identification for this marked pair; independently check each returned graph."""
from itertools import combinations
from pathlib import Path
import json,networkx as nx
from pysat.solvers import Solver
from ramsey_retention_slice import decode,check,has
D=Path(__file__).resolve().parents[1]/'results';r=json.loads((D/'ramsey_retention_slice.json').read_text())[-1];g=decode(r['graph6']);S=[i for i in range(24) if r['seed17']>>i&1];V=[i for i in range(24) if i not in S];H=(1<<17)-1

def side(order,flip):return [sum(1<<j for j,y in enumerate(order) if x!=y and bool(g[x]>>y&1)!=flip) for x in order]
def runs():
 graph=nx.Graph();graph.add_nodes_from(S);graph.add_edges_from((i,j) for i,j in combinations(S,2) if g[i]>>j&1);G=nx.algorithms.isomorphism.GraphMatcher(graph,nx.complement(graph));left=side(S+V,False);attempts=0;solved=[];example=None
 for mp in G.isomorphisms_iter():
    attempts+=1;right=side([mp[i] for i in S]+V,True);assert [v&H for v in left[:17]]==[v&H for v in right[:17]];clauses=[]
    for red in (0,1):
        L=left if red else [~x for x in left];R=right if red else [~x for x in right];small=[]
        for a in (L,R):
            groups=[]
            for k in range(1,5):
                for u in combinations(range(7),k):
                    if any(not(a[17+i]>>(17+j)&1) for i,j in combinations(u,2)):continue
                    p=H
                    for i in u:p&=a[17+i]
                    groups.append((u,p))
            small.append(groups)
        for x,p in small[0]:
            for y,q in small[1]:
                k=5-len(x)-len(y)
                if k>=0 and has(L,p&q,k):clauses.append([(-1 if red else 1)*(7*i+j+1) for i in x for j in y])
    with Solver(name='g4',bootstrap_with=clauses) as sl:
        if not sl.solve():continue
        pos=set(sl.get_model());a=left.copy()+[0]*7
        for j in range(7):
            for i in range(17):
                if right[17+j]>>i&1:a[i]|=1<<(24+j);a[24+j]|=1<<i
            for i in range(j):
                if right[17+j]>>(17+i)&1:a[24+i]|=1<<(24+j);a[24+j]|=1<<(24+i)
            for i in range(7):
                if 7*i+j+1 in pos:a[17+i]|=1<<(24+j);a[24+j]|=1<<(17+i)
        assert check(a,H,4,4) and check(a,(1<<24)-1,4,5) and check(a,H|(127<<24),5,4) and check(a,(1<<31)-1,5,5)
        forced=[u if u in pos else -u for u in range(1,50) if not sl.solve(assumptions=[-u if u in pos else u])];solved.append(len(forced))
        if example is None:example=dict(status='SAT',clauses=len(clauses),original_seed=S,reverse_seed=[mp[i] for i in S],red_masks=a,forced_cross_literals=forced,red_cross_rows=[format((v>>24)&127,'07b')[::-1] for v in a[17:24]])
 if example is not None:
    from collections import Counter
    example.update(identifications=attempts,solvable=len(solved),forced_count_hist=dict(Counter(solved)));return example
 return dict(status='UNSAT for this pair of marked sides',attempts=attempts)
if __name__=='__main__':
 out=runs();print(out);(D/'ramsey_four_witness_square.json').write_text(json.dumps(out,indent=1)+'\n')

"""Bound four-row feasibility without enumerating row tuples. Fractional packing: each core blue four can be missed at most once. Verify rounded dual bound with integers. Also compute a greedy partition into pairwise conflicting classes via coloring; both are one-sided tests."""
import json,numpy as np,networkx as nx
from scipy.optimize import linprog
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';data=[r for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];out=[]
for idx,r in enumerate(data):
 a=r['core'];I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count()==4];B=np.array([[int(not s&q) for s in S] for q in Q]);unbounded=bool((B.sum(axis=0)==0).any());colors=den=num=lpval=None;weights={}
 if not unbounded:
  lp=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(Q)));assert lp.success;y=np.maximum(0,np.rint(-lp.ineqlin.marginals*10**6)).astype('int64');den=int(min(B.T@y));num=int(sum(y));assert den>0;lpval=-lp.fun;weights={q:int(w) for q,w in zip(Q,y) if w};G=nx.from_numpy_array((B.T@B==0).astype(int));colors=min(max(nx.coloring.greedy_color(G,strategy=st).values())+1 for st in ('largest_first','saturation_largest_first','smallest_last'))
 excluded=not unbounded and (num<4*den or colors<4);assert not(excluded and r['full']);out.append(dict(row=idx,supports=len(S),fours=len(Q),fractional_max=lpval,colors=colors,num=num,den=den,weights=weights,excluded=excluded,actual=r['full']))
print([(z['row'],z['fractional_max'],z['colors'],z['weights']) for z in (out[66],out[93])]);print(sum(r['excluded'] for r in out),'of',sum(not r['actual'] for r in out));(P/'ramsey_support_bound11.json').write_text(json.dumps(out)+'\n')

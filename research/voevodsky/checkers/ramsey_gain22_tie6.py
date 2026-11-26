"""Compare the full isomorphism type of the individually addable edge graph with support/six-clique incidence. Verify fractional packing bounds by integer replay. Distinct bad or good types in this labelled class are not a prospective selection rule."""
import json,itertools,collections,igraph as ig,numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import CAT,D,decode
P=D.parent;controls=json.loads((P/'ramsey_gain22_controls.json').read_text());src=(CAT/'r37_22.g6').read_text().splitlines();out=[]
for r in controls:
 if r['score']!=6:continue
 idx=r['row'];a=decode(src[idx]);E=[(i,j) for i in range(22) for j in range(i) if not(a[i]>>j&1 or a[i]&a[j])];g=ig.Graph(22,E);key=sorted(tuple(sorted(e)) for e in g.permute_vertices(g.canonical_permutation()).get_edgelist());I=[0]
 for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v])
 Q=[q for q in I if q.bit_count()==6];S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];B=np.array([[int(not q&s) for s in S] for q in Q]);lp=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(B)));assert lp.success;y=np.maximum(0,np.rint(-lp.ineqlin.marginals*10**7)).astype('int64');den=int(min(B.T@y));num=int(sum(y));assert den>0;out.append(dict(row=idx,recolor_key=key,shape=sorted((len(vs),g.subgraph(vs).ecount()) for vs in g.connected_components() if len(vs)>1),sixes=len(Q),supports=len(S),counts=r['counts'],den=den,num=num,weights={q:int(v) for q,v in zip(Q,y) if v}));
bad,=[r for r in out if not r['counts'][2]];print('failed',bad['row'],bad['shape'],bad['supports'],bad['sixes'],bad['num']/bad['den']);print('shape matches',[(r['row'],r['counts'],r['num']/r['den']) for r in out if r['recolor_key']==bad['recolor_key']]);print('upper min max',min(r['num']/r['den'] for r in out),max(r['num']/r['den'] for r in out));(P/'ramsey_gain22_tie6.json').write_text(json.dumps(out)+'\n')

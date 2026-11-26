"""Apply the previously proposed square signal throughout the catalogue, including score-matched controls; integer primal for the exceptionally failing score-six core."""
import json,itertools,collections,numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D,CAT,decode
P=D.parent;refs=json.loads((P/'ramsey_gain22_controls.json').read_text());src=(CAT/'r37_22.g6').read_text().splitlines();out=[]
for s,r in zip(src,refs):
 a=decode(s);g=[sum(1<<j for j in range(22) if i!=j and not(a[i]>>j&1 or a[i]&a[j])) for i in range(22)];c=sum((w:=(u&v).bit_count())*(w-1)//2 for u,v in itertools.combinations(g,2))//2;out.append(dict(row=r['row'],cycles=c,score=r['score'],ok=bool(r['witness'])))
for z in (out,[r for r in out if r['score']==6],[r for r in out if r['score']>=4]):print(collections.Counter((bool(r['cycles']),r['ok']) for r in z))
a=decode(src[52]);I=[0]
for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v])
Q=[q for q in I if q.bit_count()==6];S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];B=np.array([[int(not q&s) for s in S] for q in Q]);lp=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(B)));x=np.floor(np.maximum(0,lp.x)*10**6).astype('int64');den=int(max(B@x));num=int(x.sum());assert num>=4*den>0;print('primal',num,den);(P/'ramsey_gain22_square_audit.json').write_text(json.dumps(dict(rows=out,core52_four_mass={s:int(w)*4 for s,w in zip(S,x) if w},den=num))+'\n')

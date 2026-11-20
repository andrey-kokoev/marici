"""Test a rotation-invariant directional tie breaker using the induced metric on bivectors: maximize <W, last_step wedge next_step> only on an imbalance tie. Retains no track sequence or visited list for decisions."""
from ramsey_strip_imbalance_area import G,ids
pairs=((0,1),(0,2),(1,2));K=[[G[i][k]*G[j][l]-G[i][l]*G[j][k] for k,l in pairs] for i,j in pairs]
def wedge(x,y):return [x[i]*y[j]-x[j]*y[i] for i,j in pairs]
def inner(x,y,M):return sum(x[i]*M[i][j]*y[j] for i in range(3) for j in range(3))
def add(x,y):return [a+b for a,b in zip(x,y)]
V={(i,b):[int(i==j)*(1-2*b) for j in ids] for i in ids for b in (0,1)}
for start in (2,3,5):
 current=(start,0);A=V[current][:];W=[0]*3;seq=[current];resolved=[]
 for n in range(59):
    opts={q:inner(add(A,v),add(A,v),G) for q,v in V.items() if q[0]!=current[0] and q[1]!=current[1]};best=[q for q,e in opts.items() if e==min(opts.values())]
    if len(best)>1:
        scores={q:inner(W,wedge(V[current],V[q]),K) for q in best};best=[q for q,e in scores.items() if e==max(scores.values())]
        if len(best)>1:break
        resolved.append((len(seq),scores))
    q,=best;W=add(W,wedge(A,V[q]));A=add(A,V[q]);seq.append(q);current=q
 print('start',start,'steps',len(seq),'first tie',resolved[:1],'first twelve',seq[:12],'final imbalance',A,'area',W)
 if start!=5:
    assert len(seq)==60 and seq==seq[:6]*10 and A==[0]*3
 else:assert len(seq)==1

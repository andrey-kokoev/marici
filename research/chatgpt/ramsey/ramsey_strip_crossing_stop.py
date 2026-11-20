"""Test first crossing exhaustion along every prefix, not just at endpoint. Count visits to moving folded positions (including A,D for the literal poles)."""
from collections import Counter
from ramsey_strip_cut_flux import V,E,N,col
hist=Counter();events=Counter();examples={}
def visit(p,s,t,cut,first=None):
    i=len(p);remain=V-set(p)
    if first is None and not any(set(e)<=remain for e in cut):first=i
    if p[-1]==t:
        hist[i,first]+=1
        if i==12 and s=='A' and t=='D':examples.setdefault('long route',p)
        return
    if i==10:
        events[first is not None]+=1
        if s=='A' and t=='D' and first is not None:examples.setdefault('not at exit',p)
    for v in N[p[-1]]&remain:visit(p+(v,),s,t,cut,first)
for s in 'AC':
    for t in 'BD':
        cut=[(x,y) for x,y in E if (col(x) in (s,t))!=(col(y) in (s,t))];assert len(cut)==4;visit((s,),s,t,cut)
print('finished length / first exhaustion:',hist,'ten visits before exit, crosses exhausted?',events,'example',examples);assert sum(hist.values())==96

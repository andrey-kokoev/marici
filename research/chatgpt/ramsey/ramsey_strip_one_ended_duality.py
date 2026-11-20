"""Generate literal routes from one end with no Hall closure or destination-port constraint. When does the paired-prefix duality become identifiable from only information already visited? Count candidate images by grouping all completions of the current prefix."""
from collections import Counter
from ramsey_strip_ordered_boundary_dualities import solutions,s,t,r,entry
from ramsey_strip_local_stitch import N
routes=[]
def grow(p,used):
    if len(p)==12:
        if p[-1]==t:routes.append(tuple(p))
        return
    for v in N[p[-1]]-used:
        if (r[v]==v)!=(len(p)==11) or (len(p)==11 and v!=t):continue
        grow(p+[v],used|{v,r[v]})
grow([s,entry[0]],{s,*entry});assert len(routes)==10
chosen={}
for p in routes:
    k,=[k for k,f in enumerate(solutions) if all(f[p[i]]==p[-1-i] for i in (1,2))];chosen[p]=k
order=lambda k:2 if solutions[k][solutions[k][entry[0]]]==entry[0] else 4
for port in [False,True]:
    hist=Counter();horder=Counter()
    for p in routes:
        def poss(i):return {chosen[q] for q in routes if q[:i+1]==p[:i+1] and (not port or q[-2]==p[-2])}
        hist[min(i for i in range(11) if len(poss(i))==1)]+=1;horder[min(i for i in range(11) if len(set(map(order,poss(i))))==1)]+=1
    print('exit port given',port,'first unique exchange',sorted(hist.items()),'first unique order',sorted(horder.items()))
for x in sorted({p[2] for p in routes}):
 print('visit 2',x,'witnesses:',[(p,order(chosen[p])) for p in sorted(q for q in routes if q[2]==x)][:5])

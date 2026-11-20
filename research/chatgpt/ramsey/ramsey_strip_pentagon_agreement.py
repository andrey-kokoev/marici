"""Normal forms under rotation of five labels (sixth fixed). Reduce the exact-four test to nine relative positions of a two-transposition swap, for either witness type. Count fixed agreements and exchanged pairs separately."""
from ramsey_strip_witness_orbits import orbits,acts,transform,D,M,Counter
rot=next((a,b) for p,a,b in acts if p==(1,2,3,4,0,5));adj={p:(a,b) for p,a,b in acts};forms={}
for k in (1,2):
 u=min((u for u,n in orbits.items() if n==k and transform(u,*rot)==u),key=lambda u:tuple(sorted(u)));forms[k]=u;print('type',k,'generating incidences',[(D[i],M[dict(u)[i]]) for i in [D.index(d) for d in [(0,5),(0,1),(0,2)]]]);assert sum(transform(u,a,b)==u for p,a,b in acts)==5
# Canonicalize relative positions of the swap by rotating the pentagon.
def conj(p,i):
 def shift(x,k):return (x+k)%5 if x<5 else 5
 return tuple(shift(p[shift(x,-i)],i) for x in range(6))
swaps=[p for p in adj if sum(i!=v for i,v in enumerate(p))==4 and all(p[p[i]]==i for i in range(6))];reps=sorted({min(conj(p,i) for i in range(5)) for p in swaps});assert len(reps)==9
for p in reps:
 a,b=adj[p];pairs=[(i,p[i]) for i in range(6) if i<p[i]];counts=[]
 for k,u in forms.items():
    shared=u&transform(u,a,b);f=sum(a[x]==x for x,y in shared);m=(len(shared)-f)//2;assert f+2*m==len(shared);counts.append((f,m));assert not(k==2 and f==2 and m==1)
 print('swap',pairs,'(fixed, paired)',counts)

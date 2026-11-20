"""Use the two literal BR|NN pairings as involutions ON COLUMNS, not the separate convention cycling four edge roles. Check the round trip and test the older edge half-step against all four endpoint dualities."""
from ramsey_strip_ordered_boundary_dualities import entry,exit,solutions,rows,r
from ramsey_strip_seed_half_swap import h,action
V=range(4);identity=tuple(V);comp=lambda a,b:tuple(a[b[i]] for i in V)
def opposite(row):
 p=list(V);b=row.index('B');u=row.index('R');a,c=[i for i,v in enumerate(row) if v=='N'];p[b],p[u]=u,b;p[a],p[c]=c,a;return tuple(p)
a,b=map(opposite,rows);B=rows[0].index('B');U,Vv=[w.index('R') for w in rows];Q,=set(V)-{B,U,Vv}
def swap(i,j):
 z=list(V);z[i],z[j]=j,i;return tuple(z)
g=swap(U,Vv);neutral=swap(B,Q);trip=comp(b,a);assert trip==comp(a,b)==comp(neutral,g)!=g and comp(neutral,trip)==g;assert g not in {identity,a,b,trip}
edge_step=action(h);report=[]
for f in solutions:
    assert all(f[edge_step[i]]==edge_step[f[i]] for i in range(30));report.append((exit.index(f[entry[0]]),entry.index(f[exit[0]])))
print('column product',tuple(i+1 for i in trip),'desired swap',tuple(i+1 for i in g),'compatible endpoint shift pairs',sorted(report))

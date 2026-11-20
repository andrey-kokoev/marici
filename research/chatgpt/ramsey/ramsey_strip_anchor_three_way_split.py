"""Read the three same-frame completions at the single hub-to-anchor duad. Use coordinates normalized so retained generator has step one and anchor has coordinate zero."""
from ramsey_strip_cyclic_matching_eight_states import signatures,hub,P,T,c,ring
for a in range(1,5):
 anchor=ring[0];d=P.index(tuple(sorted((hub,anchor))));normalize=lambda x:(c[x]*pow(a,-1,5))%5
 rows=[]
 for key in ((a,),tuple(sorted((a,2*a%5))),tuple(sorted((a,3*a%5)))):
    m=signatures[key];j,=[j for i,j in m if i==d];finite=sorted(tuple(sorted(normalize(x) for x in p)) for p in T[j-15] if hub not in p);rows.append((key,finite))
 print('retained generator',a,'hub-anchor completion patterns',rows)
 assert rows[1][1]==rows[2][1]!=rows[0][1]
 other=ring[(2*a)%5];d2=P.index(tuple(sorted((anchor,other))))
 detail=[]
 for key in (tuple(sorted((a,2*a%5))),tuple(sorted((a,3*a%5)))):
    m=signatures[key];j,=[j for i,j in m if i==d2];block,=[p for p in T[j-15] if hub in p];z,=set(block)-{hub};detail.append(normalize(z))
 print('two enlargements: hub partner at selected pair {0,2}',detail);assert detail==[4,3]

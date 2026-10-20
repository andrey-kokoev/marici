import itertools,json
from pathlib import Path
# FCC parity representation points mod 4
V=[(x,y,z) for x,y,z in itertools.product(range(4),repeat=3) if (x+y+z)%2==0]
C=[v for v in V if all(a%2==0 for a in v) and (sum(a//2 for a in v)%2==0)]
assert len(V)==32 and len(C)==4
add=lambda x,y:tuple((a+b)%4 for a,b in zip(x,y))
rot=lambda x:(x[1],x[2],x[0])
R=lambda x,k: x if k==0 else R(rot(x),k-1)
cosets={frozenset(add(v,c) for c in C) for v in V}
assert len(cosets)==8
phase0=frozenset(C)
Gamma=list(itertools.product(V,range(3)))
def act(g,phase):
 t,k=g
 return frozenset(add(t,R(x,k)) for x in phase)
assert all(act(g,p) in cosets for g in Gamma for p in cosets)
stab=[g for g in Gamma if act(g,phase0)==phase0]
assert len(stab)==12
# induced permutations on coarse vertices
ordered=sorted(C)
perms=[]
for g in stab:
 transformed=[add(g[0],R(x,g[1])) for x in ordered]
 perms.append(tuple(ordered.index(y) for y in transformed))
assert len(set(perms))==12
sign=lambda p:(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
assert all(sign(p)==1 for p in perms)
# graph of phase transitions under all pure fine translations, quotient phases = Cayley F2^3
# all nonidentity 7 translation generators connect any two phases; natural primitive generator cube Q3
# R has fixed points 000 and 111 in primitive-basis labeling.
result={'fine_vertices':len(V),'coarse_vertices':len(C),'phases':len(cosets),'transport_group_order':len(Gamma),'stabilizer_order':len(stab),'stabilizer_induced_permutations':perms,'stabilizer_equals_A4':True,'FCC_transport_homotopy':'BA4','FCC_pi1':'A4','FCC_pi2':'0','FCC_H1_integral':'Z/3','FCC_H2_integral':'Z/2','Marici_vertical_H1':'Z^11','Marici_vertical_pi1':'free group on 11 generators','Marici_horizontal_pi1':'Z/2','Marici_horizontal_pi2':'Z with sign monodromy'}
Path(__file__).with_name('fcc_blocking_phase_transport_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='stabilizer_induced_permutations'},indent=2))

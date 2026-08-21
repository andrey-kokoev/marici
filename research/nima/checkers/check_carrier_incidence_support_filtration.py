"""Exact incidence-filtration precursor to a causal cone on the pentagon."""
import json
from pathlib import Path

n=5
verts=range(n)
dist=lambda i,j:min((i-j)%n,(j-i)%n)

balls={d:{i:{j for j in verts if dist(i,j)<=d} for i in verts}
       for d in range(3)}

autos=[(eps,a) for eps in (1,-1) for a in verts]
naturality=True
for eps,a in autos:
    f=lambda i:(eps*i+a)%n
    for d in balls:
        for i in verts:
            if {f(j) for j in balls[d][i]} != balls[d][f(i)]:
                naturality=False
assert naturality

composition=[]
for m in range(3):
  for ell in range(3):
    target=min(2,m+ell)
    ok=True
    for i in verts:
      composed=set()
      for j in balls[m][i]:
        composed |= balls[ell][j]
      ok &= composed <= balls[target][i]
    composition.append({"m":m,"ell":ell,"target":target,"bounded":ok})
assert all(x["bounded"] for x in composition)

reflection=lambda i:(-i)%n
orientation_swapped=(reflection(1)==4 and reflection(4)==1)
assert orientation_swapped

result={
 "schema":"marici.carrier-incidence-support-filtration.v1",
 "carrier_proxy":"pentagon incidence graph (rank-two associahedral cell)",
 "balls":{str(d):{str(i):sorted(js) for i,js in layer.items()} for d,layer in balls.items()},
 "checks":{
   "dihedral_naturality":naturality,
   "composition_subadditivity":all(x["bounded"] for x in composition),
   "reflection_swaps_oriented_neighbors":orientation_swapped,
 },
 "composition":composition,
 "verdict":(
   "Incidence adjacency canonically supplies a finite, automorphism-natural "
   "support filtration with subadditive composition depth. It does not supply "
   "a future/past orientation: a Carrier reflection preserves every support "
   "ball while reversing the two local directions."
 )
}
out=Path(__file__).parents[1]/"results"/"carrier_incidence_support_filtration.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

"""Generic first logarithmic differential for the C4 seven-mark weight page."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-seven-mark-weight-page.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-seven-mark-first-differential.json"


def rank(m):
    if not m or not m[0]: return 0
    a=[[Fraction(x) for x in row] for row in m];r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r


def deck_point_map(m):
    edges=list(itertools.combinations(range(m),2))
    triples=list(itertools.combinations(range(m),3))
    epos={e:i for i,e in enumerate(edges)}
    # Two rows per triple.  Each pair curve restricts diagonally to the two
    # deck points, with the standard triangle-boundary sign.
    matrix=[[0]*len(edges) for _ in range(2*len(triples))]
    for ti,t in enumerate(triples):
        faces=[(t[1],t[2]),(t[0],t[2]),(t[0],t[1])]
        signs=[1,-1,1]
        for face,sgn in zip(faces,signs):
            for sheet in (0,1): matrix[2*ti+sheet][epos[face]]=sgn
    r=rank(matrix)
    invariant_coker=len(triples)-r
    anti_coker=len(triples)
    assert r==(m-1)*(m-2)//2
    return {"geometric_marks":m,"pair_columns":len(edges),"triple_base_points":len(triples),"deck_point_rows":2*len(triples),"differential_rank":r,"invariant_cokernel_rank":invariant_coker,"anti_invariant_cokernel_rank":anti_coker,"total_W6_E2_rank":2*len(triples)-r}


source=json.loads(SOURCE.read_text())
maps={m:deck_point_map(m) for m in (5,6)}
profiles=[]
for p in source["profile_census"]:
    m=p["geometric_marks"]; q=maps[m]
    profiles.append({**p,"W3_E2":20,"W4_E2":p["W4"],"W5_E2":p["W5"],"W6_E2":q["total_W6_E2_rank"],"W6_deck_plus":q["invariant_cokernel_rank"],"W6_deck_minus":q["anti_invariant_cokernel_rank"]})

packet={
 "schema":"marici.benincasa.four_site_qg_seven_mark_first_differential.v1",
 "surface_primitive_to_pair_degree":"zero because every E7/A1^3 primitive class is orthogonal to the anticanonical pair curve",
 "surface_H1_to_pair_H1":"zero because degree-two del Pezzo and its rational A1 contractions have H1=0",
 "pair_H1_to_triple_H1":"zero because a point has H1=0",
 "pair_H0_to_triple_H0":"signed simplex incidence followed by diagonal deck map 1->(1,1)",
 "deck_point_maps":maps,
 "E2_profile_census":profiles,
 "warning":"Generic normal-crossing/branch-avoiding locus only; collision-supported differentials are not included.",
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"maps":maps,"profiles":[{"m":p["geometric_marks"],"W":(p["W3_E2"],p["W4_E2"],p["W5_E2"],p["W6_E2"]),"terms":p["term_count"]} for p in profiles]}))

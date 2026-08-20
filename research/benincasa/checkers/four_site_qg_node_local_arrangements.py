"""Local marked-hyperplane matroids at the seven supported C4 node occurrences."""
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-node-marked-incidence.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-node-local-arrangements.json"


def facets(n=4):
    out = {}
    for length in range(1, n):
        for start in range(n):
            sites = {(start + k) % n for k in range(length)}
            q = [0] * (2*n)
            for i in sites: q[i] = 1
            for e in range(n):
                if ((e in sites) != (((e+1)%n) in sites)): q[n+e] = 1
            out["g_"+"".join(str(i+1) for i in sorted(sites))] = q
    for e in range(n):
        q=[1]*n+[0]*n; q[n+e]=2
        out[f"G_minus_e{e+1}{(e+1)%n+1}"]=q
    return out


def rank(rows):
    if not rows: return 0
    a=[[Fraction(x) for x in row] for row in rows]
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r


def canonical(v):
    g=0
    for x in v: g=math.gcd(g,abs(x))
    v=tuple(x//g for x in v)
    first=next(x for x in v if x)
    return tuple(-x for x in v) if first<0 else v


def rowspace_key(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    r=0
    for c in range(3):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return tuple(tuple(str(x) for x in row) for row in a[:r])


def os_betti(normals):
    normals=sorted(set(normals)); n=len(normals); r=rank(normals)
    if r<2: return [1,n]
    flats=Counter(rowspace_key([a,b]) for a,b in itertools.combinations(normals,2) if rank([a,b])==2)
    # Recover number of distinct hyperplanes in each rank-two flat.
    mu2=[]
    for key in flats:
        basis=[[Fraction(x) for x in row] for row in key]
        m=sum(rank(basis+[list(v)])==2 for v in normals)
        mu2.append(m-1)
    betti=[1,n,sum(mu2)]
    if r==3:
        mu3=-(1-n+sum(mu2))
        betti.append(abs(mu3))
    return betti


source=json.loads(SOURCE.read_text())
forms=facets()
records=[]; signatures=Counter()
for term in source["records"]:
    for node in term["nodes"]:
        if node["depth"]==0: continue
        point=node["point"]
        # In chart y1=1, tangent coordinates are y2,y3,y4.  Since each
        # vanishing form has zero value at the point, its affine differential
        # is represented by the last three edge coefficients.
        occurrence_normals=[tuple(forms[label][5:8]) for label in node["vanishing_labels"]]
        geometric=[canonical(v) for v in occurrence_normals]
        distinct=sorted(set(geometric))
        betti=os_betti(distinct)
        signature=(node["depth"],len(distinct),rank(distinct),tuple(betti))
        signatures[signature]+=1
        records.append({"term_index":term["term_index"],"point":point,"labels":node["vanishing_labels"],"occurrence_depth":node["depth"],"distinct_normals":distinct,"rank":rank(distinct),"os_betti":betti})

assert len(records)==196
packet={
 "schema":"marici.benincasa.four_site_qg_node_local_arrangements.v1",
 "supported_occurrence_count":len(records),
 "signature_census":[{"occurrence_depth":k[0],"distinct_hyperplanes":k[1],"arrangement_rank":k[2],"os_betti":list(k[3]),"count":v} for k,v in sorted(signatures.items())],
 "hodge_classification":"all local complements are rational hyperplane arrangements and hence mixed Tate",
 "records":records,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"occurrences":len(records),"signatures":len(signatures),"census":packet["signature_census"]}))

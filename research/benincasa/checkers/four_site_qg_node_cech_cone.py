"""Signed occurrence-resolved Cech cone for the seven marked C4 nodes."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-node-marked-incidence.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-node-cech-cone.json"


def rank(m):
    if not m or not m[0]: return 0
    a=[[Fraction(x) for x in row] for row in m]
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


def matmul(a,b):
    if not a or not b: return []
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def boundary(k,j):
    """Columns are oriented j-simplices; rows are (j-1)-simplices."""
    high=list(itertools.combinations(range(k),j+1))
    low=list(itertools.combinations(range(k),j))
    pos={s:i for i,s in enumerate(low)}
    m=[[0]*len(high) for _ in low]
    for c,s in enumerate(high):
        for i in range(len(s)):
            face=s[:i]+s[i+1:]
            m[pos[face]][c]=(-1)**i
    return m,high,low


source=json.loads(SOURCE.read_text())
term_packets=[]
for term in source["records"]:
    nodes=[row for row in term["nodes"] if row["depth"]]
    assert len(nodes)==7
    maxj=max(row["depth"]-1 for row in nodes)
    bases={j:[] for j in range(maxj+1)}
    for ni,row in enumerate(nodes):
        labels=sorted(row["vanishing_labels"])
        for j in range(len(labels)):
            for subset in itertools.combinations(range(len(labels)),j+1):
                bases[j].append((ni,labels,subset))

    differentials={}
    # d_j: C_j -> C_(j-1), j>=1.
    for j in range(1,maxj+1):
        rowpos={(ni,tuple(labels),subset):i for i,(ni,labels,subset) in enumerate(bases[j-1])}
        m=[[0]*len(bases[j]) for _ in bases[j-1]]
        for c,(ni,labels,subset) in enumerate(bases[j]):
            for i in range(len(subset)):
                face=subset[:i]+subset[i+1:]
                m[rowpos[(ni,tuple(labels),face)]][c]=(-1)**i
        differentials[j]=m

    # d_0: occurrence vertices -> V_van in the seven nonpositive-node basis.
    d0=[[0]*len(bases[0]) for _ in range(7)]
    for c,(ni,labels,subset) in enumerate(bases[0]): d0[ni][c]=1
    differentials[0]=d0

    # Verify d^2=0 and exactness in every degree, including V in degree -1.
    for j in range(1,maxj+1):
        prod=matmul(differentials[j-1],differentials[j])
        assert all(x==0 for row in prod for x in row)
    dims={-1:7,**{j:len(bases[j]) for j in bases}}
    ranks={j:rank(m) for j,m in differentials.items()}
    homology={}
    homology[-1]=dims[-1]-ranks[0]
    for j in range(maxj+1):
        outgoing=ranks[j]
        incoming=ranks.get(j+1,0)
        homology[j]=dims[j]-outgoing-incoming
    assert all(v==0 for v in homology.values())
    term_packets.append({"term_index":term["term_index"],"dimensions":{str(k):v for k,v in dims.items()},"differential_ranks":{str(k):v for k,v in ranks.items()},"homology":{str(k):v for k,v in homology.items()},"orientation":"lexicographic source-label order with standard alternating deletion signs"})

packet={
 "schema":"marici.benincasa.four_site_qg_node_cech_cone.v1",
 "term_count":len(term_packets),
 "all_terms_acyclic":True,
 "occurrence_duplicates_retained":True,
 "orientation_convention":"lexicographic source-label order; deleting position i contributes (-1)^i",
 "global_target":"V_van in the seven nonpositive-node basis",
 "term_packets":term_packets,
 "conclusion":"The signed occurrence-resolved node Cech cone is acyclic for every source term.",
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"terms":len(term_packets),"acyclic":True,"max_degree":max(max(map(int,p["homology"].keys())) for p in term_packets)}))

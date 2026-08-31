import json
from fractions import Fraction as Q
from pathlib import Path

labels=(1,2,3,5)
ell={1:Q(0),2:Q(2),3:Q(5),5:Q(9)}
pairs=[(n,m) for n in labels for m in labels]

def rank(rows):
    a=[list(map(Q,row)) for row in rows]
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

def sd(n,m): return ell[n]+ell[m],ell[n]-ell[m]
# Rows are mixed moments S^j D^k, columns are ordered-pair atoms. Degrees
# through 2N-2 contain the transformed tensor-Vandermonde monomials.
max_degree=2*len(labels)-2
joint=[[sd(n,m)[0]**j*sd(n,m)[1]**k for n,m in pairs]
       for j in range(max_degree+1) for k in range(max_degree+1-j)]
product=[[sd(n,m)[0]**j for n,m in pairs] for j in range(16)]
ratio=[[sd(n,m)[1]**k for n,m in pairs] for k in range(16)]
# The invertible linear coordinate change (S,D)<->(2 ell_n,2 ell_m)
# identifies joint evaluation with a tensor product of two Vandermonde maps.
vander=[[ell[n]**j for n in labels] for j in range(4)]
checks={
 "label_vandermonde_is_full_rank":rank(vander)==4,
 "joint_product_ratio_moments_have_full_pair_rank":rank(joint)==16,
 "product_moments_alone_are_not_faithful":rank(product)<16,
 "ratio_moments_alone_are_not_faithful":rank(ratio)<16,
 "product_ratio_coordinates_recover_ordered_labels":all(((sd(n,m)[0]+sd(n,m)[1])/2==ell[n] and (sd(n,m)[0]-sd(n,m)[1])/2==ell[m]) for n,m in pairs),
}
base=Path(__file__).parents[2]
source=(base/"nima"/"theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md").read_text(encoding="utf-8")
flat=(base/"nima"/"theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md").read_text(encoding="utf-8")
checks.update({
 "source_requires_product_and_ratio_degrees":"product degree and ratio degree" in source,
 "source_forbids_flat_sector_identification_without_intertwiner":"They cannot be identified without a source-derived bonding map" in flat,
})
result={
 "schema":"marici.strominger.rh_finite_pair_joint_flatness_no_go.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":[
  "research/nima/theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md",
  "research/nima/theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md",
  "research/strominger/results/rh_polarized_pair_joint_jet_square_audit.json"],
 "verdict":"Joint product-ratio moments separate every finite ordered-pair packet. For N distinct labels, mixed moments through total degree 2N-2 contain, after the invertible coordinate change S=x+y and D=x-y, the tensor product of two full-rank Vandermonde evaluations. Hence a finite packet flat for every joint jet is zero. Product-only and ratio-only moments are individually nonfaithful. Any nonzero joint-flat state detected by a boundary current must therefore belong to a genuine completion and cannot be obtained by enlarging a finite cutoff.",
 "checks":checks,
 "label_count":len(labels),"pair_count":len(pairs),
 "joint_rank":rank(joint),"product_only_rank":rank(product),"ratio_only_rank":rank(ratio),
 "gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=Path(__file__).parents[1]/"results"/"rh_finite_pair_joint_flatness_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

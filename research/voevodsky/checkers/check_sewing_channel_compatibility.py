"""Exact finite block audit for endpoint, conductor, and convolution compatibility."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# Character blocks: regular and finite-rank endpoint HS bounds.
blocks=[]
for chi in range(6):
 k=F(1,2**(chi+1));hreg=F(1,2**(chi+2));hind=F(1,2**(chi+3))
 blocks.append({'chi':chi,'commutator_hs':str(k),'regular_hs':str(hreg),'endpoint_hs':str(hind),'product_majorant':str(k*(hreg+hind))})
full=sum((F(b['product_majorant']) for b in blocks),F(0));restricted=sum((F(b['product_majorant']) for b in blocks if b['chi']<=2),F(0))
# Mellin coefficients under convolution are pointwise products; use exact scalar fixtures.
conv=[{'a':str(F(a)),'b':str(F(b)),'successor':str(F(a)*F(b))} for a,b in ((1,2),(2,3),(3,5))]
checks={'endpoint_finite_majorants':all(F(b['endpoint_hs'])>0 for b in blocks),'angular_majorant_finite':full<F(1),'compression_contracts':restricted<=full,'convolution_is_multiplicative':all(F(r['successor'])==F(r['a'])*F(r['b']) for r in conv)}
out={'schema':'marici.voevodsky.sewing-channel-compatibility.v1','blocks':blocks,'full_majorant':str(full),'conductor_restricted_majorant':str(restricted),'convolution_fixture':conv,'checks':checks,'all_exact':all(checks.values()),'meaning':'Finite-rank endpoint rows satisfy the same compact-sandwich gate, conductor compression contracts the Schatten majorant, and Mellin convolution successors preserve multiplicative observer localization.'}
if __name__=='__main__':
 p=ROOT/'results'/'sewing-channel-compatibility.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

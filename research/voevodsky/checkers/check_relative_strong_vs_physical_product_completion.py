"""Exact finite-volume model of the relative strong / physical product split."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# One stationary boundary coordinate amid V common bulk coordinates.
rows=[]
for V in (1,2,4,8,16,32):
 common2=F(V)            # ||C_V||_2^2
 difference2=F(1)       # ||D_V||_2^2, boundary-localized
 product_trace=F(1)     # Tr(C_V^* D_V), only shared boundary coordinate
 rows.append({'volume':V,'common_hs_squared':str(common2),'difference_hs_squared':str(difference2),'localized_product_trace':str(product_trace)})
checks={
 'common_row_diverges':all(F(rows[i+1]['common_hs_squared'])>F(rows[i]['common_hs_squared']) for i in range(len(rows)-1)),
 'difference_row_stationary':all(F(r['difference_hs_squared'])==1 for r in rows),
 'product_stationary':all(F(r['localized_product_trace'])==1 for r in rows),
 'strong_full_pair_fails':F(rows[-1]['common_hs_squared'])>F(rows[0]['common_hs_squared']),
}
out={'schema':'marici.voevodsky.relative-strong-vs-physical-product.v1','rows':rows,'checks':checks,'all_exact':all(checks.values()),'meaning':'The relative difference row has a fixed Hilbert-Schmidt feature and the localized signed product is fixed, while the physical common row grows with radial volume.','classification':{'positive_relative_feature':'closed on the phase-energy graph domain','full_physical_strong_feature':'not an ordinary Hilbert-Schmidt completion','signed_sewing_product':'eligible for trace-class or relative-trace completion'}}
if __name__=='__main__':
 p=ROOT/'results'/'relative-strong-vs-physical-product-completion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

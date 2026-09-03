"""Show that labelled residue incidence does not determine amplitude normalization."""
import json
from fractions import Fraction
# Minimal compatible pair of labelled divisors and their ordered codimension-two incidence.
labels=('q_g12','q_g23'); incidence={(labels[0],labels[1]):1}
base={'q_g12':Fraction(2,3),'q_g23':Fraction(5,7),'q_g12,q_g23':Fraction(10,21)}
rows=[]
for scale in (Fraction(1,2),Fraction(1),Fraction(3)):
 scaled={k:scale*v for k,v in base.items()}
 rows.append({'scale':str(scale),'incidence':[[*k,v] for k,v in incidence.items()],'coefficients':{k:str(v) for k,v in scaled.items()}})
assert all(r['incidence']==rows[0]['incidence'] for r in rows)
assert len({r['coefficients']['q_g12'] for r in rows})==3
print(json.dumps({'schema':'marici.nima.residue-incidence-normalization-no-go.v1','status':'passed','bold_conjecture':'labelled residue incidence determines the normalized lower-graph amplitude','incidence_unchanged_under_common_rescaling':True,'normalized_coefficients_change':True,'disposition':'falsified','residual_conjecture':'a source-normalized total-energy residue map is required in addition to labelled incidence and residue coherence'},sort_keys=True))

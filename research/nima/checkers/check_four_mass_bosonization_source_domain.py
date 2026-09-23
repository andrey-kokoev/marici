"""Audit source-defined superamplitude extraction against positive real Z data."""
import json
from pathlib import Path
from math import prod
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
paper=ROOT/'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex'
text=paper.read_text(encoding='utf-8');anchor=text.index(r'\section{The Superamplitude}')
source=text[anchor:anchor+5900]
assert r'Y \to Y_0' in source
assert r'\phi^A_1 \cdot' in source and r'\eta_{1 A}' in source
assert r'\int d^{\cal N} \phi_1' in source
assert r'\delta^{4k}(Y;Y_0)' in source
assert r'\omega_{n,k}(Y_0;Z_a)' in source
# For k=2,N=4 the sourced external datum is (z_a,phi_1 dot eta_a,
# phi_2 dot eta_a). Products of positive-degree Grassmann generators
# have ZERO ordinary scalar body; every six-column body matrix has rank<=4.
Z=s.Matrix([[j**p for p in range(6)] for j in range(1,10)])
assert Z.shape==(9,6) and Z.rank()==6
first_six=s.Matrix([[j**p for p in range(6)] for j in range(1,7)])
minor=first_six.det();vandermonde=prod(j-i for i in range(1,7) for j in range(i+1,7))
assert minor==vandermonde==34560
bosonized_body=s.Matrix([[j**p for p in range(4)]+[0,0] for j in range(1,10)])
assert bosonized_body.rank()==4
assert bosonized_body[:6,:].det()==0
retained=[0,1,3,4,5,6,7,8]
assert Z[retained,:].rank()==6 and bosonized_body[retained,:].rank()==4
assert 8-Z[retained,:].rank()==2 and 8-bosonized_body[retained,:].rank()==4
# At the source Y0 the observed plane consists of the TWO bottom basis
# rows. Every body-level C*Z_body has vanishing bottom entries, so the
# source-fibre equation has NO body solution at Y0.
Y0=s.zeros(2,6);Y0[0,4]=1;Y0[1,5]=1
assert bosonized_body[:,4:]==s.zeros(9,2)
assert Y0[:,4:]!=s.zeros(2,2)
assert bosonized_body[:4,:4].det()!=0
# Every invertible GL6 frame preserves nonvanishing of a maximal minor
# up to det(GL6); no change of frame (including Y to Y0) can turn
# this strictly positive numerical carrier into the source nilpotent body.
G=s.diag(2,3,5,7,11,13)
assert (first_six*G).det()==minor*G.det()!=0
# Deliberate negative control: discarding last two real moment coordinates
# destroys the positive six-bracket and is not a same-data comparison.
assert Z[:6,:4].row_join(s.zeros(6,2)).det()==0
report={'schema':'marici.nima.four-mass-bosonization-domain-gate.v1','passed':True,
 'primary_source':'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex, section The Superamplitude',
 'source_map':'M_(n,2)=integral d^4 phi_1 d^4 phi_2 of omega_(n,2)(Y0; (z,phi_1 dot eta,phi_2 dot eta))',
 'moment_curve_six_bracket_first_six':str(minor),
 'bosonized_external_body_rank_max':4,
 'positive_numerical_external_rank':6,
 'retained_eight_source_kernel_dimensions':{'positive_real':2,'bosonized_body':4},
 'source_Y0_body_has_no_CZ_lift':True,
 'frame_independent_body_obstruction':True,
 'claim_boundary':'No literal same-external-point identification between the strictly positive ordinary real Z6 target-form coefficient and a sourced fermion component. A GLOBAL rational target-form identity may be pulled to the nilpotent locus only after regularity/normalization and the stated Berezin extraction are proved. This does not refute either standalone form.'}
(OUT/'four-mass-bosonization-domain-gate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_six_bracket':int(minor),
 'bosonized_body_six_bracket':0,'pointwise_component_to_density_comparison':False},indent=2))

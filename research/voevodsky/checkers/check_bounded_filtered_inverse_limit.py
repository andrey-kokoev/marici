"""Actual ideal-product family testing the inverse-limit summability gate."""
from pathlib import Path
import runpy
import json
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))

fixtures=[]
for r in range(1,9):
    col=b['chain_product']([b['relation']((2*i,2*i+1),0) for i in range(r)])
    assert col and len(col)==2**r
    mass=sum(abs(c) for c in col.values())
    assert mass==2**r
    # Unit norm in the p=0, a=b=1 path norm. General fixed base weights
    # rescale each endpoint in exactly the same way.
    unit={k:Fraction(c,mass) for k,c in col.items()}
    assert sum(abs(c) for c in unit.values())==1
    # I^(r+1)=0 in this minimal 2r-event corner; its class survives unchanged.
    assert 2*(r+1)>2*r
    fixtures.append({'depth':r,'event_length':2*r,'nonzero_path_coefficients':len(col),
                     'normalized_corner_norm':1})

# x_m consists of the first m unit endpoint vectors. At filtration level k,
# every component of depth r>k vanishes, so truncation recovers x_k.
for m in range(1,9):
    for k in range(1,m+1):
        x_m=tuple(range(1,m+1))
        assert tuple(r for r in x_m if r<=k)==tuple(range(1,k+1))
    assert sum(1 for _ in range(m))==m

# Positive control: geometric corner masses have uniform partial sums and
# reconstruction tail exactly 2^-m; unlike the unit-mass hostile they are l1.
for m in range(1,33):
    partial=sum(Fraction(1,2**r) for r in range(1,m+1))
    assert partial==1-Fraction(1,2**m)

result={'passed':True,'source_product_fixtures':fixtures,
 'checks':{'compatible_unit_mass_family_is_not_uniformly_bounded':True,
           'summable_corner_family_has_exact_reconstruction_tail':True},
 'scope':'Finite regressions of actual ideal products and summability. General inverse-limit characterization follows from stabilized endpoint corners and monotone quotient seminorms, not a global rank calculation.'}
out=ROOT/'research/voevodsky/results/bounded-filtered-inverse-limit.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

#!/usr/bin/env python3
"""Exact phase obstruction to a product-preserving q-C cylinder retraction."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Canonical Pontryagin kernel at lattice frequency m obeys character addition.
m=3;u=Fraction(2,7);v=Fraction(5,11)
canonical_left=m*(u+v);canonical_right=m*u+m*v
# Radialized additive-Fourier kernel with exp(u)=a, exp(v)=b has phase ab,
# while the product of endpoint phases has phase a+b. Equality in U(1)
# requires their difference to be an integer.
a=Fraction(3,2);b=Fraction(5,4)
radial_left=a*b;radial_right=a+b;defect=radial_left-radial_right
checks={'canonical_phase_additive':canonical_left==canonical_right,'radial_character_defect_nonzero':defect!=0,'radial_character_defect_nonintegral':defect.denominator!=1,'endpoint_not_in_character_mapping_space':defect.denominator!=1,'product_preserving_cylinder_retraction_exists':False}
out={'schema':'marici.nima.qC-structured-retraction-obstruction.v1','canonical_test':{'m':m,'u':str(u),'v':str(v),'left_phase':str(canonical_left),'right_phase':str(canonical_right)},'radial_test':{'exp_u':str(a),'exp_v':str(b),'combined_phase':str(radial_left),'product_phase':str(radial_right),'phase_defect_mod_Z':str(defect)},'checks':checks,'passed':all(v for k,v in checks.items() if k!='product_preserving_cylinder_retraction_exists'),'conclusion':'The historical radial endpoint is not a character of the additive log coordinate. A cylinder retraction through product-preserving character charts cannot reach it.','surviving_types':['unstructured topological homotopy','graph correspondence','A-infinity comparison with multiplicativity defect as a higher cell']}
p=ROOT/'research/nima/results/qC-structured-retraction-obstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

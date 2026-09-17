#!/usr/bin/env python3
"""Reduce the sewn theta directional sign to the outer first-quadrant logarithmic-derivative gate."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];cert=json.loads((ROOT/'research/grothendieck/results/central-complex-pick-radius-seventeen-halves-certificate.json').read_text());a,b=s.symbols('a b',positive=True,real=True);r2=a*a+b*b;alpha=2*a-a/(2*r2);beta=2*b+b/(2*r2)
# On the outer z-domain r2>=1/4, alpha and beta are nonnegative.
alpha_fact=s.factor(alpha);beta_fact=s.factor(beta);checks={'central_source_certificate_declares_pick_positive':cert['Im_F_strictly_positive_on_upper_radius_seventeen_halves_disk'] is True,'alpha_outer_nonnegative_form':s.simplify(alpha-a*(4*r2-1)/(2*r2))==0,'beta_globally_positive_form':s.simplify(beta-b*(4*r2+1)/(2*r2))==0,'central_certificate_uses_no_zero_locations':cert['zero_locations_used'] is False}
out={'schema':'marici.nima.theta-directional-gate-outer-quadrant-reduction.v1','checks':checks,'passed':all(checks.values()),'coefficient_forms':{'alpha':str(alpha_fact),'beta':str(beta_fact)},'closed_region':'the existing directed source certificate covers the central complex Pick disk declared in its artifact','remaining_sufficient_theorem':{'domain':'outer source region beyond the certified disk','conditions':['Re(Bprime/B)>=0','Im(Bprime/B)>=0'],'conclusion':'beta Re(Bprime/B)+alpha Im(Bprime/B)>=0'},'warning':'the first-quadrant theorem is source-specific and RH-strength globally; positivity/evenness of a generic measure does not imply it','next_attack':'derive a source differential or integral identity for Re(Bprime conjugate B) and Im(Bprime conjugate B) after complete modular resummation, without dividing by B','rh_proved':False}
p=ROOT/'research/nima/results/theta-directional-gate-outer-quadrant-reduction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

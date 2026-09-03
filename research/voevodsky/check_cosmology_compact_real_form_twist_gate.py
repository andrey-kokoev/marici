"""Test whether a Cayley transform gives a source-natural contour on the fixed torus."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_compact_real_form_twist_gate.json'
def cayley(x,sign=1):
 i=complex(0,sign);return (x-i)/(x+i)
def main():
 for x in (-3,-1,0,2,7):assert abs(abs(cayley(x))-1)<1e-12
 # The two square-root choices invert the compact coordinate and reverse orientation.
 for x in (-2,-1,1,3):assert abs(cayley(x,-1)-1/cayley(x,1))<1e-12
 assert cayley(0)==-1 and abs(cayley(10**12)-1)<1e-10
 out={'schema':'marici.voevodsky.cosmology-compact-real-form-twist-gate.v1','status':'Cayley_twist_changes_boundary_pair_and_is_not_source_canonical','candidate':'z=(x-i)/(x+i) from the extended split real line to the unit circle','exact_properties':['x=0 maps to z=-1','x=infinity maps to z=1','choosing -i instead of i replaces z by z^-1 and reverses the circle orientation'],'fixed_open_obstruction':'The source open is G_m=P1 minus {0,infinity}. The Cayley map sends those omitted boundary points to {-1,1}, so it identifies the source with P1 minus {-1,1}, not with the fixed unit coordinate torus while preserving its boundary divisors.','automorphism_gate':'Algebraic automorphisms of G_m have form x -> a*x or a/x. No such automorphism maps all of R* onto S1. The Cayley map is a P1 automorphism that changes the puncture pair.','orientation_gate':'The choices i and -i are conjugate and induce opposite generators. No DNC, incidence, or physical boundary datum selects one.','decision':'A Cayley transform constructs a compact presentation only by changing the marked boundary pair and choosing an orientation-reversing quadratic datum. It is not a canonical contour constructor for the fixed exceptional torus.','next_gate':'external-boundary-condition-contract: state the minimal additional physical data that would legitimately select a compact contour and period sign','limitations':['fixed-pair algebraic and real-form audit','does not forbid an external boundary condition from choosing the twist','no physical record map constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

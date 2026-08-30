#!/usr/bin/env python3
"""WP67: exact audit of the physical16-generated experimental probe algebra."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp67_experimental_probe_algebra.json"
def dag(x): return x.conjugate().T
def ckm(cd):
 s12,s13,s23=sp.Rational(1,5),sp.Rational(1,20),sp.Rational(1,4)
 c12,c13,c23=[sp.sqrt(1-s*s) for s in (s12,s13,s23)]; sd=sp.Rational(3,5); ep=cd+sp.I*sd; em=cd-sp.I*sd
 return sp.Matrix([[c12*c13,s12*c13,s13*em],[-s12*c23-c12*s23*s13*ep,c12*c23-s12*s23*s13*ep,s23*c13],[s12*s23-c12*c23*s13*ep,-c12*s23-s12*c23*s13*ep,c23*c13]])
def abs2(z): return sp.simplify(sp.expand_complex(z*sp.conjugate(z)))
def probes(hu,hd):
 c=hu*hd-hd*hu
 return [sp.trace(hu**k) for k in (1,2,3)]+[sp.trace(hd**k) for k in (1,2,3)]+[sp.trace((hu**a)*(hd**b)) for a,b in ((1,1),(2,1),(1,2),(2,2))]+[sp.det(c)]

def main():
 hu=sp.diag(1,4,9); dd=sp.diag(2,5,11); vp,vm=ckm(sp.Rational(4,5)),ckm(sp.Rational(-4,5)); hp=vp*dd*dag(vp); hm=vm*dd*dag(vm)
 pp,pm=map(lambda h:list(map(sp.simplify,probes(hu,h))),(hp,hm))
 q=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5),0],[-sp.Rational(4,5),sp.Rational(3,5),0],[0,0,1]])
 pq=list(map(sp.simplify,probes(q*hu*dag(q),q*hp*dag(q))))
 deck=json.loads((ROOT/"research/nima/results/flavor-probe-nerve-doublets.json").read_text())
 authority=json.loads((ROOT/"research/flavor/results/wp60_source_authority_inventory.json").read_text())
 gates={
  "invariant_word_generators_descend":pq==pp,
  "experimental_algebra_separates_measured10_hostile_pair":pp!=pm,
  "physical_readouts_identify_deck_presentations":deck["probe_matrices"]["physical_rank"]==1,
  "deck_odd_probe_is_outside_physical_algebra":deck["probe_matrices"]["full_probe_rank"]==2 and deck["probe_matrices"]["physical_rank"]==1,
  "source_declares_no_extra_reference_instrument":authority["explicit_absences"]["physical_reference_port"],
 }
 assert all(gates.values()),gates
 result={
  "schema":"marici.flavor.experimental-probe-algebra.v1",
  "typed_generator_data":"six ordered masses, nine CKM moduli, signed J (physical16)",
  "algebra":"all declared experimentally reconstructible functions of physical16; polynomial subalgebra represented by spectral powers, mixed Gram words, and a CP-odd commutator invariant",
  "contextual_equivalence":"generic equality of physical16; intentionally identifies weak-basis and deck-related presentations",
  "hostile_pair":"separated by the mixed-word generator family although measured10 collapses it",
  "descent":"yes under full weak-basis group",
  "proper_image":"not applicable: this is a readout algebra, not a state operation",
  "selector":False,"rigidifier":False,"instrument":"mass spectra, charged-current CKM amplitudes, and CP-odd measurements",
  "maximality_boundary":"maximal among instruments declared in the source; added flavor-reference or UV probes define new experiments",
  "conclusion":"The largest currently typed probe algebra is generically faithful on the quotient but cannot select a state; faithfulness and selection remain independent.",
  "gates":gates,
 }
 OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"generators":len(pp),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()

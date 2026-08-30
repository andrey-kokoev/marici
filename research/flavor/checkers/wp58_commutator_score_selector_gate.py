#!/usr/bin/env python3
"""WP58: exact positive commutator-score discriminator/selector typing."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp58_commutator_score_selector_gate.json"

def dag(a): return a.conjugate().T
def score(a,b):
    c=a*b-b*a
    return sp.simplify(sp.trace(dag(c)*c))

def main():
    hu=sp.diag(1,4,9)
    hd=sp.Matrix([[2,1+sp.I,0],[1-sp.I,5,2],[0,2,7]])
    q=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5),0],[-sp.Rational(4,5),sp.Rational(3,5),0],[0,0,1]])
    c=score(hu,hd)
    cq=score(q*hu*dag(q),q*hd*dag(q))
    spectral_sum=sp.simplify(2*sum((hu[i,i]-hu[j,j])**2*(hd[i,j]*sp.conjugate(hd[i,j]))
                                    for i in range(3) for j in range(i+1,3)))
    diagonal=sp.diag(2,5,7)
    gates={
      "score_is_full_weak_basis_invariant": sp.simplify(cq-c)==0,
      "score_equals_positive_spectral_sum": sp.simplify(c-spectral_sum)==0,
      "generic_mixing_score_is_strictly_positive": bool(c>0),
      "commuting_locus_score_is_zero": score(hu,diagonal)==0,
      "nondegenerate_zero_locus_is_commuting_locus": all(hu[i,i]!=hu[j,j] for i in range(3) for j in range(i+1,3)),
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.commutator-score-selector-gate.v1",
      "arithmetic":"exact SymPy Gaussian-rational matrix algebra",
      "functional":"C(Hu,Hd)=Tr([Hu,Hd]^dag[Hu,Hd])",
      "spectral_formula":"2 sum_{i<j}(u_i-u_j)^2 |(Hd)_ij|^2",
      "exact_example_score":str(c),
      "descent":"yes under full simultaneous U(3)_Q conjugation",
      "physical_instrument":"the scalar is reconstructible from masses and CKM data; no admitted dynamics extremizes it",
      "classification":{"discriminator":True,"selector_without_extra_law":False,"rigidifier":False,
                        "minimum_locus":"commuting Hu,Hd; experimentally excluded by mixing"},
      "smallest_exact_falsifier":"one nonzero off-diagonal Hd entry makes C>0; zero-selection predicts no physical mixing",
      "conclusion":"An invariant positive score can be instrumented as a readout without becoming a selector; extremization is the missing unauthorized arrow.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()

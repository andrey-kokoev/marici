#!/usr/bin/env python3
"""WP66: exact inventory of canonical positive quotient structures."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp66_positive_channel_inventory.json"
def dag(x): return x.conjugate().T
def hs(a,b): return sp.simplify(sp.trace(dag(a)*b))
def center(x): return sp.simplify(sp.trace(x)/x.rows*sp.eye(x.rows))

def main():
    hu=sp.diag(1,4,9); hd=sp.Matrix([[2,1+sp.I,0],[1-sp.I,5,2],[0,2,7]])
    words=[sp.eye(3),hu,hd]
    gram=sp.Matrix([[hs(a,b) for b in words] for a in words])
    q=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5),0],[-sp.Rational(4,5),sp.Rational(3,5),0],[0,0,1]])
    wordsq=[q*w*dag(q) for w in words]
    gramq=sp.Matrix([[hs(a,b) for b in wordsq] for a in wordsq])
    center_cov=sp.simplify(center(q*hd*dag(q))-q*center(hd)*dag(q))
    center_idem=sp.simplify(center(center(hd))-center(hd))
    dep54=json.loads((ROOT/"research/flavor/results/wp54_spectral_conditional_expectation.json").read_text())
    dep58=json.loads((ROOT/"research/flavor/results/wp58_commutator_score_selector_gate.json").read_text())
    gates={
      "word_gram_matrix_is_positive_definite_on_example":all(x>0 for x in [gram[:k,:k].det() for k in range(1,4)]),
      "word_gram_matrix_is_full_quotient_invariant":gramq==gram,
      "center_expectation_is_covariant":center_cov==sp.zeros(3),
      "center_expectation_is_idempotent":center_idem==sp.zeros(3),
      "center_image_is_proper":center(hd)!=hd,
      "spectral_pinching_dependency_passes":all(dep54["gates"].values()),
      "commutator_score_dependency_passes":all(dep58["gates"].values()),
    }
    gates={k:bool(v) for k,v in gates.items()}
    assert all(gates.values()),gates
    rows={
      "word_gram_pairing":{"descends":True,"proper_image":False,"source_authorized":True,"instrumented_readout":True,"ensemble_survives":True,"type":"separator/readout"},
      "commutator_score":{"descends":True,"proper_image":False,"source_authorized":True,"instrumented_readout":True,"ensemble_survives":True,"type":"separator/readout"},
      "hu_spectral_pinching":{"descends":True,"proper_image":True,"source_authorized":False,"instrumented_readout":False,"ensemble_survives":False,"type":"mathematical_channel"},
      "center_expectation":{"descends":True,"proper_image":True,"source_authorized":False,"instrumented_readout":False,"ensemble_survives":False,"type":"mathematical_channel"},
    }
    result={
      "schema":"marici.flavor.positive-channel-inventory.v1",
      "arithmetic":"exact Gaussian-rational matrix algebra",
      "candidates":rows,
      "word_gram_determinant":str(gram.det()),
      "classification":"positive pairings are instrumented quotient readouts without proper images; canonical expectations have proper images but no source dynamics/instrument and false fixed loci",
      "smallest_exact_falsifiers":{"pinching":"one nonzero mixing entry","center":"one nondegenerate mass splitting"},
      "conclusion":"No canonical positive structure simultaneously supplies proper reduction, physical authorization, and ensemble survival.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"candidates":len(rows),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()

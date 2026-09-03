"""Audit readouts factoring through a face-filled, class-killing comparison."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_nonfaithful_readout_audit.json'
def matvec(a,x):return [sum(Fraction(v)*Fraction(w) for v,w in zip(r,x)) for r in a]
def main():
 # Quotient q from edge chains to H1 of the filled simplex is the zero map.
 sigma=[1,1,1];q=[[0,0,0]];assert matvec(q,sigma)==[0]
 # Every linear record map r after q annihilates sigma.
 for coefficient in (-3,-1,0,1,5):
  record=[[coefficient]];assert matvec(record,matvec(q,sigma))==[0]
 # Deliberate comparator: the faithful old coordinate detects sigma.
 faithful=[[1,0,0]];assert matvec(faithful,sigma)==[1]
 out={'schema':'marici.voevodsky.cosmology-nonfaithful-readout-audit.v1','status':'every_filled_factor_readout_annihilates_the_required_class','source_class':'the nonzero regulator/triangle class represented by (Xi_log,-sigma123)','factorization':'old triangle -> face-filled complex -> record object','universal_result':'Because the first arrow kills sigma123 in homology, every homological, regulator-compatible, or state-effect readout factoring through it also sends the class to zero.','faithfulness_test':'The old edge coordinate detects sigma123, while every filled-factor coordinate returns zero. Thus the comparison loses exactly the capability the proposed readout must preserve.','physical_gate':'No source, effect, positive pairing, or record map has been supplied that bypasses the class-killing factorization. A chain-level noninvariant number would not be a readout of the cohomology class or a horn boundary.','decision':'Nonfaithful higher-dimensional correspondences cannot yield the requested nonzero boundary readout. They may encode unrelated records, but no such record bears on Xi_log or sigma123 without a new independently sourced map that does not factor through the filled quotient.','next_gate':'freeze the characteristic-zero horn frontier: separate the proved sourced obstruction from all constructor classes eliminated or still logically open','limitations':['factorization no-go applies to readouts of the primitive cohomology class','does not classify unrelated observables on the higher-dimensional source','no physical record map was present to test'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

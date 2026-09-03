#!/usr/bin/env python3
"""Test available degree-two cancellation channels for the tau_p pair cell."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa/results';N=ROOT/'research/nima/results'
rel=json.loads((N/'cosmology_p_normal_relative_residue_cocycle.json').read_text());cech=json.loads((B/'cosmology_principal_wall_partial_fraction_cech_gate.json').read_text())
D=rel['relative_differential'];tau=cech['p_partial_fraction_pair_vector'];c=[row[0] for row in D];assert c==[1,-1,1] and [row[1] for row in D]==[-x for x in c]
# im(D)=span(c). Cancellation requires lambda*c=-tau.
ratios=[]
for ci,ti in zip(c,tau):ratios.append(Fraction(-ti,ci))
assert ratios==[Fraction(-1),Fraction(-1),Fraction(1)]
# A 2x2 minor of [c|-tau] certifies rank augmentation.
minor=c[0]*(-tau[2])-c[2]*(-tau[0]);assert minor==2
out={'schema':'marici.benincasa.cosmology-tau-p-total-bidegree-cancellation.v1','problem':'can any known degree-two source in the minimal relative residue complex cancel the tau_p pair component?','bold_conjecture':'a combination of Xi_log and minus_sigma123 has differential -tau_p','rivals':['the two known columns span the needed cancellation','their image is only the circuit line and tau_p lies outside it','an additional source-derived degree-two generator enlarges the image'],'risky_consequences':'the componentwise scalar required to identify -tau_p with the circuit vector must be constant','strongest_falsification_attempt':{'relative_differential':D,'image_generator':c,'negative_tau_p':[-x for x in tau],'required_componentwise_scalars':[str(x) for x in ratios],'rank_augmenting_minor':minor},'exact_residual':'the required scalars are (-1,-1,1), and the rank-augmenting minor is 2; -tau_p is outside the one-dimensional image of the known degree-two differential','conjecture_disposition':'falsified in the minimal relative residue complex','surviving_scope':'Xi_log and minus_sigma123 cancel only the closed circuit vector; they cannot cancel tau_p','first_missing_typed_object':'an additional source-derived total-degree-two generator whose pair differential has a component transverse to (1,-1,1)','acceptance_test':'derive the generator and verify its full differential, D squared zero, and exact tau_p cancellation','passed':True};(B/'cosmology_tau_p_total_bidegree_cancellation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

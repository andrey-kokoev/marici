#!/usr/bin/env python3
"""NET1: calibrate four-way branch probabilities from admitted resolution evidence."""
import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2];O=('++','+-','-+','--')
records=[
 ('VA1','--','research/conjecture_replay/results/VA1_executability_audit.json'),
 ('VA2','+-','research/voevodsky/results/noncorner_logarithmic_valg_channel.json'),
 ('mixed_log_Betti','--','research/voevodsky/results/mixed_log_physical_Betti_realization_audit.json'),
 ('VC1b','-+','research/benincasa/results/G12_VC1b_sparse_membership.json'),
 ('VC2b','--','research/benincasa/results/VC2b_overlap_differential_typing_audit.json'),
 ('VC2b0','++','research/benincasa/results/G12_char0_H1_presentation.json'),
 ('VC2b1','++','research/benincasa/results/G12_source_labelled_overlap_domain.json'),
 ('VC2b1a','++','research/benincasa/results/G12_coefficient_overlap_representatives.json'),
 ('VC2b2','-+','research/benincasa/results/G12_overlap_span_in_H1.json'),
 ('VC2e','++','research/benincasa/results/G12_polynomial_weighted_overlap_span.json')]
for _,_,p in records:assert (R/p).exists(),p
counts={o:sum(x[1]==o for x in records) for o in O};n=len(records);uniform={o:.25 for o in O};posterior={o:(counts[o]+1)/(n+4) for o in O};empirical={o:counts[o]/n for o in O}
def brier(prob,y):return sum((prob[o]-(o==y))**2 for o in O)
def logloss(prob,y):return -math.log(prob[y])
in_sample={'uniform_brier':sum(brier(uniform,y) for _,y,_ in records)/n,'posterior_brier':sum(brier(posterior,y) for _,y,_ in records)/n,'uniform_log_loss':sum(logloss(uniform,y) for _,y,_ in records)/n,'posterior_log_loss':sum(logloss(posterior,y) for _,y,_ in records)/n}
loo=[]
for _,y,_ in records:
 train={o:counts[o]-(o==y) for o in O};prob={o:(train[o]+1)/(n-1+4) for o in O};loo.append((brier(prob,y),logloss(prob,y)))
heldout={'uniform_brier':in_sample['uniform_brier'],'laplace_LOO_brier':sum(x[0] for x in loo)/n,'uniform_log_loss':in_sample['uniform_log_loss'],'laplace_LOO_log_loss':sum(x[1] for x in loo)/n}
checks={'ten_evidence_records':n==10,'counts_sum':sum(counts.values())==n,'posterior_normalized':abs(sum(posterior.values())-1)<1e-12,'in_sample_improves_brier':in_sample['posterior_brier']<in_sample['uniform_brier'],'loo_does_not_improve_brier':heldout['laplace_LOO_brier']>=heldout['uniform_brier'],'loo_does_not_improve_logloss':heldout['laplace_LOO_log_loss']>=heldout['uniform_log_loss']};assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.branch-probability-calibration.v1','prospective_action':'NET1_calibrate_branch_probabilities','records':[{'action':a,'outcome':o,'evidence':p} for a,o,p in records],'counts':counts,'uniform_prior':uniform,'laplace_posterior':posterior,'in_sample_scores':in_sample,'leave_one_out_scores':heldout,'resolution':'+-','reason':'The aggregate Dirichlet model fits the observed sample better in-sample, but fails to improve leave-one-out Brier score or log loss. A fitted posterior exists; advertised reliability improvement is not established.','limitations':['only ten heterogeneous actions','outcomes are not exchangeable across action kinds','several records predate the event log','no independently frozen holdout sequence'],'implication':{'premise':'NET1 outcome +-','relation':'entails','conclusion':'aggregate_branch_posterior_fitted_but_not_validated'},'next':'Collect prospectively scored action-kind-stratified resolutions; compare hierarchical calibration against uniform on an immutable holdout.','checks':checks,'passed':True};d=R/'research/conjecture_replay/results/branch_probability_calibration.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'+-','counts':counts,'posterior':posterior,'LOO':heldout}))

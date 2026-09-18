#!/usr/bin/env python3
"""Tropical/log-sum-exp limit of the positive Pluecker construction law."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def lse(A,B,beta):
 M=max(A,B);return M+math.log(math.exp(beta*(A-M))+math.exp(beta*(B-M)))/beta
rows=[]
for beta in (1,2,4,8,16,32,64):
 samples=[]
 for A,B in ((0.,0.),(-1.,2.),(3.,-.5),(-4.,-2.)):
  F=lse(A,B,beta);samples.append({'A':A,'B':B,'soft_construction':F,'tropical_max':max(A,B),'defect':F-max(A,B),'bound_log2_over_beta':math.log(2)/beta})
 rows.append({'beta':beta,'samples':samples,'all_defects_bounded':all(-1e-15<=x['defect']<=x['bound_log2_over_beta']+1e-15 for x in samples)})
# Exact logarithmic Ptolemy check on ordered positive points.
x=(1.,2.,5.,9.);a,b,c,d=x;lhs=math.log((c-a)*(d-b));A=math.log((b-a)*(d-c));B=math.log((d-a)*(c-b));exact=abs(lhs-lse(A,B,1))<1e-14
checks={'logarithmic_plucker_is_logsumexp':exact,'softmax_error_uniformly_bounded':all(x['all_defects_bounded'] for x in rows),'tropical_limit_converges':max(s['defect'] for s in rows[-1]['samples'])<.011,'coherence_wall_retains_log2_over_beta':abs(rows[-1]['samples'][0]['defect']-math.log(2)/64)<1e-15}
out={'schema':'marici.nima.nnmhv-tropical-construction-bridge.v1','soft_law':'p_ac+p_bd = LSE(p_ab+p_cd, p_ad+p_bc)','deformation':'LSE_beta(A,B)=beta^-1 log(exp(beta A)+exp(beta B))','tropical_limit':'beta -> infinity gives max(A,B)','rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'Positive Pluecker addition is a finite-temperature coherent construction. Tropicalization selects the dominant resolution; mutation walls are equal-weight loci where both constructions survive.','bridges':['tropical positive Grassmannian','max-plus algebra','zero-temperature/statistical-mechanics limit','phylogenetic tree fans for tropical Gr(2,n)','classical winner-take-all shadow of coherent addition'],'claim_boundary':'The beta deformation is an analytic interpolation of the exchange law, not a physical temperature assignment derived from amplitudes.'};p=ROOT/'research/nima/results/nnmhv-tropical-construction-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'soft_law':out['soft_law'],'tropical_limit':out['tropical_limit'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)

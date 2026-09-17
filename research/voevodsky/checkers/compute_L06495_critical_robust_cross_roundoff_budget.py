#!/usr/bin/env python3
"""Range-compatible critical/robust cross-roundoff Schur budget."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];md=np.load(root/'physical_regularized_residual_gram_L06495_refined2_matrices.npz');M=md['lower_form'];ev,V=np.linalg.eigh((M+M.T)/2);vc=V[:,0];Vr=V[:,1:];G=md['output_gram'];crit_out=math.sqrt(max(0,float(vc@G@vc)));rob_out=math.sqrt(max(0,float(np.linalg.norm(Vr.T@G@Vr,2))));L=.6495;n=np.arange(1000);sc=np.sqrt((2*n+1)/(2*L));u=2**-53
def gamma(k):return k*u/(1-k*u)
# Evaluation errors from scaled coefficient l1 norms in critical and robust coordinates.
l1c=float(np.sum(abs((Z@vc)*sc)));l1r=float(np.max(np.sum(abs((Z@Vr)*sc[:,None]),axis=0)));qR=(digamma(.25+125j).real-math.log(math.pi))/2;prime=sum(math.log(p)/math.sqrt(p) for p in (2,3))/2;special=4096*u;ec=math.sqrt(2*L)*((abs(qR)+prime)*(gamma(6000)+special)*l1c+(gamma(24000)+special)*10);er=math.sqrt(2*L)*((abs(qR)+prime)*(gamma(6000)+special)*l1r+(gamma(24000)+special)*10);cross=ec*rob_out+er*crit_out+ec*er;beta=float(ev[1]);margin=float(ev[0]);correction=cross*cross/beta;out={'schema':'marici.voevodsky.L06495-critical-robust-cross-roundoff-budget.v1','critical_output_norm':crit_out,'robust_output_operator_norm':rob_out,'critical_scaled_l1':l1c,'maximum_robust_scaled_l1':l1r,'special_function_relative_reserve':special,'critical_output_error':ec,'robust_output_error':er,'cross_gram_error':cross,'robust_floor':beta,'cross_schur_correction':correction,'critical_margin':margin,'correction_to_margin_ratio':correction/margin,'passed':bool(correction<margin/10),'scope':'binary64 arithmetic model with 4096-ulp special-function reserve; implementation-level directed validation remains open','rh_proved':False};p=root/'L06495_critical_robust_cross_roundoff_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

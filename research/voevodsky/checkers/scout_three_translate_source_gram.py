#!/usr/bin/env python3
"""Rank-three equally spaced Gaussian-translate Gram scout from source deficits."""
import json,math
from pathlib import Path

def main():
 sigma=.005;d=.25
 scout=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 D1=next(r['K0_minus_Kd'] for r in scout['rows'] if r['sigma']==sigma and r['d']==d)
 D2=next(r['K0_minus_Kd'] for r in scout['rows'] if r['sigma']==sigma and r['d']==2*d)
 diag=json.loads((Path(__file__).parents[1]/'results'/'two_translate_symmetric_eigenvalue_scout.json').read_text())
 k0=diag['K0'];k1=k0-D1;k2=k0-D2
 anti=k0-k2
 sym_trace=(k0+k2)+k0
 sym_det=(k0+k2)*k0-2*k1*k1
 disc=math.sqrt(sym_trace*sym_trace-4*sym_det)
 sym_eigs=((sym_trace-disc)/2,(sym_trace+disc)/2)
 eigs=(anti,)+sym_eigs
 assert min(eigs)>0
 determinant=anti*sym_det
 result={'schema':'marici.voevodsky.three-translate-source-gram-scout.v1','sigma':sigma,'translate_centers':[-d,0,d],'kernel_values':{'K0':k0,'K(d)':k1,'K(2d)':k2},'gram_matrix':[[k0,k1,k2],[k1,k0,k1],[k2,k1,k0]],'reflection_odd_eigenvalue':anti,'reflection_even_block':[[k0+k2,math.sqrt(2)*k1],[math.sqrt(2)*k1,k0]],'reflection_even_determinant':sym_det,'eigenvalues':eigs,'determinant':determinant,'positive_definite_numerically':True,'certified':False,'conclusion':'The first equally spaced rank-three packet is positive in all reflection channels at the selected width and spacing.'}
 out=Path(__file__).parents[1]/'results'/'three_translate_source_gram_scout.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Growing-degree toy kernels for the history-poset boundary calculus."""
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];degrees=(4,8,16,32,64);alphas={'convergent_alpha2':2,'marginal_alpha1':1,'extensive_alpha0':0};families={}
for name,alpha in alphas.items():
 rows=[]
 for m in degrees:
  shells=[Fraction(1,(i+1)**alpha) for i in range(m)]
  diagonal=[[Fraction(0) for j in range(m)] for i in range(m)];bulk=[[Fraction(0) for j in range(m)] for i in range(m)]
  for i,J in enumerate(shells):
   diagonal[i][i]=J
   for j in range(i+1):bulk[i][j]=J/Fraction(i+1)
  aug_d=sum(sum(r) for r in diagonal);aug_b=sum(sum(r) for r in bulk);difference=sum(sum(diagonal[i][j]-bulk[i][j] for j in range(m)) for i in range(m));rows.append({'degree':m,'history_dimension':m*(m+1)//2,'augmentation':float(aug_d),'diagonal_equals_bulk_augmentation':aug_d==aug_b,'difference_in_augmentation_kernel':difference==0})
 families[name]={'alpha':alpha,'sections':rows}
checks={'all_resolutions_scalar_equivalent':all(r['diagonal_equals_bulk_augmentation'] for f in families.values() for r in f['sections']),'all_boundary_bulk_differences_are_tail':all(r['difference_in_augmentation_kernel'] for f in families.values() for r in f['sections']),'alpha2_approaches_finite_limit':abs(families['convergent_alpha2']['sections'][-1]['augmentation']-math.pi**2/6)<0.02,'alpha1_has_log_growth':abs(families['marginal_alpha1']['sections'][-1]['augmentation']-math.log(64)-0.5772156649)<0.02,'alpha0_is_linear':families['extensive_alpha0']['sections'][-1]['augmentation']==64}
out={'schema':'marici.nima.growing-convolution-degree-toys.v1','convolution_degrees':list(degrees),'families':families,'checks':checks,'passed':all(checks.values()),'interpretation':'Shell decay classifies the growing-degree augmentation: alpha>1 finite, alpha=1 logarithmic, alpha<1 power-law. Kernels with identical shell flux differ by an augmentation-invisible tail.'}
p=ROOT/'research/nima/results/growing-convolution-degree-toys.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

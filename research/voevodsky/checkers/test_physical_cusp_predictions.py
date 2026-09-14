#!/usr/bin/env python3
"""Independent algebraic and numerical tests of the cusp readout predictions."""
import cmath, json, math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
# 1. Numerical boundary values of the local logarithmic period model.
r=0.37; epsilons=[1e-2,1e-4,1e-6,1e-8]
ratios=[]
for eps in epsilons:
    upper=cmath.log(complex(-r,eps)); lower=cmath.log(complex(-r,-eps))
    ratios.append((upper-lower)/(2j*math.pi))
log_error=abs(ratios[-1]-1)
# 2. Exact cellular source of the coefficient.
D=[[-1,-1],[1,1]];pair=[1,1]
boundary=[sum(D[i][j]*pair[j] for j in range(2)) for i in range(2)]
half=[v//2 for v in boundary]
# 3. Exact monodromy winding and composition tests.
def T(k):return [[1,k,0],[0,1,0],[0,0,1]]
def mul(A,B):return [[sum(A[i][q]*B[q][j] for q in range(3)) for j in range(3)] for i in range(3)]
composition=all(mul(T(k),T(l))==T(k+l) for k in range(-4,5) for l in range(-4,5))
# 4. Picard target checks in diag(1,-1^7).
d=[3,-1,-1,-1,-1,-1,-1,-3];K=[-3,1,1,1,1,1,1,1]
dot=lambda u,v:u[0]*v[0]-sum(u[i]*v[i] for i in range(1,8))
checks={'log_boundary_ratio_converges_to_one':log_error<1e-7,'log_ratio_imaginary_error_small':abs(ratios[-1].imag)<1e-14,'paired_node_boundary_is_even':boundary==[-2,2],'half_boundary_is_primitive_component_difference':half==[-1,1],'monodromy_group_law':composition,'two_windings_zero_mod_two':T(2)[0][1]%2==0,'reverse_winding_odd_mod_two':T(-1)[0][1]%2==1,'v_alg_fixed_for_tested_windings':all(T(k)[2]==[0,0,1] and [T(k)[i][2] for i in range(3)]==[0,0,1] for k in range(-4,5)),'picard_target_square_minus_six':dot(d,d)==-6,'picard_target_K_orthogonal':dot(d,K)==0,'picard_target_primitive':math.gcd(*map(abs,d))==1}
assert all(checks.values()),{k:v for k,v in checks.items() if not v}
out={'schema':'marici.voevodsky.physical-cusp-prediction-tests.v1','numerical_log_test':{'radius':r,'epsilons':epsilons,'normalized_jump_ratios':[[z.real,z.imag] for z in ratios],'final_error':log_error},'cellular_test':{'boundary_matrix':D,'pair_boundary':boundary,'half_boundary':half},'monodromy_test':{'tested_windings':[-4,4],'group_law':composition,'T_1':T(1),'T_2':T(2),'T_minus_1':T(-1)},'picard_test':{'vector':d,'square':dot(d,d),'K_pairing':dot(d,K)},'coverage':{'local_logarithmic_jump':'tested numerically','integral_cellular_coefficient':'tested exactly','winding_predictions':'tested exactly','Picard_target':'tested exactly','source_current_specialization':'external comparison gate retained'},'checks':checks,'passed':True}
(R/'research/voevodsky/results/physical_cusp_prediction_tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'checks':len(checks),'log_ratios':out['numerical_log_test']['normalized_jump_ratios'],'coverage':out['coverage']}))

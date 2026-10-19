# /// script
# dependencies = ["sympy"]
# ///
"""Exact alternative-dynamics classification; no physical control selection."""
from contextlib import redirect_stdout
from dataclasses import replace
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys
import sympy as S
from hamiltonian_descent_wg import zero
from native_t9_hamiltonian_packet import rational
from interface_preserving_carrier_dynamics import classify, native_generator, retained_chart

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
NIMA=ROOT.parent/'nima'
OUT=ROOT/'results/interface-preserving-carrier-dynamics.json'
OUT.unlink(missing_ok=True)
# Classify from source actions and omitted edge BEFORE reading response values.
c=classify()
D=c['D']
e0=S.eye(12)[:,c['edges'].index('AB')]
if str(NIMA/'checkers') not in sys.path: sys.path.insert(0,str(NIMA/'checkers'))
with redirect_stdout(io.StringIO()):
    pinned=runpy.run_path(str(NIMA/'checkers/check_pinned_T9_software_contract.py'))
fixture=pinned['m']
transport=pinned['T9']
selected=tuple('ABCD'[i]+'ABCD'[j] for i,j in fixture['E'])
Ds,A=native_generator(c,selected)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)

check('pinned-software-suite-freshly-rerun',pinned['result']['verification_status']=='pass')
check('all24-source-actions-enumerated',len(c['raw'])==24)
check('skew-action-span-rank7',len(c['basis'])==7)
check('boundary-constraint-rank6',c['boundary'].rank()==6)
check('compatible-combination-space-is-one-line',len(c['nullspace'])==1)
check('primitive-generator-nonzero-rank2',D.rank()==2)
check('omitted-arrow-fixed',D*e0==S.zeros(12,1) and e0.T*D==S.zeros(1,12))
check('common-coefficient-fixed',D*S.ones(12,1)==S.zeros(12,1))
check('fixed-Gram-conserved',zero(D.T*(10*S.eye(12)+S.ones(12))+(10*S.eye(12)+S.ones(12))*D))
check('point-sector-stationary-under-same-combination',c['Dv']==S.zeros(4))
counts={'zero':0,'nonzero_blocked':0,'nonzero_compatible':0}
for i,raw in enumerate(c['raw']):
    if zero(raw): counts['zero']+=1
    elif zero(raw*e0): counts['nonzero_compatible']+=1
    else: counts['nonzero_blocked']+=1
    check(f'single-source-action-classified/{i}',zero(raw) or not zero(raw*e0))
check('single-skew-actions-cannot-give-nonzero-closure',counts=={'zero':10,'nonzero_blocked':14,'nonzero_compatible':0})
check('native137-coefficient-generator-rank38',A.shape==(137,137) and A.rank()==38)
check('native137-coefficient-generator-skew',A.T+A==S.zeros(137))
# Full160 two-leg field, restricted WITHOUT needing a missing preparation.
Af=S.SparseMatrix(S.diag(S.kronecker_product(D,S.eye(12))+S.kronecker_product(S.eye(12),D),S.zeros(16)))
native_indices=tuple(12*c['edges'].index(a)+c['edges'].index(b) for a in selected for b in selected)+tuple(range(144,160))
R=S.SparseMatrix(137,160,{(i,j):1 for i,j in enumerate(native_indices)})
check('actual-native-interface-closes-for-all-full-inputs',R*Af==A*R)
check('aggregate-J4-stationary',S.ones(1,137)*A==S.zeros(1,137))

F=S.Matrix([[v for r in row.value for v in r] for row in fixture['source']])
check('actual-fixture-leaf-values-move',not zero(A*F))
T,L,means,middle=retained_chart(fixture,pinned['output'])
B=S.SparseMatrix(T*A*L)
N=S.SparseMatrix(S.eye(T.rows)-T*L)
Gtarget=S.SparseMatrix(L.T*L+N.T*N)
Omega=A/2
K=A.T*A/2
Otarget=S.SparseMatrix(L.T*Omega*L)
Ktarget=S.SparseMatrix(L.T*K*L)
check('retained-T9-value-chart201-coordinates',T.shape==(201,137) and means.shape==(64,137))
check('retained-chart-left-inverse',L*T==S.eye(137))
check('full-native-T9-generator-intertwining',B*T==T*A)
check('target-generator-metric-conservative',B.T*Gtarget+Gtarget*B==S.zeros(201))
check('inherited-positive-metric-on-consistent-image',T.T*Gtarget*T==S.eye(137))
check('ambient-metric-positivity-by-reconstruction',T*L+N==S.eye(201) and N*T==S.zeros(201,137))
check('source-Hamiltonian-identity',A.T*Omega==K)
check('retained-target-Hamiltonian-identity',B.T*Otarget==Ktarget)
check('retained-target-energy-pullback',T.T*Ktarget*T==K)
check('outer-family-means-do-not-move',means*A==S.zeros(64,137))
check('nontrivial-native-energy-not-in-outer-means',A.rank()>0 and means*A==S.zeros(64,137))
# A full explicit energy-factorization hostile: choose a dynamical column in
# ker(means). It has zero outer means but positive quadratic Hamiltonian.
v=next(A[:,j] for j in range(137) if A[:,j]!=S.zeros(137,1))
check('equal-family-means-can-hide-positive-energy',means*v==S.zeros(64,1) and (v.T*K*v)[0]>0)
# Stronger hostile in the actual factored-leg family: change only X legs
# along an active, incoming-sum-zero direction, keeping every leg invertible.
leg_direction=next(Ds[:,j] for j in range(11) if Ds[:,j]!=S.zeros(11,1))
m=fixture['m']
changed_x=[m['add'](m['values'][f'ax{i}'],m['scale'](rational(leg_direction[i]/3),m['H'])) for i in range(11)]
changed=[m['mul'](m['values'][f'ay{j}'],changed_x[i]) for i in range(11) for j in range(11)]
changed += [row.value for row in fixture['source'][121:]]
Fhostile=S.Matrix([[v for r in matrix for v in r] for matrix in changed])
check('factored-hidden-energy-hostile-keeps-legs-invertible',all(S.Matrix(x).det()!=0 for x in changed_x))
check('factored-equal-family-means-different-energy',means*Fhostile==means*F
      and ((A*Fhostile).T*(A*Fhostile)).trace()!=((A*F).T*(A*F)).trace())

# Exact rational Cayley step on the one-frequency source plane. Its elapsed
# angular parameter is2 atan(sqrt32)/sqrt32; not calibrated physical time.
Q=(S.eye(11)-Ds).inv()*(S.eye(11)+Ds)
U=S.SparseMatrix(S.diag(S.kronecker_product(Q,Q),S.eye(16)))
check('source-plane-frequency-squared32',Ds**3+32*Ds==S.zeros(11))
check('rational-step-orthogonal',U.T*U==S.eye(137))
check('rational-step-same-generator',U*A==A*U)
Fnext=U*F
rows=[]
for row,values in zip(fixture['source'],Fnext.tolist()):
    values=tuple(rational(v) for v in values)
    rows.append(replace(row,value=(values[:2],values[2:])))
next_packet=transport(tuple(rows),fixture)
actual=S.Matrix([[v for r in row.value for v in r]
                 for row in next_packet.original+tuple(child for family in next_packet.final for child in family.members)+next_packet.final])
check('native-implementation-agrees-with-complete-value-chart',actual==T*Fnext)
check('nontrivial-step-changes-native-leaves',next_packet.original!=pinned['output'].original)
check('outer-family-values-stay-fixed',all(a.value==b.value for a,b in zip(next_packet.final,pinned['output'].final)))
check('original-J4-and-branch-readout-stay-fixed',next_packet.observe(fixture)==pinned['observed'])
check('source-energy-preserved',((A*Fnext).T*(A*Fnext)).trace()==((A*F).T*(A*F)).trace())
old={(a.label,b.label) for a in fixture['source'] for b in fixture['source'] if a.target==b.target}
new={(a.label,b.label) for family in next_packet.final for a in fixture['leaves']((family,)) for b in fixture['leaves']((family,))}
check('exact977-native-contexts-stay-fixed',old==new and len(new)==977)

# Do not substitute this alternative for the separate old four-mode rotor.
Ec=S.zeros(12,4)
for i,e in enumerate(('AD','CA','DB','BC')): Ec[c['edges'].index(e),i]=1
G=10*S.eye(12)+S.ones(12)
Pc=(Ec.T*G*Ec).inv()*Ec.T*G
Nc=S.eye(12)-Ec*Pc
cover_columns=S.Matrix.hstack(*(S.Matrix(48,1,list(Pc*b*Nc)) for b in c['basis']))
check('alternative-leaks-into-old-cover-projection',(Pc*D*Nc).rank()==2)
check('both-native-and-old-cover-constraints-force-zero',not S.Matrix.vstack(c['boundary'],cover_columns).nullspace())
result={
 'schema':'marici.strominger.interface-preserving-carrier-dynamics.v1','verification_status':'pass','checks':checks,
 'search_scope':'all S4 skew-action generators and their real linear span on twelve directed carrier arrows',
 'single_generator_counts':counts,'skew_span_dimension':7,'compatible_subspace_dimension':1,
 'basis_permutations':[c['group'][i] for i in c['pivots']],'primitive_coefficients':c['coefficients'],
 'source_arrow_order':c['edges'],'source_generator':[[str(v) for v in D.row(i)] for i in range(12)],
 'native_generator_rank':38,'point_generator_rank':0,'native_interface_closes':True,
 'extra23_slot_preparation_needed_for_native_future':False,
 'full_retained_T9_value_chart':{'ambient_coordinates':201,'independent_leaf_coordinates':137,
                               'intermediate_family_values':32,'final_family_values':32,'target_rule':'B=T A L'},
 'outer_family_mean_generator':'zero','energy_not_recoverable_from_outer_family_means':True,
 'old_four_mode_rotor_compatibility':False,
 'source_control_selection':'declared linear combination; no primitive or physical permission inferred',
 'clock':'Cayley step: supplied angular time2 atan(sqrt32)/sqrt32',
 'energy_normalization':'declared presymplectic coefficient energy ||A F||^2/4, not physical calibration',
 'Postnikov_identification':False,'physical_Hamiltonian_selection':False,
 'input_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                (Path(__file__),HERE/'interface_preserving_carrier_dynamics.py',NIMA/'checkers/check_pinned_T9_software_contract.py')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} interface-preserving carrier dynamics checks')
print('One nontrivial source-algebra line closes native137 dynamics; complete retained T9 intertwines.')
print('All activity is hidden from family means; old four-mode rotor and physical/Postnikov identifications do not follow.')

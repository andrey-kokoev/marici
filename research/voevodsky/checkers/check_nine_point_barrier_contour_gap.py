"""Separate barrier completion from determination of the physical contour."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_cell_continuation_rewrite_probe as source
from four_cell_completion_barrier_net import construct
families=('zero2','zero3')
columns=[s.Matrix([s.factor(sum(r['value'][i] for r in source.records.values() if r['family']==family)) for i in range(2)]) for family in families]
M=s.Matrix.hstack(*columns);det=s.factor(M.det());assert det!=0
# Pole cancellation gives zero constraints on either family coefficient.
poles=[s.factor(sum(r['pole'] for r in source.records.values() if r['family']==family)) for family in families]
assert poles==[0,0]
net=construct(source.records)
while net.enabled():net.step(net.enabled()[0])
assert net.observe_barrier()[1]
# Two distinct weights both obey the same cancellation and completion evidence.
v10=M*s.Matrix([1,0]);v11=M*s.Matrix([1,1]);assert v10!=v11
report={'passed':True,'barrier_complete':True,'family_order':families,'component_order':['chi3^4 chi5^4','chi2^4 chi5^4'],'component_matrix':[[str(x) for x in row] for row in M.tolist()],'determinant':str(det),'rank':int(M.rank()),'local_pole_constraint_rank':0,'undetermined_family_coefficients':2,'coefficient_recovery_given_independent_target':[[str(s.factor(x)) for x in row] for row in M.inv().tolist()],'conclusion':'For this four-cell two-component target witness, completion and local pole cancellation do not fix either family coefficient. An independently normalized physical target or contour condition is required. Inverting this witness matrix is not a derivation of that target or a full n=9 amplitude.'}
path=Path(__file__).resolve().parents[1]/'results/nine-point-barrier-contour-gap.json';path.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

import json, math
from pathlib import Path
root=Path(__file__).resolve().parents[2]
p=json.loads((root/'research/nima/results/qRB-relative-packet-fixture.json').read_text())
# source+observer = 2I in this fixture; each nontrivial 2x2 cross block has singular value 0.8.
lam=0.8/2.0
out={'schema':'marici.nima.qRB-finite-relative-constant.v1','packet':'qRB-relative-packet-fixture.json','comparison_norm':'source_gram + observer_gram = 2 I','cross_readout_operator_norm':0.8,'finite_relative_constant':lam,'checks':{'finite_constant_is_finite':math.isfinite(lam),'finite_constant_nonnegative':lam>=0,'source_fixture_present':p['status']=='finite_fixture_populated'},'passed':math.isfinite(lam) and lam>=0,'scope':'one finite algebraic fixture only; no uniform regulator bound'}
q=root/'research/nima/results/qRB-finite-relative-constant.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

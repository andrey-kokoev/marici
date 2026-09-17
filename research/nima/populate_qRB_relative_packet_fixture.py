import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
s=json.loads((root/'research/voevodsky/checkers/relative-c34-positive-dilation-v1.json').read_text())
out={'schema':'marici.nima.qRB-relative-packet.v1','status':'finite_fixture_populated','basis':['e1','e2'],'source_gram':s['matrices']['source_gram'],'observer_gram':s['matrices']['observer_gram'],'signed_cross_readout':s['matrices']['signed_cross_readout'],'refinement_maps':['identity finite rung'],'regulator_indices':{'L':'fixture','R':'finite','N':'finite','n':'0','F':'fixed'},'comparison_norm':'source_gram + observer_gram','endpoint_rows':[],'required_checks':['finite_source_gram_psd','finite_observer_gram_psd','cross_readout_trace_class','refinement_compatibility'],'uniform_constant':'not tested','source_fixture_checks':s['checks'],'rh_proved':False}
p=root/'research/nima/results/qRB-relative-packet-fixture.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

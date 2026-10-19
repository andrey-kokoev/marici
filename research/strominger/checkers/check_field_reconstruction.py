"""Exact, gated 137-label reconstruction; prior operator packet is the baseline."""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,json,hashlib,copy
from field_reconstruction import readout,reconstruct,positive_real
from field_metric_comparisons import project,pairing,rank
from field_refibration import EDGES
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_field_metric_dg_binding as prior
    import check_rung_automorphism_classification as classification
    import check_field_comparison_preparation as legacy
A,Z,O=prior.A,prior.Z,prior.O
K,P,Q=prior.K,prior.P,prior.Q
C=classification.C;ops={'P':P,'Q':Q,'C':C}
field=prior.field;reference=prior.reference
packet=readout(field,K,ops,reference,Z)
assert packet['P']==prior.refined(field)[0] and packet['Q']==prior.refined(field)[1]
# Explicitly isolate the additional cycle information, not just projector energy.
sector_changed=project(field,prior.group.add(prior.group.scale(prior.phase,P),Q),Z)
sector_packet=readout(sector_changed,K,ops,reference,Z)
assert packet['P']==sector_packet['P'] and packet['Q']==sector_packet['Q'] and packet['C']!=sector_packet['C']
phase_field={e:tuple(prior.phase*v for v in values) for e,values in field.items()}
assert readout(phase_field,K,ops,reference,Z)==packet

def proportional(decoded,original):
    y=decoded['representative'];rho=decoded['normalization_squared']
    edge,axis=next((e,i) for e in EDGES for i in range(3) if original[e][i]!=Z)
    scalar=y[edge][axis]/original[edge][axis]
    assert scalar.flip(8)*scalar==rho and positive_real(rho)
    assert all(y[e][i]==scalar*original[e][i] for e in EDGES for i in range(3))
    return y,rho

base=reconstruct(packet,K,ops,Z,O);y,rho=proportional(base,field)
assert base['reference_probe_ranks']=={'P':1,'Q':2}
assert reconstruct(readout(phase_field,K,ops,reference,Z),K,ops,Z,O)==base
proportional(reconstruct(sector_packet,K,ops,Z,O),sector_changed)
# Reconstruct with a different excluded reference; the mark is not data-fitted.
other_reference=(2,3)
proportional(reconstruct(readout(field,K,ops,other_reference,Z),K,ops,Z,O),field)
# Compare all 144 earlier operator blocks, not only 137 new scalar labels.
def native(values):
    flat=[values[tuple('ABCD'.index(c) for c in label.split(':')[0])]['xyz'.index(label.split(':')[1])] for label in prior.labels]
    return prior.apply(prior.s.B,flat)
old=legacy.prepare(native(field));old_y=legacy.prepare(native(y))
assert legacy.recover(old)==native(field)
for section in ('counted','reference'):
    for key,block in old[section].items():
        other=old_y[section][key]
        assert all(other.get(k,Z)==rho*block.get(k,Z) for k in set(block)|set(other))
# The two incoming reference-target probes are the reconstruction gate.
a,t=reference;probe_edges=tuple((b,t) for b in range(4) if b not in (a,t))
def scaled_probes(epsilon):
    return {edge:tuple(epsilon*v for v in values) if edge in probe_edges else values for edge,values in field.items()}
def phase_reference(values):
    return {edge:tuple(prior.phase*v for v in vector) if edge==reference else vector for edge,vector in values.items()}
def distance_squared(left,right):
    return sum(((left[name]['blocks'][branch][i][j]-right[name]['blocks'][branch][i][j]).flip(8)*(left[name]['blocks'][branch][i][j]-right[name]['blocks'][branch][i][j])
                for name in ops for branch,n in (('arrow',11),('state',4)) for i in range(n) for j in range(n)),Z)
profiles=[];baseline_signal=None
for epsilon in (O,A(F(1,10)),A(F(1,100))):
    values=scaled_probes(epsilon);measurement=readout(values,K,ops,reference,Z)
    decoded=reconstruct(measurement,K,ops,Z,O);proportional(decoded,values)
    signal=distance_squared(measurement,readout(phase_reference(values),K,ops,reference,Z))
    assert positive_real(signal)
    if baseline_signal is None:baseline_signal=signal
    assert signal==epsilon*epsilon*baseline_signal
    profiles.append({'epsilon':epsilon.record(),'squared_readout_difference':signal.record(),'reference_probe_ranks':decoded['reference_probe_ranks']})
# At zero the selected eleven fields still span C3, yet reference phase is lost.
blind=scaled_probes(Z);blind_other=phase_reference(blind)
assert rank(tuple(blind[e] for e in EDGES if e!=reference),Z)==3
blind_packet=readout(blind,K,ops,reference,Z)
assert blind_packet==readout(blind_other,K,ops,reference,Z) and blind!=blind_other
assert any(any(v!=Z for v in blind[e]) for e in EDGES if e!=reference)
try:reconstruct(blind_packet,K,ops,Z,O)
except ValueError as error:assert 'Reference probes do not span' in str(error)
else:raise AssertionError('Degenerate reference accepted')
# Fixed source metric; the ordinary anchored field difference stays constant.
field_signal=pairing(tuple((prior.phase-O)*v for v in field[reference]),tuple((prior.phase-O)*v for v in field[reference]),K,Z)
assert positive_real(field_signal)
# Malformed and inconsistent packets are not mistaken for valid reconstruction.
negative_controls=0
for mutation in ('missing','provenance','cycle','negative'):
    bad=copy.deepcopy(packet)
    if mutation=='missing':del bad['C']
    elif mutation=='provenance':bad['C']['reference']=(1,0)
    elif mutation=='cycle':
        matrix=[list(row) for row in bad['C']['blocks']['state']];matrix[0][0]+=O
        bad['C']['blocks']['state']=tuple(tuple(row) for row in matrix)
    else:
        for channel in bad.values():
            for branch,matrix in channel['blocks'].items():channel['blocks'][branch]=tuple(tuple(-x for x in row) for row in matrix)
    try:reconstruct(bad,K,ops,Z,O)
    except ValueError:negative_controls+=1
    else:raise AssertionError('Invalid packet accepted: '+mutation)
report={'schema':'marici.field-reconstruction.v1','status':'pass','slot_labels':137,'complex_scalar_channels_per_slot':3,
 'operators':['P','I-P','C'],'generic_domain':{'selected_span':3,'reference_probe_ranks':base['reference_probe_ranks']},
 'decoder':'Exact representative y and positive rho; y/sqrt(rho) reconstructs the field up to common phase',
 'cycle_separates_projector_invisible_change':True,'common_phase_remains_invisible':True,
 'prior_operator_blocks_reconstructed':144,'prior_counted_blocks':121,'prior_reference_blocks':23,
 'reference_choices_tested':[reference,other_reference],'invalid_packets_rejected':negative_controls,
 'degenerate_counterexample':{'selected_span':3,'same_all_411_values':True,'not_related_by_common_phase':True,'decoder_rejects':True},
 'stability':{'source_norm':'sum_e c_e* K3 c_e','tester_norm':'unweighted sum of squared moduli of the 411 complex coordinates; diagnostic choice, not source-selected instrument cost','fixed_anchored_field_difference_squared':field_signal.record(),'profiles':profiles,'readout_signal_scaling':'squared difference scales exactly as epsilon^2','uniform_inverse_bound_near_zero':False},
 'scope':'Conditional exact field reconstruction, not universal injectivity, minimum measurement count, physical instrument availability, or original 2x2 DG binding.',
 'prerequisite_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['readout_layers']['projector_cycle_reconstruction']
assert atlas['slot_labels']==137 and atlas['complex_scalar_channels_per_slot']==3
assert atlas['reference_probe_ranks_required']==base['reference_probe_ranks']
assert atlas['prior_operator_blocks_recovered']==144 and not atlas['universal_injectivity']
paths=[Path(__file__),Path(__file__).with_name('field_reconstruction.py'),Path(__file__).with_name('field_metric_comparisons.py'),Path(prior.__file__),atlas_path,ROOT/'research/strominger/field-reconstruction-v1.md',ROOT/'research/strominger/field-comparison-preparation-v1.md',Path(legacy.__file__),Path(classification.__file__)]
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/field-reconstruction';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))

"""Independent retained-field and numerical routes, including failure strata."""
from pathlib import Path
from fractions import Fraction as F
from dataclasses import replace
import contextlib,io,json,hashlib
from field_refibration import encode,EDGES
from reconstruction_aware_tower import (Context,field_rows,retain_field_families,observe_field_rows,make_packet,
    horizontal,vertical,semantic,verify,raw_rows,operator_packet,recover_operator_packet)
from field_reconstruction import positive_real
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_field_reconstruction as previous
prior=previous.prior;A,Z,O=previous.A,previous.Z,previous.O
owner=prior.adapter['diagram'];generator=prior.adapter['generated'];reference=previous.reference
matrix=lambda M:tuple(tuple(M.get((i,j),Z) for j in range(3)) for i in range(3))
source_files=[Path(previous.classification.__file__),Path(prior.group.s.__file__)]
context=Context(matrix(previous.K),tuple((name,matrix(op)) for name,op in previous.ops.items()),
                tuple(sorted(prior.s.B.items())),tuple((p.relative_to(ROOT).as_posix(),hashlib.sha256(p.read_bytes()).hexdigest()) for p in source_files),A(F(1,1000)))
weak=previous.scaled_probes(A(F(1,1000000)))
zero={edge:(Z,Z,Z) for edge in EDGES}
reference_only=dict(zero);reference_only[reference]=previous.field[reference]
fixtures={'spanning':previous.field,'weak-probes':weak,'blind-reference':previous.blind,'zero':zero,'reference-only':reference_only}
profiles=[];packets={};squares=0
for name,field in fixtures.items():
    retained=field_rows(encode(field,reference,generator))
    rows=observe_field_rows(retained,context,owner['Row'],owner['mean'],Z)
    for policy in ('inherited','common'):
        start=make_packet(rows,field,reference,context,policy,owner,Z,O)
        left11=vertical(start,owner);left10=vertical(left11,owner)
        right6=horizontal(start,owner);right5=vertical(right6,owner);right4=vertical(right5,owner)
        assert semantic(horizontal(left11,owner))==semantic(right5)
        lower=horizontal(left10,owner)
        assert semantic(lower)==semantic(right4) and lower.history!=right4.history
        # Independent field-family lift: retain actual paired occurrences before
        # evaluating them. It does NOT reconstruct them from numeric leaf values.
        retained1=retain_field_families(retained,1,policy)
        retained2=retain_field_families(retained1,2,policy)
        direct=observe_field_rows(retained2,context,owner['Row'],owner['mean'],Z)
        assert direct==raw_rows(right6,owner)
        assert owner['leaves'](direct)==rows
        for node in (start,left11,left10,right6,right5,right4):
            assert node.context==context and node.certificate==start.certificate and node.operator_fallback==start.operator_fallback
            assert owner['leaves'](raw_rows(node,owner))==rows
        data=verify(right4,context,owner,Z,O)
        assert data==previous.readout(field,previous.K,previous.ops,reference,Z)
        if start.operator_fallback:
            restored,rho=recover_operator_packet(start.operator_fallback,Z,O)
            previous.proportional({'representative':restored,'normalization_squared':rho},field) if field!=zero else None
            assert len(start.operator_fallback)==144
        status=start.certificate.status
        if name=='spanning':assert status=='reconstructible' and not start.operator_fallback
        elif name=='weak-probes':assert status=='reconstructible-weak-reference-probes' and start.operator_fallback
        else:assert status=='requires-retained-operator-data' and start.operator_fallback
        profiles.append({'fixture':name,'policy':policy,'status':status,'leaf_count':len(rows),'terminal_family_count':len(direct),
                         'fallback_blocks':len(start.operator_fallback),
                         'reference_margin_lower_squared':start.certificate.reference_margin_lower_squared.record() if start.certificate.reference_margin_lower_squared is not None else None,
                         'reference_margin_upper_squared':start.certificate.reference_margin_upper_squared.record() if start.certificate.reference_margin_upper_squared is not None else None})
        packets[name,policy]=right4;squares+=2
# A distinct pair of valid generic packets can have exactly the same terminal
# channel averages: relabel non-reference source vertices 2 and 3.
p=(0,1,3,2)
moved={tuple(p[i] for i in edge):v for edge,v in previous.field.items()}
moved_rows=observe_field_rows(field_rows(encode(moved,reference,generator)),context,owner['Row'],owner['mean'],Z)
original_rows=owner['leaves'](raw_rows(packets['spanning','common'],owner))
assert moved_rows!=original_rows and owner['mean'](moved_rows)==owner['mean'](original_rows)
# Blind-reference fields have identical scalar leaves but DIFFERENT explicit
# operator sidecars; the fallback preserves precisely the lost distinction.
blind_other=previous.blind_other
blind_rows=observe_field_rows(field_rows(encode(blind_other,reference,generator)),context,owner['Row'],owner['mean'],Z)
blind_original=owner['leaves'](raw_rows(packets['blind-reference','common'],owner))
assert blind_rows==blind_original
assert operator_packet(blind_other)!=packets['blind-reference','common'].operator_fallback
# Bounded corruption checks: each must fail the owning package validator.
base=packets['spanning','common'];fallback=packets['blind-reference','common']
def reject(packet,expected=context):
    try:verify(packet,expected,owner,Z,O)
    except (ValueError,AssertionError):return
    raise AssertionError('Corrupt transport packet accepted')
reject(replace(base,context=replace(context,coordinates='unrecorded-frame')))
reject(replace(base,certificate=replace(base.certificate,status='invented-stability')))
reject(replace(base,history=('G7',)))
reject(replace(fallback,operator_fallback=()))
reject(replace(fallback,operator_fallback=fallback.operator_fallback[:-1]))
reject(replace(fallback,operator_fallback=operator_packet(previous.field)))
view=dict(base.view);key=next(iter(view));family=view[key][0]
# Correct mean without retained members must not masquerade as a lossless row.
view[key]=(replace(family,members=()),)+view[key][1:]
reject(replace(base,view=view))
view=dict(base.view);key=next(iter(view));family=view[key][0]
view[key]=(replace(family,mass=family.mass+1),)+view[key][1:]
reject(replace(base,view=view))
report={'schema':'marici.reconstruction-aware-tower.v1','status':'pass','commuting_squares_checked':squares,
 'profiles':profiles,'independent_field_family_and_numeric_routes_agree':True,'all_137_leaves_preserved':True,
 'route_histories_remain_distinct':True,'average_only_collision':True,'fallback_distinguishes_scalar_collision':True,
 'negative_controls':8,'phase_reference':'not supplied; operator fallback also reconstructs only modulo common phase',
 'conditioning_scope':'Certified bounds for the four linear reference equations only; no whole-decoder stability claim',
 'placement_scope':'Retained-pair lift of the numerical transport diagram after field-slot preparation; not an identification of its rung numbers with native field presentation grades',
 'scope':'No new DG multiplication binding, physical instrument, calibration or reference d. Extra operator sidecars are explicit, not counted as 137 scalar values.',
 'prerequisite_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['readout_layers']['reconstruction_aware_transport']
assert atlas['leaf_labels']==137 and atlas['complex_channels_per_leaf']==3
assert atlas['retention_policies']==['inherited','common'] and not atlas['terminal_average_is_faithful']
paths=[Path(__file__),Path(__file__).with_name('reconstruction_aware_tower.py'),Path(__file__).with_name('field_reconstruction.py'),Path(__file__).with_name('field_refibration.py'),atlas_path,ROOT/'research/nima/checkers/check_rung_transport_diagram.py',ROOT/'research/strominger/reconstruction-aware-tower-v1.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/reconstruction-aware-tower';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))

"""Compile radar integration in private snapshots; never write owner interfaces."""
from pathlib import Path
import subprocess
import hashlib
import json
import os
import re
import sys
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[2]
tools=Path.home()/'tools/cubical-agda'
agda=tools/'agda-2.8.0/agda.exe'
work=root/'temp/native-radar-formal'
locations=[(root/'research/nima/agda',work/'owner'),(tools/'cubical-0.9',work/'cubical'),(root/'research/voevodsky/agda',work/'own')]
snapshot={};module_sources={};copied_targets={};checked_files=set()
for source,target in locations:
    for src in source.rglob('*'):
        if not src.is_file() or src.suffix not in ('.agda','.agda-lib'):continue
        dst=target/src.relative_to(source);data=src.read_bytes()
        dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists() or dst.read_bytes()!=data:dst.write_bytes(data)
        snapshot[str(src)]=hashlib.sha256(data).hexdigest()
        copied_targets[str(src)]=dst
        if src.suffix=='.agda':
            name='.'.join(src.relative_to(source).with_suffix('').parts)
            module_sources.setdefault(name,str(src))
args=[str(agda),'--transliterate','--no-libraries','--safe','--cubical','--guardedness','--no-import-sorts','-WnoUnsupportedIndexedMatch']
if '--fresh' in sys.argv:args+=['--ignore-interfaces']
for _,target in locations:args+=['-i',str(target)]
admission='--admission' in sys.argv
three_profile='--three-profile' in sys.argv
output_mode='--output' in sys.argv
structural='--structural' in sys.argv
overlap='--overlap' in sys.argv
retained_overlap='--retained-overlap' in sys.argv
observed_boundary='--observed-boundary' in sys.argv
profile_gate='--profile-gate' in sys.argv
action_charts='--action-charts' in sys.argv
typed_comparisons='--typed-comparisons' in sys.argv
retained_fibers='--retained-fibers' in sys.argv
native_profiles='--native-profiles' in sys.argv
profile_pullback='--profile-pullback' in sys.argv
clifford_profiles='--clifford-profiles' in sys.argv
phase_boundary='--phase-boundary' in sys.argv
three_profile='--three-profile' in sys.argv
comparison='--comparison' in sys.argv
negative_markers={'NativeRadarBadPort':'16 != 0','NativeRadarBadEvidence':'true != false',
    'RadarClockBadGrid':'32 != 28','RadarClockBadCausality':'23 != 25',
    'RadarClockBadEnclosure':'31 != 30','RadarClockBadCalibration':'16 != 32',
    'RadarClockBadBudget':'1719544332 != 0'}
modules=([('RadarClockPhysicalCertificates',False)]+[(m,True) for m in negative_markers]) if admission else [('NativeRadarReadout',False),('NativeRadarBadPort',True),('NativeRadarBadEvidence',True)]
if output_mode:
    negative_markers.update({'RadarOutputBadSquare':'1 != 0','RadarOutputBadOrientation':'1 != 0',
        'RadarOutputBadDelay':'1135910583808460207424026 != 906694364710971881029632'})
    modules=[('RadarOutputPhysicalCertificates',False)]+[(m,True) for m in negative_markers]
if structural:modules=[('ObservedCarrierSynthesis',False),('NativeRadarBadPort',True),('NativeRadarBadEvidence',True)]
if overlap:modules=[('SourceAnchoredTidalOverlap',False),('NativeRadarBadEvidence',True)]
if retained_overlap:
    negative_markers.update({'RetainedOverlapBadSource':'newtonian != rosen', 'RetainedOverlapBadGradient':'negsuc 143 of type'})
    modules=[('RetainedLocalTidalOverlap',False),('RetainedOverlapBadSource',True),('RetainedOverlapBadGradient',True)]
if observed_boundary:
    negative_markers.update({'RetainedOverlapBadSource':'newtonian != rosen', 'RetainedOverlapBadGradient':'negsuc 143 of type'})
    modules=[('ObservationRespectingBoundary',False),('RetainedOverlapBadSource',True),('RetainedOverlapBadGradient',True)]
if profile_gate:
    negative_markers.update({'ProfileGateBadConstant':'negsuc 143', 'RetainedOverlapBadGradient':'negsuc 143 of type'})
    modules=[('ProfileBoundNativeGate',False),('ProfileGateBadConstant',True),('RetainedOverlapBadGradient',True)]
if action_charts:
    negative_markers.update({'ActionChartBadPotential':'0 != 16', 'ActionChartBadSixth':'512 != 0'})
    modules=[('ActionChartComparison',False),('ActionChartBadPotential',True),('ActionChartBadSixth',True)]
if typed_comparisons:
    negative_markers.update({'ActionChartBadPotential':'0 != 16', 'ActionChartBadSixth':'512 != 0'})
    modules=[('TypedPhysicalComparisons',False),('ActionChartBadPotential',True),('ActionChartBadSixth',True)]
if retained_fibers:
    negative_markers.update({'ActionChartBadPotential':'0 != 16', 'ActionChartBadSixth':'512 != 0'})
    modules=[('RetainedObservationFibers',False),('ActionChartBadPotential',True),('ActionChartBadSixth',True)]
if native_profiles:
    negative_markers.update({'ActionChartBadPotential':'0 != 16', 'ActionChartBadSixth':'512 != 0'})
    modules=[('NativeRetainedProfiles',False),('ActionChartBadPotential',True),('ActionChartBadSixth',True)]
if profile_pullback:
    negative_markers.update({'ActionChartBadPotential':'0 != 16', 'ActionChartBadSixth':'512 != 0'})
    modules=[('NativeProfilePullback',False),('ActionChartBadPotential',True),('ActionChartBadSixth',True)]
if clifford_profiles:
    negative_markers.update({'CliffordBadLiftErasure':'Bool.false != Agda.Builtin.Bool.Bool.true', 'CliffordBadHistoryErasure':'unit != times'})
    modules=[('RetainedCliffordProfiles',False),('CliffordBadLiftErasure',True),('CliffordBadHistoryErasure',True)]
if phase_boundary:
    negative_markers.update({'PhaseSelectionBadUniqueness':'Bool.false != Agda.Builtin.Bool.Bool.true','CliffordBadHistoryErasure':'unit != times'})
    modules=[('PhaseAlgebraSelectionBoundary',False),('PhaseSelectionBadUniqueness',True),('CliffordBadHistoryErasure',True)]
if three_profile:
    negative_markers.update({'ThreeProfileBadIdentification':'true != false'})
    modules=[('ThreeProfileCoherence',False),('ThreeProfileBadIdentification',True)]
if comparison:
    negative_markers.update({'InterpretationComparisonBad':'!= false'})
    modules=[('InterpretationComparison',False),('InterpretationComparisonBad',True)]
results=[]
for module,negative in modules:
    command=[x for x in args if not (negative and x=='--ignore-interfaces')]
    result=subprocess.run(command+[str(work/'own'/f'{module}.agda')],cwd=work,capture_output=True,encoding='utf-8',errors='replace',timeout=600)
    log=root/'research/voevodsky'/f'{module}.log';log.write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    text=result.stdout+'\n'+result.stderr
    checked_files.update(str(Path(p).resolve()).casefold() for p in re.findall(r'\(([^)\n]+\.agda)\)',text))
    marker=negative_markers.get(module,'')
    accepted=result.returncode!=0 and '[UnequalTerms]' in text and 'expression refl' in text and marker in text if negative else result.returncode==0
    results.append(dict(module=module,exit_code=result.returncode,expected_rejection=negative,passed=accepted,log=str(log.relative_to(root))))
    print(text[-1800:].encode('ascii',errors='backslashreplace').decode('ascii'))
# Freshness is about the actual proof dependency closure, not every unrelated
# owner file copied for import resolution. Include both static import closure
# and compiler-reported checked paths; retain out-of-closure drift separately.
used={p for p in snapshot if Path(p).suffix=='.agda-lib'}
queue=[module_sources[m] for m,_ in modules]
queue += [p for p,dst in copied_targets.items() if str(dst.resolve()).casefold() in checked_files]
while queue:
    src=queue.pop()
    if src in used:continue
    used.add(src)
    text=copied_targets[src].read_text(encoding='utf-8')
    for name in re.findall(r'^\s*(?:open\s+)?import\s+([^\s;]+)',text,re.M):
        if name in module_sources:queue.append(module_sources[name])
changed=[src for src,digest in snapshot.items() if not Path(src).exists() or hashlib.sha256(Path(src).read_bytes()).hexdigest()!=digest]
unchanged=not any(src in used for src in changed)
proof_snapshot={p:snapshot[p] for p in sorted(used)}
out=dict(passed=all(r['passed'] for r in results) and unchanged,fresh='--fresh' in sys.argv,finished_utc=datetime.now(timezone.utc).isoformat(),results=results,
    admission_mode=admission,output_mode=output_mode,structural_mode=structural,overlap_mode=overlap,retained_overlap_mode=retained_overlap,observed_boundary_mode=observed_boundary,profile_gate_mode=profile_gate,action_charts_mode=action_charts,typed_comparisons_mode=typed_comparisons,retained_fibers_mode=retained_fibers,native_profiles_mode=native_profiles,profile_pullback_mode=profile_pullback,clifford_profiles_mode=clifford_profiles,phase_boundary_mode=phase_boundary,three_profile_mode=three_profile,comparison_mode=comparison,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),agda_sha256=hashlib.sha256(agda.read_bytes()).hexdigest(),
    original_sources_unchanged=unchanged,source_snapshot_hashes=proof_snapshot,
    freshness_scope='Transitive static imports of audited roots, compiler-reported checked files, and copied library configuration; unimported drift is not proof dependency drift.',
    copied_source_count=len(snapshot),out_of_closure_source_drift=[p for p in changed if p not in used],scope='Safe cubical formal finite integer numerator/package/retained-resolution comparison. Supplied admission and real normalization/continuum physics are separate obligations.')
receipt_name='source-anchored-overlap-formal.json' if overlap else ('observed-carrier-synthesis-formal.json' if structural else ('radar-output-enclosure-formal.json' if output_mode else ('radar-clock-admission-formal.json' if admission else 'native-radar-formal.json')))
if retained_overlap:receipt_name='retained-local-tidal-overlap-formal.json'
if observed_boundary:receipt_name='observation-respecting-boundary-formal.json'
if profile_gate:receipt_name='profile-bound-native-gate-formal.json'
if action_charts:receipt_name='action-chart-comparison-formal.json'
if typed_comparisons:receipt_name='typed-physical-comparisons-formal.json'
if retained_fibers:receipt_name='retained-observation-fibers-formal.json'
if native_profiles:receipt_name='native-retained-profiles-formal.json'
if profile_pullback:receipt_name='native-profile-pullback-formal.json'
if clifford_profiles:receipt_name='retained-clifford-profiles-formal.json'
if phase_boundary:receipt_name='phase-algebra-selection-boundary-formal.json'
if three_profile:receipt_name='three-profile-coherence-formal.json'
if comparison:receipt_name='interpretation-comparison-formal.json'
(root/'research/voevodsky'/receipt_name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('passed=',out['passed'],'fresh=',out['fresh'])
raise SystemExit(0 if out['passed'] else 1)

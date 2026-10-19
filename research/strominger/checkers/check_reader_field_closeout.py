"""Fresh closeout replay and immutable-by-content evidence snapshot."""
from pathlib import Path
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results';OUT=BASE/'reader-field-closeout';OUT.mkdir(exist_ok=True)
commands=[
 [sys.executable,'research/strominger/checkers/check_baryon_tensor_grid.py'],
 [sys.executable,'research/strominger/checkers/derive_tetrahedral_field_attachment.py'],
 [sys.executable,'research/strominger/checkers/derive_neutron_belt_field_attachment.py'],
 [sys.executable,'research/strominger/checkers/construct_global_PN_transport.py'],
 [sys.executable,'research/strominger/checkers/check_neutron_contrast_electron_transport.py'],
 [sys.executable,'research/strominger/checkers/check_full_five_channel_candidate.py'],
 ['node','research/strominger/checkers/check_extended_field_frames.mjs'],
]
runs=[]
for command in commands:
    completed=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=300);runs.append({'command':command,'exitCode':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr})
    if completed.returncode:
        (OUT/'failed-run.json').write_text(json.dumps(runs,indent=2)+'\n');raise SystemExit(completed.stderr or completed.stdout)
    print('PASS',command[-1],flush=True)
receipts=['baryon-tensor-grid/verification.json','tetrahedral-field-attachment/verification.json','neutron-belt-field-attachment/verification.json','global-PN-transport/verification.json','neutron-contrast-electron-transport/verification.json','full-five-channel-candidate/verification.json','extended-field-frames/verification.json','global-PN-NE-extension/verification.json','window-translation-covariance/verification.json','window-combination-coherence/verification.json']
artifacts=[];mismatches=[]
for name in receipts:
    path=BASE/name;raw=path.read_bytes();d=json.loads(raw);digest=hashlib.sha256(raw).hexdigest();snapshot=OUT/'snapshots'/f'{digest}.json';snapshot.parent.mkdir(exist_ok=True)
    if snapshot.exists():assert snapshot.read_bytes()==raw
    else:snapshot.write_bytes(raw)
    for key,value in d.get('sourceHashes',{}).items():
        if not isinstance(value,str):continue
        source=ROOT/key.replace('\\','/')
        if not source.exists() or hashlib.sha256(source.read_bytes()).hexdigest()!=value:mismatches.append({'receipt':name,'source':key})
    artifacts.append({'path':path.relative_to(ROOT).as_posix(),'sha256':digest,'snapshot':snapshot.relative_to(ROOT).as_posix(),'status':d.get('status'),'freshReplayed':name in receipts[:7]})
assert not mismatches,mismatches
frames=json.loads((BASE/receipts[6]).read_text());states=sum(x['packetAndFieldFrameStates'] for x in frames['rows']);conflicts=sum(x['markedChartsWithBothFieldParities'] for x in frames['rows']);assert states==250040 and frames['transitions']==458912 and conflicts==0
summary={'schema':'marici.reader-field-closeout.v1','status':'fresh-replay-passed','actor':'marici.Strominger','ledgerEntry':4326,'verificationLevel':'Exact algebra and bounded executable checks; conditional field architecture; no independent scientific review or physical validation','coherenceObligation':'Attachment transport and bounded dynamic route compatibility; global sewing remains open','freshCheckerRuns':len(runs),'boundedFrameTest':{'depth':frames['depth'],'seedMarkings':frames['seedMarkings'],'states':states,'transitions':frames['transitions'],'markedChartFrameConflicts':conflicts},'artifacts':artifacts,'runRecords':runs,'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limits':['No derived M/C torus or vortex topology','No order-seven or order-fourteen symmetry from grouping 28 steps','PN completion and window-to-sector coupling remain model choices','Added electron-return ledger term is not a physical energy derivation','No universal-depth or all-assembly coherence theorem','Production/viewer and occupancy permissions unchanged']}
(OUT/'verification.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:summary[k] for k in ['status','freshCheckerRuns','boundedFrameTest']}))

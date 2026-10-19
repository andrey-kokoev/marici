"""Bounded apples-to-apples archived-input benchmark; never edits original runs."""
import argparse,json,subprocess,sys,time,hashlib
from pathlib import Path
from reference_solver_encodings import MODES
ROOT=Path(__file__).resolve().parents[3]
parser=argparse.ArgumentParser();parser.add_argument('--timeout-ms',type=int,default=30000)
parser.add_argument('--seeds',type=int,nargs='+',default=[0]);args=parser.parse_args()
if args.timeout_ms<=0:raise ValueError('Positive budget required')
out=ROOT/'research/strominger/results/reference-solver-benchmark';out.mkdir(parents=True,exist_ok=True)
worker=Path(__file__).with_name('benchmark_reference_solver.py');production=Path(__file__).with_name('solve_reference_n14.py')
hash_file=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=hash_file(production)
subprocess.run([sys.executable,str(worker),'--equivalence','--output',str(out/'equivalence.json')],cwd=ROOT,check=True,capture_output=True,text=True,timeout=120)
cases=[('na23',5),('mg24',5),('mg24',7),('mg24',8),('mg24',9)]
rows=[];manifest={}
summary_path=out/f"benchmark-{args.timeout_ms}ms-seeds-{'-'.join(map(str,args.seeds))}.json"
def save(complete):
    sources=[Path(__file__),worker,Path(__file__).with_name('reference_solver_encodings.py'),production,Path(__file__).with_name('replay_reference_solver_candidate.mjs')]
    report={'status':'complete' if complete else 'running','timeoutMs':args.timeout_ms,'seeds':args.seeds,'modes':MODES,'rows':rows,'inputHashes':manifest,
            'productionSolverUnchanged':hash_file(production)==before,'equivalenceReceipt':'equivalence.json',
            'sourceHashes':{p.relative_to(ROOT).as_posix():hash_file(p) for p in sources},
            'scope':'Sequential fresh worker processes on saved inputs; timeout is a censored observation, not a runtime estimate or negative result. Build and solver time measured separately. No production solver replacement.'}
    summary_path.write_text(json.dumps(report,indent=2)+'\n')
for isotope,origin in cases:
    input_path=ROOT/f'research/strominger/results/reference-{isotope}-search/D{origin}-input.json'
    manifest[input_path.relative_to(ROOT).as_posix()]=hash_file(input_path)
    original=json.loads((input_path.parent/'verification.json').read_text())
    expected=next(r['solver']['status'] for r in original['rows'] if r['maxOrigin']==origin)
    for seed in args.seeds:
        for mode in MODES:
            stem=f'{isotope}-D{origin}-{mode}-seed{seed}-{args.timeout_ms}ms';result_path=out/(stem+'.json')
            started=time.perf_counter()
            subprocess.run([sys.executable,str(worker),'--input',str(input_path.relative_to(ROOT)),'--output',str(result_path),'--mode',mode,'--seed',str(seed),'--timeout-ms',str(args.timeout_ms)],cwd=ROOT,check=True,capture_output=True,text=True,timeout=args.timeout_ms/1000+90)
            wall=time.perf_counter()-started;result=json.loads(result_path.read_text())
            assert result['inputSha256']==manifest[input_path.relative_to(ROOT).as_posix()]
            if expected in ('sat','unsat') and result['status'] in ('sat','unsat'):assert result['status']==expected
            replay=None
            if result['status']=='sat':
                replay=stem+'-replay.json'
                subprocess.run(['node',str(Path(__file__).with_name('replay_reference_solver_candidate.mjs')),str(input_path),str(result_path),str(out/replay)],cwd=ROOT,check=True,capture_output=True,text=True,timeout=120)
            row={'isotope':isotope,'origin':origin,'mode':mode,'seed':seed,'status':result['status'],'buildSeconds':result['buildSeconds'],
                 'checkSeconds':result['checkSeconds'],'processWallSeconds':wall,'encoding':result['encoding'],'resultFile':result_path.name,'replayFile':replay}
            rows.append(row);save(False)
            print(json.dumps(row),flush=True)
assert hash_file(production)==before
assert all(hash_file(ROOT/path)==digest for path,digest in manifest.items())
save(True)
print('Completed: '+str(summary_path),flush=True)

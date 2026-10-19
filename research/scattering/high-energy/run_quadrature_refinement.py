"""Launch/resume inspection of a bounded, source-pinned 33-node response128 calculation.

Run with uv --with numpy --with scipy --with sympy. --start launches an owned
worker; --status reads its durable state. No frozen archive or source is edited.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from zipfile import ZipFile
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

WORK=ROOT/'.ai/tmp/scattering-h6-response33'
JOB=HOME/'results/quadrature33-job.v1.json'
RESULT=HOME/'results/quadrature17-vs33.v1.json'
ARCHIVE=HOME/'pentachoron_full_response128_packet_bundle.zip'
HIGH=HOME/'pentachoron_higher_closed_cutoff_bundle.zip'
BUDGET=3600


def stamp():return datetime.now(timezone.utc).isoformat()


def save(state):
    JOB.parent.mkdir(parents=True,exist_ok=True)
    temp=JOB.with_suffix('.tmp');temp.write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8');temp.replace(JOB)


def extract(archive,destination,expected):
    assert digest(archive)==expected,'archive hash mismatch'
    destination.mkdir(parents=True,exist_ok=True)
    with ZipFile(archive) as z:
        manifest=json.loads(z.read('MANIFEST.sha256.json'))
        for name,value in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==value,name
        for member in z.infolist():
            assert (destination/member.filename).resolve().is_relative_to(destination.resolve())
            assert (member.external_attr>>16)&0o170000!=0o120000
        z.extractall(destination)


def worker():
    state=json.loads(JOB.read_text(encoding='utf-8'));state.update(status='preparing',worker_pid=os.getpid(),worker_started_at=stamp());save(state)
    started=time.monotonic()
    try:
        historical_validate()
        assert state['source_sha256'][Path(__file__).relative_to(ROOT).as_posix()]==digest(Path(__file__))
        delivery=WORK/'delivery';calc=WORK/'calculation'
        # Nested source archives exceed Windows MAX_PATH; preserve extended paths
        # through the source entrypoint instead of editing any source solver.
        if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
        extract(ARCHIVE,delivery,state['source_sha256'][ARCHIVE.relative_to(ROOT).as_posix()])
        provenance=json.loads((delivery/'input_provenance.json').read_text())['source_archives']
        assert digest(HIGH)==provenance[HIGH.name]
        compact=delivery/'inputs/pentachoron_closed_mode_feedback_bundle.zip'
        extract(compact,calc,provenance[compact.name])
        env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
        command=[sys.executable,'-u',str(calc/'reproduce_feedback.py'),'--source',str(HIGH),'--directions','128','--points','33','--case','h6_response33']
        state.update(status='running',command=command,source_work_directory=str(calc));save(state)
        with (WORK/'solver.log').open('ab',buffering=0) as log:
            flags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name=='nt' else 0
            child=subprocess.Popen(command,cwd=calc,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=flags,start_new_session=os.name!='nt')
            state['child_pid']=child.pid;save(state)
            try:code=child.wait(timeout=max(1,BUDGET-(time.monotonic()-started)))
            except subprocess.TimeoutExpired:
                # Terminate only this worker's owned solver process tree.
                if os.name=='nt':subprocess.run(['taskkill','/PID',str(child.pid),'/T','/F'],capture_output=True)
                else:
                    import signal
                    os.killpg(child.pid,signal.SIGTERM)
                child.wait(timeout=30)
                state.update(status='budget_exhausted',finished_at=stamp());save(state);return
        if code!=0:raise RuntimeError('source driver exited '+str(code)+'; inspect '+str(WORK/'solver.log'))
        import numpy as np
        spec=importlib.util.spec_from_file_location('source_packet_compare',delivery/'compare_response_spaces.py')
        helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
        output=calc/'runs/h6_response33'
        with np.load(output/'packet_kernels.npz',allow_pickle=False) as data:
            assert len(data['K'])==33
            full=helper.evaluate(data,1);subset=helper.evaluate(data,2)
        comparisons={}
        for key in ('peak_transport','whole_packet_transport','product_probability'):
            assert subset[key]!=0
            change=abs(full[key]-subset[key])/abs(subset[key])
            comparisons[key]={'relative_absolute_change':change,'within_one_percent':change<=.01}
        with np.load(delivery/'results/response128/packet_kernels.npz',allow_pickle=False) as old:
            baseline=helper.evaluate(old,1)
        result={'schema':'marici.scattering.quadrature17-vs33.v1','source_sha256':state['source_sha256'],
                'status':'computed_numerical_comparison','response_directions':128,
                'matched_17':subset,'matched_33':full,'comparisons':comparisons,
                'historical_17_replay':baseline,
                'historical_17_relative_changes':{k:abs(subset[k]-baseline[k])/abs(baseline[k]) for k in comparisons},
                'stationary_solver_replayed':True,'new_grid_nodes':33,
                'kernel_sha256':digest(output/'packet_kernels.npz'),
                'solver_error_margin_certified':False,
                'H6_disposition':'Review comparison, source verification and solver error margins before changing proposition status.'}
        RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        state.update(status='completed_pending_review',result=RESULT.relative_to(ROOT).as_posix(),finished_at=stamp());save(state)
    except Exception as error:
        state.update(status='failed',error=repr(error),finished_at=stamp());save(state)
        raise


def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--start',action='store_true');g.add_argument('--retry-failed',action='store_true');g.add_argument('--status',action='store_true');g.add_argument('--worker',action='store_true');args=p.parse_args()
    if args.status:
        print(JOB.read_text(encoding='utf-8') if JOB.exists() else 'No H6 job recorded.');return
    if args.worker:worker();return
    history=[]
    if JOB.exists():
        old=json.loads(JOB.read_text(encoding='utf-8'))
        if not args.retry_failed or old['status'] not in ('failed','budget_exhausted'):
            raise SystemExit('Existing job: inspect --status; only a recorded failed/exhausted job admits --retry-failed.')
        history=old.pop('prior_attempts',[]);history.append(old)
    elif args.retry_failed:raise SystemExit('No failed job to retry.')
    if not (Path(sys.prefix)/'pyvenv.cfg').exists():raise SystemExit('Launch with a persistent virtual environment, not an ephemeral uv run environment.')
    if not Path(sys.executable).resolve().is_relative_to(WORK.resolve()):
        raise SystemExit('Use a persistent venv under '+str(WORK)+'; ephemeral uv run environments are removed after launch.')
    historical_validate();WORK.mkdir(parents=True,exist_ok=True)
    state={'schema':'marici.scattering.quadrature33-job.v1','status':'launching','created_at':stamp(),
           'budget_seconds':BUDGET,'prior_attempts':history,'log':str(WORK/'solver.log'),'worker_log':str(WORK/'worker.log'),
           'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in (ARCHIVE,HIGH,Path(__file__))}}
    save(state)
    with (WORK/'worker.log').open('ab',buffering=0) as log:
        flags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name=='nt' else 0
        child=subprocess.Popen([sys.executable,'-u',str(Path(__file__).resolve()),'--worker'],stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,creationflags=flags,start_new_session=os.name!='nt',close_fds=True)
    print(json.dumps({'worker_pid':child.pid,'job_record':str(JOB),'status':'launched','budget_seconds':BUDGET}))


if __name__=='__main__':main()

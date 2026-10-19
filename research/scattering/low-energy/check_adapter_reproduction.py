"""Isolated current-source replay of the historical native rim adapter.

Preserves the owner receipt; compares all mathematical output, not just flags.
A successful replay does not refresh every ancestor or historical source pin.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
BASE=ROOT/'research/voevodsky'
CHECKER=BASE/'checkers/check_native_rim_phase_adapter.py'
OWNER=BASE/'results/native_rim_phase_adapter.json'
HELPER=BASE/'checkers/assemble_relative_geometry.py'
HISTORICAL_HELPER_SHA='f155f96079238a2f21c5147c5eae8c41212db1dbdab4d5e40cfb26f1a45bec7a'
CURRENT_HELPER_SHA='5e088a6d19f61f9cc449328c072ac34c3a4c62a3fb1deac88859ec10d8482d2c'
NOTE=HOME/'ADAPTER-REPRODUCTION.md'
RESULT=HOME/'results/adapter-reproduction.v1.json'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path):return json.loads(path.read_text(encoding='utf-8'))


def module_closure():
    """Conservative static closure of imports in the two source checker trees."""
    roots=[BASE/'checkers',ROOT/'research/nima/checkers'];todo=[CHECKER];seen=set()
    while todo:
        p=todo.pop()
        if p in seen:continue
        seen.add(p)
        for node in ast.walk(ast.parse(p.read_text(encoding='utf-8'))):
            modules=([node.module] if isinstance(node,ast.ImportFrom) else
                     [a.name for a in node.names] if isinstance(node,ast.Import) else [])
            for name in modules:
                candidates=[r/(name+'.py') for r in roots if name and (r/(name+'.py')).is_file()]
                assert len(candidates)<=1,'ambiguous local import: '+str(name)
                todo.extend(candidates)
    return seen


def compare(stored,fresh):
    # Preserve every field other than the explicitly audited provenance map.
    assert set(stored)==set(fresh),'adapter result schema changed'
    assert {k:v for k,v in stored.items() if k!='source_hashes'}=={
        k:v for k,v in fresh.items() if k!='source_hashes'},'adapter mathematical payload changed'
    old=stored['source_hashes'];new=fresh['source_hashes']
    assert set(old)==set(new),'source binding inventory changed'
    changes=[{'source':key,'historical_sha256':old[key],'current_sha256':new[key]}
             for key in sorted(old) if old[key]!=new[key]]
    assert changes==[{'source':'checkers/assemble_relative_geometry.py',
                      'historical_sha256':HISTORICAL_HELPER_SHA,'current_sha256':CURRENT_HELPER_SHA}],'unreviewed source drift'
    assert fresh['verification_passed'] is True and all(v is True for v in fresh['checks'].values())
    return changes


def build():
    owner_before=OWNER.read_bytes();stored=json.loads(owner_before)
    modules=module_closure()
    source_paths={BASE/p for p in stored['source_hashes']}|modules
    hashes_before={p:sha(p) for p in source_paths|{OWNER}}
    # Keep source-relative paths so each unmodified __file__-based constructor
    # resolves only copied inputs and writes only into its temporary results tree.
    with tempfile.TemporaryDirectory(prefix='low-energy-adapter-replay-') as temp:
        sandbox=Path(temp)
        for p in source_paths:
            target=sandbox/p.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(p,target)
        output=sandbox/OWNER.relative_to(ROOT);output.parent.mkdir(parents=True,exist_ok=True)
        script=sandbox/CHECKER.relative_to(ROOT)
        module_record=sandbox/'loaded-modules.json'
        wrapper='''import json, pathlib, runpy, sys
script=pathlib.Path(sys.argv[1]); root=pathlib.Path(sys.argv[2]).resolve()
sys.path.insert(0,str(script.parent))
runpy.run_path(str(script),run_name="__main__")
files=sorted({str(pathlib.Path(m.__file__).resolve()) for m in sys.modules.values() if getattr(m,"__file__",None) and pathlib.Path(m.__file__).suffix==".py"})
pathlib.Path(sys.argv[3]).write_text(json.dumps(files),encoding="utf-8")
'''
        p=subprocess.run([sys.executable,'-I','-B','-c',wrapper,str(script),str(sandbox),str(module_record)],
                         cwd=sandbox,capture_output=True,text=True,timeout=120)
        assert p.returncode==0,'isolated adapter replay failed: '+p.stderr
        fresh=load(output)
        loaded=load(module_record);runtime_local=[]
        for raw in loaded:
            path=Path(raw)
            assert not path.is_relative_to(ROOT),'original repository module leaked into sandbox'
            if path.is_relative_to(sandbox):
                relative=path.relative_to(sandbox);assert ROOT/relative in modules,'untracked runtime source import'
                runtime_local.append(relative.as_posix())
        # The static closure is conservative (it includes imports in uncalled
        # functions); require the actual direct adapter helpers to be loaded.
        for source in (HELPER,BASE/'checkers/check_neutron_rim_port_transport.py',BASE/'checkers/check_belt_operator_inputs.py'):
            assert source.relative_to(ROOT).as_posix() in runtime_local,'direct helper not loaded: '+str(source)
        changes=compare(stored,fresh)
        # Deliberately perturb substantive output, source inventory, and a pass
        # flag: a provenance-only waiver must not accept any of these changes.
        controls=[]
        for name in ('changed-adapter-matrix','changed-schedule','failed-check','extra-source-binding','unreviewed-helper-version'):
            bad=json.loads(json.dumps(fresh))
            if name=='changed-adapter-matrix':bad['adapter_matrix'][0][0]=['1','0','0','0']
            elif name=='changed-schedule':bad['schedule'][0]['tick']=999
            elif name=='failed-check':bad['verification_passed']=False
            elif name=='extra-source-binding':bad['source_hashes']['unreviewed.py']='0'*64
            else:bad['source_hashes']['checkers/assemble_relative_geometry.py']='0'*64
            try:compare(stored,bad)
            except AssertionError:controls.append(name)
            else:raise AssertionError('hostile reproduction accepted: '+name)
    assert OWNER.read_bytes()==owner_before,'owner receipt modified'
    assert all(sha(p)==h for p,h in hashes_before.items()),'source modified during replay'
    paths=source_paths|{OWNER,NOTE,Path(__file__)}
    return {'schema':'marici.scattering.low-energy-adapter-reproduction.v1','status':'pass_scoped_reproduction',
            'scientific_checker_freshly_replayed':True,'passed_checks':len(fresh['checks']),
            'matching_mathematical_payload':True,'provenance_differences':changes,
            'historical_receipt_rewritten':False,'historical_source_binding_fresh':False,
            'all_ancestors_reproduced':False,'new_proposition_outcomes_admitted':False,
            'scope':'Same full local adapter output and schedule under current copied sources; not a bytewise historical receipt replay or full ancestor-chain refresh.',
            'runtime_local_imports':sorted(runtime_local),'hostile_controls_refused':controls,
            'fresh_adapter_result':fresh,
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)}}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert load(RESULT)==r,'stale adapter reproduction receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','passed_checks','matching_mathematical_payload','provenance_differences','historical_receipt_rewritten','hostile_controls_refused')}))


if __name__=='__main__':main()

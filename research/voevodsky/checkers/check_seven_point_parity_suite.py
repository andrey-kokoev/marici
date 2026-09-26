"""Fresh end-to-end seven-point parity reproduction, no cached proof stages."""
from pathlib import Path
import hashlib,json,subprocess,sys,time,platform,importlib.metadata
root=Path(__file__).resolve().parents[1];checkers=root/'checkers';results=root/'results'
out=results/'seven-point-parity-suite.json';start=time.monotonic()
stages=[('check_seven_point_kinematic_chart.py','seven-point-kinematic-chart.json',[]),('check_seven_point_universal_ward_basis.py','seven-point-universal-ward-basis.json',[]),('check_seven_point_generic_reduced_parity.py','seven-point-generic-reduced-parity.json',[]),('check_seven_point_generic_quartics.py','seven-point-generic-quartics-lcm.json',['--fresh']),('check_seven_point_full_parity_tensor.py','seven-point-full-parity-tensor.json',[]),('check_seven_point_ward_reduced_parity.py','seven-point-ward-reduced-parity.json',[])]
files={checkers/script for script,_,_ in stages}|{Path(__file__),checkers/'check_seven_point_parity.py',checkers/'nine_point_source_r.py'}
primary=root.parents[0]/'sources/nima/papers/n2mhv-tree/0808.2475/newrecursionv6.tex';files.add(primary)
def hashes():return {str(p.relative_to(root.parents[1])):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
report={'passed':False,'source_sha256':hashes(),'runtime':{'python':platform.python_version(),'sympy':importlib.metadata.version('sympy'),'python_flint':importlib.metadata.version('python-flint')},'stages':[]}
def save():out.write_text(json.dumps(report,indent=2)+'\n')
save()
for script,artifact,args in stages:
 print('RUN',script,flush=True);stage_start=time.monotonic()
 completed=subprocess.run([sys.executable,str(checkers/script),*args],capture_output=True,text=True,timeout=300)
 log=results/(script.removesuffix('.py')+'.log');log.write_text(completed.stdout+'\n'+completed.stderr)
 assert completed.returncode==0,(script,completed.returncode,str(log))
 payload=json.loads((results/artifact).read_text());assert payload['passed'],artifact
 report['stages'].append({'checker':script,'artifact':artifact,'artifact_sha256':hashlib.sha256((results/artifact).read_bytes()).hexdigest(),'seconds':round(time.monotonic()-stage_start,3)})
 save()
assert report['source_sha256']==hashes(),'source changed during proof run'
quartics=json.loads((results/'seven-point-generic-quartics-lcm.json').read_text());terms=results/'seven-point-generic-reduced-parity.json'
assert quartics['source_sha256']==hashlib.sha256(terms.read_bytes()).hexdigest()
assert len(quartics['identities'])==15
report['passed']=True;report['seconds']=round(time.monotonic()-start,3)
report['claim']='Complete seven-point NNMHV superamplitude agrees with Grassmann-Fourier parity transform of NMHV as a rational identity on the regular six-modulus momentum-twistor chart. Momentum delta/common phase stripped, Parke-Taylor factors retained.'
report['limits']='Computational algebra certificate using the published recursion conventions; not a proof-assistant formalization, independent rederivation of recursion, or positive-contour completeness proof. Does not complete the parked nine-point contour problem.'
save();print(json.dumps({'passed':True,'stages':len(stages),'seconds':report['seconds'],'claim':report['claim']},indent=2))

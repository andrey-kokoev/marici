"""A linear defect shared by runtime and manifest must reach the source oracle."""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib,json,shutil,subprocess,sys
base=Path(__file__).resolve().parent
files=list(base.glob('*.py'))
def hashes():return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
before=hashes()
with TemporaryDirectory(prefix='shared-semantic-mutation-') as tmp:
 target=Path(tmp)/'checkers';target.mkdir();results=Path(tmp)/'results';results.mkdir()
 for p in files:shutil.copy2(p,target/p.name)
 shutil.copy2(base.parent/'results/combined-signature.json',results/'combined-signature.json')
 def run(checker):return subprocess.run([sys.executable,'-E',str(target/checker)],cwd=target,capture_output=True,text=True,timeout=180)
 baseline=run('check_replay_semantics.py');assert baseline.returncode==0,baseline.stderr
 mutations=[('scanning_set_program.py',"(n+'.f',g+'.p'),(n+'.b',g+'.u')","(n+'.b',g+'.p'),(n+'.f',g+'.u')"),('rule_templates.py','x.f--0.p x.b--0.u','x.b--0.p x.f--0.u')]
 for name,old,new in mutations:
  p=target/name;text=p.read_text();assert text.count(old)==1;changed=text.replace(old,new);compile(changed,str(p),'exec');p.write_text(changed)
 shutil.rmtree(target/'__pycache__',ignore_errors=True)
 certificates=run('check_full_certificates.py')
 assert certificates.returncode==0,certificates.stderr
 semantic=run('check_replay_semantics.py')
 assert semantic.returncode!=0 and "assert result['terminal']==interpret(bits,ops)" in semantic.stderr and 'AssertionError' in semantic.stderr,semantic.stderr
 report={'passed':True,'mutation':'Swap scan fuel/cursor routing in both production GS rule and declarative GS template','baseline_passed':True,'all_57_certificate_fixtures_still_pass':True,'source_oracle_detected':True,'oracle_stderr':semantic.stderr,'scope':'One isolated shared semantic defect, not exhaustive mutation coverage. Altered contract digest is recomputed by the trace producer.'}
assert before==hashes()
report['production_sources_unchanged']=True
p=base.parent/'results/shared-semantic-mutation.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='oracle_stderr'}))

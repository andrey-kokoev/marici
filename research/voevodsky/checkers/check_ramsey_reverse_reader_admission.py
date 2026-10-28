from pathlib import Path
import subprocess,json
ROOT=Path(__file__).resolve().parents[3]
def main():
    run=subprocess.run(['node','research/voevodsky/checkers/check_ramsey_reverse_reader_admission.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=180)
    (ROOT/'research/voevodsky/results/ramsey-reverse-reader-admission-run.log').write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
    assert run.returncode==0,run.stdout+'\n'+run.stderr
    d=json.loads((ROOT/'research/voevodsky/results/ramsey-reverse-reader-admission-v1.json').read_text())
    assert d['status']=='passed' and d['freshMarkingsPerImplementation']==24 and d['implementationsChecked']==2
    assert not d['sourceAdmittedReversalProduced'] and not d['parentDescentResolved']
    print(run.stdout)
if __name__=='__main__':main()

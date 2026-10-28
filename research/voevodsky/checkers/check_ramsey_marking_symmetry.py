from pathlib import Path
import subprocess,json
ROOT=Path(__file__).resolve().parents[3]
def main():
    run=subprocess.run(['node','research/voevodsky/checkers/check_ramsey_marking_symmetry.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=180)
    (ROOT/'research/voevodsky/results/ramsey-marking-symmetry-run.log').write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
    assert run.returncode==0,run.stdout+'\n'+run.stderr
    d=json.loads((ROOT/'research/voevodsky/results/ramsey-marking-symmetry-v1.json').read_text())
    assert d['status']=='passed' and d['operationCovarianceCells']==576
    assert d['fixedSubdivisionSymmetries']==8 and d['complementaryRoleSymmetries']==4
    assert d['complementarySymmetriesFixingVertices']==0 and not d['parentDescentResolved']
    print(run.stdout)
if __name__=='__main__':main()

"""Exclude single recolorings on the 68 exact-six cores by coloring compatibility graphs, not by assembling a seven-port panel."""
import gzip,json,tempfile,subprocess
from pathlib import Path
from collections import Counter
from ramsey_retention_slice import CAT,D,decode

def audit():
    prior=json.loads((D.parent/'ramsey_deleted27_seven_control.json').read_text())['witnesses']['6'];inputs=[];counts=[Counter(),Counter()];passed=[]
    for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')):
        for z in prior.get(str(i),{}):inputs.append(' '.join(map(str,[i,int(z)]+decode(l.strip()))))
    assert len(inputs)==68
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'gate.exe';subprocess.run(['rustc','--edition=2021','-Awarnings','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(inputs),text=True,capture_output=True,check=True)
    for l in p.stdout.splitlines():
        i,z,u,v,old,k,n,m=map(int,l.split());counts[old][k]+=1
        if k==3:passed.append(dict(record=i,deletion=z,edge=[u,v],old_red=bool(old),residual_rows=m))
    out=dict(cores=68,stage_key=['blue_eight','six_colors','neighbor_coloring','unresolved'],red_additions=counts[0],red_removals=counts[1],unresolved=passed);print(counts,len(passed),len({(r['record'],r['deletion']) for r in passed}),passed[:3]);(D.parent/'ramsey_seven_link_gate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()

"""Scan edge-count strata for five-port candidates; independently verify positives with full coverage."""
import gzip,json,subprocess,tempfile
from pathlib import Path
from ramsey_intact27_joint_five import CAT,D,decode,find

def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);layers={k:[] for k in (85,86,87,94)}
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:
        for i,l in enumerate(f):
            s=l.rstrip();e=sum(s[1:].translate(w))
            if e in layers:layers[e].append((i,s.decode()))
    out={}
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'pack.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_intact27_seven_pack.rs')),'-o',str(exe)],check=True)
        for k,rows in layers.items():
            p=subprocess.run([str(exe)],input='\n'.join(f'{i} {s}' for i,s in rows),text=True,capture_output=True,check=True);assert int(p.stderr)==len(rows);ids=list(map(int,p.stdout.split()));seeds=dict(rows);yes={}
            for i in ids:
                r=find(decode(seeds[i]));assert r['counts']['seven'];yes[i]=r
                if r['example']:break
            out[k]=dict(total=len(rows),seven_candidates=ids,fully_checked=yes);print(k,len(rows),len(ids),next((i for i,r in yes.items() if r['example']),None),flush=True)
    (D.parent/'ramsey_intact27_pack_layers.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()

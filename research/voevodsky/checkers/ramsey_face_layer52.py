"""Replicate the 51-edge control and run the next unresolved common-core layer."""
from ramsey_retention_slice import CAT,D,decode
from collections import Counter
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import gzip,json,tempfile,subprocess

def audit():
    p=D.parent;marked=json.loads((p/'ramsey_face_double_root.json').read_text())['marked'];groups={r['type']:dict(r['matches']) for r in json.loads((p/'ramsey_face_bridge_screen.json').read_text())};b=decode((CAT/'r35_13.g6').read_text().strip());rows=[r for r in marked if r['catalogue'] and r['e'] in (51,52)];ids={i for r in rows for i in groups[r['type']]};A={i:decode(s.strip()) for i,s in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rt')) if i in ids};jobs=[(r['e'],[i,r['q'],r['t'],*A[i],*b]) for r in rows for i in groups[r['type']]]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'test.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_face_marked_projection.rs')),'-o',str(exe)],check=True)
        def run(chunk):
            s='\n'.join(' '.join(map(str,l)) for e,l in chunk);lines=subprocess.run([str(exe)],input=s,text=True,capture_output=True,check=True).stdout.splitlines();assert len(lines)==len(chunk);return [[e,*map(int,l.split())] for (e,_),l in zip(chunk,lines)]
        with ThreadPoolExecutor(8) as pool:result=[l for part in pool.map(run,[jobs[j:j+4] for j in range(0,len(jobs),4)]) for l in part]
    totals={e:[sum(l[j] for l in result if l[0]==e) for j in (4,5,6)] for e in (51,52)};assert totals[51]==[900,0,0];print(totals);(p/'ramsey_face_layer52.json').write_text(json.dumps(dict(totals=totals,columns=['edges','catalogue','Q','T','embeddings','first_pass','both_pass'],rows=result),indent=2)+'\n')
if __name__=='__main__':audit()

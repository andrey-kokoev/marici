"""Blind core selection by unchanged two-side blue-six rule. Compare winners to cube after search."""
from ramsey_retention_slice import CAT,D,decode
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import gzip,json,tempfile,subprocess

def audit(layer=53):
    assert layer in (53,54)
    p=D.parent;b=decode((CAT/'r35_13.g6').read_text().strip());marked=json.loads((p/'ramsey_face_double_root.json').read_text())['marked'];types=[r for r in marked if r['e']==layer and r['catalogue']];groups={r['type']:dict(r['matches']) for r in json.loads((p/'ramsey_face_bridge_screen.json').read_text())};ids=set.union(*(set(groups[r['type']]) for r in types));A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rt')) if i in ids};jobs=[[i,r['q'],r['t'],*A[i],*b] for r in types for i in groups[r['type']]];assert (len(ids),len(jobs))==({53:(684,2052),54:(4989,4989)}[layer])
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'scan.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_face_blue_six_scan.rs')),'-o',str(exe)],check=True)
        def run(chunk):
            out=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,l)) for l in chunk),text=True,capture_output=True,check=True);ls=out.stdout.splitlines();assert len(ls)==len(chunk);return [l.split(' ',6) for l in ls]
        with ThreadPoolExecutor(8) as pool:res=[(list(map(int,l[:6])),json.loads(l[6])) for batch in pool.map(run,[jobs[i:i+12] for i in range(0,len(jobs),12)]) for l in batch]
    wins=[dict(record=i,q=q,t=t,sites=w) for (i,q,t,n,f,k),ls in res for w in ls];counts=[sum(r[j] for r,_ in res) for j in (3,4,5)];corecounts=[len({r[0] for r,_ in res if r[j]}) for j in (3,4,5)];assert counts[-1]==len(wins)
    out=dict(marking_counts=counts,core_counts=corecounts,both_pass=wins)
    if layer==53:
        from ramsey_face_unmark_cube import G,cells,bits,rel,iso
        z=cells.index('0**');H=bits(((1<<35)-1)&~(G[z]|G[34]|1<<z|1<<34));a=rel(G,H);cubeids=[i for i in {v['record'] for v in wins} if next(iso(a,A[i]),None)!=None];assert len(cubeids)==1;out['cube_record']=cubeids[0]
    print('layer',layer,'counts',counts,corecounts,'winners',len(wins));(p/f'ramsey_face_blind_layer{layer}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]) if len(sys.argv)>1 else 53)

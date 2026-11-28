"""All feasible restored rows per successful pair. Verify a complete predecessor for each, then locate the forward additions relative to its deleted vertex."""
import os,subprocess,tempfile,json
from pathlib import Path
from collections import Counter
from ramsey_cube_retention_floor import induced,G,D
from ramsey_retention_slice import check

def audit():
    prev=json.loads((D.parent/'ramsey_cube_two_cut_joint.json').read_text());good=[r for r in prev['cases'] if r['wins']];a=induced(G,json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels']);counts=Counter();shapes=Counter();pairs=Counter();runs=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'all.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_cube_two_cut_joint.rs')),'-o',str(exe)],check=True);data='\n'.join(' '.join(map(str,[*r['cuts'][0],*r['cuts'][1],*a])) for r in good);p=subprocess.run([str(exe)],input=data,text=True,capture_output=True,env={**os.environ,'RAMSEY_ALL_ROWS':'1'},check=True)
    lines=p.stdout.splitlines();assert len(lines)==len(good)==24
    for r,l in zip(good,lines):
        ws=json.loads(l.split(' ',6)[-1]);assert len({s for s,_,_ in ws})==len(ws)==r['wins'];classes=set()
        for s,add,_ in ws:
            g=a[:]+[s];
            for i,j in r['cuts']+add:g[i]^=1<<j;g[j]^=1<<i
            for i in range(26):g[i]|=(s>>i&1)<<26
            assert check(g,(1<<27)-1,3,8);locations=tuple(sorted(sum(s>>i&1 for i in e) for e in r['cuts']));overlap=len(set(r['cuts'][0])&set(r['cuts'][1]));d=s.bit_count();middles=[[v for v in range(27) if g[i]&g[j]&(1<<v)] for i,j in r['cuts']];assert all(len(h)==1 for h in middles);counts[locations]+=1;classes.add(locations);shapes[d,overlap,locations]+=1;r0=dict(cuts=r['cuts'],row=[i for i in range(26) if s>>i&1],locations=locations,predecessor_common_neighbors=middles,reverse_add=add);runs.append(r0)
        pairs[tuple(sorted(classes))]+=1
    print('rows',counts,'pairs',pairs,'shape',shapes);out=dict(counts={str(k):v for k,v in counts.items()},pair_types={str(k):v for k,v in pairs.items()},shapes={str(k):v for k,v in shapes.items()},cases=runs);(D.parent/'ramsey_cube_cut_location.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()

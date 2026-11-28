"""Resolve the surviving one-link trials on all 68 exact-six cores. Include known seven-port positive control."""
import ast,gzip,json,tempfile,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from ramsey_retention_slice import CAT,D,decode,check

def audit():
    gate=json.loads((D.parent/'ramsey_seven_link_gate.json').read_text());todo=sorted(gate['unresolved'],key=lambda r:not r['old_red']);ids={r['record'] for r in todo};graphs={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};jobs=[]
    for r in todo:
        a=graphs[r['record']][:];u,v=r['edge'];z=r['deletion'];assert (a[u]>>v&1)==r['old_red'] and z not in (u,v);a[u]^=1<<v;a[v]^=1<<u;jobs.append((z,a))
    jobs.append((26,json.loads((D.parent/'ramsey_gain26_regular_panel_control.json').read_text())['core']+[0]));counts=Counter();wins=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'run.exe';subprocess.run(['rustc','-Awarnings','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        def run(chunk):
            res=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,[z]+a)) for z,a in chunk),text=True,capture_output=True,check=True);rows=list(map(ast.literal_eval,res.stdout.splitlines()));assert len(rows)==len(chunk);return rows
        with ThreadPoolExecutor(8) as pool:results=[rs for batch in pool.map(run,[jobs[i:i+8] for i in range(0,len(jobs),8)]) for rs in batch]
    assert results[-1] and len(results)==len(jobs)
    for j,(rows,(z,a)) in enumerate(zip(results,jobs)):
        if j<len(todo):counts['remove' if todo[j]['old_red'] else 'add']+=1
        if not rows:continue
        assert len(rows)==7;g=a[:]+[0]*8
        for v,s in enumerate(rows,27):
            assert not s>>z&1;g[-1]|=1<<v;g[v]=s|1<<34
            for h in range(27):g[h]|=int(bool(s>>h&1))<<v
        assert check(g,((1<<35)-1)^(1<<z),3,9)
        if j<len(todo):wins.append(dict(**todo[j],rows=rows))
    assert counts=={'remove':57,'add':812};out=dict(tested=counts,witnesses=wins,control_rows=results[-1]);print('tested',counts,'wins',len(wins),wins[:1]);(D.parent/'ramsey_one_recolor_exact.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()

"""Read the existing strip closure census as an independent constraint, not as an issued five-edge matching half. Filter to the exact poles and marked entry; test whether closure selects the changing apex even at fixed exit."""
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).resolve().parent

def run():
    rows=json.loads((D/'ramsey_strip_closure_control.json').read_text());counts=Counter();examples={}
    for r in rows:
        w=r['path'];
        if w[:2]!=[0,16] or w[-1]!=29:continue
        counts[w[2],w[-2],r['closes']]+=1
        if r['closes'] and w[-2]==7:examples.setdefault(w[2],w)
    assert set(examples)=={10,13};return dict(counts=[dict(fork=f,exit=e,closes=c,n=n) for (f,e,c),n in sorted(counts.items())],closed_at_exit7=examples)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_source_apex_holdout.json').write_text(json.dumps(out)+'\n')

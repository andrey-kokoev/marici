"""Audit independent views, before pole decoding. Enumerate the compatible column-to-vertex bridges after calibrating the A-cut. No rule tying column identity across execution recuts is imposed."""
from itertools import permutations
from pathlib import Path
import json,sys
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import execute,validate,registry
from ramsey_strip_reanchor_test import src,dst,rowpair

def run():
    cols=range(4);swap=(0,2,1,3);stationary=src.index('B');assert dst.index('B')==stationary
    def view(word):return [(s,t,e) for s,t,_,e in validate(execute(word))]
    first=[('AB','BC','CA'),('AD','DB','BA')];second=[w[i:]+w[:i] for w,i in zip(first,[1,2])];observations=[]
    for words in (first,second):
        paths=list(map(view,words));base=paths[0][0][0];assert all(p[0][0]==p[-1][1]==base for p in paths)
        observations.append(dict(rows=[src,dst],column_index=stationary,row_pairings=[rowpair(w) for w in (src,dst)],execution=paths,base=base))
    r,b=map(set,first);admitted=[]
    for bind in permutations('ABCD'):
        rho=dict(zip(bind,[bind[i] for i in swap]));image=lambda e:rho[e[1]]+rho[e[0]]
        if {image(e) for e in r}!=b or {image(e) for e in b}!=r:continue
        # Even grant the extra calibration that the first row's moving R denotes C.
        if bind[src.index('R')]=='C':admitted.append(''.join(bind))
    assert set(admitted)=={'ACDB','BCDA'};initial='ACDB';records=[]
    for bind in admitted:
        endpoint=bind[stationary];assert set(bind)==set(initial)
        records.append(dict(column_binding=[initial,bind],mapped_stationary_endpoint=['A',endpoint],follows_recut=endpoint==observations[1]['base']))
    return dict(observations=observations,compatible_binding_histories=records)
if __name__=='__main__':
    out=run();print(out['compatible_binding_histories']);(D/'ramsey_basepoint_identifiability.json').write_text(json.dumps(out)+'\n')

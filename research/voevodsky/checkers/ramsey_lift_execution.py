"""Explicitly execute a trusted, reviewed local candidate. The journal itself never imports candidate code."""
import argparse, hashlib, json
from pathlib import Path

def need(x,msg):
    if not x:raise ValueError(msg)

def enc(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def h(b):return hashlib.sha256(b).hexdigest()
def ids(x):return isinstance(x,list) and all(isinstance(i,str) and i for i in x) and len(set(x))==len(x)

def inspect_run(t):
    l,k=t['input'];q=t['reduced'];cells=q['cells'];src=t['lifted']['occurrences'];need(isinstance(cells,dict) and ids(src) and all(ids(v) and v and set(v)<=set(src) for v in cells.values()),'cell provenance');g=t['geometry_readout'];need(sorted(g)==sorted([l,k]) and all(type(i) is int and i>0 for i in [l,k,*g]),'coordinate recovery');plus,minus=t['extra'],t['cancelled'];need(ids(plus) and ids(minus) and set(plus)<=cells.keys() and set(minus)<=set(src) and set(minus).isdisjoint(i for v in cells.values() for i in v),'correction witnesses');need(len(cells)-len(plus)+len(minus)==l*k,'baseline accounting');need(t['reduced_digest']==h(enc(q)),'wrong reduced object');return len(cells)

def execute(path,l,k):
    code=path.read_bytes();ns={'__name__':'ramsey_candidate','__file__':str(path)};exec(compile(code,str(path),'exec'),ns);lifted=ns['lift'](l,k);reduced=ns['reduce_once'](json.loads(enc(lifted)));raw=enc(reduced)
    # Both readers receive only the same serialized output, in independent copies.
    coords=ns['coordinates'](json.loads(raw));plus,minus=ns['witnesses'](json.loads(raw));t=dict(input=[l,k],implementation=h(code),lifted=lifted,reduced=reduced,reduced_digest=h(raw),geometry_readout=coords,extra=plus,cancelled=minus);inspect_run(t);return t
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('trusted_implementation',type=Path);p.add_argument('l',type=int);p.add_argument('k',type=int);p.add_argument('output',type=Path);p.add_argument('--verify',action='store_true');a=p.parse_args();result=execute(a.trusted_implementation,a.l,a.k)
    if a.verify:need(enc(result)==enc(json.loads(a.output.read_text())),'replay mismatch');print('Exact replay matches.')
    else:
        with a.output.open('x',encoding='utf8') as f:json.dump(result,f,indent=2)

"""Actual ordered derivative convolution, including nontrivial ideal action."""
from pathlib import Path
from itertools import product
from collections import defaultdict
import runpy
import contextlib
import io
import json
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_two_stage_filtered_attachment.py'))
D=b['ordered_derivative'];src=b['b']

def join(left,right):
    out=defaultdict(int)
    for (edges,buf),c in left.items():
        for (edges2,buf2),d in right.items():
            key=(edges+edges2,buf[:-1]+(buf[-1]+buf2[0],)+buf2[1:])
            out[key]+=c*d
    return {k:v for k,v in out.items() if v}

checks=0
for marks in product((0,1),repeat=4):
    u={((0,1),marks[:2]):1};v={((2,3),marks[2:]):1}
    uv=src['multiply'](u,v)
    for k in range(5):
        total=defaultdict(int)
        for i in range(k+1):
            for key,c in join(D(0,u,i),D(3,v,k-i)).items():total[key]+=c
        assert D(0,uv,k)=={key:c for key,c in total.items() if c}
        checks+=1

a=src['relation']((0,1),0);c=src['relation']((2,3),0)
ac=src['multiply'](a,c)
assert not D(0,a,0) and not D(3,c,0)
assert not D(0,ac,1)
assert D(0,ac,2)==join(D(0,a,1),D(3,c,1)) and D(0,ac,2)
# Highest jet retains the full marked path; prefix/interior/suffix records empty.
for marks in product((0,1),repeat=4):
    path={((0,1,2,3),marks):1}
    top=D(0,path,4)
    assert len(top)==1
    (edges,buffers),coefficient=next(iter(top.items()))
    assert tuple(e[3] for e in edges)==marks
    assert buffers==((),)*5 and coefficient==1
result={'passed':True,'ordered_jet_product_identities':checks,
 'checks':{'relation_action_is_visible_in_second_jet':True,
           'highest_jet_retains_marked_path':True},
 'scope':'Exact finite derivative convolution. Continuity and faithful filtered completion are proved using source norms and endpoint separation in the companion note; no completed derived tensor assertion.'}
out=ROOT/'research/voevodsky/results/filtered-fox-jet-product.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

"""Recut the same validated events, not a fresh replay. Keep one literal row view and BOTH natural endpoint observations; do not insert a column->native-vertex field."""
from pathlib import Path
import sys,json
from itertools import product
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import paths,validate,emitted
from ramsey_strip_reanchor_test import src,dst,rowpair

def run():
    strip=(src,dst,rowpair(src),rowpair(dst));p,q=paths[:2];stationary=src.index('B');assert dst.index('B')==stationary
    def rot(p,i):return validate(p[i:]+p[:i])
    cuts=[];initial=dict(emitted);ab=next(e for e in p if e[3]=='AB');ba=next(e for e in q if e[3]=='BA');assert ab[:2]==ba[:2][::-1]
    for i,j in product(range(len(p)),range(len(q))):
        a,b=rot(p,i),rot(q,j);assert all(any(e is x for x in initial.values()) for e in a+b)
        if a[0][0]!=b[0][0]:continue
        assert a[0][0]==a[-1][1]==b[-1][1];cuts.append(dict(offsets=(i,j),words=[[x[3] for x in t] for t in (a,b)],cursor_endpoint=a[0][0],saved_AB_source=ab[0],saved_BA_target=ba[1],seam_ids=(ab[2],ba[2])))
    assert [(c['cursor_endpoint'],c['saved_AB_source']) for c in cuts]==[('A','A'),('B','A')];assert emitted==initial
    return dict(literal_view=strip,stationary_column_one_based=stationary+1,offset_pairs_tried=len(p)*len(q),common_base_cuts=cuts,new_events=0)
if __name__=='__main__':
    out=run();print(json.dumps(out));(D/'ramsey_retained_event_recut.json').write_text(json.dumps(out)+'\n')

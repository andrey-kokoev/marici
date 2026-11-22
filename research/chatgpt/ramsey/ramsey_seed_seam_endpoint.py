"""Endpoint reader uses only two triangles and an unoriented diagonal. Known cyclic labels, calibration and masks enter evaluation, not the seam reader."""
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).parent;load=lambda p:json.loads(p.read_text());seed=load(D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json');V=set('ABCD');F=lambda f:'F_'+''.join(sorted(f));face=lambda f:set(f[2:]);faces=[set(c[:-1]) for c in seed['retained_face_cycles']];assert all(c[0]==c[-1] for c in seed['retained_face_cycles']);diag={'B','F_ACD'} # held out endpoint, not the diagonal

def boundary(fs):
    a,b=fs;u,v=sorted(a&b);return (u,F(a),v,F(b))
def select(fs,d):
    m,=set(boundary(fs))&d;return m
m=select(faces,diag);rims=[boundary(fs) for fs in combinations(map(set,combinations('ABCD',3)),2)];assert len(rims)==6
# Site addresses from existing geometric chart, raw vertex numbers only in evaluation adapter.
from ramsey_sector_arrow_bridge import features,point,cal,ws
from ramsey_sector_square_rim import cycles
L={i%35 for t in (1,7,11,16) for i in (t,-t)};U=sorted(set(range(1,35))-L);x,=features[U.index(2)];side=features[U.index(4)];rim,=[c for f,c in cycles.items() if x in f and side<=f];i=rim.index(x);forward={rim[(i+1)%4],rim[(i+2)%4]}==side;color=lambda mark:(mark in rim)!=forward;root_color=2 in L;assert color(m)==root_color and color((diag-{m}).pop())!=root_color
sig={i:{t for t in L if (i-t)%35 in L} for i in U};E=[(i,j) for i,j in combinations(U,2) if not sig[i]&sig[j]];ref=sum(1<<n for n,(i,j) in enumerate(E) if (i-j)%35 in L);decode={point[''.join(map(str,v))]:ws[int(k)] for k,v in cal.items()};assert ref==decode[m];opts=Counter();cov=0
for p in permutations('ABCD'):
    def act(v):return p['ABCD'.index(v)] if v in V else F({act(c) for c in face(v)})
    fs=[{act(c) for c in f} for f in faces];opts[select(fs,diag)]+=1;assert select(fs,set(map(act,diag)))==act(m);cov+=1
r=dict(source_rim=boundary(faces),candidate=m,point=x,side=sorted(side),query_oriented_rim=rim,forward=forward,predicted_red=color(m),antipode_red=color((diag-{m}).pop()),mask_errors=(ref^decode[m]).bit_count(),corner_only_same=(diag&V)=={m},unbound_embeddings=opts,passive_relabelings=cov,face_pair_controls=[dict(rim=c,endpoint=(set(c)&diag).pop()) for c in rims]);print(r);(D/'ramsey_seed_seam_endpoint.json').write_text(json.dumps(r,indent=2)+'\n')

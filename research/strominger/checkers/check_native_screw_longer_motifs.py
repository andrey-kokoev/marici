"""Larger monotone native-edge motifs on the existing screw mesh.
No new occupied cells or interpolated vertices are admitted.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,runpy,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
prerequisite=Path(__file__).with_name('check_native_screw_strands.py')
log=io.StringIO()
with contextlib.redirect_stdout(log):s=runpy.run_path(str(prerequisite))
vertices,edges,neighbor=s['vertices'],s['edges'],s['neighbor']
axial,radial,iterate=s['axial'],s['radial'],s['iterate']
add,scale,d=s['add'],s['scale'],s['d']
# Normalized transverse diamond coordinates. Every occupied vertex is one
# of (+/-1,0),(0,+/-1), irrespective of its axial coordinate.
def xy(v):
    x,y=radial(v);return x/2,y
def turn(u,v):
    x,y=xy(u);z,w=xy(v);cross=x*w-y*z
    return 1 if cross>0 else -1 if cross<0 else 0
assert {xy(v) for v in vertices}=={(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1))}
axis_crossing=[];surface_edges=[]
for edge in edges:
    u,v=tuple(edge);p,q=xy(u),xy(v)
    if p==(-q[0],-q[1]):
        # Opposite corners cross the axis at the midpoint.
        assert xy(scale(F(1,2),add(u,v)))==(0,0);axis_crossing.append(edge)
    else:
        # Same corner or adjacent corners: the entire straight segment lies
        # on a single face of the diamond prism, not just its sample points.
        assert p==q or p[0]*q[0]+p[1]*q[1]==0
        assert any(sx*p[0]+sy*p[1]==1 and sx*q[0]+sy*q[1]==1 for sx in (-1,1) for sy in (-1,1))
        surface_edges.append(edge)
surface=set(surface_edges)

# Exact pair witness, using shared vertices first and segment intersection as
# fallback. Axial bounding intervals discard irrelevant translated copies.
def collision(left,right):
    common=set(left)&set(right)
    if common:return min(common)
    for p,q in zip(left,left[1:]):
        for r,t in zip(right,right[1:]):
            if max(axial(p),axial(q))<min(axial(r),axial(t)) or max(axial(r),axial(t))<min(axial(p),axial(q)):continue
            hit=s['intersect'](p,q,r,t)
            if hit is not None:return hit
    return None

def fundamental(path,period):
    # Odd screw periods require two copies to obtain pure translation.
    if period%2:return path+[iterate(v,period) for v in path[1:]],2*period
    return path,period

screens=[];all_candidates=[]
for period in (2,3,4):
    candidates=[]
    for seed,start in s['seeds'].items():
        end=iterate(start,period);assert end in vertices
        for sign in (1,-1):
            def walk(path,quarters):
                v=path[-1]
                if v==end:
                    if quarters:
                        assert quarters*sign>0 and (quarters-2*period)%4==0
                        candidates.append({'seed':seed,'sign':sign,'quarters':quarters,'path':path})
                    return
                for w in sorted(neighbor[v]):
                    if not axial(v)<axial(w)<=axial(end):continue
                    if frozenset((v,w)) not in surface:continue
                    delta=turn(v,w)
                    if delta and delta!=sign:continue
                    walk(path+[w],quarters+delta)
            walk([start],0)
    # Ensure the putative periodic seam uses already available geometry for
    # every whole repetition that fits in the four-block tested core.
    for c in candidates:
        assert all(frozenset((u,v)) in surface for u,v in zip(c['path'],c['path'][1:]))
        for k in range(1,4//period):
            moved=[iterate(v,k*period) for v in c['path']]
            assert all(frozenset((u,v)) in edges for u,v in zip(moved,moved[1:]))
    positives=[c for c in candidates if c['sign']==1];negatives=[c for c in candidates if c['sign']==-1]
    witnesses=[]
    for i,left in enumerate(positives):
        lp,L=fundamental(left['path'],period)
        for j,right in enumerate(negatives):
            rp,L2=fundamental(right['path'],period);assert L==L2
            assert axial(lp[-1])-axial(lp[0])==L
            assert axial(rp[-1])-axial(rp[0])==L
            assert abs(axial(lp[0])-axial(rp[0]))<=1
            hit=None;shift_found=None
            # The seed offsets differ by at most one; both path spans are L.
            # More distant translation copies cannot meet in axial coordinate.
            for shift in range(-2,3):
                moved=[add(v,scale(L*shift,d)) for v in rp]
                hit=collision(lp,moved)
                if hit is not None:shift_found=shift;break
            assert hit is not None, ('Unexpected disjoint pair',period,i,j)
            witnesses.append({'positive':i,'negative':j,'copy_shift':shift_found,'point':hit})
    screens.append({'screw_blocks':period,'candidates':len(candidates),'positive_candidates':len(positives),'negative_candidates':len(negatives),
                    'quarter_turn_totals':sorted(set(c['quarters'] for c in candidates)),
                    'opposite_handed_pair_tests':len(witnesses),'disjoint_opposite_handed_pairs':0,'intersection_witnesses':witnesses})
    all_candidates.append({'period':period,'positive':positives,'negative':negatives})
report={'schema':'marici.native-screw-longer-motifs.v1','status':'pass',
 'scope':'Existing certified occupied mesh only; strict axial progress; monotone angular winding allowing zero-turn axial edges; two-, three-, four-block motifs. No radial expansion.',
 'surface':{'normalized_equation':'abs(X)+abs(Y)=1','surface_edges':len(surface_edges),'axis_crossing_edges_excluded':len(axis_crossing),
            'all_occupied_vertices_on_surface':True,'all_axis_avoiding_native_edges_on_surface':True},
 'screens':screens,'candidates':all_candidates,
 'topological_obstruction':'Two axial-monotone periodic curves on the same diamond-prism surface with unequal angular winding numbers must intersect. Opposite nonzero windings are unequal.',
 'radial_layer_tested':False,'prerequisite_output':log.getvalue()}
paths=[Path(__file__),prerequisite,ROOT/'research/strominger/results/native-screw-patch/verification.json',ROOT/'research/strominger/native-screw-longer-motifs-v1.md']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/native-screw-longer-motifs';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2,default=s['serial'])+'\n')
print(json.dumps({'status':'pass','surface':report['surface'],'screens':[{k:v for k,v in screen.items() if k!='intersection_witnesses'} for screen in screens]},indent=2))

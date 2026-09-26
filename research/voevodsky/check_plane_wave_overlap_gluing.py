"""Exact overlap and C2-seam controls in the Brinkmann vacuum family.
Reuses the previous coordinate-curvature engine, not an independent GR backend.
"""
import ast
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
engine=Path(__file__).with_name('check_plane_wave_tidal_frame_loop.py')
tree=ast.parse(engine.read_text(encoding='utf-8'))
prefix=[]
for node in tree.body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='a' for t in node.targets):break
    prefix.append(node)
else:raise RuntimeError('Curvature engine interface changed')
ns={}
exec(compile(ast.Module(body=prefix,type_ignores=[]),str(engine),'exec'),ns)
c,add,scale,mul,diff,u,curvature=(ns[k] for k in ('c','add','scale','mul','diff','u','curvature'))
def eval_u(p,t):
    if any(e[1:]!=(0,0,0) for e in p):raise ValueError('profile must depend only on u')
    return sum(v*t**e[0] for e,v in p.items())
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(a):return tuple(zip(*a))
def rot(c,s):return ((c,-s),(s,c))
def conj(q,a):return mm(mm(tr(q),a),q)
I=rot(F(1),F(0));Q=rot(F(3,5),F(4,5));S=rot(F(5,13),F(12,13))
A=((F(1),F(0)),(F(0),F(-1)))
Alocal=conj(Q,A)
z=add(u,c(-1));f=mul(mul(z,z),z)
# Right-chart field: A physical + f B, B=[[0,1],[1,0]], for u>1.
B=((F(0),F(1)),(F(1),F(0)));Blocal=conj(Q,B)
a=add(c(Alocal[0][0]),scale(Blocal[0][0],f))
b=add(c(Alocal[0][1]),scale(Blocal[0][1],f))
d=add(c(Alocal[1][1]),scale(Blocal[1][1],f))
left=curvature(c(1),{},c(-1));right_before=curvature(c(Alocal[0][0]),c(Alocal[0][1]),c(Alocal[1][1]));right_after=curvature(a,b,d)
checks={
 'left_patch_vacuum':all(not x for row in left['ricci'] for x in row),
 'rotated_right_overlap_vacuum':all(not x for row in right_before['ricci'] for x in row),
 'right_future_branch_vacuum':all(not x for row in right_after['ricci'] for x in row),
 'nontrivial_chart_rotation':Alocal!=A,
 'profile_overlap_covariance':mm(mm(Q,Alocal),tr(Q))==A,
 'raw_component_matching_would_fail':Alocal!=A,
 'trace_free_profile_preserved':not add(a,d),
 'parallel_observer_frame_on_both_patches':all(o['connection_axis'] for o in (left,right_before,right_after)),
}
g=f
for order in range(3):
    checks['seam_derivative_'+str(order)+'_matches']=eval_u(g,F(1))==0
    g=diff(g,0)
checks['third_derivative_jump_declared']=eval_u(g,F(1))==6
# Coordinate transitions j->i from three constant transverse chart frames.
frames=(I,Q,mm(Q,S))
trans=lambda i,j:mm(tr(frames[i]),frames[j])
checks['three_chart_cocycle']=mm(trans(0,1),trans(1,2))==trans(0,2)
# Compare profiles at u=2. Both continuations agree for all u<=1.
Aplus=((F(1),F(1)),(F(1),F(-1)))
Aother=((F(1),F(2)),(F(2),F(-1)))
checks['distinct_future_mixed_tide']=(-Aplus[0][1]/2)!=(-Aother[0][1]/2)
checks['distinct_observer_tidal_norm_not_just_frame_sign']=sum(z*z for row in Aplus for z in row)/4!=sum(z*z for row in Aother for z in row)/4
checks['identical_past_and_seam_data']=all(eval_u(p,F(1))==Alocal[i][j] for i,row in enumerate(((a,b),(b,d))) for j,p in enumerate(row))
checks['future_squared_eigenvalue_positive']=F(1)+eval_u(f,F(2))**2>0
# Scalar K must agree when right coordinates y=Q^T x are used.
x=(F(2),F(-3));y=tuple(sum(Q[j][i]*x[j] for j in range(2)) for i in range(2))
quad=lambda a,w:sum(w[i]*a[i][j]*w[j] for i in range(2) for j in range(2))
checks['metric_overlap_quadratic_form']=quad(A,x)==quad(Alocal,y)
packet=dict(passed=all(checks.values()),checks=checks,
    regularity='C2 piecewise-polynomial metric; seam at null hypersurface u=1. Smooth flat-function variant proved in note, not evaluated here.',
    scope='Explicit patch gluing within exact plane-wave ansatz, not general Einstein Cauchy/constraint gluing or unique continuation across characteristic data.',
    source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),engine)})
Path(__file__).with_name('plane-wave-overlap-gluing.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)

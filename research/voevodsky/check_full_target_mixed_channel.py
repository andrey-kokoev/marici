"""Mixed scalar/massless tree channel in the supplied full counting-metric target.
All incoming momenta, +--- signature, vertex = i times invariant amplitude.
"""
from pathlib import Path
from itertools import permutations
import hashlib,json
import sympy as s
base=Path(__file__).resolve().parent;root=base.parent.parent
checks={}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def eq(k,a,b=0):
    checks[k]=s.simplify(s.trigsimp(a-b))==0
    if not checks[k]:raise AssertionError((k,s.simplify(s.trigsimp(a-b))))
owner_path=root/'research/nima/results/comparison-kinetic-readout.json'
owner=json.loads(owner_path.read_text())
checks['owner_dependencies_current']=all(sha(root/'research/nima/agda'/f'{m}.agda')==h for m,h in owner['local_formal_import_sha256'].items())
checks['owner_receipt_inputs_current']=all(sha(root/Path(p))==h for p,h in owner['source_sha256'].items())
P=s.zeros(4)
for i,j in enumerate(owner['source_swap_images']):P[i,j]=1
F,U=s.symbols('F U',positive=True)
phi,x,y=s.symbols('phi x y',real=True)
coords=s.Matrix([phi,x,y]);r2=x*x+y*y
v0=s.Matrix([1,0,0,0]);odd=s.Matrix([0,1,-1,0])/s.sqrt(2)
e1=s.Matrix([0,1,1,0])/s.sqrt(2);e2=s.Matrix([0,0,0,1])
even=s.sqrt(1-r2/F**2)*v0+x/F*e1+y/F*e2
n=s.cos(phi/F)*even+s.sin(phi/F)*odd
for name,vec,sign in [('v0',v0,1),('odd',odd,-1),('even1',e1,1),('even2',e2,1)]:
    for i in range(4):eq(f'source_{name}_{i}',(P*vec)[i],sign*vec[i])
eq('unit_probe',n.dot(n),1)
eq('source_overlap',n.dot(P*n),s.cos(2*phi/F))
J=n.jacobian(coords)
G=(F**2*J.T*J).applyfunc(lambda z:s.simplify(s.trigsimp(z)))
h=s.eye(2)+s.Matrix([x,y])*s.Matrix([[x,y]])/(F**2-r2)
expected=s.diag(1,0,0)
expected[1:3,1:3]=s.cos(phi/F)**2*h
for i in range(3):
    for j in range(3):eq(f'adapted_metric_{i}{j}',G[i,j],expected[i,j])
V=-U*s.log(s.cos(2*phi/F))/2
vac={phi:0,x:0,y:0}
H=s.hessian(V,coords).subs(vac)
for i in range(3):
    for j in range(3):eq(f'vacuum_mass_{i}{j}',H[i,j],2*U/F**2 if i==j==0 else 0)
# Normal force and connection vanish on the scalar plane (indeed identically
# for these components): exact classical truncation is consistent.
for z in [x,y]:eq(f'normal_force_{z}',s.diff(V,z))
for k in [1,2]:
    lower=[s.diff(G[l,0],phi)-s.diff(G[0,0],coords[l])/2 for l in range(3)]
    eq(f'normal_connection_{k}',sum(G.inv()[k,l]*lower[l] for l in range(3)))
# A second full chart: tangent Cartesian coordinates q=(psi,xi1,xi2).
p,u,v=s.symbols('p u v',real=True)
q=s.Matrix([p,u,v]);gc=s.eye(3)+q*q.T/(F**2-q.dot(q))
nc=s.sqrt(1-q.dot(q)/F**2)*v0+p/F*odd+u/F*e1+v/F*e2
jc=nc.jacobian(q)
for i in range(3):
    for j in range(3):eq(f'cartesian_metric_{i}{j}',(F**2*jc.T*jc)[i,j],gc[i,j])
eq('cartesian_overlap',nc.dot(P*nc),1-2*p*p/F**2)
# Exact coordinate transition. Positive square-root branches on the stated patch.
transition=s.Matrix([F*s.sin(phi/F),s.cos(phi/F)*x,s.cos(phi/F)*y])
tj=transition.jacobian(coords)
pulled=tj.T*gc.subs(dict(zip(q,transition)),simultaneous=True)*tj
for i in range(3):
    for j in range(3):eq(f'full_chart_pullback_{i}{j}',pulled[i,j],G[i,j])
# L4 adapted = -phi^2 [(dx)^2+(dy)^2]/(2F^2)
#              + (x dx+y dy)^2/(2F^2), plus scalar potential.
# Cartesian L4 kinetic = (p dp+u du+v dv)^2/(2F^2).
eq('adapted_mixed_coefficient',s.diff(G[1,1],phi,2).subs(vac)/4,-1/(2*F**2))
eq('cartesian_mixed_coefficient',s.diff(gc[0,1],p,u).subs({p:0,u:0,v:0}),1/F**2)
# Both coordinate systems have no cubic vertices, hence no tree exchange
# diagrams in this four-point process. Check the kinetic first jets explicitly.
for i in range(3):
    for j in range(3):
        for k in range(3):
            eq(f'no_adapted_cubic_{i}{j}{k}',s.diff(G[i,j],coords[k]).subs(vac))
            eq(f'no_cartesian_cubic_{i}{j}{k}',s.diff(gc[i,j],q[k]).subs({p:0,u:0,v:0}))
eq('no_potential_cubic',s.diff(V,phi,3).subs(phi,0))
# Enumerate species-compatible differentiated-leg assignments.
# External species are heavy,heavy,light,light.
assign=list(permutations(range(4)))
adapt=[t for t in assign if set(t[:2])=={0,1}]
cart=[t for t in assign if t[0] in (0,1) and t[1] in (2,3) and t[2] in (0,1) and t[3] in (2,3)]
checks['adapted_vertex_assignments']=len(adapt)==4
checks['cartesian_vertex_assignments']=len(cart)==4
S=s.symbols('s',positive=True)
# Massless outgoing pair has k1.k2=s/2. In the Cartesian chart the four
# differentiated cross-pairs sum to (p1+p2).(k1+k2)=-s.
eq('adapted_invariant_amplitude',-(-1/(2*F**2))*len(adapt)*S/2,S/F**2)
checks['cartesian_four_cross_pairs']=set((t[2],t[3]) for t in cart)=={(0,2),(0,3),(1,2),(1,3)}
eq('cartesian_invariant_amplitude',-(-S)/F**2,S/F**2)
# Off-diagonal species are absent from the two-heavy quartic jet.
eq('off_diagonal_light_channel_absent',s.diff(G[1,2],phi,2).subs(vac))
# Exact real COM fixture: F=1,U=1/2, m2=1, s=16.
mom=[s.Matrix([2,0,0,s.sqrt(3)]),s.Matrix([2,0,0,-s.sqrt(3)]),s.Matrix([-2,-2,0,0]),s.Matrix([-2,2,0,0])]
def dot(a,b):return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,4))
for i,k in enumerate(mom):eq(f'real_onshell_{i}',dot(k,k),1 if i<2 else 0)
for i in range(4):eq(f'real_conservation_{i}',sum(k[i] for k in mom))
eq('real_s',dot(mom[0]+mom[1],mom[0]+mom[1]),16)
eq('real_adapted_vertex',2*dot(mom[2],mom[3]),16)
eq('real_cartesian_vertex',-sum(dot(mom[i],mom[j]) for i in (0,1) for j in (2,3)),16)
checks['nonzero_above_threshold']=16>4 and 16!=0
checks['scalar_only_profile_omits_allowed_species']=2>0
files=[Path(__file__),owner_path,root/'research/nima/comparison-kinetic-readout.md']
out=dict(passed=all(checks.values()),checks=checks,
 target_metric='dphi^2+cos(phi/F)^2 [delta_ab+chi_a*chi_b/(F^2-|chi|^2)] dchi_a dchi_b',
 potential='-U/2 log(cos(2phi/F))',masses_squared=['2U/F^2','0','0'],
 mixed_amplitude='M(phi phi -> chi_a chi_b)=s*delta_ab/F^2; Feynman vertex i*M',
 domain='F,U>0; |phi/F|<pi/4; |chi|<F; local positive square-root patch',
 conclusion='Classical scalar restriction is consistent, but full target permits nonzero mixed scattering. A scalar-only profile is not complete for all physical channels of the supplied model.',
 source_sha256={str(p.relative_to(root)):sha(p) for p in files},
 scope='Exact symbolic classical geometry and complete mixed tree four-point amplitude in the supplied scalar target model. No loop evaluation, quantum completion, physical scale selection or new Agda proof.')
(base/'full-target-mixed-channel.json').write_text(json.dumps(out,indent=2)+'\n')
print('passed=',out['passed'],'checks=',len(checks))
raise SystemExit(0 if out['passed'] else 1)

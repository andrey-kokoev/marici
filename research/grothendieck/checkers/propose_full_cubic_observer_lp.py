"""Numerical candidate only. The leading-window reduction requires certification."""
from pathlib import Path
import runpy,json,math
import numpy as np
from scipy.sparse import coo_matrix,eye,hstack,vstack
from scipy.optimize import linprog
from numpy.polynomial.laguerre import laggauss

ROOT=Path(__file__).resolve().parents[3]
audit=runpy.run_path(str(Path(__file__).with_name('audit_cubic_analytical_shapes.py')))
columns=audit['columns'];shapes=list(audit['shape_rows']);shape_index={s:i for i,s in enumerate(shapes)}
primes=[2,3,5,7,11,13]
def vertex(mask):
    out=2
    for i,p in enumerate(primes):
        if mask&(1<<i):out*=p
    return out
nodes,weights=laggauss(64)
def mean(A):
    t0=math.pi*A*A;t=t0+nodes
    density=(t-1.5)/t0*((t/t0)**1.75+A**(-6)*(t/t0)**(-1.25))
    x=np.log(t/math.pi)/2
    return float(np.dot(weights,density*x*np.tanh(3*x))/np.dot(weights,density))
L=0.13668992788637229;means={}
row=[];col=[];values=[];starts=[]
for j,data in enumerate(columns):
    start=0;locations=[]
    for pair,kind in zip(data['pairs'],data['kinds']):
        if kind:locations.append(vertex(start))
        start|=sum(1<<p for p in pair)
    starts.append(locations)
    for A in locations:means.setdefault(A,mean(A))
    q1,q2=[means[A]-L for A in locations]
    for shape,sign,windows in data['entries']:
        if [vertex(w[0]) for w in windows]!=locations:continue
        r=4*shape_index[shape]
        for k,value in enumerate([1.,q2,q1,q1*q2]):
            row.append(r+k);col.append(j);values.append(sign*value)
M=coo_matrix((values,(row,col)),shape=(4*len(shapes),270)).tocsr()
active=np.asarray(M.getnnz(axis=1)).ravel()>0
original_indices=np.flatnonzero(active);M=M[active]
C=2.;h=1/math.sqrt(8)
w=np.asarray([C*C,C*h,C*h,h*h])[original_indices%4]
m=M.shape[0]
Aub=vstack([hstack([M,-eye(m)]),hstack([-M,-eye(m)])],format='csr')
objective=np.r_[np.zeros(270),w]
bounds=[(None,None)]*270+[(0,None)]*m
bounds[18]=(1.,1.)
sol=linprog(objective,A_ub=Aub,b_ub=np.zeros(2*m),bounds=bounds,method='highs',
            options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
assert sol.success,sol.message
source=sol.x[:270]
z=sol.ineqlin.marginals[m:]-sol.ineqlin.marginals[:m]
if (M.T@z)[18]<0:z=-z
z=z/(M.T@z)[18]
residual=np.asarray(M.T@z).ravel();residual[18]-=1
assert np.max(np.abs(residual))<1e-7
out={'schema':'marici.grothendieck.full-cubic-lp-proposal.v1','certified':False,
     'analytical_shapes':len(shapes),'active_scalar_rows':m,'source_columns':270,
     'C_even_proposal':C,'h_proposal':h,'mean_proposals':{str(k):v for k,v in means.items()},
     'source_block_starts':starts,'leading_minimum_image_norm':float(sol.fun),
     'leading_observer_norm':float(np.max(abs(z)/w)),
     'numerical_max_constraint_residual':float(np.max(abs(residual))),
     'source_proposal':source.tolist(),
     'observer_nonzero_rows':[[int(original_indices[i]),float(z[i])] for i in range(m) if abs(z[i])>1e-15],
     'scope':'Candidate for full analytical-block LP after leading-window approximation. No interval feasibility or optimality is asserted by this file.'}
p=ROOT/'research/grothendieck/results/full-cubic-lp-proposal.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['source_proposal','observer_nonzero_rows','source_block_starts','mean_proposals']},indent=2))

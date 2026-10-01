"""Record boundary, conserved transport, and a local phase-covariant trial.

Four vertices, six oriented links, integer record currents, and complex carrier
amplitudes. Hop strengths are explicit inputs. This constructs a discrete
U(1)-covariant matter transport interface, not Maxwell or particle physics.
"""
from itertools import combinations, product

vertices=range(4)
links=list(combinations(vertices,2))
B=[[int(v==b)-int(v==a) for a,b in links] for v in vertices]


def boundary(j):
    return [sum(row[e]*j[e] for e in range(6)) for row in B]


def path_current(path):
    j=[0]*6
    for a,b in zip(path,path[1:]):
        edge=(min(a,b),max(a,b))
        j[links.index(edge)] += 1 if a<b else -1
    return j


for length in range(1,5):
    for path in product(vertices,repeat=length+1):
        if any(a==b for a,b in zip(path,path[1:])): continue
        j=path_current(path)
        assert boundary(j)==[int(v==path[-1])-int(v==path[0]) for v in vertices]
        assert sum(boundary(j))==0
assert path_current((0,1,0)) == [0]*6  # current cancels, two traversal records remain

psi=[1+2j,2-1j,-1+1j,3+0j]
U=[1j,1,-1j,-1,1j,1]
kappa=[1,2,3,4,5,6]


def transport(psi,U,kappa):
    H=0.
    derivative=[0j]*4  # derivative of H w.r.t. conjugate psi
    currents=[]
    for (a,b),u,k in zip(links,U,kappa):
        error=psi[b]-u*psi[a]
        H += k*abs(error)**2
        derivative[b] += k*error
        derivative[a] -= k*u.conjugate()*error
        currents.append(2*k*(psi[b].conjugate()*u*psi[a]).imag)
    velocity=[-1j*x for x in derivative]
    rho_dot=[2*(p.conjugate()*v).real for p,v in zip(psi,velocity)]
    assert max(abs(x+y) for x,y in zip(rho_dot,boundary(currents))) < 1e-10
    assert abs(sum(rho_dot)) < 1e-10
    return H,currents,velocity


H,J,velocity=transport(psi,U,kappa)
phases=(1+0j,1j,-1+0j,-1j)
for gauge in product(phases,repeat=4):
    transformed_psi=[g*p for g,p in zip(gauge,psi)]
    transformed_U=[gauge[b]*u*gauge[a].conjugate() for (a,b),u in zip(links,U)]
    h,j,v=transport(transformed_psi,transformed_U,kappa)
    assert abs(h-H)<1e-10
    assert max(abs(x-y) for x,y in zip(j,J))<1e-10
    assert max(abs(x-g*y) for x,g,y in zip(v,gauge,velocity))<1e-10
    # Gauge-invariant oriented triangle product U01*U12*conjugate(U02).
    tri=U[0]*U[3]*U[1].conjugate()
    tri2=transformed_U[0]*transformed_U[3]*transformed_U[1].conjugate()
    assert abs(tri-tri2)<1e-10
# Field-independent scaling of the entire hopping action is still free.
h2,j2,v2=transport(psi,U,[2*k for k in kappa])
assert abs(h2-2*H)<1e-10
assert max(abs(x-2*y) for x,y in zip(j2,J))<1e-10
# Family aggregation transports current weights; count members rather than
# assigning a single unit of charge/current to a fresh family label.
paths=[(0,1,2),(0,3,2),(1,3)]
aggregate=[sum(path_current(p)[e] for p in paths) for e in range(6)]
assert boundary(aggregate)==[sum(boundary(path_current(p))[v] for p in paths) for v in vertices]
print('All composable paths of lengths1..4 satisfy the endpoint continuity law.')
print('256 local phase changes preserve hopping energy, link currents, triangle holonomy, and covariant velocity.')
print('Schrodinger hopping evolution conserves total |psi|^2 and satisfies rho_dot+B J=0.')
print('Retained-family aggregation preserves current boundary exactly.')
print('Doubling all hopping strengths doubles response while preserving every gauge and continuity identity.')
print('Physical electric charge assignment, link-field dynamics, spacetime propagation, and coupling normalization remain inputs.')

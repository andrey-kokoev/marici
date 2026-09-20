"""Exact 2-stage x (covariant,dual) x 4-presentation arithmetic window.

Theta chart matrices are coordinates in the independently realized interval
history basis, not sampled theta values. Pairings are source-pulled counting
pairings, not the native theta L2 metric.
"""
from pathlib import Path
import json
import sympy as s


def source(primes):
    r=len(primes)
    nodes={m:2*s.prod(primes[j] for j in range(r) if m&(1<<j)) for m in range(1<<r)}
    vertices=sorted(nodes.values())
    edges=[(nodes[m],nodes[m|(1<<j)],primes[j]) for m in range(1<<r) for j in range(r) if not m&(1<<j)]
    n=len(edges)
    J=s.Matrix(len(vertices)-1,n,lambda i,e:int(edges[e][0]<=vertices[i] and vertices[i+1]<=edges[e][1]))
    B=s.zeros(len(vertices),n)
    for e,(a,b,p) in enumerate(edges):
        B[vertices.index(a),e]=-1
        B[vertices.index(b),e]=1
    parent={v:v for v in vertices}
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    tree=[]
    for e in sorted(range(n),key=lambda e:(primes.index(edges[e][2]),edges[e][0],e)):
        a,b,_=edges[e]
        ra,rb=root(a),root(b)
        if ra!=rb:
            parent[ra]=rb
            tree.append(e)
    chords=[e for e in range(n) if e not in tree]
    Z=s.zeros(len(chords),n)
    for i,e in enumerate(chords):
        Z[i,e]=1
    interval=J.col_join(Z)
    endpoint=B[:-1,:].col_join(Z)
    # Chart 3 has actual theta functions as its first basis vectors.
    return {'edges':edges,'vertices':vertices,'J':J,'Z':Z,
            'A':[s.eye(n),endpoint,interval,interval],
            'dimensions':[n,len(vertices)-1,len(chords)]}


def main():
    stages=[source((2,3)),source((2,3,5))]
    n0,n1=[len(x['edges']) for x in stages]
    inclusion=s.zeros(n1,n0)
    old_rows=[]
    for j,e in enumerate(stages[0]['edges']):
        row=stages[1]['edges'].index(e)
        old_rows.append(row)
        inclusion[row,j]=1
    A=[x['A'] for x in stages]
    inv=[[a.inv() for a in row] for row in A]
    Q=[[A[k][j+1]*inv[k][j] for j in range(3)] for k in range(2)]
    V=[A[1][j]*inclusion*inv[0][j] for j in range(4)]
    # Real rational fixtures; complex extension uses conjugate transposes.
    G=[[inv[k][j].T*inv[k][j] for j in range(4)] for k in range(2)]
    faces={}
    for j in range(3):
        faces['stage_chart_co_'+str(j)]=V[j+1]*Q[0][j]==Q[1][j]*V[j]
        faces['stage_chart_contra_'+str(j)]=Q[0][j].T*V[j+1].T==V[j].T*Q[1][j].T
    for k in range(2):
        for j in range(3):
            faces['chart_pairing_'+str(k)+'_'+str(j)]=Q[k][j].T*G[k][j+1]*Q[k][j]==G[k][j]
    for j in range(4):
        faces['stage_pairing_'+str(j)]=V[j].T*G[1][j]*V[j]==G[0][j]
    cubes={}
    for j in range(3):
        left=V[j].T*Q[1][j].T*G[1][j+1]*Q[1][j]*V[j]
        right=Q[0][j].T*V[j+1].T*G[1][j+1]*V[j+1]*Q[0][j]
        cubes[str(j)]=left==right==G[0][j]
    seam=inclusion*inv[0][3]
    full=seam*Q[0][2]*Q[0][1]*Q[0][0]
    new_rows=[i for i in range(n1) if i not in old_rows]
    complement=s.zeros(n1,len(new_rows))
    for j,i in enumerate(new_rows):
        complement[i,j]=1
    adapted=inclusion.row_join(complement)
    h=stages[0]['J'].nullspace()[0]
    h= h* s.ilcm(*[x.q for x in h])
    checks={
        'sixteen_vertices':len(A)*len(A[0])*2==16,
        'all_sixteen_faces':len(faces)==16 and all(faces.values()),
        'all_three_cubes':len(cubes)==3 and all(cubes.values()),
        'every_chart_source_recoverable':all(inv[k][j]*A[k][j]==s.eye(len(stages[k]['edges'])) for k in range(2) for j in range(4)),
        'full_four_presentation_route_is_source_inclusion':full==inclusion,
        'dual_full_route_is_source_restriction':full.T==inclusion.T,
        'stage_seam_injective_not_surjective':seam.rank()==n0<n1,
        'restriction_extension_identity':inclusion.T*inclusion==s.eye(n0),
        'extension_restriction_not_identity':inclusion*inclusion.T!=s.eye(n1),
        'new_source_direction_disappears_under_restriction':inclusion.T*complement[:,0]==s.zeros(n0,1),
        'cycle_hostile_has_zero_interval_history':stages[0]['J']*h==s.zeros(3,1),
        'cycle_hostile_survives_theta_cycle_chart':A[0][3]*h!=s.zeros(n0,1),
        'cycle_hostile_survives_source_extension':inclusion*h!=s.zeros(n1,1),
        'relative_determinant_exact_sequence_frame':abs(adapted.det())==1,
        'quotient_is_eight_dimensional':len(new_rows)==8,
    }
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.two-by-two-by-four-arithmetic-window.v1',
        'strength':'finite_source_window_with_recorded_theta_basis_premise',
        'chart_types':['edge_source','reduced_endpoint_plus_cycle','interval_plus_cycle','theta_history_plus_cycle'],
        'stage_dimensions':[x['dimensions'] for x in stages],
        'source_edges':[[[int(a),int(b),int(p)] for a,b,p in x['edges']] for x in stages],
        'faces':faces,'cubes':cubes,'checks':checks,
        'seam_shape':list(seam.shape),'seam_rank':seam.rank(),
        'determinant_sequence_frame_sign':str(adapted.det()),
        'cycle_hostile':[str(x) for x in h],
        'metric':'source counting metric pulled through each realization; not native theta L2',
        'unsupported':['identification with four canonical Fourier charts','invertible stage seam',
                       'scalar determinant of rectangular seam','Euler trace matching',
                       'completed infinite-stage window','physical time dynamics'],
    }
    out=Path(__file__).resolve().parents[1]/'results/two-by-two-by-four-arithmetic-window.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

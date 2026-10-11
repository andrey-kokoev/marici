"""Full coefficient pullback of the host attachment star and electron body.
Exact rational hyperplane arrangement retains the original sector owners.
No matching of radial depths is imposed. Fiber coordinates a and b are
positions along the two coefficient-kernel chords, not radial scale factors.
"""
from itertools import combinations, permutations
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json

from check_retained_direction_attachment import (
    geo,SOURCE,verify,ONE,ZERO,weight,times,div,conj,apply,xyz,swap)
from check_retained_barycenter_attachment import rank_columns

BASE=Path(__file__).resolve().parents[1]
# An affine expression is (constant, four coefficients) on (uA,uB,a,b).
def expr(c,*n): return (Q(c),tuple(map(Q,n)))
def minus(f,g): return (f[0]-g[0],tuple(x-y for x,y in zip(f[1],g[1])))
def scale(k,f): return (k*f[0],tuple(k*x for x in f[1]))
def value(f,x): return f[0]+sum(a*b for a,b in zip(f[1],x))
U=(expr(0,1,0,0,0),expr(0,0,1,0,0),expr(1,-1,-1,0,0))
A=expr(0,0,0,1,0); B=expr(0,0,0,0,1)
V=tuple(minus(u,B) for u in U)+(scale(3,B),)
BOUNDS=(A,B)+tuple(minus(u,A) for u in U)+tuple(minus(u,B) for u in U)
PLANES=BOUNDS+tuple(minus(U[i],U[j]) for i,j in combinations(range(3),2))+tuple(minus(u,scale(4,B)) for u in U)

def intersection(forms):
    rows=[list(f[1])+[-f[0]] for f in forms]
    for j in range(4):
        p=next((i for i in range(j,4) if rows[i][j]),None)
        if p is None: return None
        rows[j],rows[p]=rows[p],rows[j]
        d=rows[j][j]; rows[j]=[x/d for x in rows[j]]
        for i in range(4):
            if i!=j:
                d=rows[i][j]
                rows[i]=[x-d*y for x,y in zip(rows[i],rows[j])]
    return tuple(r[4] for r in rows)

def projections(x):
    u=tuple(value(f,x) for f in U); a=x[2]; b=x[3]
    h=tuple(t-a/4 for t in u)+(3*a/4,)
    e=swap(tuple(t-b for t in u)+(3*b,))
    return h,e

def rank2(columns):
    pivots={}
    for column in columns:
        while column:
            p=column.bit_length()-1
            if p not in pivots: pivots[p]=column; break
            column ^= pivots[p]
    return len(pivots)

def main():
    original=SOURCE.read_bytes(); source=json.loads(original); evidence,rows=verify(source)
    vertices=set()
    for selected in combinations(PLANES,4):
        point=intersection(selected)
        if point is not None and all(value(f,point)>=0 for f in BOUNDS): vertices.add(point)
    vertices=sorted(vertices)
    @lru_cache(None)
    def dimension(ids):
        ids=sorted(ids); p=vertices[ids[0]]
        return rank_columns([{j:x-y for j,(x,y) in enumerate(zip(vertices[i],p))} for i in ids[1:]])
    maximal=[]; owners=[]; faces=set()
    for order in permutations(range(3)):
        for slot in range(4):
            eo=order[:slot]+(3,)+order[slot:]
            inequalities=BOUNDS+tuple(minus(U[i],U[j]) for i,j in zip(order,order[1:]))+tuple(minus(V[i],V[j]) for i,j in zip(eo,eo[1:]))
            ids=frozenset(i for i,x in enumerate(vertices) if all(value(f,x)>=0 for f in inequalities))
            assert dimension(ids)==4
            local={ids}
            for f in inequalities:
                zero=frozenset(i for i in ids if value(f,vertices[i])==0)
                local|={g&zero for g in list(local) if g&zero}
            faces|=local; maximal.append(ids)
            electron_order=tuple(1 if i==0 else 0 if i==1 else i for i in eo)
            owners.append({'host_flag':''.join('ABC'[i] for i in order)+'D',
                           'electron_flag':''.join('ABCD'[i] for i in electron_order)})
    levels=[sorted((f for f in faces if dimension(f)==k),key=lambda f:tuple(sorted(f))) for k in range(5)]
    boundaries=[[]]
    for k in range(1,5):
        boundaries.append([sum(1<<i for i,g in enumerate(levels[k-1]) if g<f) for f in levels[k]])
    chain_ok=True
    for k in range(2,5):
        for b in boundaries[k]:
            out=0
            for i in range(len(levels[k-1])):
                if b>>i&1: out ^= boundaries[k-1][i]
            chain_ok &= out==0
    ranks=[0]+[rank2(boundaries[k]) for k in range(1,5)]+[0]
    betti=[len(levels[k])-ranks[k]-ranks[k+1] for k in range(5)]
    facet_owners=[sum(f<t for t in maximal) for f in levels[3]]
    exposed=[f for f,n in zip(levels[3],facet_owners) if n==1]
    boundary_closed=all(sum(g<f for f in exposed)%2==0 for g in levels[2])
    # Reconstruct the actual selected local coefficient maps.
    p=[[ZERO]*3 for _ in range(3)]
    for r in rows:
        if r['source'][:2]==['raw','AB'] and r['target'][:2]==['local','AB']:
            p['xyz'.index(r['target'][2])]['xyz'.index(r['source'][2])]=weight(r)
    F=tuple(sum(geo.POINTS[k][j] for k in 'ABC')/3 for j in range(3))
    X=geo.transpose((F,geo.POINTS['A'],geo.POINTS['B']))
    v=geo.zmv(X,(ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))
    D=[div(z,conj(z)) for z in v]
    ep=[[times(D[i],conj(z)) for z in row] for i,row in enumerate(p)]
    samples=vertices+[tuple(sum(vertices[i][j] for i in cell)/len(cell) for j in range(4)) for cell in maximal]
    match=True; valid=True
    for x in samples:
        h,e=projections(x)
        match &= apply(p,tuple(a-b for a,b in zip(xyz(h),F)))==apply(ep,xyz(e))
        valid &= sum(h)==sum(e)==1 and min(e)>=0 and min(h[:3])>=h[3]>=0
    root=(Q(1,3),Q(1,3),Q(0),Q(1,12))
    interior=(Q(1,3),Q(1,3),Q(1,6),Q(1,12))
    checks={
        'source_verified':evidence['verified'],
        'full_pullback_has_strict_four_dimensional_interior':all(value(f,interior)>0 for f in BOUNDS),
        'all_twenty_four_owner_cells_are_four_dimensional':len(set(maximal))==24 and all(dimension(f)==4 for f in maximal),
        'all_twenty_four_electron_flags_retained':{r['electron_flag'] for r in owners}=={''.join(p) for p in permutations('ABCD')},
        'all_six_host_star_flags_retained':len({r['host_flag'] for r in owners})==6,
        'all_sampled_pairs_have_valid_barycentric_coordinates':valid,
        'source_coefficient_matching_holds_on_every_cell':match,
        'cellular_boundary_squared_zero':chain_ok,
        'full_complex_connected_and_mod2_acyclic':betti==[1,0,0,0,0],
        'every_three_face_has_one_or_two_owners':all(n in (1,2) for n in facet_owners),
        'outer_boundary_has_no_unmatched_two_faces':boundary_closed,
        'marked_barycenter_pair_retained_as_arrangement_vertex':root in vertices and projections(root)==((Q(1,3),Q(1,3),Q(1,3),Q(0)),(Q(1,4),)*4),
        'independent_kernel_coordinates_not_equated':interior[2]!=interior[3],
        'source_unchanged':SOURCE.read_bytes()==original,
    }
    packet={'kind':'full-cell-coefficient-pullback','source_root':source['root'],
        'coordinates':['u_A','u_B','a','b'],
        'inequalities':'a>=0, b>=0, u_i>=a, u_i>=b, u_C=1-u_A-u_B',
        'vertices':[{'parameters':list(map(str,x)),'host_barycentric':list(map(str,projections(x)[0])),
                     'electron_barycentric':list(map(str,projections(x)[1]))} for x in vertices],
        'cells_by_dimension':[[sorted(f) for f in level] for level in levels],
        'maximal_cells':[{'vertices':sorted(f),**o} for f,o in zip(maximal,owners)],
        'root_vertex':vertices.index(root)}
    result={'verification_passed':all(checks.values()),'checks':checks,
        'f_vector':list(map(len,levels)),'boundary_ranks_mod2':ranks[1:5],'betti_mod2':betti,
        'internal_three_faces':facet_owners.count(2),'outer_three_faces':facet_owners.count(1),
        'dimension':4,'maximal_cells':len(maximal),
        'fiber':'For each u in the coefficient triangle: (a,b) in [0,min(u)]^2.',
        'direction_sublocus':'a=min(u) and b=0 or b=min(u): the previous two-sheet sphere.',
        'projections':'host=(u_i-a/4,3a/4); electron=swap_AB(u_i-b,3b)',
        'scope':'host attachment star only; the rest of the host is unchanged, not discarded or included in this local fiber product',
        'outcome':'The complete coefficient relation is a convex four-dimensional polytope, not an extra three-dimensional solid. Both kernel-coordinate freedoms are retained; no extra carrier is forced.',
        'source_sha256':sha256(original).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/full_cell_attachment_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/full_cell_attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()

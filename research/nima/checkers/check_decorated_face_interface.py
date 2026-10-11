"""Native pair couplings through source-selected decorated face records.

The record carries two tangent coordinates, one normal coordinate, and a
separately tagged collective scalar. This is a linear coefficient interface,
not an assertion of a new geometric simplex filler or a particle mass.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import hashlib
from check_1836_pair_face_factorization import Z, ONE, add, mul, sumz, rank
from check_wg_reservoir_completion import solve
from check_twelve_triangle_positive_geometry import POINTS, mean, transpose, zmv, OMEGA, zmul, zconj

ROOT=Path(__file__).resolve().parents[1]


def real(a):return [[(F(x),F(0)) for x in row] for row in a]
def mm(a,b):return [[sumz(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def identity(n):return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def rinv(a):return [list(row) for row in zip(*(solve(a,[F(i==j) for i in range(3)]) for j in range(3)))]
def diag4(a):return [row+[Z] for row in a]+[[Z,Z,Z,ONE]]


def main():
    ap=ROOT/'results/twelve-triangle-1836-arrows.json'
    gp=ROOT/'results/twelve-triangle-positive-geometry.json'
    arrows=json.loads(ap.read_bytes());geometry=json.loads(gp.read_bytes())
    owners={r['outer_arrow']:r['triangle'][0].removeprefix('F_') for r in geometry['triangles_and_transports']}
    rotations={r['outer_arrow']:[[F(x) for x in row] for row in r['rotation']] for r in geometry['triangles_and_transports']}
    faces=sorted(set(owners.values()))
    labels={f:sorted(g for g,p in owners.items() if p==f) for f in faces}
    val={(tuple(a['source']),tuple(a['target'])):(F(a['weight_real']),F(a['weight_imag_sqrt3'])) for a in arrows}
    x0=transpose((mean([POINTS[k] for k in 'ABC']),POINTS['A'],POINTS['B']))
    v0=zmv(x0,(ONE,OMEGA,zmul(OMEGA,OMEGA)))
    modes={g:zmv(rotations[g],v0) for g in owners}
    bases={};inverses={};results=[]
    for fa,fb in combinations(faces,2):
        va,vb=sorted(set(fa)&set(fb))
        a,b=POINTS[va],POINTS[vb]
        normal=(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
        basis=[list(row) for row in zip(a,b,normal)]
        inverse=rinv(basis)
        key='/'.join((fa,fb));bases[key]=basis;inverses[key]=inverse
        assert mm(real(basis),real(inverse))==identity(3)
        assert mm(real(inverse),real(basis))==identity(3)
        for source,target in [(fa,fb),(fb,fa)]:
            sp=[(g,i) for g in labels[source] for i in range(3)]
            tp=[(g,i) for g in labels[target] for i in range(3)]
            # Extract common-frame alignment coordinates, then resolve them
            # into the two tangent and one normal basis vectors of Oab.
            aggregate=[[ (rotations[h][j][k]/12,F(0)) for h,j in sp] for k in range(3)]
            extract_g=mm(real(inverse),aggregate)
            lift_g=mm(real([[rotations[g][i][k] for k in range(3)] for g,i in tp]),real(basis))
            extract_n=[[tuple(v/80 for v in zconj(modes[h][j])) for h,j in sp]]
            lift_n=[[modes[g][i]] for g,i in tp]
            # Keep local-input and aligned-input stages separate.
            extract=[row+[Z]*9 for row in extract_g]+[[Z]*9+extract_n[0]]
            lift=[row+[Z] for row in lift_g]+[[Z,Z,Z]+row for row in lift_n]
            native_g=[[val.get((('local',h,'xyz'[j]),('aligned',g,'xyz'[i])),Z) for h,j in sp] for g,i in tp]
            native_n=[[val.get((('aligned',h,'xyz'[j]),('raw',g,'xyz'[i])),Z) for h,j in sp] for g,i in tp]
            native=[row+[Z]*9 for row in native_g]+[[Z]*9+row for row in native_n]
            assert mm(lift,extract)==native
            assert rank(extract)==rank(lift)==rank(native)==4
            # Independent channel controls: dropping either normal or scalar
            # loses original coefficients. Nothing is repaired by fitting.
            missing_normal=[row[:] for row in extract];missing_normal[2]=[Z]*18
            missing_scalar=[row[:] for row in extract];missing_scalar[3]=[Z]*18
            assert mm(lift,missing_normal)!=native
            assert mm(lift,missing_scalar)!=native
            results.append(dict(source=source,target=target,shared_face=['O',va,vb],
                                exact_reconstruction=True,interface_rank=4,
                                normal_required=True,collective_scalar_required=True))
    # Chart comparisons act on the same abstract four-channel interface.
    # T_new,old = diag(B_new^-1 B_old, 1). These are not compositions
    # of the original G/N operators, which have distinct stage domains.
    def transition(new,old):return diag4(mm(real(inverses[new]),real(bases[old])))
    keys=list(bases)
    for a in keys:assert transition(a,a)==identity(4)
    for a,b in product(keys,repeat=2):
        assert mm(transition(a,b),transition(b,a))==identity(4)
    for a,b,c in product(keys,repeat=3):
        assert mm(transition(c,b),transition(b,a))==transition(c,a)
    result=dict(schema='marici.nima.decorated-face-interface.v1',status='pass',
                arrow_source_sha256=hashlib.sha256(ap.read_bytes()).hexdigest(),
                geometry_source_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),
                interface='two tangent components + one normal component + a separately tagged collective scalar',
                construction='B_face=(vertex_a, vertex_b, vertex_a cross vertex_b); exact inverse; collective mode from original triangle coefficients',
                directed_pair_checks=results,charts=6,inverse_checks=36,cocycle_checks=216,
                controls=['deleting normal channel breaks reconstruction','deleting scalar channel breaks reconstruction'],
                disposition='All native cross-sector coefficients factor exactly through this rank-four decorated face record; its frame transitions satisfy exact cocycles.',
                residual='The face record retains full three-component frame information plus a stage-distinct scalar; it is not intrinsic tangent-face data or a derived internal quark. No global vertex/edge extension or mass readout is asserted.')
    out=ROOT/'results/decorated-face-interface.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

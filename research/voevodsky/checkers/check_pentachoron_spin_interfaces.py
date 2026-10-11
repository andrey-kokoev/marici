"""Geometry-derived spin interfaces for the boundary of a regular 4-simplex.
Exact arithmetic in Q(sqrt(2),sqrt(3),sqrt(5),i), without dependencies.
No projection coordinates, selected global rank, or fitted phases are used.
"""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from pathlib import Path
import json


class A:
    roots = (2, 3, 5, -1)

    def __init__(self, value=0):
        self.c = value.c if isinstance(value, A) else tuple(value) if isinstance(value, tuple) else (F(value),)+(F(0),)*15

    def __add__(self, other):
        other = A(other)
        return A(tuple(x+y for x,y in zip(self.c,other.c)))
    __radd__ = __add__

    def __neg__(self):
        return A(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + -A(other)

    def __rsub__(self, other):
        return A(other) + -self

    def __mul__(self, other):
        other = A(other)
        out = [F(0)]*16
        for i,x in enumerate(self.c):
            if not x:
                continue
            for j,y in enumerate(other.c):
                if not y:
                    continue
                coefficient = x*y
                for k,root in enumerate(self.roots):
                    if (i & j) & (1 << k):
                        coefficient *= root
                out[i ^ j] += coefficient
        return A(tuple(out))
    __rmul__ = __mul__

    def flip(self, bit):
        return A(tuple(-x if i & bit else x for i,x in enumerate(self.c)))

    def inverse(self):
        if self == 0:
            raise ZeroDivisionError()
        value, numerator = self, A(1)
        for bit in (8,1,2,4):
            if any(x and i & bit for i,x in enumerate(value.c)):
                conjugate = value.flip(bit)
                numerator *= conjugate
                value *= conjugate
        assert all(x == 0 for x in value.c[1:])
        return A(tuple(x/value.c[0] for x in numerator.c))

    def __truediv__(self, other):
        return self * A(other).inverse()

    def __eq__(self, other):
        return self.c == A(other).c

    def record(self):
        return {str(i): str(x) for i,x in enumerate(self.c) if x}


def root(bit):
    return A(tuple(F(i == bit) for i in range(16)))


S2,S3,S5,CI = [root(i) for i in (1,2,4,8)]
ZERO,ONE = A(0),A(1)
I = ((ONE,ZERO),(ZERO,ONE))


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),ZERO)


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def wedge(a,b):
    return tuple(tuple(a[i]*b[j]-a[j]*b[i] for j in range(4)) for i in range(4))


def chiral(b, sign):
    return (b[1][2]+sign*b[0][3], b[2][0]+sign*b[1][3], b[0][1]+sign*b[2][3])


def pauli(v):
    x,y,z = v
    return ((z,x-CI*y),(x+CI*y,-z))


def add(a,b):
    return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))


def scale(x,a):
    return tuple(tuple(x*y for y in row) for row in a)


def mm(a,b):
    return tuple(tuple(dot(row,col) for col in zip(*b)) for row in a)


def adj(a):
    return tuple(tuple(x.flip(8) for x in col) for col in zip(*a))


def rank(a):
    a = [list(row) for row in a]
    count = 0
    for c in range(len(a[0])):
        p = next((j for j in range(count,len(a)) if a[j][c] != 0), None)
        if p is None:
            continue
        a[count],a[p] = a[p],a[count]
        inv = a[count][c].inverse()
        a[count] = [x*inv for x in a[count]]
        for j in range(count+1,len(a)):
            if a[j][c] != 0:
                coefficient = a[j][c]
                a[j] = [x-coefficient*y for x,y in zip(a[j],a[count])]
        count += 1
    return count


def constraints(blocks):
    rows = []
    for (a,b),(left,right) in blocks.items():
        for i in range(2):
            row = [ZERO]*10
            for j in range(2):
                row[2*a+j] = -left[i][j]
                row[2*b+j] = right[i][j]
            rows.append(row)
    return rows


def main():
    vertices = [tuple(A(x) for x in v)+(ZERO,) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    vertices.append((ZERO,ZERO,ZERO,S5))
    columns = [sub(v,vertices[0]) for v in vertices[1:]]
    determinant = sum((A((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))) *
                       columns[p[0]][0]*columns[p[1]][1]*columns[p[2]][2]*columns[p[3]][3]
                       for p in permutations(range(4))),ZERO)
    assert determinant == -16*S5
    assert S2*S2 == 2 and S3*S3 == 3 and S5*S5 == 5 and CI*CI == -1
    probe = ONE+S2+S3*S5+CI*S5
    assert probe*probe.inverse() == 1
    center = (ZERO,ZERO,ZERO,S5/5)
    normals = [tuple(-S5*x/4 for x in sub(v,center)) for v in vertices]
    edges = list(combinations(range(5),2))
    for a,b in edges:
        assert dot(sub(vertices[a],vertices[b]),sub(vertices[a],vertices[b])) == 8
        assert dot(normals[a],normals[b]) == F(-1,4)
    assert all(dot(n,n) == 1 for n in normals)
    triangles = {}
    for c in range(5):
        facet = [i for i in range(5) if i != c]
        for j,d in enumerate(facet):
            f = [i for i in facet if i != d]
            b = wedge(sub(vertices[f[1]],vertices[f[0]]),sub(vertices[f[2]],vertices[f[0]]))
            # det(B-A,C-A,D-A,E-A) = -16 sqrt(5), so the
            # positively oriented ambient simplex is -[ABCDE].
            triangles[c,d] = scale(A((-1)**(c+j+1)),b)
    for a,b in edges:
        assert triangles[a,b] == scale(A(-1),triangles[b,a])
    tests = ['Regular 4D lengths, unit outward facet normals and opposite oriented shared triangles.']
    results = []
    for chirality in (1,-1):
        directions = {key:tuple(x/(4*S3) for x in chiral(b,chirality)) for key,b in triangles.items()}
        projectors = {key:scale(A(F(1,2)),add(I,scale(A(-1),pauli(n)))) for key,n in directions.items()}
        for c in range(5):
            neighbors = [d for d in range(5) if d != c]
            for d in neighbors:
                p = projectors[c,d]
                assert dot(directions[c,d],directions[c,d]) == 1
                assert mm(p,p) == p and adj(p) == p and p[0][0]+p[1][1] == 1
            for d,e in combinations(neighbors,2):
                assert dot(directions[c,d],directions[c,e]) == F(-1,3)
                assert rank(list(projectors[c,d])+list(projectors[c,e])) == 2
            assert all(sum((directions[c,d][i] for d in neighbors),ZERO) == 0 for i in range(3))
            assert tuple(tuple(sum((projectors[c,d][i][j] for d in neighbors),ZERO) for j in range(2)) for i in range(2)) == scale(A(2),I)
        for a,b in edges:
            assert add(projectors[a,b],projectors[b,a]) == I
        # Facet 4 = ABCD has w=0. Its oriented bivectors reproduce the old
        # outward normals in face order ABC, ABD, ACD, BCD, for both chiralities.
        assert directions[4,3] == tuple(A(s)/S3 for s in (1,1,-1))
        assert directions[4,2] == tuple(A(s)/S3 for s in (1,-1,1))
        assert directions[4,1] == tuple(A(s)/S3 for s in (-1,1,1))
        assert directions[4,0] == tuple(A(s)/S3 for s in (-1,-1,-1))
        tests.append(f'Chirality {chirality}: every cell recovers the tetrahedral tight frame; ABCD exactly matches the retained normals.')

        # Minimal normal-plane fold from facet a to b. It fixes the common
        # triangle tangent plane. cos(theta)=-1/4, cos(theta/2)=sqrt(6)/4.
        cosine = S2*S3/4
        transports = {}
        for a,b in edges:
            first = normals[a]
            second = tuple((4*y+x)/(S3*S5) for x,y in zip(first,normals[b]))
            def fold(x):
                along, across = dot(first,x),dot(second,x)
                return tuple(y-A(F(5,4))*(along*v+across*w)+(S3*S5/4)*(along*w-across*v)
                             for y,v,w in zip(x,first,second))
            assert fold(first) == normals[b]
            shared = [i for i in range(5) if i not in (a,b)]
            for i in shared[1:]:
                tangent = sub(vertices[i],vertices[shared[0]])
                assert fold(tangent) == tangent
            k = tuple(x/(2*cosine) for x in chiral(wedge(normals[a],normals[b]),chirality))
            u = add(scale(cosine,I),scale(-CI,pauli(k)))
            assert mm(adj(u),u) == I
            assert u[0][0]*u[1][1]-u[0][1]*u[1][0] == 1
            axes = [tuple(A(i==j) for i in range(4)) for j in range(4)]
            for i,j in combinations(range(4),2):
                before = pauli(chiral(wedge(axes[i],axes[j]),chirality))
                after = pauli(chiral(wedge(fold(axes[i]),fold(axes[j])),chirality))
                assert mm(mm(u,before),adj(u)) == after
            # The sign convention here represents the directed normal-plane
            # rotor; swapping direction is its adjoint.
            transports[a,b] = u
            transports[b,a] = adj(u)
            assert mm(u,projectors[a,b]) == mm(projectors[a,b],u)
        geometric = constraints({(a,b):(mm(transports[a,b],projectors[a,b]),projectors[b,a]) for a,b in edges})
        identity = constraints({(a,b):(projectors[a,b],projectors[b,a]) for a,b in edges})
        full = constraints({(a,b):(transports[a,b],I) for a,b in edges})
        assert rank(identity) == rank(geometric) == 10
        full_rank = rank(full)
        holonomy = mm(transports[2,0],mm(transports[1,2],transports[0,1]))
        fixed_rank = rank(add(holonomy,scale(A(-1),I)))
        assert full_rank == 10 and fixed_rank == 2
        assert holonomy[0][0]+holonomy[1][1] == 2*S2*S3/9
        assert rank(add(scale(A(-1),holonomy),scale(A(-1),I))) == 2
        tests.append(f'Chirality {chirality}: all ten folds map facet normals correctly, fix shared triangles and intertwine all six bivector generators; neither loop lift has a fixed spinor.')
        tests.append(f'Chirality {chirality}: inherited rank-one matching has zero states, with either identity or geometric folding transports.')
        tests.append(f'Chirality {chirality}: geometric full-spinor parallel matching also has zero states; one loop has no fixed spinor.')
        # A different, explicitly declared assembly functional: minimize the
        # unweighted squared full-spinor seam mismatch instead of forcing zero.
        laplacian = mm(adj(full),full)
        i10 = tuple(tuple(A(i==j) for j in range(10)) for i in range(10))
        kappa = S2*S3/3
        low_energy,high_energy = A(4)-3*kappa,A(4)+2*kappa
        low = scale((5*kappa).inverse(),add(scale(high_energy,i10),scale(A(-1),laplacian)))
        high = add(i10,scale(A(-1),low))
        assert adj(low) == low and mm(low,low) == low
        assert sum((low[i][i] for i in range(10)),ZERO) == 4
        assert mm(laplacian,low) == scale(low_energy,low)
        assert mm(laplacian,high) == scale(high_energy,high)
        assert rank(low) == 4
        for c in range(5):
            assert tuple(tuple(low[2*c+i][2*c+j] for j in range(2)) for i in range(2)) == scale(A(F(2,5)),I)
            for i in range(2):
                for j in range(2):
                    assert sum((low[2*c+i][2*d+j] for d in range(5)),ZERO) == A(i==j)
        tests.append(f'Chirality {chirality}: symmetric squared-mismatch energy has a four-dimensional lowest space, not a doublet, with exact two-level spectral decomposition.')
        results.append(dict(chirality=chirality,face_matching_dimension=10-rank(geometric),
                            full_parallel_dimension=10-full_rank,loop_fixed_dimension=2-fixed_rank,
                            loop_trace=(holonomy[0][0]+holonomy[1][1]).record(),
                            lowest_energy=low_energy.record(),lowest_multiplicity=4,
                            higher_energy=high_energy.record(),higher_multiplicity=6,
                            lowest_projector_cell_compression='2/5 times I_2',
                            loop_matrix=[[x.record() for x in row] for row in holonomy]))
    # A global cell-polarity change would require opposite signs on all K5
    # edges. Every assignment has a monochromatic triple. Its members have
    # two distinct zero face restrictions; they vanish. Every remaining cell
    # then has at least two zero restrictions and also vanishes.
    for signs in product((-1,1),repeat=5):
        triple = next(t for t in combinations(range(5),3) if len({signs[c] for c in t}) == 1)
        assert len(triple) == 3
    tests.append('All 32 cell-polarity assignments contain a monochromatic triangle; whole-cell sign flips cannot repair the rank-one gluing.')
    result = dict(verification_passed=True,test_count=len(tests),tests=tests,
                  coefficient_basis='mask bits: sqrt(2), sqrt(3), sqrt(5), i',
                  chirality_results=results,
                  scope='Piecewise constant retained spinors with the stated linear matching rules; not a no-go for spinor fields or other couplings.',
                  supplied_flat_full_port_extension_recovered=False,
                  physical_charge_mass_or_exchange_derived=False)
    out = Path(__file__).resolve().parents[1]/'results/pentachoron_spin_interfaces.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

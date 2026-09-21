"""Typed-unit readout and an explicit interval cofiber attachment.

Exact signed-coordinate fixtures, not a numerical theta or Agda proof.
"""
from itertools import product, permutations, combinations
from collections import defaultdict
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
TAU = s.Rational(1,2)


def clean(A):
    return A.applyfunc(s.expand)


def star(A):
    return A.conjugate().T


def concatenate(p,q):
    assert p[0][-1] == q[0][0]
    return p[0][:-1]+q[0], p[1]+q[1]


def weight(p):
    return s.sympify(s.prod((s.Integer(1),TAU**2,-TAU**2)[i] for i in p[1]))


class PathModel:
    def __init__(self, primes):
        self.primes = primes
        self.vertices = sorted({2*s.prod(subset) for n in range(len(primes)+1)
                                for subset in combinations(primes,n)})
        self.edges = [(a,a*p) for a in self.vertices for p in primes
                      if a*p in self.vertices and (a//2)%p != 0]
        self.paths = []
        def visit(vs,letters):
            self.paths.append((vs,letters))
            for a,b in self.edges:
                if a == vs[-1]:
                    for letter in range(3):
                        visit(vs+(b,),letters+(letter,))
        for a in self.vertices:
            visit((a,),())
        self.P = {a:[p for p in self.paths if p[0][-1]==a] for a in self.vertices}
        self.idx = {a:{p:i for i,p in enumerate(ps)} for a,ps in self.P.items()}
        self.end = self.vertices[-1]
        self.middle = [b for a,b in self.edges if a==2]
        self.U = {m:[p for p in self.paths if p[0][0]==2 and p[0][-1]==m] for m in self.middle}
        self.Z = [(m,u,p) for m in self.middle for u in self.U[m] for p in self.P[m]]
        self.zi = {key:i for i,key in enumerate(self.Z)}
        self.Hom = [p for p in self.paths if p[0][0]==2 and p[0][-1]==self.end]
        self.coev = s.SparseMatrix(len(self.Z),1,{
            (self.zi[m,u,u],0):1 for m in self.middle for u in self.U[m]})
        self.Qz = s.diag(*(weight(p)/weight(u) for m,u,p in self.Z))
        self.Qy = s.diag(*(weight(p) for p in self.P[self.end]))

    def attachment(self, h):
        entries = defaultdict(lambda:s.Integer(0))
        for path,c in h.items():
            vs,ls = path
            m = vs[1]
            u = (vs[:2],ls[:1])
            suffix = (vs[1:],ls[1:])
            for prefix in self.P[m]:
                entries[self.idx[self.end][concatenate(prefix,suffix)],self.zi[m,u,prefix]] += c
        return clean(s.SparseMatrix(len(self.P[self.end]),len(self.Z),dict(entries)))

    def read_units(self,A):
        out = {}
        for p in self.Hom:
            vs,ls = p
            m = vs[1]
            u = (vs[:2],ls[:1])
            suffix = (vs[1:],ls[1:])
            value = s.expand(A[self.idx[self.end][suffix],self.zi[m,u,((m,),())]])
            if value:
                out[p] = value
        return out

    def column(self,h):
        return s.SparseMatrix(len(self.P[self.end]),1,
                             {(self.idx[self.end][p],0):c for p,c in h.items() if c})


def cone_checks(model):
    # A genuinely joint input, with both middle-vertex blocks and complex scalars.
    h = {p:(1+s.I if i%2 else 2-s.I) for i,p in enumerate(model.Hom)}
    u, v = model.coev, model.attachment(h)
    assert model.read_units(v) == h
    vu = clean(v*u)
    assert vu == model.column(h)
    n, z, y = 1, u.rows, v.rows
    # Cone(i), for i:Cone(u)->Cone(vu), is a three-term complex.
    d0 = s.Matrix.vstack(s.eye(n),-u)
    d1 = s.Matrix.hstack(vu,v)
    assert clean(d1*d0) == s.zeros(y,n)
    # Projection to Cone(v), section, and specified contracting homotopy.
    F = s.Matrix.hstack(u,s.eye(z))
    G = s.Matrix.vstack(s.zeros(n,z),s.eye(z))
    H = s.Matrix.hstack(s.eye(n),s.zeros(n,z))
    assert F*d0 == s.zeros(z,n)
    assert clean(v*F) == d1
    assert clean(d1*G) == v
    assert F*G == s.eye(z)
    assert d0*H == s.eye(n+z)-G*F
    assert H*d0 == s.eye(n)
    # The attachment composite is nullhomotopic, NOT the zero chain map.
    assert u != s.zeros(z,n) and v != s.zeros(y,z)
    # p i=(u,v); the identity Z->Z is its nullhomotopy.
    assert s.eye(z)*u == u and v*s.eye(z) == v

    Qx, Qz, Qy = s.eye(n),model.Qz,model.Qy
    Qmid = s.diag(Qx,Qz)
    us = clean(Qx.inv()*star(u)*Qz)
    vs = clean(Qz.inv()*star(v)*Qy)
    assert clean(us*vs) == clean(Qx.inv()*star(vu)*Qy)
    # Cochain conjugate dual: d^0=-d1^vee, d^1=+d0^vee.
    delta0 = clean(-Qmid.inv()*star(d1)*Qy)
    delta1 = clean(Qx.inv()*star(d0)*Qmid)
    assert clean(delta1*delta0) == s.zeros(n,y)
    Fs = clean(Qmid.inv()*star(F)*Qz)
    Gs = clean(Qz.inv()*star(G)*Qmid)
    Hs = clean(Qmid.inv()*star(H)*Qx)
    assert clean(Gs*Fs) == s.eye(z)
    assert clean(Hs*delta1) == s.eye(n+z)-clean(Fs*Gs)
    assert clean(delta1*Hs) == s.eye(n)
    assert clean(Fs*(-vs)) == delta0
    assert clean(Gs*delta0) == -vs
    assert clean(delta1*Fs) == s.zeros(n,z)
    return {"projective_dimensions":[n,z,y],"cone_deformation_retract":True,
            "nonzero_attachment_composite_has_explicit_nullhomotopy":True,
            "dual_deformation_retract_and_cochain_signs":True}


def main():
    diamond = PathModel((2,3))
    assert len(diamond.paths)==34 and len(diamond.Hom)==18
    basis = []
    for p in diamond.Hom:
        A = diamond.attachment({p:1})
        assert diamond.read_units(A)=={p:1}
        assert A*diamond.coev==diamond.column({p:1})
        basis.append(A)
    # The signed Hilbert-Schmidt pairing on ALL projective input states
    # overcounts the prescribed joint coefficient form by dim(P_m)=4.
    hs = s.zeros(18)
    for i,A in enumerate(basis):
        for j,B in enumerate(basis):
            # Diagonal signatures permit an exact sparse trace contraction.
            hs[i,j] = sum(s.conjugate(c)*B[r,k]*diamond.Qy[r,r]/diamond.Qz[k,k]
                          for (r,k),c in A.todok().items())
    joint = s.diag(*(weight(p) for p in diamond.Hom))
    assert hs == 4*joint and hs != joint
    closure = cone_checks(diamond)

    braid = PathModel((2,3,5))
    assert len(braid.paths)==314 and len(braid.Hom)==162
    for p in braid.Hom:
        A = braid.attachment({p:1})
        assert braid.read_units(A)=={p:1}
        assert A*braid.coev==braid.column({p:1})
    # Reuse the actual interval incidence with a complex two-sheet fixture.
    signs = (-1,1,1,-1,-1,1)
    endpoint_index = {a:i for i,a in enumerate(braid.vertices)}
    features = [(1+(i+1)*s.I,i+2-s.I) for i in range(7)]
    ghosts = [defaultdict(lambda:s.Integer(0)),defaultdict(lambda:s.Integer(0))]
    for ri,primes in enumerate(permutations((2,3,5))):
        vertices = [2]
        for p in primes:
            vertices.append(vertices[-1]*p)
        vs = tuple(vertices)
        ghosts[0][vs,(0,0,0)] += signs[ri]
        for event in range(3):
            for j in range(2):
                coefficient = sum(features[k][j] for k in range(endpoint_index[vs[event]],endpoint_index[vs[event+1]]))
                letters = [0,0,0]
                letters[event] = j+1
                ghosts[1][vs,tuple(letters)] += signs[ri]*coefficient
    for ghost in ghosts:
        h = {p:s.expand(c) for p,c in ghost.items() if c}
        A = braid.attachment(h)
        assert A != s.zeros(A.rows,A.cols)
        assert braid.read_units(A)==h
        assert clean(A*braid.coev)==braid.column(h)
        terminal = defaultdict(lambda:s.Integer(0))
        for (vs,ls),c in h.items():
            terminal[tuple(i for i in ls if i)] += c
        assert all(s.expand(c)==0 for c in terminal.values())

    result = {
        "schema":"marici.nima.joint-record-interval-attachment.v1", "passed":True,
        "joint_records_identified_as_typed_projective_hom_coefficients":True,
        "diamond_path_algebra_dimension":34,"diamond_joint_hom_dimension":18,
        "braid_path_algebra_dimension":314,"braid_joint_hom_dimension":162,
        "canonical_coevaluation_and_typed_unit_readout_on_all_basis_vectors":True,
        "signed_hilbert_schmidt_overcount_in_diamond":4,
        "typed_unit_pairing_has_no_overcount":True,
        "smallest_interval_attachment":closure,
        "both_braid_ghosts_survive_attachment_and_projective_composite":True,
        "both_braid_ghosts_die_only_in_terminal_record_compression":True,
        "scope":"Finite signed-coordinate path-algebra and chain-complex fixtures. General identifications are proved in the note. No identification of a record with a cofiber object, no sampled theta faithfulness claim, and no Agda verification of stable categories.",
    }
    out=ROOT/'research/nima/results/joint-record-interval-attachment.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

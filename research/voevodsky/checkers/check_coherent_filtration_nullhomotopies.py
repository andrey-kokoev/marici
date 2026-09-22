"""Exact finite-flag, refinement and total-complex sign checks.

Common two-term models supply strict zero composites. No source-module
splitting or projectivity of completed ideals is assumed in the theorem.
"""
from pathlib import Path
import json
import sympy as s

def inclusion(n):
    return s.zeros(1,n).col_join(s.eye(n))
def projection(n,m):
    assert n>=m
    return s.eye(m).row_join(s.zeros(m,n-m))
# Finite horizons and natural refinement maps: K_i=[F_(i+1)->F_i].
refinements=0
for i in range(4):
    for T in (5,6,7):
        d=inclusion(T-i-1)
        assert d.rank()==T-i-1
        # Quotient by the next filtration term is one-dimensional.
        q=s.zeros(1,T-i);q[0,0]=1
        assert q*d==s.zeros(1,T-i-1)
    R10=projection(6-i,5-i);R21=projection(7-i,6-i)
    assert R10*R21==projection(7-i,5-i)
    for big,small in ((6,5),(7,6),(7,5)):
        R0=projection(big-i,small-i)
        Rm=projection(big-i-1,small-i-1)
        assert R0*inclusion(big-i-1)==inclusion(small-i-1)*Rm
        # The differential on the refinement kernel is the identity.
        Z=big-small
        j0=s.zeros(small-i,Z).col_join(s.eye(Z))
        jm=s.zeros(small-i-1,Z).col_join(s.eye(Z))
        assert inclusion(big-i-1)*jm==j0
        if i<3:
            # Adjacent map is identity from source degree -1 to target degree 0.
            assert projection(big-i-1,small-i-1)*s.eye(big-i-1)==s.eye(small-i-1)*Rm
        refinements+=1
# Coherent nonidentity frame coordinates.
F=3
iF=s.Matrix([1,2,3]);rF=s.Matrix([[1,0,0]])
Delta=s.Matrix([[-1,s.Rational(1,2),0],[-1,0,s.Rational(1,3)]])
hF=s.Matrix([[0,0],[2,0],[0,3]])
assert iF*rF+hF*Delta==s.eye(F)
assert Delta*hF==s.eye(F-1)

def model(top,index):
    v={-1:top-index-1,0:top-index}
    parts={k:[] for k in range(-2,3)}
    for a in (-1,0):
        for b in (0,1):parts[a+b].append((a,b))
    for k in parts:parts[k].sort(key=lambda ab:ab[1])
    def size(ab):return v[ab[0]]*(F if ab[1]==0 else F-1)
    dims={k:sum(size(ab) for ab in parts[k]) for k in parts}
    offsets={}
    for k in parts:
        offset=0
        for ab in parts[k]:offsets[ab]=offset;offset+=size(ab)
    M={'v':v,'parts':parts,'dims':dims,'offsets':offsets}
    return M

def zero(M,N,k,degree):return s.zeros(N['dims'].get(k+degree,0),M['dims'].get(k,0))
def put(mat,M,N,source,target,block):
    a=M['offsets'][source];b=N['offsets'][target]
    mat[b:b+block.rows,a:a+block.cols]=block

def differential(M,k):
    out=zero(M,M,k,1)
    for a,b in M['parts'].get(k,[]):
        if a==-1:
            put(out,M,M,(a,b),(0,b),s.kronecker_product(s.eye(F if b==0 else F-1),inclusion(M['v'][-1])))
        if b==0:
            sign=-1 if a%2 else 1
            put(out,M,M,(a,b),(a,1),sign*s.kronecker_product(Delta,s.eye(M['v'][a])))
    return out

def homotopy(M,k):
    out=zero(M,M,k,-1)
    for a,b in M['parts'].get(k,[]):
        if b==1:
            sign=-1 if a%2 else 1
            put(out,M,M,(a,b),(a,0),sign*s.kronecker_product(hF,s.eye(M['v'][a])))
    return out

def projector(M,k):
    out=zero(M,M,k,0)
    for a,b in M['parts'].get(k,[]):
        if b==0:put(out,M,M,(a,b),(a,b),s.kronecker_product(iF*rF,s.eye(M['v'][a])))
    return out

def edge(M,N,k):
    out=zero(M,N,k,1)
    for a,b in M['parts'].get(k,[]):
        if a==-1:put(out,M,N,(a,b),(0,b),s.eye((F if b==0 else F-1)*M['v'][-1]))
    return out

models=[model(5,j) for j in range(4)]
for M in models:
    for k in (-1,0,1):
        assert differential(M,k+1)*differential(M,k)==zero(M,M,k,2)
        assert differential(M,k-1)*homotopy(M,k)+homotopy(M,k+1)*differential(M,k)==s.eye(M['dims'][k])-projector(M,k)
        assert homotopy(M,k-1)*homotopy(M,k)==zero(M,M,k,-2)
for M,N in zip(models,models[1:]):
    for k in (-1,0,1):
        assert differential(N,k+1)*edge(M,N,k)+edge(M,N,k+1)*differential(M,k)==zero(M,N,k,2)
        assert homotopy(N,k+1)*edge(M,N,k)+edge(M,N,k-1)*homotopy(M,k)==zero(M,N,k,0)
for M,N,P in zip(models,models[1:],models[2:]):
    for k in (-1,0,1):assert edge(N,P,k+1)*edge(M,N,k)==zero(M,P,k,2)
# Reconstruct every tail of the original flag with D=d-A and augmentation
# equal to the sum of the actual inclusions. This checks the cone sign.
reconstructions=0
for start in range(5):
    dims0=[5-j for j in range(start,5)]
    dimsm=[n-1 for n in dims0]
    D=s.zeros(sum(dims0),sum(dimsm));eps=s.zeros(dims0[0],sum(dims0))
    ro=co=0
    for j,(n,nm) in enumerate(zip(dims0,dimsm)):
        D[ro:ro+n,co:co+nm]=inclusion(nm)
        if j+1<len(dims0):D[ro+n:ro+n+nm,co:co+nm]=-s.eye(nm)
        eps[:,ro:ro+n]=s.zeros(dims0[0]-n,n).col_join(s.eye(n))
        ro+=n;co+=nm
    assert eps*D==s.zeros(eps.rows,D.cols)
    assert D.rank()==D.cols and eps.rank()==dims0[0]
    assert D.rows-D.cols==dims0[0]
    reconstructions+=1
result={'passed':True,'refinement_checks':refinements,'common_flag_models':len(models),
 'filtered_tail_reconstructions':reconstructions,
 'checks':{'refinement_kernel_is_identity_complex':True,
 'refinement_compositions_strict':True,'adjacent_maps_are_closed_degree_one_maps':True,
 'adjacent_composites_strictly_zero':True,'total_complex_signs':True,
 'horizontal_contraction_identity':True,'contraction_anticommutes_with_degree_one_maps':True},
 'scope':'Exact finite matrix and sign checks. All-horizon coherence follows from the common two-term flag models and natural quotient maps; no global projective resolution, uniqueness of Toda values, or uniform all-depth bound is inferred.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/coherent-filtration-nullhomotopies.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

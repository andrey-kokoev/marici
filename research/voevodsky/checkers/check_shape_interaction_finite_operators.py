"""Independent exact audit of finite-operator identities in the supplied note.
Standard library only: Q(sqrt(2),i) matrices and sparse multivariate Q polynomials.
No fitted probability, geometry adapter, or scattering continuum is assumed.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from pathlib import Path
from hashlib import sha256
import json

BASE=Path(__file__).resolve().parents[1]


class K:
    """a + b sqrt(2) + i(c + d sqrt(2))."""
    def __init__(self,a=0,b=0,c=0,d=0):self.v=tuple(map(Q,(a,b,c,d)))
    @staticmethod
    def cast(x):return x if isinstance(x,K) else K(x)
    def __add__(self,o):
        o=K.cast(o);return K(*(x+y for x,y in zip(self.v,o.v)))
    __radd__=__add__
    def __neg__(self):return K(*(-x for x in self.v))
    def __sub__(self,o):return self+-K.cast(o)
    def __rsub__(self,o):return K.cast(o)+-self
    def __mul__(self,o):
        o=K.cast(o);out=[Q(0)]*4
        for j,x in enumerate(self.v):
            for k,y in enumerate(o.v):
                r=(j%2)+(k%2);im=(j//2)+(k//2)
                out[(r%2)+2*(im%2)]+=x*y*(2 if r>=2 else 1)*(-1 if im>=2 else 1)
        return K(*out)
    __rmul__=__mul__
    def conjugate(self):return K(self.v[0],self.v[1],-self.v[2],-self.v[3])
    def __eq__(self,o):return self.v==K.cast(o).v
    def __repr__(self):return repr(self.v)


NAMES=('a','b','c','z','t','p','q','r','s')
ZERO_EXP=(0,)*len(NAMES)
class Poly:
    def __init__(self,value=0):
        if isinstance(value,dict):self.terms={k:Q(v) for k,v in value.items() if v}
        else:self.terms={} if value==0 else {ZERO_EXP:Q(value)}
    @staticmethod
    def cast(x):return x if isinstance(x,Poly) else Poly(x)
    @staticmethod
    def variable(name):
        exponent=list(ZERO_EXP);exponent[NAMES.index(name)]=1
        return Poly({tuple(exponent):Q(1)})
    def __add__(self,o):
        out=dict(self.terms)
        for e,v in Poly.cast(o).terms.items():out[e]=out.get(e,Q(0))+v
        return Poly(out)
    __radd__=__add__
    def __neg__(self):return Poly({e:-v for e,v in self.terms.items()})
    def __sub__(self,o):return self+-Poly.cast(o)
    def __rsub__(self,o):return Poly.cast(o)+-self
    def __mul__(self,o):
        out={}
        for e,v in self.terms.items():
            for f,w in Poly.cast(o).terms.items():
                key=tuple(x+y for x,y in zip(e,f));out[key]=out.get(key,Q(0))+v*w
        return Poly(out)
    __rmul__=__mul__
    def __pow__(self,n):
        out=Poly(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,o):return self.terms==Poly.cast(o).terms
    def coefficient(self,name,power):
        i=NAMES.index(name);out={}
        for e,v in self.terms.items():
            if e[i]==power:
                key=list(e);key[i]=0;out[tuple(key)]=v
        return Poly(out)
    def truncate(self,name,degree):
        i=NAMES.index(name);return Poly({e:v for e,v in self.terms.items() if e[i]<=degree})
    def encoded(self):
        return [{'powers':{n:k for n,k in zip(NAMES,e) if k},'coefficient':str(v)} for e,v in sorted(self.terms.items())]


def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def zeros(n,m):return [[0 for _ in range(m)] for _ in range(n)]
def plus(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def times(s,A):return [[s*x for x in row] for row in A]
def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def adjoint(A):return [[x.conjugate() if isinstance(x,K) else x for x in col] for col in zip(*A)]
def kron(A,B):return [[x*y for x in a for y in b] for a in A for b in B]
def equal(A,B):return len(A)==len(B) and all(len(a)==len(b) and all(x==y for x,y in zip(a,b)) for a,b in zip(A,B))
def determinant(A):
    out=0;n=len(A)
    for pi in permutations(range(n)):
        sign=(-1)**sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        term=sign
        for i,j in enumerate(pi):term=term*A[i][j]
        out=out+term
    return out

def adjugate(A):
    n=len(A)
    return [[(-1)**(i+j)*determinant([[A[r][s] for s in range(n) if s!=i] for r in range(n) if r!=j]) for j in range(n)] for i in range(n)]


def main():
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    I2=eye(2);X=[[0,1],[1,0]];Z=[[1,0],[0,-1]]
    ii=K(0,0,1);root_half=K(0,Q(1,2))
    A=times(root_half,plus(I2,times(ii,Z)))
    B=times(root_half,plus(I2,times(ii,X)))
    check('braid_matrices_unitary',equal(mm(adjoint(A),A),I2) and equal(mm(adjoint(B),B),I2))
    check('braid_relation_ABA_BAB',equal(mm(mm(A,B),A),mm(mm(B,A),B)))
    check('braid_representation_noncommutative',not equal(mm(A,B),mm(B,A)))
    v1=mm(B,[[1],[0]]);v2=mm(mm(mm(A,A),B),[[1],[0]])
    check('same_coset_histories_have_claimed_states',equal(v1,[[root_half],[ii*root_half]]) and equal(v2,[[ii*root_half],[root_half]]))
    check('same_coset_history_states_orthogonal',equal(mm(adjoint(v1),v2),[[0]]))
    phase_reports=[]
    for label,phase,cos1,cos2 in [('0',K(1),K(1),K(1)),('pi/4',root_half*(1+ii),root_half,K(0)),('pi/2',ii,K(0),K(-1))]:
        ua=times(phase,X);ub=times(phase*phase,I2)
        Hphase=times(Q(1,4),plus(plus(ua,adjoint(ua)),plus(ub,adjoint(ub))))
        check('crossing_phase_generator_'+label,equal(Hphase,plus(times(Q(1,2)*cos1,X),times(Q(1,2)*cos2,I2))))
        phase_reports.append(label)
    # Frobenius structure, including unit/counit and a concrete unitary dilation.
    m=[[1,0,0,0],[0,0,0,1]];delta=adjoint(m);eta=[[1],[1]]
    M2=mm(delta,m);M3=mm(mm(kron(delta,I2),delta),m);P=M2
    check('merge_associative',equal(mm(m,kron(m,I2)),mm(m,kron(I2,m))))
    check('split_coassociative',equal(mm(kron(delta,I2),delta),mm(kron(I2,delta),delta)))
    swap=[[int(j==((i%2)*2+i//2)) for j in range(4)] for i in range(4)]
    check('commutative_and_cocommutative',equal(mm(m,swap),m) and equal(mm(swap,delta),delta))
    check('unit_and_counit',equal(mm(m,kron(eta,I2)),I2) and equal(mm(m,kron(I2,eta)),I2) and equal(mm(kron(adjoint(eta),I2),delta),I2) and equal(mm(kron(I2,adjoint(eta)),delta),I2))
    check('frobenius_compatibility',equal(mm(kron(m,I2),kron(I2,delta)),P) and equal(mm(kron(I2,m),kron(delta,I2)),P))
    check('both_conversion_gram_operators_are_P',equal(mm(adjoint(M2),M2),P) and equal(mm(adjoint(M3),M3),P))
    check('special_but_not_invertible',equal(mm(m,delta),I2) and not equal(mm(delta,m),eye(4)))
    p,q=Poly.variable('p'),Poly.variable('q')
    check('channel_weight_normalization_for_all_p_q',(1-q)+q*p+q*(1-p)==1)
    check('P_orthogonal_projector',equal(mm(P,P),P) and equal(adjoint(P),P))
    # The previous two checks and the conversion Gram identities prove S*S=I
    # for all p,q in [0,1], not just this rational-amplitude realization.
    S=plus(eye(4),times(Q(-2,3),P))+times(Q(2,3),M2)+times(Q(2,3),M3)
    check('explicit_16_by_4_channel_isometry',len(S)==16 and equal(mm(adjoint(S),S),eye(4)))
    remainder=plus(eye(16),times(-1,mm(S,adjoint(S))))
    U=[s+r for s,r in zip(S,remainder)]+[z+s for z,s in zip(zeros(4,4),times(-1,adjoint(S)))]
    check('explicit_20_by_20_unitary_completion',equal(mm(adjoint(U),U),eye(20)) and equal(mm(U,adjoint(U)),eye(20)))
    unequal=[[0],[1],[0],[0]]
    check('dropping_survival_loses_unequal_input',equal(mm(M2,unequal),zeros(4,1)) and equal(mm(M3,unequal),zeros(8,1)) and not equal(mm(S,unequal),zeros(16,1)))
    superposition=[[root_half],[root_half]]
    check('basis_split_is_not_arbitrary_state_cloning',not equal(mm(delta,superposition),kron(superposition,superposition)))
    # Equal-coupling three-state model: exact spectral projectors and symmetric square.
    H3=[[0,1,0],[1,0,1],[0,1,0]];T=times(root_half,H3);T2=mm(T,T)
    P0=plus(eye(3),times(-1,T2));Pplus=times(Q(1,2),plus(T2,T));Pminus=times(Q(1,2),plus(T2,times(-1,T)))
    spectral=[P0,Pplus,Pminus]
    check('three_state_spectral_projectors',equal(plus(plus(P0,Pplus),Pminus),eye(3)) and all(equal(mm(a,b),a if i==j else zeros(3,3)) for i,a in enumerate(spectral) for j,b in enumerate(spectral)))
    check('three_state_spectral_eigenvalues',all(equal(mm(T,Pj),times(value,Pj)) for value,Pj in zip((0,1,-1),spectral)))
    start=[[1],[0],[0]]
    check('three_state_propagator_coefficients',equal(mm(P0,start),[[Q(1,2)],[0],[Q(-1,2)]]) and equal(mm(plus(Pplus,Pminus),start),[[Q(1,2)],[0],[Q(1,2)]]) and equal(mm(plus(Pplus,times(-1,Pminus)),start),[[0],[root_half],[0]]))
    r,s=Poly.variable('r'),Poly.variable('s')
    # r=cos(phi), s=cos(2phi). The I/X projectors diagonalize the
    # crossing-phase Hamiltonian for arbitrary scalar coefficients.
    shifted_X=times(Q(1,2),plus(times(r,X),times(s,I2)))
    Xplus=times(Q(1,2),plus(I2,X));Xminus=times(Q(1,2),plus(I2,times(-1,X)))
    check('general_crossing_phase_spectral_decomposition',equal(mm(shifted_X,Xplus),times(Q(1,2)*(s+r),Xplus)) and equal(mm(shifted_X,Xminus),times(Q(1,2)*(s-r),Xminus)) and equal(plus(Xplus,Xminus),I2))
    # Reuse r,s below as cos(x),sin(x) for the three-state propagator.
    PE=Q(1,4)*(1+r)**2;Ptwo=Q(1,2)*s**2;Pthree=Q(1,4)*(1-r)**2
    check('three_state_probability_normalization_mod_circle',PE+Ptwo+Pthree-1==Q(1,2)*(r*r+s*s-1))
    check('binomial_relation_mod_circle',Ptwo**2-4*PE*Pthree==Q(1,4)*(s*s+r*r-1)*(s*s+1-r*r))
    V=[[1,0,0],[0,root_half,0],[0,root_half,0],[0,0,1]]
    binary=plus(kron(X,I2),kron(I2,X))
    check('symmetric_square_subspace_is_isometric_and_invariant',equal(mm(adjoint(V),V),eye(3)) and equal(mm(binary,V),mm(V,times(K(0,1),H3))))
    single=Q(1,187);probabilities=[(1-single)**2,2*single*(1-single),single**2]
    check('conditional_372_binomial_numbers',sum(probabilities)==1 and probabilities[1]/probabilities[2]==372 and probabilities[0]/probabilities[1]==93)
    # Symbolic four-state Hamiltonian and Taylor expansion; no sampled couplings.
    a,b,c,z,t=[Poly.variable(n) for n in ('a','b','c','z','t')]
    H=[[Poly(0),a,Poly(0),Poly(0)],[a,Poly(0),b,Poly(0)],[Poly(0),b,Poly(0),c],[Poly(0),Poly(0),c,Poly(0)]]
    check('four_state_Hermitian_for_real_couplings',equal(H,adjoint(H)))
    real=[Poly(0) for _ in range(4)];imag=[Poly(0) for _ in range(4)];hn=eye(4)
    for n in range(9):
        destination=real if n%2==0 else imag
        sign=(-1)**(n//2) if n%2==0 else (-1)**((n+1)//2)
        for j in range(4):destination[j]=destination[j]+Q(sign,factorial(n))*hn[j][0]*t**n
        hn=mm(hn,H)
    probs=[(x*x+y*y).truncate('t',8) for x,y in zip(real,imag)]
    check('four_state_probability_conservation_through_order_8',sum(probs,Poly(0))==1)
    check('two_output_leading_order_and_coefficient',all(probs[2].coefficient('t',n)==0 for n in range(4)) and probs[2].coefficient('t',4)==Q(1,4)*a*a*b*b)
    check('three_output_leading_order_and_coefficient',all(probs[3].coefficient('t',n)==0 for n in range(6)) and probs[3].coefficient('t',6)==Q(1,36)*a*a*b*b*c*c)
    check('extra_split_controls_leading_ratio',9*probs[3].coefficient('t',6)==c*c*probs[2].coefficient('t',4))
    check('visible_projection_leaks_to_intermediate_at_order_2',probs[1].coefficient('t',2)==a*a and sum((probs[j] for j in (0,2,3)),Poly(0)).coefficient('t',2)==-a*a)
    check('old_binomial_law_not_four_state_identity',(probs[2]**2-4*probs[0]*probs[3]).coefficient('t',6)==-Q(1,9)*a*a*b*b*c*c)
    M=plus(times(z,eye(4)),times(-1,H));D=determinant(M);Adj=adjugate(M)
    expectedD=z**4-(a*a+b*b+c*c)*z*z+a*a*c*c
    check('four_state_characteristic_polynomial',D==expectedD)
    check('full_adjugate_inverse_identity',equal(mm(M,Adj),times(D,eye(4))) and equal(mm(Adj,M),times(D,eye(4))))
    check('resolvent_transfer_numerators',Adj[2][0]==a*b*z and Adj[3][0]==a*b*c)
    check('exact_final_row_resolvent_relation',z*Adj[3][0]==c*Adj[2][0])
    visible=(0,2,3);hpp=[[H[i][j] for j in visible] for i in visible];coupling=[[a],[b],[Poly(0)]]
    schur_times_z=plus(times(z,plus(times(z,eye(3)),times(-1,hpp))),times(-1,mm(coupling,adjoint(coupling))))
    projected_adj=[[Adj[i][j] for j in visible] for i in visible]
    check('full_projected_Schur_identity',equal(mm(schur_times_z,projected_adj),times(z*D,eye(3))) and equal(mm(projected_adj,schur_times_z),times(z*D,eye(3))))
    check('Schur_determinant_identity',determinant(schur_times_z)==z*z*D)
    check('z_zero_self_energy_pole_need_not_be_full_pole',D.coefficient('z',0)==a*a*c*c)
    # Negative control: forgetting the hidden state sets the E-to-2 resolvent
    # numerator to zero, whereas the full model's numerator is ab*z.
    reducedM=plus(times(z,eye(3)),times(-1,hpp))
    check('discarding_C_without_self_energy_loses_conversion',adjugate(reducedM)[1][0]==0 and Adj[2][0]!=0)
    source=BASE/'braid-composition-effective-shape-interaction-operators.md'
    result={'verification_passed':all(checks.values()),'checks':checks,'exact_arithmetic':['Q(sqrt(2),i)','sparse multivariate Q polynomials'],
        'covered_note_sections':[4,7,20,21,22,23,24,26,27,28,29,30],
        'scope_of_section_7':'three exact representation phases and arbitrary-coefficient I/X spectral projectors; not arbitrary braid-history dynamics',
        'characteristic_polynomial':D.encoded(),'transfer_numerators':{'G_2E':Adj[2][0].encoded(),'G_3E':Adj[3][0].encoded()},
        'four_state_probability_series_through_order_8':{name:prob.encoded() for name,prob in zip(('E','C','2','3'),probs)},
        'isometry_fixture':{'p':'1/2','q':'8/9','S_dimension':[16,4],'unitary_completion_dimension':[20,20]},
        'all_parameter_isometry_proof':'M2* M2 = M3* M3 = P, P orthogonal, and (1-q)+qp+q(1-p)=1 for p,q in [0,1]',
        'binomial_probabilities_conditioned_on_working_ratio':list(map(str,probabilities)),
        'qualifications':['Resolvent statements require z outside the spectrum; Schur form also requires z != 0.',
            'Ratios require nonzero denominators; no ratio is claimed when conversion amplitudes vanish.',
            'Short-time ratios assume fixed nonzero a,b,c and t tending to zero; fitting ct alone does not validate this regime.',
            'No physical calibration or prediction of 372; its use in the binomial test is conditional.',
            'No complete braid/configuration-space/subdivision audit, native phase adapter, geometric collective closure, or asymptotic scattering construction.'],
        'source_hashes':{p.name:sha256(p.read_bytes()).hexdigest() for p in (source,Path(__file__))}}
    output=BASE/'results/shape_interaction_finite_operators.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':result['verification_passed'],'checks':checks,'receipt':str(output)},indent=2))


if __name__=='__main__':main()

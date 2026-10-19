"""Exact stationary scattering for three identical semi-infinite discrete leads.
Central generator is the retained eleven-state interface fixture. Lead/contact
laws are explicit extra inputs; channels are ports, not photon multiplicities.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from decimal import Decimal,localcontext
import json
from check_native_adapter_collective_closure import F

BASE=Path(__file__).resolve().parents[1]

class C:
    """Q(sqrt(151),i), with exact real/imaginary quadratic-field components."""
    __slots__=('r','s')
    def __init__(self,r=0,s=0):self.r=F.cast(r);self.s=F.cast(s)
    @staticmethod
    def cast(x):return x if isinstance(x,C) else C(x)
    def __bool__(self):return bool(self.r or self.s)
    def __add__(self,o):
        o=C.cast(o);return C(self.r+o.r,self.s+o.s)
    __radd__=__add__
    def __neg__(self):return C(-self.r,-self.s)
    def __sub__(self,o):return self+-C.cast(o)
    def __rsub__(self,o):return C.cast(o)+-self
    def __mul__(self,o):
        o=C.cast(o)
        if not self or not o:return C()
        return C(self.r*o.r-self.s*o.s,self.r*o.s+self.s*o.r)
    __rmul__=__mul__
    def conjugate(self):return C(self.r,-self.s)
    def inverse(self):
        q=(self.r*self.r+self.s*self.s).inverse()
        return C(self.r*q,-self.s*q)
    def __truediv__(self,o):return self*C.cast(o).inverse()
    def __eq__(self,o):
        o=C.cast(o);return self.r==o.r and self.s==o.s
    def abs2(self):return self.r*self.r+self.s*self.s
    def encoded(self):return self.r.encoded()+self.s.encoded()


def zero(n,m):return [[C() for _ in range(m)] for _ in range(n)]
def eye(n):return [[C(int(i==j)) for j in range(n)] for i in range(n)]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(x,A):return [[x*a for a in row] for row in A]
def multiply(A,B):
    out=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b:out[i][j]=out[i][j]+a*b
    return out

def equal(A,B):return len(A)==len(B) and all(len(a)==len(b) and all(x==y for x,y in zip(a,b)) for a,b in zip(A,B))
def adjoint(A):return [[x.conjugate() for x in col] for col in zip(*A)]
def diag(xs):return [[C(x) if i==j else C() for j in range(len(xs))] for i,x in enumerate(xs)]
def block(A,rows,cols):return [[A[i][j] for j in cols] for i in rows]
def solve(A,B):
    """Exact elimination on the full system, independent of Schur elimination."""
    n=len(A);m=len(B[0]);rows=[list(a)+list(b) for a,b in zip(A,B)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if rows[i][j]),None)
        if pivot is None:raise ValueError('Singular system')
        rows[j],rows[pivot]=rows[pivot],rows[j]
        inverse=rows[j][j].inverse();rows[j]=[x*inverse if x else C() for x in rows[j]]
        for i in range(n):
            if i==j or not rows[i][j]:continue
            coefficient=rows[i][j]
            rows[i]=[x-coefficient*y if y else x for x,y in zip(rows[i],rows[j])]
    assert equal([row[:n] for row in rows],eye(n))
    answer=[row[n:n+m] for row in rows]
    assert equal(multiply(A,answer),B)
    return answer

def evaluate_matrix(coefficients,x):
    result=zero(len(coefficients[0]),len(coefficients[0][0]))
    for matrix in reversed(coefficients):result=add(scale(x,result),matrix)
    return result

def evaluate_scalar(coefficients,x):
    result=F()
    for coefficient in reversed(coefficients):result=result*x+coefficient
    return result

def approximate(x):
    with localcontext() as context:
        context.prec=45
        def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
        return str(+(dec(x.a)+dec(x.b)*Decimal(151).sqrt()))

def require_open_band(energy):
    if not Q(0)<energy<Q(4):raise ValueError('No nonzero propagating flux in the declared open band')
    return True

def read_matrix(raw):return [[C(F(*x)) for x in row] for row in raw]
def encoded_matrix(A):return [[x.encoded() for x in row] for row in A]


def main():
    source_path=BASE/'results/native_joint_generator_resolvent.json'
    source=json.loads(source_path.read_text(encoding='utf-8'));assert source['verification_passed']
    for name,digest in source['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    K=read_matrix(source['joint_generator']);n=len(K);assert n==11
    metric=[F(*x) for x in source['gram_diagonal']];port_metric=metric[:3]
    V=zero(n,3)
    for j in range(3):V[j][j]=C(1)
    contact=diag([1,1,1]+[0]*8)
    central_with_contact=add(K,contact)
    Kpp=block(K,range(3),range(3));Kpq=block(K,range(3),range(3,n));Kqp=block(K,range(3,n),range(3));Kqq=block(K,range(3,n),range(3,n))
    sigma_coefficients=[read_matrix(A) for A in source['self_energy_numerator_coefficients_ascending']]
    hidden_D=[F(*x) for x in source['hidden_characteristic_coefficients_ascending']]
    closed_numerators=[read_matrix(A) for A in source['visible_resolvent_numerator_coefficients_ascending']]
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    swap=(0,2,1)
    check('closed_visible_resolvent_has_output_exchange_symmetry',all(A[i][j]==A[swap[i]][swap[j]] for A in closed_numerators for i in range(3) for j in range(3)))
    check('output_lead_metrics_equal',port_metric[1]==port_metric[2])
    # A two-site truncation checks the contact assembly explicitly. Its energy
    # is K plus metric-weighted squares on each contact/link and a Dirichlet end.
    size=n+6;finite=zero(size,size)
    for i in range(n):
        for j in range(n):finite[i][j]=K[i][j]
    finite_metric=metric+[port_metric[j] for j in range(3) for _ in range(2)]
    for j in range(3):
        first=n+2*j;second=first+1
        for a,b in ((j,first),(first,second)):
            assert finite_metric[a]==finite_metric[b]
            finite[a][a]=finite[a][a]+1;finite[b][b]=finite[b][b]+1
            finite[a][b]=finite[a][b]-1;finite[b][a]=finite[b][a]-1
        finite[second][second]=finite[second][second]+1
    check('positive_contact_construction_has_correct_central_block',equal(block(finite,range(n),range(n)),central_with_contact))
    check('free_lead_diagonals_are_two',all(finite[i][i]==2 for i in range(n,size)))
    check('finite_contact_metric_self_adjoint',all(C(finite_metric[i])*finite[i][j]==C(finite_metric[j])*finite[j][i].conjugate() for i in range(size) for j in range(size)))
    # Interior band E=2-2cos(k), eta=exp(ik), k in (0,pi). Rational half-angle
    # parameters give exact test energies without numerical root approximations.
    samples=[]
    for tau in (Q(1,2),Q(1),Q(2)):
        cosine=(1-tau*tau)/(1+tau*tau);sine=2*tau/(1+tau*tau)
        E=2-2*cosine;require_open_band(E)
        eta=C(cosine,sine);gamma=2*sine;ii=C(0,1)
        tag=str(E)
        print('Exact port scattering at E='+tag,flush=True)
        check('propagating_dispersion_'+tag,0<E<4 and sine>0 and eta.abs2()==1 and C(E-2)+eta+eta.conjugate()==0)
        # Semi-infinite lead surface resolvent g=-eta, self-energy=-eta.
        # The positive contact adds +1 to the central diagonal.
        lead_surface=-eta
        check('retarded_lead_surface_equation_'+tag,lead_surface*(C(E-2)-lead_surface)==1 and lead_surface.s.a<0 and lead_surface.s.b==0)
        M=add(scale(E,eye(n)),scale(-1,central_with_contact))
        M=add(M,scale(eta,contact))
        response=solve(M,V);Gpp=block(response,range(3),range(3))
        # Independently eliminate all eight hidden coordinates using their
        # previously certified exact polynomial self-energy.
        denominator=evaluate_scalar(hidden_D,E);assert denominator
        sigma=scale(C(denominator.inverse()),evaluate_matrix(sigma_coefficients,E))
        reduced_pencil=add(add(scale(E,eye(3)),scale(-1,Kpp)),scale(eta-1,eye(3)))
        reduced_pencil=add(reduced_pencil,scale(-1,sigma))
        Gschur=solve(reduced_pencil,eye(3))
        check('full_and_hidden_eliminated_open_responses_match_'+tag,equal(Gpp,Gschur))
        # Directly check hidden rows: they are retained in the full response.
        hidden_response=block(response,range(3,n),range(3))
        check('all_hidden_equations_satisfied_'+tag,equal(multiply(add(scale(E,eye(8)),scale(-1,Kqq)),hidden_response),multiply(Kqp,Gpp)))
        # S differs from the physical endpoint-wave convention only by the
        # common unit-modulus phase -eta^2.
        S=add(eye(3),scale(-ii*gamma,Gpp))
        physical_S=scale(-eta*eta,S)
        W=diag(port_metric)
        check('flux_metric_unitarity_'+tag,equal(multiply(multiply(adjoint(S),W),S),W))
        inverseW=diag([g.inverse() for g in port_metric])
        check('flux_metric_unitarity_both_orders_'+tag,equal(multiply(multiply(S,inverseW),adjoint(S)),inverseW))
        probability=[[port_metric[i]/port_metric[j]*S[i][j].abs2() for j in range(3)] for i in range(3)]
        check('all_incoming_fluxes_normalized_'+tag,all(sum((probability[i][j] for i in range(3)),F())==1 for j in range(3)))
        check('probabilities_nonnegative_'+tag,all(not p or p.positive() for row in probability for p in row))
        check('reciprocal_normalized_probabilities_'+tag,all(probability[i][j]==probability[j][i] for i in range(3) for j in range(3)))
        check('identical_output_probabilities_'+tag,probability[1][0]==probability[2][0] and bool(probability[1][0]))
        # Verify the actual discrete equations for three independent incoming
        # plane waves, rather than only assuming a scattering formula.
        internal=scale(ii*gamma*eta,response)
        psi1=add(eye(3),physical_S)
        psi2=add(scale(eta.conjugate(),eye(3)),scale(eta,physical_S))
        check('lead_endpoint_equations_'+tag,equal(add(add(scale(E-2,psi1),psi2),block(internal,range(3),range(3))),zero(3,3)))
        check('central_contact_equations_'+tag,equal(multiply(add(scale(E,eye(n)),scale(-1,central_with_contact)),internal),scale(-1,multiply(V,psi1))))
        # Two lossy shortcuts can still appear innocuous: wrong flux convention,
        # or a different smaller Hermitian system after deleting the hidden block.
        euclidean_sums=[sum((S[i][j].abs2() for i in range(3)),F()) for j in range(3)]
        check('ignoring_metric_breaks_probability_normalization_'+tag,any(x!=1 for x in euclidean_sums))
        erased_pencil=add(add(scale(E,eye(3)),scale(-1,Kpp)),scale(eta-1,eye(3)))
        erasedG=solve(erased_pencil,eye(3));erasedS=add(eye(3),scale(-ii*gamma,erasedG))
        check('erasing_hidden_block_changes_scattering_'+tag,not equal(erasedS,S))
        check('erased_model_can_still_be_unitary_'+tag,equal(multiply(multiply(adjoint(erasedS),W),erasedS),W))
        erased_probability=[[port_metric[i]/port_metric[j]*erasedS[i][j].abs2() for j in range(3)] for i in range(3)]
        check('hidden_erasure_changes_normalized_probabilities_'+tag,any(erased_probability[i][j]!=probability[i][j] for i in range(3) for j in range(3)))
        samples.append({'half_angle_parameter':str(tau),'energy':str(E),'eta':eta.encoded(),'lead_width':str(gamma),
            'S_in_port_coordinates':encoded_matrix(S),
            'normalized_probabilities':[[p.encoded() for p in row] for row in probability],
            'probabilities_decimal':[[approximate(p) for p in row] for row in probability],
            'incoming_belt_reflection':approximate(probability[0][0]),
            'incoming_belt_each_output':approximate(probability[1][0]),
            'unweighted_column_sums':[p.encoded() for p in euclidean_sums],
            'erased_hidden_incoming_belt_probabilities':[approximate(erased_probability[i][0]) for i in range(3)]})
    rejected=[]
    for energy in map(Q,(-1,0,4,5)):
        try:require_open_band(energy)
        except ValueError:rejected.append(energy)
    check('threshold_and_out_of_band_inputs_rejected',len(rejected)==4)
    result={'verification_passed':all(checks.values()),'checks':checks,
        'central_source_dimension':11,'retained_hidden_dimension':8,'channels':['belt_collective','proton_port','electron_current_port'],
        'lead_contract':{'onsite':'2','hopping':'-1','contact_energy':'sum_j h_j |x_j-psi_j,1|^2','continuum_band':['0','4'],
            'lead_metric':'h_j at every site in lead j','central_contact_shift':'diag(1,1,1,0,...,0)',
            'domain':'0<E<4; thresholds require limits, outside-band modes are evanescent'},
        'retarded_surface_resolvent':'g(E)=-exp(ik), E=2-2cos(k), 0<k<pi',
        'open_response':'G=(EI-K-P+exp(ik)P)^(-1)',
        'scattering_convention':'S=I-i Gamma G_PP, Gamma=2sin(k); physical endpoint convention is -exp(2ik)S',
        'probability_formula':'P(i<-j)=(h_i/h_j)|S_ij|^2; all three leads have the same group velocity',
        'metric':[g.encoded() for g in port_metric],'samples':samples,
        'all_energy_symmetry_argument':'Closed visible resolvent commutes with output swap; identical lead/contact self-energies and equal output metrics preserve it. Equal output flux follows throughout the propagating band wherever the response is defined.',
        'qualifications':['Lead and contact laws are declared, not derived from shape topology or fitted to 372.',
            'Three ports are not a two-particle survival/2gamma/3gamma asymptotic dictionary.',
            'Scattering normalization concerns incoming propagating lead states, not arbitrary initial central excitations.',
            'Bound-state content, thresholds, finite wave packets and continuously moving ports are not yet analyzed.',
            'Full electron spinor coupling, physical energy calibration and physical interaction identification remain open.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in (source_path,Path(__file__),BASE/'checkers/check_native_adapter_collective_closure.py')}}
    (BASE/'results/native_port_scattering.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'samples':[{'E':s['energy'],'R':s['incoming_belt_reflection'],'each_T':s['incoming_belt_each_output']} for s in samples]},indent=2))

if __name__=='__main__':main()

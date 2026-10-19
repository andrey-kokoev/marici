"""Read internal phase from retained native records, with no external t input.

Standard-library numerical audit, not exact source certification. Archived
spectral values only propose polynomial projectors: their complete spectral
identities are tested against the actual matrix. No supplier is executed.
"""
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
import ast,cmath,json,math

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'research/scattering/high-energy/pentachoron_connected_phase_energy_bundle.zip'
FREEZE=ROOT/'research/strominger/inputs/native-relational-clock-freeze.json'


def scalar(text):
    def walk(n):
        if isinstance(n,ast.Constant) and type(n.value) in (int,float):return n.value
        if isinstance(n,ast.Name) and n.id=='I':return 1j
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,(ast.UAdd,ast.USub)):
            return walk(n.operand)*(1 if isinstance(n.op,ast.UAdd) else -1)
        if isinstance(n,ast.BinOp):
            a,b=walk(n.left),walk(n.right)
            if isinstance(n.op,ast.Add):return a+b
            if isinstance(n.op,ast.Sub):return a-b
            if isinstance(n.op,ast.Mult):return a*b
            if isinstance(n.op,ast.Div):return a/b
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='sqrt' and len(n.args)==1 and not n.keywords:
            return math.sqrt(walk(n.args[0]))
        raise ValueError('Unadmitted archived coefficient')
    return complex(walk(ast.parse(text,mode='eval').body))


def eye(n):return [[complex(i==j) for j in range(n)] for i in range(n)]
def adj(a):return [[z.conjugate() for z in col] for col in zip(*a)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[c*x for x in row] for row in a]
def diff(a,b):return add(a,scale(-1,b))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def inner(a,b):return sum(x.conjugate()*y for x,y in zip(a,b))
def outer(a,b):return [[x*y.conjugate() for y in b] for x in a]
def trace(a):return sum(a[i][i] for i in range(len(a)))
def norm(a):return math.sqrt(sum(abs(z)**2 for row in a for z in row))
def vnorm(v):return math.sqrt(sum(abs(z)**2 for z in v))
def vdiff(a,b):return [x-y for x,y in zip(a,b)]
def record(z):return {'real':float(complex(z).real),'imag':float(complex(z).imag)}
def encoded(a):return [[record(z) for z in row] for row in a]


def projector(H,energies,i):
    identity=eye(len(H));P=identity
    for j,E in enumerate(energies):
        if i!=j:P=mm(P,scale(1/(energies[i]-E),diff(H,scale(E,identity))))
    return P


def main():
    assert json.loads(FREEZE.read_text())['disposition']=='preregistered; not yet computed'
    with ZipFile(SOURCE) as z:
        manifest=json.loads(z.read('SHA256.json'))
        for name,digest in manifest.items():assert sha256(z.read(name)).hexdigest()==digest
        raw=z.read('pentachoron_connected_phase_energy_results.json');receipt=json.loads(raw)
    read=lambda name:[[scalar(v) for v in row] for row in receipt['matrices'][name]]
    L,X,T=map(read,('L_original','cycle_X','cycle_T'));H=add(L,X);n=len(H);assert n==20
    identity=eye(n)
    residuals={'hermitian':norm(diff(H,adj(H))),
               'cycle_defect':norm(diff(X,mm(adj(diff(T,identity)),diff(T,identity))))}
    values=receipt['with_retained_cycles']['original_spectrum'];groups=[]
    for E in values:
        if not groups or abs(E-groups[-1][0])>1e-8:groups.append([])
        groups[-1].append(E)
    assert len(groups)==5 and all(len(g)==4 for g in groups)
    energies=[sum(g)/len(g) for g in groups];Ps=[projector(H,energies,i) for i in range(5)]
    total=[[0j]*n for _ in range(n)];rebuilt=[[0j]*n for _ in range(n)]
    for i,(E,P) in enumerate(zip(energies,Ps)):
        total=add(total,P);rebuilt=add(rebuilt,scale(E,P))
        residuals[f'projector_{i}']=max(norm(diff(mm(P,P),P)),norm(diff(P,adj(P))),abs(trace(P)-4),norm(diff(mm(H,P),scale(E,P))))
        for j in range(i):assert norm(mm(P,Ps[j]))<2e-9
    residuals['spectral_completeness']=norm(diff(total,identity))
    residuals['source_operator_reconstruction']=norm(diff(rebuilt,H))
    assert max(residuals.values())<2e-9
    # A corrupted archived eigenvalue must not pass the same matrix test.
    bad=energies[:];bad[1]+=0.125;badP=projector(H,bad,1)
    assert norm(diff(mm(H,badP),scale(bad[1],badP)))>1e-3
    Pg,Pe=Ps[:2];Eg,Ee=energies[:2];gap=Ee-Eg
    incoming=scale(1/4,Pg)
    residuals['incoming_stationarity']=norm(diff(mm(H,incoming),mm(incoming,H)))
    assert residuals['incoming_stationarity']<2e-9 and Eg>0
    # Exactly stationary algebraically: a spectral projector commutes with H.
    # Matrix residuals check this instance; they are not rigorous error bounds.
    address=[complex(i==0) for i in range(n)]
    ground,excited=mv(Pg,address),mv(Pe,address)
    weights=[inner(v,v).real for v in (ground,excited)];assert min(weights)>1e-8
    ground=[z/math.sqrt(weights[0]) for z in ground];excited=[z/math.sqrt(weights[1]) for z in excited]
    residuals['ground_eigenvector']=vnorm(vdiff(mv(H,ground),[Eg*z for z in ground]))
    residuals['excited_eigenvector']=vnorm(vdiff(mv(H,excited),[Ee*z for z in excited]))
    assert abs(inner(ground,excited))<2e-9
    coherence_op=outer(ground,excited)
    q_cos=add(coherence_op,adj(coherence_op));q_sin=scale(1/1j,diff(coherence_op,adj(coherence_op)))
    readings=[];populations_all=[];wrapped=[]
    phases=[i*math.pi/8 for i in range(33)]
    for theta in phases:
        phase=cmath.exp(-1j*theta)
        psi=[(g+phase*e)/math.sqrt(2) for g,e in zip(ground,excited)]
        coherence=2*inner(psi,mv(coherence_op,psi))
        assert abs(coherence-phase)<2e-9
        quadratures=[inner(psi,mv(Q,psi)).real for Q in (q_cos,q_sin)]
        assert abs(quadratures[0]-math.cos(theta))<2e-9 and abs(quadratures[1]+math.sin(theta))<2e-9
        derivative=[-1j*phase*e/math.sqrt(2) for e in excited]
        native_derivative=[-1j*z/gap for z in mv(diff(H,scale(Eg,identity)),psi)]
        assert vnorm(vdiff(derivative,native_derivative))<2e-9
        assert abs(inner(psi,mv(H,psi)).real-(Eg+Ee)/2)<2e-9
        assert abs(inner(psi,psi)-1)<2e-9
        predicted=[(abs(g)**2+abs(e)**2)/2+(g.conjugate()*e*phase).real for g,e in zip(ground,excited)]
        populations=[abs(z)**2 for z in psi];assert vnorm(vdiff(populations,predicted))<2e-9
        shifted=[cmath.exp(0.731j)*z for z in psi]
        assert abs(2*inner(shifted,mv(coherence_op,shifted))-coherence)<2e-9
        readings.append({'phase_modulo':record(coherence),'quadratures':quadratures,'all_native_populations':populations})
        populations_all.append(populations);wrapped.append(-cmath.phase(coherence))
    unwrapped=[wrapped[0]]
    for current,previous in zip(wrapped[1:],wrapped[:-1]):
        increment=(current-previous+math.pi)%(2*math.pi)-math.pi
        unwrapped.append(unwrapped[-1]+increment)
    assert max(abs(x-y) for x,y in zip(unwrapped,phases))<2e-9
    population_range=max(max(col)-min(col) for col in zip(*populations_all));assert population_range>1e-4
    assert vnorm(vdiff(populations_all[0],populations_all[16]))<2e-9
    assert abs(unwrapped[16]-unwrapped[0]-2*math.pi)<2e-9
    offset=7
    assert norm(diff(diff(add(H,scale(offset,identity)),scale(Eg+offset,identity)),diff(H,scale(Eg,identity))))<2e-9
    dephased=scale(1/2,add(outer(ground,ground),outer(excited,excited)))
    residuals['dephased_stationarity']=norm(diff(mm(H,dephased),mm(dephased,H)))
    assert residuals['dephased_stationarity']<2e-9 and abs(2*trace(mm(dephased,coherence_op)))<2e-9
    checks={'archive_manifest_and_matrix_spectral_identities':True,
            'corrupted_spectral_value_rejected':True,'all_twenty_source_coordinates_retained':True,
            'positive_energy_incoming_mixture_has_no_internal_clock':True,
            'source_addressed_coherent_control_has_readable_phase_quadratures':True,
            'clock_orbit_matches_native_generator':True,
            'all_native_populations_predicted_without_external_time':True,
            'clock_ignores_common_phase_and_energy_offset':True,
            'identical_endpoints_need_winding_history':True,
            'dephasing_erases_clock_without_changing_mean_energy':True}
    result={'status':'passed','checks':checks,
        'scientific_disposition':'The actual incoming mixture has no internal clock. A declared coherent preparation of existing source modes supplies a readable relative phase and native observable changes, but not selected physical time.',
        'source_dimension':n,'source_ground_multiplicity':4,'ground_energy_model_units':Eg,
        'first_excited_energy_model_units':Ee,'gap_model_units':gap,'control_projection_weights':weights,
        'control_source_address':0,'ground_mode':[record(z) for z in ground],'excited_mode':[record(z) for z in excited],
        'incoming_density':encoded(incoming),'source_native_operator':encoded(H),
        'maximum_native_population_range':population_range,'readings':readings,
        'history_unwrapped_phase':unwrapped,'residuals':residuals,
        'clock_definition':'Read both quadratures of 2 Tr(rho |g><e|); retain oriented winding. No external t is an argument of the observable reconstruction.',
        'generator_relation':'d psi/d theta=-i(H-E_ground I)psi/gap, modulo common phase.',
        'not_derived':['Native selection of this coherent preparation.','A monotone processing history and orientation.','Seconds, local-global clock coupling, time dilation or Einstein dynamics.'],
        'scope':'Standard-library numerical audit of archived matrices and explicit two-mode algebra; not a supplier rerun or rigorous numerical error certificate.',
        'source_hashes':{SOURCE.relative_to(ROOT).as_posix():sha256(SOURCE.read_bytes()).hexdigest(),
                        FREEZE.relative_to(ROOT).as_posix():sha256(FREEZE.read_bytes()).hexdigest(),
                        'archived_receipt':sha256(raw).hexdigest(),'checker':sha256(Path(__file__).read_bytes()).hexdigest()}}
    out=ROOT/'research/strominger/results/native-relational-clock.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'incoming_has_clock':False,
        'coherent_control_has_clock':True,'gap_model_units':gap,'maximum_native_population_range':population_range,
        'maximum_matrix_residual':max(residuals.values()),'physical_time_derived':False},indent=2))

if __name__=='__main__':main()

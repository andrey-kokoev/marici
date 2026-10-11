"""Source-bound real-slice/positive-pairing test; not a new Ward identity audit.
uv run --with sympy python research/nima/checkers/check_ward_chart_real_cut_obstruction.py
"""
import hashlib
from itertools import permutations, product
import json
from pathlib import Path
import re
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
SOURCE = OWNER/'check_two_open_pair_ward_naturality.rs'
CONTRACT = OWNER/'contracts/ward-chart-real-cut-obstruction.v1.json'
OUT = OWNER/'results/ward-chart-real-cut-obstruction.json'
CHECKS = []


def require(name,value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)


def equal(A,B):
    return (A-B).applyfunc(s.simplify) == s.zeros(*A.shape)


def body(text,name):
    start = re.search(r'\bfn\s+'+re.escape(name)+r'\s*\(',text)
    if start is None:
        raise ValueError('Missing source function '+name)
    left = text.index('{',start.end())
    depth,quoted,escaped = 1,False,False
    for i in range(left+1,len(text)):
        char = text[i]
        if quoted:
            if escaped: escaped = False
            elif char == '\\': escaped = True
            elif char == '"': quoted = False
        elif char == '"': quoted = True
        elif char == '{': depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0: return text[left+1:i]
    raise ValueError('Unclosed source function '+name)


def compact(text):
    return re.sub(r'\s+','',text)


def read_source(text):
    """Restricted, fail-closed reader of the actual seven-primitive match table."""
    a = s.Symbol('a',real=True,nonzero=True)  # Necessary target-real valuation.
    names = re.findall(r'const (VAR_[A-Z0-9]+): usize = \d+;',text)
    variables = {name:(a if name == 'VAR_A' else s.Symbol(name[4:])) for name in names}
    source_body = body(text,'base_gram')
    table = source_body.split('match (first, second) {',1)[1].split('pair =>',1)[0]
    pattern = re.compile(r'\s*(\(\d+,\s*\d+\)(?:\s*\|\s*\(\d+,\s*\d+\))*)\s*=>\s*(.*?)\s*,(?=\s*(?:\(\d+,|$))',re.S)
    G,seen,pos = s.zeros(7),set(),0
    while table[pos:].strip():
        match = pattern.match(table,pos)
        if match is None:
            raise ValueError('Unparsed Gram arm near '+table[pos:pos+100])
        lhs,expression = match.groups()
        expression = compact(expression)
        if expression == 'Polynomial::default()':
            value = s.S.Zero
        else:
            atoms = re.findall(r'variable\((VAR_[A-Z0-9]+),(-?\d+)\)',expression)
            if not atoms:
                raise ValueError('Unknown Gram expression '+expression)
            terms = [f'variable({name},{coefficient})' for name,coefficient in atoms]
            expected = terms[0]+''.join('.add(&'+term+')' for term in terms[1:])
            if expression != expected:
                raise ValueError('Unsupported Gram operation '+expression)
            value = sum(int(coefficient)*variables[name] for name,coefficient in atoms)
        for i,j in re.findall(r'\((\d+),\s*(\d+)\)',lhs):
            i,j = int(i),int(j)
            if (i,j) in seen or not 0 <= i <= j < 7:
                raise ValueError('Duplicate or invalid source pairing')
            seen.add((i,j)); G[i,j] = G[j,i] = value
        pos = match.end()
    require('complete-seven-primitive-table',seen == {(i,j) for i in range(7) for j in range(i,7)})
    # These guards bind the derived road/reference coordinates below to their
    # actual source definitions. Any unsupported source change fails admission.
    for name,first in (('p',0),('k',2)):
        expected = f'''match road {{ 0 => Vector::primitive({first}), 1 => Vector::primitive({first+1}),
        2 => Vector::primitive({first}).plus(Vector::primitive({first+1})).scale(-1), _ => unreachable!(), }}'''
        require('source-road-map:'+name,compact(body(text,name)) == compact(expected))
    expected_momentum = '''let road = slot / 2; if slot % 2 == 0 { p(road) } else { k(road).scale(-1) }'''
    expected_reference = '''assert!(shift == 1 || shift == 2); let road = slot / 2;
        if slot % 2 == 0 { k((road + shift) % 3) } else { p((road + shift) % 3) }'''
    require('source-edge-momenta',compact(body(text,'edge_momentum')) == compact(expected_momentum))
    require('source-edge-references',compact(body(text,'edge_reference')) == compact(expected_reference))
    require('localized-source-reference-division','shift_exponent(VAR_A,-1)' in compact(body(text,'divide_by_reference')))
    require('unchanged-source-size','const VERTICES: usize = 5;' in text and 'const BASE_PRIMITIVES: usize = 7;' in text and 'const TEST_VECTORS: usize = 4;' in text)
    return a,G


def projector(p,r,metric):
    denominator = (p.T*metric*r)[0]
    if denominator == 0:
        raise ValueError('Singular reference chart')
    return (-metric+(p*r.T+r*p.T)/denominator).applyfunc(s.simplify)


def encoded(M):
    return [[str(v) for v in row] for row in M.tolist()]


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    source_bytes = SOURCE.read_bytes()
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    require('frozen-contract',contract['schema'] == 'marici.nima.ward-chart-real-cut-obstruction.v1')
    a,G7 = read_source(source_bytes.decode('utf-8'))
    G = G7[:4,:4]
    expected = s.Matrix([[0,0,0,a],[0,0,-a,0],[0,-a,0,0],[a,0,0,0]])
    require('actual-source-momentum-block',G == expected)
    require('polarization-gauge-data-cannot-change-block',G.free_symbols == {a})
    B = s.Matrix.hstack(*(s.Matrix(c) for c in contract['predictions']['congruence_basis_columns']))
    D = s.diag(2*a,2*a,-2*a,-2*a)
    require('invertible-congruence',B.det() != 0 and B.T*G*B == D)
    require('source-determinant',G.det() == a**4)
    for sign in (-1,1):
        eigenvalues = G.subs(a,sign).eigenvals()
        require('both-real-signs-have-inertia-22',eigenvalues == {s.Integer(-1):2,s.Integer(1):2})
        require('signature-convention-does-not-repair',(-G).subs(a,sign).eigenvals() == eigenvalues)
    signed_permutations = 0
    for order,signs in product(permutations(range(4)),product((-1,1),repeat=4)):
        P = s.zeros(4)
        for j,i in enumerate(order): P[i,j] = signs[j]
        transformed = P.T*G*P
        C = P.T*B
        require('crossing-relabel-congruence',C.T*transformed*C == D)
        signed_permutations += 1
    p = [s.eye(4)[:,0],s.eye(4)[:,1],-s.eye(4)[:,0]-s.eye(4)[:,1]]
    k = [s.eye(4)[:,2],s.eye(4)[:,3],-s.eye(4)[:,2]-s.eye(4)[:,3]]
    denominators = {}
    for slot,shift in product(range(6),(1,2)):
        road = slot//2
        momentum = p[road] if slot%2 == 0 else -k[road]
        reference = k[(road+shift)%3] if slot%2 == 0 else p[(road+shift)%3]
        value = (momentum.T*G*reference)[0]
        require('all-native-reference-denominators',value in (a,-a))
        denominators[f'{slot},{shift}'] = value
    require('real-boundary-leaves-localized-chart',all(v.subs(a,0) == 0 for v in denominators.values()))
    require('boundary-momentum-Gram-zero',G.subs(a,0) == s.zeros(4))
    eta = s.diag(1,-1,-1,-1)
    complex_point = s.Matrix.hstack(s.Matrix([1,0,0,1]),s.Matrix([0,1,s.I,0]),
                                   s.Matrix([0,a/2,-s.I*a/2,0]),s.Matrix([a/2,0,0,-a/2]))
    require('complex-Minkowski-control',equal(complex_point.T*eta*complex_point,G))
    require('complex-control-not-a-real-momentum-tuple',complex_point[2,1] == s.I)
    split_metric = s.diag(1,1,-1,-1)
    split_point = s.Matrix.hstack(s.Matrix([1,0,1,0]),s.Matrix([0,1,0,1]),
                                 s.Matrix([0,-a/2,0,a/2]),s.Matrix([a/2,0,-a/2,0]))
    require('real-split-signature-control',equal(split_point.T*split_metric*split_point,G)
            and all(v.is_real for v in split_point))
    # Extend the controls to all seven base primitives by epsilon_i=p_i.
    # This is one source-consistent specialization, not a generic 4D embedding
    # of all free Gram coordinates or the four additional test vectors.
    valuation = {v:s.S.Zero for v in G7.free_symbols if v != a}
    valuation.update({s.Symbol('E0K1'):a,s.Symbol('E1K0'):-a,s.Symbol('E2K0'):a})
    for coordinates,metric in ((complex_point,eta),(split_point,split_metric)):
        seven = s.Matrix.hstack(coordinates,coordinates[:,0],coordinates[:,1],-coordinates[:,0]-coordinates[:,1])
        require('full-base-specialization-control',equal(seven.T*metric*seven,G7.subs(valuation)))
    point = complex_point.subs(a,1)
    cp,ck = [point[:,0],point[:,1],-point[:,0]-point[:,1]], [point[:,2],point[:,3],-point[:,2]-point[:,3]]
    J = s.Matrix([1,0,0,0])
    bad = projector(cp[1],ck[0],eta)  # Native slot=2, shift=2.
    require('actual-analytic-closure',bad == s.diag(-1,0,0,1))
    require('Ward-transversality-survives',bad*eta*cp[1] == s.zeros(4,1) and (J.T*eta*cp[1])[0] == 0)
    mixed = -bad*eta
    require('rank-two-idempotency-is-not-positivity',mixed*mixed == mixed and mixed.rank() == 2)
    negative = (J.H*bad*J)[0]
    require('attempted-positive-pairing-rejected',negative == -1)
    for shift in (1,2):
        P = projector(cp[1],ck[(1+shift)%3],eta)
        require('both-native-reference-choices-have-same-current-contraction',(J.H*P*J)[0] == -1)
    polarizations = s.Matrix.hstack(s.I*J,s.Matrix([0,0,0,1]))
    require('legitimate-bilinear-completeness',polarizations*polarizations.T == bad)
    hermitian_sum = polarizations*polarizations.H
    require('conjugation-changes-the-closure',hermitian_sum == s.diag(1,0,0,1) and hermitian_sum != bad)
    # A real boundary point exists, but the original graph references fail.
    n,r = s.Matrix([1,0,0,1]),s.Matrix([1,0,0,-1])
    boundary = s.Matrix.hstack(n,2*n,3*n,4*n)
    require('real-collinear-boundary-control',boundary.T*eta*boundary == G.subs(a,0))
    caught = False
    try: projector(n,3*n,eta)
    except ValueError: caught = True
    require('collinear-native-reference-refused',caught)
    good = projector(n,r,eta)
    helicities = s.Matrix.hstack(s.Matrix([0,1,s.I,0])/s.sqrt(2),s.Matrix([0,1,-s.I,0])/s.sqrt(2))
    require('new-reference-real-photon-control',good == s.diag(0,1,1,0) and helicities*helicities.H == good)
    # Ordinary real 2-to-2 null kinematics is not excluded; it has different Gram data.
    real_scattering = s.Matrix.hstack(s.Matrix([1,1,0,0]),s.Matrix([1,-1,0,0]),s.Matrix([1,0,1,0]),s.Matrix([1,0,-1,0]))
    target_gram = real_scattering.T*eta*real_scattering
    require('real-two-to-two-kinematics-survives',all(target_gram[i,i] == 0 for i in range(4))
            and real_scattering[:,0]+real_scattering[:,1] == real_scattering[:,2]+real_scattering[:,3])
    require('real-scattering-is-not-the-native-specialization',target_gram[0,1] == 2 and G[0,1] == 0)
    caught = False
    try: require('deliberately-false-Born-identification',bad == hermitian_sum)
    except AssertionError: caught = True
    require('failed-physical-identification-raises',caught)
    require('native-source-unmodified',SOURCE.read_bytes() == source_bytes)
    result = {'schema':'marici.nima.ward-chart-real-cut-obstruction-result.v1','status':'pass',
              'classification':'generic-native-Ward-chart-has-no-direct-real-Lorentzian-phase-space-realization',
              'strength':'exact necessary-principal-Gram obstruction; not a fresh Ward closure or full scattering reconstruction',
              'full_source_base_Gram':encoded(G7),'momentum_Gram':encoded(G),'congruence_basis':encoded(B),
              'congruence_diagonal':encoded(D),'determinant':str(G.det()),'inertia_for_real_nonzero_a':[2,2,0],
              'signed_permutation_controls':signed_permutations,
              'native_reference_denominators':{key:str(v) for key,v in denominators.items()},
              'complex_Minkowski_control':encoded(complex_point),'split_signature_control':encoded(split_point),
              'analytic_polarization_sum':encoded(bad),'conjugated_sum':encoded(hermitian_sum),
              'Ward_transverse_current_pairing':str(negative),'real_boundary_positive_sum':encoded(good),
              'real_scattering_control_Gram':encoded(target_gram),'checks':CHECKS,'scope':contract['scope'],
              'first_missing_comparison':'source-derived reconstruction to real physical amplitude and positive phase-space pairing; not a reference relabeling',
              'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (Path(__file__).resolve(),SOURCE,CONTRACT)}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','classification','inertia_for_real_nonzero_a',
                       'signed_permutation_controls','Ward_transverse_current_pairing','first_missing_comparison')},indent=2))


if __name__ == '__main__':
    main()

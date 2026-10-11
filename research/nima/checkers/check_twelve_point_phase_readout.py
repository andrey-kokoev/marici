"""Source-preserving exact phase/attachment/readout comparison; no fitting.
Run collect_phase_readout_diagnostics.py under SciPy, then this under SymPy.
"""
import ast
import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import runpy
from types import SimpleNamespace
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-phase-readout-evidence'
FULL = ROOT/'quarantine/20261007-generation-evidence/checkers/check_full_12x12_gram.py'
CHECKS = []


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def simp(m):
    return m.applyfunc(s.simplify)


def shim():
    # Exact interpretation of the SAME Euler phase constructor, no new entries.
    return {'np':SimpleNamespace(zeros=lambda shape,**kw:s.zeros(*shape)),
            'math':SimpleNamespace(cos=lambda x:(s.exp(s.I*x)+s.exp(-s.I*x))/2,
                                   sin=lambda x:(s.exp(s.I*x)-s.exp(-s.I*x))/(2*s.I)),
            'complex':lambda x,y:x+s.I*y}


def main():
    out = ROOT/'results/twelve-point-phase-readout.json'
    out.unlink(missing_ok=True)
    CHECKS.clear()
    transport = ROOT/'results/phase-readout-transport.json'
    data = json.loads(transport.read_text(encoding='utf-8'))
    require('transport-schema', data['schema'] == 'marici.nima.phase-readout-transport.v1')
    expected = {'checkers/collect_phase_readout_diagnostics.py','checkers/collect_continuum_diagnostics.py',
                str(FULL.relative_to(ROOT)).replace('\\','/'),
                'quarantine/20261007-phase-readout-evidence/checkers/check_flavor_solver.py',
                'quarantine/20261007-phase-readout-evidence/checkers/check_ckm_variational.py'}
    require('complete-source-binding', set(data['source_sha256']) == expected)
    for name,h in data['source_sha256'].items():
        require('source-current:' + name, hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == h)
    for archive,count in [(ARCHIVE,5),(ROOT/'quarantine/20261007-generation-evidence',9)]:
        entries = [line.split(maxsplit=1) for line in (archive/'SHA256SUMS').read_text().splitlines()]
        require('originals-preserved:' + archive.name,len(entries) == count)
        for h,name in entries:
            require('archive:' + archive.name + ':' + name,
                    hashlib.sha256((archive/name.lstrip('*')).read_bytes()).hexdigest() == h)
    require('historical-receipts-untouched',data['historical_receipts_unchanged'])
    require('syntax-defect-is-not-mathematical-evidence', data['variational_execution_defect']['type'] == 'SyntaxError')
    G0 = s.Matrix(data['base_gram']).applyfunc(s.Rational)
    require('old-full-matrix-not-substituted',G0.shape == (12,12) and all(
        G0[i,j] == (3456 if i == j else 1152 if i//4 == j//4 else 576)
        for i in range(12) for j in range(12)))
    theta = s.symbols('theta0:12', real=True)
    tree = ast.parse(FULL.read_text(encoding='utf-8'))
    def writes(node,name):
        return any(isinstance(t,ast.Subscript) and isinstance(t.value,ast.Name) and t.value.id == name
                   for n in ast.walk(node) if isinstance(n,ast.Assign) for t in n.targets)
    loops = [node for node in tree.body if isinstance(node,ast.For) and writes(node,'G_phased')]
    require('one-actual-full-phase-constructor',len(loops) == 1)
    env = shim() | {'G_base':G0,'G_phased':s.zeros(12),'theta':theta}
    exec(compile(ast.Module(body=loops,type_ignores=[]),str(FULL),'exec'),env)
    G = env['G_phased']
    D = s.diag(*(s.exp(s.I*t) for t in theta))
    require('full-twelve-slot-unitarity',D.H*D == s.eye(12))
    require('full-source-conjugation-law',simp(G-D.H*G0*D) == s.zeros(12))
    # Positivity/spectrum belongs to the whole supplied source, not just subblocks.
    require('base-spectrum-reused',G0.eigenvals() == {s.Integer(11520):1,s.Integer(4608):2,s.Integer(2304):9})
    rows_u,rows_d,cols = (data['indices'][k] for k in ('up_indices','down_indices','doublet_indices'))
    require('actual-readout-roles', (rows_u,rows_d,cols) == ([1,5,9],[0,4,8],[2,6,10]))
    A = G0.extract(rows_u,cols)
    require('same-base-cross-blocks', A == G0.extract(rows_d,cols) == 576*(s.eye(3)+s.ones(3)))
    L, Ru, Rd = (D.extract(ids,ids) for ids in (cols,rows_u,rows_d))
    Mu,Md = G.extract(rows_u,cols),G.extract(rows_d,cols)
    require('actual-up-attachment',simp(Mu-Ru.H*A*L) == s.zeros(3))
    require('actual-down-attachment',simp(Md-Rd.H*A*L) == s.zeros(3))
    HQ = simp(Mu.H*Mu)
    require('shared-doublet-operators-equal',simp(HQ-Md.H*Md) == s.zeros(3))
    require('adjoint-adapter-to-existing-flavor-convention',simp(HQ-L.H*A**2*L) == s.zeros(3))
    # Y= M^dagger: doublet rows, singlet columns. No untyped transpose swap.
    require('independent-singlet-phases-remove-together',simp(L*Mu.H*Ru.H-A) == s.zeros(3)
            and simp(L*Md.H*Rd.H-A) == s.zeros(3))
    U = s.Matrix.hstack(s.Matrix([1,-1,0])/s.sqrt(2),
                       s.Matrix([1,1,-2])/s.sqrt(6),s.ones(3,1)/s.sqrt(3))
    eigen = s.diag(576,576,2304)
    require('entire-three-mode-spectral-frame',simp(U.H*U) == s.eye(3) and A*U == U*eigen)
    require('aligned-common-doublet-frame',simp((L.H*U).H*(L.H*U)) == s.eye(3))
    require('right-space-is-not-common-doublet-space',simp(Mu*Mu.H-Ru.H*A**2*Ru) == s.zeros(3))

    # Uniform U(2) ambiguity lemma, including arbitrary complex phases of v.
    # For a nonzero two-vector v, this changes a displayed modulus, not its source.
    r = s.symbols('r',positive=True)
    p,q,t = s.symbols('p q t',real=True)
    # A positive radius encodes the stated nonzero domain. This also covers
    # zero in EITHER component, without an ambiguous conjugate of 1/sqrt(0).
    v = r*s.Matrix([s.cos(t)*s.exp(s.I*p),s.sin(t)*s.exp(s.I*q)])
    W = s.Matrix([[v[0],-s.conjugate(v[1])],[v[1],s.conjugate(v[0])]])/r
    R = s.Matrix([[1,1],[-1,1]])/s.sqrt(2)
    require('all-complex-two-vector-frame-lemma',simp(W.H*W) == s.eye(2)
            and simp(W.H*v) == s.Matrix([r,0]))
    rotated = simp(R.H*W.H*v)
    require('readout-changes-at-fixed-source',s.simplify(rotated[0]*s.conjugate(rotated[0])) == r*r/2)
    require('eigenvalue-degeneracy-allows-this-change',
            s.diag(R,s.ones(1))*eigen == eigen*s.diag(R,s.ones(1)))
    require('original-numeric-instance-replayed',len(data['fixed_original_source_eigenframe_change']) == 2)

    # Lift the original solver's matrix-building body; omit only its numerical SVD.
    solver_path = ARCHIVE/'checkers/check_flavor_solver.py'
    solver_tree = ast.parse(solver_path.read_text(encoding='utf-8'))
    fn = copy.deepcopy(next(n for n in solver_tree.body if isinstance(n,ast.FunctionDef) and n.name == 'yukawa_eigenvalues'))
    cut = next(i for i,n in enumerate(fn.body) if isinstance(n,ast.Assign)
               and any(isinstance(t,ast.Name) and t.id == 'M_sq' for t in n.targets))
    fn.body = fn.body[:cut]+[ast.Return(value=ast.Name(id='Y',ctx=ast.Load()))]
    code = ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[]))
    constants = {n.targets[0].id:s.Rational(str(n.value.value)) for n in solver_tree.body
                 if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)
                 and n.targets[0].id in ('G_diag','G_off')}
    env = shim() | constants
    exec(compile(code,str(solver_path),'exec'),env)
    phi = s.symbols('phi0:3',real=True)
    Y = env['yukawa_eigenvalues'](phi)
    P = s.diag(*(s.exp(s.I*x) for x in phi))
    require('solver-exact-source-law',simp(Y-P.H*A*P) == s.zeros(3))
    require('solver-is-actually-Hermitian',simp(Y-Y.H) == s.zeros(3))
    require('solver-squared-spectrum-fixed',simp(Y*Y.H-P.H*A**2*P) == s.zeros(3))
    target = list(map(lambda v:s.Rational(str(v)),data['solver']['target']))
    floor = sum((x-y)**2 for x,y in zip([s.S.One,s.Rational(1,4),s.Rational(1,4)],target))
    require('uniform-positive-mass-target-residual',floor == s.Rational(953772669,10000000000))
    # Do not conflate this separate solver's independent doublet phases with Mu,Md.
    Ys = env['yukawa_eigenvalues']([0,s.pi,0])
    hs,ha = Ys*Ys.H,A*A.H
    pu,pa = (hs-576**2*s.eye(3))/(2304**2-576**2),s.ones(3)/3
    require('solver-can-change-relative-heavy-line',s.trace(pu*pa) == s.Rational(1,9)
            and hs*ha-ha*hs != s.zeros(3))

    # Reuse the richer sector implementation without running its receipt-writing main.
    flavor_path = ROOT.parent/'flavor/checkers/nine_link_exact_checks.py'
    flavor = runpy.run_path(str(flavor_path))
    rotation = flavor['check_rotation']()
    require('existing-flavor-invariants-still-transport',all(rotation['symbolic_invariants_equal'].values())
            and all(rotation['concrete_invariants_equal'].values()))
    require('richer-existing-source-is-not-aligned',s.sympify(rotation['det_commutator_concrete_before']) != 0)
    texture = flavor['build_textures']()['example_I_S38']
    yu,yd = texture['Yu'],texture['Yd']
    sub = {x:s.S.One for x in yu.free_symbols|yd.free_symbols}
    sub.update({flavor['eps']:s.Rational(1,10),flavor['sym']('u21'):2,flavor['sym']('d22'):2})
    yu,yd = yu.subs(sub),yd.subs(sub)
    for name,y in [('u',yu),('d',yd)]:
        h = y*y.H
        require('existing-control-full-rank:'+name,y.det() != 0)
        poly = h.charpoly()
        require('existing-control-simple-spectrum:'+name,s.discriminant(poly.as_expr(),poly.gen) != 0)
    for name in ('check_flavor_solver.py','check_ckm_variational.py'):
        stream = io.StringIO()
        exit_code = None
        try:
            with redirect_stdout(stream):
                runpy.run_path(str(ROOT/'checkers'/name),run_name='__main__')
        except SystemExit as exc:
            exit_code = exc.code
        report = json.loads(stream.getvalue())
        require('retired-verification-refused:'+name,exit_code == 2 and report['verification_performed'] is False)
    refused = False
    try:
        require('injected-phase-splitting-claim',floor == 0)
    except AssertionError:
        refused = True
    require('false-mass-fit-gate-refuses',refused)
    sources = [Path(__file__).resolve(),transport,ARCHIVE/'SHA256SUMS',
               ROOT/'quarantine/20261007-generation-evidence/SHA256SUMS',flavor_path,
               ROOT.parent/'flavor/flavor-nine-link-conventions.md',ROOT.parent/'flavor/flavor-chart-transition-packet.md',
               ROOT/'checkers/check_flavor_solver.py',ROOT/'checkers/check_ckm_variational.py']
    sources += [ROOT/name for name in data['source_sha256']]
    result = {'schema':'marici.nima.twelve-point-phase-readout.v1','status':'pass',
              'classification':'full-source-alignment; singlet-eigenframe-readout-does-not-descend; solver-mass-splitting-impossible-in-fixed-phase-law',
              'full_phase_law':'G(theta)=D^dagger G_base D',
              'attachment':'M_u=R_u^dagger A L; M_d=R_d^dagger A L; A=576(I+J)',
              'shared_doublet_squared_map':'M_u^dagger M_u=M_d^dagger M_d=L^dagger A^2 L',
              'singular_values':[576,576,2304],
              'degenerate_frame_residual':'at a nonzero two-vector, squared modulus changes from r^2 to r^2/2 without changing the source operators',
              'solver_normalized_mass_error_floor':str(floor),
              'separate_solver_heavy_line_overlap_witness':'1/9, not full-model alignment',
              'existing_flavor_control_commutator_determinant':rotation['det_commutator_concrete_before'],
              'scope':'Conditional on original matrix, standard Hermitian pairings and supplied matter roles. No physical generation map, universal mixing no-go, Born rule or new flavor fit.',
              'checks':CHECKS,'check_count':len(CHECKS),
              'source_sha256':{str(p.relative_to(ROOT.parent.parent)).replace('\\','/'):
                               hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','classification','solver_normalized_mass_error_floor','existing_flavor_control_commutator_determinant','check_count')},indent=2))


if __name__ == '__main__':
    main()

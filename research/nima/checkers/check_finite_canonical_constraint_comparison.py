"""Source-preserving finite action/parametrized-constraint comparison, not ADM.
uv run --with sympy python research/nima/checkers/check_finite_canonical_constraint_comparison.py
"""
import ast
from contextlib import redirect_stdout
import hashlib
import io
from itertools import product
import json
from pathlib import Path
import runpy
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-constraint-evidence'
CHECKS = []


def require(name,condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def same(a,b):
    return (a-b).applyfunc(s.simplify) == s.zeros(*a.shape)


def retained(path,rotor=False,hostile=False):
    """Preserve all computations/assertions; suppress only known receipt IO.
The rotor's already computed local chart objects are additionally exported.
"""
    tree = ast.parse(path.read_text(encoding='utf-8'))
    suppressed = []
    exports = []
    class Capture(ast.NodeTransformer):
        def visit_Expr(self,node):
            f = node.value.func if isinstance(node.value,ast.Call) else None
            if isinstance(f,ast.Attribute) and isinstance(f.value,ast.Name) and f.value.id == 'out':
                if f.attr in ('unlink','write_text'):
                    suppressed.append(f.attr)
                    return None
            return self.generic_visit(node)
        def visit_Return(self,node):
            if (rotor and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name)
                    and node.value.func.id == 'dict' and any(k.arg == 'contact_H' for k in node.value.keywords)):
                names = ['Sc','Gc','qi','pi','D','phasedot']
                node.value.keywords += [ast.keyword(arg=n,value=ast.Name(id=n,ctx=ast.Load())) for n in names]
                exports.append(names)
            return self.generic_visit(node)
    tree = Capture().visit(tree)
    require('known-IO-only:'+path.name,sorted(suppressed) == (['unlink','write_text'] if rotor else ['write_text']))
    if hostile:
        at = [i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id == 'all_ok' for t in n.targets)]
        require('original-gate-located',len(at) == 1)
        tree.body[at[0]:at[0]] = ast.parse("closure_checks[0]['conjugation_preserves_stabilizer'] = False").body
    env = {'__file__':str(path),'__name__':'_retained_constraint_comparison_'}
    with redirect_stdout(io.StringIO()):
        exec(compile(ast.fix_missing_locations(tree),str(path),'exec'),env)
        if rotor:
            require('checked-chart-objects-exported',len(exports) == 1)
            return env['main']()
    return env


def main():
    out = ROOT/'results/finite-canonical-constraint-comparison.json'
    out.unlink(missing_ok=True)
    CHECKS.clear()
    legacy_names = ['check_discrete_constraint_algebra.py','check_holonomy_flux_algebra.py','check_su2_promotion.py']
    receipt_names = ['discrete-constraint-algebra.json','holonomy-flux-algebra.json',
                     'field-promotion-identified.json','retained-rotor-phase-transport.json']
    receipts = [ROOT/'results'/name for name in receipt_names]
    before = [p.read_bytes() if p.exists() else None for p in receipts]
    entries = [line.split(maxsplit=1) for line in (ARCHIVE/'SHA256SUMS').read_text().splitlines()]
    require('nine-source-originals-retained',sum(not name.lstrip('*').startswith('./results/') for _,name in entries) == 9)
    for digest,name in entries:
        require('archive:'+name,hashlib.sha256((ARCHIVE/name.lstrip('*')).read_bytes()).hexdigest() == digest)
    old = {name:retained(ARCHIVE/'checkers'/name) for name in legacy_names}
    hostile = retained(ARCHIVE/'checkers'/legacy_names[0],hostile=True)
    require('old-baseline-survives',old[legacy_names[0]]['all_ok'])
    require('old-failure-did-not-fail-execution',hostile['result']['all_checks_pass'] is False
            and hostile['result']['classification'] == old[legacy_names[0]]['result']['classification'])
    for name in legacy_names[1:]:
        tree = ast.parse((ARCHIVE/'checkers'/name).read_text())
        require('formula-report-has-no-functions-or-assertions:'+name,
                not any(isinstance(n,(ast.FunctionDef,ast.Assert)) for n in ast.walk(tree)))
        with redirect_stdout(io.StringIO()):
            ns = runpy.run_path(str(ROOT/'checkers'/name))
            code = None
            try:
                ns['main']()
            except SystemExit as error:
                code = error.code
        require('quarantine-refuses-verification:'+name,code == 2)
    live = runpy.run_path(str(ROOT/'checkers'/legacy_names[0]))
    repaired = live['verify']()
    require('whole-old-group-source-preserved',live['s4'] == old[legacy_names[0]]['s4']
            and live['pts'] == old[legacy_names[0]]['pts'])
    mul,inv = live['mul'],live['inv']
    perms = live['s4']
    matrices = {g:s.Matrix(4,4,lambda i,j:int(i == g[j])) for g in perms}
    omega8 = s.zeros(8)
    omega8[:4,4:] = s.eye(4); omega8[4:,:4] = -s.eye(4)
    lifts = {g:s.diag(P,P.inv().T) for g,P in matrices.items()}
    for g in perms:
        require('canonical-action:'+str(g),lifts[g].T*omega8*lifts[g] == omega8)
        require('all-source-compositions:'+str(g),all(lifts[mul(g,h)] == lifts[g]*lifts[h] for h in perms))
    g,h = (1,0,2,3),(0,2,1,3)
    require('transport-not-commutation',mul(mul(mul(g,h),inv(g)),inv(h)) != tuple(range(4))
            and set(live['stabilizer'](0)) != set(live['stabilizer'](g[0])))

    rotor_path = ROOT/'checkers/check_retained_rotor_phase_transport.py'
    rotor = retained(rotor_path,rotor=True)
    x,k,th,phi,H = [rotor[n] for n in ('x','kappa','theta','phi','contact_H')]
    a,q,p,b = x
    require('strong-completed-H-retained',H == q*q+p*p+k and H.is_positive is True)
    require('empty-literal-zero-level',s.ask(s.Q.positive(H)) is True and H.subs({q:0,p:0}) == k)
    omega = s.Matrix([[0,0,0,-1],[0,0,1,0],[0,-1,0,0],[1,0,0,0]])
    beta = rotor['beta'](x)
    dbeta = s.Matrix(4,4,lambda i,j:s.diff(beta[j],x[i])-s.diff(beta[i],x[j]))
    require('full-four-coordinate-form',dbeta == -omega and omega.det() == 1)
    require('legacy-curvature-sign-residual',-dbeta/k-(-omega/k) == 2*omega/k and omega != s.zeros(4))
    mom,th0,eta = s.symbols('Ptheta theta0 parameter',real=True)
    coordinates = s.Matrix([*x,th,mom])
    omega_ext = s.diag(omega,s.Matrix([[0,1],[-1,0]]))
    C = mom+H
    def pb(f,g):
        return s.simplify((s.Matrix([s.diff(f,v) for v in coordinates]).T*omega_ext
                           *s.Matrix([s.diff(g,v) for v in coordinates]))[0])
    vector = s.Matrix([pb(v,C) for v in coordinates])
    require('regular-nonempty-parametrized-constraint',s.diff(C,mom) == 1 and C.subs(mom,-H) == 0
            and pb(C,C) == 0)
    require('same-full-base-generator',same(vector[:4,:],rotor['D']) and vector[4] == 1 and vector[5] == 0)
    section = s.Matrix([*x,th0,-H])
    require('section-recovers-full-symplectic-form',section.jacobian(x).T*omega_ext*section.jacobian(x) == omega)
    chi = th-th0
    constraints = [C,chi]
    brackets = s.Matrix(2,2,lambda i,j:pb(constraints[i],constraints[j]))
    require('regular-angle-section',brackets == s.Matrix([[0,-1],[1,0]]))
    for i,j in product(range(4),repeat=2):
        correction = (s.Matrix([[pb(x[i],c) for c in constraints]])*brackets.inv()
                      *s.Matrix([pb(c,x[j]) for c in constraints]))[0]
        require('Dirac-comparison:'+str((i,j)),s.simplify(pb(x[i],x[j])-correction-omega[i,j]) == 0)
    # The original lift, not an independently fitted phase law.
    alpha_ext = s.Matrix([*(-beta/k),-mom/k,0,1])
    lifted_vector = s.Matrix([*vector,rotor['phasedot']])
    require('same-phase-is-horizontal-on-constraint',s.simplify(alpha_ext.dot(lifted_vector)+C/k) == 0)
    full = s.Matrix([*coordinates,phi])
    for e in (0,1):
        sign = (-1)**e
        target,phase = rotor['lift'](eta,e,x,phi)
        moved = s.Matrix([*target,sign*th+eta,mom,phase])
        alpha_target = s.Matrix([*(-rotor['beta'](target)/k),-mom/k,0,1])
        require('complete-Pin-phase-transport:'+str(e),same(moved.jacobian(full).T*alpha_target,sign*alpha_ext))
        base = moved[:6,:]
        require('complete-Pin-canonical-transport:'+str(e),same(base.jacobian(coordinates).T*omega_ext*base.jacobian(coordinates),sign*omega_ext))
        require('constraint-transport:'+str(e),s.simplify(C.subs(dict(zip(x,target)),simultaneous=True)-C) == 0)
    ai = s.symbols('initial_scalar',real=True)
    for name in ('Sc','Gc'):
        action = rotor[name]+b*ai  # Identity type-II chart on the spectator pair (b,a).
        require('existing-HJ-chart-on-constraint:'+name,
                s.trigsimp(s.diff(action,th)+H.subs(p,s.diff(action,q))) == 0
                and s.diff(action,b) == ai and s.diff(action,ai) == b)
    # Dropping k changes the supplied module phase: it is not the same lift.
    _,actual_return_phase = rotor['lift'](s.pi,0,x,phi)
    zero_offset_phase = actual_return_phase+s.pi
    require('constant-removal-changes-full-phase',s.simplify(s.exp(s.I*(actual_return_phase-phi))) == -1
            and s.simplify(s.exp(s.I*(zero_offset_phase-phi))) == 1)
    refused = False
    try:
        require('hostile-literal-H-has-zero-point',H.subs({q:0,p:0}) == 0)
    except AssertionError:
        refused = True
    require('false-constraint-gate-refused',refused)
    require('all-historical-and-predecessor-receipts-unchanged',before == [p.read_bytes() if p.exists() else None for p in receipts])
    paths = [Path(__file__).resolve(),rotor_path,ROOT/'checkers/check_clifford_retained_order.py',
             ROOT/'retained-rotor-phase-transport.md',ROOT/'retained-rotor-generator.md',ARCHIVE/'SHA256SUMS']
    paths += [ROOT/'checkers'/name for name in legacy_names]+[ARCHIVE/'checkers'/name for name in legacy_names]
    result = {'schema':'marici.nima.finite-canonical-constraint-comparison.v1','status':'pass',
              'classification':'canonical and parametrized comparisons constructed; finite ADM and forced-SU2 promotion claims withdrawn',
              'finite_source':'All 24 S4 actions and four stabilizers retained; covariance is not commutation',
              'legacy_failed_predicate_returned_normally':True,
              'literal_rotor_H_zero':'empty for the retained positive kappa',
              'legacy_curvature_sign_residual':'2*Omega/kappa; the retained conventions give d(alpha)=+Omega/kappa',
              'conditional_constraint':str(C),'added_data':'T*R pair for the unwrapped angular parameter, not physical time',
              'retained':'four base coordinates, phase fiber, module-selected constant, two HJ charts and reversal transport',
              'first_missing_ADM_interface':'field phase space with a Poisson/constraint comparison; group conjugation does not provide it',
              'not_derived':['spacetime or physical time','GR hypersurface-deformation brackets','SU2 selection','Planck-area calibration'],
              'checks':CHECKS,'source_sha256':{str(path.relative_to(ROOT)).replace('\\','/'):
                    hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','classification','literal_rotor_H_zero','conditional_constraint')},indent=2))


if __name__ == '__main__':
    main()

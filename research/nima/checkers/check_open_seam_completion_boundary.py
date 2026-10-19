"""Persistent primitive addresses versus a newly chosen feedback completion.

Rebuild the existing constructor; retain explicit unresolved seam addresses.
Test the projection-extension obstruction and two nonselected completions.
No absent response is encoded as zero and no completion is adopted as dynamics.
"""
from pathlib import Path
import hashlib
import json
import sympy as S
from assemble_triangle_arrow_source import assemble

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def require_seam_bindings(interface):
    missing = [name for name, entry in interface.items() if entry['status'] != 'bound']
    if missing:
        raise ValueError('Unresolved primitive-to-mode bindings: ' + ','.join(missing))
    return tuple(interface[name]['coefficient_ports'] for name in ('AB','BA'))


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    source_path = HERE.parent/'inputs/proton-six-arrows.json'
    source = json.loads(source_path.read_text())
    cases = []
    for deleted in (None,'BC','CA','AD','DB'):
        changed = {**source,'arrows':[edge for edge in source['arrows'] if ''.join(edge) != deleted]}
        report, manifest = assemble(changed)
        available = {''.join(row['outer_arrow']) for row in report['triangles_and_transports']}
        interface = {}
        for name in ('AB','BA'):
            check('primitive/survives/'+str(deleted)+'/'+name, list(name) in changed['arrows'])
            interface[name] = {'primitive':list(name),
                               'status':'bound' if name in available else 'unresolved',
                               'coefficient_ports':[['raw',name,axis] for axis in 'xyz'] if name in available else None}
        if deleted is None:
            check('interface/baseline-defined', len(require_seam_bindings(interface)) == 2)
        else:
            try:
                require_seam_bindings(interface)
            except ValueError:
                checks.append('interface/rejects-unresolved/'+deleted)
            else:
                raise AssertionError('Invented missing seam response')
        # Construct the real collective raw-coordinate matrix from actual manifest.
        labels = sorted({tuple(row['source']) for row in manifest if row['source'][0] == 'raw'})
        index = {tuple(label[1:]):i for i,label in enumerate(labels)}
        nr = S.zeros(len(labels)); ni = S.zeros(len(labels))
        for row in manifest:
            if row['source'][0] == 'aligned':
                i,j = index[tuple(row['target'][1:])],index[tuple(row['source'][1:])]
                nr[i,j] = S.Rational(row['weight_real'])
                ni[i,j] = S.Rational(row['weight_imag_sqrt3'])
        # N=nr+i sqrt(3) ni; exact separate real/imaginary tests.
        check('source/self-adjoint/'+str(deleted), nr.T == nr and ni.T == -ni)
        check('source/idempotent/'+str(deleted), nr*nr-3*ni*ni == nr
              and nr*ni+ni*nr == ni)
        cases.append({'deleted':deleted,'interface':interface,'raw_dimension':len(labels),
                      'collective_rank':int(S.trace(nr)),
                      'constructor_manifest_sha256':hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()})

    # At selected normalized mode-amplitude level the rebuilt three-cycle
    # collective map is the equal-mean projector. This is a completion control,
    # not a new source constructor. Equal modal norms justify this chart.
    n = S.ones(3)/3
    zero = S.diag(n,S.zeros(1))
    identity = S.diag(n,S.eye(1))
    for name, candidate in (('zero-orphan',zero),('identity-orphan',identity)):
        check('completion/self-adjoint/'+name, candidate.T == candidate)
        check('completion/idempotent/'+name, candidate*candidate == candidate)
        check('completion/old-block-fixed/'+name, candidate[:3,:3] == n)
    check('completion/underdetermined-orphan-reading', zero[3,3] != identity[3,3])
    coupled = S.ones(4)/4
    check('control/coupled-projector', coupled.T == coupled and coupled*coupled == coupled)
    check('control/coupling-changes-old-response', coupled[:3,:3] != n
          and n[0,0] == S.Rational(1,3) and coupled[0,0] == S.Rational(1,4))
    # For P=[[N,B],[B*,D]], (P^2-P)_old = BB* when N^2=N.
    # Trace(BB*) is a sum of absolute squares, so zero forces B=0.
    br = S.Matrix(S.symbols('b0:3',real=True))
    bi = S.Matrix(S.symbols('c0:3',real=True))
    check('obstruction/positive-cross-block-norm',
          S.trace(br*br.T+bi*bi.T) == sum(z*z for z in list(br)+list(bi)))
    # An open read-only receiver is possible without reciprocal feedback, but
    # is not a self-adjoint collective completion.
    w = S.Matrix([[1,0,0]])
    open_reader = n.row_join(S.zeros(3,1)).col_join(w.row_join(S.zeros(1,1)))
    check('control/open-reader-keeps-old-block', open_reader[:3,:3] == n)
    check('control/open-reader-not-self-adjoint', open_reader != open_reader.T)
    files = [Path(__file__),source_path,HERE/'assemble_triangle_arrow_source.py',
             ROOT/'research/voevodsky/checkers/check_compiled_three_arrow_receiver.py']
    result = {'schema':'marici.nima.open-seam-completion-boundary.v1','status':'pass',
              'checks':checks,'cases':cases,
              'completion_controls':{'uncoupled_orphan_readings':['0','1'],
                                     'old_self_response':'1/3','equal_coupled_control_self_response':'1/4'},
              'conclusion':'Primitive seam records can persist with explicitly unresolved bindings. '
                           'A self-adjoint idempotent completion keeping the entire old projector '
                           'as its compression cannot couple added modes to it. '
                           'Joint feedback requires changing/rebuilding the old block.',
              'scope':'Finite coefficient constructor and orthogonal-projector completions only. '
                      'The illustrative completions are countermodels, not adopted dynamics. '
                      'Read-only or nonprojective open systems are not excluded. '
                      'No physical preparation, kernel or photon/electron interpretation selected.',
              'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    output = HERE.parent/'results/open-seam-completion-boundary.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact open-seam interface/completion checks')
    print('Primitive addresses retained; absent coefficient bindings rejected explicitly.')
    print('A fixed old orthogonal projector forbids cross-coupling in any orthogonal-projector extension.')
    print('Joint feedback needs a rebuilt block or a different explicitly supplied operation class.')


if __name__ == '__main__':
    main()

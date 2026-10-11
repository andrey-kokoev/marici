"""Exact block/action/probe comparison on the strongest existing 12-arrow source.
First run collect_generation_diagnostics.py under the admitted SciPy profile.
Then: uv run --with sympy python research/nima/checkers/check_twelve_arrow_generation_boundary.py
"""
from contextlib import redirect_stdout
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-generation-evidence'
CHECKS = []
RETIRED = ['check_larger_carrier.py','check_small_carriers.py',
           'check_subgroup_gram_hierarchy.py','check_full_12x12_gram.py',
           'check_gram_from_geometry.py','check_symmetry_breaking_hierarchy.py']


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def integral_matrix(name, values):
    matrix = s.Matrix(values).applyfunc(s.Rational)
    require('exact-integer-data:' + name, all(x.q == 1 for x in matrix))
    return matrix


def main():
    out = ROOT/'results/twelve-arrow-generation-boundary.json'
    out.unlink(missing_ok=True)
    CHECKS.clear()
    entries = [line.split(maxsplit=1) for line in (ARCHIVE/'SHA256SUMS').read_text().splitlines()]
    require('nine-preserved-inputs', len(entries) == 9)
    for digest, name in entries:
        require('archive:' + name, hashlib.sha256((ARCHIVE/name.lstrip('*')).read_bytes()).hexdigest() == digest)
    data_path = ROOT/'results/generation-diagnostic-transport.json'
    data = json.loads(data_path.read_text(encoding='utf-8'))
    require('typed-transport', data['schema'] == 'marici.nima.generation-diagnostic-transport.v1')
    expected = {'checkers/collect_generation_diagnostics.py','checkers/collect_continuum_diagnostics.py'}
    expected |= {'quarantine/20261007-generation-evidence/checkers/' + name for name in RETIRED}
    require('complete-transport-provenance', set(data['source_sha256']) == expected)
    for path, digest in data['source_sha256'].items():
        require('source-current:' + path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest)
    require('old-receipts-untouched', data['historical_receipts_unchanged'])
    require('execution-defect-not-scientific-evidence', data['larger_script_execution_defect'] == {'type':'NameError','name':'json'})
    with redirect_stdout(io.StringIO()):
        tower = runpy.run_path(str(ROOT/'checkers/check_carrier_gram_tower.py'))
        source = runpy.run_path(str(ROOT/'checkers/check_carrier_probe_adapter.py'))
    edges, group = source['edges'], source['group']
    action = [tuple(edges.index((g[i],g[j])) for i,j in edges) for g in group]
    require('entire-existing-source', len(edges) == 12 and len(group) == 24
            and len({p[0] for p in action}) == 12)
    I, J = s.eye(12), s.ones(12)
    seeds = [tuple(int(i == j) for i in range(12)) for j in range(12)]
    Gsource = s.Matrix(12,12,lambda i,j:tower['inner'](seeds[i],seeds[j]))
    require('same-completed-source-Gram', Gsource == 10*I+J)
    Gtarget = s.Matrix(12,12,lambda i,j:source['dot'](source['fixed'][i], source['fixed'][j]))
    require('restricted-probe-rank-retained', Gtarget.rank() == 6)

    # A transitive invariant partition is determined by the block containing 0.
    # Exhaust every subset of admissible divisor size, not all Bell(12) partitions.
    candidates = 0
    partitions = []
    for size in (1,2,3,4,6,12):
        for rest in combinations(range(1,12),size-1):
            candidates += 1
            block = frozenset((0,)+rest)
            images = {frozenset(p[i] for i in block) for p in action}
            if all(image == block or image.isdisjoint(block) for image in images):
                partition = tuple(sorted(tuple(sorted(image)) for image in images))
                require('complete-block-orbit:' + str(size) + ':' + str(len(partitions)),
                        len(partition)*size == 12 and set().union(*map(set,partition)) == set(range(12)))
                partitions.append(partition)
    require('exhaustive-transitive-block-search', candidates == 695 and len(partitions) == 6)
    require('complete-shape-classification', sorted((len(p),len(p[0])) for p in partitions)
            == [(1,12),(3,4),(4,3),(4,3),(6,2),(12,1)])
    blocks = next(p for p in partitions if len(p) == 3)
    def endpoints(block):
        return {frozenset(edges[i]) for i in block}
    require('unique-four-arrow-matching-partition', sum(len(p[0]) == 4 for p in partitions) == 1
            and all(len(endpoints(b)) == 2 and set.union(*(set(e) for e in endpoints(b))) == set(range(4))
                    and all(edges.index((edges[i][1],edges[i][0])) in b for i in b) for b in blocks))
    outgoing = tuple(sorted(tuple(i for i,e in enumerate(edges) if e[0] == v) for v in range(4)))
    incoming = tuple(sorted(tuple(i for i,e in enumerate(edges) if e[1] == v) for v in range(4)))
    require('other-quotients-are-actual-star-maps', outgoing in partitions and incoming in partitions)
    block_actions = [tuple(blocks.index(tuple(sorted(p[i] for i in b))) for b in blocks) for p in action]
    require('matching-block-action-is-S3', len(set(block_actions)) == 6)
    require('only-four-source-elements-fix-all-blocks', sum(q == (0,1,2) for q in block_actions) == 4)
    # Explicitly label the old numerical block model by these actual arrows.
    tau = tuple(i for block in blocks for i in block)
    inverse_tau = {i:k for k,i in enumerate(tau)}
    rho = [tuple(inverse_tau[p[i]] for i in tau) for p in action]
    require('no-rho-factorization-through-blockwise-H', any(
        any(p[i]//4 != i//4 for i in range(12)) for p in rho))
    require('raw-partitions-not-physical-rivals', factorial(12)//(factorial(4)**3*factorial(3)) == 5775)

    # Enumerate the DECLARED H without changing probes into move counts.
    gram = [[0]*12 for _ in range(12)]
    moves = [[0]*12 for _ in range(12)]
    order = 0
    for triple in product(group,repeat=3):
        h = tuple(4*b+triple[b][i] for b in range(3) for i in range(4))
        fixed = [i for i in range(12) if h[i] == i]
        for i in fixed:
            for j in fixed:
                gram[i][j] += 1
        for i,j in enumerate(h):
            moves[i][j] += 1
        order += 1
    GH, moves = s.Matrix(gram), s.Matrix(moves)
    B = s.Matrix(12,12,lambda i,j:int(i//4 == j//4))
    require('whole-declared-H-enumerated', order == 24**3)
    require('exact-fixed-label-H-Gram', GH == 2304*I+288*B+864*J)
    require('distinct-point-transfer-counts', moves == 3456*B)
    Gold = integral_matrix('original-full-matrix', data['full_base_gram'])
    Mold = integral_matrix('original-cross-probe-matrix', data['subgroup_cross_probe_matrix'])
    require('original-full-matrix-preserved', Gold == 2304*I+576*B+576*J)
    require('neither-declared-counting-rule', Gold != GH and Gold != moves)
    require('old-count-residual-located', GH-Gold == 288*(J-B))
    require('base-metric-covariance-is-not-a-group-lift', all(
        Gold.extract(p,p) == Gold and GH.extract(p,p) == GH for p in rho))
    Euniform, Eblocks = J/12, B/4-J/12
    Ewithin = I-B/4
    for name,e,rank in [('uniform',Euniform,1),('between-blocks',Eblocks,2),('within-blocks',Ewithin,9)]:
        require('spectral-projector:' + name, e*e == e and s.trace(e) == rank)
    require('actual-old-full-spectrum', Gold == 11520*Euniform+4608*Eblocks+2304*Ewithin)
    require('correct-count-full-spectrum', GH == 13824*Euniform+3456*Eblocks+2304*Ewithin)
    rows, cols = data['up_indices'], data['doublet_indices']
    require('original-submatrix-is-reused', Gold.extract(rows,cols) == Mold)
    require('valid-supplied-old-submatrix', Mold == 576*s.eye(3)+576*s.ones(3))
    Mfixed = GH.extract(rows,cols)
    require('correct-fixed-probe-submatrix', Mfixed == 288*s.eye(3)+864*s.ones(3))
    require('not-the-completed-restricted-probe-Gram', GH.rank() == Gold.rank() == 12 and Gtarget.rank() == 6)

    for name in RETIRED:
        buffer = io.StringIO()
        code = None
        try:
            with redirect_stdout(buffer):
                runpy.run_path(str(ROOT/'checkers'/name),run_name='__main__')
        except SystemExit as exc:
            code = exc.code
        report = json.loads(buffer.getvalue())
        require('quarantine-refuses-verification:' + name,
                code == 2 and report['status'] == 'quarantined' and report['verification_performed'] is False)
    refused = False
    try:
        require('injected-wrong-subgroup-count', Gold == GH)
    except AssertionError:
        refused = True
    require('false-derivation-gate-refuses', refused)
    sources = [Path(__file__).resolve(), data_path, ARCHIVE/'SHA256SUMS',
               ROOT/'checkers/check_carrier_gram_tower.py', ROOT/'checkers/check_carrier_probe_adapter.py',
               ROOT/'checkers/biclique_complex.py', ROOT/'carrier-gram-restriction-tower.md',
               ROOT/'carrier-probe-adapter-and-state-reference.md']
    sources += [ROOT/'checkers'/name for name in RETIRED]
    sources += [ROOT/path for path in data['source_sha256']]
    result = {
        'schema':'marici.nima.twelve-arrow-generation-boundary.v1','status':'pass',
        'scientific_disposition':'canonical-matching-quotient-constructed; independent-H-not-derived; subgroup-count-defect; physical-generations-not-selected',
        'block_system_shapes': [{'blocks':len(p),'block_size':len(p[0])} for p in partitions],
        'four_arrow_blocks': [[list(edges[i]) for i in b] for b in blocks],
        'matching_block_permutation_image_order':6,'blockwise_kernel_order':4,'H_order':order,
        'fixed_label_counts':{'self':3456,'same_block_distinct':1152,'different_block':864},
        'point_transfer_counts':{'same_block':3456,'different_block':0},
        'old_counts':{'self':3456,'same_block_distinct':1152,'different_block':576},
        'old_full_spectrum':{'11520':1,'4608':2,'2304':9},
        'fixed_label_full_spectrum':{'13824':1,'3456':2,'2304':9},
        'old_cross_probe_spectrum':[576,576,2304],
        'fixed_label_cross_probe_spectrum':[288,288,2880],
        'scope':'Existing directed-arrow source and declared fixed-label/counting maps. Three matching blocks are not three SM generations. Relabelled partitions are not distinct physical predictions. No CKM, physical masses, unique matter representation or general generation no-go is inferred.',
        'checks':CHECKS,'check_count':len(CHECKS),
        'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):
                         hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','scientific_disposition','block_system_shapes','fixed_label_counts','check_count')},indent=2))


if __name__ == '__main__':
    main()

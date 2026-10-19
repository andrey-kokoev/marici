"""Rebuild the unchanged triangle constructor under indirect-edge deletion.

Keep vertices, seam input arrows and named mode reader fixed. Missing output
ports are unavailable, not zero. Surviving single-port responses are controls,
not substitutes for the unavailable joint seam experiment.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from assemble_triangle_arrow_source import assemble
from check_twelve_triangle_positive_geometry import (
    ONE, ZERO, OMEGA, mean, transpose, zmv, zmul, zadd, zconj, zscale, znorm)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = HERE.parent / 'inputs/proton-six-arrows.json'


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    files = [SOURCE, HERE/'assemble_triangle_arrow_source.py',
             HERE/'check_twelve_triangle_positive_geometry.py', HERE/'check_triangle_half_phase.py']
    hashes = {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    source = json.loads(SOURCE.read_text())
    baseline, manifest = assemble(source)
    def modes(report):
        points = {k:tuple(map(F,v)) for k,v in source['vertices'].items()}
        out = {}
        for row in report['triangles_and_transports']:
            center,a,b = row['triangle']
            points[center] = mean([points[k] for k in center.split('_')[1:]])
            out[''.join(row['outer_arrow'])] = zmv(
                transpose(tuple(points[k] for k in row['triangle'])),
                (ONE,OMEGA,zmul(OMEGA,OMEGA)))
        return out
    fixed_modes = modes(baseline)
    def read_response(rows, available, source_port, target_port):
        if source_port not in available or target_port not in available:
            return None
        # Same baseline vector injection in the aligned source block and same
        # normalized mode-amplitude reader in the raw target block.
        v, w = fixed_modes[source_port], fixed_modes[target_port]
        output = [ZERO]*3
        for row in rows:
            if row['source'][:2] == ['aligned',source_port] and row['target'][:2] == ['raw',target_port]:
                i,j = 'xyz'.index(row['target'][2]),'xyz'.index(row['source'][2])
                weight = (F(row['weight_real']),F(row['weight_imag_sqrt3']))
                output[i] = zadd(output[i],zmul(weight,v[j]))
        value = ZERO
        for a,b in zip(w,output):
            value = zadd(value,zmul(zconj(a),b))
        return zscale(value,1/sum(znorm(z) for z in w))
    for a in ('AB','BA'):
        for b in ('AB','BA'):
            check('baseline/seam-response/'+a+'/'+b,
                  read_response(manifest,fixed_modes,a,b) == (F(1,12),F(0)))
    indirect = ('BC','CA','AD','DB')
    results = []
    for mask in range(16):
        removed = {edge for i,edge in enumerate(indirect) if mask & (1<<i)}
        changed = {**source,'arrows':[e for e in source['arrows'] if ''.join(e) not in removed]}
        check(f'input/seam-survives/{mask}', all(list(edge) in changed['arrows'] for edge in ('AB','BA')))
        check(f'input/vertices-fixed/{mask}', changed['vertices'] == source['vertices'])
        try:
            report, rows = assemble(changed)
        except ValueError as error:
            check(f'rejection/no-complete-triangle/{mask}',
                  str(error) == 'Source has no complete oriented triangle; no reference frame is available'
                  and bool(removed & {'BC','CA'}) and bool(removed & {'AD','DB'}))
            results.append({'deleted':sorted(removed),'constructor_status':'rejected',
                            'reason':str(error),'joint_seam_response':None})
            continue
        available = modes(report)
        check(f'constructor/unchanged-surviving-local-modes/{mask}',
              all(available[a] == fixed_modes[a] for a in available))
        seam = [[read_response(rows,available,a,b) for a in ('AB','BA')] for b in ('AB','BA')]
        joint = seam if all(value is not None for row in seam for value in row) else None
        check(f'constructor/joint-reader-only-baseline/{mask}', (joint is not None) == (mask == 0))
        if mask:
            check(f'constructor/three-triangle-open-carrier/{mask}',
                  report['triangles'] == report['proper_rotations'] == 3 and not report['boundary_chain_zero'])
            check(f'constructor/135-transfers/{mask}', report['arrows_per_stage'] == [27,27,81])
            present = set(available) & {'AB','BA'}
            check(f'constructor/exactly-one-seam-port/{mask}', len(present) == 1)
            for a in present:
                check(f'control/fixed-local-reader-changes/{mask}/{a}',
                      read_response(rows,available,a,a) == (F(1,3),F(0)))
        results.append({'deleted':sorted(removed),'constructor_status':'assembled',
                        'derived_cycles':report['derived_cycles'], 'mode_ports':sorted(available),
                        'triangles':report['triangles'], 'transfers':report['unique_directed_arrows'],
                        'closed_boundary':report['boundary_chain_zero'],
                        'assembled_norm_squared':report['assembled_norm_squared'],
                        'joint_seam_response':joint,'partial_response_with_unavailable_entries':seam})
    check('census/7-assembled-9-rejected', sum(r['constructor_status']=='assembled' for r in results)==7
          and sum(r['constructor_status']=='rejected' for r in results)==9)
    check('inputs/unchanged', hashes == {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    def serial(value):
        if isinstance(value,F): return str(value)
        if isinstance(value,(tuple,list)): return [serial(x) for x in value]
        if isinstance(value,dict): return {k:serial(v) for k,v in value.items()}
        return value
    receipt = {'schema':'marici.nima.seed-deletion-constructor-response.v1','status':'pass',
               'checks':checks,'variants':results,'input_sha256':hashes,
               'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'scope':'Unchanged directed-triangle coefficient constructor, not the affine pair '
                       'constructor or exchange law. Fixed aligned-to-raw local-mode probe. '
                       'Null means unavailable, never a zero response. No preparation amplitudes, '
                       'new exchange kernel or physical coupling inferred.',
               'conclusion':'Deleting an indirect edge changes generated orbit and collective response, '
                            'but removes one surviving-input seam arrow from coefficient mode ports. '
                            'The fixed AB/BA joint experiment has no supplied rebuilt interface.'}
    out = HERE.parent/'results/seed-deletion-constructor-response.json'
    out.write_text(json.dumps(serial(receipt),indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact constructor-deletion checks')
    print('16 source variants: 7 assembled, 9 lack a complete triangle.')
    print('Every indirect-edge deletion destroys the two-port coefficient reader; missing is not zero.')
    print('Surviving unchanged local probe changes from 1/12 to 1/3 under reconstructed collective feedback.')


if __name__ == '__main__':
    main()

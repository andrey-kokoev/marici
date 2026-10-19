"""Cubic phase input adapter to the unchanged shared geometry/cycle machinery.

Phase pairs [a,b] mean a+i*sqrt(3)*b. The explicit lift is
(X,Y,Z)=(b,h*Re(u^3),a), restricted to real u^3 and order-three actions.
Not an arbitrary raw-arrow frontend. See docs/arrow-assembly.md.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble
from evolve_relative_geometry_modes import evolve


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-3*b*d, a*d+b*c


def cube(z):
    return mul(mul(z, z), z)


def pair(value):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError('Phase must be a rational pair [a,b]')
    return tuple(Q(x) for x in value)


def decode_source(source):
    if set(source) != {'schema', 'height_scale', 'phase_multiplier', 'seeds'} or source['schema'] != 'marici.cubic-phase-source.v1':
        raise ValueError('Expected cubic-phase-source.v1 fields only')
    h = Q(source['height_scale'])
    if h <= 0:
        raise ValueError('height_scale must be positive; zero changes the carrier dimension')
    r, s = pair(source['phase_multiplier'])
    if (r, s) == (1, 0) or cube((r, s)) != (1, 0):
        raise ValueError('Multiplier must have exact order three')
    if not isinstance(source['seeds'], list) or not source['seeds']:
        raise ValueError('At least one phase seed is required')
    seeds = []
    for seed in source['seeds']:
        if set(seed) != {'phase', 'role'}:
            raise ValueError('Seed requires phase and role only')
        a, b = pair(seed['phase'])
        c = cube((a, b))
        if c[1] != 0:
            raise ValueError('Seed cubic phase must be real')
        seeds.append({'point': list(map(str, (b, h*c[0], a))), 'role': seed['role']})
    # Multiplication by r+i sqrt(3)s in (X,Y,Z), with invariant Y.
    return {'metric': [[3,0,0],[0,1,0],[0,0,1]],
            'generators': [{'matrix': [[str(r), '0', str(s)], ['0','1','0'],
                                      [str(-3*s), '0', str(r)]], 'translation': [0,0,0]}],
            'seeds': seeds}


def run(source):
    decoded = decode_source(source)
    raw = assemble(decoded)
    cycle = evolve(decoded)
    h = Q(source['height_scale'])
    vertices = [tuple(map(Q,p)) for p in raw['vertices']]
    def encode(p):
        return {'phase': [str(p[2]), str(p[0])], 'height_moment': str(p[1]/h)}
    facets = []
    for ids in raw['supporting_facets']:
        centroid = tuple(sum(vertices[i][k] for i in ids)/len(ids) for k in range(3))
        facets.append({'vertices': ids, **encode(centroid)})
    return {'schema': 'marici.cubic-phase-assembly.v1', 'phase_source': source,
            'decoded_source': decoded, 'unselected_geometry': raw, 'cycle': cycle,
            'phase_cells': {'vertices': [encode(p) for p in vertices],
                            'center': encode(tuple(map(Q,raw['center']))),
                            'facet_centroids': facets,
                            'cone_cells': raw['cone_cells'],
                            'affine_rule': 'Interpolate phase and height_moment separately; Y=height_scale*height_moment.'},
            'scope': 'Explicit cubic lift adapter; supplied height scale retained. Shared assembler unchanged. No particle classifier.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    path = Path(args.source)
    result = run(json.loads(path.read_text(encoding='utf-8')))
    paths = [path.resolve(), Path(__file__).resolve(),
             ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',
             ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py']
    result['source_hashes'] = {p.as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    dest = Path(args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'counts': result['cycle']['geometry']['counts'],
                      'return_steps': result['cycle']['scheduled_atomic_steps_to_word_return']}, indent=2))


if __name__ == '__main__':
    main()

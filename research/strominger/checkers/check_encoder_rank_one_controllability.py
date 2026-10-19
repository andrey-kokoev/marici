"""Exact hypotheses for the connected rank-one phase controllability lemma.

The all-dimensional Lie argument is written in the companion note. This checker
certifies its induction hypotheses on all 39 source-derived conjugate controls,
not a symbolic 1521-dimensional Lie closure or an encoder compiler.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_witnessed_interface_compiler import ROOT, BASE, rat, blockdiag, enc


def main():
    paths = {
        'orbit': BASE/'results/encoder-conjugated-bank-controls.json',
        'source': BASE/'results/neutron-seam-control-transport.json',
        'memory': BASE/'results/neutron-comparison-memory.json',
    }
    raw = {key:p.read_bytes() for key,p in paths.items()}
    data = {key:json.loads(value) for key,value in raw.items()}
    orbit = data['orbit']
    assert orbit['status']=='pass' and orbit['orbit_span_dimension']==39
    for path,digest in orbit['source_hashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, path
    metric = blockdiag(rat(data['source']['metric']),rat(data['memory']['memory_metric']))
    B = rat(data['memory']['residual_incidence'])
    def dot(a,b):
        return sum((x*y for x,y in zip(a,b) if x and y),F(0))
    def mv(a,v):
        return [dot(row,v) for row in a]
    vectors = rat(orbit['directions'])
    tree = orbit['nonzero_overlap_spanning_tree']
    order = [0]
    parent = {}
    for edge in tree:
        p,c = edge['parent'],edge['child']
        assert p in order and c not in order
        assert dot(vectors[p],mv(metric,vectors[c])) == F(edge['metric_overlap']) != 0
        parent[c]=p
        order.append(c)
    assert sorted(order)==list(range(39))
    orthogonal = []
    duals = []
    norms = []
    steps = []
    for step,index in enumerate(order):
        v = vectors[index]
        remainder = v[:]
        total = dot(v,mv(metric,v))
        projection = F(0)
        coefficients = []
        for q,dual,norm in zip(orthogonal,duals,norms):
            coefficient = dot(v,dual)/norm
            coefficients.append(coefficient)
            projection += coefficient*coefficient*norm
            remainder = [x-coefficient*y for x,y in zip(remainder,q)]
        dual = mv(metric,remainder)
        residual = dot(remainder,dual)
        assert residual>0 and total==projection+residual
        assert all(dot(q,dual)==0 for q in orthogonal)
        if step:
            assert projection>0
            assert parent[index] in order[:step]
        else:
            assert projection==0
        steps.append({'step':step,'orbit_direction':index,
                      'old_span_projection_squared_norm':str(projection),
                      'new_orthogonal_squared_norm':str(residual),
                      'projection_coefficients':list(map(str,coefficients))})
        orthogonal.append(remainder)
        duals.append(dual)
        norms.append(residual)
    complement = rat(orbit['orthogonal_complement_basis'])
    assert len(complement)==6
    for v in complement:
        assert not any(v[24:]) and not any(mv(B,v[:24]))
        assert all(dot(q,mv(metric,v))==0 for q in orthogonal)
    # Hostile against the lemma's use of span alone: two orthogonal lines have
    # zero old-span projection, hence no mixing step. Duplicate lines instead
    # have zero new component. Both must be rejected by the induction criterion.
    def extension_admitted(projected,new):
        return projected>0 and new>0
    assert not extension_admitted(F(0),F(1))
    assert not extension_admitted(F(1),F(0))
    assert extension_admitted(F(1,2),F(1,2))
    hashes = {p.relative_to(ROOT).as_posix():hashlib.sha256(raw[k]).hexdigest() for k,p in paths.items()}
    own = Path(__file__).resolve()
    hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for path,digest in hashes.items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest
    report = {
        'status':'pass', 'active_complex_dimension':39,
        'induction_steps':steps, 'connected_independent_order':order,
        'polar_fixed_complement_dimension':6,
        'conditional_lie_algebra':'u(39), by the written rank-one induction lemma',
        'conditional_real_lie_dimension':39*39,
        'all_38_extensions_have_nonzero_old_and_new_components':True,
        'orthogonal_and_duplicate_line_hostiles_rejected':True,
        'source_hashes':hashes,
        'scope':'Exact rational verification of the written controllability lemma hypotheses. Assumes arbitrary bank phase parameter and finite conjugating software operations with inverses. Not a formal proof, numerical compiler, error certificate, or physical switching admission.',
    }
    (BASE/'results/encoder-rank-one-controllability.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','active_dimension':39,'nondegenerate_extensions':38,'polar_fixed_complement':6,'conditional_lie_dimension':1521}))


if __name__=='__main__':
    main()

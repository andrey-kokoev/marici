"""Test replacing explicit rim exclusions by one non-invariant-mode selector.

A facet is active iff its centroid is moved by at least one source isometry.
The score is sum_g ||g(centroid)-centroid||_G^2. No particle name or target facet
list enters selection. Complex coordinates explain the neutron's order-3 case.
This is a candidate geometric mode rule, not a derived physical coupling law.
"""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

from assemble_relative_geometry import assemble, dot_metric, subtract, apply
from check_relative_geometry_sources import match_target
from check_common_assembly_symmetry import BASE, load_targets


def select(source):
    source = deepcopy(source)
    # Remove the old explicit rim exclusions before any geometry is generated.
    for seed in source['seeds']:
        if seed['role'] == 'external_interface':
            seed['role'] = 'carrier'
    full = assemble(source)
    points = [tuple(map(Q, p)) for p in full['vertices']]
    G = [[Q(x) for x in row] for row in source['metric']]
    generators = [(tuple(tuple(Q(x) for x in row) for row in g['matrix']),
                   tuple(Q(x) for x in g['translation'])) for g in source['generators']]
    center = tuple(map(Q, full['center']))
    assert all(apply(g, center) == center for g in generators)
    scores = {}
    for facet in full['carrier_facets']:
        centroid = tuple(sum(points[i][k] for i in facet)/len(facet) for k in range(len(G)))
        displacements = [subtract(apply(g, centroid), centroid) for g in generators]
        score = sum(dot_metric(v, v, G) for v in displacements)
        assert score >= 0
        scores[tuple(sorted(facet))] = score
    kept = [f for f in full['carrier_facets'] if scores[tuple(sorted(f))] > 0]
    removed = [list(f) for f, score in sorted(scores.items()) if score == 0]
    output = deepcopy(full)
    output['carrier_facets'] = kept
    output['external_interfaces'] = removed
    output['cone_cells'] = [[full['center_vertex_id']]+f for f in kept]
    output['positive_cone_determinants_in_source_coordinates'] = [v for f, v in zip(
        full['carrier_facets'], full['positive_cone_determinants_in_source_coordinates'])
        if scores[tuple(sorted(f))] > 0]
    output['counts'].update(external_interfaces=len(removed), carrier_facets=len(kept), cone_cells=len(kept))
    output['mode_scores'] = [{'facet': list(f), 'score': str(v)} for f, v in sorted(scores.items())]
    output['selection_rule'] = 'retain facets whose centroid has a nonzero component outside the common fixed affine subspace'
    return output, source


def change_frame(source, scales, translation):
    out = deepcopy(source)
    d = len(scales)
    out['metric'] = [[str(Q(source['metric'][i][j])/(scales[i]*scales[j])) for j in range(d)] for i in range(d)]
    for old, new in zip(source['generators'], out['generators']):
        A = [[Q(old['matrix'][i][j])*scales[i]/scales[j] for j in range(d)] for i in range(d)]
        b = [Q(old['translation'][i])*scales[i]+translation[i]-sum(A[i][j]*translation[j] for j in range(d))
             for i in range(d)]
        new['matrix'] = [[str(x) for x in row] for row in A]
        new['translation'] = list(map(str, b))
    for old, new in zip(source['seeds'], out['seeds']):
        new['point'] = [str(Q(old['point'][i])*scales[i]+translation[i]) for i in range(d)]
    return out


def complex_multiply(a, b):
    # Exact a0 + i*sqrt(3)*a1 arithmetic.
    return a[0]*b[0]-3*a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def neutron_complex_check(source, output):
    g = source['generators'][0]
    generator = ([[Q(x) for x in row] for row in g['matrix']], tuple(map(Q, g['translation'])))
    points = [tuple(map(Q, p)) for p in output['vertices']]
    omega_bar = (Q(-1, 2), Q(-1, 2))
    def u(p):
        return p[2], p[0]
    cubes = []
    for p in points:
        q = apply(generator, p)
        assert u(q) == complex_multiply(omega_bar, u(p))
        cube = complex_multiply(complex_multiply(u(p), u(p)), u(p))
        assert cube == ((Q(1) if p[1] > 0 else Q(-1)), Q(0))
        cubes.append(list(map(str, cube)))
    projected_cap_areas = []
    for row in output['mode_scores']:
        facet = row['facet']
        centroid = tuple(sum(points[i][k] for i in facet)/len(facet) for k in range(3))
        z = u(centroid)
        assert Q(row['score']) == 3*(z[0]**2+3*z[1]**2)
        # Orbit average projects onto the fixed axis; its complement is the
        # real two-dimensional carrier of the conjugate complex modes.
        p1 = apply(generator, centroid)
        p2 = apply(generator, p1)
        average = tuple((a+b+c)/3 for a, b, c in zip(centroid, p1, p2))
        assert average == (Q(0), centroid[1], Q(0))
        if Q(row['score']) == 0:
            # Crucial negative control: projection does NOT erase the cap.
            # Only its centroid mode vanishes; all three vertices survive.
            zs = [u(points[i]) for i in facet]
            norm = lambda z: z[0]**2+3*z[1]**2
            assert all(norm(z) == 1 for z in zs)
            ab, ac, bc = norm(subtract(zs[1], zs[0])), norm(subtract(zs[2], zs[0])), norm(subtract(zs[2], zs[1]))
            area_gram = ab*ac-((ab+ac-bc)/2)**2
            assert area_gram == Q(27, 4)
            projected_cap_areas.append(str(area_gram))
    return {'complex_coordinate': 'u=Z+i*sqrt(3)*X', 'rotation': 'u -> conjugate(omega)*u',
            'upper_rim_equation': 'u^3=1', 'lower_rim_equation': 'u^3=-1',
            'fixed_mode_projector': '(I+R+R^2)/3 = diag(0,1,0)',
            'nontrivial_real_mode_projector': 'diag(1,0,1)',
            'cap_centroid_complex_amplitude': '0', 'side_centroid_complex_norm_squared': '4/9',
            'zero_score_facets': sum(Q(row['score']) == 0 for row in output['mode_scores']),
            'projected_cap_area_gram_determinants': projected_cap_areas,
            'negative_control': 'Caps remain nondegenerate under complex-plane projection. Their removal requires the explicit facet-centroid mode selection, not a coordinate change alone.'}


def main():
    targets, evidence = load_targets()
    results, generated = {}, {}
    for name, target_name in [('proton', 'proton'), ('neutron', 'neutron_belt'), ('electron', 'electron_pentachoron')]:
        path = BASE/'inputs'/f'relative-{name}.json'
        raw = path.read_bytes()
        source = json.loads(raw)
        output, unprotected_source = select(source)
        assert all(seed['role'] != 'external_interface' for seed in unprotected_source['seeds'])
        comparison = match_target(output, targets[target_name])
        assert comparison is not None
        d = len(source['metric'])
        transformed = change_frame(unprotected_source, [Q(i+2) for i in range(d)], [Q(i-2, 3) for i in range(d)])
        moved, _ = select(transformed)
        assert moved['mode_scores'] == output['mode_scores']
        assert match_target(moved, targets[target_name]) is not None
        output['source_sha256'] = hashlib.sha256(raw).hexdigest()
        output['explicit_external_roles_removed'] = True
        (BASE/'results'/f'mode-selected-{name}.json').write_text(json.dumps(output, indent=2)+'\n')
        results[name] = {'counts': output['counts'], 'mode_scores': output['mode_scores'],
                         'exact_marked_target_match': comparison,
                         'affine_frame_covariance_checked': True, 'source_sha256': output['source_sha256']}
        generated[name] = (unprotected_source, output)
    neutron = neutron_complex_check(*generated['neutron'])
    assert neutron['zero_score_facets'] == 2
    report = {'status': 'passed', 'rule': 'facet-centroid non-invariant-mode support',
              'explicit_neutron_rim_protection_used': False,
              'results': results, 'neutron_complex_interpretation': neutron,
              'target_sha256': evidence,
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_relative_geometry_mode_selection.py', 'assemble_relative_geometry.py',
                               'check_relative_geometry_sources.py', 'check_common_assembly_symmetry.py')},
              'scope': 'A new centroid-mode admission hypothesis reproduces all three supplied geometric targets without explicit neutron exclusions. It is not mere complex reparameterization, a derived dynamical law, or a coefficient-arrow count.'}
    (BASE/'results/relative_geometry_mode_selection.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

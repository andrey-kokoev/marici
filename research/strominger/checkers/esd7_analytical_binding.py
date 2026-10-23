"""Explicit cube-index to generated tetrahedron bridge; no inferred fillers.
The sorting bridge is a new finite construction, not an assumed registry ID map.
"""
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction

ROLES = ('H123', 'H124', 'H134', 'H234')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def folded_simplex(index):
    """Sort each vertex of the fixed-axis unit-cube staircase independently."""
    point = list(index)
    vertices = [tuple(sorted(point))]
    for axis in range(3):
        point[axis] += 1
        vertices.append(tuple(sorted(point)))
    return tuple(vertices)


def bind(assembly, registry):
    scale = assembly['scale']
    require(scale == 7, 'source prototype registry is specifically esd7')
    require(registry['passed'] and registry['tetrahedron_count'] == 343, 'source registry failed')
    vertices = {v['id']: tuple(v['cumulative']) for v in assembly['vertices']}
    tetrahedra = {tuple(vertices[v] for v in t['vertices']): t for t in assembly['tetrahedra']}
    require(len(tetrahedra) == 343, 'generated tetrahedron identity collision')
    faces = {f['id']: f for f in assembly['triangles']}
    edges = {e['id']: e for e in assembly['edges']}
    parent = registry['parent_face_prototypes']
    require(set(parent) == set(ROLES), 'source face roles')
    assignments = []; contexts = defaultdict(list); seen = set(); covered = set()
    for row in registry['cells']:
        index = row['index']
        require(len(index) == 3 and all(type(x) is int and 0 <= x < scale for x in index), 'invalid source cube index')
        index = tuple(index)
        require(index not in seen, 'duplicate registry index'); seen.add(index)
        require(row['id'] == 'esd7:'+','.join(map(str,index)), 'registry ID/index mismatch')
        require(row['face_prototypes'] == parent, 'unbound face prototype variant')
        require(row['analytical_form'] == registry['parent_tetrahedron_prototype'], 'unbound tetrahedron prototype variant')
        key = folded_simplex(index)
        require(key in tetrahedra, 'sorting bridge misses generated tetrahedron')
        t = tetrahedra[key]
        require(t['id'] not in covered, 'sorting bridge is not injective'); covered.add(t['id'])
        # Folding changes orientation. Retain the actual sign; never identify
        # all cube staircases with positively oriented geometric tetrahedra.
        assignment = {'registryId':row['id'], 'index':list(index), 'tetrahedron':t['id'],
                      'foldedVertices':[list(v) for v in key], 'orientation':t['orientation'],
                      'analyticalPrototype':row['analytical_form'], 'faceRoles':dict(zip(ROLES,t['faces'])),
                      'sourceHigherCoherenceClaim':row['higher_coherence'],
                      'H234DecayWitness':row['H234_decay_witness'], 'fillerInstalled':False}
        witness = row['H234_decay_witness']; exponent = Fraction(witness['minimum_cutoff_exponent'])
        require(exponent > 0, 'positive cutoff exponent required')
        require(all(Fraction(order)*exponent >= int(target) for target,order in witness['source_orders_for_target_orders'].items()),
                'decay budget insufficient')
        assignments.append(assignment)
        for role, fid in assignment['faceRoles'].items():
            require(fid in faces, 'unresolved face')
            contexts[fid].append({'tetrahedron':t['id'], 'registryId':row['id'], 'role':role, 'prototype':parent[role]})
    require(seen == set(product(range(scale), repeat=3)), 'missing source registry index')
    require(covered == {t['id'] for t in assembly['tetrahedra']}, 'incomplete geometric coverage')
    interfaces = []; pairs = Counter()
    for fid, face in sorted(faces.items()):
        local = sorted(contexts[fid], key=lambda x:x['tetrahedron'])
        require(len(local) == face['incidence'], 'missing local face context')
        obligation = face['homotopyObligation']
        route = [edges[e]['vertices'] for e in obligation['composite']]
        direct = edges[obligation['direct']]['vertices']
        require(route == [face['vertices'][:2],face['vertices'][1:]] and direct == [face['vertices'][0],face['vertices'][2]],
                'face homotopy endpoint mismatch')
        roles = sorted(c['role'] for c in local)
        if len(local) == 2:
            pairs['/'.join(roles)] += 1
        interfaces.append({'face':fid, 'vertices':face['vertices'], 'localContexts':local,
                           'sharedEdgeRoute':obligation['composite'], 'directEdge':obligation['direct'],
                           'comparisonRequired':len(local)==2, 'distinctLocalRoles':len(set(roles))>1,
                           'comparisonDischarged':False, 'homotopyInstalled':False})
    return {'assignments':sorted(assignments,key=lambda a:a['tetrahedron']), 'faceBindings':interfaces,
            'sharedRolePairs':dict(sorted(pairs.items())), 'registryBridgeEstablished':True,
            'bridgeOrigin':'new finite sorting construction; not a pre-existing registry identification',
            'sourceHigherCoherenceClaimsImportedAsProof':False,
            'analyticalCoherenceDischarged':False, 'globalFieldTransportEstablished':False,
            'full114ChannelEstablished':False}

"""Validate catalogue structure, references and isotope bookkeeping.

Dependency-free validator for the explicitly supported JSON Schema subset used
by the adjacent schema. Unsupported keywords fail closed. This is not a general
JSON Schema implementation and does not verify scientific claims or web sources.
"""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import re
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMA = json.loads((HERE / 'element-isotope-catalog.schema.json').read_text(encoding='utf-8'))
KEYWORDS = {'$schema', '$defs', '$ref', 'title', 'type', 'additionalProperties',
            'required', 'properties', 'const', 'enum', 'minItems', 'items',
            'uniqueItems', 'minimum', 'minLength', 'pattern'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_schema(schema):
    require(not set(schema) - KEYWORDS, f'Unsupported schema keywords: {set(schema)-KEYWORDS}')
    if 'type' in schema:
        require(schema['type'] in {'object', 'array', 'string', 'integer'}, 'Unsupported schema type')
    if 'additionalProperties' in schema:
        require(schema['additionalProperties'] is False, 'Only closed object schemas supported')
    if '$ref' in schema:
        ref = schema['$ref']
        require(ref.startswith('#/$defs/') and ref[8:] in SCHEMA['$defs'], f'Invalid local schema reference {ref}')
    if 'pattern' in schema:
        re.compile(schema['pattern'])
    for key in ('properties', '$defs'):
        for child in schema.get(key, {}).values():
            check_schema(child)
    if 'items' in schema:
        check_schema(schema['items'])


def structure(value, schema, path='$'):
    if '$ref' in schema:
        structure(value, SCHEMA['$defs'][schema['$ref'][8:]], path)
    kind = schema.get('type')
    if kind:
        valid = {'object': isinstance(value, dict), 'array': isinstance(value, list),
                 'string': isinstance(value, str), 'integer': type(value) is int}[kind]
        require(valid, f'{path}: expected {kind}')
    if 'const' in schema:
        require(value == schema['const'], f'{path}: wrong constant')
    if 'enum' in schema:
        require(value in schema['enum'], f'{path}: invalid enum value {value!r}')
    if kind == 'object':
        require(set(schema.get('required', [])) <= value.keys(), f'{path}: missing required fields')
        properties = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            require(value.keys() <= properties.keys(), f'{path}: unknown fields')
        for key, child in value.items():
            if key in properties:
                structure(child, properties[key], f'{path}.{key}')
    if kind == 'array':
        require(len(value) >= schema.get('minItems', 0), f'{path}: too few entries')
        if schema.get('uniqueItems'):
            require(len({json.dumps(x, sort_keys=True) for x in value}) == len(value), f'{path}: duplicate entries')
        for i, child in enumerate(value):
            structure(child, schema['items'], f'{path}[{i}]')
    if kind == 'string':
        require(len(value) >= schema.get('minLength', 0), f'{path}: empty text')
        if 'pattern' in schema:
            require(re.search(schema['pattern'], value) is not None, f'{path}: invalid text pattern')
    if kind == 'integer' and 'minimum' in schema:
        require(value >= schema['minimum'], f'{path}: below minimum')


def unique(rows, key):
    values = [row[key] for row in rows]
    require(len(values) == len(set(values)), f'Duplicate {key}')
    return set(values)


def validate(data):
    check_schema(SCHEMA)
    structure(data, SCHEMA)
    sources = unique(data['sources'], 'id')
    constituents = unique(data['constituents'], 'id')
    mechanisms = unique(data['mechanisms'], 'id')
    external = {s['id'] for s in data['sources'] if s['kind'] == 'external'}
    for source in data['sources']:
        location = source['location']
        if source['kind'] == 'repository':
            relative = Path(location)
            require(not relative.is_absolute() and '\\' not in location, 'Use repository-relative forward-slash paths')
            resolved = (ROOT / relative).resolve()
            require(resolved.is_relative_to(ROOT) and resolved.is_file(), f'Missing or escaping source: {location}')
        else:
            url = urlparse(location)
            require(url.scheme == 'https' and bool(url.netloc), f'Invalid source URL: {location}')

    def references(obj):
        if isinstance(obj, dict):
            for key, child in obj.items():
                if key == 'source_ids':
                    require(set(child) <= sources, f'Unresolved source IDs: {set(child)-sources}')
                if key == 'constituent_ids':
                    require(set(child) <= constituents, 'Unresolved constituent IDs')
                if key == 'mechanism_ids':
                    require(set(child) <= mechanisms, 'Unresolved mechanism IDs')
                references(child)
        elif isinstance(obj, list):
            for child in obj:
                references(child)
    references(data)
    unique(data['elements'], 'atomic_number')
    unique(data['elements'], 'symbol')
    isotopes = []
    for element in data['elements']:
        unique(element['isotopes'], 'mass_number')
        for isotope in element['isotopes']:
            isotopes.append(isotope)
            observation = isotope['observations']
            require(isotope['id'] == f"{element['symbol']}-{isotope['mass_number']}", 'Isotope ID mismatch')
            require(observation['protons'] == element['atomic_number'], 'Proton count mismatch')
            require(observation['protons'] + observation['neutrons'] == isotope['mass_number'], 'Mass-number mismatch')
            require(observation['neutral_atom_electrons'] == element['atomic_number'], 'Neutral electron count mismatch')
            require(bool(external.intersection(observation['source_ids'])), 'Observations need an external reference')
    unique(isotopes, 'id')
    return {'verification_passed': True, 'elements': len(data['elements']),
            'isotopes': len(isotopes), 'constituents': len(constituents), 'mechanisms': len(mechanisms),
            'scope': 'Schema subset, references and bookkeeping only; no physical claims or remote sources verified.'}


def self_test(data):
    mutations = [
        lambda d: d['constituents'][0].update(mechanism_ids=['missing']),
        lambda d: d['mechanisms'].append(deepcopy(d['mechanisms'][0])),
        lambda d: d['elements'][0]['isotopes'][0]['model'].pop('mass_readout'),
        lambda d: d.pop('coverage'),
        lambda d: d.update(unexpected=True),
        lambda d: d['elements'][0].update(atomic_number=True),
        lambda d: d['elements'][0]['isotopes'][0]['observations'].update(stability='proved_stable'),
        lambda d: d['elements'][0]['isotopes'][0]['observations'].update(neutrons=9),
        lambda d: d['elements'][0]['isotopes'][0]['model']['geometry'].update(status='proven_particle'),
        lambda d: d['elements'][0]['isotopes'][0]['model'].update(constituent_ids=['missing']),
        lambda d: d['elements'][0]['isotopes'][0]['observations'].update(source_ids=['missing']),
        lambda d: d['sources'].append(deepcopy(d['sources'][0])),
        lambda d: d['sources'][2].update(location='../outside.md'),
        lambda d: d['elements'][0]['isotopes'].append(deepcopy(d['elements'][0]['isotopes'][0]))
    ]
    for mutation in mutations:
        changed = deepcopy(data)
        mutation(changed)
        try:
            validate(changed)
        except ValueError:
            continue
        raise ValueError('Invalid catalogue mutation was accepted')
    return len(mutations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('catalogue', nargs='?', type=Path, default=HERE / 'element-isotope-catalog.json')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    catalogue = json.loads(args.catalogue.read_text(encoding='utf-8'))
    result = validate(catalogue)
    if args.self_test:
        result['rejected_invalid_mutations'] = self_test(catalogue)
    print(json.dumps(result, indent=2))

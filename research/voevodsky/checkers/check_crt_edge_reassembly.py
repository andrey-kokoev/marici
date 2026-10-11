"""Typed edge decomposition, witness-preserving reassembly, and bounded CRT minimization.
Standard library only. Constructor grammar: lift3, lift5, scale(k), add,
reduce3, reduce5, pair. Inputs are free ports; every non-input operation costs 1.
"""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

@dataclass(frozen=True)
class Term:
    op: str
    args: tuple = ()
    parameter: object = None

def node(op, *args, parameter=None):
    return Term(op, args, parameter)

a, b, x = [node('input', parameter=name) for name in ('a', 'b', 'x')]
INPUT_TYPES = {'a': 'Z3', 'b': 'Z5', 'x': 'Z15'}

def forward(a, b):
    # Intentionally expanded expression, mathematically the same CRT assembly.
    u = node('scale', node('lift3', a), parameter=5)
    v = node('scale', node('lift5', b), parameter=3)
    return node('add', node('add', u, u), node('add', v, v))

def inverse(x):
    return node('pair', node('reduce3', x), node('reduce5', x))

source = {
    'assembled': forward(a, b),
    'decomposed': inverse(x),
    'pair_round_trip': inverse(forward(a, b)),
    'residue_round_trip': forward(node('reduce3', x), node('reduce5', x)),
}
WITNESSES = [
    {'id': 'residue3', 'root': 'assembled', 'relation': 'output mod 3 = input a'},
    {'id': 'residue5', 'root': 'assembled', 'relation': 'output mod 5 = input b'},
    {'id': 'pair_round_trip', 'root': 'pair_round_trip', 'relation': 'output = (input a,input b)'},
    {'id': 'residue_round_trip', 'root': 'residue_round_trip', 'relation': 'output = input x'},
]

def infer(op, types, parameter):
    unary = {'lift3': ('Z3', 'Z15'), 'lift5': ('Z5', 'Z15'),
             'reduce3': ('Z15', 'Z3'), 'reduce5': ('Z15', 'Z5')}
    if op in unary:
        expected, result = unary[op]
        if types != [expected]: raise ValueError('typed port mismatch')
        return result
    if op == 'scale':
        if types != ['Z15'] or not isinstance(parameter, int): raise ValueError('typed scalar mismatch')
        return 'Z15'
    if op == 'add':
        if types != ['Z15', 'Z15']: raise ValueError('typed addition mismatch')
        return 'Z15'
    if op == 'pair':
        if types != ['Z3', 'Z5']: raise ValueError('typed pair mismatch')
        return 'Z3xZ5'
    raise ValueError('unknown constructor')

def compile_graph(roots, share=False):
    edges, types, cache = [], dict(INPUT_TYPES), {}
    def visit(t):
        if t.op == 'input': return t.parameter
        if share and t in cache: return cache[t]
        inputs = [visit(arg) for arg in t.args]
        result_type = infer(t.op, [types[i] for i in inputs], t.parameter)
        result = f'n{len(edges)}'
        edges.append({'output': result, 'op': t.op, 'inputs': inputs,
                      'parameter': t.parameter, 'type': result_type})
        types[result] = result_type
        cache[t] = result
        return result
    outputs = {name: visit(t) for name, t in roots.items()}
    return {'ports': INPUT_TYPES, 'edges': edges, 'roots': outputs, 'witnesses': WITNESSES}

def decode_graph(graph):
    # Arity, ordered ports and witness attachments are part of decomposition.
    if graph['ports'] != INPUT_TYPES or graph['witnesses'] != WITNESSES:
        raise ValueError('boundary or witness loss')
    terms = {name: node('input', parameter=name) for name in INPUT_TYPES}
    types = dict(INPUT_TYPES)
    for edge in graph['edges']:
        if edge['output'] in terms: raise ValueError('duplicate producer')
        if any(i not in terms for i in edge['inputs']): raise ValueError('unbound input')
        typ = infer(edge['op'], [types[i] for i in edge['inputs']], edge['parameter'])
        if typ != edge['type']: raise ValueError('output type mismatch')
        terms[edge['output']] = node(edge['op'], *(terms[i] for i in edge['inputs']), parameter=edge['parameter'])
        types[edge['output']] = typ
    return {name: terms[ref] for name, ref in graph['roots'].items()}

def normalized(t):
    if t.op == 'input': return t
    args = tuple(normalized(arg) for arg in t.args)
    if t.op in ('scale', 'add'):
        # Coefficient collection in Z15. Nonlinear/non-ring operations are atoms.
        def collect(term, factor, out):
            if term.op == 'add':
                for arg in term.args: collect(arg, factor, out)
            elif term.op == 'scale': collect(term.args[0], factor * term.parameter, out)
            else: out[term] = (out.get(term, 0) + factor) % 15
        coefficients = {}
        collect(Term(t.op, args, t.parameter), 1, coefficients)
        summands = [atom if coefficient == 1 else node('scale', atom, parameter=coefficient)
                    for atom, coefficient in sorted(coefficients.items(), key=lambda item: repr(item[0])) if coefficient]
        if not summands: raise ValueError('zero constructor absent from this fixture grammar')
        result = summands[0]
        for summand in summands[1:]: result = node('add', result, summand)
        return result
    return Term(t.op, args, t.parameter)

def evaluate(graph, env):
    values = dict(env)
    for e in graph['edges']:
        args = [values[i] for i in e['inputs']]
        op = e['op']
        if op.startswith('lift'): value = args[0]  # canonical residue representative
        elif op == 'scale': value = e['parameter'] * args[0] % 15
        elif op == 'add': value = sum(args) % 15
        elif op == 'reduce3': value = args[0] % 3
        elif op == 'reduce5': value = args[0] % 5
        elif op == 'pair': value = tuple(args)
        else: raise ValueError(op)
        values[e['output']] = value
    return {name: values[ref] for name, ref in graph['roots'].items()}

def witness_holds(values, env):
    return (values['assembled'] % 3 == env['a']
            and values['assembled'] % 5 == env['b']
            and values['pair_round_trip'] == (env['a'], env['b'])
            and values['residue_round_trip'] == env['x'])

expanded = compile_graph(source)
rebuilt = decode_graph(expanded)
shared = compile_graph(rebuilt, share=True)
normal_terms = {name: normalized(t) for name, t in rebuilt.items()}
reduced = compile_graph(normal_terms, share=True)
checks = {'lossless_edge_reassembly': rebuilt == source,
          'witness_constraints_retained': expanded['witnesses'] == shared['witnesses'] == reduced['witnesses'] == WITNESSES}
rows = []
for aa, bb, xx in product(range(3), range(5), range(15)):
    env = dict(a=aa, b=bb, x=xx)
    vals = [evaluate(g, env) for g in (expanded, shared, reduced)]
    rows.append(vals[0] == vals[1] == vals[2] and all(witness_holds(value, env) for value in vals))
checks['all_225_environments_preserve_all_roots_and_witnesses'] = all(rows)

# Independent minimization of the forward map in a frozen affine grammar.
# The map has unique coefficients, since the input domain includes (1,0),(0,1).
solutions = [(c, d) for c, d in product(range(15), repeat=2)
             if all(((c * aa + d * bb) % 15) % 3 == aa
                    and ((c * aa + d * bb) % 15) % 5 == bb
                    for aa, bb in product(range(3), range(5)))]
checks['unique_affine_coefficients'] = solutions == [(10, 6)]
# Both typed lifts are necessary. With only two more nodes, an expression
# depending on both inputs has coefficients (k,1), (1,k), or (k,k).
# These include two-addition cases (2,1), (1,2), (2,2).
at_most_four = {(k, 1) for k in range(15)} | {(1, k) for k in range(15)} | {(k, k) for k in range(15)}
checks['no_four_node_forward_in_affine_grammar'] = (10, 6) not in at_most_four
forward_normal = compile_graph({'assembled': normal_terms['assembled']}, share=True)
checks['five_node_forward_attained'] = len(forward_normal['edges']) == 5

# Hostiles preserve clear distinctions: ill-typed edges, lost witnesses, wrong coefficients.
def copied(g): return json.loads(json.dumps(g))
bad_witness = copied(expanded)
bad_witness['witnesses'].pop()
try:
    decode_graph(bad_witness)
    checks['witness_deletion_rejected'] = False
except ValueError:
    checks['witness_deletion_rejected'] = True
bad_type = copied(expanded)
next(e for e in bad_type['edges'] if e['op'] == 'lift3')['inputs'] = ['b']
try:
    decode_graph(bad_type)
    checks['endpoint_type_substitution_rejected'] = False
except ValueError:
    checks['endpoint_type_substitution_rejected'] = True
bad_coefficient = copied(reduced)
for edge in bad_coefficient['edges']:
    if edge['op'] == 'scale' and edge['parameter'] == 6:
        edge['parameter'] = 5
# A well-typed mutation, caught by correctness rather than by typing.
decode_graph(bad_coefficient)
bad_example = evaluate(bad_coefficient, dict(a=2, b=3, x=8))
checks['well_typed_bad_coefficient_rejected'] = not witness_holds(bad_example, dict(a=2, b=3, x=8))

result = {
    'schema': 'marici.voevodsky.crt-edge-reassembly.v1',
    'passed': all(checks.values()), 'checks': checks,
    'cost': 'One node per non-input constructor; four witness predicates counted separately and never deleted.',
    'whole_derivation_nodes': {name: len(g['edges']) for name, g in [('expanded', expanded), ('shared', shared), ('normalized', reduced)]},
    'forward_nodes': {name: len(compile_graph({'assembled': terms['assembled']}, share=share)['edges'])
                      for name, terms, share in [('expanded', source, False), ('shared', rebuilt, True), ('normalized', normal_terms, True)]},
    'witness_count': len(WITNESSES), 'exhaustive_environments': len(rows),
    'affine_coefficient_solutions': solutions,
    'minimality_scope': 'Forward map only, using canonical typed lifts, Z15 scalar multiplication and addition. No CRT primitive, lookup table, branching or alternate encoding. No minimum claimed for the entire four-root graph.',
    'graphs': {'expanded': expanded, 'shared': shared, 'normalized': reduced},
    'negative_example': bad_example,
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'geometric_scope': 'Typed constructor hyperedges with retained witnesses, not a proof that bare geometric edges reconstruct tetrahedral fillers or a 2-Segal identification.',
}
out = Path(__file__).resolve().parents[1] / 'results' / 'crt_edge_reassembly.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k != 'graphs'}, indent=2))
if not result['passed']: raise SystemExit(1)

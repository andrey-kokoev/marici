"""Bounded Layer 4 active-view prototype; stdlib only, no arbitrary code rules.

The Agda model is checked separately. This Python/JSON implementation is tested,
not extracted from Agda. Rule names and hashes alone never validate cache values.
"""
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
from agda_receipt_audit import OWNER, verify_receipt

SCHEMA = 'marici.active-view.v1'
PLAN = 'marici.active-view-plan.v1'
RULES = {'output': 'bool-output-replay-v1', 'trace': 'bool-trace-replay-v1'}
MAX_STEPS, MAX_REQUESTS, MAX_VIEWS, MAX_TOTAL_STEPS = 4096, 128, 256, 65536
MAX_BYTES = 8 * 1024 * 1024


class Invalid(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise Invalid(message)


def wire(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(wire(value)).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keys(value, expected):
    need(type(value) is dict and set(value) == set(expected), 'unexpected or missing fields')


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, 'integer outside policy bounds')


def request_valid(r):
    keys(r, ('history', 'input'))
    need(type(r['input']) is bool, 'input must be Boolean')
    h = r['history']
    need(type(h) is list and len(h) <= MAX_STEPS, 'history exceeds policy bound')
    need(all(type(a) is str and a in ('stay', 'turn') for a in h), 'unknown instruction')


def replay(r):
    value = r['input']
    states = [value]
    for action in r['history']:
        if action == 'turn':
            value = not value
        states.append(value)
    return {'output': value, 'trace': states}


def cache(field, value):
    return {'rule': RULES[field], 'value': value}


def load(path):
    def unique(pairs):
        result = {}
        for k, v in pairs:
            need(k not in result, 'duplicate JSON key')
            result[k] = v
        return result
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_BYTES + 1)
    need(len(raw) <= MAX_BYTES, 'input exceeds byte bound')
    return json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique,
                      parse_constant=lambda x: (_ for _ in ()).throw(Invalid('nonfinite JSON number')))


class Engine:
    def __init__(self):
        # Existing receipt verifier uses assertions: never permit -O to disable it.
        need(__debug__, 'optimized Python is not admitted for receipt verification')
        checked = verify_receipt('ActiveViewMachine', 'active-view-machine',
                                 ['ActiveViewBadTrace', 'ActiveViewBadHistory'])
        self.receipt = OWNER / 'results/active-view-machine-formal-audit.json'
        paths = [self.receipt, Path(__file__).resolve()]
        paths += [OWNER / 'agda' / p for p in checked['local_sources_checked']]
        self.pins = {p: file_digest(p) for p in paths}
        self.binding = digest({'formal_receipt': checked['source_bound_receipt_sha256'],
                               'runtime': self.pins[Path(__file__).resolve()]})

    def guard(self):
        need(all(file_digest(p) == h for p, h in self.pins.items()), 'policy sources changed; reopen engine')

    def validate(self, doc):
        self.guard()
        keys(doc, ('schema', 'binding', 'requests', 'views'))
        need(doc['schema'] == SCHEMA and doc['binding'] == self.binding, 'unknown or stale artifact policy')
        rs, vs = doc['requests'], doc['views']
        need(type(rs) is dict and len(rs) <= MAX_REQUESTS, 'dependency store bound')
        need(type(vs) is list and len(vs) <= MAX_VIEWS, 'view count bound')
        total = 0
        for ref, r in rs.items():
            request_valid(r)
            need(ref == digest(r), 'dependency content/address mismatch')
            total += len(r['history'])
        need(total <= MAX_TOTAL_STEPS, 'total history bound')
        memo = {}
        for view in vs:
            keys(view, ('request', 'cache'))
            ref, cached = view['request'], view['cache']
            need(type(ref) is str and ref in rs, 'missing retained dependency')
            need(type(cached) is dict and set(cached) <= set(RULES), 'unregistered cache component')
            if cached and ref not in memo:
                memo[ref] = replay(rs[ref])
            for field, item in cached.items():
                keys(item, ('rule', 'value'))
                need(item['rule'] == RULES[field], 'unknown replay rule')
                if field == 'output':
                    need(type(item['value']) is bool, 'output must be Boolean')
                else:
                    need(type(item['value']) is list and len(item['value']) <= MAX_STEPS + 1
                         and all(type(x) is bool for x in item['value']), 'trace must be bounded Booleans')
                need(item['value'] == memo[ref][field], 'cache disagrees with retained source')
        need(len(wire(doc)) <= MAX_BYTES, 'artifact exceeds byte bound')
        return memo, sum(len(rs[r]['history']) for r in memo)

    def build(self, requests):
        need(type(requests) is list and len(requests) <= MAX_REQUESTS, 'expected bounded request list')
        rs, vs = {}, []
        for r in requests:
            request_valid(r)
            ref = digest(r)
            need(ref not in rs or rs[ref] == r, 'content address collision')
            rs[ref] = deepcopy(r)
            computed = replay(r)
            vs.append({'request': ref, 'cache': {f: cache(f, computed[f]) for f in RULES}})
        doc = {'schema': SCHEMA, 'binding': self.binding, 'requests': rs, 'views': vs}
        self.validate(doc)
        return doc

    @staticmethod
    def sizes(doc):
        return {'active_bytes': len(wire(doc['views'])),
                'retained_dependency_bytes': len(wire(doc['requests'])),
                'total_bytes': len(wire(doc))}

    @staticmethod
    def missing_refs(doc):
        return {v['request'] for v in doc['views'] if set(v['cache']) != set(RULES)}

    def plan(self, doc, min_savings=1, replay_budget=MAX_TOTAL_STEPS):
        _, validation_steps = self.validate(doc)
        integer(min_savings, 0, MAX_BYTES)
        integer(replay_budget, 0, MAX_TOTAL_STEPS)
        work = deepcopy(doc)
        refs = self.missing_refs(work)
        cost = sum(len(work['requests'][r]['history']) for r in refs)
        need(cost <= replay_budget, 'existing omissions already exceed recovery budget')
        actions = []
        # Deterministic allowlist selection; no conjectural contraction search.
        for index, view in enumerate(work['views']):
            for field in ('trace', 'output'):
                if field not in view['cache']:
                    continue
                candidate = deepcopy(view)
                del candidate['cache'][field]
                saving = len(wire(view)) - len(wire(candidate))
                ref = view['request']
                extra = 0 if ref in refs else len(work['requests'][ref]['history'])
                if saving >= min_savings and cost + extra <= replay_budget:
                    actions.append({'view': index, 'field': field, 'rule': RULES[field], 'bytes_saved': saving})
                    del view['cache'][field]
                    refs.add(ref)
                    cost += extra
        return {'schema': PLAN, 'binding': self.binding, 'source': digest(doc), 'target': digest(work),
                'parameters': {'min_savings': min_savings, 'replay_budget': replay_budget},
                'actions': actions, 'before': self.sizes(doc), 'after': self.sizes(work),
                'validation_steps': validation_steps,
                'apply_validation_steps': validation_steps + sum(
                    len(work['requests'][r]['history'])
                    for r in {v['request'] for v in work['views'] if v['cache']}),
                'full_recovery_steps_bound': cost}

    def apply(self, doc, plan):
        keys(plan, ('schema', 'binding', 'source', 'target', 'parameters', 'actions', 'before', 'after',
                    'validation_steps', 'apply_validation_steps', 'full_recovery_steps_bound'))
        keys(plan['parameters'], ('min_savings', 'replay_budget'))
        need(plan['source'] == digest(doc), 'stale source plan')
        expected = self.plan(doc, **plan['parameters'])
        # Exact canonical JSON comparison also excludes Boolean-for-integer tricks.
        need(wire(plan) == wire(expected), 'unadmitted or altered reduction plan')
        result = deepcopy(doc)
        for action in plan['actions']:
            del result['views'][action['view']]['cache'][action['field']]
        self.validate(result)
        need(result['requests'] == doc['requests'], 'retained dependencies changed')
        return result

    def recover(self, doc, fields=('output', 'trace')):
        need(type(fields) in (tuple, list) and all(type(f) is str and f in RULES for f in fields)
             and len(fields) == len(set(fields)), 'unknown recovery fields')
        memo, validation_steps = self.validate(doc)
        result = deepcopy(doc)
        recovery_steps = 0
        added = 0
        for view in result['views']:
            missing = [f for f in fields if f not in view['cache']]
            if not missing:
                continue
            ref = view['request']
            if ref not in memo:
                memo[ref] = replay(doc['requests'][ref])
                recovery_steps += len(doc['requests'][ref]['history'])
            for f in missing:
                view['cache'][f] = cache(f, deepcopy(memo[ref][f]))
                added += 1
        return result, {'validation_steps': validation_steps, 'recovery_steps': recovery_steps,
                        'cache_fields_added': added, **self.sizes(result)}

    def undo(self, doc, plan):
        keys(plan, ('schema', 'binding', 'source', 'target', 'parameters', 'actions', 'before', 'after',
                    'validation_steps', 'apply_validation_steps', 'full_recovery_steps_bound'))
        keys(plan['parameters'], ('min_savings', 'replay_budget'))
        need(plan['target'] == digest(doc), 'stale target plan')
        need(type(plan['actions']) is list and len(plan['actions']) <= 2 * MAX_VIEWS, 'action count bound')
        full, metrics = self.recover(doc)
        previous = deepcopy(doc)
        for action in plan['actions']:
            keys(action, ('view', 'field', 'rule', 'bytes_saved'))
            index, field = action['view'], action['field']
            integer(index, 0, len(previous['views']) - 1)
            need(type(field) is str and field in RULES, 'unknown restoration component')
            need(action['rule'] == RULES[field], 'unknown restoration rule')
            need(field not in previous['views'][index]['cache'], 'duplicate or already present restoration')
            previous['views'][index]['cache'][field] = deepcopy(full['views'][index]['cache'][field])
        need(digest(previous) == plan['source'], 'restored source differs from plan')
        expected = self.plan(previous, **plan['parameters'])
        need(wire(expected) == wire(plan), 'unadmitted or altered restoration plan')
        metrics['plan_revalidation_steps'] = expected['validation_steps']
        metrics['temporarily_materialized_fields'] = metrics.pop('cache_fields_added')
        metrics['restored_fields'] = len(plan['actions'])
        metrics.update(self.sizes(previous))
        return previous, metrics

    def inspect(self, doc):
        _, validation_steps = self.validate(doc)
        refs = self.missing_refs(doc)
        return {**self.sizes(doc), 'views': len(doc['views']), 'requests': len(doc['requests']),
                'visible_fields': [sorted(v['cache']) for v in doc['views']],
                'validation_steps': validation_steps,
                'full_recovery_steps_bound': sum(len(doc['requests'][r]['history']) for r in refs)}


def demo(engine):
    requests = [{'history': [], 'input': True}, {'history': ['turn', 'turn'], 'input': True},
                {'history': ['stay', 'turn'] * 128, 'input': False}]
    full = engine.build(requests)
    plan = engine.plan(full)
    small = engine.apply(full, plan)
    restored, cost = engine.recover(small)
    undone, undo_cost = engine.undo(small, plan)
    need(wire(restored) == wire(full) and wire(undone) == wire(full), 'demo round trip failed')
    return {'full': full, 'plan': plan, 'compact': small,
            'recovery': cost, 'undo': undo_cost,
            'undo_plan_bytes': len(wire(plan)), 'total_compact_with_plan_bytes': len(wire(small)) + len(wire(plan)),
            'exact_json_round_trip': True,
            'scope': 'Closed Boolean replay policy; Python conformance tested, not extracted or fully verified.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('build', 'plan', 'apply', 'recover', 'undo', 'inspect'):
        p = sub.add_parser(command)
        p.add_argument('input', help='JSON file (request list for build, artifact otherwise)')
        if command == 'plan':
            p.add_argument('--min-savings', type=int, default=1)
            p.add_argument('--replay-budget', type=int, default=MAX_TOTAL_STEPS)
        if command in ('apply', 'undo'):
            p.add_argument('plan_file')
        if command == 'recover':
            p.add_argument('--fields', nargs='+', choices=tuple(RULES), default=list(RULES))
    sub.add_parser('demo')
    args = parser.parse_args()
    try:
        engine = Engine()
        if args.command == 'demo':
            result = demo(engine)
        else:
            value = load(args.input)
            if args.command == 'build':
                result = engine.build(value)
            elif args.command == 'plan':
                result = engine.plan(value, args.min_savings, args.replay_budget)
            elif args.command == 'apply':
                result = engine.apply(value, load(args.plan_file))
            elif args.command == 'undo':
                artifact, metrics = engine.undo(value, load(args.plan_file))
                print(json.dumps({'metrics': metrics}), file=sys.stderr)
                result = artifact
            elif args.command == 'recover':
                artifact, metrics = engine.recover(value, args.fields)
                print(json.dumps({'metrics': metrics}), file=sys.stderr)
                result = artifact
            else:
                result = engine.inspect(value)
        sys.stdout.buffer.write(wire(result) + b'\n')
    except (OSError, ValueError, AssertionError, KeyError, TypeError, RecursionError) as error:
        print(f'active-view: {error}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

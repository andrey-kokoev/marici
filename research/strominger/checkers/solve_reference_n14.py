"""Target constraints on an existing finite packet universe; not new physics."""
import json, sys, time
import z3
p = json.load(open(sys.argv[1], encoding='utf-8'))
ids = p['packets']
x = {i: z3.Bool('packet_' + str(i)) for i in ids}
entry = {i: z3.Int('entry_' + str(i)) for i in ids}
exit_rank = {i: z3.Int('exit_' + str(i)) for i in ids}
s = z3.Solver()
s.set(timeout=120000, random_seed=0)
s.add(x[p['root']], entry[p['root']] == 0)
incoming = {i: set() for i in ids}
outgoing = {i: set() for i in ids}
for op in p['operations']:
    incoming[op['target']].add(op['source'])
    outgoing[op['source']].add(op['target'])
for a, b in p['conflicts']:
    s.add(z3.Or(z3.Not(x[a]), z3.Not(x[b])))
for i in ids:
    s.add(z3.Implies(x[i], z3.And(entry[i] >= 0, entry[i] < len(ids), exit_rank[i] >= 0, exit_rank[i] < len(ids))))
    if i != p['root']:
        s.add(z3.Implies(x[i], z3.Or(*[z3.And(x[j], entry[j] < entry[i]) for j in incoming[i]])))
    if i in p['exits']:
        s.add(z3.Implies(x[i], exit_rank[i] == 0))
    else:
        s.add(z3.Implies(x[i], z3.Or(*[z3.And(x[j], exit_rank[j] < exit_rank[i]) for j in outgoing[i]])))
y = [z3.Or(*[x[i] for i in body['packets']]) for body in p['bodies']]
for species, count in p['target'].items():
    s.add(z3.PbEq([(y[i], 1) for i, b in enumerate(p['bodies']) if b['species'] == species], count))
for contact in p['contacts']:
    a, b = contact['bodies']
    witness = z3.Or(*[z3.And(x[i], x[j]) for i, j in contact['links']])
    s.add(z3.Implies(z3.And(y[a], y[b]), witness))
start = time.monotonic()
answer = s.check()
r = {'status': str(answer), 'elapsedSeconds': time.monotonic() - start, 'solver': 'z3-' + z3.get_version_string(), 'timeoutMs': 120000, 'selectedPackets': None, 'unknownReason': None}
if answer == z3.sat:
    model = s.model()
    r['selectedPackets'] = [i for i in ids if z3.is_true(model.eval(x[i], model_completion=True))]
elif answer == z3.unknown:
    r['unknownReason'] = s.reason_unknown()
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(r, f, indent=2)
print(json.dumps({k:v for k,v in r.items() if k != 'selectedPackets'}))

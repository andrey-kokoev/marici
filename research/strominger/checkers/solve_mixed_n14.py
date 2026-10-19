"""Global per-octahedron choices plus the unchanged selected-packet constraints."""
import json, sys, time
import z3
p = json.load(open(sys.argv[1], encoding='utf-8'))
x = {i: z3.Bool('p'+str(i)) for i in p['packets']}
d = {k: z3.Int('d'+str(i)) for i,k in enumerate(p['items'])}
s = z3.Solver(); s.set(timeout=120000, random_seed=0)
for v in d.values(): s.add(v >= 0, v <= 2)
for i in p['packets']:
    for key,value in p['requirements'][str(i)]: s.add(z3.Implies(x[i], d[key] == value))
s.add(z3.Or(*[x[i] for i in p['roots']]))
for a,b in p['conflicts']: s.add(z3.Or(z3.Not(x[a]), z3.Not(x[b])))
a = {i:z3.Int('a'+str(i)) for i in p['packets']}
b = {i:z3.Int('b'+str(i)) for i in p['packets']}
w = []
incoming = {i:[] for i in p['packets']}; outgoing = {i:[] for i in p['packets']}
for op in p['operations']:
    enabled = z3.And(x[op['source']], x[op['target']], *[d[k] == v for k,v in op['requirements']])
    w.append(enabled)
    incoming[op['target']].append(z3.And(enabled, a[op['source']] < a[op['target']]))
    outgoing[op['source']].append(z3.And(enabled, b[op['target']] < b[op['source']]))
for i in p['packets']:
    s.add(z3.Implies(x[i], z3.And(a[i] >= 0, a[i] < len(x), b[i] >= 0, b[i] < len(x))))
    if i in p['roots']: s.add(z3.Implies(x[i], a[i] == 0))
    else: s.add(z3.Implies(x[i], z3.Or(*incoming[i])))
    if i in p['exits']: s.add(z3.Implies(x[i], b[i] == 0))
    else: s.add(z3.Implies(x[i], z3.Or(*outgoing[i])))
y = [z3.Or(*[x[i] for i in body['packets']]) for body in p['bodies']]
for c in p['contacts']:
    i,j = c['bodies']; s.add(z3.Implies(z3.And(y[i],y[j]), z3.Or(*[w[k] for k in c['links']])))
answers=[]
for query in p.get('queries',[{'target':p['target'],'fixedChoices':p.get('fixedChoices',{})}]):
    s.push()
    for k,v in query.get('fixedChoices',{}).items(): s.add(d[k] == v)
    for species,count in query['target'].items():
        values=[(y[i],1) for i,body in enumerate(p['bodies']) if body['species']==species]
        s.add(z3.PbEq(values,count) if values else z3.BoolVal(count==0))
    start=time.monotonic(); answer=s.check()
    r={'status':str(answer),'solver':'z3-'+z3.get_version_string(),'timeoutMs':120000,'elapsedSeconds':time.monotonic()-start,'unknownReason':s.reason_unknown() if answer==z3.unknown else None,'selectedPackets':None,'choices':None}
    if answer==z3.sat:
        m=s.model(); r['selectedPackets']=[i for i in x if z3.is_true(m.eval(x[i],model_completion=True))]; r['choices']={k:m.eval(v,model_completion=True).as_long() for k,v in d.items()}
    answers.append(r); s.pop()
result={'answers':answers} if 'queries' in p else answers[0]
with open(sys.argv[2],'w',encoding='utf-8') as f: json.dump(result,f,indent=2)
print(json.dumps({'queries':len(answers),'statuses':[a['status'] for a in answers]}))

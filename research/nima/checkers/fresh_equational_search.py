"""Bounded, certificate-producing equational completion from one supplied axiom.
Only the supplied axiom is loaded: no known-answer template, published
proof, proof hints, or cached theorem is consulted.
The goal list is a fixed standard Boolean NAND basis. Failure is unresolved.
"""
from collections import Counter
from itertools import count
from pathlib import Path
import argparse
import heapq
import hashlib
import json
import time


def variables(t):
    return {t} if isinstance(t, str) else variables(t[0]) | variables(t[1])


def sub(t, env):
    return env.get(t, t) if isinstance(t, str) else tuple(sub(x, env) for x in t)


def walk(t, env):
    return walk(env[t], env) if isinstance(t, str) and t in env else (t if isinstance(t, str) else tuple(walk(x, env) for x in t))


def unify(a, b):
    env, pending = {}, [(a, b)]
    while pending:
        a, b = (walk(x, env) for x in pending.pop())
        if a == b: continue
        if not isinstance(a, str) and isinstance(b, str): a, b = b, a
        if isinstance(a, str):
            if a in variables(b): return None
            env[a] = b
        else:
            pending.extend(zip(a, b))
    return {x: walk(y, env) for x, y in env.items()}


def match(p, t, env=None):
    env = {} if env is None else env
    if isinstance(p, str):
        if p in env: return env if env[p] == t else None
        env[p] = t
        return env
    if isinstance(t, str): return None
    env = match(p[0], t[0], env)
    return None if env is None else match(p[1], t[1], env)


def positions(t):
    if not isinstance(t, str):
        for i in range(2):
            for p in positions(t[i]): yield (i,) + p
    yield ()


def at(t, path):
    for p in path: t = t[p]
    return t


def replace(t, path, value):
    if not path: return value
    parts = list(t)
    parts[path[0]] = replace(parts[path[0]], path[1:], value)
    return tuple(parts)


def weight(t):
    return 1 if isinstance(t, str) else 1 + weight(t[0]) + weight(t[1])


def rank(t):
    return weight(t), repr(t)


def refl(t): return ('refl', t)
def sym(p): return ('sym', p)
def chain(p, q): return ('trans', p, q)
def congr(t, path, p): return ('cong', t, path, p) if path else p

def proof_sub(p, env):
    k = p[0]
    if k == 'refl': return (k, sub(p[1], env))
    if k == 'call': return (k, p[1], {x:sub(y,env) for x,y in p[2].items()})
    if k == 'sym': return (k, proof_sub(p[1],env))
    if k == 'trans': return (k, proof_sub(p[1],env), proof_sub(p[2],env))
    if k == 'cong': return (k, sub(p[1],env), p[2], proof_sub(p[3],env))
    raise ValueError(k)


def proof_vars(p):
    if p[0] == 'refl': return variables(p[1])
    if p[0] == 'call': return set().union(*(variables(t) for t in p[2].values()))
    if p[0] == 'sym': return proof_vars(p[1])
    if p[0] == 'trans': return proof_vars(p[1]) | proof_vars(p[2])
    return variables(p[1]) | proof_vars(p[3])


def canonical(eq, proof):
    env = {}
    def visit(t):
        if isinstance(t, str):
            if t not in env: env[t] = f'x{len(env)}'
        else: visit(t[0]); visit(t[1])
    visit(eq[0]); visit(eq[1])
    for extra in proof_vars(proof) - env.keys(): env[extra] = 'x0'
    return tuple(sub(t, env) for t in eq), proof_sub(proof, env)


def call(i, eq, prefix=''):
    return ('call', i, {v: prefix + v for v in variables(eq[0]) | variables(eq[1])})


def orientations(eq, proof):
    for a, b, p in [(eq[0],eq[1],proof),(eq[1],eq[0],sym(proof))]:
        if not isinstance(a,str) and variables(b) <= variables(a): yield a,b,p


# Classical Sheffer conditions plus commutativity. They are goals, not premises.
x, y, z = 'x0', 'x1', 'x2'
GOALS = {
 'commutativity': ((x,y),(y,x)),
 'involution': (((x,x),(x,x)),x),
 'sheffer-2': ((x,(y,(y,y))),(x,x)),
 'sheffer-3': ((((y,y),x),((z,z),x)), ((x,(y,z)),(x,(y,z))))
}


def complete(equation, seconds=20, max_facts=250, max_weight=45):
    records = [{'equation': equation, 'proof': ('axiom',)}]
    active, heap, seen, found = [0], [], set(), {}
    serial = count()
    started = time.monotonic()
    attempts = 0

    def enqueue(eq, proof):
        if eq[0] == eq[1] or sum(map(weight,eq)) > max_weight: return
        eq, proof = canonical(eq, proof)
        key = tuple(sorted(eq,key=repr))
        if key in seen: return
        seen.add(key)
        heapq.heappush(heap, (sum(map(weight,eq)), next(serial), eq, proof))

    def simplify(t, excluding=None):
        proof = refl(t)
        for _ in range(200):
            changed = False
            for path in positions(t):
                current = at(t,path)
                for i in active:
                    if i == excluding: continue
                    eq = records[i]['equation']
                    for a,b,p in orientations(eq, call(i,eq)):
                        env = match(a,current)
                        if env is None: continue
                        value = sub(b,env)
                        if rank(value) >= rank(current): continue
                        proof = chain(proof,congr(t,path,proof_sub(p,env)))
                        t = replace(t,path,value)
                        changed = True
                        break
                    if changed: break
                if changed: break
            if not changed: return t,proof
        return t,proof

    def overlaps(i,j):
        nonlocal attempts
        aeq, beq = records[i]['equation'], records[j]['equation']
        ae = tuple(sub(t,{v:'a'+v for v in variables(t)}) for t in aeq)
        be = tuple(sub(t,{v:'b'+v for v in variables(t)}) for t in beq)
        for a,b,pa in orientations(ae,call(i,aeq,'a')):
            for c,d,pb in orientations(be,call(j,beq,'b')):
                for path in positions(c):
                    if isinstance(at(c,path),str): continue
                    attempts += 1
                    env = unify(a,at(c,path))
                    if env is None: continue
                    left = sub(replace(c,path,b),env)
                    right = sub(d,env)
                    proof = chain(sym(proof_sub(congr(c,path,pa),env)),proof_sub(pb,env))
                    enqueue((left,right),proof)

    def goals():
        for name, goal in GOALS.items():
            if name in found: continue
            a,p = simplify(goal[0]); b,q = simplify(goal[1])
            if a == b: found[name] = chain(p,sym(q))

    goals()
    overlaps(0,0)
    while heap and len(records) < max_facts and time.monotonic()-started < seconds:
        if len(records) % 7 == 0:
            oldest = min(range(len(heap)), key=lambda k: heap[k][1])
            item = heap[oldest]
            heap[oldest] = heap[-1]; heap.pop(); heapq.heapify(heap)
            _,_,eq,p = item
        else:
            _,_,eq,p = heapq.heappop(heap)
        a,pa = simplify(eq[0]); b,pb = simplify(eq[1])
        if a == b: continue
        eq,p = canonical((a,b),chain(sym(pa),chain(p,pb)))
        i = len(records)
        records.append({'equation':eq,'proof':p})
        active.append(i)
        goals()
        if len(found) == len(GOALS): break
        for j in list(active):
            if time.monotonic()-started >= seconds: break
            overlaps(i,j)
            if i != j: overlaps(j,i)
        for j in list(active):
            if j == i: continue
            old = records[j]['equation']
            a,pa = simplify(old[0],j); b,pb = simplify(old[1],j)
            if (a,b) != old:
                active.remove(j)
                enqueue((a,b),chain(sym(pa),chain(call(j,old),pb)))
        if len(heap) > 12000:
            heap = heapq.nsmallest(6000,heap); heapq.heapify(heap)
    return {'schema':'marici.fresh-equational-search.v1', 'input':equation,
            'status':'basis-derived' if len(found)==len(GOALS) else 'unresolved',
            'goals':GOALS, 'derived':found, 'records':records,
            'statistics':{'facts':len(records),'active':len(active),'pending':len(heap),'overlaps':attempts},
            'limits':{'seconds':seconds,'facts':max_facts,'weight':max_weight,'pending_trim':12000,'age_selection_period':7}}


def decode(t):
    if type(t) is int and t >= 0: return f'x{t}'
    if isinstance(t,list) and len(t)==2: return tuple(decode(x) for x in t)
    raise ValueError('invalid source term')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--ordinal',type=int,required=True)
    parser.add_argument('--seconds',type=int,default=20,choices=range(1,61))
    parser.add_argument('--facts',type=int,default=250,choices=range(1,1001))
    parser.add_argument('--weight',type=int,default=45,choices=range(14,81))
    args = parser.parse_args()
    code_bytes = Path(__file__).read_bytes()
    input_bytes = args.source.read_bytes()
    packet = json.loads(input_bytes)
    source = next(s for s in packet['survivors'] if s['cost']==6 and s['ordinal']==args.ordinal)
    equation = decode(source['left']),decode(source['right'])
    result = complete(equation,args.seconds,args.facts,args.weight)
    if code_bytes != Path(__file__).read_bytes() or input_bytes != args.source.read_bytes():
        raise RuntimeError('inputs changed during search')
    result['provenance'] = {
        'prover_sha256': hashlib.sha256(code_bytes).hexdigest(),
        'candidate_source_sha256': hashlib.sha256(input_bytes).hexdigest(),
        'cost': 6, 'ordinal': args.ordinal,
        'selection': 'explicit benchmark input, not autonomous formula selection',
        'cached_adequacy_used': False}
    args.output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({'status':result['status'],'derived':list(result['derived']),'statistics':result['statistics']}))

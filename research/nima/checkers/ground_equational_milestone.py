"""Fresh one-parameter axiom instantiation with proof-producing congruence closure.
No old consequence files, candidate-specific lemmas, or published proofs are read.
The supplied equation is the only axiom. A bounded miss is unresolved.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from fresh_equational_search import GOALS, decode
from check_fresh_equations import verify, vars_


class BudgetStop(Exception):
    pass


def trans(p, q):
    if p[0] == 'refl': return q
    if q[0] == 'refl': return p
    return ('trans', p, q)


def sym(p):
    return p if p[0] == 'refl' else ('sym', p)


@lru_cache(None)
def trees(cost):
    if cost == 0: return ('x0',)
    return tuple((a, b) for k in range(cost)
                 for a in trees(k) for b in trees(cost-1-k))


class Closure:
    def __init__(self, equation, seconds=60, nodes=100000, unions=60000):
        self.records = [{'equation': equation, 'proof': ['axiom']}]
        self.started = time.monotonic()
        self.seconds, self.node_limit, self.union_limit = seconds, nodes, unions
        self.terms, self.children, self.parents, self.sizes = [], [], [], []
        self.edges, self.uses, self.keys = [], [], []
        self.syntax, self.signatures, self.dirty = {}, {}, set()
        self.axiom_unions = self.congruence_unions = 0

    def check(self):
        if time.monotonic()-self.started >= self.seconds: raise BudgetStop('seconds')

    def find(self, n):
        # Keep the explanation forest immutable: union by size, no path compression.
        while self.parents[n] != n: n = self.parents[n]
        return n

    def path(self, n):
        p = ('refl', self.terms[n])
        while self.parents[n] != n:
            p = trans(p, ('call', self.edges[n], {'x0': 'x0'}))
            n = self.parents[n]
        return p

    def explain(self, a, b):
        if self.find(a) != self.find(b): raise ValueError('unproved equality')
        return ('refl', self.terms[a]) if a == b else trans(self.path(a), sym(self.path(b)))

    def union(self, a, b, reason, kind):
        self.check()
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        if len(self.records)-1 >= self.union_limit: raise BudgetStop('unions')
        p = trans(sym(self.path(a)), trans(reason, self.path(b)))
        # Every stored edge points from the attached root to its new parent.
        if self.sizes[ra] > self.sizes[rb] or (self.sizes[ra] == self.sizes[rb] and ra < rb):
            ra, rb, p = rb, ra, sym(p)
        idx = len(self.records)
        self.records.append({'equation': (self.terms[ra], self.terms[rb]), 'proof': p})
        self.parents[ra], self.edges[ra] = rb, idx
        self.sizes[rb] += self.sizes[ra]
        self.uses[rb].update(self.uses[ra])
        self.dirty.update(self.uses[rb])
        self.uses[ra] = set()
        if kind == 'axiom': self.axiom_unions += 1
        else: self.congruence_unions += 1

    def intern(self, children, term):
        if children in self.syntax: return self.syntax[children]
        self.check()
        if len(self.terms) >= self.node_limit: raise BudgetStop('nodes')
        n = len(self.terms)
        self.syntax[children] = n
        self.terms.append(term); self.children.append(children)
        self.parents.append(n); self.sizes.append(1); self.edges.append(None)
        self.uses.append(set()); self.keys.append(None)
        if children is not None:
            for c in children: self.uses[self.find(c)].add(n)
            self.dirty.add(n)
        return n

    def add(self, term):
        if isinstance(term, str):
            if term != 'x0': raise ValueError('rigid parameter must be x0')
            return self.intern(None, term)
        children = tuple(self.add(t) for t in term)
        return self.intern(children, term)

    def instance(self, term, env):
        if isinstance(term, str): return env[term]
        a, b = (self.instance(t, env) for t in term)
        return self.intern((a,b), (self.terms[a],self.terms[b]))

    def rebuild(self):
        while self.dirty:
            self.check()
            n = self.dirty.pop()
            a, b = self.children[n]
            key = (self.find(a), self.find(b))
            oldkey = self.keys[n]
            if oldkey != key and self.signatures.get(oldkey) == n:
                del self.signatures[oldkey]
            self.keys[n] = key
            other = self.signatures.get(key)
            if other is None:
                self.signatures[key] = n
            elif self.find(other) != self.find(n):
                c, d = self.children[other]
                # These premise paths exist before this new union.
                left, right = self.explain(a,c), self.explain(b,d)
                p = ('cong', self.terms[n], (0,), left)
                middle = (self.terms[c], self.terms[b])
                q = ('cong', middle, (1,), right)
                self.union(n, other, trans(p,q), 'congruence')


def references(p):
    if p[0] == 'call': yield p[1]
    elif p[0] == 'sym': yield from references(p[1])
    elif p[0] == 'trans':
        yield from references(p[1]); yield from references(p[2])
    elif p[0] == 'cong': yield from references(p[3])


def prune(records, conclusion):
    needed, pending = {0}, list(references(conclusion))
    while pending:
        i = pending.pop()
        if i in needed: continue
        needed.add(i); pending.extend(references(records[i]['proof']))
    indices = sorted(needed); renaming = {v:i for i,v in enumerate(indices)}
    def rename(p):
        if p[0] == 'call': return ('call', renaming[p[1]], p[2])
        if p[0] in ('axiom','refl'): return p
        if p[0] == 'sym': return ('sym',rename(p[1]))
        if p[0] == 'trans': return ('trans',rename(p[1]),rename(p[2]))
        return ('cong',p[1],p[2],rename(p[3]))
    return [{'equation':records[i]['equation'],'proof':rename(records[i]['proof'])}
            for i in indices], rename(conclusion)


def search(equation, seconds=60, pool_cost=5, instances=30000, nodes=100000, unions=60000):
    closure = Closure(equation, seconds, nodes, unions)
    names = sorted(vars_(equation[0]) | vars_(equation[1]))
    visited = 0; target = None; stop = 'instance-pool-exhausted'
    try:
        target = tuple(closure.add(t) for t in GOALS['involution'])
        pools = [[closure.add(t) for t in trees(k)] for k in range(pool_cost+1)]
        closure.rebuild()
        degrees = sorted(product(range(pool_cost+1), repeat=len(names)), key=lambda ks:(sum(ks),ks))
        for ks in degrees:
            for values in product(*(pools[k] for k in ks)):
                if visited >= instances: raise BudgetStop('instances')
                closure.check()
                env = dict(zip(names,values))
                a,b = (closure.instance(t,env) for t in equation)
                p = ('call',0,{v:closure.terms[n] for v,n in env.items()})
                closure.union(a,b,p,'axiom'); visited += 1
                closure.rebuild()
                if closure.find(target[0]) == closure.find(target[1]):
                    raise BudgetStop('goal-derived')
    except BudgetStop as exc:
        stop = str(exc)
    derived = {}
    reached = target is not None and closure.find(target[0]) == closure.find(target[1])
    if reached:
        records, proof = prune(closure.records, closure.explain(*target))
        derived['involution'] = proof
    else:
        records = closure.records[:1]
    certificate = {'schema':'marici.fresh-equational-search.v1','input':equation,
                   'records':records,'goals':GOALS,'derived':derived,'status':'unresolved'}
    # The existing certificate's status concerns the FOUR-law basis, not this milestone.
    certificate = json.loads(json.dumps(certificate))
    replay = verify(certificate, equation)
    return {'schema':'marici.ground-equational-milestone.v1',
            'status':'goal-derived' if reached else 'unresolved',
            'target':'involution','certificate':certificate,'replay':replay,
            'statistics':{'instances':visited,'nodes':len(closure.terms),
                'unions':len(closure.records)-1,'axiom_unions':closure.axiom_unions,
                'congruence_unions':closure.congruence_unions,
                'exported_records':len(records),'stop':stop,
                'elapsed_seconds':time.monotonic()-closure.started},
            'limits':{'seconds':seconds,'pool_cost':pool_cost,'instances':instances,'nodes':nodes,'unions':unions},
            'adequacy_constructed':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--ordinal',type=int,required=True)
    args = parser.parse_args()
    dependencies = [Path(__file__),Path(__file__).with_name('fresh_equational_search.py'),
                    Path(__file__).with_name('check_fresh_equations.py')]
    hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies}
    data = args.source.read_bytes()
    candidate = next(s for s in json.loads(data)['survivors'] if s['cost']==6 and s['ordinal']==args.ordinal)
    equation = decode(candidate['left']),decode(candidate['right'])
    runpath = Path(__file__).resolve().parents[3]/'.ai/tmp/scc-state/nima-double-negation-run.json'
    manifest = {'schema':'marici.ground-equational-run.v1','command':[sys.executable,*sys.argv],
        'build':'interpreted Python source','source_sha256':hashes,
        'executable_sha256':hashlib.sha256(Path(sys.executable).read_bytes()).hexdigest(),
        'input':str(args.source),'input_sha256':hashlib.sha256(data).hexdigest(),
        'pid':os.getpid(),'parent_pid':os.getppid(),'children':[],
        'started_at':datetime.now(timezone.utc).isoformat(),'status':'running',
        'output':str(args.output),'expected_schema':'marici.ground-equational-milestone.v1'}
    runpath.write_text(json.dumps(manifest,indent=2)+'\n')
    result = search(equation)
    if args.source.read_bytes()!=data or any(hashlib.sha256(p.read_bytes()).hexdigest()!=hashes[str(p)] for p in dependencies):
        raise RuntimeError('source changed during search')
    result['provenance'] = {'input_sha256':hashlib.sha256(data).hexdigest(),'source_sha256':hashes,
        'cost':6,'ordinal':args.ordinal,'cached_adequacy_used':False,'cached_consequences_used':False}
    args.output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    manifest.update(status=result['status'],exit_code=0,finished_at=datetime.now(timezone.utc).isoformat())
    runpath.write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','statistics','limits','replay']}))


if __name__ == '__main__': main()

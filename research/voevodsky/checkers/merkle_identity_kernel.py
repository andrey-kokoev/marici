"""Small Merkle equality kernel for commutative Q-polynomials.
No eval, arbitrary code, division, analytic functions or implicit axioms.
Proof rules: ring, refl, sym, trans, congruence and explicitly scoped assumption.
"""
from fractions import Fraction as Q
from hashlib import sha256
import argparse
import json
from pathlib import Path

DOMAIN = b'marici.polynomial-proof.v1\0'
MAX_OBJECTS, MAX_DEPTH, MAX_TERMS, MAX_DEGREE = 10000, 100, 4096, 64

def digest(record):
    return sha256(DOMAIN + json.dumps(record,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def shape(record, fields):
    if not isinstance(record,dict) or set(record)!=set(fields.split()): raise ValueError('record shape')

def bounded_coefficient(value):
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > 4096:
        raise ValueError('coefficient bit limit')
    return value

def add(a,b):
    out=dict(a)
    for m,c in b.items():
        out[m]=bounded_coefficient(out.get(m,Q(0))+c)
        if not out[m]: del out[m]
    if len(out)>MAX_TERMS: raise ValueError('polynomial size limit')
    return out

def mul(a,b):
    if len(a)*len(b)>MAX_TERMS*4: raise ValueError('multiplication work limit')
    out={}
    for m,c in a.items():
        for n,d in b.items():
            monomial=tuple(sorted(m+n))
            if len(monomial)>MAX_DEGREE: raise ValueError('degree limit')
            out=add(out,{monomial:bounded_coefficient(c*d)})
    return out

class Builder:
    def __init__(self): self.objects={}
    def put(self,record):
        key=digest(record); self.objects[key]=record; return key
    def var(self,name): return self.put({'kind':'term','type':'Q','op':'var','name':name})
    def const(self,value): return self.put({'kind':'term','type':'Q','op':'const','value':str(Q(value))})
    def term(self,op,*args): return self.put({'kind':'term','type':'Q','op':op,'args':list(args)})
    def proof(self,rule,lhs,rhs,**extra): return self.put({'kind':'proof','rule':rule,'lhs':lhs,'rhs':rhs,**extra})
    def artifact(self,variables,assumptions,proof):
        context=self.put({'kind':'context','variables':variables,'assumptions':assumptions})
        root=self.put({'kind':'judgment','context':context,'proof':proof})
        return {'schema':'marici.polynomial-proof-store.v1','root':root,'objects':dict(self.objects)}

class Kernel:
    def __init__(self,artifact):
        shape(artifact,'schema root objects')
        if artifact['schema']!='marici.polynomial-proof-store.v1': raise ValueError('unsupported store schema')
        self.store=artifact['objects']
        if not isinstance(self.store,dict) or len(self.store)>MAX_OBJECTS: raise ValueError('object limit')
        self.root=artifact['root']; self.terms={}; self.proofs={}; self.active=set()
        root=self.get(self.root); shape(root,'kind context proof')
        if root['kind']!='judgment': raise ValueError('not a judgment')
        context=self.get(root['context']); shape(context,'kind variables assumptions')
        if context['kind']!='context' or not isinstance(context['variables'],list): raise ValueError('context shape')
        names=context['variables']
        if any(not isinstance(n,str) or not n.isidentifier() for n in names) or len(names)!=len(set(names)): raise ValueError('variable declarations')
        self.variables=set(names); self.assumptions=context['assumptions']
        if not isinstance(self.assumptions,dict): raise ValueError('assumptions shape')
        for label,pair in self.assumptions.items():
            if not isinstance(label,str) or not isinstance(pair,list) or len(pair)!=2: raise ValueError('assumption shape')
            for ref in pair: self.term(ref)
        self.proof_root=root['proof']
    def get(self,key):
        if not isinstance(key,str) or key not in self.store or digest(self.store[key])!=key: raise ValueError('missing object or hash mismatch')
        return self.store[key]
    def term(self,key,depth=0):
        if depth>MAX_DEPTH: raise ValueError('term depth limit')
        if key in self.terms: return self.terms[key]
        record=self.get(key)
        if record.get('kind')!='term' or record.get('type')!='Q': raise ValueError('term type')
        op=record.get('op')
        if op=='var':
            shape(record,'kind type op name')
            if record['name'] not in self.variables: raise ValueError('undeclared variable')
            result={(record['name'],):Q(1)}
        elif op=='const':
            shape(record,'kind type op value')
            if not isinstance(record['value'],str) or len(record['value'])>1024: raise ValueError('rational size/type')
            c=Q(record['value'])
            if str(c)!=record['value']: raise ValueError('noncanonical rational')
            result={():c} if c else {}
        elif op in ('add','mul','neg'):
            shape(record,'kind type op args')
            if not isinstance(record['args'],list) or len(record['args'])!=(1 if op=='neg' else 2): raise ValueError('term arity')
            args=[self.term(r,depth+1) for r in record['args']]
            result=add(*args) if op=='add' else mul(*args) if op=='mul' else {m:-c for m,c in args[0].items()}
        else: raise ValueError('unsupported expression constructor')
        self.terms[key]=result; return result
    def proof(self,key,depth=0):
        if depth>MAX_DEPTH: raise ValueError('proof depth limit')
        if key in self.proofs: return self.proofs[key]
        if key in self.active: raise ValueError('cyclic proof')
        self.active.add(key)
        record=self.get(key)
        if record.get('kind')!='proof': raise ValueError('not a proof')
        rule=record.get('rule'); lhs,rhs=record.get('lhs'),record.get('rhs')
        left,right=self.term(lhs),self.term(rhs); used=set()
        base='kind rule lhs rhs'
        if rule in ('ring','refl'):
            shape(record,base)
            if (left!=right if rule=='ring' else lhs!=rhs): raise ValueError('false equality')
        elif rule=='assumption':
            shape(record,base+' label'); label=record['label']
            if self.assumptions.get(label)!=[lhs,rhs]: raise ValueError('unscoped or mismatched assumption')
            used.add(label)
        elif rule in ('sym','trans','congruence'):
            shape(record,base+' premises')
            refs=record['premises']
            if not isinstance(refs,list) or len(refs)>(2): raise ValueError('premise arity')
            premises=[self.proof(r,depth+1) for r in refs]
            for _,_,deps in premises: used.update(deps)
            if rule=='sym':
                if len(premises)!=1 or (lhs,rhs)!=(premises[0][1],premises[0][0]): raise ValueError('symmetry endpoints')
            elif rule=='trans':
                if len(premises)!=2 or premises[0][1]!=premises[1][0] or (lhs,rhs)!=(premises[0][0],premises[1][1]): raise ValueError('transitivity endpoints')
            else:
                l,r=self.get(lhs),self.get(rhs)
                if l['op'] not in ('add','mul','neg') or l['op']!=r['op'] or len(premises)!=len(l['args']): raise ValueError('congruence constructor')
                if l['args']!=[p[0] for p in premises] or r['args']!=[p[1] for p in premises]: raise ValueError('congruence endpoints')
        else: raise ValueError('unsupported proof rule')
        self.active.remove(key)
        result=(lhs,rhs,frozenset(used)); self.proofs[key]=result; return result
    def verify(self):
        lhs,rhs,used=self.proof(self.proof_root)
        return {'verified':True,'root':self.root,'lhs':lhs,'rhs':rhs,'type':'Q',
                'used_assumptions':sorted(used),'unconditional':not used,
                'scope':'Universal commutative Q-polynomial equality, conditional on exactly the listed context assumptions.'}

def verify(artifact): return Kernel(artifact).verify()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('artifact',type=Path)
    parser.add_argument('--require-unconditional',action='store_true'); args=parser.parse_args()
    try:
        if args.artifact.stat().st_size>10_000_000: raise ValueError('input file size limit')
        result=verify(json.loads(args.artifact.read_text(encoding='utf-8')))
        print(json.dumps(result,indent=2))
        if args.require_unconditional and not result['unconditional']: raise SystemExit(1)
    except (ValueError,KeyError,TypeError,ZeroDivisionError,RecursionError) as error:
        print(json.dumps({'verified':False,'error':str(error)})); raise SystemExit(1)

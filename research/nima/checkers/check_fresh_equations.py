"""Small independent equational certificate checker. No search or theorem cache."""
from pathlib import Path
import argparse
import json


def term(t):
    if isinstance(t, str) and t.startswith('x') and t[1:].isdigit(): return t
    if isinstance(t, (tuple,list)) and len(t)==2: return tuple(term(x) for x in t)
    raise ValueError('invalid term')


def vars_(t):
    return {t} if isinstance(t,str) else vars_(t[0]) | vars_(t[1])


def inst(t, sigma):
    return sigma.get(t,t) if isinstance(t,str) else tuple(inst(x,sigma) for x in t)


def contextual(t, path, old, new):
    if not path:
        if t != old: raise ValueError('congruence boundary mismatch')
        return new
    if isinstance(t,str) or path[0] not in (0,1): raise ValueError('invalid congruence path')
    xs=list(t); xs[path[0]]=contextual(xs[path[0]],path[1:],old,new)
    return tuple(xs)


def infer(p, known):
    if not isinstance(p,(list,tuple)) or not p: raise ValueError('invalid inference')
    k=p[0]
    arities={'refl':2,'call':3,'sym':2,'trans':3,'cong':4}
    if k not in arities or len(p)!=arities[k]: raise ValueError('inference schema mismatch')
    if k=='refl':
        t=term(p[1]); return t,t
    if k=='call':
        i=p[1]
        if type(i) is not int or not 0 <= i < len(known): raise ValueError('nonprior reference')
        a,b=known[i]
        sigma={v:term(t) for v,t in p[2].items()}
        if set(sigma) != vars_(a)|vars_(b): raise ValueError('substitution domain mismatch')
        return inst(a,sigma),inst(b,sigma)
    if k=='sym': return infer(p[1],known)[::-1]
    if k=='trans':
        a,b=infer(p[1],known); c,d=infer(p[2],known)
        if b!=c: raise ValueError('transitivity boundary mismatch')
        return a,d
    if k=='cong':
        context=term(p[1]); a,b=infer(p[3],known)
        return context,contextual(context,p[2],a,b)
    raise ValueError('unregistered inference')


def verify(packet, expected_input=None):
    if packet.get('schema')!='marici.fresh-equational-search.v1': raise ValueError('packet schema mismatch')
    x,y,z='x0','x1','x2'
    goals={
        'commutativity':((x,y),(y,x)),
        'involution':(((x,x),(x,x)),x),
        'sheffer-2':((x,(y,(y,y))),(x,x)),
        'sheffer-3':((((y,y),x),((z,z),x)),((x,(y,z)),(x,(y,z))))}
    supplied={name:tuple(term(t) for t in eq) for name,eq in packet['goals'].items()}
    if supplied!=goals: raise ValueError('goal contract mismatch')
    source=tuple(term(x) for x in packet['input'])
    if expected_input is not None and source!=expected_input: raise ValueError('wrong external input')
    if not packet['records']: raise ValueError('missing input axiom')
    known=[]
    for i,record in enumerate(packet['records']):
        equation=tuple(term(x) for x in record['equation'])
        if i==0:
            if record['proof'] != ['axiom'] or equation!=source: raise ValueError('input axiom mismatch')
        elif infer(record['proof'],known)!=equation: raise ValueError(('incorrect conclusion',i))
        known.append(equation)
    for name,proof in packet['derived'].items():
        if infer(proof,known)!=goals[name]: raise ValueError('goal mismatch')
    complete=set(packet['derived'])==set(goals)
    if packet['status']!=('basis-derived' if complete else 'unresolved'): raise ValueError('status mismatch')
    return {'facts_checked':len(known),'goals_checked':sorted(packet['derived']),
            'basis_complete':complete,'external_input_bound':expected_input is not None}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    args=parser.parse_args()
    print(json.dumps(verify(json.loads(args.source.read_text()))))

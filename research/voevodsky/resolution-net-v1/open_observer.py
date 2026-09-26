"""Independent open-tree observer, alpha-invariant but receipt-order faithful."""
from reference import Admission,Seed,Step

def encode(history):
    if isinstance(history,Seed):
        if isinstance(history.evidence,Admission):return ('seed0',history.evidence)
        return ('seed1',history.package,encode(history.evidence))
    return ('step',history.rule,tuple(encode(p) for p in history.premises))

def substitute(term,inputs):
    kind=term[0]
    if kind=='hole':return encode(inputs[term[1]]) if term[1] in inputs else term
    if kind=='seed1':return ('seed1',term[1],substitute(term[2],inputs))
    if kind=='step':return ('step',term[1],tuple(substitute(t,inputs) for t in term[2]))
    return term

def flatten_term(term):
    if term[0]=='seed1':return term[2]
    if term[0]=='step':return ('step',term[1],tuple(flatten_term(t) for t in term[2]))
    raise ValueError('not a resolution of resolutions')

def size(term):
    if term[0] in ('seed0','seed1'):return 1
    if term[0]=='step':return 1+sum(size(t) for t in term[2])
    raise ValueError('unexpected free hole at outer layer')

def observe(net):
    net.validate()
    def visit(port):
        i,entry=port
        if i in net.boundaries:
            slot,p=net.boundaries[i];h=('hole',slot,p);return h,0,h
        a=net.agents[i]
        if a.kind=='flatten':
            term,cost,raw=visit(net.wires[i,0])
            if cost:raise ValueError('nested active region')
            return flatten_term(term),size(term),('F',raw)
        if a.kind=='seed':
            if a.arity==0:
                term=('seed0',a.payload);return term,0,term
            term,cost,raw=visit(net.wires[i,1])
            return ('seed1',a.payload,term),cost,('seed1',a.payload,raw)
        children=[visit(net.wires[i,k]) for k in range(1,a.arity+1)]
        return ('step',a.payload,tuple(x[0] for x in children)),sum(x[1] for x in children),('step',a.payload,tuple(x[2] for x in children))
    term,cost,raw=visit(net.wires[0,0])
    return {'denotation':term,'pending_work':cost,'missing':tuple(sorted(slot for slot,_ in net.boundaries.values())),
            'shape':raw,'receipts':net.receipts,'released':net.released()}

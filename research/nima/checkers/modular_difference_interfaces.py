"""Raw-atom difference blocks; no moment rows or external solver dependency."""
from fractions import Fraction as Q
from dataclasses import dataclass
import json,hashlib,copy

def rational(x):
    if type(x) not in (int,str,Q):raise ValueError('EXACT_RATIONAL_REQUIRED')
    return Q(x)
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def canonical(raw):
    s=copy.deepcopy(raw)
    if set(s)!={'m','binding','retention','blocks','public','exterior'}:raise ValueError('UNSUPPORTED_STATE')
    if type(s['m']) is not int or s['m']<2 or not isinstance(s['binding'],str) or not s['binding']:raise ValueError('INVALID_SOURCE')
    if s['retention'] not in ('archive-backed','public-only'):raise ValueError('INVALID_POLICY')
    def nodes(values):
        values=list(values)
        if any(type(v) is not int or not 0<=v<=s['m'] for v in values) or values!=sorted(set(values)) or 0 not in values:raise ValueError('INVALID_NODES')
        return values
    def edges(es,allowed):
        result=[]
        for u,v,w in es:
            if type(u) is not int or type(v) is not int or u not in allowed or v not in allowed:raise ValueError('INVALID_EDGE')
            result.append([u,v,str(rational(w))])
        return result
    ownership={};boundary=set()
    for b in s['blocks']:
        if set(b)!={'nodes','boundary','evidence'}:raise ValueError('UNSUPPORTED_BLOCK')
        b['nodes']=nodes(b['nodes']);b['boundary']=nodes(b['boundary'])
        if not set(b['boundary'])<=set(b['nodes']):raise ValueError('INVALID_BOUNDARY')
        b['evidence']=edges(b['evidence'],b['nodes']);boundary.update(b['boundary'])
        for v in b['nodes']:ownership.setdefault(v,[]).append(b)
    if set(ownership)!=set(range(s['m']+1)):raise ValueError('INCOMPLETE_SOURCE')
    if any(len(bs)>1 and any(v not in b['boundary'] for b in bs) for v,bs in ownership.items()):raise ValueError('SHARED_INTERIOR')
    s['public']=nodes(s['public'])
    if not set(s['public'])<=boundary:raise ValueError('PUBLIC_NODE_NOT_ON_INTERFACE')
    s['exterior']=edges(s['exterior'],boundary)
    return s

def block_edges(block):
    return [[u,v,str(w)] for j in block['nodes'] if j for u,v,w in ((0,j,100+2*(j-1)),(j,0,0))]+block['evidence']

def closure(nodes,edges):
    n=len(nodes);where={v:k for k,v in enumerate(nodes)};D=[[None]*n for _ in nodes];paths=[[None]*n for _ in nodes]
    for i in range(n):D[i][i]=Q(0);paths[i][i]=[]
    for index,(u,v,w) in enumerate(edges):
        i,j=where[u],where[v];w=Q(w)
        if D[i][j] is None or w<D[i][j]:D[i][j]=w;paths[i][j]=[index]
    def negative():
        return next((paths[i][i] for i in range(n) if D[i][i]<0),None)
    cycle=negative()
    if cycle is not None:return {'status':'INCONSISTENT','cycle':cycle}
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] is None or D[k][j] is None:continue
                value=D[i][k]+D[k][j]
                if D[i][j] is None or value<D[i][j]:D[i][j]=value;paths[i][j]=paths[i][k]+paths[k][j]
        cycle=negative()
        if cycle is not None:return {'status':'INCONSISTENT','cycle':cycle}
    assert all(v is not None for row in D for v in row)
    return {'status':'CONSISTENT','distance':[[str(v) for v in row] for row in D],'paths':paths}

def summary(nodes,proof,public):
    D=proof['distance'];return [[a,b,D[nodes.index(a)][nodes.index(b)]] for a in public for b in public if a!=b]

def compile_state(raw):
    state=canonical(raw);proofs=[closure(b['nodes'],block_edges(b)) for b in state['blocks']]
    return compose_blocks(state,proofs)

def compose_blocks(state,proofs):
    """Proposal assembly; callers must validate reused proof dependencies."""
    assert len(proofs)==len(state['blocks'])
    packet={'state':state,'state_digest':digest(state),'blocks':proofs}
    bad=next((i for i,p in enumerate(proofs) if p['status']=='INCONSISTENT'),None)
    if bad is not None:
        packet.update(status='INCONSISTENT',inconsistent_block=bad);return None,packet
    nodes=sorted(set(v for b in state['blocks'] for v in b['boundary']));edges=[];expansions=[]
    for bi,(b,p) in enumerate(zip(state['blocks'],proofs)):
        for u,v,w in summary(b['nodes'],p,b['boundary']):
            edges.append([u,v,w]);path=p['paths'][b['nodes'].index(u)][b['nodes'].index(v)]
            expansions.append([['block',bi,k] for k in path])
    for k,e in enumerate(state['exterior']):edges.append(e);expansions.append([['exterior',k]])
    combined=closure(nodes,edges);packet.update(composed=combined,interface_nodes=nodes,status=combined['status'])
    if combined['status']=='INCONSISTENT':
        packet['expanded_cycle']=[entry for k in combined['cycle'] for entry in expansions[k]]
        return None,packet
    public_rows=summary(nodes,combined,state['public']);packet['summary']=public_rows
    live=LiveState(state['m'],state['binding'],state['public'],public_rows,state['retention'],digest(state),state if state['retention']=='archive-backed' else None)
    return live,packet

@dataclass(frozen=True)
class LiveState:
    m: int
    binding: str
    public: tuple
    rows: tuple
    policy: str
    origin: str
    _archive: object
    def __init__(self,m,binding,public,rows,policy,origin,archive):
        values={'m':m,'binding':binding,'public':tuple(public),'rows':tuple(tuple(e) for e in rows),
                'policy':policy,'origin':origin,'_archive':copy.deepcopy(archive)}
        for key,value in values.items():object.__setattr__(self,key,value)
    def contains(self,values):
        if len(values)!=len(self.public):raise ValueError('PUBLIC_ARITY')
        y=dict(zip(self.public,map(rational,values)))
        return y[0]==0 and all(y[v]-y[u]<=Q(w) for u,v,w in self.rows)
    def descriptor(self):
        return {'m':self.m,'binding':self.binding,'public':list(self.public),'summary':[list(e) for e in self.rows],
                'retention':self.policy,'origin_digest':self.origin}
    def expose(self,requested):
        if any(type(v) is not int or not 0<=v<=self.m for v in requested):raise ValueError('INVALID_NODE')
        if set(requested)<=set(self.public):return self,None
        if self._archive is None:raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        state=copy.deepcopy(self._archive);state['public']=sorted(set(self.public)|set(requested))
        for b in state['blocks']:b['boundary']=sorted(set(b['boundary'])|(set(requested)&set(b['nodes'])))
        return compile_state(state)
    def fill(self,values):
        if self._archive is None:raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        if len(values)!=len(self.public):raise ValueError('PUBLIC_ARITY')
        y=dict(zip(self.public,map(rational,values)))
        if y[0]!=0 or any(y[v]-y[u]>Q(w) for u,v,w in self.rows):raise ValueError('PUBLIC_POINT_EXCLUDED')
        _,p=compile_state(self._archive);nodes=p['interface_nodes'];D=p['composed']['distance']
        boundary={v:min(y[a]+Q(D[nodes.index(a)][nodes.index(v)]) for a in self.public) for v in nodes}
        source={}
        for b,proof in zip(self._archive['blocks'],p['blocks']):
            for v in b['nodes']:
                value=min(boundary[a]+Q(proof['distance'][b['nodes'].index(a)][b['nodes'].index(v)]) for a in b['boundary'])
                if v in source:assert source[v]==value
                source[v]=value
        return [str(source[v]) for v in range(self.m+1)]

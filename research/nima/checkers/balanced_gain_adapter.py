"""Certified chart adapter; raw atom semantics, normalized difference backend."""
from fractions import Fraction as Q
import copy
from modular_difference_interfaces import canonical,compile_state,digest,rational

def validate(raw):
    state=copy.deepcopy(raw);probe=copy.deepcopy(raw)
    for block,p in zip(state['blocks'],probe['blocks']):
        p['evidence']=[];normalized=[]
        for u,v,g,b in block['evidence']:
            g,b=rational(g),rational(b)
            if g<=0 or u==0 or v==0:raise ValueError('POSITIVE_GAIN_ON_RAW_ATOMS_REQUIRED')
            normalized.append([u,v,str(g),str(b)]);p['evidence'].append([u,v,str(b)])
        block['evidence']=normalized
    probe['exterior']=[];exterior=[]
    for u,v,g,b in state['exterior']:
        g,b=rational(g),rational(b)
        if g<=0 or u==0 or v==0:raise ValueError('POSITIVE_GAIN_ON_RAW_ATOMS_REQUIRED')
        exterior.append([u,v,str(g),str(b)]);probe['exterior'].append([u,v,str(b)])
    state['exterior']=exterior;canonical(probe)
    return state

def gain_rows(state):return [row for b in state['blocks'] for row in b['evidence']]+state['exterior']
def chart(state):
    m=state['m'];rows=gain_rows(state);adj={v:[] for v in range(1,m+1)}
    for k,(u,v,g,b) in enumerate(rows):
        adj[u].append((v,Q(g),k,1));adj[v].append((u,1/Q(g),k,-1))
    scales={0:Q(1)};paths={};components=[]
    for root in range(1,m+1):
        if root in scales:continue
        scales[root]=Q(1);paths[root]=[];todo=[root];component=[]
        while todo:
            u=todo.pop();component.append(u)
            for v,g,k,sign in adj[u]:
                proposed=scales[u]*g
                if v not in scales:
                    scales[v]=proposed;paths[v]=paths[u]+[[k,sign]];todo.append(v)
                elif scales[v]!=proposed:
                    cycle=paths[u]+[[k,sign]]+[[edge,-s] for edge,s in reversed(paths[v])]
                    return None,cycle
        components.append(component)
    for component in components:
        minimum=min(scales[v] for v in component)
        for v in component:scales[v]/=minimum
    return [scales[v] for v in range(m+1)],None

def normalize(state,scales):
    normalized=copy.deepcopy(state);normalized['binding']='balanced-gain-chart-v1:'+digest(state)
    for block in normalized['blocks']:
        caps=[[0,v,str(Q(98+2*v)/scales[v])] for v in block['nodes'] if v]
        block['evidence']=caps+[[u,v,str(Q(b)/scales[v])] for u,v,g,b in block['evidence']]
    normalized['exterior']=[[u,v,str(Q(b)/scales[v])] for u,v,g,b in normalized['exterior']]
    # Canonical component scales >=1 make the engine's original cap rows
    # redundant. Explicit tighter caps supply exactly the scaled source box.
    assert all(s>=1 for s in scales)
    return normalized

def compile_gain(raw):
    state=validate(raw);scales,cycle=chart(state)
    packet={'state':state,'state_digest':digest(state)}
    if cycle is not None:
        packet.update(status='UNSUPPORTED',reason='UNBALANCED_CHART',gain_cycle=cycle);return None,packet
    normalized=normalize(state,scales);live,proof=compile_state(normalized)
    packet.update(status=proof['status'],scales=list(map(str,scales)),normalized=proof)
    return (GainLive(live,scales,state) if live is not None else None),packet

class GainLive:
    def __init__(self,live,scales,state):
        self._live=live;self.scales=tuple(scales);self.public=live.public
        self._archive=copy.deepcopy(state) if live.policy=='archive-backed' else None
        self.origin=digest(state);self.policy=live.policy
    def contains(self,raw_values):
        if len(raw_values)!=len(self.public):raise ValueError('PUBLIC_ARITY')
        return self._live.contains([rational(v)/self.scales[k] for k,v in zip(self.public,raw_values)])
    def fill(self,raw_values):
        if len(raw_values)!=len(self.public):raise ValueError('PUBLIC_ARITY')
        z=self._live.fill([rational(v)/self.scales[k] for k,v in zip(self.public,raw_values)])
        return [str(Q(v)*s) for v,s in zip(z,self.scales)]
    def audit(self,node,threshold):
        if type(node) is not int or node not in self.public or node==0:raise ValueError('UNEXPOSED_RAW_ATOM')
        h=rational(threshold);rows={(u,v):Q(w) for u,v,w in self._live.rows}
        lo=-self.scales[node]*rows[node,0];hi=self.scales[node]*rows[0,node]
        return {'node':node,'threshold':str(h),'interval':[str(lo),str(hi)],
                'status':'FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED'}
    def expose(self,requested):
        requested=tuple(requested)
        if any(type(v) is not int or not 0<=v<=self._live.m for v in requested):raise ValueError('INVALID_NODE')
        if set(requested)<=set(self.public):return self,None
        if self._archive is None:raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        state=copy.deepcopy(self._archive);state['public']=sorted(set(state['public'])|set(requested))
        for b in state['blocks']:b['boundary']=sorted(set(b['boundary'])|(set(requested)&set(b['nodes'])))
        return compile_gain(state)

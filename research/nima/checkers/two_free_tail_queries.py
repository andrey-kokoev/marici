"""Exact, refinement-closed threshold queries with two free source atoms.

Measurement boxes concern full (U,V), in the original normalization. Pins
are exact supplied hypotheses, not observations inferred from a witness.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from check_symbolic_tail_interface import polygon_vertices,dual,farkas,dot,exact_rational,observable_pair,canonical_digest

@dataclass(frozen=True)
class TwoFreeTail:
    m: int
    free: tuple
    pins: tuple
    source_binding: str
    evidence: tuple = ()
    def __post_init__(self):
        if type(self.m) is not int or self.m<2:raise ValueError('INVALID_SIZE')
        free=tuple(self.free)
        if len(free)!=2 or any(type(i) is not int or not 0<=i<self.m for i in free) or not free[0]<free[1]:raise ValueError('INVALID_FREE_PAIR')
        pins=tuple(sorted((j,exact_rational(v)) for j,v in self.pins))
        if any(type(j) is not int for j,v in pins) or [j for j,v in pins]!=[j for j in range(self.m) if j not in free]:raise ValueError('INCOMPLETE_OR_DUPLICATE_PINS')
        if any(not 0<=v<=100+2*j for j,v in pins):raise ValueError('PIN_OUTSIDE_SOURCE')
        if type(self.source_binding) is not str or not self.source_binding:raise ValueError('INVALID_BINDING')
        evidence=[]
        for kind,a,b in self.evidence:
            a=observable_pair(a)
            if kind=='measurement_box':
                b=observable_pair(b)
                if min(b)<0:raise ValueError('NEGATIVE_ERROR')
            elif kind=='free_halfspace':b=exact_rational(b)
            else:raise ValueError('UNSUPPORTED_EVIDENCE')
            evidence.append((kind,a,b))
        object.__setattr__(self,'free',free);object.__setattr__(self,'pins',pins);object.__setattr__(self,'evidence',tuple(evidence))
    def measure(self,center,error):
        return TwoFreeTail(self.m,self.free,self.pins,self.source_binding,self.evidence+(('measurement_box',center,error),))
    def refine(self,normal,upper):
        return TwoFreeTail(self.m,self.free,self.pins,self.source_binding,self.evidence+(('free_halfspace',normal,upper),))
    def descriptor(self):
        events=[]
        for kind,a,b in self.evidence:
            events.append({'kind':kind,'center':list(map(str,a)),'error':list(map(str,b))} if kind=='measurement_box'
                          else {'kind':kind,'normal':list(map(str,a)),'upper':str(b)})
        return {'schema':'two-free-tail-state-v1','source_rule':'cap=100+2j;slope=128^-j;0<=j<m',
                'source_binding':self.source_binding,'m':self.m,'free':list(self.free),
                'pins':[[j,str(v)] for j,v in self.pins],'evidence':events}
    def rows(self):
        i,j=self.free;r,s=Q(1,128**i),Q(1,128**j)
        rows=[((Q(-1),Q(0)),Q(0)),((Q(1),Q(0)),Q(100+2*i)),
              ((Q(0),Q(-1)),Q(0)),((Q(0),Q(1)),Q(100+2*j))]
        offset=(sum((v for k,v in self.pins),Q(0)),sum((v*Q(1,128**k) for k,v in self.pins),Q(0)))
        for kind,a,b in self.evidence:
            if kind=='free_halfspace':rows.append((a,b));continue
            for n,center,error,shift in zip(((Q(1),Q(1)),(r,s)),a,b,offset):
                rows.extend([(n,center+error-shift),(tuple(-x for x in n),-center+error+shift)])
        return rows
    def audit(self,threshold):
        h=exact_rational(threshold);rows=self.rows();vertices=polygon_vertices(rows)
        if not vertices:result={'status':'INCONSISTENT','farkas':farkas(rows)}
        else:
            endpoints=[]
            for objective in ((Q(-1),Q(0)),(Q(1),Q(0))):
                point=max(vertices,key=lambda x:(dot(objective,x),tuple(-v for v in x)))
                endpoints.append({'point':list(map(str,point)),'value':str(dot(objective,point)),
                                  'dual':dual(rows,objective,point)})
            lo=-Q(endpoints[0]['value']);hi=Q(endpoints[1]['value'])
            status='FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED'
            result={'status':status,'interval':[str(lo),str(hi)],'minimum':endpoints[0],'maximum':endpoints[1]}
        state=self.descriptor();query={'kind':'free-atom-threshold','atom':self.free[0],'relation':'<=','threshold':str(h)}
        sd=canonical_digest(state)
        return {'schema':'two-free-tail-certificate-v1','state':state,'query':query,'state_digest':sd,
                'query_digest':canonical_digest({'state_digest':sd,'query':query}),'result':result}

"""Generator-based exact support, membership and lazy refined optimization."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from dataclasses import dataclass
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def encpoint(x):return list(map(str,x))

class Generator:
    """Persistent source description: m only; no cap, slope or facet arrays."""
    def __init__(self,m):assert type(m) is int and m>=2;self.m=m
    @staticmethod
    def mass(k):return Q(k*(k+99))
    @staticmethod
    def weighted(k):
        q=Q(1,128);power=q**k
        return 100*(1-power)/(1-q)+2*(q-k*power+(k-1)*power*q)/(1-q)**2
    def support(self,a):
        if len(a)!=2:raise ValueError('UNDECLARED_OBSERVABLE')
        left,right=0,self.m
        if a[1]>0:
            while left<right:
                mid=(left+right)//2
                if a[0]+a[1]*Q(1,128**mid)>0:left=mid+1
                else:right=mid
            lo,hi=0,left
        elif a[1]<0:
            while left<right:
                mid=(left+right)//2
                if a[0]+a[1]*Q(1,128**mid)>0:right=mid
                else:left=mid+1
            lo,hi=left,self.m
        else:lo,hi=(0,self.m) if a[0]>0 else (0,0)
        point=(self.mass(hi)-self.mass(lo),self.weighted(hi)-self.weighted(lo))
        return {'normal':encpoint(a),'upper':str(dot(a,point)),'positive_interval':[lo,hi],'point':encpoint(point)}
    def greedy(self,u):
        assert 0<=u<=self.mass(self.m)
        left,right=0,self.m
        while left<right:
            mid=(left+right+1)//2
            if self.mass(mid)<=u:left=mid
            else:right=mid-1
        k=left;remainder=u-self.mass(k)
        value=self.weighted(k)+(Q(1,128**k)*remainder if k<self.m else 0)
        return k,remainder,value
    def member(self,point):
        if len(point)!=2:raise ValueError('UNDECLARED_OBSERVABLE')
        u,v=point;total=self.mass(self.m)
        if u<0:return {'admitted':False,'separator':self.support((Q(-1),Q(0)))}
        if u>total:return {'admitted':False,'separator':self.support((Q(1),Q(0)))}
        high_k,high_partial,high=self.greedy(u)
        complement_k,complement_partial,complement=self.greedy(total-u)
        low=self.weighted(self.m)-complement
        if v>high:
            j=min(high_k,self.m-1);return {'admitted':False,'separator':self.support((-Q(1,128**j),Q(1)))}
        if v<low:
            j=min(complement_k,self.m-1);return {'admitted':False,'separator':self.support((Q(1,128**j),Q(-1)))}
        theta=(v-low)/(high-low) if high!=low else Q(0)
        return {'admitted':True,'lift':{'high_prefix':high_k,'high_partial':str(high_partial),
          'complement_prefix':complement_k,'complement_partial':str(complement_partial),'theta':str(theta)},
          'vertical_bounds':[str(low),str(high)]}

def polygon_vertices(rows):
    out=set()
    for (a,b),(c,d) in combinations(rows,2):
        den=a[0]*c[1]-a[1]*c[0]
        if not den:continue
        x=((b*c[1]-a[1]*d)/den,(a[0]*d-b*c[0])/den)
        if all(dot(n,x)<=v for n,v in rows):out.add(x)
    return sorted(out)
def dual(rows,objective,point):
    target=dot(objective,point)
    if objective==(Q(0),Q(0)):return []
    active=[i for i,(a,b) in enumerate(rows) if dot(a,point)==b]
    for i in active:
        a,b=rows[i];j=next((j for j in (0,1) if a[j]),None)
        if j is None:continue
        z=objective[j]/a[j]
        if z>=0 and tuple(z*v for v in a)==objective:return [[i,str(z)]]
    for i,j in combinations(active,2):
        a,b=rows[i];c,d=rows[j];den=a[0]*c[1]-c[0]*a[1]
        if not den:continue
        x=(objective[0]*c[1]-c[0]*objective[1])/den;y=(a[0]*objective[1]-objective[0]*a[1])/den
        if min(x,y)>=0 and x*b+y*d==target:return [[i,str(x)],[j,str(y)]]
    raise AssertionError('missing exact dual')
def farkas(rows):
    for i,(a,b) in enumerate(rows):
        if not any(a) and b<0:return [[i,'1']]
    for i,j in combinations(range(len(rows)),2):
        a,b=rows[i];c,d=rows[j];k=next((k for k in (0,1) if c[k]),None)
        if k is None:continue
        t=-a[k]/c[k]
        if t>=0 and tuple(a[k]+t*c[k] for k in (0,1))==(0,0) and b+t*d<0:return [[i,'1'],[j,str(t)]]
    for i,j,k in combinations(range(len(rows)),3):
        a,b=rows[i];c,d=rows[j];e,f=rows[k]
        # Cross-product null vector of the 2x3 normal matrix.
        v=(c[0]*e[1]-e[0]*c[1],e[0]*a[1]-a[0]*e[1],a[0]*c[1]-c[0]*a[1])
        if max(v)<=0:v=tuple(-x for x in v)
        if min(v)>=0 and any(v) and v[0]*b+v[1]*d+v[2]*f<0:return [[n,str(z)] for n,z in zip((i,j,k),v) if z]
    raise AssertionError('missing exact Farkas certificate')

def lazy_maximize(model,frames,objective):
    if len(objective)!=2 or any(len(a)!=2 for a,b in frames):raise ValueError('UNDECLARED_OBSERVABLE')
    # A feasible unrestricted support witness already attains a global upper
    # bound. Do not walk all tied outer vertices to rediscover that witness.
    support=model.support(objective);point=tuple(map(Q,support['point']))
    if all(dot(a,point)<=b for a,b in frames):
        membership=model.member(point);assert membership['admitted']
        rows=[{'a':support['normal'],'b':support['upper'],'kind':'source','support':support}]
        rows += [{'a':encpoint(a),'b':str(b),'kind':'frame'} for a,b in frames]
        return {'status':'OPTIMAL','rows':rows,'cuts':[],'point':encpoint(point),'value':support['upper'],
                'lift':membership['lift'],'dual':[[0,'1']],'source_facets_generated':0,'path':'feasible_global_support'}
    records=[]
    for a in ((Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))):
        s=model.support(a);records.append({'a':s['normal'],'b':s['upper'],'kind':'source','support':s})
    for a,b in frames:records.append({'a':encpoint(a),'b':str(b),'kind':'frame'})
    cuts=[]
    while True:
        rows=[(tuple(map(Q,r['a'])),Q(r['b'])) for r in records];vertices=polygon_vertices(rows)
        if not vertices:
            return {'status':'INCONSISTENT','rows':records,'cuts':cuts,'dual':farkas(rows),'source_facets_generated':len(cuts)}
        point=max(vertices,key=lambda x:(dot(objective,x),tuple(-v for v in x)))
        membership=model.member(point)
        if membership['admitted']:
            return {'status':'OPTIMAL','rows':records,'cuts':cuts,'point':encpoint(point),'value':str(dot(objective,point)),
              'lift':membership['lift'],'dual':dual(rows,objective,point),'source_facets_generated':len(cuts)}
        s=membership['separator'];a=tuple(map(Q,s['normal']));b=Q(s['upper'])
        assert dot(a,point)>b and (a,b) not in rows
        cuts.append({'rejected_point':encpoint(point),'support':s})
        records.append({'a':s['normal'],'b':s['upper'],'kind':'source','support':s})
        assert len(cuts)<=2*model.m

SOURCE_RULE={'cap':'100+2j','slope':'128^-j','range':'0<=j<m'}
def exact_rational(value):
    if type(value) not in (int,str,Q):raise ValueError('EXACT_RATIONAL_REQUIRED')
    try:return Q(value)
    except (ValueError,ZeroDivisionError) as error:raise ValueError('INVALID_RATIONAL') from error
def observable_pair(values):
    if not isinstance(values,(tuple,list)) or len(values)!=2:raise ValueError('UNDECLARED_OBSERVABLE')
    return tuple(exact_rational(v) for v in values)
def canonical_digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

@dataclass(frozen=True)
class RetainedInterface:
    m: int
    frames: tuple = ()
    source_binding: str = 'normalized-tail-box-v1'
    def __post_init__(self):
        if type(self.m) is not int or self.m<2:raise ValueError('INVALID_SOURCE_SIZE')
        if type(self.source_binding) is not str or not self.source_binding:raise ValueError('INVALID_SOURCE_BINDING')
        # Normalize and copy caller-owned containers; a frozen outer object
        # alone would not prevent mutation of nested input lists.
        normalized=tuple((observable_pair(a),exact_rational(b)) for a,b in self.frames)
        object.__setattr__(self,'frames',normalized)
    def refine(self,normal,upper):
        frame=(observable_pair(normal),exact_rational(upper))
        return RetainedInterface(self.m,self.frames+(frame,),self.source_binding)
    def descriptor(self):
        return {'schema':'retained-tail-state-v1','source_rule':dict(SOURCE_RULE),'source_binding':self.source_binding,
                'm':self.m,'frames':[{'a':encpoint(a),'b':str(b)} for a,b in self.frames]}
    def _certificate(self,query,result):
        state=self.descriptor();state_digest=canonical_digest(state)
        return {'schema':'state-bound-tail-query-v1','state':state,'state_digest':state_digest,'query':query,
                'query_digest':canonical_digest({'state_digest':state_digest,'query':query}),'result':result}
    def member(self,point):
        point=observable_pair(point);query={'kind':'point-membership','point':encpoint(point)}
        for index,(a,b) in enumerate(self.frames):
            lhs=dot(a,point)
            if lhs>b:
                return self._certificate(query,{'admitted':False,'reason':'RETAINED_FRAME','frame_index':index,'lhs':str(lhs),'upper':str(b)})
        answer=Generator(self.m).member(point)
        answer={**answer,'reason':'SOURCE_LIFT' if answer['admitted'] else 'SOURCE_SEPARATOR'}
        return self._certificate(query,answer)
    def maximize(self,objective):
        return lazy_maximize(Generator(self.m),self.frames,observable_pair(objective))
    def certify_maximum(self,objective):
        objective=observable_pair(objective)
        return self._certificate({'kind':'linear-maximum','objective':encpoint(objective)},self.maximize(objective))

def main():
    source_path=ROOT/'grothendieck/results/two-moment-tail-complexity.json';source=load(source_path)
    contract={'schema':'symbolic-tail-interface-v1','source_sha256':sha(source_path),
      'source_rule':{'cap':'100+2j','slope':'128^-j','range':'0<=j<m'},
      'base_representation':'Fixed generator program plus m and source binding. No persistent facet, vertex, cap or slope arrays.',
      'queries':['exact linear support','point membership with a source lift or separating support','persistent observable halfspaces followed by linear maximization or inconsistency'],
      'support_rule':'Find the positive coefficient interval by monotonicity and evaluate two closed finite sums.',
      'membership_rule':'Greedy high/low slope allocations at fixed U give the exact V interval; interpolate the two source allocations.',
      'refinement_rule':'Retain every frame. Start with four source support bounds; generate a separating source facet only when an outer optimum has no source lift.',
      'bounds':{'source_cuts_per_query':'at most 2m','outer_rows':'at most 4+number_of_frames+2m','dual_nonzeros':2,'farkas_nonzeros':3,
        'tested_m':[2,3,4,8,16,64,256,1024],'tested_rational_bits':16384},
      'limitations':'Exact rational bit lengths and query time may grow with m. Arbitrary refinements can force many generated cuts. All accumulated frames and returned certificates count as information.',
      'scope':'Owning admitted tail faces and exact normalized two-moment geometry. Not prime-realizability or a full-tail midpoint certificate.'}
    cp=OUT/'symbolic-tail-interface-contract.json';save(cp,contract)
    support_tests=[];membership_tests=[];refinement_tests=[];reset_controls=[]
    def support_case(model,a):
        result=model.support(a);support_tests.append({'m':model.m,'result':result});return result
    def member_case(model,point,expected=None):
        result=model.member(point)
        if expected is not None:assert result['admitted']==expected
        membership_tests.append({'m':model.m,'point':encpoint(point),'result':result});return result
    for family in source['families']:
        model=Generator(family['m']);facets=family['facets']
        for facet in facets:
            normal=tuple(map(Q,facet['normal']));answer=support_case(model,normal);assert Q(answer['upper'])==Q(facet['upper'])
            for v in facet['edge_endpoints']:member_case(model,tuple(map(Q,v)),True)
            member_case(model,tuple(map(Q,facet['omission_witness'])),False)
        for a in ((Q(1),Q(1)),(Q(-1),Q(-1)),(Q(1),Q(-1)),(Q(-1),Q(1))):support_case(model,a)
    for m in contract['bounds']['tested_m']:
        model=Generator(m);total=model.mass(m)
        for a in ((Q(1),Q(0)),(Q(0),Q(1)),(-Q(1,128**(m//2)),Q(1)),(Q(1,128**(m-1)),Q(-1))):support_case(model,a)
        for u in (Q(0),Q(50),total/3,total):
            hi=model.greedy(u)[2];lo=model.weighted(m)-model.greedy(total-u)[2]
            member_case(model,(u,(lo+hi)/2),True)
            member_case(model,(u,hi+1),False);member_case(model,(u,lo-1),False)
        member_case(model,(Q(-1),Q(0)),False);member_case(model,(total+1,Q(0)),False)
        # The same persistent tests are used at small and large m.
        traces=[('source-dependent',[((Q(1),Q(0)),Q(50)),((Q(-1),Q(0)),Q(-25)),((Q(0),Q(-1)),Q(-75))]),
          ('coupled-refinement',[((Q(1),Q(0)),Q(50)),((-Q(1,2),Q(1)),Q(0)),((Q(0),Q(-1)),Q(-30))])]
        for name,trace in traces:
            state=RetainedInterface(m)
            for index,(normal,upper) in enumerate(trace):
                previous=state;state=state.refine(normal,upper);assert len(previous.frames)==index
                frames=state.frames;answer=state.maximize((Q(0),Q(1)))
                assert (answer['status']=='INCONSISTENT')==(index==2)
                if index<2:assert Q(answer['value'])==(25 if name=='coupled-refinement' and index==1 else 50)
                refinement_tests.append({'m':m,'trace':name,'stage':index+1,'frames':[{'a':encpoint(a),'b':str(b)} for a,b in frames],
                                         'objective':['0','1'],'result':answer})
        # Resetting to just the final frame incorrectly makes both chains feasible.
        for name,trace in traces:
            answer=lazy_maximize(model,[trace[-1]],(Q(0),Q(1)));assert answer['status']=='OPTIMAL'
            a,b=trace[-1]
            reset_controls.append({'m':m,'trace':name,'frames':[{'a':encpoint(a),'b':str(b)}],
                                   'objective':['0','1'],'result':answer})
    try:lazy_maximize(Generator(2),[((Q(0),Q(0),Q(1)),Q(0))],(Q(0),Q(1)))
    except ValueError as error:assert str(error)=='UNDECLARED_OBSERVABLE'
    else:raise AssertionError('undeclared coordinate accepted')
    packet={'support_queries':support_tests,'membership_queries':membership_tests,'refinement_queries':refinement_tests,'reset_controls':reset_controls,
      'lift_decoder':'t_j=(1-theta)*(cap_j-high(T-U)_j)+theta*high(U)_j; a high descriptor fills its prefix, then its partial slot, then zero.',
      'source_program_state':{'fields':['m'],'fixed_rule':contract['source_rule']}}
    # Check exact output arithmetic sizes; do not call them constant-space.
    peak=0
    def scan(x):
        nonlocal peak
        if isinstance(x,dict):
            for v in x.values():scan(v)
        elif isinstance(x,list):
            for v in x:scan(v)
        elif isinstance(x,str):
            try:v=Q(x)
            except (ValueError,ZeroDivisionError):return
            peak=max(peak,abs(v.numerator).bit_length(),v.denominator.bit_length())
    scan(packet);assert peak<=16384
    pp=OUT/'symbolic-tail-interface-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
    result={'verdict':'GENERATOR_AND_LAZY_CERTIFICATES_PASS','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'support_queries':len(support_tests),'membership_queries':len(membership_tests),'persistent_refinement_queries':len(refinement_tests),
      'largest_m':1024,'necessary_original_space_facets_at_largest_m':2048,
      'maximum_source_facets_generated_in_tested_refined_queries':max(t['result']['source_facets_generated'] for t in refinement_tests),
      'largest_exported_rational_bits':peak,
      'conclusion':'Exact declared queries can use the source generator and query-specific certificates rather than materialize the full residual polygon.',
      'scope':contract['scope'],'limitations':contract['limitations']}
    assert sha(source_path)==contract['source_sha256'];save(OUT/'symbolic-tail-interface.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()

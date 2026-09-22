"""Real interval task certification with an explicit order-16 source prior.

CLI: uv run python <this-file> task.json
Input: mode, raw {positive,crossed,vacuum:{center: rational, radius: rational}},
optional budget (default 2621440), optional witness with three rational source
coefficients, and auto_witness (default false). An optional second CLI argument
selects a certified refinement bundle. Automatic witnesses use INNER intervals;
no witness is inferred from passing the necessary outer-box budget test.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys

RESULTS=Path(__file__).resolve().parents[1]/'results'
NAMES=('positive','crossed','vacuum');WEIGHTS={'positive':32,'crossed':32,'vacuum':8}
ORDER=16;DEFAULT_BUDGET=Q(40*2**ORDER)

def rational(value):
    if isinstance(value,(float,bool)):raise ValueError('Use exact rational strings or integers, not floats/bools')
    return Q(value)
def pair(value):return Q(int(value[0]),int(value[1]))
def interval(data):
    if set(data)!={'center','radius'}:raise ValueError('Intervals require center and radius')
    c=rational(data['center']);r=rational(data['radius'])
    if r<0:raise ValueError('Negative interval radius')
    return c-r,c+r

def divide(x,y):
    if y[0]<=0:raise ValueError('Positive calibration lower bound required')
    values=[a/b for a in x for b in y]
    return min(values),max(values)
def multiply(x,y):
    values=[a*b for a in x for b in y]
    return min(values),max(values)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def minimum_abs(x):return Q(0) if x[0]<=0<=x[1] else min(abs(x[0]),abs(x[1]))
def robust_inner(data,calibration):
    l,u=calibration
    if not 0<l<=u:raise ValueError('Invalid positive calibration interval')
    a=(data[0]/l,data[1]/l);b=(data[0]/u,data[1]/u)
    lo=max(a[0],b[0]);hi=min(a[1],b[1])
    return None if lo>hi else (lo,hi)
def closest_to_zero(x):
    return Q(0) if x[0]<=0<=x[1] else min(x,key=abs)
def scale(x,a):return multiply(x,(a,a))
def contains(outer,inner):return outer[0]<=inner[0] and inner[1]<=outer[1]

def outward_decimal(q,places,up):
    scaled=q*10**places
    n=-((-scaled.numerator)//scaled.denominator) if up else scaled.numerator//scaled.denominator
    sign='-' if n<0 else '';n=abs(n);base=10**places
    return f'{sign}{n//base}.{n%base:0{places}d}'
def describe(x):
    return {'lower_rational':str(x[0]),'upper_rational':str(x[1]),
            'lower_decimal':outward_decimal(x[0],8,False),
            'upper_decimal':outward_decimal(x[1],8,True)}

class SourceTask:
    def __init__(self,calibration_path=RESULTS/'three-channel-source-task-calibration.json'):
        path=Path(calibration_path)
        self.cal=json.loads(path.read_text(encoding='utf-8'))
        if self.cal.get('schema')!='marici.grothendieck.three-channel-source-task-calibration.v1':
            raise ValueError('Unknown task calibration schema')
        protocol_path=path.parent/self.cal['protocol_file']
        raw=protocol_path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=self.cal['protocol_sha256']:raise ValueError('Stale task calibration')
        self.protocol=json.loads(raw)
        parameters=self.protocol['parameters']
        if (parameters['A'],parameters['y'],parameters['gamma'])!=(2,3,1):
            raise ValueError('This task calibration requires A=2, y=3, gamma=1')
        if hashlib.sha256((path.parent/self.protocol['filter_manifest']).read_bytes()).hexdigest()!=self.protocol['filter_manifest_sha256']:
            raise ValueError('Stale bin-filter protocol')
        self.sigma={n:tuple(pair(self.cal['source_functional'][n][k]) for k in ('lower','upper'))
                    for n in ('positive','crossed')}
        self.tail_multiplier=pair(self.cal['residual_tail_multiplier_upper'])
        assert self.tail_multiplier>0
        self.refinements=self.cal.get('diagonal_refinements',{})
        if self.refinements:
            parent_path=path.parent/self.cal['parent_calibration_file']
            if hashlib.sha256(parent_path.read_bytes()).hexdigest()!=self.cal['parent_calibration_sha256']:
                raise ValueError('Stale refinement parent')
            self.parent=SourceTask(parent_path)
            if (self.cal['protocol_sha256']!=self.parent.cal['protocol_sha256'] or
                self.cal['source_domain']!=self.parent.cal['source_domain'] or
                self.tail_multiplier>self.parent.tail_multiplier):
                raise ValueError('Refinement changes the protocol or weakens the tail bound')
            if any(not contains(self.parent.sigma[n],self.sigma[n]) for n in self.sigma):
                raise ValueError('Source-functional enclosure is not a refinement')
            if set(self.refinements)-{'private','reuse'}:raise ValueError('Unknown refinement mode')
            for mode in self.refinements:self.calibrations(mode)

    def calibrations(self,mode):
        if mode not in ('private','reuse'):raise ValueError('Choose private or reuse mode')
        channels=dict(self.protocol['channels'])
        if mode=='reuse':channels['crossed']=self.protocol['modes']['reuse']['crossed_channel']
        base={n:(pair(channels[n]['forward_gain_lower']),pair(channels[n]['forward_gain_upper'])) for n in NAMES}
        if self.refinements:base=self.parent.calibrations(mode)
        if mode in self.refinements:
            refined=self.refinements[mode]
            if set(refined)!=set(NAMES):raise ValueError('Incomplete diagonal refinement')
            parent=self.parent.calibrations(mode)
            for n in NAMES:
                value=tuple(pair(refined[n][k]) for k in ('lower','upper'))
                if not 0<value[0]<=value[1] or not contains(base[n],value) or not contains(parent[n],value):
                    raise ValueError('Non-nested or invalid calibration refinement')
                base[n]=value
        return base

    def certify(self,data):
        if set(data)-{'mode','raw','budget','witness','auto_witness'}:
            raise ValueError('Unsupported task fields; the acquired background and moment order are fixed')
        auto=data.get('auto_witness',False)
        if not isinstance(auto,bool):raise ValueError('auto_witness must be a boolean')
        mode=data.get('mode','private');E=self.calibrations(mode)
        if set(data['raw'])!=set(NAMES):raise ValueError('All three raw intervals required')
        raw={n:interval(data['raw'][n]) for n in NAMES}
        budget=rational(data.get('budget',str(DEFAULT_BUDGET)))
        if budget<0:raise ValueError('Negative source budget')
        boxes={n:divide(raw[n],E[n]) for n in NAMES}
        components={n:2**ORDER*WEIGHTS[n]*minimum_abs(boxes[n]) for n in NAMES}
        lower=sum(components.values(),Q(0))
        result={'mode':mode,'status':'UNRESOLVED',
                'source_domain':self.cal['source_domain'],'acquired_background':2,'receiver_gamma':1,
                'prior':{'moment_order':ORDER,'budget':str(budget),
                         'formula':'sum_(integer A>=2) A^16 [32 sum_(j=0)^269 |a_(A,j)|+8|b_A|] <= budget'},
                'necessary_moment_cost_lower_bound':str(lower),
                'necessary_cost_by_channel':{n:str(v) for n,v in components.items()},
                'coefficient_outer_boxes':{n:describe(v) for n,v in boxes.items()}}
        if lower>budget:
            result.update(status='CERTIFIED_INFEASIBLE',
                          contradiction='The joint necessary source cost exceeds the declared budget.',
                          excess_lower_bound=str(lower-budget))
            return result
        if 'witness' in data:
            if set(data['witness'])!=set(NAMES):raise ValueError('Witness must name exactly three local source coefficients')
            witness={n:rational(data['witness'][n]) for n in NAMES}
            cost=2**ORDER*sum((WEIGHTS[n]*abs(witness[n]) for n in NAMES),Q(0))
            fits={n:contains(raw[n],scale(E[n],witness[n])) for n in NAMES}
            accepted=cost<=budget and all(fits.values())
            result['witness_check']={'accepted':accepted,'moment_cost':str(cost),
                                     'fits_for_every_calibration_value':fits,
                                     'coefficients_at_A2':{n:str(v) for n,v in witness.items()},
                                     'other_coefficients_and_backgrounds':'zero'}
            if accepted:
                result['status']='CERTIFIED_FEASIBLE';result['feasibility_witness_origin']='supplied'
        if auto and result['status']!='CERTIFIED_FEASIBLE':
            inner={n:robust_inner(raw[n],E[n]) for n in NAMES}
            search={'inner_boxes':{n:None if x is None else describe(x) for n,x in inner.items()},
                    'accepted':False}
            if all(x is not None for x in inner.values()):
                witness={n:closest_to_zero(inner[n]) for n in NAMES}
                cost=2**ORDER*sum((WEIGHTS[n]*abs(witness[n]) for n in NAMES),Q(0))
                fits={n:contains(raw[n],scale(E[n],witness[n])) for n in NAMES}
                assert all(fits.values())
                search.update(moment_cost=str(cost),coefficients_at_A2={n:str(v) for n,v in witness.items()},
                              fits_for_every_calibration_value=fits,other_coefficients_and_backgrounds='zero')
                if cost<=budget:
                    search['accepted']=True;result['status']='CERTIFIED_FEASIBLE'
                    result['feasibility_witness_origin']='robust_inner_intervals'
            result['automatic_witness_search']=search
        remaining=budget-lower
        tail_v=remaining/(8*3**ORDER)
        tail_r=remaining*self.tail_multiplier/(32*3**ORDER)
        local_v=boxes['vacuum']
        local_r=add(multiply(self.sigma['positive'],boxes['positive']),
                    multiply(self.sigma['crossed'],boxes['crossed']))
        aggregate_v=add(local_v,(-tail_v,tail_v))
        aggregate_r=add(local_r,(-tail_r,tail_r))
        positive=aggregate_v[0]>0 and aggregate_r[0]>0
        result.update(remaining_budget_upper_bound=str(remaining),
                      local_readout_enclosures={'vacuum':describe(local_v),'residual_per_w_squared':describe(local_r)},
                      tail_l1_upper_bounds={'vacuum_rational':str(tail_v),'residual_per_w_squared_rational':str(tail_r),
                                            'vacuum_decimal_upper':outward_decimal(tail_v,8,True),
                                            'residual_decimal_upper':outward_decimal(tail_r,8,True)},
                      joint_tail_region={'vacuum_weight':str(8*3**ORDER),
                                         'residual_weight':str(Q(32*3**ORDER)/self.tail_multiplier),
                                         'bound':str(remaining),
                                         'meaning':'vacuum_weight*sum_(A>=3)|u_A| + residual_weight*sum_(A>=3)|t_A| <= bound'},
                      aggregate_readout_enclosures={'vacuum':describe(aggregate_v),'residual_per_w_squared':describe(aggregate_r)},
                      conditional_aggregate_bounds_positive=positive,
                      nonvacuous_positive_task_certificate=bool(positive and result['status']=='CERTIFIED_FEASIBLE'),
                      scope='Universal outer bounds conditional on the stated raw intervals and source prior. Nonemptiness is certified only by an accepted witness; the rectangle need not be jointly attainable.')
        return result

if __name__=='__main__':
    if len(sys.argv) not in (2,3):raise SystemExit(__doc__)
    data=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    engine=SourceTask(sys.argv[2]) if len(sys.argv)==3 else SourceTask()
    print(json.dumps(engine.certify(data),indent=2))

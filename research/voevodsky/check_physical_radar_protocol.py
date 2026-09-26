"""Rational outward enclosures of physical null rays for the frozen radar protocol.
Wave: p=cosh(u/4), q=cos(u/4); flat moving control: p=q=1+u/4.
All certificate arithmetic is rational. Floats below are display-only.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt, factorial
from pathlib import Path
import hashlib
import json
from finite_radar_protocol import Protocol,Row,Packet,TIMES,DIRECTIONS,WEIGHTS,by_time,encode_section,on_native_section,flat_packet,error_bound

GRID=2**80
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        lo=F(self.lo);hi=F(self.hi)
        if lo>hi:raise ValueError('empty enclosure')
        object.__setattr__(self,'lo',F((lo*GRID).__floor__(),GRID))
        object.__setattr__(self,'hi',F((hi*GRID).__ceil__(),GRID))
    @staticmethod
    def of(x):return x if isinstance(x,I) else I(F(x),F(x))
    def __add__(self,x):
        x=I.of(x);return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,x):return self+-I.of(x)
    def __rsub__(self,x):return I.of(x)+-self
    def __mul__(self,x):
        x=I.of(x);ends=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(ends),max(ends))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.of(x)
        if x.lo<=0<=x.hi:raise ValueError('division through zero')
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x):return I.of(x)/self
    def __pow__(self,n):
        if n<0:return 1/(self**(-n))
        ans=I.of(1)
        for _ in range(n):ans=ans*self
        return ans
    def mid(self):return (self.lo+self.hi)/2
    def width(self):return self.hi-self.lo

def exp_pos(x):
    x=I.of(x)
    if x.lo<0 or x.hi>1:raise ValueError('exponential certificate domain')
    # Degree 24 Taylor polynomial; exp(x)<3 on [0,1], Lagrange remainder.
    term=I.of(1);out=term
    for k in range(1,25):
        term=term*x/k;out=out+term
    return out+I(F(0),3*x.hi**25/F(factorial(25)))

def sin_cos(x):
    x=I.of(x)
    if x.lo<0 or x.hi>F(1,2):raise ValueError('trigonometric certificate domain')
    # Taylor through degree 24; derivatives bounded by one, both remainders <=x^25/25!.
    sine=I.of(0);cosine=I.of(0);power=I.of(1)
    for k in range(25):
        if k%2:sine=sine+((-1)**((k-1)//2))*power/F(factorial(k))
        else:cosine=cosine+((-1)**(k//2))*power/F(factorial(k))
        power=power*x
    rem=x.hi**25/F(factorial(25));err=I(-rem,rem)
    return sine+err,cosine+err

def tan(x):
    s,c=sin_cos(x);return s/c

def tanh(x):
    e=exp_pos(2*I.of(x));return (e-1)/(e+1)

def sqrt_rational(x):
    x=F(x);k=isqrt((x*GRID*GRID).__floor__())
    ans=I(F(k,GRID),F(k+1,GRID))
    assert ans.lo**2<=x<=ans.hi**2
    return ans

A=F(1,4);SQRT2=sqrt_rational(2)
p=Protocol(F(1,32),F(1,4),F(1),'retained-Rosen-transverse-labels','central-proper-clock-c=1')
vectors={'x3':(3,0,3),'y4':(0,4,4),'xy5':(3,4,5)}
checks={};brackets=[]

def residual(t,h,bx,by):
    end=t+h
    sx=(tanh(A*end)-tanh(A*t))/A
    sy=(tan(A*end)-tan(A*t))/A
    return 2*I.of(h)-bx*bx/sx-by*by/sy

def wave_leg(t,direction):
    vx,vy,length=vectors[direction];bx=p.epsilon*vx;by=p.epsilon*vy;d=p.epsilon*length
    lo=d/2;hi=d
    f_lo=residual(t,lo,bx,by);f_hi=residual(t,hi,bx,by)
    assert f_lo.hi<0 and f_hi.lo>0
    for _ in range(48):
        mid=(lo+hi)/2;fm=residual(t,mid,bx,by)
        if fm.hi<0:lo=mid
        elif fm.lo>0:hi=mid
        else:
            # f'>=2 yields a root enclosure even with uncertain starting t.
            lo=max(lo,mid-max(fm.hi,F(0))/2)
            hi=min(hi,mid+max(-fm.lo,F(0))/2)
            break
    out=I(lo,hi)
    brackets.append(dict(start_width=str(t.width()),root_width=str(out.width()),direction=direction))
    return out

def moving_radius(t,direction):
    d=p.epsilon*vectors[direction][2]
    alpha=(A*d*d+sqrt_rational(A*A*d**4+8*d*d))/4
    # Exact h_out=(1+A*t)alpha; h_back=(1+A*t)(1+A*alpha)alpha.
    return (1+A*t)*alpha*(2+A*alpha)/SQRT2

def process_intervals(radii):
    q={k:(r/p.epsilon)**2 for k,r in radii.items()}
    shapes={t:(q[t,'x3']/9,(q[t,'xy5']-q[t,'x3']-q[t,'y4'])/24,q[t,'y4']/16) for t in TIMES}
    return tuple(-sum((WEIGHTS[t]*shapes[t][k] for t in TIMES),I.of(0))/(2*p.step**2) for k in range(3))

def encode_i(x):return dict(lo=str(x.lo),hi=str(x.hi),display=[float(x.lo),float(x.hi)])

sources={}
for source in ('vacuum-cosh-cos-initially-resting','flat-moving-isotropic-Rosen'):
    radii={};rows=[];clock_bounds=[]
    for j in TIMES:
        emission=p.center+j*p.step;t=I.of(emission)/SQRT2
        for direction in DIRECTIONS:
            if source.startswith('vacuum'):
                out=wave_leg(t,direction);back=wave_leg(t+out,direction)
                radius=(out+back)/SQRT2
            else:radius=moving_radius(t,direction)
            assert radius.lo>0
            radii[j,direction]=radius
            arrival=emission+2*radius
            rows.append(Row(j,direction,emission,arrival.mid()))
            clock_bounds.append(dict(time=j,direction=direction,emission=str(emission),reception=encode_i(arrival),rounded_reception=str(arrival.mid())))
    actual_y=process_intervals(radii)
    packet=Packet(p,tuple(rows),'certified-rounding:'+source)
    rounded_y=by_time(packet)
    sigma=max(r.width()/2 for r in radii.values());M=max(r.hi for r in radii.values())
    rounding_error=error_bound(p,M,sigma)
    checks[source+'_native_comparison']=on_native_section(encode_section(packet))==rounded_y
    checks[source+'_rounded_value_consistent']=all(x.lo-rounding_error<=y<=x.hi+rounding_error for x,y in zip(actual_y,rounded_y))
    checks[source+'_rounding_error_small']=rounding_error<F(1,10**7)
    sources[source]=dict(clocks=clock_bounds,actual_Y=[encode_i(x) for x in actual_y],rounded_Y=[str(x) for x in rounded_y],distance_rounding_error=str(sigma),processed_rounding_error=str(rounding_error))
    if source.startswith('vacuum'):
        checks['physical_wave_nonzero_negative_11']=actual_y[0].hi<0
        checks['physical_wave_nonzero_positive_22']=actual_y[2].lo>0
        checks['wave_packet_output_enclosures_narrow']=max(x.width() for x in actual_y)<F(1,10**7)
    else:
        checks['curvature_free_moving_control_nonzero_11']=actual_y[0].hi<0
        checks['curvature_free_moving_control_negative_22']=actual_y[2].hi<0
        checks['moving_packet_output_enclosures_narrow']=max(x.width() for x in actual_y)<F(1,10**7)
# Whole-domain geometric bounds used in every root bracket.
_,cos_half=sin_cos(I.of(F(1,2)))
e=exp_pos(F(1,2));cosh_half=(e+1/e)/2
checks['wave_metric_lower_half']= (cos_half**2).lo>F(1,2)
checks['wave_metric_upper_two']= (cosh_half**2).hi<2
checks['wave_all_rays_in_certificate_domain']=F(5,4)/SQRT2.lo+2*F(5,32)<2
checks['physical_static_control_zero']=by_time(flat_packet(p))==(0,0,0)
checks['eighteen_certified_wave_legs']=len(brackets)==18
checks['wave_and_flat_tidal_values_distinct']=(-A*A/2,A*A/2)!=(0,0)
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),Path(__file__).with_name('finite_radar_protocol.py')]
receipt=dict(passed=all(checks.values()),checks=checks,arithmetic=dict(grid='2^80 outward rounding',taylor_degree=24,null_bisections=48,float_use='display only'),
    physical_tidal_readouts=dict(wave=['-1/32','1/32','0'],flat_moving=['0','0','0']),sources=sources,wave_leg_certificates=brackets,
    scope='Analytic vacuum/flat solutions and ideal worldlines, exact rational enclosures; not empirical validation, proof-assistant certification or a pointwise-curvature interpretation of finite Y.',
    source_sha256={str(x.relative_to(root)):hashlib.sha256(x.read_bytes()).hexdigest() for x in paths})
Path(__file__).with_name('physical-radar-protocol.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=receipt['passed'],checks=checks,Y_display={s:[x['display'] for x in r['actual_Y']] for s,r in sources.items()}),indent=2))
raise SystemExit(0 if receipt['passed'] else 1)

"""Exact rational endpoint evaluation plus independent corner controls.
Universal enclosure soundness is in RadarOutputEnclosure.agda, not inferred
from corner enumeration. A concrete real-number instance remains separate.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import re
from finite_radar_protocol import Protocol,Row,Packet,by_time
base=Path(__file__).resolve().parent;root=base.parents[1]
load=lambda n:json.loads((base/n).read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
formal=load('radar-output-enclosure-formal.json');physical=load('physical-radar-protocol.json');gen=load('radar-output-certificate-generation.json')
source_path=base/'agda/RadarOutputPhysicalCertificates.agda';source=source_path.read_text(encoding='utf-8')
checks={}
checks['fresh_formal_enclosure_theorem']=formal['passed'] and formal['fresh'] and formal['output_mode']
checks['ten_intended_rejections']=sum(r['expected_rejection'] and r['passed'] for r in formal['results'])==10
checks['compiled_sources_current']=all(Path(p).exists() and sha(Path(p))==h for p,h in formal['source_snapshot_hashes'].items())
checks['generator_current']=sha(base/'generate_radar_output_certificates.py')==gen['generator_sha256']
checks['generated_delay_source_current']=sha(source_path)==gen['source_sha256']
checks['physical_receipt_link']=sha(base/'physical-radar-protocol.json')==gen['physical_receipt_sha256'] and physical['passed']
checks['physical_dependencies_current']=all(sha(root/p)==h for p,h in physical['source_sha256'].items())
checks['clock_certificate_link']=sha(base/'radar-clock-certificate-generation.json')==gen['clock_generation_sha256']
p=Protocol(F(1,32),F(1,4),F(1),'retained-Rosen-transverse-labels','central-proper-clock-c=1')
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
neg=lambda a:(-a[1],-a[0])
scale=lambda c,a:(c*a[0],c*a[1])
def square(a):
    if a[0]<0:raise ValueError('nonnegative-delay guard required')
    return (a[0]**2,a[1]**2)
def temporal(q,d):return add(add(q[1,d],neg(scale(2,q[0,d]))),q[-1,d])
def enclose(delay,D):
    q={key:square(v) for key,v in delay.items()}
    tx,ty,txy=(temporal(q,d) for d in ('x3','y4','xy5'))
    n=(scale(16,tx),scale(6,add(add(txy,neg(tx)),neg(ty))),scale(9,ty))
    alpha=F(2048,144*D*D)
    return tuple(neg(scale(alpha,x)) for x in n)
output={}
for case in gen['cases']:
    name=case['source'];prefix='wave' if name.startswith('vacuum') else 'moving';D=int(case['denominator'])
    rows=physical['sources'][name]['clocks'];delay={};aligned=True
    for row in rows:
        label={-1:'before',0:'center',1:'after'}[row['time']];d=row['direction']
        low=int(re.search(rf'^{prefix}-low-delay {label} {d} = (\d+)$',source,re.M)[1])
        high=int(re.search(rf'^{prefix}-high-delay {label} {d} = (\d+)$',source,re.M)[1])
        delay[row['time'],d]=(F(low),F(high))
        emitted=F(row['emission'])
        aligned &= low==D*(F(row['reception']['lo'])-emitted) and high==D*(F(row['reception']['hi'])-emitted)
    checks[prefix+'_delay_alignment']=aligned
    checks[prefix+'_positive_lower_delays']=all(v[0]>0 and v[0]<=v[1] for v in delay.values())
    box=enclose(delay,D)
    minima=[None]*3;maxima=[None]*3;contained=True
    for choices in product((0,1),repeat=9):
        selected=tuple(Row(row['time'],row['direction'],F(row['emission']),F(row['emission'])+delay[row['time'],row['direction']][choice]/D) for row,choice in zip(rows,choices))
        y=by_time(Packet(p,selected,'synthetic:input-enclosure-corner'))
        for i,value in enumerate(y):
            contained &= box[i][0]<=value<=box[i][1]
            minima[i]=value if minima[i] is None else min(minima[i],value)
            maxima[i]=value if maxima[i] is None else max(maxima[i],value)
    checks[prefix+'_all_512_corners_contained']=contained
    checks[prefix+'_component_extrema_sharp_on_box']=all(box[i]==(minima[i],maxima[i]) for i in range(3))
    rounded=tuple(Row(row['time'],row['direction'],F(row['emission']),F(row['rounded_reception'])) for row in rows)
    y=by_time(Packet(p,rounded,'certified-rounding:'+name))
    checks[prefix+'_rounded_native_reading_contained']=all(lo<=v<=hi for (lo,hi),v in zip(box,y))
    checks[prefix+'_old_analytic_output_overlap']=all(lo<=F(old['hi']) and F(old['lo'])<=hi for (lo,hi),old in zip(box,physical['sources'][name]['actual_Y']))
    checks[prefix+'_zero_excluded_diagonals']=box[0][1]<0 and (box[2][0]>0 if prefix=='wave' else box[2][1]<0)
    checks[prefix+'_width_below_1e_minus_10']=all(hi-lo<F(1,10**10) for lo,hi in box)
    output[name]=[dict(lo=str(lo),hi=str(hi),width=str(hi-lo),display=[float(lo),float(hi)]) for lo,hi in box]
try:
    square((F(-1),F(1)));checks['zero_crossing_square_refused']=False
except ValueError:checks['zero_crossing_square_refused']=True
checks['normalization_reverses_endpoints']=neg(scale(F(2),(F(1),F(3))))==(F(-6),F(-2))
receipt=dict(passed=all(checks.values()),checks=checks,output_enclosures=output,
    formal_receipt_sha256=sha(base/'radar-output-enclosure-formal.json'),generation_receipt_sha256=sha(base/'radar-output-certificate-generation.json'),
    scope='Formal ordered-arithmetic theorem with verified integer specialization; exact Fraction endpoint evaluation and 1024 synthetic corner controls. Ideal real arrivals require input enclosure soundness and the declared real coefficient interpretation; no hardware claim.')
(base/'radar-output-enclosure-audit.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(passed=receipt['passed'],checks=len(checks),outputs={k:[v['display'] for v in xs] for k,xs in output.items()}),indent=2))
raise SystemExit(0 if receipt['passed'] else 1)

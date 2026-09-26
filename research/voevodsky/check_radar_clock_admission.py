"""Audit the compiled certificate literals against retained physical clock receipts."""
from fractions import Fraction as F
from pathlib import Path
import json
import re
import hashlib
base=Path(__file__).resolve().parent;root=base.parents[1]
load=lambda name:json.loads((base/name).read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
physical=load('physical-radar-protocol.json')
formal=load('radar-clock-admission-formal.json')
generated=load('radar-clock-certificate-generation.json')
source_path=base/'agda/RadarClockPhysicalCertificates.agda'
source=source_path.read_text(encoding='utf-8')
checks={}
checks['fresh_formal_closure']=formal['passed'] and formal['fresh'] and formal['admission_mode']
checks['seven_intended_rejections']=sum(r['expected_rejection'] and r['passed'] for r in formal['results'])==7
checks['compiled_sources_current']=all(Path(p).exists() and sha(Path(p))==h for p,h in formal['source_snapshot_hashes'].items())
checks['generation_source_current']=generated['generated_source_sha256']==sha(source_path)
checks['generator_current']=generated['generator_sha256']==sha(base/'generate_radar_clock_certificates.py')
checks['physical_receipt_link']=generated['physical_receipt_sha256']==sha(base/'physical-radar-protocol.json') and physical['passed']
checks['physical_dependencies_current']=all(sha(root/p)==h for p,h in physical['source_sha256'].items())
time={-1:'before',0:'center',1:'after'}
for name,packet in physical['sources'].items():
    prefix='wave' if name=='vacuum-cosh-cos-initially-resting' else 'moving'
    k=int(re.search(rf'{prefix}-certificate : ClockCertificate (\d+) {prefix}-rows',source)[1]);D=k+1
    quarter=int(re.search(rf'quarter-ticks {prefix}-certificate = (\d+)',source)[1])
    budget=int(re.search(rf'error-budget {prefix}-certificate = (\d+)',source)[1])
    checks[prefix+'_grid_denominator']=D==4*quarter and D>0
    for row in packet['clocks']:
        t=time[row['time']];d=row['direction'];label=prefix+'_'+t+'_'+d
        get=lambda field:int(re.search(rf'^{prefix}-{field} {t} {d} = (\d+)$',source,re.M)[1])
        a=get('arrival');lo=get('lower');hi=get('upper')
        checks[label+'_same_source_clocks']=F(a,D)==F(row['rounded_reception']) and F((row['time']+4)*quarter,D)==F(row['emission'])
        checks[label+'_same_enclosure']=F(lo,D)==F(row['reception']['lo']) and F(hi,D)==F(row['reception']['hi'])
        checks[label+'_certified_interval_arithmetic']=lo+get('below')==a and a+get('above')==hi and hi==lo+get('width') and get('width')+get('slack')==budget
        checks[label+'_causal_gap']=a==(row['time']+4)*quarter+1+get('delay')
    summary=next(x for x in generated['certificates'] if x['source']==name)
    checks[prefix+'_conditional_distance_error']=F(summary['distance_error_bound'])==F(budget,2*D)
out=dict(passed=all(checks.values()),checks=checks,formal_receipt_sha256=sha(base/'radar-clock-admission-formal.json'),
    generation_receipt_sha256=sha(base/'radar-clock-certificate-generation.json'),
    boundary='Checks provenance alignment and finite arithmetic only. Real-ray membership in input enclosures is retained external analytic evidence, not a consequence of source hashes.')
(base/'radar-clock-admission-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('passed=',out['passed'],'checks=',len(checks))
raise SystemExit(0 if out['passed'] else 1)

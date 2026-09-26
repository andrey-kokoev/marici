"""Exact bridge from retained physical rounded clocks to the formal numerator.
Does not fabricate an Agda witness of the abstract physical admission policy.
"""
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import hashlib
import json
from finite_radar_protocol import Protocol,Row,Packet,by_time
base=Path(__file__).resolve().parent;root=base.parents[1]
physical_path=base/'physical-radar-protocol.json'
formal_path=base/'native-radar-formal.json'
physical=json.loads(physical_path.read_text());formal=json.loads(formal_path.read_text())
checks={};packets={}
checks['formal_fresh_positive_and_negative_controls']=formal['passed'] and formal['fresh'] and formal['original_sources_unchanged']
checks['formal_source_snapshot_current']=all(Path(p).exists() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==digest for p,digest in formal['source_snapshot_hashes'].items())
checks['physical_receipt_passed']=physical['passed']
checks['physical_dependencies_current']=all(hashlib.sha256((root/p).read_bytes()).hexdigest()==digest for p,digest in physical['source_sha256'].items())
p=Protocol(F(1,32),F(1,4),F(1),'retained-Rosen-transverse-labels','central-proper-clock-c=1')
weights={-1:1,0:-2,1:1};directions=('x3','y4','xy5')
for name,source in physical['sources'].items():
    rows=tuple(Row(row['time'],row['direction'],F(row['emission']),F(row['rounded_reception'])) for row in source['clocks'])
    D=lcm(*(x.denominator for row in rows for x in (row.emission,row.reception)))
    ticks={(row.time,row.direction):(int(row.emission*D),int(row.reception*D)) for row in rows}
    squares={key:(v[1]-v[0])**2 for key,v in ticks.items()}
    shape=lambda t:(16*squares[t,'x3'],6*(squares[t,'xy5']-squares[t,'x3']-squares[t,'y4']),9*squares[t,'y4'])
    old=tuple(sum(weights[t]*shape(t)[c] for t in (-1,0,1)) for c in range(3))
    temporal={d:sum(weights[t]*squares[t,d] for t in (-1,0,1)) for d in directions}
    native=(16*temporal['x3'],6*(temporal['xy5']-temporal['x3']-temporal['y4']),9*temporal['y4'])
    decoded=tuple(F(-2048*n,144*D*D) for n in native)
    checks[name+'_clock_ticks_roundtrip']=all(F(ticks[r.time,r.direction][0],D)==r.emission and F(ticks[r.time,r.direction][1],D)==r.reception for r in rows)
    checks[name+'_positive_tick_denominator']=D>0
    checks[name+'_future_tick_reception']=all(a<b for a,b in ticks.values())
    checks[name+'_integer_numerator_comparison']=old==native
    checks[name+'_physical_unit_normalization']=decoded==by_time(Packet(p,rows,'certified-rounding:'+name))
    checks[name+'_nonzero_instance']=any(native)
    packets[name]=dict(denominator=str(D),denominator_predecessor=str(D-1),normalization='-2048/(144*D^2)',numerator=[str(x) for x in native],
        clocks=[dict(time=t,direction=d,emission=str(ticks[t,d][0]),reception=str(ticks[t,d][1])) for t in (-1,0,1) for d in directions])
out=dict(passed=all(checks.values()),checks=checks,packets=packets,
    formal_receipt_sha256=hashlib.sha256(formal_path.read_bytes()).hexdigest(),physical_receipt_sha256=hashlib.sha256(physical_path.read_bytes()).hexdigest(),
    scope='Exact finite clock/numerator/normalization bridge. Underlying ideal clock enclosures and continuum physics remain separate; abstract Agda Admission is not instantiated by a hash string.')
(base/'native-radar-tick-bridge.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(passed=out['passed'],checks=checks),indent=2))
raise SystemExit(0 if out['passed'] else 1)

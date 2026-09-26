"""Exact frame/probe comparison; uses retained rounded physical clock records."""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from finite_radar_protocol import Protocol,Row,Packet,by_time,encode_section,DIRECTIONS

def transpose(a):return tuple(zip(*a))
def mul(a,b):return tuple(tuple(sum(x*y for x,y in zip(r,c)) for c in transpose(b)) for r in a)
def apply(a,v):return tuple(sum(x*y for x,y in zip(r,v)) for r in a)
def matrix(v):return ((v[0],v[1]),(v[1],v[2]))
def solve(a,b):
    rows=[list(map(F,r))+[F(x)] for r,x in zip(a,b)]
    for k in range(3):
        pivot=next((i for i in range(k,3) if rows[i][k]),None)
        if pivot is None:raise ValueError('probe quadratic design is singular')
        rows[k],rows[pivot]=rows[pivot],rows[k]
        divisor=rows[k][k];rows[k]=[x/divisor for x in rows[k]]
        for i in range(3):
            if i!=k:
                factor=rows[i][k];rows[i]=[x-factor*y for x,y in zip(rows[i],rows[k])]
    return tuple(r[-1] for r in rows)
def design(vectors):return tuple((x*x,2*x*y,y*y) for x,y in vectors)
def native(section,vectors):
    # Read the selected rows directly; never decode a source packet.
    values={d:F(0) for d in DIRECTIONS};seen=set()
    for index,row in section.choices:
        assert index==(row.time,row.direction) and index not in seen
        seen.add(index)
        q=((row.reception-row.emission)/(2*section.protocol.epsilon))**2
        values[row.direction]+=({-1:1,0:-2,1:1}[row.time])*q
    assert len(seen)==9
    return matrix(solve(design(vectors),tuple(-values[d]/(2*section.protocol.step**2) for d in DIRECTIONS)))

root=Path(__file__).resolve().parents[2]
receipt_path=Path(__file__).with_name('physical-radar-protocol.json')
receipt=json.loads(receipt_path.read_text())
checks={}
checks['physical_certificate_passed']=receipt['passed']
checks['physical_certificate_dependencies_current']=all(hashlib.sha256((root/path).read_bytes()).hexdigest()==digest for path,digest in receipt['source_sha256'].items())
p=Protocol(F(1,32),F(1,4),F(1),'retained-Rosen-transverse-labels','central-proper-clock-c=1')
vectors=((F(3),F(0)),(F(0),F(4)),(F(3),F(4)))
Q=((F(3,5),F(-4,5)),(F(4,5),F(3,5)))
T=transpose(Q);identity=((1,0),(0,1))
checks['rotation_orthogonal']=mul(T,Q)==identity
passive=tuple(apply(T,v) for v in vectors)
active=tuple(apply(Q,v) for v in vectors)
for name,source in receipt['sources'].items():
    rows=tuple(Row(r['time'],r['direction'],F(r['emission']),F(r['rounded_reception'])) for r in source['clocks'])
    packet=Packet(p,rows,'certified-rounding:'+name);section=encode_section(packet)
    Y=native(section,vectors)
    checks[name+'_original_protocol_agrees']=Y==matrix(by_time(packet))
    checks[name+'_passive_covariance']=native(section,passive)==mul(mul(T,Y),Q)
    checks[name+'_roundtrip_frame']=mul(mul(Q,native(section,passive)),T)==Y
    checks[name+'_labels_without_vectors_are_insufficient']=native(section,passive)!=Y
    if name.startswith('flat-moving'):
        # Exact isotropy of this supplied source makes scalar radar distances
        # unchanged when the physical apparatus is rotated.
        checks['active_isotropic_control_covariance']=native(section,active)==mul(mul(Q,Y),T)
        checks['active_change_is_not_fixed_frame_identity']=native(section,active)!=Y
        a,b=source['actual_Y'][0],source['actual_Y'][2]
        checks['actual_not_only_rounded_anisotropy']=F(a['lo'])>F(b['hi'])
try:
    solve(design(((1,0),(2,0),(3,0))),(1,4,9))
    checks['singular_probe_design_rejected']=False
except ValueError:checks['singular_probe_design_rejected']=True
# Direct scalar null-leg invariance under passive rotation (non-diagonal SPD control).
S=((F(2),F(1,3)),(F(1,3),F(1)))
def inv2(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))
b=(F(3,32),F(4,32));bp=apply(T,b)
quadratic=lambda a,v:sum(x*y for x,y in zip(v,apply(a,v)))
checks['null_leg_scalar_passive_invariance']=quadratic(inv2(S),b)==quadratic(inv2(mul(mul(T,S),Q)),bp)
out=dict(passed=all(checks.values()),checks=checks,physical_receipt_sha256=hashlib.sha256(receipt_path.read_bytes()).hexdigest(),scope='Exact finite comparison plus retained physical certificate; no arbitrary apparatus-independent curvature interpretation.')
Path(__file__).with_name('radar-frame-comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)

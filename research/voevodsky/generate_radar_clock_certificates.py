"""Generate checkable finite certificates; generation is not proof acceptance."""
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import json
import hashlib
base=Path(__file__).resolve().parent
source=base/'physical-radar-protocol.json'
data=json.loads(source.read_text())
assert data['passed']
header='''{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockPhysicalCertificates where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (_·_)
open import Cubical.Data.Int.Base using (pos)
open import NativeRadarReadout using (Rows; clocks; Time; before; center; after; Direction; x3; y4; xy5; frozen-calibration)
open import RadarClockAdmission
-- Generated arithmetic certificates only. Enclosure soundness for a real
-- null ray is NOT a theorem of this file. See the retained analytic receipt.
'''
parts=[header];summary=[];times={-1:'before',0:'center',1:'after'}
for idx,(name,packet) in enumerate(data['sources'].items()):
    prefix='wave' if name=='vacuum-cosh-cos-initially-resting' else 'moving'
    assert name in ('vacuum-cosh-cos-initially-resting','flat-moving-isotropic-Rosen')
    vals=[F(x) for r in packet['clocks'] for x in (r['emission'],r['rounded_reception'],r['reception']['lo'],r['reception']['hi'])]
    D=lcm(*(x.denominator for x in vals));assert D>0 and D%4==0
    quarter=D//4
    records=[]
    for r in packet['clocks']:
        em,arrival,lo,hi=[int(F(x)*D) for x in (r['emission'],r['rounded_reception'],r['reception']['lo'],r['reception']['hi'])]
        assert em==(r['time']+4)*quarter and em<arrival and 0<=lo<=arrival<=hi
        records.append(dict(time=times[r['time']],direction=r['direction'],arrival=arrival,lower=lo,upper=hi,below=arrival-lo,above=hi-arrival,width=hi-lo,delay=arrival-em-1))
    budget=max(r['width'] for r in records)
    for field in ('arrival','lower','upper','below','above','width','delay','slack'):
        parts.append(f'{prefix}-{field} : Grid\n')
        for r in records:
            value=budget-r['width'] if field=='slack' else r[field]
            parts.append(f"{prefix}-{field} {r['time']} {r['direction']} = {value}\n")
    parts.append(f'''{prefix}-rows : Rows
{prefix}-rows t d = clocks (pos (slot t · {quarter})) (pos ({prefix}-arrival t d))
{prefix}-certificate : ClockCertificate {D-1} {prefix}-rows
calibration {prefix}-certificate = frozen-calibration
calibration-fixed {prefix}-certificate = refl
quarter-ticks {prefix}-certificate = {quarter}
denominator-grid {prefix}-certificate = refl
arrival {prefix}-certificate = {prefix}-arrival
row-grid {prefix}-certificate t d = refl
delay-minus-one {prefix}-certificate = {prefix}-delay
refinement {prefix}-certificate = 0
lower {prefix}-certificate = {prefix}-lower
upper {prefix}-certificate = {prefix}-upper
below {prefix}-certificate = {prefix}-below
above {prefix}-certificate = {prefix}-above
width {prefix}-certificate = {prefix}-width
error-budget {prefix}-certificate = {budget}
slack {prefix}-certificate = {prefix}-slack
''')
    for field in ('causal','inside-lower','inside-upper','width-exact','within-budget'):
        for r in records:parts.append(f"{field} {prefix}-certificate {r['time']} {r['direction']} = refl\n")
    summary.append(dict(source=name,denominator=str(D),receipt_width_budget_ticks=str(budget),reception_error_bound=str(F(budget,D)),distance_error_bound=str(F(budget,2*D))))
output=base/'agda/RadarClockPhysicalCertificates.agda'
output.write_text(''.join(parts),encoding='utf-8')
receipt=dict(generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),physical_receipt_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),generated_source_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),certificates=summary,scope='Generation and exact rational extraction; Agda acceptance is recorded separately. No real-ray enclosure-soundness proof is generated.')
(base/'radar-clock-certificate-generation.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))

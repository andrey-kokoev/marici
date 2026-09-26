"""Emit arithmetic links from admitted absolute-clock bounds to delay intervals."""
from pathlib import Path
from fractions import Fraction as F
import json
import hashlib
base=Path(__file__).resolve().parent
physical=json.loads((base/'physical-radar-protocol.json').read_text())
generation=json.loads((base/'radar-clock-certificate-generation.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert generation['physical_receipt_sha256']==sha(base/'physical-radar-protocol.json')
text=['''{-# OPTIONS --safe --cubical --guardedness #-}
module RadarOutputPhysicalCertificates where
open import Cubical.Foundations.Prelude
open import NativeRadarReadout using (before; center; after; x3; y4; xy5)
open import RadarClockAdmission using (Grid)
open import RadarClockPhysicalCertificates
open import RadarOutputEnclosure
''']
summary=[]
for source in generation['certificates']:
    name=source['source'];prefix='wave' if name.startswith('vacuum') else 'moving'
    D=int(source['denominator']);packet=physical['sources'][name];rows=[]
    for row in packet['clocks']:
        emitted=F(row['emission'])*D
        low=F(row['reception']['lo'])*D-emitted
        high=F(row['reception']['hi'])*D-emitted
        assert emitted.denominator==low.denominator==high.denominator==1 and 0<=low<=high
        rows.append(({-1:'before',0:'center',1:'after'}[row['time']],row['direction'],int(low),int(high)))
    for field,index in (('low',2),('high',3)):
        text.append(f'{prefix}-{field}-delay : Grid\n')
        for row in rows:text.append(f'{prefix}-{field}-delay {row[0]} {row[1]} = {row[index]}\n')
    text.append(f'{prefix}-delays : DelayCertificate {prefix}-certificate\nlow-delay {prefix}-delays = {prefix}-low-delay\nhigh-delay {prefix}-delays = {prefix}-high-delay\n')
    for field in ('lower-shift','upper-shift'):
        for t,d,_,_ in rows:text.append(f'{field} {prefix}-delays {t} {d} = refl\n')
    # General CertifiedBounds theorem applies without evaluating huge unary integer products.
    summary.append(dict(source=name,denominator=str(D),minimum_delay_ticks=str(min(x[2] for x in rows))))
path=base/'agda/RadarOutputPhysicalCertificates.agda';path.write_text(''.join(text),encoding='utf-8')
receipt=dict(generator_sha256=sha(Path(__file__)),source_sha256=sha(path),physical_receipt_sha256=sha(base/'physical-radar-protocol.json'),clock_generation_sha256=sha(base/'radar-clock-certificate-generation.json'),cases=summary)
(base/'radar-output-certificate-generation.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))

"""Retained full-turn witness attached to both existing rung routes.

This is an explicit enriched-row adapter, not identification with the old
137-row fixture or a new classical measurement postulate.
"""
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from fractions import Fraction as F
from pathlib import Path
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    coherent=runpy.run_path(str(HERE/'check_triangle_coherent_generator_transport.py'))
    tower=runpy.run_path(str(HERE/'check_rung_transport_diagram.py'))
prior=coherent['prior']; c=prior['c']; ledger=c['ledger']
C=prior['C']; R=prior['R']; B=prior['B']; K=prior['K']
J=S.Matrix([[0,1],[-1,0]])
rotor=lambda angle:S.cos(S.pi*angle)*S.eye(2)+S.sin(S.pi*angle)*J

@dataclass(frozen=True)
class FullTurn:
    primitive_registry: tuple
    records: tuple
    stages: tuple
    angles_over_pi: tuple


def summary(payload):
    return S.Matrix([sum(v for path,v in zip(payload.paths,payload.values) if path[-1][2]==label)
                     for label in ledger.labels])


left=ledger.compose_payloads(c['L'],c['R'])
right=ledger.compose_payloads(c['R'],c['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
records=[c['L'],c['R'],whole];stages=[]
for tick in range(7):
    records.extend((left,right));stages.append((left.label,right.label))
    if tick<6:
        left,right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)
witness=FullTurn(tuple(c['PACKETS']),tuple(records),tuple(stages),tuple(F(n,3) for n in range(7)))


def validate(w):
    """Check the recovered packet itself, including all parent-slot joins."""
    if w.primitive_registry!=tuple(c['PACKETS']):raise ValueError('source registry changed')
    if len(w.stages)!=7 or w.angles_over_pi!=tuple(F(n,3) for n in range(7)):
        raise ValueError('not the declared positive complete rotor turn')
    lookup={p.label:p for p in w.records}
    if len(lookup)!=len(w.records):raise ValueError('duplicate retained record identity')
    for p in w.records:
        if p.operation=='compose':
            if any(label not in lookup for label in p.parents):raise ValueError('missing operand')
            a,b=(lookup[label] for label in p.parents)
            expected_slots={(i,j) for i,x in enumerate(a.paths) for j,y in enumerate(b.paths) if x[-1][1]==y[0][0]}
            if len(p.paths)!=len(p.parent_slots) or len(p.paths)!=len(p.values):raise ValueError('missing slot witness')
            if len(set(p.parent_slots))!=len(p.parent_slots) or set(p.parent_slots)!=expected_slots:
                raise ValueError('incomplete or duplicated endpoint composition')
            for word,value,(i,j) in zip(p.paths,p.values,p.parent_slots):
                if word!=a.paths[i]+b.paths[j] or a.paths[i][-1][1]!=b.paths[j][0][0]:
                    raise ValueError('invalid retained join')
                if value!=a.values[i]*b.values[j]:raise ValueError('changed composition coefficient')
    initial=None
    previous=None
    for n,(a,b) in enumerate(w.stages):
        lp,rp=lookup[a],lookup[b]
        if n==0:
            if lp.parents!=(c['L'].label,c['R'].label) or rp.parents!=(c['R'].label,c['L'].label):
                raise ValueError('not the actual component operands')
        else:
            if lp.parents!=(w.stages[n-1][0],whole.label) or rp.parents!=(w.stages[n-1][1],whole.label):
                raise ValueError('chronological parent chain changed')
        z=summary(lp)-summary(rp)
        if previous is not None and z!=K*previous:raise ValueError('source continuation square failed')
        if initial is None:initial=z
        if R*z!=R*B*C**n*prior['coordinates']:raise ValueError('rotor attachment failed')
        if lp.word_length!=n+2 or rp.word_length!=n+2:raise ValueError('lost path depth')
        previous=z
    if R*previous!=R*initial or rotor(w.angles_over_pi[-1])!=S.eye(2):
        raise ValueError('incomplete signed return')
    return w

checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
def reject(name,w):
    try:validate(w)
    except (ValueError,KeyError):checks.append(name);return
    raise AssertionError(name)
check('actual-full-turn-validated',validate(witness)==witness)
check('three-steps-only-adjoint-return',rotor(F(1))==-S.eye(2))
check('six-steps-signed-return',rotor(F(2))==S.eye(2))
reject('reject-three-step-as-full-witness',replace(witness,stages=witness.stages[:4],angles_over_pi=witness.angles_over_pi[:4]))
reject('reject-erased-unwrapped-phase',replace(witness,angles_over_pi=(F(0),)*7))
reject('reject-dropped-source-operand',replace(witness,records=witness.records[1:]))
swapped=list(witness.stages);swapped[1],swapped[2]=swapped[2],swapped[1]
reject('reject-reordered-comparison-history',replace(witness,stages=tuple(swapped)))

# A genuine enrichment is necessary: the original numeric Row does not carry
# a full-turn certificate. Promotions retain enriched leaves unchanged.
@dataclass(frozen=True)
class WitnessRow(tower['Row']):
    witness: FullTurn | None = None

lookup={p.label:p for p in witness.records}
rows=[]
for tick,pair in enumerate(witness.stages):
    for role,label in zip(('LR','RL'),pair):
        p=lookup[label]
        for i,(word,value) in enumerate(zip(p.paths,p.values)):
            rows.append(WitnessRow(('leaf',tick,role,i,tuple(e[2] for e in word)),
                ('vertex',word[0][0]),('vertex',word[-1][1]),tower['scale'](value,tower['I']),
                witness=witness))
source=tuple(sorted(rows,key=lambda r:r.label))
indexed=tower['indexed']; unindex=tower['unindex']; leaves=tower['leaves']

def decode(view):
    recovered=leaves(unindex(view))
    if not recovered or any(not isinstance(r,WitnessRow) or r.witness is None for r in recovered):
        raise ValueError('full witness not retained')
    w=validate(recovered[0].witness)
    if any(r.witness!=w for r in recovered):raise ValueError('inconsistent witness bindings')
    bylabel={p.label:p for p in w.records}
    expected=[]
    for tick,pair in enumerate(w.stages):
        for role,label in zip(('LR','RL'),pair):
            for i,(word,value) in enumerate(zip(bylabel[label].paths,bylabel[label].values)):
                expected.append((('leaf',tick,role,i,tuple(e[2] for e in word)),
                                 ('vertex',word[0][0]),('vertex',word[-1][1]),tower['scale'](value,tower['I'])))
    actual=[(r.label,r.source,r.target,r.value) for r in recovered]
    if actual!=sorted(expected,key=lambda row:row[0]):raise ValueError('witness does not bind these leaves')
    return w

for policy in ('inherited','common'):
    def promote(rows):return tower['incoming_promotion'](tower['incoming_promotion'](rows,1,policy),2,policy)
    upper=indexed(unindex(indexed(promote(source),'source')),'target')
    lower=indexed(promote(unindex(indexed(unindex(indexed(source,'source')),'target'))),'target')
    check('rung-route-square/'+policy,upper==lower)
    check('whole-witness-recovered/'+policy,decode(upper)==witness and decode(lower)==witness)
    check('all-stage-leaves-recovered/'+policy,leaves(unindex(upper))==source)
    check('clock-not-reset-by-transport/'+policy,decode(upper).angles_over_pi[-1]==2)
    check('old-reference-unchanged/'+policy,tower['physical_reference'].value==tower['scale'](2,tower['I']))
    check('numeric-summary-not-the-witness/'+policy,tower['read_at_four'](upper)==tower['scale'](-1,tower['I']))
# Losing a leaf must fail even if every surviving leaf still carries the
# unchanged full certificate: metadata alone cannot fake the attachment.
try:decode(indexed(source[1:],'target'))
except ValueError:checks.append('reject-leaf-loss-with-intact-certificate')
else:raise AssertionError('detached metadata accepted')
# The complete packet is recoverable from rung4, not from its scalar mean.
plain=tuple(tower['Row'](r.label,r.source,r.target,r.value) for r in source)
try:decode(indexed(plain,'target'))
except ValueError:checks.append('reject-numeric-only-substitution')
else:raise AssertionError('numeric-only substitution accepted')

result={
    'schema':'marici.nima.full-turn-witness-rung-attachment.v1','status':'pass','checks':checks,
    'source_leaf_count':len(source),'retained_payload_records':len(witness.records),
    'witness':'actual six-update retained path family, positive rotor lift, parent-slot composition chain, signed return and nonzero unwrapped clock',
    'clock_over_pi':[str(a) for a in witness.angles_over_pi],
    'positive_result':'both existing rung routes transport and recover the complete enriched witness, not merely an endpoint sum',
    'adapter_boundary':'explicit WitnessRow enrichment using retained leaves; not proof that the original numeric Row or historical 137-row fixture already encoded this witness',
    'formal_boundary':'finite exact attachment and existing rotor identities; no new native Agda comparison identifies it with every generic witness or the earlier square-cone Tick',
    'physical_boundary':'no extra classical observer, Born rule, seconds calibration, or charge/mass interpretation introduced',
}
(ROOT/'results/full-turn-witness-rung-attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact full-turn witness/rung attachment checks')
print(f'{len(source)} actual history leaves and {len(witness.records)} operand records retained through both rung routes.')
print('Three-step, erased-phase, missing-parent and reordered-history substitutions rejected.')

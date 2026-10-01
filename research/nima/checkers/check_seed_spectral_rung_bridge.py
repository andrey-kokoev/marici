"""Existing full-seed spectral decoder through existing rung candidates.
No new phase update, dynamics, or physical reference normalization.
"""
from fractions import Fraction as F
from pathlib import Path
from dataclasses import dataclass, replace
import runpy
import check_natural_tower_return as spectral

bundle=spectral.main()  # Fresh original spectral assertions.
transport=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
Row=transport['Row']; indexed=transport['indexed']; unindex=transport['unindex']
promote=transport['incoming_promotion']; leaves=transport['leaves']

@dataclass(frozen=True)
class RetainedSpectrum:
    root: str
    modes: tuple
    occurrences: tuple
    basis: str

record=RetainedSpectrum('six-arrow-seed-spectrum',bundle['modes'],bundle['packets'],'ABCD')

def decode(record):
    grouped={}
    for d,(a,b),projector in record.modes:
        term=spectral.rscale(projector,a,b,d)
        grouped[d]=spectral.radd(grouped.get(d,(spectral.Z,spectral.Z)),term)
    assert all(imag==spectral.Z for real,imag in grouped.values())
    matrix=spectral.Z
    for real,imag in grouped.values(): matrix=spectral.add(matrix,real)
    expected={(source,target) for _,source,target in record.occurrences}
    support={(record.basis[j],record.basis[i]) for i in range(4) for j in range(4) if matrix[i][j]}
    assert support==expected
    assert all(matrix[record.basis.index(t)][record.basis.index(s)]==1
               for _,s,t in record.occurrences)
    assert len(expected)==len(record.occurrences)==6
    return matrix,record.occurrences

M,packets=decode(record)
assert M==bundle['matrix']
# One row per original occurrence. Numeric mean is an explicitly reversible
# support encoding: six times each unit entry, with original unit row masses.
source=[]
for position,(label,s,t) in enumerate(packets):
    value=tuple(tuple(F(6) if (record.basis[j],record.basis[i])==(s,t) else F(0)
                      for j in range(4)) for i in range(4))
    source.append(Row(('occurrence',position,label,record),('vertex',s),('vertex',t),value))
source=tuple(source)
assert transport['mean'](source)==M

def verify(rows):
    original=leaves(rows)
    assert original==source
    restored=[]
    for row in original:
        _,position,label,retained=row.label
        decoded,occurrences=decode(retained)
        assert decoded==M and retained==record
        assert occurrences[position][0]==label
        restored.append(occurrences[position])
    assert tuple(restored)==packets
    assert transport['mean'](rows)==M

for policy in ('inherited','common'):
    left11=indexed(source,'source')
    left10=indexed(unindex(left11),'target')
    def t9(rows): return promote(promote(rows,1,policy),2,policy)
    right6=t9(source)
    right5=indexed(right6,'source')
    right4=indexed(unindex(right5),'target')
    assert indexed(t9(unindex(left11)),'source')==right5
    assert indexed(t9(unindex(left10)),'target')==right4
    for rows in (source,unindex(left11),unindex(left10),right6,unindex(right5),unindex(right4)):
        verify(rows)
    print('PASS spectral bridge:',policy,'rung6/4 families',len(right6),'seed occurrences',len(source))
# Dropping a spectral mode fails the reconstruction certificate.
truncated=RetainedSpectrum(record.root,record.modes[:-1],record.occurrences,record.basis)
try:
    decode(truncated)
except AssertionError:
    pass
else:
    raise AssertionError('Truncated spectral record unexpectedly reconstructed seed')
# Correct spectrum cannot authorize reordered occurrence provenance.
wrong=RetainedSpectrum(record.root,record.modes,tuple(reversed(packets)),record.basis)
assert decode(wrong)[0]==M
assert decode(wrong)[1]!=packets  # Same incidence does not recover original occurrence order.
print('PASS: full eigenvalues/projectors, basis and occurrence history survive both rung routes.')
print('CONTROLS: missing mode rejected; spectral matrix alone cannot recover occurrence order.')
print('Scope: two existing candidate transports, no state evolution or physical calibration selected.')

# Observation boundary: vary numerical payloads, holding topology/masses fixed.
# These probe rows do NOT claim to be newly certified spectral seed packages.
def rank(matrix):
    a=[list(map(F,row)) for row in matrix]; pivot=0
    for column in range(len(a[0])):
        candidate=next((i for i in range(pivot,len(a)) if a[i][column]),None)
        if candidate is None: continue
        a[pivot],a[candidate]=a[candidate],a[pivot]
        divisor=a[pivot][column]
        a[pivot]=[v/divisor for v in a[pivot]]
        for i in range(len(a)):
            if i!=pivot:
                factor=a[i][column]
                a[i]=[x-factor*y for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==len(a): break
    return pivot

def transported(rows,policy):
    return promote(promote(rows,1,policy),2,policy)

def scalar_rows(values):
    return tuple(replace(row,value=((F(value),),)) for row,value in zip(source,values))

observation_maps={}
for policy in ('inherited','common'):
    columns=[]; observed=[]
    for j in range(6):
        rows=transported(scalar_rows([int(i==j) for i in range(6)]),policy)
        columns.append(tuple(r.value[0][0] for r in rows))
        observed.append(transport['mean'](rows)[0][0])
    family_map=tuple(zip(*columns))
    assert rank(family_map)==(4 if policy=='inherited' else 1)
    assert tuple(observed)==(F(1,6),)*6
    observation_maps[policy]=tuple(observed)
    print('Observation ranks:',policy,'family reader',rank(family_map),'aggregate reader',1)
assert observation_maps['inherited']==observation_maps['common']
# Five independent zero-sum probes span the scalar aggregate kernel.
kernel=tuple(tuple(F(int(i==j)-int(i==5)) for i in range(6)) for j in range(5))
assert rank(kernel)==5
for vector in kernel:
    for policy in observation_maps:
        assert transport['mean'](transported(scalar_rows(vector),policy))==((F(0),),)
# A zero-sum change between different targets survives the family observation
# for inherited transport, but not the common-family or aggregate observation.
hostile=scalar_rows((1,-1,0,0,0,0))
assert any(r.value!=((F(0),),) for r in transported(hostile,'inherited'))
assert all(r.value==((F(0),),) for r in transported(hostile,'common'))
# On edge-supported coefficients, the six matrix entries are distinct:
# unlike generic rows, their aggregate reading is injective.
for policy in observation_maps:
    columns=[]
    for j in range(6):
        rows=tuple(replace(row,value=spectral.scale(row.value,F(i==j)))
                   for i,row in enumerate(source))
        result=transport['mean'](transported(rows,policy))
        columns.append(tuple(v for line in result for v in line))
    assert rank(tuple(zip(*columns)))==6
print('PASS: aggregate kernels scalar=5, unrestricted six 4x4 rows=80, edge-supported coefficients=0.')
print('PASS: family reader distinguishes candidates; equal aggregate readers do not authorize a physical profile.')

# Comparison on canonical transport IMAGES, not arbitrary family trees.
def validate_image(rows,policy):
    original=leaves(rows)
    assert len(original)==len(source)
    for row,template in zip(original,source):
        assert replace(row,value=template.value)==template
    assert rows==transported(original,policy)
    return original

def compare_image(rows,from_policy,to_policy):
    return transported(validate_image(rows,from_policy),to_policy)

def aligned_family_reader(rows):
    # Independently specified original target partition, recovered from leaves;
    # NOT the candidate's possibly coarser outer family summary.
    groups=indexed(leaves(rows),'target')
    return tuple((key,transport['mean'](groups[key])) for key in sorted(groups))

probes=[source,hostile]
probes.extend(scalar_rows([int(i==j) for i in range(6)]) for j in range(6))
for original in probes:
    inherited=transported(original,'inherited')
    common=transported(original,'common')
    assert compare_image(inherited,'inherited','common')==common
    assert compare_image(common,'common','inherited')==inherited
    assert compare_image(compare_image(inherited,'inherited','common'),'common','inherited')==inherited
    assert compare_image(compare_image(common,'common','inherited'),'inherited','common')==common
    assert aligned_family_reader(inherited)==aligned_family_reader(common)
    assert leaves(inherited)==leaves(common)==original
    assert transport['mean'](inherited)==transport['mean'](common)
# Same means/leaves do not authorize an arbitrary altered family certificate.
canonical=transported(source,'common')
for forged in ((replace(canonical[0],mass=canonical[0].mass+1),),
               (replace(canonical[0],label=('forged',0)),)):
    try:
        compare_image(forged,'common','inherited')
    except AssertionError:
        pass
    else:
        raise AssertionError('Noncanonical image admitted')
print('PASS: canonical-image comparison has both inverse laws and preserves aligned target-family readings.')
print('CONTROLS: altered family mass/label rejected even with unchanged retained leaves.')

# Theory-page path-resource proposal: executed walks are additional data,
# not changes to the fixed primitive seed registry or its spectrum.
registry={label:(s,t) for label,s,t in packets}
def walk_reading(events,costs):
    assert events
    start=registry[events[0]][0]; endpoint=start; resource=F(0)
    for label in events:
        s,t=registry[label]
        assert s==endpoint
        assert costs[label]>0
        endpoint=t; resource+=costs[label]
    return start,endpoint,resource

one_return=('AB','BA'); two_returns=one_return+one_return
for costs in ({label:F(1) for label in registry},
              {label:F(i+1,3) for i,label in enumerate(registry)}):
    once=walk_reading(one_return,costs)
    twice=walk_reading(two_returns,costs)
    assert once[:2]==twice[:2]==('A','A')
    assert twice[2]==2*once[2]>once[2]>0
    # Transporting the representation preserves a supplied execution receipt;
    # representation conversion itself is NOT appended as an executed walk.
    before=(transported(source,'inherited'),one_return)
    after=(compare_image(before[0],'inherited','common'),before[1])
    assert leaves(before[0])==leaves(after[0])
    assert walk_reading(before[1],costs)==walk_reading(after[1],costs)
    assert (compare_image(after[0],'common','inherited'),after[1])==before
print('PASS: same seed and terminal endpoint admit distinct positive traversal resources.')
print('PASS: supplied execution receipts survive presentation comparison; no cost assigned to regrouping.')

# Reuse the actual finite execution ledger; do not interpret its two states as
# all four seed vertices without testing a typed endpoint adapter.
from check_paw_half_turn_promotion import Ledger
from itertools import product
ledger=Ledger()
a=ledger.half_turn(1); b=ledger.half_turn(-1)
first=ledger.promote(a,b)
c=ledger.half_turn(1); d=ledger.half_turn(-1)
second=ledger.promote(c,d)
double=ledger.promote(first,second)
assert first.source==first.target==double.source==double.target==1
assert first.variation_in_pi==2 and double.variation_in_pi==4
assert double.events==first.events+second.events
assert len({event.occurrence for event in double.events})==4
try:
    ledger.promote(first,first)
except ValueError:
    pass
else:
    raise AssertionError('Re-execution with reused occurrence IDs admitted')
# A global assignment sending every seed edge to ONE endpoint-flipping event
# would be a two-coloring. Either directed triangle obstructs it.
adapters=[]
for signs in product((-1,1),repeat=4):
    endpoint_map=dict(zip('ABCD',signs))
    if all(endpoint_map[t]==-endpoint_map[s] for _,s,t in packets):
        adapters.append(endpoint_map)
assert not adapters
print('PASS: existing ledger emits fresh events and retains composition without adding events.')
print('OBSTRUCTION: no four-vertex endpoint map sends all six seed arrows to single half-turn events.')

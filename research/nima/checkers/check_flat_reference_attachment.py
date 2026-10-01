"""Flat port-frame transport of the fixed reference; exact gauge controls.

Frames are declared coordinate identifications, not derived physical data.
A nonflat reference-loop control separates local invertibility from descent.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/flat-reference-attachment.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
I=m['I']; mul=m['mul']; add=m['add']; scale=m['scale']; Z=m['m']['Z']
d=m['physical_reference'].value; r=scale(F(1,2),I)


def inverse(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det
    return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))


def chain(*args):
    result=I
    for a in args: result=mul(result,a)
    return result


def total(args):
    result=Z
    for a in args: result=add(result,a)
    return result


rows=m['source']; stages={}
for policy in ('inherited','common'):
    first=m['incoming_promotion'](rows,1,policy)
    stages[policy]=(first,m['incoming_promotion'](first,2,policy))
all_rows=rows+tuple(row for levels in stages.values() for level in levels for row in level)
ports=sorted({p for row in all_rows for p in (row.source,row.target)},key=repr)
# Distinct exact invertible shears at each port.
frames={p:((F(1+n*n),F(n)),(F(n),F(1))) for n,p in enumerate(ports,1)}
changes={p:((F(1),F(n+1)),(F(0),F(1))) for n,p in enumerate(ports)}
changed={p:mul(changes[p],frames[p]) for p in ports}


def realization(row,fs):
    s,t=fs[row.source],fs[row.target]
    reference=chain(t,inverse(s))
    actual=chain(t,r,row.value,inverse(s))
    return actual,reference,inverse(reference)


def decode(actual,source,target,fs):
    return chain(d,inverse(fs[target]),actual,fs[source])


for row in all_rows:
    a,ref,ret=realization(row,frames)
    assert chain(ref,ret)==chain(ret,ref)==I
    assert decode(a,row.source,row.target,frames)==row.value
    assert decode(ref,row.source,row.target,frames)==d
    a2,ref2,ret2=realization(row,changed)
    gs,gt=changes[row.source],changes[row.target]
    assert a2==chain(gt,a,inverse(gs))
    assert ref2==chain(gt,ref,inverse(gs))
    assert ret2==chain(gs,ret,inverse(gt))
    assert decode(a2,row.source,row.target,changed)==row.value

# Common-target reference composition transports the existing matrix operation.
for family in m['indexed'](rows,'target').values():
    for a in family:
        av,_,_=realization(a,frames)
        for b in family:
            bv,_,br=realization(b,frames)
            composed=chain(bv,br,av)
            assert decode(composed,a.source,a.target,frames)==chain(b.value,r,a.value)

# Promote by transporting target endomorphisms, then attaching the new source.
# This works for both endpoint policies and is invariant under frame changes.
for fs in (frames,changed):
    for levels in stages.values():
        for level in levels:
            for family in level:
                target=fs[family.target]; terms=[]
                for member in family.members:
                    a,_,ret=realization(member,fs)
                    transport=chain(target,inverse(fs[member.target]))
                    terms.append(scale(F(member.mass,family.mass),
                                       chain(transport,a,ret,inverse(transport))))
                endomorphism=total(terms)
                new_reference=chain(target,inverse(fs[family.source]))
                promoted=chain(endomorphism,new_reference)
                assert promoted==realization(family,fs)[0]
                assert decode(promoted,family.source,family.target,fs)==family.value

# All frame-generated reference loops telescope. A local invertible twist need
# not: choose a genuine two-edge cycle already present in the carrier fixture.
a=next(row for row in rows if row.source==('a',0,0) and row.target==('a',2,2))
b=next(row for row in rows if row.source==a.target and row.target==a.source)
_,da,_=realization(a,frames); _,db,_=realization(b,frames)
assert chain(db,da)==I
H=((F(1),F(1)),(F(0),F(1)))
twisted=chain(frames[a.target],H,inverse(frames[a.source]))
assert chain(twisted,inverse(twisted))==I
holonomy=chain(db,twisted)
assert holonomy==chain(frames[a.source],H,inverse(frames[a.source]))!=I
# A passive frame change conjugates the loop, never turns it into the identity.
g=changes[a.source]
assert chain(g,holonomy,inverse(g))!=I

result={
 'status':'passed',
 'classification':'flat_reference_attachment_realizes_port_lift_with_frame_invariant_readout',
 'obligation':'attachment transport and route compatibility before physical readout',
 'stratum':'Finite invertible-reference fixture; declared global port frames; both retained endpoint policies',
 'checks':{'local_units':True,'reference_decodes_to_fixed_rung4_value':True,
           'common_target_composition':True,'two_promotion_rounds':True,
           'passive_frame_covariance':True,'decoded_values_unchanged':True,
           'nonflat_reference_holonomy_control':True},
 'unsupported':['source selection of globally flat reference transport',
                'selection of next-level endpoint policy','physical reference normalization',
                'weak-return or nontrivial-bundle extension'],
 'next_constructor':'Determine whether the source reference attachments have trivial loop holonomy or must retain path-indexed transport data.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

"""Joint error geometry and distinguishability tests; no experimental data."""
from pathlib import Path
import importlib.util,json
from flint import arb,acb,ctx

p=Path(__file__).with_name('evaluate_three_channel_cubic_protocol.py')
s=importlib.util.spec_from_file_location('protocol',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
o=m.ThreeChannelObserver();ctx.prec=2048
names=o.names
parse=lambda text:arb(text.replace('[','').replace(']',''))
state={'positive':acb(1),'crossed':acb(arb(1)/2),'vacuum':acb(0)}
errors={n:'1e-543' for n in names}
for endpoint in (o.lower,o.upper):
    raw={n:endpoint[n]*state[n] for n in names}
    result=o.normalize(raw,errors)
    for n in names:
        center=parse(result['coordinates'][n]['center'])
        radius=parse(result['coordinates'][n]['radius_upper'])
        assert abs(center-state[n].real)<radius
    assert parse(result['coordinates']['positive']['radius_upper'])<arb('0.01')
    assert parse(result['coordinates']['crossed']['radius_upper'])<arb('0.01')

other=dict(state);other['crossed']=acb(arb(3)/4)
fine=o.separate(state,other,errors)
coarse=o.separate(state,other,{n:'1e-540' for n in names})
assert fine['certified_distinct'] and fine['separating_channels']==['crossed']
assert not coarse['certified_distinct']
reuse=m.ThreeChannelObserver(mode='reuse')
reuse_comparison=reuse.separate(state,other,{n:'1e-540' for n in names})
assert reuse_comparison['certified_distinct'] and reuse_comparison['separating_channels']==['crossed']
# Independent raw-record aggregation: no scalar-observer gains enter this map.
records=[acb(0)]*449
rows=reuse.bin_receiver.manifest['rows']
p=next(i for i,r in enumerate(rows) if r['coefficient']=='positive')
x=next(i for i,r in enumerate(rows) if r['coefficient']=='crossed')
records[p]=acb(2);records[x]=acb(3)
raw,budgets=reuse.aggregate_reuse(records,['1e-545']*449,['4','0'],'1e-12')
assert raw['positive']==2*rows[p]['sign'] and raw['crossed']==3*rows[x]['sign'] and raw['vacuum']==4
assert budgets['crossed']>=arb(448)*arb('1e-545')
assert budgets['crossed']<arb(449)*arb('1e-545')
# Calibration uncertainty cannot be ignored just because acquisition error is zero.
a={'positive':acb(1000),'crossed':acb(0),'vacuum':acb(0)}
b=dict(a);b['positive']=acb(1001)
assert not o.separate(a,b,{n:'0' for n in names})['certified_distinct']
# Generic vacuum coefficient fixture. The w-dependent owning example is
# certified symbolically in the builder; no value of w is assigned here.
vac=dict(state);vac['vacuum']=acb(arb('1e-10'))
vac_result=o.separate(state,vac,{'positive':'1','crossed':'1','vacuum':'2.5e-11'})
assert vac_result['certified_distinct'] and vac_result['separating_channels']==['vacuum']
# A joint l1 budget can separate even when none of the marginal disks do.
a={n:acb(0) for n in names}
b={'positive':acb(o.gain['positive']*arb('1e-9')),
   'crossed':acb(o.gain['crossed']*arb('1e-9')),'vacuum':acb(0)}
joint=o.separate(a,b,{n:'1e-9' for n in names},'6e-10')
assert joint['certified_distinct'] and joint['using_total_l1_budget'] and not joint['separating_channels']
for raw,err in [({'positive':acb(0),'crossed':acb(0)},errors),
                (state,{'positive':'0','crossed':'-1','vacuum':'0'})]:
    try:o.normalize(raw,err)
    except ValueError:pass
    else:raise AssertionError('Invalid or incomplete acquisition accepted')
report={'schema':'marici.grothendieck.three-channel-cubic-tests.v1','passed':True,
        'crossed_separation_at_1e_minus543':fine,
        'crossed_separation_at_1e_minus540':coarse,
        'reused_record_separation_at_1e_minus540':reuse_comparison,
        'vacuum_separation_despite_poor_feature_precision':vac_result,
        'joint_l1_only_separation':joint,
        'checks':['calibration endpoint coverage without a source amplitude prior',
                  'calibration uncertainty blocks spurious separation',
                  'missing vacuum data rejected','negative error rejected'],
        'scope':'Interval-model and synthetic prediction fixtures; no physical acquisition or value of w_seam is inferred.'}
(m.base.RESULTS/'three-channel-cubic-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print('PASS: coordinate enclosures, conditioning, calibration-aware separation, vacuum independence and joint l1 geometry')

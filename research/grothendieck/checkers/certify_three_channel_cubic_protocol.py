"""Three independently retained cubic coordinates, calibrated in one protocol.

Private bin-filter rows isolate v0 and vx; an independently acquired unit
vacuum row isolates k. Includes all 720 minimal six-event cubic basis products.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import runpy,json,math,hashlib
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/grothendieck/results'
build=runpy.run_path(str(Path(__file__).with_name('build_time_bin_cubic_observer.py')),run_name='__main__')
exact=build['exact'];audit=exact['audit'];g=audit['g']
raw_derivative=audit['raw_derivative'];join=audit['join']

names=('positive','crossed','vacuum')
shapes={
 'positive':((('e',0,1,1),('e',3,7,1),('e',15,31,0)),(0,0,0,0)),
 'crossed':((('e',0,1,1),('e',5,7,1),('e',15,31,0)),(0,0,0,0)),
 'vacuum':((('e',0,1,0),('e',3,7,0),('e',15,31,0)),(0,0,0,0))}
expected={
 'positive':(((0,1),(2,3),(4,5)),(1,1,0)),
 'crossed':(((0,2),(1,3),(4,5)),(1,1,0)),
 'vacuum':(((0,1),(2,3),(4,5)),(0,0,0))}
hits={name:[] for name in names};degrees={i:0 for i in range(4)};count=0
for pairs in g['pairings'](tuple(range(6))):
    for kinds in product((0,1),repeat=3):
        signature=(tuple(map(tuple,pairs)),tuple(kinds));degrees[sum(kinds)]+=1
        start=0;factors=[]
        for pair,kind in zip(pairs,kinds):
            factors.append(raw_derivative(start,pair,kind))
            start|=sum(1<<p for p in pair)
        values={name:0 for name in names};reuse_value=Counter()
        for triple in product(*factors):
            seams,buffers,c=join(join(triple[0],triple[1]),triple[2])
            shape=(seams,tuple(map(len,buffers)))
            if shape in exact['J']:
                windows=[]
                for i,seam in enumerate(seams):
                    windows.extend(buffers[i])
                    if seam[3]:windows.append((seam[1],seam[2]))
                windows.extend(buffers[-1])
                reuse_value[tuple(windows)]+=c*exact['J'][shape]
            for name in names:
                if shape==shapes[name]:values[name]+=c
        nonzero={w:c for w,c in reuse_value.items() if c}
        if signature==expected['crossed']:
            assert len(nonzero)==16 and set(nonzero.values())=={16}
        else:assert not nonzero
        for name,value in values.items():
            if value:
                assert signature==expected[name] and value==1
                hits[name].append({'source_column':count,'signature':signature,'coefficient':value})
        count+=1
assert count==720 and degrees=={0:90,1:270,2:270,3:90}
assert all(len(hits[n])==1 for n in names)

ctx.prec=384
E={'positive':build['N0'],
   'crossed':build['response'](exact['A1'])*build['response'](exact['b']['D']),
   'vacuum':arb(1)}
assert all(e>0 for e in E.values())

def qp(q):return [str(q.numerator),str(q.denominator)]
def lower_pair(x):return qp(x.lower().fmpq())
def upper_pair(x):return qp(x.upper().fmpq())
def round_inverse(value):
    exponent=math.floor(float(value.log()/arb(10).log()))-8
    n=round(float(value/(arb(10)**exponent)))
    q=Fraction(n*10**max(exponent,0),10**max(-exponent,0))
    return [str(q.numerator),str(q.denominator)],arb(q.numerator)/q.denominator

channels={};G={};delta={}
for name in names:
    pair,G[name]=round_inverse(1/E[name]) if name!='vacuum' else (['1','1'],arb(1))
    delta[name]=arb(abs(G[name]*E[name]-1).upper())
    channels[name]={'shape':shapes[name],'source_signature':expected[name],
                    'forward_gain_lower':lower_pair(E[name]),'forward_gain_upper':upper_pair(E[name]),
                    'rational_inverse':pair,'relative_calibration_defect_upper':upper_pair(delta[name]),
                    'raw_test_norm_upper':['1','1']}
assert delta['vacuum'].is_zero()
reuse_pair,reuse_gain=round_inverse(1/build['Nx'])
reuse_defect=arb(abs(reuse_gain*build['Nx']-1).upper())
reuse_channel={**channels['crossed'],
               'shape':None,'source_readout':'signed sum Jx of the 448 matched feature blocks',
               'forward_gain_lower':lower_pair(build['Nx']),
               'forward_gain_upper':upper_pair(build['Nx']),
               'rational_inverse':reuse_pair,
               'relative_calibration_defect_upper':upper_pair(reuse_defect)}
assert exact['reserve'][0]==shapes['positive'] and exact['reserve'][1]==1
reuse_error=reuse_gain*arb('1e-540')+reuse_defect/2
assert reuse_error<arb('0.04')
assert G['crossed']/reuse_gain>arb('63')
# These are scoped coefficient budgets, not a global relative source guarantee.
errors={'positive':G['positive']*arb('1e-543')+delta['positive'],
        'crossed':G['crossed']*arb('1e-543')+delta['crossed']/2}
assert errors['positive']<arb('0.01') and errors['crossed']<arb('0.01')
# The previous scalar-observer noise budget does not resolve a half-unit crossed reading privately.
assert G['crossed']*arb('1e-540')>1
# Vacuum separation remains symbolic in w>0; never set w=1.
vacuum_difference=Fraction(1,10**10);vacuum_error=Fraction(25,10**12)
assert vacuum_difference-2*vacuum_error>0

filter_path=OUT/'time-bin-cubic-observer.json'
manifest={'schema':'marici.grothendieck.three-channel-cubic-protocol.v1',
          'filter_manifest':filter_path.name,'filter_manifest_sha256':hashlib.sha256(filter_path.read_bytes()).hexdigest(),
          'parameters':{'A':2,'y':3,'gamma':1,'source_domain':'J3 in the fixed six-event corner',
                        'prime_labels':[2,3,5,7,11,13],'vertex_rule':'2 times product of primes selected by bit mask'},
          'channel_order':list(names),'channels':channels,
          'modes':{'private':{'raw_records':3},
                   'reuse':{'raw_records':450,'crossed_channel':reuse_channel,
                            'aggregation':'Use all 449 retained raw bin-filter readings: sum the 448 crossed-labelled rows with their signs for Jx; retain the reserved positive row separately. Independently acquire the vacuum row. Do not try to reconstruct these from the combined scalar observer.'}},
          'default_mode':'private',
          'source_model':'raw=(E0*a, Ex*b, c) on x=a*v0+b*vx+c*k+nuisance; all other 717 minimal cubic basis products are nuisance',
          'variance':'linear source coefficients; no physical w_seam^2 multiplier or final conjugation in these coordinates',
          'acquisition':'Private mode uses two private joint bin-filter readings. Reuse mode retains the two labelled combinations from the 449 raw feature readings. Both require a separately acquired unit vacuum scalar, not an arithmetic feature reading.',
          'vacuum_example':{'coefficient_difference':'1e-10*w_seam','per_reading_error':'2.5e-11*w_seam',
                            'assumption':'w_seam>0; no numerical value is assigned'},
          'precision_bits':2048}
path=OUT/'three-channel-cubic-protocol.json'
path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
report={'schema':'marici.grothendieck.three-channel-cubic-certificate.v1','passed':True,
        'manifest_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'source_audit':{'minimal_cubic_columns':count,'columns_by_retained_degree':degrees,
                        'nonzero_columns':hits,'exact_rank':3,'nuisance_columns':717},
        'rigorous_balls':{name:{'raw_gain':str(E[name]),'rational_inverse_norm_upper':str(G[name]),
                               'relative_calibration_defect_upper':str(delta[name])} for name in names},
        'conditional_example_errors':{name:str(e) for name,e in errors.items()},
        'reuse_mode':{'rational_crossed_inverse_norm_upper':str(reuse_gain),
                      'crossed_error_at_1e_minus540_for_coefficient_bound_one_half':str(reuse_error),
                      'private_to_reuse_crossed_gain_ratio':str(G['crossed']/reuse_gain),
                      'all_720_columns_checked':True},
        'claims':{'normalized_positive_and_crossed_errors_below_0_01_at_stated_budgets':True,
                  'private_crossed_noise_amplification_exceeds_one_at_1e_minus540':True,
                  'vacuum_example_separation_for_every_positive_w':True},
        'scope':'Rank-three calibrated measurements on the declared J3 corner, not full source reconstruction. Calibration intervals share parameters and are not assumed probabilistically independent. Physical acquisition accuracy is external.'}
(OUT/'three-channel-cubic-certificate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))

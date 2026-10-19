"""Exact tensor-chart transport of the anchored PN obstruction packet."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import sys,json,gzip,hashlib,itertools
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima'))
from anchored_contact_comparisons import R,restore,recover,prepare
from eight_sector_pn_transport import action,encode,decode,transition,expanded_block,validate
from exact_multiradical import sqrt,serialize
OUT=ROOT/'research/nima/results/eight-sector-PN-transport';OUT.mkdir(exist_ok=True)
inputs={}
def load(path,compressed=False):
    raw=path.read_bytes();inputs[path]=hashlib.sha256(raw).hexdigest()
    return json.loads(gzip.decompress(raw) if compressed else raw)
base=ROOT/'research/strominger/results'
receipt=load(base/'eight-sector-interface/verification.json')
assert receipt['status']=='pass'
# Read-only freshness gate: never import the source checker's writing modules.
for name,digest in receipt['sourceHashes'].items():
    p=ROOT/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,('stale source receipt',name)
    inputs[p]=digest
archive=load(ROOT/'research/nima/results/anchored-PN-contact/packets.json.gz',True)
sourceReceipt=load(ROOT/'research/nima/results/anchored-PN-contact/verification.json')
assert inputs[ROOT/'research/nima/results/anchored-PN-contact/packets.json.gz']==sourceReceipt['packetsSha256']
descriptor=archive['descriptor'];charts=receipt['unnormalizedCharts'];names=list(charts)
transitions={(r['target'],r['source']):r['matrix'] for r in receipt['transitions']}
provenance={'sourceDescriptor':descriptor,'chartReceiptSha256':inputs[base/'eight-sector-interface/verification.json'],
            'nativeRefinementChanged':False,'readerAssignment':'none; one full N field embedded isometrically in comparison workspace'}
# The original three neutron sectors are the INTERNAL 36 coordinates. The
# eight-sector index is a distinct OUTER tensor axis. No 3-to-8 relabelling.
cube=receipt['sectorSigns']
profiles={'native-coarse-slot':[R(F(x))*sqrt(F(1,2)) for x in charts[receipt['nativeAxis']][0]],
          'parity-difference':[R(F(s[0]*s[1]*s[2]))*sqrt(F(1,8)) for s in cube]}
Nports=[p for c in descriptor['carriers'] if c['id']=='N' for p in c['ports']]
Pports=[p for c in descriptor['carriers'] if c['id']=='P' for p in c['ports']]
metrics=[F(v) for p in Nports for v in p['metric']]
def nfield(values):return [x for p in Nports for x in values[p['id']]]
def weighted_gram(columns):
    return [[sum((a.conj()*b*metrics[k%36] for k,(a,b) in enumerate(zip(u,v))),R()) for v in columns] for u in columns]
counts={'packetRecoveries':0,'identityAndRoundTrips':0,'compositionTriangles':0,'expandedBlockChecks':0,'residualGrams':0}
results={};saved={}
for profileName,profile in profiles.items():
    # Full matrix identities independently audit imported chart transitions.
    for a,b,c in itertools.product(names,repeat=3):
        for j in range(8):
            e=[R(int(k==j)) for k in range(8)]
            assert action(transitions[c,b],action(transitions[b,a],e))==action(transitions[c,a],e)
    routePairs=[]
    for route in archive['relativeContrastRoutes']:
        left=route['convertAfterSourceRotation'];right=route['rotateAfterConversion']
        lv=recover(left,descriptor);rv=recover(right,descriptor)
        assert all(lv[p['id']]==rv[p['id']] for p in Pports)
        routePairs.append((left,right,lv,rv))
    gramByChart={}
    for chart in names:
        columns=[]
        for j,(left,right,lv,rv) in enumerate(routePairs):
            lp=encode(left,descriptor,charts,profile,provenance,chart)
            rp=encode(right,descriptor,charts,profile,provenance,chart)
            assert decode(lp,descriptor,charts,profile,provenance)==left
            assert decode(rp,descriptor,charts,profile,provenance)==right
            counts['packetRecoveries']+=2
            w=list(map(restore,lp['weights']))
            assert sum((x.conj()*x for x in w),R())==R(1)
            # Reconstruct workspace fields from the expanded anchor column,
            # rather than merely asserting that decoding the core is possible.
            for pkt,original in [(lp,lv),(rp,rv)]:
                anchor=pkt['core']['anchor'];ap=anchor['port'];ai=anchor['coordinate'];av=restore(anchor['value'])
                assert ap.startswith('P:') # source fixtures give an unchanged P anchor
                am=F(next(p for p in Pports if p['id']==ap)['metric'][ai])
                from anchored_contact_comparisons import inverse
                inv=inverse(av.conj()*am)
                for s in range(8):
                    for p in Nports:
                        block=expanded_block(pkt,p['id'],ap,s,None)
                        assert [row[ai]*inv for row in block]==[w[s]*x for x in original[p['id']]]
                # Each of all 900 source block types obeys isometric pullback.
                # Expand one nonzero sector pair fully, independently compare
                # entries with outer products of workspace coordinate vectors.
                s=next(i for i,x in enumerate(w) if x!=0)
                for tc in descriptor['carriers']:
                    for t in tc['ports']:
                        for sc in descriptor['carriers']:
                            for p in sc['ports']:
                                tw=w[s] if tc['id']=='N' else R(1);sw=w[s] if sc['id']=='N' else R(1)
                                block=expanded_block(pkt,t['id'],p['id'],s if tc['id']=='N' else None,s if sc['id']=='N' else None)
                                expected=[[tw*x*(sw*y).conj()*F(p['metric'][k]) for k,y in enumerate(original[p['id']])] for x in original[t['id']]]
                                assert block==expected;counts['expandedBlockChecks']+=1
            d=[a-b for a,b in zip(nfield(rv),nfield(lv))]
            columns.append([x*v for x in w for v in d])
            # Original packet, including cross comparisons and anchor, survives.
            assert lp['core']['blocks']!=rp['core']['blocks']
            if j==0:saved[profileName,chart]=lp
        gram=weighted_gram(columns);assert gram==[[R(3),R()],[R(),R(3)]]
        gramByChart[chart]=serialize(gram);counts['residualGrams']+=1
    # Exact identity/inverse/cocycle on complete factored packets.
    origin=saved[profileName,names[0]]
    for a,b,c in itertools.product(names,repeat=3):
        pa=transition(origin,a,descriptor,charts,transitions,profile,provenance)
        pb=transition(pa,b,descriptor,charts,transitions,profile,provenance)
        pc=transition(pb,c,descriptor,charts,transitions,profile,provenance)
        direct=transition(pa,c,descriptor,charts,transitions,profile,provenance)
        assert pc==direct;counts['compositionTriangles']+=1
    for a in names:
        pa=transition(origin,a,descriptor,charts,transitions,profile,provenance)
        assert transition(pa,a,descriptor,charts,transitions,profile,provenance)==pa
        assert transition(pa,names[0],descriptor,charts,transitions,profile,provenance)==origin
        counts['identityAndRoundTrips']+=1
    results[profileName]={'residualGrams':gramByChart}
    print(profileName,'passes',flush=True)
# Projection hostile on the ACTUAL two-column PN discrepancy, not a toy scalar.
parity=profiles['parity-difference'];averageGram={}
for chart in names:
    w=list(map(restore,saved['parity-difference',chart]['weights']))
    ds=[]
    for left,right,lv,rv in routePairs:
        d=[a-b for a,b in zip(nfield(rv),nfield(lv))];ds.append([x*v for x in w[:4] for v in d])
    averageGram[chart]=serialize(weighted_gram(ds))
    if chart!='antipodal':assert weighted_gram(ds)==[[R(),R()],[R(),R()]]
# Chart antipodal averages also kill this odd-parity profile.
assert averageGram['antipodal']==[[{},{}],[{},{}]]
controls=[]
profile=profiles['parity-difference'];original=saved['parity-difference',names[0]]
def reject(name,mutator):
    p=deepcopy(original);mutator(p)
    try:validate(p,descriptor,charts,profile,provenance)
    except (AssertionError,KeyError,IndexError,ValueError):controls.append(name)
    else:raise AssertionError('accepted '+name)
reject('drop-differences',lambda p:p['weights'].__setitem__(slice(4,None),[{}]*4))
reject('chart-label-only-change',lambda p:p.update(chart='antipodal'))
reject('source-origin-drift',lambda p:p['provenance']['sourceDescriptor']['markedReaders'][0].update(origin=999))
reject('missing-source-neutron-sector',lambda p:p['core']['blocks'].pop(Nports[-1]['id']))
reject('forged-cross-comparison',lambda p:p['core']['blocks'][Pports[0]['id']][Nports[0]['id']][0].__setitem__(0,{'1':'999'}))
reject('unnormalized-profile',lambda p:p['profile'].__setitem__(0,{'1':'9'}))
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in inputs.items())
for p in [Path(__file__).resolve(),ROOT/'research/nima/eight_sector_pn_transport.py',ROOT/'research/nima/anchored_contact_comparisons.py',ROOT/'research/nima/eight-sector-PN-transport-v1.md']:
    inputs[p]=hashlib.sha256(p.read_bytes()).hexdigest()
report={'schema':'marici.nima.eight-sector-PN-transport.v1','status':'pass','counts':counts,'profiles':results,
        'averageOnlyResidualGrams':averageGram,'negativeControls':controls,
        'representation':'Separable factored operator comparisons: original anchored core plus explicit normalized sector profile and chart weights. Expanded blocks generated and tested; no original field sidecar.',
        'scope':'Two declared isometric embeddings of one complete N field, with unchanged P. Outer eight-sector index is separate from the three internal N sectors. Not four independent native readers, a locality theorem, geometric sewing or a new native move.',
        'sourceHashes':{p.relative_to(ROOT).as_posix():h for p,h in inputs.items()}}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'pass','counts':counts,'negativeControls':controls}))

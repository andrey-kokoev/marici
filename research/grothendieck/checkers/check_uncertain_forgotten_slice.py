"""Audit labelled transfer, interval inverses and recoverable acquisition evidence."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations
import importlib.util,json,copy,tempfile,subprocess,sys,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
vp=HERE.parent/'certificates'/'reconstruct_uncertain_forgotten_slice.py';v=module('adapter',vp)
owner_path=ROOT/'research/voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py';owner=module('owner',owner_path)
protected=[OUT/'calibration-refinement-frozen-inputs.json',OUT/'three-channel-source-task-calibration-bulk-norm.json',OUT/'order16-vacuum-acquisition-inputs.json']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hashes={p.name:sha(p) for p in protected}
folder=OUT/'uncertain-forgotten-slice';folder.mkdir(exist_ok=True)

def payload(A,y,radius=Q(0)):
    return {'schema':'labelled-forgotten-ideal-interval-readings-v1','background':A,'model_sha256':v.digest(v.model(A)),
            'readings':{name:[str(value-radius),str(value+radius)] for name,value in zip(v.IDS,y)},
            'terminal_check':['0','0'],
            'provenance':{'kind':'synthetic','support_evidence':None,'error_contract':None}}
def apply(R,a):return [sum(Q(c)*x for c,x in zip(row,a)) for row in R]
exact=0;corners=0;reports={}
for A in (2,3,4):
    m=v.model(A);R=m['forward_matrix']
    assert m['inverse_matrix']==owner.MODEL['inverse_matrix_path_coefficients_from_readings']
    for row,old in zip(m['rows'],owner.MODEL['readings']):
        assert [[Q(x, A) for x in edge] for edge in row['seams']]==[[Q(x,2) for x in edge] for edge in old['arithmetic_seams']]
    # Independent cut enumeration of all forgotten orders: transferred PPP and
    # QQQ rows remain distinct unit coefficient selectors, not arbitrary gains.
    for idx,word in ((0,v.path(0)),(1,v.path(7))):
        assert [(p,v.record(A,p,m['rows'][idx]['seams'])) for p in permutations(v.P) if v.record(A,p,m['rows'][idx]['seams'])]==[(word,1)]
    sources=[]
    for j in range(1,8):sources.append([Q(int(i==j)-int(i==0)) for i in range(8)])
    for T in range(1,8):sources.append([Q((-1)**(T.bit_count()-i.bit_count())) if i&T==i else Q(0) for i in range(8)])
    sources.extend([[Q(0)]*8,list(map(Q,(-28,1,2,3,4,5,6,7)))])
    for a in sources:
        y=apply(R,a);p=payload(A,y);o=v.reconstruct(json.loads(json.dumps(p)))
        assert list(map(Q,o['compatible_set']['center']))==a
        assert v.recover(json.loads(json.dumps(o)))==p
        if A==2:
            old=owner.reconstruct({'schema':'seven-dimensional-ideal-readings-v1','model_sha256':owner.MODEL_SHA256,
                                   'readings':dict(zip(v.IDS,map(str,y))),'terminal_check':'0'})
            assert old['path_coefficients']==o['compatible_set']['center']
            for r,key in ((1,'I'),(2,'I_squared'),(3,'I_cubed'),(4,'I_fourth')):
                assert (o['filtration_certificates'][str(r)]=='guaranteed')==old['filtration_membership'][key]
        exact+=1
    # Full reading-basis roundtrip.
    for j in range(7):
        y=[Q(int(i==j)) for i in range(7)];o=v.reconstruct(payload(A,y))
        assert apply(R,list(map(Q,o['compatible_set']['center'])))==y;exact+=1
    cubic=[Q((-1)**i.bit_count()) for i in range(8)]
    p=payload(A,apply(R,cubic),Q(1,100));o=v.reconstruct(p)
    assert o['filtration_certificates']=={'1':'guaranteed','2':'undetermined','3':'undetermined','4':'ruled_out_by_a_coordinate'}
    center=list(map(Q,o['compatible_set']['center']));G=[list(map(Q,row)) for row in o['compatible_set']['generators']]
    samples=[]
    for signs in product((-1,1),repeat=7):
        a=[center[i]+sum(G[i][j]*signs[j] for j in range(7)) for i in range(8)]
        assert sum(a)==0
        y=apply(R,a)
        assert all(Q(p['readings'][name][0])<=x<=Q(p['readings'][name][1]) for name,x in zip(v.IDS,y))
        samples.append(a);corners+=1
    assert [[str(min(a[i] for a in samples)),str(max(a[i] for a in samples))] for i in range(8)]==o['path_marginals']
    # Marginal upper endpoints cannot be retained as an independent source box:
    # their simultaneous choice violates the ideal equation.
    assert sum(Q(b[1]) for b in o['path_marginals'])!=0
    assert max(sum(abs(Q(x)) for x in row) for row in v.B)==4
    assert max(sum(abs(Q(v.B[i][j])) for i in range(8)) for j in range(7))==4
    # Out-of-domain ideal collision persists at every audited background.
    collision=((5,2,3,7,11,13),(5,3,2,7,11,13))
    assert all(v.record(A,collision[0],row['seams'])-v.record(A,collision[1],row['seams'])==0 for row in m['rows'])
    reports[str(A)]={'model_sha256':v.digest(m),'outside_domain_collision':[list(x) for x in collision],
                     'terminal_collision_value':'0','noisy_cubic_filtration':o['filtration_certificates']}
    (folder/f'A{A}-model.json').write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
    (folder/f'A{A}-readings.json').write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8')
    (folder/f'A{A}-compatible-set.json').write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')

rejected=[]
def reject(name,change):
    p=v.load(folder/'A3-readings.json');change(p)
    try:v.reconstruct(p)
    except ValueError:rejected.append(name)
    else:raise AssertionError(name)
reject('missing reading',lambda p:p['readings'].pop('vacuum_QQQ'))
reject('unsupported background',lambda p:p.__setitem__('background',5))
reject('background changed without binding',lambda p:p.__setitem__('background',4))
reject('wrong normalization/model',lambda p:p.__setitem__('model_sha256','0'*64))
reject('numeric rather than rational reading',lambda p:p['readings']['vacuum_PPP'].__setitem__(0,0))
reject('reversed interval',lambda p:p['readings'].__setitem__('vacuum_PPP',['2','1']))
reject('contradictory terminal evidence',lambda p:p.__setitem__('terminal_check',['1','2']))
reject('source archive field',lambda p:p.__setitem__('source_archive',[0]*8))
reject('support inferred from readings',lambda p:p['provenance'].__setitem__('support_certified',True))
reject('zero denominator',lambda p:p['readings'].__setitem__('vacuum_PPP',['1/0','2']))
# Merely attaching a support reference must never promote conditional inversion.
p=v.load(folder/'A3-readings.json');p['provenance']['support_evidence']='external:unverified-support-record'
assert v.reconstruct(p)['source_domain_status'].startswith('conditional_only')
o=v.reconstruct(p);o['compatible_set']['generators'][0][0]='0'
try:v.recover(o)
except ValueError:rejected.append('corrupt joint uncertainty')
else:raise AssertionError('Corrupt output accepted')
o=v.reconstruct(p);o['model']['inverse_matrix'][0][0]=True
try:v.recover(o)
except ValueError:rejected.append('boolean substituted for structural integer')
else:raise AssertionError('Structural type corruption accepted')
with tempfile.TemporaryDirectory() as directory:
    d=Path(directory);(d/vp.name).write_bytes(vp.read_bytes())
    for A in (2,3,4):
        (d/'readings.json').write_bytes((folder/f'A{A}-readings.json').read_bytes())
        result=subprocess.run([sys.executable,'-I',str(d/vp.name),str(d/'readings.json')],cwd=d,capture_output=True,text=True)
        assert result.returncode==0,result.stderr
        (d/'output.json').write_text(result.stdout,encoding='utf-8')
        recovered=subprocess.run([sys.executable,'-I',str(d/vp.name),'--recover',str(d/'output.json')],cwd=d,capture_output=True,text=True)
        assert recovered.returncode==0,recovered.stderr
        assert json.loads(recovered.stdout)==v.load(d/'readings.json')
    for text in ('{"schema":0,"schema":1}','{"x":NaN}','{"x":0.1}'):
        (d/'bad.json').write_text(text,encoding='utf-8')
        try:v.load(d/'bad.json')
        except ValueError:rejected.append('strict JSON')
        else:raise AssertionError('Invalid JSON admitted')
assert hashes=={p.name:sha(p) for p in protected}
report={'passed':True,'exact_roundtrips':exact,'joint_noise_vertices_checked':corners,
        'adapter_sha256':sha(vp),'owner_decoder_sha256':sha(owner_path),'owner_A2_model_sha256':owner.MODEL_SHA256,
        'backgrounds':reports,'rejected_corruptions':rejected,'protected_file_hashes':hashes,
        'isolated_two_file_execution_and_input_recovery':True,
        'scope':'Conditional finite rational slice inverses and recoverable input evidence; no source support or physical error bound certified.'}
(OUT/'uncertain-forgotten-slice-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {exact} exact roundtrips; {corners} joint noise vertices; {len(rejected)} corruptions; labelled A2/A3/A4 audit and isolated evidence recovery')

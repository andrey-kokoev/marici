"""Independent ordered-cut tests for the archive-free seven-reading decoder."""
from pathlib import Path
from fractions import Fraction
import runpy,json,copy,tempfile,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
program=ROOT/'research/voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py'
d=runpy.run_path(str(program))
f=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
shapes=[tuple(('e',a,b,0) for a,b in seams) for seams in d['SEAMS']]
def source(a):return {(d['path'](i),(0,)*6):Fraction(c) for i,c in enumerate(a) if c}
def measured(col):
    return [f['vacuum_rows'](0,63,col,len(sh)).get(sh,Fraction(0)) for sh in shapes]
def payload(y,terminal=True):
    p={'schema':'seven-dimensional-ideal-readings-v1','model_sha256':d['MODEL_SHA256'],
       'readings':{name:str(c) for name,c in zip(d['IDS'],y)}}
    if terminal:p['terminal_check']='0'
    return p
def run(a):
    p=json.loads(json.dumps(payload(measured(source(a)))))
    answer=d['reconstruct'](p)
    assert list(map(Fraction,answer['path_coefficients']))==list(map(Fraction,a))
    return p,answer
# Basis identities verify the inverse on the entire rational ideal slice.
columns=[]
for j in range(1,8):
    a=[Fraction(int(i==j)-int(i==0)) for i in range(8)]
    columns.append({i:c for i,c in enumerate(measured(source(a))) if c})
    run(a)
assert f['rank'](columns)==7
# Conversely each reading-basis vector is realized by its decoded source,
# verified with the actual ordered-cut recorder, not the decoder's equations.
for j in range(7):
    y=[Fraction(int(i==j)) for i in range(7)]
    a=list(map(Fraction,d['reconstruct'](payload(y))['path_coefficients']))
    assert measured(source(a))==y
# Recover all seven ideal interaction modes and their exact ideal orders.
for t in range(1,8):
    a=[Fraction((-1)**(t.bit_count()-b.bit_count()) if b&t==b else 0) for b in range(8)]
    p,r=run(a)
    assert r['ideal_order_in_declared_slice']==t.bit_count()
    for order in range(t.bit_count()):assert not f['vacuum_rows'](0,63,source(a),order)
    assert f['vacuum_rows'](0,63,source(a),t.bit_count())
zero_p,zero_r=run([0]*8)
assert zero_r['filtration_membership']['I_fourth']
mixed_p,mixed_r=run([-28,1,2,3,4,5,6,7])
cubic_a=[(-1)**i.bit_count() for i in range(8)]
cubic_p,cubic_r=run(cubic_a)
assert cubic_r['ideal_order_in_declared_slice']==3

bad_cases=[]
x=copy.deepcopy(mixed_p);del x['readings']['vacuum_QQQ'];bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['readings']['extra']='0';bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['readings']['vacuum_PPP']=1;bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['readings']['vacuum_PPP']=True;bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['readings']['vacuum_PPP']='nan';bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['model_sha256']='0'*64;bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['terminal_check']='1';bad_cases.append(x)
x=copy.deepcopy(mixed_p);x['source_archive']={};bad_cases.append(x)
for bad in bad_cases:
    try:d['reconstruct'](bad)
    except ValueError:pass
    else:raise AssertionError('invalid input accepted')

# The readings do NOT establish their own domain assumptions.
# This cube source has nonzero total coefficient but all seven readings zero.
nonideal=source([0,1,0,-1,0,-1,0,0])
assert measured(nonideal)==[0]*7 and f['rho_column'](0,nonideal)=={():Fraction(-1)}
bad=payload(measured(nonideal));bad['terminal_check']='-1'
try:d['reconstruct'](bad)
except ValueError:pass
else:raise AssertionError('contradictory terminal record accepted')
# Even a zero terminal check cannot certify the eight-path support:
# prepend forgotten 5, swap (2,3), and append (7,11,13).
outside={((2,0,1,3,4,5),(0,)*6):Fraction(1),((2,1,0,3,4,5),(0,)*6):Fraction(-1)}
assert not f['rho_column'](0,outside) and measured(outside)==[0]*7
assert d['reconstruct'](payload(measured(outside)))['source_terms']==[]
# This is an intentionally exhibited out-of-domain collision, NOT a claim
# that the decoder recovered the unknown source outside its contract.

B=d['INVERSE']
linf=max(sum(abs(c) for c in row) for row in B)
l1=max(sum(abs(row[j]) for row in B) for j in range(7))
assert linf==l1==4
with tempfile.TemporaryDirectory() as td:
    folder=Path(td);shutil.copyfile(program,folder/'decode.py')
    (folder/'input.json').write_text(json.dumps(mixed_p),encoding='utf-8')
    call=subprocess.run([sys.executable,'-I',str(folder/'decode.py'),str(folder/'input.json')],
                        cwd=folder,capture_output=True,text=True,timeout=30)
    assert call.returncode==0,call.stderr
    assert json.loads(call.stdout)==mixed_r
    # Duplicate keys must not be accepted by the standalone JSON interface.
    text=json.dumps(mixed_p).replace('"vacuum_PPP": "-28"','"vacuum_PPP": "-28", "vacuum_PPP": "0"')
    (folder/'input.json').write_text(text,encoding='utf-8')
    call=subprocess.run([sys.executable,'-I',str(folder/'decode.py'),str(folder/'input.json')],
                        cwd=folder,capture_output=True,text=True,timeout=30)
    assert call.returncode!=0 and 'duplicate' in call.stderr
out=ROOT/'research/voevodsky/results'
for name,data in (
 ('seven-dimensional-ideal-slice-model',{'model':d['MODEL'],'model_sha256':d['MODEL_SHA256']}),
 ('seven-dimensional-ideal-readings-example',mixed_p),
 ('seven-dimensional-ideal-reconstruction-example',mixed_r),
 ('seven-dimensional-ideal-cubic-readings',cubic_p),
 ('seven-dimensional-ideal-cubic-reconstruction',cubic_r)):
    (out/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
report={'passed':True,'independent_source_dimension':7,'reconstructed_path_coefficients':8,
 'existing_vacuum_plus_additional_rows':[1,6],'forward_rank':7,
 'exact_source_basis_roundtrips':7,'exact_reading_basis_roundtrips':7,
 'interaction_modes_and_filtration_checked':7,'invalid_payloads_rejected':len(bad_cases),
 'duplicate_keys_rejected':True,'isolated_two_file_decoder_passed':True,
 'source_archive_used':False,
 'inverse_operator_norms_on_unscaled_coefficients':{'l1':l1,'linfinity':linf},
 'domain_warnings_verified':['nonideal cube source can have seven zero readings',
   'ideal source outside cube can have seven zero readings AND zero terminal check'],
 'scope':'Exact inverse on the assumed fixed ideal slice. Independent evidence of domain membership remains necessary; readout consistency alone cannot establish it. Synthetic inputs, not measured acquisition data.'}
(out/'seven-dimensional-ideal-decoder-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))

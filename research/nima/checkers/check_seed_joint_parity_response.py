# /// script
# dependencies = ["sympy"]
# ///
"""Exact linearization of the freshly proved joint source-probe response.

The integer matrices are derived from the formal Boolean updates, not fitted
seed response matrices. Scalar conjunction is a declared diagnostic question.
"""
from itertools import product
from pathlib import Path
import hashlib
import json
import re
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/seed-joint-parity-response.json'
OUT.unlink(missing_ok=True)
formal_path=ROOT/'results/agda-SeedJointParityResponse.json'
formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('formal-response-square-verified',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
for name in ('SeedJointParityResponse','SeedGeometricResponseState','SeedFaceObstruction',
             'ActualSeedEndpointTable','SeedSeamPathComparisonBoundary'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())
text=(ROOT/'agda/SeedJointParityResponse.agda').read_text(encoding='utf-8')
first=dict(re.findall(r'^first-step ([A-D]{2}) b = (not b|b)$',text,re.M))
second=dict(re.findall(r'^second-step ([A-D]{2}) b = (not b|b)$',text,re.M))
seedtext=(ROOT/'agda/ActualSeedEndpointTable.agda').read_text(encoding='utf-8')
sources=dict(re.findall(r'^source ([A-D]{2}) = ([A-D])$',seedtext,re.M))
targets=dict(re.findall(r'^target ([A-D]{2}) = ([A-D])$',seedtext,re.M))
check('all-actual-occurrence-updates-extracted',set(first)==set(second)==set(sources)==set(targets))
points=tuple(product(range(2),repeat=2)); index={p:i for i,p in enumerate(points)}
I=S.eye(4); operators={}
for e in sources:
    mask=(int(first[e]=='not b'),int(second[e]=='not b'))
    matrix=S.zeros(4)
    for i,(a,b) in enumerate(points): matrix[index[(a^mask[0],b^mask[1])],i]=1
    operators[e]=matrix
    check('reversible-existing-probe-update/'+e,matrix*matrix==I and matrix.T*matrix==I)

pathtext=(ROOT/'agda/SeedSeamPathComparisonBoundary.agda').read_text(encoding='utf-8')
legs={}
for name in ('x0','x1','y0','y1'):
    body=re.search(r'^'+name+r' = (.*)$',pathtext,re.M).group(1)
    legs[name]=tuple(re.findall(r'step ([A-D]{2})',body))
def operator(word):
    check('typed-word/'+','.join(word),all(targets[e]==sources[f] for e,f in zip(word,word[1:])))
    out=I
    for e in word: out=operators[e]*out
    return out
X=[operator(legs[f'x{i}']) for i in range(2)]
Y=[operator(legs[f'y{j}']) for j in range(2)]
C={(i,j):operator(legs[f'x{i}']+legs[f'y{j}']) for i,j in product(range(2),repeat=2)}
for (i,j),matrix in C.items(): check(f'actual-sequential-factorization/{i}{j}',matrix==Y[j]*X[i])
initial=I[:,0]
readings={ij:points[list(matrix*initial).index(1)] for ij,matrix in C.items()}
check('four-corners-separated',len(set(readings.values()))==4)
check('formal-corner-values-match',all(readings[i,j]==(1-i,1-j) for i,j in C))
mixed=C[1,1]-C[1,0]-C[0,1]+C[0,0]
check('mixed-factorization',mixed==(Y[1]-Y[0])*(X[1]-X[0]))
check('mixed-is-nonzero-rank-one',mixed.rank()==1 and mixed.trace()==4)
check('commuting-does-not-erase-mixed-response',X[0]*Y[0]==Y[0]*X[0])
vector=mixed*initial
check('mixed-record-vector',list(vector)==[1,-1,-1,1])
reader=S.Matrix([[a*b for a,b in points]])
check('declared-conjunction-contrast', (reader*vector)[0]==1)
check('either-probe-alone-has-zero-mixed-contrast',all((S.Matrix([[p[k] for p in points]])*vector)[0]==0 for k in range(2)))
check('finite-probes-do-not-recover-whole-history',operator(legs['x0']+legs['y1'])**3==operator(legs['x0']+legs['y1']))
result={
    'schema':'marici.nima.seed-joint-parity-response.v1','verification_status':'pass','checks':checks,
    'formal_receipt_sha256':hashlib.sha256(formal_path.read_bytes()).hexdigest(),
    'point_order':[list(p) for p in points],
    'actual_corners':{f'{i}{j}':{'word':list(legs[f'x{i}']+legs[f'y{j}']),'reading':list(readings[i,j])} for i,j in C},
    'mixed_matrix':[[int(v) for v in row] for row in mixed.tolist()],
    'mixed_record_vector':list(map(int,vector)), 'mixed_rank':1,'mixed_trace':4,
    'declared_conjunction_contrast':1,
    'scope':'Derived finite observer of existing geometric response; exact integer linearization. Conjunction is a declared diagnostic, not a physically selected scalar or calibration.',
    'boundaries':['No identification of this four-value observer with rung4.',
                  'No source admission of the four-corner product as replacement for the two-triangle context.',
                  'No identification with the existing2x2 matrix fixture or its1/15 contrast.',
                  'Directed history and geometric state remain retained beyond this finite observer.']}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact joint-parity response checks')
print('All four native seam outputs separated; mixed record vector=(1,-1,-1,1).')
print('Scalar conjunction contrast=1 is a declared diagnostic, not a physical normalization.')

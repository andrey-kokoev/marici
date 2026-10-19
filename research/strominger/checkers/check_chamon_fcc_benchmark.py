"""Actual FCC incidence -> signed Chamon stabilizers -> published reference.

Imports selected, content-pinned upstream functions without a NumPy dependency.
Also matches the native operators to Shirley--Liu--Dua Eq. (C1).
"""
from pathlib import Path
from itertools import product
from types import SimpleNamespace
from math import gcd
import ast,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger/results'
UPSTREAM=ROOT/'research/strominger/references/chamon-decoder-upstream'
PINS={'chamdec_stabs_syndromes.py':'194d9ad3b5b2a0ecc1a64cc99b044392024bcb6d',
      'chamdec_conversions.py':'840909bdf1c9b1e4f761c01a551fc6e3e6a81177'}
class ZeroArray:
    """Only the zero-allocation and indexed assignment used by the builder."""
    def __init__(self,shape):self.rows=[[0]*shape[1] for _ in range(shape[0])]
    def __setitem__(self,key,value):
        i,j=key;self.rows[i][j]=value

def imported_functions(filename,names):
    data=(UPSTREAM/filename).read_bytes()
    digest=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert digest==PINS[filename],('Upstream source changed',filename)
    tree=ast.parse(data.decode('utf-8'),filename=filename)
    definitions=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in definitions}==set(names)
    env={'np':SimpleNamespace(zeros=ZeroArray)}
    exec(compile(ast.Module(body=definitions,type_ignores=[]),filename,'exec'),env)
    return {name:env[name] for name in names}
build=imported_functions('chamdec_stabs_syndromes.py',['create_chamon_stabs'])['create_chamon_stabs']
convert=imported_functions('chamdec_conversions.py',['qubit_2_location','stab_2_location'])

# Word (x,z,p) means i^p X^x Z^z; Y = i X Z. Keep scalar phases.
IDENTITY=(0,0,0)
def mul(a,b):return (a[0]^b[0],a[1]^b[1],(a[2]+b[2]+2*(a[1]&b[0]).bit_count())%4)
def atom(qubit,pauli):
    b=1<<qubit
    return {'X':(b,0,0),'Y':(b,b,1),'Z':(0,b,0)}[pauli]
def word(factors):
    result=IDENTITY
    for q,p in factors:result=mul(result,atom(q,p))
    return result
def commute(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2==0
def eliminate(words,n):
    basis={};relations=[]
    for index,w in enumerate(words):
        coefficients=1<<index
        while w[0] or w[1]:
            pivot=(w[0]|(w[1]<<n)).bit_length()-1
            if pivot not in basis:
                basis[pivot]=(w,coefficients);break
            b,mask=basis[pivot];w=mul(w,b);coefficients^=mask
        else:relations.append((coefficients,w[2]))
    return len(basis),relations

def prove(words,n):
    assert all(mul(w,w)==IDENTITY for w in words),'Non-involutory generator'
    assert all(commute(a,b) for i,a in enumerate(words) for b in words[i+1:]),'Noncommuting generators'
    rank,relations=eliminate(words,n)
    assert all(phase==0 for _,phase in relations),'Minus identity or nontrivial scalar in stabilizer group'
    assert len(relations)==len(words)-rank
    return rank,relations

def compare_support(actual,reference):
    assert actual[:2]==reference[:2],'Upstream coordinate/support mismatch'
def show(w):return {'X':hex(w[0]),'Z':hex(w[1]),'iExponent':w[2]}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

# Primitive FCC coordinates matching the paper's cubic presentation. These
# are lattice coordinates: do not replace the physical FCC metric by I.
def primitive(v):
    x,y,z=v;nums=(y+z-x,x+z-y,x+y-z)
    assert all(t%2==0 for t in nums)
    return tuple(t//2 for t in nums)
def physical(u):return (u[1]+u[2],u[0]+u[2],u[0]+u[1])

# Eq. (C1), arXiv:2206.12791v1: the two Laurent columns are represented by
# exponent sets over F2. X_native -> Z_paper, Y_native -> X_paper,
# Z_native -> Y_paper. The check anchor in FCC coordinates is center+111.
SX={(0,-1,0),(0,0,-1),(-1,-1,0),(-1,0,-1)}
SZ={(-1,0,0),(0,0,-1),(-1,-1,0),(0,-1,-1)}
CYCLE={'X':'Z','Y':'X','Z':'Y'}
basis=[physical(tuple(int(i==j) for j in range(3))) for i in range(3)]
assert [[sum(a*b for a,b in zip(v,w)) for w in basis] for v in basis]==[[2,1,1],[1,2,1],[1,1,2]]
def pmul(a,b):
    result=set()
    for v in a:
        for w in b:
            term=tuple(x+y for x,y in zip(v,w))
            if term in result:result.remove(term)
            else:result.add(term)
    return result
pinv=lambda a:{tuple(-x for x in v) for v in a}
assert pmul(pinv(SX),SZ)^pmul(pinv(SZ),SX)==set()
assert all(CYCLE[CYCLE[CYCLE[p]]]==p for p in CYCLE)
assert mul(atom(0,CYCLE['X']),atom(0,CYCLE['Y']))==mul((0,0,1),atom(0,CYCLE['Z']))

subprocess.run(['node',str(Path(__file__).with_name('export_chamon_fcc_covers.mjs'))],cwd=ROOT,check=True,capture_output=True,text=True)
geometry_path=BASE/'chamon-fcc-covers/verification.json'
geometry=json.loads(geometry_path.read_text())
for path,digest in geometry['sourceHashes'].items():assert sha(ROOT/path)==digest
class_labels={(1,0,0):'A',(0,1,0):'B',(0,0,1):'C',(1,1,1):'D'}
class_dictionary={label:tuple((x+1)%2 for x in bits) for bits,label in class_labels.items()}
assert set(class_dictionary.values())==set(map(tuple,geometry['classes']))
reports=[];cached={};polynomial_squares=0
for cover in geometry['covers']:
    lengths=tuple(cover['lengths']);assert all(L%2==0 for L in lengths)
    half=tuple(x//2 for x in lengths);sites=list(map(tuple,cover['qubits']));n=len(sites)
    indices={v:i for i,v in enumerate(sites)};centers={tuple(o['center']):i for i,o in enumerate(cover['octahedra'])}
    assert len(indices)==len(centers)==n
    assert all(sum(v)%2==0 and physical(primitive(v))==v for v in sites)
    words=[];groups={label:[] for label in class_labels.values()}
    for index,octa in enumerate(cover['octahedra']):
        factors=octa['factors'];center=tuple(octa['center'])
        assert len(factors)==6
        for f in factors:
            assert sites[f['qubit']]==tuple(f['wrapped'])
            assert all(u==v+d*L for u,v,d,L in zip(f['unwrapped'],f['wrapped'],f['deck'],lengths))
        actual=word([(f['qubit'],f['pauli']) for f in factors]);words.append(actual)
        groups[class_labels[tuple(octa['classBits'])]].append(index)
        # Import the published Laurent operator in the same physical cover.
        anchor=tuple(x+1 for x in center)
        assert sum(anchor)%2==0
        poly_factors=[]
        for exponent in sorted(SX|SZ):
            point=tuple(a+d for a,d in zip(anchor,physical(exponent)))
            wrapped=tuple(x%L for x,L in zip(point,lengths))
            label='Y' if exponent in SX&SZ else ('X' if exponent in SX else 'Z')
            poly_factors.append((indices[wrapped],label))
        transformed=word([(f['qubit'],CYCLE[f['pauli']]) for f in factors])
        assert transformed==word(poly_factors),('Published operator mismatch',lengths,center)
        polynomial_squares+=1
    rank,relations=prove(words,n)
    class_products={}
    for label,rows in groups.items():
        result=IDENTITY
        for i in rows:result=mul(result,words[i])
        assert result==IDENTITY,('Class product',lengths,label,result)
        assert len(rows)==n//4;class_products[label]={'checks':len(rows),'product':show(result)}
    logical=4*gcd(*half);assert n-rank==logical,('Ground space',lengths,rank,logical)
    reference=None
    if min(lengths)>=4:
        # The original upstream function body is unchanged. Its NumPy zeros
        # allocation is replaced by a plain indexed zero array only.
        matrix=build(*half).rows;assert len(matrix)==n and all(len(row)==2*n for row in matrix)
        ref_sites=[];ref_centers=[]
        for z in range(lengths[2]):
            for y in range(lengths[1]):
                for i in range(half[0]):
                    ref_sites.append((2*i+(y+z)%2,y,z));ref_centers.append((2*i+1-(y+z)%2,y,z))
        if len(set(lengths))==1:
            assert [convert['qubit_2_location'](i,half[0]) for i in range(n)]==ref_sites
            assert [convert['stab_2_location'](i,half[0]) for i in range(n)]==ref_centers
        mismatches=[]
        for row,center in zip(matrix,ref_centers):
            x=z=0
            for j,point in enumerate(ref_sites):
                bit=1<<indices[point]
                if row[j]:x|=bit
                if row[n+j]:z|=bit
            actual=words[centers[center]]
            if (x,z)!=actual[:2]:mismatches.append(center)
            compare_support(actual,(x,z))
            # Positive tensor-Pauli convention supplies the phase absent from
            # the upstream binary support matrix, and matches native factors.
            assert (x,z,(x&z).bit_count()%4)==actual
        assert not mismatches,('Upstream coordinate/support mismatch',mismatches)
        reference={'function':'create_chamon_stabs','parameters':half,'rowsCompared':n,'supportMismatches':0,
                   'coordinateHelpersChecked':len(set(lengths))==1,'zeroArrayAdapter':True,
                   'binaryMatrixSHA256':hashlib.sha256(json.dumps(matrix,separators=(',',':')).encode()).hexdigest()}
    else:
        assert lengths==(2,2,2) and all(w==IDENTITY for w in words) and rank==0
    periods=[primitive(tuple(L if j==i else 0 for j in range(3))) for i,L in enumerate(lengths)]
    report={'lengths':lengths,'spins':n,'stabilizers':len(words),'commutingPairsChecked':n*(n-1)//2,
            'binaryRank':rank,'relationRank':len(relations),'logicalQubits':n-rank,'groundSpaceDimension':1<<(n-rank),
            'minusIdentityAbsent':True,'classProducts':class_products,'upstreamComparison':reference,
            'primitivePeriodGenerators':periods,'signedGenerators':[show(w) for w in words],
            'kernelRelations':[{'generatorMask':hex(mask),'iExponent':phase} for mask,phase in relations]}
    reports.append(report);cached[lengths]=(cover,words)

# Mutation controls distinguish signs, noncommutation, coordinate order and
# repeated-site multiplication. These are not merely count comparisons.
controls=[];cover,words=cached[4,4,4];n=len(words)
bad=words.copy();x,z,p=bad[0];bad[0]=(x,z,(p+2)%4)
try:prove(bad,n)
except AssertionError as e:
    assert 'identity' in str(e);controls.append('flipped_generator_sign')
else:raise AssertionError('Sign corruption accepted')
factors=cover['octahedra'][0]['factors'];corrupt=[(f['qubit'],f['pauli']) for f in factors];corrupt[0]=(corrupt[0][0],'Z')
bad=words.copy();bad[0]=word(corrupt)
try:prove(bad,n)
except AssertionError as e:
    assert 'Noncommuting' in str(e);controls.append('single_site_axis_corruption')
else:raise AssertionError('Axis corruption accepted')
try:compare_support(words[0],words[1])
except AssertionError:controls.append('wrong_check_coordinate_alignment')
else:raise AssertionError('Wrong coordinate alignment accepted')
small,small_words=cached[2,2,2]
deduplicated=word(list(dict.fromkeys((f['qubit'],f['pauli']) for f in small['octahedra'][0]['factors'])))
assert deduplicated!=small_words[0];controls.append('repeated_factor_deduplication')

report={'schema':'marici.chamon-fcc-benchmark.v1','status':'pass','nativeGrammarChanged':False,
        'classDictionaryByShift111':class_dictionary,'covers':reports,
        'periodFour':{k:reports[1][k] for k in ('spins','stabilizers','binaryRank','logicalQubits','groundSpaceDimension','minusIdentityAbsent')},
        'periodTwoAllStabilizersIdentity':True,'allClassProductsIdentity':True,'upstreamSupportMatches':True,
        'upstreamRowsCompared':sum(r['upstreamComparison']['rowsCompared'] for r in reports if r['upstreamComparison']),
        'upstreamGitBlobs':PINS,'publishedPolynomial':{'reference':'arXiv:2206.12791v1, Appendix C, Eq. C1',
          'XExponents':sorted(SX),'ZExponents':sorted(SZ),'primitiveCoordinateRule':'((y+z-x)/2,(x+z-y)/2,(x+y-z)/2)',
          'nativeToPaperPauliFrame':CYCLE,'checkAnchorFCCShift':[1,1,1],
          'operatorSquaresChecked':polynomial_squares,'laurentCommutationZero':True,
          'primitiveMetric':[[2,1,1],[1,2,1],[1,1,2]],
          'periodConvention':'Use the recorded primitive period generators, not an unrelated rectangular cubic torus.'},
        'mutationControlsRejected':controls,
        'scope':'Native unsplit-octahedron incidence, signed periodic stabilizer algebra, upstream binary-support adapter and the published one-generator Laurent map. No new native particle operation or full gauge-to-Chamon Clifford circuit is asserted.'}
paths=[Path(__file__),geometry_path,UPSTREAM/'README.md',*[UPSTREAM/name for name in PINS],
       ROOT/'references/2210.09867v2.pdf',ROOT/'references/2206.12791v1.pdf',ROOT/'research/strominger/chamon-fcc-benchmark-v1.md']
# Include native generator sources directly, rather than relying only on a
# nested receipt's freshness.
paths.extend(ROOT/p for p in geometry['sourceHashes'])
report['sourceHashes']={p.relative_to(ROOT).as_posix():sha(p) for p in paths}
out=BASE/'chamon-fcc-benchmark';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','periodFour':report['periodFour'],'periodTwoAllStabilizersIdentity':True,
                  'upstreamRowsCompared':report['upstreamRowsCompared'],'publishedPolynomialSquares':polynomial_squares,
                  'mutationControlsRejected':controls,'nativeGrammarChanged':False},indent=2))

"""Fresh native probes plus independent rational rank verification."""
from pathlib import Path
from fractions import Fraction as F
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/strominger/results/four-progression-directions'
for name in ['check_four_progression_directions.mjs','check_progression_leaf_invariant.mjs']:
    result=subprocess.run(['node',str(Path(__file__).with_name(name))],cwd=ROOT,capture_output=True,text=True,timeout=180)
    assert result.returncode==0,result.stderr

def rank(vectors):
    a=[[F(x) for x in row] for row in vectors];r=0
    if not a:return 0
    for j in range(len(a[0])):
        k=next((i for i in range(r,len(a)) if a[i][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];p=a[r][j];a[r]=[x/p for x in a[r]]
        for i in range(r+1,len(a)):
            p=a[i][j]
            if p:a[i]=[x-p*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r
raw=(OUT/'verification.json').read_bytes();d=json.loads(raw);leafRaw=(OUT/'leaf-invariant.json').read_bytes();leaf=json.loads(leafRaw)
assert d['profiles']=={'spatial 2, combined 3':8,'spatial 0, combined 1':16}
for row in d['rows']:
    for section in ['reachableBodies','sameCarrierSteps','restoredReference','restoredReferenceAndCoefficients']:
        for key in ['spatial','combined']:
            item=row[section][key];assert rank([g[key] for g in item['generators']])==item['rank']
    for g in row['restoredReferenceAndCoefficients']['combined']['generators']:
        delta=g['displacementTimesFour'];assert sum(delta)==0 and delta[0]+delta[2]==0;assert g['combined'][3]>0
assert leaf['counts']['P']==leaf['counts']['N']==48;assert leaf['counts']['nonplanarNAdvances']==0
squares=sum(len(row['commutingSquares']) for row in d['rows']);assert squares==24
result={'status':'three-not-four-repeatable-progression-directions-in-current-grammar','profiles':d['profiles'],'restoredSpatialRank':2,'combinedSpatialAndRealizationRank':3,'commutingGeneratorSquares':squares,'templateInvariant':'equal M heights h=x0+x2 are preserved on every live native successor; all translation template classes checked','discoveryDepth':12,'templateCoverage':{'P':48,'N':48},'sourceHashes':{'research/strominger/results/four-progression-directions/verification.json':hashlib.sha256(raw).hexdigest(),'research/strominger/results/four-progression-directions/leaf-invariant.json':hashlib.sha256(leafRaw).hexdigest(),'research/strominger/checkers/check_four_progression_directions.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'scope':'Forward native word generation, not unconstrained spatial translations. The all-path upper bound uses the source translation templates and induction, not finite absence alone. Three-dimensional affine progression span in ambient spatial-rank-three plus grade; no continuous manifold, five-dimensional configuration, negative-grade control or physical dimension theorem.'}
(OUT/'rank-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

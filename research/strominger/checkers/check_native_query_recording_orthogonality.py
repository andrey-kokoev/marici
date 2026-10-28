"""Exact controlled-recording test; logical reversibility is not isometry."""
from pathlib import Path
from fractions import Fraction as F
import contextlib, io, runpy, hashlib, json
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
with contextlib.redirect_stdout(io.StringIO()):
    p=runpy.run_path(str(BASE/'checkers/check_native_query_pairing_selection.py'))
G=p['group'];features=p['features'];n=len(G)
checks=0
def check(ok):
    global checks
    if not ok:raise AssertionError('recording test failed')
    checks+=1
results=[]
for lam in (F(0),F(1,9)):
    H=lambda i,j:(F(i==j)+lam)/(3+9*lam)
    for eta in (F(0),F(1,2)):
        # Unit pointer vectors with overlap eta. R is positive definite.
        check(1-eta*eta>0)
        R=lambda r,s:F(1) if r==s else eta
        metric=lambda a,b:H(a//2,b//2)*R(a%2,b%2)
        ports=[]
        for name,f in features.items():
            T=lambda a:2*(a//2)+((a%2)^int(f[a//2]))
            check(sorted(T(a) for a in range(2*n))==list(range(2*n)))
            check(all(T(T(a))==a for a in range(2*n)))
            check(all(T(2*i)//2==i and T(2*i)%2==int(f[i]) for i in range(n)))
            isometry=all(metric(T(a),T(b))==metric(a,b) for a in range(2*n) for b in range(2*n))
            check(isometry==(lam==0))
            ports.append({'query':name,'isometry':isometry})
        results.append({'lambda':str(lam),'pointer_overlap':str(eta),'ports':ports})
# Explicit AB witness, with genuinely nonorthogonal but distinct pointer vectors.
f=features['AB'];i=next(i for i in range(n) if f[i]==0);j=next(j for j in range(n) if f[j]==1)
lam=F(1,9);eta=F(1,2)
H=lambda i,j:(F(i==j)+lam)/(3+9*lam)
before=H(i,i)+H(j,j)+2*H(i,j)
after=H(i,i)+H(j,j)+2*eta*H(i,j)
check(before==F(11,18) and after==F(7,12))
# The entire blank-input Gram defect has the exact nondemolition factor.
for f in features.values():
    for i in range(n):
        for j in range(n):
            pointer_overlap=F(1) if f[i]==f[j] else eta
            defect=H(i,j)*(pointer_overlap-1)
            check(defect==(F(0) if f[i]==f[j] else (eta-1)*H(i,j)))
# Identical pointer states (overlap 1) hide the defect but record no distinction.
check(all(H(i,j)*(F(1)-1)==0 for i in range(n) for j in range(n)))
# Query-sector zeros propagated by the native left transports eliminate every
# off-diagonal entry, as required by the preceding classification.
for i,g in enumerate(G):
    for j,k in enumerate(G):
        if i==j:continue
        check(any(f[G.index(p['compose'](h,g))]!=f[G.index(p['compose'](h,k))]
                  for h in G for f in features.values()))
files=[Path(__file__).resolve(),BASE/'native-query-recording-orthogonality-v1.md',
       ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda',
       ROOT/'research/nima/agda/BoundaryGeneratedQuestions.agda',
       ROOT/'research/kitaev/broadcastability-is-the-algebraic-record-boundary.md']
report={'status':'pass','checks':checks,'models':results,
        'witness':{'query':'AB','pointer_overlap':'1/2','squared_norm_before':str(before),'squared_norm_after':str(after)},
        'conclusion':'Retained reversible query recording does not imply joint isometry. Isometric nondemolition with distinct unit pointer states forces orthogonal query sectors.',
        'scope':'Exact finite algebra and written theorem; no native amplitude/pointer implementation or physical authority derived.',
        'sha256':{str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=BASE/'results/native-query-pairing-selection/recording-orthogonality.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','checks','witness','conclusion')}))

"""Exact 12x3 grid reconstruction from native baryon supports and return line."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from assemble_metric_coefficient_protocol import read_operator,product,A,ZERO,ONE,encode
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
def components(m,n):
    adj={i:set() for i in range(n)}
    for i,j in m:adj[i].add(j);adj[j].add(i)
    todo=set(range(n));blocks=[]
    while todo:
        seed=min(todo);found={seed};q=[seed]
        for i in q:
            for j in adj[i]:
                if j not in found:found.add(j);q.append(j)
        todo-=found;blocks.append(sorted(found))
    return blocks
results={};hashes={}
for species in ['proton','neutron']:
    file=BASE/'common-three-carrier-protocol'/f'{species}.json';raw=file.read_bytes();hashes[file.relative_to(ROOT).as_posix()]=hashlib.sha256(raw).hexdigest();d=json.loads(raw);metric=[F(v) for v in d['source']['metric']];n=len(metric);assert n==36
    L=read_operator(d['operators']['L'],n);G=read_operator(d['operators']['G'],n);N=read_operator(d['operators']['N'],n)
    fine,coarse=(L,G) if species=='proton' else (G,L)
    rows,cols=components(fine,n),components(coarse,n);assert len(rows)==12 and len(cols)==3;assert all(len(b)==3 for b in rows);assert all(len(b)==12 for b in cols)
    grid=[]
    for row in rows:
        line=[]
        for col in cols:
            intersection=set(row)&set(col);assert len(intersection)==1;line.append(intersection.pop())
        grid.append(line)
    assert len(set(sum(grid,[])))==36
    # The actual native return column supplies the gauge; no fitted phase.
    z=[N.get((i,0),ZERO) for i in range(n)];assert all(x!=ZERO for x in z)
    weights=[A(metric[i])*z[i].flip(8)*z[i] for i in range(n)];assert all(w==w.flip(8) and w!=ZERO for w in weights)
    W=[[weights[i] for i in row] for row in grid];rs=[sum(row,ZERO) for row in W];cs=[sum((W[i][j] for i in range(12)),ZERO) for j in range(3)];total=sum(rs,ZERO)
    for i in range(12):
        for j in range(3):assert W[i][j]*total==rs[i]*cs[j]
    # x_i = z_i y_i. Transformed metric is m_i |z_i|^2. Source geometry and
    # physical inner product are unchanged, only coordinates are rescaled.
    transformed=lambda op:{(i,j):z[i].inverse()*a*z[j] for (i,j),a in op.items()}
    fineT,coarseT,returnT=map(transformed,[fine,coarse,N]);expectedFine={};expectedCoarse={};expectedReturn={}
    for i in range(12):
        for j in range(3):
            target=grid[i][j]
            for k in range(3):expectedFine[target,grid[i][k]]=cs[k]/total
            for k in range(12):expectedCoarse[target,grid[k][j]]=rs[k]/total
            for k in range(12):
                for l in range(3):expectedReturn[target,grid[k][l]]=weights[grid[k][l]]/total
    assert fineT==expectedFine;assert coarseT==expectedCoarse;assert returnT==expectedReturn
    assert product(fineT,coarseT)==product(coarseT,fineT)==returnT
    def serial(xs):return [x.record() for x in xs]
    results[species]={'grid':grid,'rowBlocks':rows,'columnBlocks':cols,'coordinateLabels':d['source']['coordinates'],'sourceReturnColumn':serial(z),'transformedMetric':serial(weights),'rowProbabilities':serial([x/total for x in rs]),'columnProbabilities':serial([x/total for x in cs]),'weightFactorizationExact':True,'fineProjection':'I_12 tensor weighted-mean-on-3','coarseProjection':'weighted-mean-on-12 tensor I_3','nativeL':'fine' if species=='proton' else 'coarse','nativeG':'coarse' if species=='proton' else 'fine','nativeReturn':'weighted-mean-on-12 tensor weighted-mean-on-3','allOperatorCoefficientsMatch':True}
out=BASE/'baryon-tensor-grid';out.mkdir(exist_ok=True)
receipt={'status':'native-baryon-tensor-grid-derived','carriers':results,'sourceHashes':hashes,'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact full-operator and induced-metric factorization using each native rank-one return column as invertible diagonal coordinate gauge. No source metric replacement or zero-mode deletion. All 36 source coordinates and source labels retained. Does not identify tensor axes with geometric M/C/R, derive the source projectors from T, or include the electron field.'}
(out/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'carriers':list(results),'grid':[12,3],'exactWeightFactorization':True,'exactFullOperatorFactorization':True}))

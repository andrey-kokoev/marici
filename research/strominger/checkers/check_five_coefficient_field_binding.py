"""Test fixed vs phase-dependent complex-linear coefficient/field bindings."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,re
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
from assemble_metric_coefficient_protocol import A,ONE,read_operator,product,ZERO
BASE=ROOT/'research/strominger/results';phasePath=ROOT/'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';phaseText=phasePath.read_text()
perms={s:json.loads(re.search(s+r':Object\.freeze\((\[[0-9,]+\])\)',phaseText).group(1)) for s in ['proton','neutron']}
Pi={s:{(i,j):ONE for i,j in enumerate(p)} for s,p in perms.items()};I5={(i,i):ONE for i in range(5)}
for p in Pi.values():assert product(p,p)==I5
sources={s:json.loads((BASE/f'common-three-carrier-protocol/{s}.json').read_text()) for s in perms}
def gram(B,metric):
    adj={(j,i):v.flip(8)*A(metric[i]) for (i,j),v in B.items()};return product(adj,B)
root2=A(tuple(F(1) if i==1 else F(0) for i in range(16)))
# P: geometric signed permutation, independently rebuilt from its marked move.
labels=sources['proton']['source']['coordinates'];rotation=geo.rotation((2,3,0,1));rename=dict(zip('ABCD','CDAB'));U={}
for j,label in enumerate(labels):
    edge,axis=label.split(':');target=''.join(rename[v] for v in edge)
    for i in range(3):
        if rotation[i]['xyz'.index(axis)]:U[labels.index(target+':'+'xyz'[i]),j]=A(rotation[i]['xyz'.index(axis)])
byColumn={j:(i,v) for (i,j),v in U.items()};used=set();orbits=[]
for j in range(36):
    if j in used:continue
    i,v=byColumn[j];assert i!=j;used|={i,j};orbits.append((j,i,v))
assert len(orbits)==18
p=perms['proton'];pairs=[];seen=set();fixed=[]
for i,j in enumerate(p):
    if i==j:fixed.append(i)
    elif i not in seen:pairs.append((i,j));seen|={i,j}
B={}
for (a,b),(j,i,v) in zip(pairs,orbits):B[j,a]=ONE;B[i,b]=v
j,i,v=orbits[2];B[j,fixed[0]]=ONE/root2;B[i,fixed[0]]=v/root2
assert product(U,B)==product(B,Pi['proton']);assert gram(B,[F(1)]*36)==I5
# N: ordered-corner co-moving field transport is I. A fixed B must identify
# columns 1/3 and 2/4, hence rank at most three and cannot retain five inputs.
p=perms['neutron'];cycles=[];seen=set()
for i in range(5):
    if i not in seen:
        cycle={i,p[i]};seen|=cycle;cycles.append(sorted(cycle))
assert len(cycles)==3
metric=list(map(F,sources['neutron']['source']['metric']));slots=[i for i,m in enumerate(metric) if m==F(1,2)];assert len(slots)>=6
# Construct two different norm-preserving seeds to expose nonuniqueness.
seeds=[{(i,j):root2 for j,i in enumerate(slots[:5])},{(i,j):root2 for j,i in enumerate(slots[1:6])}];assert seeds[0]!=seeds[1]
for seed in seeds:
    assert gram(seed,metric)==I5
    current=seed
    for origin in range(28):
        nxt=product(current,Pi['neutron'])
        assert product(nxt,Pi['neutron'])==current # U B_r = B_(r+1) Pi, U=I
        assert gram(nxt,metric)==I5
        if origin%2==0:assert nxt!=seed
        else:assert nxt==seed
        current=nxt
# Algebraic antiunitary obstruction: T B(ix)=-i T Bx versus
# B' Pi(ix)=+i B' Pi x. Any complex-linear B,B' satisfying both must vanish.
serialize=lambda B:[{'field':i,'coefficient':j,'value':v.record()} for (i,j),v in sorted(B.items())]
paths=[Path(__file__).resolve(),phasePath,*[BASE/f'common-three-carrier-protocol/{s}.json' for s in perms]]
result={'status':'five-coefficient-binding-possibility-and-obstructions-tested','nativePermutations':perms,'proton':{'fixedComplexLinearIsometricIntertwinerExists':True,'constructedSeed':serialize(B),'sourceFieldOrbits':len(orbits),'noncanonical':True},'neutron':{'fixedOrderedFrameBindingMaximumRank':len(cycles),'fixedInjectiveBindingExists':False,'phaseDependentRule':'B_(r+1)=B_r Pi_N; B_(r+1) Pi_N=B_r','phaseDependentIsometricBindingsChecked':2,'advancesPerBinding':28,'allFiveCoefficientsRetained':True,'constructedSeeds':[serialize(seed) for seed in seeds],'outwardAntiunitaryTransportWithComplexLinearBindings':'No nonzero solution for all complex inputs, even if target binding varies by phase. Requires alternating semilinear chart convention or a different coefficient-field correspondence.'},'sourceHashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'scope':'Constructed embeddings establish algebraic compatibility/nonuniqueness, not a source-derived geometric binding. P seed chooses arbitrary disjoint geometric transport orbits; N seeds choose arbitrary equal-metric slots. No intertwining of unspecified five-dimensional L/G, PN cross-species map or E binding asserted. Phase-dependent embedding records coordinates; field state need not evolve nontrivially. Absolute origin and full operation word remain separate and are not quotiented by phase.'}
out=BASE/'five-coefficient-field-binding';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'protonFixedIsometricBinding':True,'neutronFixedRankBound':3,'neutronPhaseDependentIsometricBindings':2,'allFiveRetained':True}))

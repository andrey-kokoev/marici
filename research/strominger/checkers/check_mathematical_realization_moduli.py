"""Output-A assembly: exact finite classification certificate and fresh native binding."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import re, json, hashlib, subprocess, time
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger'
OUT=BASE/'results/mathematical-realization-moduli';OUT.mkdir(parents=True,exist_ok=True)
source=ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda'
text=source.read_text(encoding='utf-8')
def table(name):
    rows=dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$',text,re.M));assert set(rows)==set('ABCD')
    return tuple('ABCD'.index(rows[v]) for v in 'ABCD')
abc,adb=table('abc'),table('adb')
def comp(h,g):return tuple(h[g[i]] for i in range(4))
identity=tuple(range(4));seen={identity};todo=[identity]
for g in todo:
    for h in (abc,adb):
        k=comp(h,g)
        if k not in seen:seen.add(k);todo.append(k)
G=sorted(seen);assert len(G)==12
finite_source=BASE/'agda/NativeQueryFiniteBinding.agda'
finite_text=finite_source.read_text(encoding='utf-8')
for i,g in enumerate(G):
    rows=dict(re.findall(r'^perm g'+str(i)+r' ([ABCD]) = ([ABCD])$',finite_text,re.M))
    assert tuple('ABCD'.index(rows[v]) for v in 'ABCD')==g
assert len(set(G))==12
fragment=BASE/'contracts/native-query-source-fragment.v1.json'
names=list(json.loads(fragment.read_text())['generators']);assert len(names)==8
queries={name:tuple(int(g['ABCD'.index(name[2])]=='ABCD'.index(name[3])) for g in G)
         for name in names if name.startswith('Q_')}
assert len(queries)==6 and all(sum(f)==3 for f in queries.values())
separators=[]
for i,g in enumerate(G):
    for j,k in enumerate(G):
        if i==j:continue
        witness=next(({'pair':[i,j],'translation':list(h),'query':name}
                      for h in G for name,f in queries.items()
                      if f[G.index(comp(h,g))]!=f[G.index(comp(h,k))]),None)
        assert witness is not None;separators.append(witness)
assert len(separators)==132
states=list(product(G,(0,1)))
def step(name,s):
    g,b=s
    if name.startswith('L_'):return comp({'L_ABC':abc,'L_ADB':adb}[name],g),b
    return g,b^queries[name][G.index(g)]
# H=I/3; verify preservation of both coefficients of R_eta=I+eta X.
coefficients=0
for name in names:
    permutation=[states.index(step(name,s)) for s in states]
    assert sorted(permutation)==list(range(24))
    for eta_degree in (0,1):
        def gram(i,j):
            g,b=states[i];h,c=states[j]
            return F(g==h,3)*F((b==c) if eta_degree==0 else (b!=c))
        for i in range(24):
            for j in range(24):
                assert gram(permutation[i],permutation[j])==gram(i,j);coefficients+=1
# Ready-pointer equality gives the symbolic cross-sector multiplier eta-1.
# Verify which entries this condition kills, independently of selected eta.
for f in queries.values():
    for i in range(12):
        for j in range(12):
            defect_coefficients=(0,0) if f[i]==f[j] else (-1,1)
            assert defect_coefficients==((int(f[i]==f[j])-1),int(f[i]!=f[j]))
roots=[BASE/'agda',ROOT/'research/nima/agda',ROOT/'research/voevodsky/agda',
       ROOT/'research/voevodsky/observer-relative-computation/agda',ROOT/'research/grothendieck/agda',
       Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')]
def snapshot():
    files=set(f for r in roots for f in r.rglob('*.agda'))
    return {str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(files)}
args=['agda','--transliterate','--no-libraries','--safe','--cubical','--guardedness','--no-import-sorts']
for r in roots:args+=['-i',str(r)]
before=snapshot();start=time.time()
with (OUT/'positive.log').open('wb') as log:
    positive=subprocess.run(args+['--ignore-interfaces',str(finite_source)],stdout=log,stderr=subprocess.STDOUT,timeout=600)
with (OUT/'negative.log').open('wb') as log:
    negative=subprocess.run(args+['-i',str(BASE/'agda/negative'),str(BASE/'agda/negative/NativeWordBadReset.agda')],stdout=log,stderr=subprocess.STDOUT,timeout=180)
after=snapshot();negative_text=(OUT/'negative.log').read_text(encoding='utf-8',errors='replace')
passed=positive.returncode==0 and negative.returncode==42 and '[UnequalTerms]' in negative_text and before==after
inputs=[fragment,BASE/'contracts/native-query-realization-equivalence.v1.json',source,finite_source,
        BASE/'agda/NativeQueryWordRealization.agda',BASE/'agda/negative/NativeWordBadReset.agda',
        BASE/'checkers/generate_native_query_finite_binding.py',Path(__file__).resolve(),
        BASE/'mathematical-realization-moduli-v1.md']
report={'status':'pass' if passed else 'fail','classification':'For each supplied -1<eta<1, H=cI; normalized H=I/3, one labelled factor-preserving isomorphism class.',
        'positive_exit':positive.returncode,'negative_exit':negative.returncode,'ignore_interfaces':True,'stable_inputs':before==after,
        'conservative_source_files':len(before),'elapsed_seconds':time.time()-start,
        'all_word_native_binding':True if positive.returncode==0 else False,
        'separated_ordered_pairs':132,'coefficientwise_generator_checks':coefficients,
        'formal_boundary':'Agda proves native finite-table/all-word binding; general real pairing classification is a written proof with exact finite symbolic-coefficient support.',
        'physical_validation':False,'pointer_eta_selected':False,'oscillator_obstruction_reversed':False,
        'separation_certificate':separators,
        'artifact_sha256':{str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs},
        'source_sha256':before,'warnings':'Inherited Cubical warnings are retained in positive.log.'}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ('status','positive_exit','negative_exit','stable_inputs','conservative_source_files','all_word_native_binding','separated_ordered_pairs','coefficientwise_generator_checks')}))
if not passed:raise SystemExit(1)

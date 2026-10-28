"""Canonical support involution with kernel bindings to the actual external trees."""
from pathlib import Path
import hashlib,json,itertools,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-diagram-involution'
SIG=[1,0,3,2];VN=['c0','m0','c1','m1'];CH=[0,7,0,7]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tag(t):return '-'.join(map(str,t))
def code(f,v):return f's{f}{v}'
def support(t):
    out=[];v=next(v for v in range(4) if v not in t)
    for piece,(a,b) in [('AB',(t[0],t[1])),('BC',(t[1],t[2])),('AC',(t[0],t[2]))]:
        for w in range(4):
            for f in range(4):
                for g in range(4):
                    if f==w or g==w or CH[f]!=CH[a] or CH[g]!=CH[b]:continue
                    for side in [0,1]:out.append((piece,w,f,g,side))
    out += [('full',v,f,i) for i,f in enumerate(t)]
    return out

def flip(o):
    if o[0]=='full':return ('full',SIG[o[1]],SIG[o[2]],o[3])
    return (o[0],SIG[o[1]],SIG[o[2]],SIG[o[3]],o[4])
def source(o):return (o[2],o[1]) if o[0]=='full' else (o[2+o[4]],o[1])
def term(o):
    if o[0]=='full':return f'(P.S.full-source , (P.S.{["first-port","middle-port","final-port"][o[3]]} , tt))'
    piece,v,f,g,side=o
    return f'(P.S.{piece} , (({VN[v]} , (F.vp-{f}-{v} , F.vp-{g}-{v})) , (P.S.{["source-leg","target-leg"][side]} , tt)))'
def prepare():
    priors=[BASE/'results'/f'{n}-v1.json' for n in ['ramsey-marking-symmetry','ramsey-external-seed-policy','ramsey-external-pe']]
    for path in priors:
        d=json.loads(path.read_text());assert d['status']=='passed'
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale source '+p
    symmetry=json.loads(priors[0].read_text());assert symmetry['selectedComplement']['permutation']==SIG and symmetry['selectedComplement']['frameMap'][0]==7
    lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module RamseyDiagramInvolutionExamples where',
      'open import Cubical.Foundations.Prelude','open import Cubical.Data.Unit.Base using (Unit; tt)',
      'open import Cubical.Data.Empty.Base using (⊥)','open import RamseySingleFrameFaces using (c0; m0; c1; m1)',
      'import RamseyRequestedPortExamples as C','import RamseyFourFacetVertexCells as F',
      'open import RamseyExternalPEExamples','import RamseyExternalSeedPolicyExamples as Policy',
      'data Code : Type where','  '+' '.join(code(f,v) for f in range(4) for v in range(4) if f!=v)+' : Code',
      'input : Code → P.S.InputIndex']
    pairs=[(f,v) for f in range(4) for v in range(4) if f!=v]
    for f,v in pairs:lines += [f'input {code(f,v)} = C.q{CH[f]} , ({VN[v]} , F.vp-{f}-{v})']
    lines += ['swap : Code → Code']
    for f,v in pairs:lines += [f'swap {code(f,v)} = {code(SIG[f],SIG[v])}']
    lines += ['swap-square : (s : Code) → swap (swap s) ≡ s']
    for f,v in pairs:lines += [f'swap-square {code(f,v)} = refl']
    lines += ['pair-preserved : (s : Code) → Policy.PairChart (fst (input (swap s)))']
    for f,v in pairs:lines += [f'pair-preserved {code(f,v)} = tt']
    lines += ['base-not-invariant : ((s : Code) → Policy.BaseChart (fst (input s)) → Policy.BaseChart (fst (input (swap s)))) → ⊥',
      'base-not-invariant alleged = alleged s01 tt']
    lines += ['ComplementChart : C.Chart → Type']
    for c in range(24):lines += [f'ComplementChart C.q{c} = '+('Unit' if c==7 else '⊥')]
    lines += ['base-to-complement : (s : Code) → Policy.BaseChart (fst (input s)) → ComplementChart (fst (input (swap s)))']
    for f,v in pairs:lines += [f'base-to-complement {code(f,v)} '+('allowed = tt' if CH[f]==0 else '()')]
    lines += ['complement-to-base : (s : Code) → ComplementChart (fst (input s)) → Policy.BaseChart (fst (input (swap s)))']
    for f,v in pairs:lines += [f'complement-to-base {code(f,v)} '+('allowed = tt' if CH[f]==7 else '()')]
    rows=[];selection_cells=0
    triples=list(itertools.permutations(range(4),3));supports={t:support(t) for t in triples}
    for t,occurrences in supports.items():
        target=tuple(SIG[i] for i in t);other=supports[target]
        assert len(occurrences)==len(other)==55
        mapped=[other.index(flip(o)) for o in occurrences];assert len(set(mapped))==55
        for i,o in enumerate(occurrences):
            assert flip(flip(o))==o
            f,v=source(o);assert source(flip(o))==(SIG[f],SIG[v])
            suffix=tag(t)+'-'+str(i);tree='tree-'+tag(t);to='tree-'+tag(target)
            lines += [f'occ-{suffix} : P.T.Occurrence {tree}',f'occ-{suffix} = {term(o)}',
              f'origin-{suffix} : P.T.origin {tree} occ-{suffix} ≡ input {code(f,v)}',f'origin-{suffix} = refl',
              f'transport-{suffix} : P.T.origin {to} {term(flip(o))} ≡ input (swap {code(f,v)})',f'transport-{suffix} = refl']
        v=next(i for i in range(4) if i not in t)
        for piece,(a,b) in [('AB',(t[0],t[1])),('BC',(t[1],t[2])),('AC',(t[0],t[2]))]:
            for side in [0,1]:
                chosen=(piece,v,a,b,side)
                assert chosen in occurrences and flip(chosen) in other
                assert flip(chosen)==(piece,SIG[v],SIG[a],SIG[b],side)
            for label,triple,x,y,w in [('source',t,a,b,v),('target',target,SIG[a],SIG[b],SIG[v])]:
                name='selected-'+label+'-'+tag(t)+'-'+piece
                charts=' '.join('{'+n+' = C.q'+str(CH[f])+'}' for n,f in zip(['a','b','c'],triple))
                lines += [f'{name} : P.S.{piece.lower()}-index {charts} F.triple-{tag(triple)} ≡ ({VN[w]} , (F.vp-{x}-{w} , F.vp-{y}-{w}))',f'{name} = refl']
            selection_cells+=1
        rows.append({'triple':t,'target':target,'canonicalOccurrences':55,'occurrencePermutation':mapped})
    FIX.mkdir(parents=True,exist_ok=True)
    (FIX/'RamseyDiagramInvolutionExamples.agda').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (FIX/'RamseyDiagramInvolutionBadIdentity.agda').write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDiagramInvolutionBadIdentity where
open import Cubical.Foundations.Prelude
open import RamseyDiagramInvolutionExamples
bad : input s01 ≡ input (swap s01)
bad = refl
''',encoding='utf-8')
    # Explicitly exchange the singleton policies rather than pretending to preserve either.
    assert all((CH[f]==0)==(CH[SIG[f]]==7) and (CH[f]==7)==(CH[SIG[f]]==0) for f,v in pairs)
    return priors,rows,selection_cells

def main():
    priors,rows,selected=prepare()
    if '--generate' in sys.argv:return
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,*[BASE/'fixtures'/n for n in ['ramsey-external-seed-policy','ramsey-external-pe','ramsey-four-facet-vertex-cells','ramsey-native-edge-attachments','ramsey-requested-port']],ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,ok in [('RamseyDiagramInvolutionExamples',True),('RamseyDiagramInvolutionBadIdentity',False)]:
        run=subprocess.run(args+[str(FIX/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    files=[*priors,Path(__file__),BASE/'contracts/ramsey-diagram-involution-attempt.v1.json',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-diagram-involution.verification.v1','status':'passed',
      'scope_id':'canonical-external-occurrence-involution-and-policy-exchange-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'canonicalSourceIndices':12,'actualTrees':24,'canonicalOccurrences':1320,'sourceOriginCells':1320,'transportedOriginCells':1320,
      'selectedBranchTransportChecks':selected,'kernelSelectedIndexBindingCells':2*selected,'kernelSingletonPolicyExchange':True,'unselectedEPrerequisitesRetained':True,
      'twoChartPolicyPreserved':True,'singletonPoliciesExchanged':True,'baseOnlyPolicyPreserved':False,
      'literalSourceIdentityHostileRejected':True,'kernelWholeDependentTreeEquivalence':False,
      'independentTargetInputsEliminated':False,'nativeOperationAdded':False,'parentDescentResolved':False,
      'supportInvolution':rows,'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-diagram-involution-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory','supportInvolution']},indent=2))
if __name__=='__main__':main()

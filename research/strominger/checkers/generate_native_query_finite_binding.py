"""Generate explicit finite source tables and proof clauses (not proof receipts)."""
from pathlib import Path
from collections import deque
import re
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger'
text=(ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda').read_text(encoding='utf-8')
def table(name):
    rows=dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$',text,re.M))
    assert set(rows)==set('ABCD');return tuple('ABCD'.index(rows[v]) for v in 'ABCD')
abc,adb=table('abc'),table('adb')
def comp(h,g):return tuple(h[g[i]] for i in range(4))
e=tuple(range(4));words={e:[]};queue=deque([e])
while queue:
    g=queue.popleft()
    for name,h in [('LABC',abc),('LADB',adb)]:
        k=comp(h,g)
        if k not in words:words[k]=words[g]+[name];queue.append(k)
G=sorted(words);assert len(G)==12 and G[0]==e
name=lambda g:'g'+str(G.index(g))
s=['{-# OPTIONS --safe --cubical --guardedness #-}',
'module NativeQueryFiniteBinding where',
'open import Cubical.Foundations.Prelude',
'open import Cubical.Foundations.Equiv',
'open import Cubical.Foundations.Isomorphism',
'open import Cubical.Data.Bool.Base using (Bool; false)',
'open import Cubical.Data.Sigma.Base using (_×_)',
'open import Cubical.Data.List.Base using (List; []; _∷_)',
'import NativeQueryControlledRecorder as R',
'import NativeSeedTransitionProbe as Q',
'import NativeQueryWordRealization as W',
'import SeedAttachedObserver as Seed',
'open Seed using (Vertex; A; B; C; D)',
'open W using (Op; LABC; LADB; QAB; QBC; QCA; QAD; QDB; QBA)',
'', 'data G : Type where', '  '+' '.join(name(g) for g in G)+' : G','',
'perm : G → Vertex → Vertex']
for g in G:
    for i,v in enumerate('ABCD'):s.append(f'perm {name(g)} {v} = {"ABCD"[g[i]]}')
s+=['','inverseG leftABC leftADB : G → G']
for g in G:s.append(f'inverseG {name(g)} = {name(tuple(g.index(i) for i in range(4)))}')
for label,h in [('leftABC',abc),('leftADB',adb)]:
    for g in G:s.append(f'{label} {name(g)} = {name(comp(h,g))}')
for lemma,expr in [('right','perm g (perm (inverseG g) v)'),('left','perm (inverseG g) (perm g v)')]:
    s+=['',f'{lemma} : (g : G) (v : Vertex) → {expr} ≡ v']
    for g in G:
        for v in 'ABCD':s.append(f'{lemma} {name(g)} {v} = refl')
s+=['','equivalence : G → Vertex ≃ Vertex',
'equivalence g = isoToEquiv (iso (perm g) (perm (inverseG g)) (right g) (left g))']
for label in ('ABC','ADB'):
    q=label.lower()
    s+=['',f'left{label}-value : (g : G) (v : Vertex) → perm (left{label} g) v ≡ Q.{q} (perm g v)']
    for g in G:
        for v in 'ABCD':s.append(f'left{label}-value {name(g)} {v} = refl')
    s+=[f'left{label}-path : (g : G) → equivalence (left{label} g) ≡ compEquiv (equivalence g) Q.{label}',
        f'left{label}-path g = equivEq (funExt (left{label}-value g))']
s+=['','State : Type','State = G × Bool','',
'embed : State → R.Carrier','embed (g , b) = equivalence g , b','',
'step : Op → State → State',
'step LABC (g , b) = leftABC g , b',
'step LADB (g , b) = leftADB g , b']
for a,b in [('A','B'),('B','C'),('C','A'),('A','D'),('D','B'),('B','A')]:
    s.append(f'step Q{a}{b} (g , bit) = g , R.toggle (Q.equal (perm g {a}) {b}) bit')
s+=['','step-binding : (o : Op) (s : State) → embed (step o s) ≡ W.native-step o (embed s)',
'step-binding LABC (g , b) = cong (λ e → e , b) (leftABC-path g)',
'step-binding LADB (g , b) = cong (λ e → e , b) (leftADB-path g)']
for a,b in [('A','B'),('B','C'),('C','A'),('A','D'),('D','B'),('B','A')]:s.append(f'step-binding Q{a}{b} (g , bit) = refl')
s+=['','run : List Op → State → State','run [] s = s','run (o ∷ os) s = run os (step o s)',
'', 'all-word-binding : (os : List Op) (s : State) → embed (run os s) ≡ W.native-run os (embed s)',
'all-word-binding [] s = refl',
'all-word-binding (o ∷ os) s = all-word-binding os (step o s) ∙ cong (W.native-run os) (step-binding o s)',
'', 'record-reading : (os : List Op) (s : State) → snd (run os s) ≡ snd (W.native-run os (embed s))',
'record-reading os s = cong snd (all-word-binding os s)',
'', 'access : G → List Op']
for g in G:s.append(f'access {name(g)} = '+''.join(o+' ∷ ' for o in words[g])+'[]')
s+=['','access-correct : (g : G) → run (access g) (g0 , false) ≡ (g , false)']
for g in G:s.append(f'access-correct {name(g)} = refl')
(BASE/'agda/NativeQueryFiniteBinding.agda').write_text('\n'.join(s)+'\n',encoding='utf-8')
print('Generated twelve actual permutations, inverse/translation tables, and native all-word binding.')

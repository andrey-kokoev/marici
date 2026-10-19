"""Export actual terminal family trees, preserving every owner Row field."""
import contextlib
import io
from pathlib import Path
import runpy
import sys
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    a=runpy.run_path(str(ROOT/'research/strominger/checkers/check_generated_rung4_adapter.py'))

def seq(xs): return '('+' ∷ '.join([*xs,'[]'])+')'
def key(x):
    if isinstance(x,Fraction): return key((x.numerator,x.denominator))
    if isinstance(x,int): return f'({"negative" if x<0 else "nat"} {abs(x)})'
    if isinstance(x,str): return '(text '+seq(map(str,map(ord,x)))+')'
    assert isinstance(x,tuple)
    return '(tuple '+seq(key(y) for y in x)+')'
def row(r):
    i=r.label[1] if not r.members else 0
    return '(row '+' '.join(key(x) for x in (r.label,r.source,r.target,r.value))+f' {r.mass} {i} '+seq(row(c) for c in r.members)+')'
lines=['{-# OPTIONS --safe --cubical --guardedness #-}',
       'module ActualNativeOuterFamilies where',
       'open import Cubical.Foundations.Prelude',
       'open import Cubical.Data.List.Base using (List; []; _∷_; length)',
       'open import Cubical.Data.Bool.Base using (true)',
       'open import Cubical.Data.Bool.Properties using (false≢true)',
       'open import Cubical.Data.Empty.Base using (⊥)',
       'open import NativeOuterFamilyEncoding',
       'import WholePackageSigmaPi as W','']
source=a['rows']
lines+=['direct-reference : Key','direct-reference = '+key(a['bound'].direct_value),'',
        'original : List Row','original = '+seq(row(r) for r in source),'']
for policy in ('inherited','common'):
    t=a['terminals'][policy]
    a['verify_terminal'](t)
    rs=a['unindex'](t.view)
    lines += [policy+' : List Row',policy+' = '+seq(row(r) for r in rs),'',
              policy+'-valid : valid-all '+policy+' ≡ true',policy+'-valid = refl',
              policy+'-count : length '+policy+' ≡ '+str(len(rs)),policy+'-count = refl',
              policy+'-mass : mass-total '+policy+' ≡ 137',policy+'-mass = refl',
              policy+'-leaves : leaves '+policy+' ≡ original',policy+'-leaves = refl','']
lines += ['-- The complete exported forest survives packaging as retained data.',
          'package : W.Universe.Complete ℓ-zero',
          'package = W.Universe.pack (W.Universe.atom (List Row)) inherited',
          'recover-forest : W.Universe.value package ≡ inherited',
          'recover-forest = refl','',
          '-- Unit outer-family weights cannot replace the actual leaf masses.',
          'no-unit-outer-weights : length inherited ≡ mass-total inherited → ⊥',
          'no-unit-outer-weights p = false≢true (sym (cong (same 32) p))','']
content='\n'.join(lines)
path=ROOT/'research/strominger/agda/ActualNativeOuterFamilies.agda'
if '--check' in sys.argv:
    assert path.read_text(encoding='utf-8')==content, 'native family export drift'
    print('Native family trees match live source objects, including payloads and memberships.')
else:
    path.write_text(content,encoding='utf-8')
    print('Exported both exact terminal family trees and original leaf rows.')

"""Export fresh proof DAGs as explicit Agda terms; never imports a cached proof."""
from pathlib import Path
import argparse
import json
from check_fresh_equations import verify, term, vars_, contextual


def expr(t):
    return t if isinstance(t,str) else f'(stroke {expr(t[0])} {expr(t[1])})'


def proof(p, records):
    kind=p[0]
    if kind=='refl': return 'refl'
    if kind=='sym': return f'(sym {proof(p[1],records)})'
    if kind=='trans': return f'({proof(p[1],records)} ∙ {proof(p[2],records)})'
    if kind=='call':
        a,b=(term(t) for t in records[p[1]]['equation'])
        return '('+f'f{p[1]} '+ ' '.join(expr(term(p[2][v])) for v in sorted(vars_(a)|vars_(b)))+')'
    if kind=='cong':
        context=term(p[1]); path=p[2]; old=context
        for i in path: old=old[i]
        body=contextual(context,path,old,'hole')
        return f'(cong (λ hole → {expr(body)}) {proof(p[3],records)})'
    raise ValueError('unknown proof constructor')


def emit(packet):
    verify(packet)
    records=packet['records']; left,right=(term(t) for t in packet['input'])
    xs=' '.join(sorted(vars_(left)|vars_(right)))
    out=['{-# OPTIONS --safe --cubical --guardedness #-}', 'module FreshEquationalConsequences where',
         'open import Cubical.Foundations.Prelude',
         '-- Consequences of the supplied axiom, NOT an adequacy certificate.',
         'module Derived {ℓ : Level} (A : Type ℓ) (stroke : A → A → A)',
         f'  (hypothesis : ({xs} : A) → {expr(left)} ≡ {expr(right)}) where']
    for i,record in enumerate(records):
        a,b=(term(t) for t in record['equation']); xs=' '.join(sorted(vars_(a)|vars_(b)))
        out += [f'  f{i} : ({xs} : A) → {expr(a)} ≡ {expr(b)}',
                f'  f{i} '+('= hypothesis' if i==0 else xs+' = '+proof(record['proof'],records))]
    for name,p in packet['derived'].items():
        a,b=(term(t) for t in packet['goals'][name]); xs=' '.join(sorted(vars_(a)|vars_(b)))
        out += [f'  {name} : ({xs} : A) → {expr(a)} ≡ {expr(b)}',f'  {name} {xs} = {proof(p,records)}']
    return '\n'.join(out)+'\n'


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path); parser.add_argument('output',type=Path)
    args=parser.parse_args()
    packet=json.loads(args.source.read_text())
    args.output.write_text(emit(packet),encoding='utf-8')
    a,b=(term(t) for t in packet['input']); xs=' '.join(sorted(vars_(a)|vars_(b)))
    negative='\n'.join([
        '{-# OPTIONS --safe --cubical --guardedness #-}', 'module FreshWrongConclusion where',
        'open import Cubical.Foundations.Prelude', 'import FreshEquationalConsequences as F',
        'module Bad {ℓ : Level} (A : Type ℓ) (stroke : A → A → A)',
        f'  (hypothesis : ({xs} : A) → {expr(a)} ≡ {expr(b)}) where',
        '  module D = F.Derived A stroke hypothesis',
        f'  bad : ({xs} fresh : A) → fresh ≡ x0',
        f'  bad {xs} fresh = D.f0 {xs}', ''])
    (args.output.parent / 'negative/FreshWrongConclusion.agda').write_text(negative,encoding='utf-8')

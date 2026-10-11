"""Bounded proof search in the product/negation fragment.
Inputs are types, not proof terms. Output is independently checked by Agda.
This is a specialized constructor, not a universality or completeness proof.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
BOT = '⊥'
def prod(a,b): return ('product',a,b)
def arr(a,b): return ('arrow',a,b)
def neg(a): return arr(a,BOT)
def nand(a,b): return neg(prod(a,b))
A,B,C = 'A','B','C'
W = nand(nand(nand(A,B),C),nand(A,nand(nand(A,C),A)))
D = neg(neg(C))

class Search:
    def __init__(self):
        self.visits = 0
        self.next_name = 0
    def fresh(self):
        n = 'v'+str(self.next_name)
        self.next_name += 1
        return n
    def solve(self, goal, context=(), fuel=24, active=frozenset()):
        self.visits += 1
        if self.visits > 200000: raise RuntimeError('node budget exhausted')
        if fuel == 0: return None
        # Product elimination is invertible; preserve terms witnessing each projection.
        ctx = list(context)
        for ty,tm in ctx:
            if isinstance(ty,tuple) and ty[0]=='product':
                for component,projection in zip(ty[1:],('fst','snd')):
                    if component not in [t for t,_ in ctx]:
                        ctx.append((component,(projection,tm)))
        for ty,tm in ctx:
            if ty == goal: return tm
        key = (goal,frozenset(t for t,_ in ctx))
        if key in active: return None
        active = active | {key}
        if isinstance(goal,tuple) and goal[0]=='arrow':
            name=self.fresh()
            body=self.solve(goal[2],tuple(ctx)+((goal[1],('var',name)),),fuel-1,active)
            if body is not None: return ('lambda',name,body)
        elif isinstance(goal,tuple) and goal[0]=='product':
            left=self.solve(goal[1],tuple(ctx),fuel-1,active)
            if left is not None:
                right=self.solve(goal[2],tuple(ctx),fuel-1,active)
                if right is not None: return ('pair',left,right)
        # This fragment only needs applications whose codomain is the goal.
        for ty,tm in ctx:
            if isinstance(ty,tuple) and ty[0]=='arrow' and ty[2]==goal:
                argument=self.solve(ty[1],tuple(ctx),fuel-1,active)
                if argument is not None: return ('apply',tm,argument)
        return None

def render(t):
    tag=t[0]
    if tag=='var': return t[1]
    if tag=='lambda': return '(λ '+t[1]+' → '+render(t[2])+')'
    if tag=='pair': return '('+render(t[1])+' , '+render(t[2])+')'
    if tag=='apply': return '('+render(t[1])+' '+render(t[2])+')'
    return '('+tag+' '+render(t[1])+')'

def intrinsic(t, expected, context=()):
    """Elaborate the searched AST into an independently checked indexed proof."""
    def infer(u):
        if u[0] == 'var': return next(ty for name,ty in context if name == u[1])
        if u[0] == 'fst': return infer(u[1])[1]
        if u[0] == 'snd': return infer(u[1])[2]
        if u[0] == 'apply': return infer(u[1])[2]
        raise ValueError('annotation required')
    tag = t[0]
    if tag == 'var':
        index = next(i for i,(name,ty) in enumerate(context) if name == t[1] and ty == expected)
        member = 'here'
        for _ in range(index): member = '(there '+member+')'
        return '(hypothesis '+member+')'
    if tag == 'lambda':
        assert expected[0] == 'arrow'
        return '(abstraction '+intrinsic(t[2],expected[2],((t[1],expected[1]),)+context)+')'
    if tag == 'pair':
        assert expected[0] == 'product'
        return '(pair '+intrinsic(t[1],expected[1],context)+' '+intrinsic(t[2],expected[2],context)+')'
    if tag in ('fst','snd'):
        source = infer(t[1]); assert source[0] == 'product'
        assert source[1 if tag == 'fst' else 2] == expected
        return '('+('first' if tag == 'fst' else 'second')+' '+intrinsic(t[1],source,context)+')'
    source = infer(t[1]); assert source[0] == 'arrow' and source[2] == expected
    return '(application '+intrinsic(t[1],source,context)+' '+intrinsic(t[2],source[1],context)+')'

def size(t):
    if t[0]=='var': return 1
    if t[0]=='lambda': return 1+size(t[2])
    return 1+sum(size(x) for x in t[1:])

if __name__=='__main__':
    results={}
    for name,goal in [('forward',arr(W,D)),('backward',arr(D,W)),
                      ('swap',arr(nand(A,B),nand(B,A)))]: 
        search=Search(); term=search.solve(goal)
        if term is None: raise RuntimeError(name+' unresolved')
        results[name]={'term':term,'agda':render(term),'term_nodes':size(term),'search_visits':search.visits}
    # A control against an implicit double-negation-elimination rule.
    control=Search().solve(arr(D,C))
    assert control is None, 'unexpected classical rule or search defect'
    out=ROOT/'research/voevodsky/agda/GeneratedWolframRefutations.agda'
    out.write_text('''{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedWolframRefutations where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary.Properties using (isProp¬)

module Construct {ℓ : Level} (A B C : Type ℓ) where
  N : Type ℓ → Type ℓ → Type ℓ
  N X Y = (X × Y) → ⊥
  W : Type ℓ
  W = N (N (N A B) C) (N A (N (N A C) A))
  D : Type ℓ
  D = (C → ⊥) → ⊥
  forward : W → D
  forward = '''+results['forward']['agda']+'''
  backward : D → W
  backward = '''+results['backward']['agda']+'''
  -- Search supplies the maps; propositionality supplies their inverse laws.
  equivalence : W ≃ D
  equivalence = isoToEquiv record
    { fun = forward ; inv = backward
    ; rightInv = λ d → isProp¬ (C → ⊥) _ d
    ; leftInv = λ w → isProp¬ ((N (N A B) C) × (N A (N (N A C) A))) _ w }
  -- A further request to the same search, without a theorem-specific rule.
  swap : N A B → N B A
  swap = '''+results['swap']['agda']+'''\n''',encoding='utf-8')
    certificates = '''{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedWolframConstruction where
open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using ([])
open import RefutationConstructionWG

A B C : Formula
A = atom 0
B = atom 1
C = atom 2
N : Formula → Formula → Formula
N X Y = arrow (product X Y) bottom
W D : Formula
W = N (N (N A B) C) (N A (N (N A C) A))
D = arrow (arrow C bottom) bottom
'''
    for name,goal,label in [('forward',arr(W,D),'arrow W D'),
                            ('backward',arr(D,W),'arrow D W'),
                            ('swap',arr(nand(A,B),nand(B,A)),'arrow (N A B) (N B A)')]:
        certificates += '\n'+name+' : Proof [] ('+label+')\n'
        certificates += name+' = '+intrinsic(results[name]['term'],goal)+'\n'
        certificates += name+'-trace : Trace '+name+'\n'+name+'-trace = trace '+name+'\n'
        certificates += name+'-preserved : construct '+name+' ≡ '+name+'\n'
        certificates += name+'-preserved = construct-correct '+name+'\n'
    (ROOT/'research/voevodsky/agda/GeneratedWolframConstruction.agda').write_text(certificates,encoding='utf-8')
    packet={'scope':'bounded type-directed map synthesis; not the equational converse',
            'rules':['variable','pair','projection','lambda','application'],
            'fuel':24,'node_budget':200000,'maps':results,
            'double_negation_elimination_control':'not found (bounded negative, not a noninhabitation proof)'}
    (ROOT/'research/voevodsky/results/wg-ucc-audit/refutation-synthesis.json').write_text(json.dumps(packet,indent=2)+'\n')
    print(json.dumps({n:{k:v for k,v in r.items() if k not in ('term','agda')} for n,r in results.items()}))

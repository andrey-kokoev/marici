"""Replay published Otter equational inferences and emit explicit Agda proofs.
Sources: https://www.cs.unm.edu/~mccune/papers/basax/Sh-{1,2}.proof
The generator is untrusted: generated Agda must independently typecheck.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def parse(s):
    tokens = re.findall(r'[A-Za-z][A-Za-z0-9_]*|[(),]', s)
    i = 0
    def term():
        nonlocal i
        t = tokens[i]; i += 1
        if t != 'f': return t
        assert tokens[i] == '('; i += 1
        a = term()
        assert tokens[i] == ','; i += 1
        b = term()
        assert tokens[i] == ')'; i += 1
        return (a,b)
    t = term(); assert i == len(tokens)
    return t

def vars(t):
    return {t} if isinstance(t,str) else vars(t[0]) | vars(t[1])
def subst(t,s):
    if isinstance(t,str):
        return s.get(t,t)
    return tuple(subst(x,s) for x in t)
def rename(t,p): return subst(t,{v:p+v for v in vars(t)})
def walk(t,s):
    if isinstance(t,str): return walk(s[t],s) if t in s else t
    return tuple(walk(x,s) for x in t)
def unify(a,b):
    env = {}; todo = [(a,b)]
    while todo:
        a,b = (walk(t,env) for t in todo.pop())
        if a == b: continue
        if not isinstance(a,str) and isinstance(b,str): a,b = b,a
        if isinstance(a,str):
            if a in vars(b): return None
            env[a] = b
        elif isinstance(b,tuple): todo.extend(zip(a,b))
        else: return None
    return {k:walk(v,env) for k,v in env.items()}
def match(p,t,env=None):
    env = {} if env is None else env
    if isinstance(p,str):
        if p in env: return env if env[p] == t else None
        env[p] = t; return env
    if isinstance(t,str): return None
    env = match(p[0],t[0],env)
    return None if env is None else match(p[1],t[1],env)
def at(t,path):
    for p in path: t=t[p]
    return t
def replace(t,path,u):
    if not path:return u
    i=path[0]; out=list(t); out[i]=replace(t[i],path[1:],u); return tuple(out)
def positions(t):
    # innermost-leftmost first, matching Otter demodulation traversal
    if isinstance(t,tuple):
        for i in (0,1):
            for p in positions(t[i]): yield (i,)+p
    yield ()
def show(t):
    return t if isinstance(t,str) else '('+show(t[0])+' * '+show(t[1])+')'
def call(n,eq,prefix=''):
    return ('call',n,tuple(rename(v,prefix) for v in sorted(vars(eq[0])|vars(eq[1]))))
def ps(p,s):
    if p[0]=='call':return ('call',p[1],tuple(subst(t,s) for t in p[2]))
    if p[0]=='sym':return ('sym',ps(p[1],s))
    if p[0]=='trans':return ('trans',ps(p[1],s),ps(p[2],s))
    if p[0]=='cong':return ('cong',subst(p[1],s),p[2],ps(p[3],s))
    raise ValueError(p)
def proofvars(p):
    if p[0]=='call':return set().union(*(vars(t) for t in p[2]))
    if p[0]=='sym':return proofvars(p[1])
    if p[0]=='trans':return proofvars(p[1]) | proofvars(p[2])
    if p[0]=='cong':return vars(p[1]) | proofvars(p[3])
    raise ValueError(p)
def sym(p):return ('sym',p)
def trans(p,q):return ('trans',p,q)
def congr(t,path,p):return p if not path else ('cong',t,path,p)
def emit(p):
    tag=p[0]
    if tag=='call': return '('+p[1]+(' '+' '.join(show(t) for t in p[2]) if p[2] else '')+')'
    if tag=='sym': return '(sym '+emit(p[1])+')'
    if tag=='trans':return '(trans '+emit(p[1])+' '+emit(p[2])+')'
    if tag=='cong':return '(cong (λ hole → '+show(replace(p[1],p[2],'hole'))+') '+emit(p[3])+')'

def load(file):
    rows=[]
    for line in file.read_text().splitlines():
        m=re.match(r'([\d,]+) \[([^\]]*)\] (.*)\.$',line)
        if not m:continue
        ids=[int(x) for x in m[1].split(',')]
        body=m[3]
        if '!=' in body or '$' in body:continue
        a,b=body.split('=')
        rows.append((ids,m[2].split(',') if m[2] else [],(parse(a),parse(b))))
    return rows

def replay(rows,label,axiom):
    db={}; output=[]
    for ids,ann,goal in rows:
        n=ids[-1]; name=label+str(n)
        if not ann:
            if goal[0]==goal[1]:
                continue
            assert n==3
            proof=call(axiom,goal)
            current=goal
        elif ann[0] in ('para_into','para_from'):
            into,frm=ann[1:3] if ann[0]=='para_into' else ann[2:0:-1]
            def loc(s):
                v=[int(x) for x in s.split('.')];assert v[1]==1
                return v[0],tuple(x-1 for x in v[2:])
            ni,pi=loc(into); nf,pf=loc(frm)
            en,eq=db[ni]; fn,feq=db[nf]
            eq=tuple(rename(t,'i') for t in eq)
            feq=tuple(rename(t,'s') for t in feq)
            assert len(pf)==1
            u=unify(at(eq,pi),feq[pf[0]])
            assert u is not None,(label,n,'unification')
            eq=tuple(subst(t,u) for t in eq); feq=tuple(subst(t,u) for t in feq)
            source=ps(call(fn,db[nf][1],'s'),u)
            if pf[0]==1:source=sym(source)
            base=ps(call(en,db[ni][1],'i'),u)
            lifted=congr(eq[pi[0]],pi[1:],source)
            proof=trans(sym(lifted),base) if pi[0]==0 else trans(base,lifted)
            current=replace(eq,pi,feq[1-pf[0]])
        elif ann[0]=='back_demod':
            en,current=db[int(ann[1])];proof=call(en,current)
        else:raise ValueError((n,ann))
        if 'demod' in ann:
            start=ann.index('demod')+1
            for item in ann[start:]:
                if not item.isdigit():break
                dn,deq=db[int(item)]
                found=False
                for side in (0,1):
                    for path in positions(current[side]):
                        env=match(deq[0],at(current[side],path))
                        if env is None:continue
                        # A rewrite may not invent unconstrained variables.
                        assert vars(deq[1]) <= env.keys()
                        dproof=ps(call(dn,deq),env)
                        new=subst(deq[1],env)
                        lifted=congr(current[side],path,dproof)
                        proof=trans(sym(lifted),proof) if side==0 else trans(proof,lifted)
                        current=replace(current,(side,)+path,new)
                        found=True;break
                    if found:break
                assert found,(label,n,'demod failed',item)
        if 'flip.1' in ann:
            current=current[::-1];proof=sym(proof)
        env=match(current,goal)
        assert env is not None,(label,n,'result differs',current,goal)
        # Require renaming, not specialization, in the final printed clause.
        assert all(isinstance(t,str) for t in env.values()) and len(set(env.values()))==len(env)
        proof=ps(proof,env)
        names=sorted(vars(goal[0])|vars(goal[1]))
        proof=ps(proof,{v:names[0] for v in proofvars(proof)-set(names)})
        typ=('( '+' '.join(names)+' : A) → ') if names else ''
        output += [f'  {name} : {typ}{show(goal[0])} ≡ {show(goal[1])}',
                   f'  {name} '+ ' '.join(names)+' = '+emit(proof),'']
        for ident in ids:db[ident]=(name,goal)
    return db,output

if __name__=='__main__':
    second,lines2=replay(load(ROOT/'results/Sh-2.proof'),'s','sh2')
    first,lines1=replay(load(ROOT/'results/Sh-1.proof'),'t','sh1')
    header='''{-# OPTIONS --safe --cubical --guardedness #-}
-- Generated by checkers/build_wolfram_converse.py from published Otter proofs.
-- Every inference is an explicit use of congruence, symmetry, transitivity,
-- and substitution; no reflected solver or postulate is trusted.
module WolframConverse where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)

module Converse {ℓ : Level} (A : Type ℓ) (_|_ : A → A → A)
  (wolfram : (a b c : A) → ((a | b) | c) | (a | ((a | c) | a)) ≡ c) where
  infixl 20 _*_
  _*_ : A → A → A
  x * y = y | x

  sh2 : (x y z : A) → (((x * (y * x)) * x) * (y * (z * x))) ≡ y
  sh2 x y z = wolfram x z y

'''
    middle='''  sh1 : (x y z : A) → (x * ((y * x) * x)) * (y * (z * x)) ≡ y
  sh1 x y z = trans
    (cong (λ v → v * (y * (z * x))) (s2281 x y))
    (trans (cong (λ v → v * (y * (z * x))) (s2426 y x)) (s2556 x y z))

'''
    ending='''  neg : A → A
  neg x = x * x
  meet join : A → A → A
  meet x y = neg (x * y)
  join x y = neg x * neg y

  double-negation : (x : A) → neg (neg x) ≡ x
  double-negation x = t95 x x

  sheffer-2 : (x y : A) → x * (y * neg y) ≡ neg x
  sheffer-2 = t147

  sheffer-3 : (x y z : A)
    → ((neg y * x) * (neg z * x)) ≡ neg (x * (y * z))
  sheffer-3 x y z = t158 y x z

  original-is-nand : (x y : A) → (x | y) ≡ neg (meet x y)
  original-is-nand x y = trans (t93 y x) (sym (double-negation (x * y)))
'''
    out=ROOT/'agda/WolframConverse.agda'
    out.write_text((header+'\n'.join(lines2)+middle+'\n'.join(lines1)+ending).replace('|', '∣'),encoding='utf-8')
    print(f'Replayed {len(lines2)//3}+{len(lines1)//3} equations; emitted {out}')

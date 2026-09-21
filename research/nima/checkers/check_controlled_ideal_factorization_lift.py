"""Exact finite regressions for the universal-form/Fox factorization lift."""
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
from functools import lru_cache
import importlib.util
import json

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('descent',HERE/'check_seven_event_factorization_descent.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def add(out,col,scale=1):
    for k,v in col.items():out[k]+=scale*v


def mass(col):return sum(abs(v) for v in col.values())


def end(start,word):return start|sum(1<<j for j in word)


@lru_cache(None)
def bar(start,word,marks):
    # Unnormalized universal forms: d a = 1 tensor a - a tensor 1.
    out={(start,start):1};state=start
    for j,keep in zip(word,marks):
        target=state|(1<<j);nxt=defaultdict(int)
        for chain,c in out.items():
            if keep:
                nxt[chain[:-1]+(state,target)]+=c
                nxt[chain[:-1]+(target,target)]-=c
            else:nxt[chain[:-1]+(target,)]+=c
        out=f.clean(nxt);state=target
    # Normalize the last k incidence factors modulo vertex identities.
    return {chain:c for chain,c in out.items()
            if all(chain[i]!=chain[i+1] for i in range(1,len(chain)-1))}


@lru_cache(None)
def lift(chain):
    def block(x,y,derivative):
        word=tuple(i for i in range(y.bit_length()) if (y^x)&(1<<i))
        if not derivative:return {(word,(0,)*len(word)):1}
        return {(word,tuple(int(i==j) for i in range(len(word)))):1
                for j in range(len(word))}
    out=block(chain[0],chain[1],False)
    for x,y in zip(chain[1:-1],chain[2:]):out=f.multiply(out,block(x,y,True))
    return out


def bar_column(start,column):
    out=defaultdict(int)
    for (word,marks),c in column.items():add(out,bar(start,word,marks),c)
    return f.clean(out)


def section(column):
    out=defaultdict(int)
    for chain,c in column.items():add(out,lift(chain),c)
    return f.clean(out)


@lru_cache(None)
def generator(chain,j,keep):
    first=f.multiply(lift(chain),{((j,),(keep,)):1})
    out=defaultdict(int,first)
    add(out,section(bar_column(chain[0],first)),-1)
    return f.clean(out)


def fox(start,column):
    groups=defaultdict(lambda:defaultdict(int))
    for (word,marks),coefficient in column.items():
        for i,(j,keep) in enumerate(zip(word,marks)):
            for chain,c in bar(start,word[:i],marks[:i]).items():
                groups[chain,j,keep][word[i+1:],marks[i+1:]]+=coefficient*c
    return {key:f.clean(value) for key,value in groups.items() if f.clean(value)}


def factor_lift(start,column,depth):
    if depth==1:return {(key,):c for key,c in column.items()}
    out=defaultdict(int)
    for (chain,j,keep),suffix in fox(start,column).items():
        relation=generator(chain,j,keep)
        assert not bar_column(chain[0],relation)
        suffix_start=chain[-1]|(1<<j)
        # This necessary membership condition holds for inputs in I^depth.
        assert not bar_column(suffix_start,suffix)
        rest=factor_lift(suffix_start,suffix,depth-1)
        for left,c in relation.items():
            for right,d in rest.items():out[(left,)+right]+=c*d
    return f.clean(out)


def multiply_presentation(column):
    out=defaultdict(int)
    for factors,c in column.items():
        word=sum((p[0] for p in factors),())
        marks=sum((p[1] for p in factors),())
        out[word,marks]+=c
    return f.clean(out)


def main():
    words=0;forms=set();fox_checks=0
    for n in range(1,5):
        for word in permutations(range(n)):
            for marks in product((0,1),repeat=n):
                col={(word,marks):1};b=bar(0,word,marks)
                assert mass(b)<=2**sum(marks)
                forms.update(b)
                lifted=section(b)
                assert bar_column(0,lifted)==b
                actual=defaultdict(int)
                for (w,m),c in lifted.items():add(actual,f.record(0,w,m),c)
                assert f.clean(actual)==f.record(0,word,marks)
                telescoped=defaultdict(int)
                for (chain,j,keep),suffix in fox(0,col).items():
                    add(telescoped,f.multiply(generator(chain,j,keep),suffix))
                expected=defaultdict(int,col);add(expected,lifted,-1)
                assert f.clean(telescoped)==f.clean(expected)
                words+=1;fox_checks+=1
    for chain in forms:
        p=(chain[-1]^chain[0]).bit_count()
        assert mass(lift(chain))<=2**p
        assert bar_column(chain[0],lift(chain))=={chain:1}

    fixtures=[]
    for depth in (2,3):
        for kinds in product((0,1),repeat=depth):
            for suffix_length in (0,1,2):
                factors=[f.relation((2*i,2*i+1),kind) for i,kind in enumerate(kinds)]
                tail=tuple(range(2*depth,2*depth+suffix_length))
                factors[-1]=f.multiply(factors[-1],{(tail,(1,)*len(tail)):1})
                col=f.chain_product(factors)
                lifted=factor_lift(0,col,depth)
                assert multiply_presentation(lifted)==col
                n=2*depth+suffix_length
                assert mass(lifted)<=32**n*mass(col)
                fixtures.append({'depth':depth,'length':n,'source_mass':mass(col),'lift_mass':mass(lifted)})
    # Nonlocal kernel factors, not only products of local diamonds.
    for marks in product((0,1),repeat=3):
        left={( (2,0,1),marks):1}
        a=defaultdict(int,left);add(a,section(bar_column(0,left)),-1);a=f.clean(a)
        if not a:continue
        col=f.multiply(a,f.relation((3,4),1))
        lifted=factor_lift(0,col,2)
        assert multiply_presentation(lifted)==col
        assert mass(lifted)<=16**5*mass(col)
        fixtures.append({'depth':2,'length':5,'nonlocal':True,'source_mass':mass(col),'lift_mass':mass(lifted)})
    result={'passed':True,'marked_words_and_fox_telescoping_checks':words,
            'normalized_form_section_checks':len(forms),'factorization_fixtures':fixtures,
            'scope':'Finite exact regressions only. The uniform exponential bound and scale-intersection identification are proved in the companion note.'}
    out=HERE.parent/'results/controlled-ideal-factorization-lift.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'words':words,'forms':len(forms),'factorization_fixtures':len(fixtures)}))


if __name__=='__main__':main()

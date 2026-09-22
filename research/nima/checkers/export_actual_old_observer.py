"""Source-faithful presentation of O2 for the original two/four-event seeds.

Run with: uv run --with sympy python research/nima/checkers/export_actual_old_observer.py
The four-event seed is divided by its fixed positive late-sector factor.
"""
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
import importlib.util
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1];OTHER=ROOT.parent/'voevodsky'
spec=importlib.util.spec_from_file_location('source',OTHER/'certificates/verify_filtered_obstruction.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
r=S.Symbol('rho');zero=lambda n,m:S.zeros(n,m)


def frac(a):return S.Rational(a.numerator,a.denominator)
def tidy(m):return m.applyfunc(S.cancel)
def same(a,b):return all(S.cancel(x)==0 for x in a-b)
def pack(m):return [[str(S.cancel(x)) for x in row] for row in m.tolist()]


@lru_cache(None)
def source_corner(a,b):
    events=tuple(i for i in range(4) if (b^a)&(1<<i))
    paths=[(w,m) for w in permutations(events) for m in product((0,1),repeat=len(events))]
    records=[s.record(a,*p) for p in paths];keys=sorted(set().union(*(set(col) for col in records)))
    recorder=S.Matrix([[frac(col.get(k,0)) if col.get(k,0) else 0 for col in records] for k in keys])
    kernel=recorder.nullspace();k=S.Matrix.hstack(*kernel) if kernel else zero(len(paths),0)
    return paths,k


def main():
    # Each seed is an exact coefficient functional on the whole path domain.
    seeds=[('vacuum',0,3,{((0,1),(0,0)):S.Integer(1)}),
           ('old_residual',0,15,{((0,1,2,3),(1,0,0,0)):-r,((0,1,2,3),(0,1,0,0)):S.Integer(1)})]
    candidates={};context_count=0
    for family,start,end,terms in seeds:
        length=len(next(iter(terms))[0])
        # Every nonzero context must be a prefix/suffix of a supported seed word.
        for i in range(length+1):
            for j in range(i,length+1):
                groups={}
                for (word,marks),coef in terms.items():
                    context=(word[:i],marks[:i],word[j:],marks[j:])
                    groups.setdefault(context,{})[(word[i:j],marks[i:j])]=coef
                a,b=(1<<i)-1,(1<<j)-1
                for context,row in groups.items():
                    context_count+=1
                    candidates.setdefault((a,b),[]).append((family,context,row))
    corners={};guards=[];basis=[];offset=0
    for a in range(16):
        for b in range(16):
            if a&b!=a or (b^a).bit_count()<2:continue
            paths,k=source_corner(a,b);rows=candidates.get((a,b),[])
            raw=S.Matrix([[row.get(path,0) for path in paths] for _,_,row in rows]) if rows else zero(0,len(paths))
            values=raw*k
            independent=list(values.T.rref()[1])
            selected=raw[independent,:] if independent else zero(0,len(paths))
            evaluation=selected*k;rank=len(independent)
            pivots=list(evaluation.rref()[1])
            if rank:
                minor=evaluation[:,pivots];guards.append(S.factor(minor.det()))
                representatives=tidy(k[:,pivots]*minor.inv())
                assert same(selected*representatives,S.eye(rank))
            else:representatives=zero(len(paths),0)
            corners[a,b]={'paths':paths,'kernel':k,'rows':selected,'evaluation':evaluation,
                          'representatives':representatives,'offset':offset,'rank':rank}
            for local,selected_index in enumerate(independent):
                family,context,_=rows[selected_index]
                basis.append({'index':offset+local,'corner_masks':[a,b],'seed_family':family,
                    'prefix':list(context[0]),'prefix_marks':list(context[1]),
                    'suffix':list(context[2]),'suffix_marks':list(context[3])})
            offset+=rank
    n=offset
    def evaluate(a,b,source):
        if (a,b) not in corners:return zero(n,1)
        corner=corners[a,b];column=S.Matrix([source.get(path,0) for path in corner['paths']])
        out=zero(n,1);value=corner['rows']*column
        for i in range(corner['rank']):out[corner['offset']+i]=value[i]
        return tidy(out)
    def act_source(a,b,source,edge,side):
        u,event,mark=edge;v=u|(1<<event)
        if side=='left':
            if v!=a:return None
            return u,b,{((event,)+w,(mark,)+m):coef for (w,m),coef in source.items()}
        if b!=u:return None
        return a,v,{(w+(event,),m+(mark,)):coef for (w,m),coef in source.items()}
    representatives=[]
    for (a,b),corner in corners.items():
        for j in range(corner['rank']):
            source={path:corner['representatives'][i,j] for i,path in enumerate(corner['paths']) if corner['representatives'][i,j]!=0}
            representatives.append((a,b,source))
    edges=[(a,e,mark) for a in range(16) for e in range(4) if not a&(1<<e) for mark in (0,1)]
    actions={};equivariance_checks=0
    for side in ('left','right'):
        for edge in edges:
            columns=[]
            for a,b,source in representatives:
                acted=act_source(a,b,source,edge,side)
                columns.append(evaluate(*acted) if acted else zero(n,1))
            action=tidy(S.Matrix.hstack(*columns));actions[side,edge]=action
            # Check the evaluation kernel, not only selected state representatives.
            for (a,b),corner in corners.items():
                if (side=='left' and edge[0]|(1<<edge[1])!=a) or (side=='right' and b!=edge[0]):continue
                for j in range(corner['kernel'].cols):
                    source={path:corner['kernel'][i,j] for i,path in enumerate(corner['paths']) if corner['kernel'][i,j]!=0}
                    acted=act_source(a,b,source,edge,side)
                    assert same(evaluate(*acted),action*evaluate(a,b,source))
                    equivariance_checks+=1
    def word_action(a,word,marks,side):
        states=[a]
        for e in word:states.append(states[-1]|(1<<e))
        out=S.eye(n)
        seq=list(zip(states[:-1],word,marks))
        for edge in (reversed(seq) if side=='left' else seq):out=actions[side,edge]*out
        return tidy(out)
    ideal_images={}
    for side in ('left','right'):
        images=[]
        for a in range(16):
            for i in range(4):
                for j in range(i+1,4):
                    if a&((1<<i)|(1<<j)):continue
                    for kind in (0,1):
                        action=zero(n,n)
                        for (word,marks),coef in s.relation((i,j),kind).items():
                            action+=frac(coef)*word_action(a,word,marks,side)
                        images.append(tidy(action))
        image=S.Matrix.hstack(*images);cols=image.columnspace()
        ideal_images[side]=S.Matrix.hstack(*cols) if cols else zero(n,0)
    assert ideal_images['left'].cols==ideal_images['right'].cols==1
    assert S.Matrix.hstack(ideal_images['left'],ideal_images['right']).rank()==1
    # Every ideal action has >=2 events; another one exceeds this four-event packet.
    assert all(same(word_action(a,(i,j),(0,0),side)*ideal_images['left'],zero(n,1))
               for side in ('left','right') for a in range(16) for i in range(4) for j in range(4)
               if i!=j and not a&((1<<i)|(1<<j)))
    assert all(same(action*ideal_images['left'],zero(n,1)) for action in actions.values())
    a0=evaluate(0,3,s.relation((0,1),0));a1=evaluate(0,3,s.relation((0,1),1))
    initial=corners[0,3]
    assert initial['rank']==2 and initial['kernel'].cols==2
    initial_values=S.Matrix.hstack(a0,a1)[initial['offset']:initial['offset']+2,:]
    assert same(initial_values,S.diag(1,1-r))
    vacuum_projection=zero(1,n);vacuum_projection[0,initial['offset']]=1
    assert vacuum_projection*a0==S.ones(1,1)
    assert all(same(action*a0,zero(n,1)) and same(vacuum_projection*action,zero(1,n)) for action in actions.values())
    x=s.multiply({((0,1),(0,1)):1},s.relation((2,3),0))
    v2=s.multiply(s.relation((0,1),1),s.relation((2,3),0))
    xv=evaluate(0,15,x);uv=evaluate(0,15,v2)
    assert same((1-r)*xv,uv)
    # Exact specialization guards: the actual rho lies strictly between .45 and .48.
    all_expressions=guards+[entry for action in actions.values() for entry in action]+[
        value for _,_,source in representatives for value in source.values()]
    denominators=set()
    for expression in all_expressions:
        numerator,denominator=S.fraction(S.cancel(expression))
        denominators.add(denominator)
    for guard in guards:denominators.add(guard)
    for polynomial in denominators:
        poly=S.Poly(polynomial,r)
        assert poly.eval(S.Rational(9,20))!=0 and poly.eval(S.Rational(12,25))!=0
        assert poly.count_roots(S.Rational(9,20),S.Rational(12,25))==0
    def sparse(m):return [[i,j,str(m[i,j])] for i in range(m.rows) for j in range(m.cols) if m[i,j]!=0]
    artifact={'schema':'actual-old-observer-symbolic-presentation-v1',
        'protocol':'original unit vacuum seed on (2,3), plus original four-event residual seed; source ideal restricted to the background-two packet',
        'field':'Q(rho), specializing at the fixed actual ratio rho=A/B',
        'background':2,'event_primes':[2,3,5,7],
        'seeds':[{'family':family,'corner_masks':[a,b],
                  'terms':[{'word':list(w),'marks':list(m),'coefficient':str(value)}
                           for (w,m),value in terms.items()]} for family,a,b,terms in seeds],
        'calibration_guard':['9/20','12/25'],
        'calibration_guard_reference':'research/voevodsky/the-current-calibration-refinements-fix-one-physical-sector-ratio-not-a-family-of-observers.md',
        'dimension':n,'basis':basis,
        'initial_corner_evaluation':pack(initial_values),
        'first_transition':{'projection':pack(vacuum_projection),'section':pack(a0),'split':True},
        'source_representatives':[{'corner_masks':[a,b],'terms':[{'word':list(w),'marks':list(m),'coefficient':str(value)} for (w,m),value in source.items()]} for a,b,source in representatives],
        'actions':[{'side':side,'start_mask':edge[0],'event_index':edge[1],'retained':edge[2],'entries':sparse(action)} for (side,edge),action in actions.items()],
        'ideal_image_basis':pack(ideal_images['left']),'ideal_depth_dimensions':[n,1,0],
        'chosen_old_lift':{'x_evaluation':pack(xv),'v2_evaluation':pack(uv),'normalization':'(1-rho)*Obs2(x)=Obs2(v2)'},
        'audit':{'nonzero_context_candidates_before_restriction':context_count,'source_corners_checked':len(corners),
                 'source_action_checks':equivariance_checks,'marked_prime_action_matrices':len(actions),
                 'specialization_guards':[str(x) for x in sorted(denominators,key=str)]},
        'boundary':['actual fixed calibration identification remains an owning analytical hypothesis',
                    'positive common seed factors are removed by whole-family normalization',
                    'this is O2, not the full 270-row O3 or a four-tower tetrahedron']}
    (ROOT/'results/actual-old-observer-symbolic.json').write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'dimension':n,'ideal_depth_dimensions':[n,1,0],**artifact['audit']},indent=2))


if __name__=='__main__':main()

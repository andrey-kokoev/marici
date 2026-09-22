"""Portable combinatorial certificate for combined output plus raw row 76.

Standard library only; no solver, producer, discovery checker or integration.
Certifies the specified vacuum-increment comparison, not full raw-observer
reconstruction. Nonzero physical responses remain declared hypotheses.
"""
from itertools import combinations,permutations,product
from fractions import Fraction
from collections import defaultdict
from pathlib import Path
import hashlib,json,sys

def need(ok,message):
    if not ok:raise ValueError(message)
def frozen(x):return tuple(frozen(y) for y in x) if isinstance(x,list) else x
def fields(x,keys):need(type(x) is dict and set(x)==set(keys),'unexpected fields')
def no_duplicates(items):
    d={}
    for k,v in items:need(k not in d,'duplicate key');d[k]=v
    return d
def bad_number(x):raise ValueError('nonfinite number')
def load(path):return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=no_duplicates,parse_constant=bad_number)
def multiply(a,b):
    out=defaultdict(int)
    for (w,m),c in a.items():
        for (v,n),d in b.items():out[w+v,m+n]+=c*d
    return {k:c for k,c in out.items() if c}
def forgotten(pair):
    return {(tuple(pair),(0,0)):1,(tuple(reversed(pair)),(0,0)):-1}
def profile(col,depth=3):
    out=defaultdict(int)
    for (word,marks),coefficient in col.items():
        states=[0]
        for event in word:
            need(not states[-1]&(1<<event),'repeated event')
            states.append(states[-1]|(1<<event))
        windows=tuple((states[k],states[k+1]) for k,m in enumerate(marks) if m)
        for cuts in combinations(range(len(word)),depth):
            bounds=(-1,)+cuts+(len(word),)
            seams=tuple(('e',states[k],states[k+1],marks[k]) for k in cuts)
            buffers=tuple(sum(marks[a+1:b]) for a,b in zip(bounds,bounds[1:]))
            out[(seams,buffers),windows]+=coefficient
    return {key:value for key,value in out.items() if value}
def contexts(col,i,j,last=6,degree=2):
    for pre in permutations(range(i)):
        for post in permutations(range(j,last)):
            for marks in product((0,1),repeat=len(pre)+len(post)):
                if sum(marks)!=degree:continue
                yield multiply(multiply({(pre,marks[:len(pre)]):1},col),{(post,marks[len(pre):]):1})
def original_sectors(depth):
    for choices in product((0,1),repeat=depth-1):
        seams=[]
        for i,c in enumerate(choices):
            start=(1<<(2*i))-1
            seams.append(('e',start|(1<<(2*i)),(1<<(2*i+2))-1,1) if c else ('e',start,start|(1<<(2*i)),1))
        start=(1<<(2*(depth-1)))-1
        seams.append(('e',start,start|(1<<(2*(depth-1))),0))
        yield tuple(seams),(0,)*(depth+1)
def other_shapes():
    out=set(original_sectors(3))
    pairings=sorted({tuple(tuple(sorted(p[k:k+2])) for k in (0,2,4)) for p in permutations(range(6))})
    for pairs in pairings:
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            state=0;seams=[]
            for pair,kind in zip(pairs,kinds):
                seams.append(('e',state,state|(1<<min(pair)),kind));state|=sum(1<<p for p in pair)
            out.add((tuple(seams),(0,)*4))
    for p1,p2 in (((0,1),(2,3)),((0,2),(1,3))):
        start=sum(1<<p for p in p1)
        for p,q,last in product(p1,p2,(4,5)):
            out.add(((('e',0,1<<p,1),('e',start,start|(1<<q),1),('e',15,15|(1<<last),0)),(0,)*4))
    return out
SHAPE=((('e',0,1,1),('e',7,15,0),('e',15,31,0)),(0,1,0,0))
SHARED=((0,2),(1,3),(1,4),(2,4),(3,5),(3,6),(4,6))
RAW_BASIS=((0,3),(0,4),(0,5),(0,6),(1,5),(1,6))
CONTRACT={
 'retained_products':['combined_scalar_with_existing_error_fields','unscaled_joint_filter_row'],
 'raw_error_rule':'component_error_at_most_total_joint_l1_error',
 'comparison_target':'background-two vacuum acquisition kernel, not complete raw observer',
 'external_hypotheses':['common filter nonzero on windows [2,4] and [4,12]',
   '270 declared private rows have nonzero response factors',
   'fixed labelled source and unchanged first two observer stages',
   'declared acquired readings and error budget are valid']}
def verify(manifest_path,policy):
    fields(policy,('schema','manifest_sha256','raw_row_index','raw_shape','contract','raw_increment_intervals','inherited_filtration_dimensions'))
    need(policy['schema']=='minimal-matched-retention-v1','schema')
    need(policy['contract']==CONTRACT,'retention contract')
    need(policy['manifest_sha256']==hashlib.sha256(Path(manifest_path).read_bytes()).hexdigest(),'manifest digest')
    need(type(policy['raw_row_index']) is int and policy['raw_row_index']==76,'unsupported selected row')
    need(frozen(policy['raw_shape'])==SHAPE,'wrong selected shape')
    need(frozen(policy['raw_increment_intervals'])==RAW_BASIS,'wrong increment basis')
    need(policy['inherited_filtration_dimensions']==[6,5,1,0] and all(type(x) is int for x in policy['inherited_filtration_dimensions']),'wrong filtration')
    m=load(manifest_path);need(len(m['rows'])==449,'manifest row count')
    rows={}
    for row in m['rows']:
        fields(row,('shape','sign','coefficient'))
        shape=frozen(row['shape'])
        need(shape not in rows,'duplicate shape')
        need(type(row['sign']) is int and row['sign'] in (-1,1),'sign')
        need(row['coefficient'] in ('crossed','positive'),'gain label')
        need(len(shape[0])==3 and len(shape[1])==4,'shape arity')
        need(all(type(n) is int and n>=0 for n in shape[1]),'buffer count')
        for edge in shape[0]:
            need(len(edge)==4 and edge[0]=='e' and all(type(z) is int for z in edge[1:]),'typed seam')
            _,a,b,k=edge
            need(0<=a<b<=63 and a&b==a and (b-a).bit_count()==1 and k in (0,1),'invalid seam')
        need(sum(e[3] for e in shape[0])+sum(shape[1])==2,'not a two-feature block')
        rows[shape]=(row['sign'],row['coefficient'])
    need(frozen(m['rows'][76]['shape'])==SHAPE,'manifest index/shape mismatch')
    need(sum(label=='positive' for sign,label in rows.values())==1,'reserved block count')
    for label in ('crossed','positive'):
        values=m['coefficients_per_w_squared'][label]
        need(len(values)==2 and all(type(x) is str for x in values),'rational gain pair')
        need(Fraction(values[0])/Fraction(values[1])!=0,'zero gain')
    others=other_shapes()
    def scalar_zero(image):
        need(not any(shape in others for shape,windows in image),'other old row detects witness')
        groups=defaultdict(int)
        for (shape,windows),value in image.items():
            if shape in rows:
                sign,label=rows[shape];groups[label,windows]+=sign*value
        need(not any(groups.values()),'combined test detects witness')
    def invisible_all(col,i,j):
        for full in contexts(col,i,j):
            image=profile(full)
            need(not any(shape in rows or shape in others for shape,windows in image),'retained raw row detects residual witness')
        for depth,last in ((1,2),(2,4)):
            if j<=last:
                for full in contexts(col,i,j,last,depth-1):
                    need(not any(shape in set(original_sectors(depth)) for shape,windows in profile(full,depth)),'lower detector sees witness')
    # Verify that the original private rows already retain seven vacuum
    # interval coefficients: place both marked slots outside each interval.
    for i,j in SHARED:
        choices=[k for k in ((1,1,0),(1,0,1),(0,1,1)) if all(not k[p//2] for p in range(i,j) if p%2==0)]
        need(bool(choices),'shared interval not supplied by private family')
    # The signed old test supplies (2,5), but not the (2,6) direction below.
    for word in permutations(range(2,5)):
        image=profile({((0,1)+word+(5,),(1,1,0,0,0,0)):1})
        groups=defaultdict(int)
        for (shape,windows),value in image.items():
            if shape in rows:
                sign,label=rows[shape];groups[label,windows]+=sign*value
        groups={key:value for key,value in groups.items() if value}
        expected={('crossed',((0,1),(1,3))):2} if word==(2,3,4) else {}
        need(groups==expected,'extra shared corner identity')
    # The selected single row sees exactly the canonical four-event word.
    for word in permutations(range(2,6)):
        image=profile({((0,1)+word,(1,1,0,0,0,0)):1})
        need(image.get((SHAPE,((0,1),(1,3))),0)==int(word==(2,3,4,5)),'selected row identity')
    h={((2,3,4,5),(0,)*4):1,((2,3,5,4),(0,)*4):1,((2,4,3,5),(0,)*4):-2}
    need(sum(h.values())==0,'witness not in forgotten ideal')
    for full in contexts(h,2,6):scalar_zero(profile(full))
    need(profile(multiply({((0,1),(1,1)):1},h)).get((SHAPE,((0,1),(1,3))),0)==1,'minimality witness')
    # Six different source corners remain invisible even to ALL raw rows.
    for i,j in RAW_BASIS:
        w=tuple(range(i,j));alt=(w[1],w[0])+w[2:]
        invisible_all({(w,(0,)*len(w)):1,(alt,(0,)*len(w)):-1},i,j)
    # Actual I^2 lifts establish the five-dimensional second level.
    for i,j in RAW_BASIS:
        if j-i<4:continue
        col=multiply(multiply(forgotten((i,i+1)),forgotten((i+2,i+3))),{(tuple(range(i+4,j)),(0,)*(j-i-4)):1})
        need(col.get((tuple(range(i,j)),(0,)*(j-i)),0)==1,'I2 lift coefficient')
        invisible_all(col,i,j)
    cubic=multiply(multiply(forgotten((0,1)),forgotten((2,3))),forgotten((4,5)))
    need(len(cubic)==8 and not any(shape in rows or shape in others for shape,w in profile(cubic)),'vacuum cubic invisibility')
    return {'verified':True,'additional_retained_raw_rows':1,'selected_index_zero_based':76,
      'same_vacuum_increment_as_all_raw_rows':True,'increment_dimension':6,
      'inherited_filtration_dimensions':[6,5,1,0],
      'minimality':'zero extra rows fails; one specified raw row suffices for this comparison',
      'scope':CONTRACT['comparison_target'],'external_hypotheses':CONTRACT['external_hypotheses']}
if __name__=='__main__':
    try:
        need(len(sys.argv)==3,'usage: verify_minimal_matched_retention.py MANIFEST.json POLICY.json')
        print(json.dumps(verify(sys.argv[1],load(sys.argv[2])),indent=2))
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError) as exc:
        print('REJECTED: '+str(exc),file=sys.stderr);sys.exit(1)

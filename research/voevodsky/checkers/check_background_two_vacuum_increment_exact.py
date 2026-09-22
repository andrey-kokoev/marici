"""Audit the eight potentially new vacuum corners against the full old union.

Use blockwise vanishing where available, and the declared signed common
matched test where necessary. Independent analytical blocks must not be
silently substituted for a single calibrated detector.
"""
from pathlib import Path
from itertools import permutations,product
import runpy,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
a=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_270_row_alternative_nullhomotopy.py'))
f=a['f'];raw3=a['raw3'];t=a['t']
vacshape=((('e',0,1,0),('e',3,7,0),('e',15,31,0)),(0,0,0,0))
selected=set(a['selected'])-{vacshape}
J=a['a']['J'];reserve=a['a']['reserve'][0]
# The matched test is ONE signed common-waveform functional, not 448
# independent detector rows. Retain the other independently declared rows.
other=set(a['pivots'])
other.update((row[0],(0,0,0,0)) for row,weight in t['selected'](3))
for pair1,pair2 in (((0,1),(2,3)),((0,2),(1,3))):
    start=sum(1<<p for p in pair1)
    for p,q,last in product(pair1,pair2,(4,5)):
        other.add(((('e',0,1<<p,1),('e',start,start|(1<<q),1),('e',15,15|(1<<last),0)),(0,0,0,0)))
def detector_values(col):
    out={}
    for (shape,windows),value in raw3(col).items():
        if shape in other or shape==reserve:out['separate',shape,windows]=value
        if shape in J:
            key=('matched_common_test',windows)
            out[key]=out.get(key,0)+J[shape]*value
    return {key:value for key,value in out.items() if value}
shared={(0,2),(1,3),(1,4),(2,4),(3,5),(3,6),(4,6)}
intervals=[(i,j) for i in range(7) for j in range(i+2,7)]
results=[]
for i,j in intervals:
    if (i,j) in shared:continue
    word=tuple(range(i,j));other=(word[1],word[0])+word[2:]
    source={(word,(0,)*len(word)):1,(other,(0,)*len(word)):-1}
    contexts=0;overlaps=[]
    for pre in permutations(range(i)):
        for post in permutations(range(j,6)):
            for marks in product((0,1),repeat=len(pre)+len(post)):
                if sum(marks)!=2:continue
                col=f['multiply'](f['multiply']({(pre,marks[:len(pre)]):1},source),{(post,marks[len(pre):]):1})
                im=raw3(col);seen=[key for key,c in im.items() if key[0] in selected]
                contexts+=1
                if seen:overlaps.append({'prefix':list(pre),'suffix':list(post),'marks':list(marks),'block_count':len(seen)})
    # Old stages have support ending at masks 3 and 15 respectively.
    lower_checks=0;lower_nonzero=[]
    for depth,last in ((1,2),(2,4)):
        if j>last:continue
        for pre in permutations(range(i)):
            for post in permutations(range(j,last)):
                for marks in product((0,1),repeat=len(pre)+len(post)):
                    if sum(marks)!=depth-1:continue
                    col=f['multiply'](f['multiply']({(pre,marks[:len(pre)]):1},source),{(post,marks[len(pre):]):1})
                    im=t['ordered'](0,col,depth)
                    # Require each selected sector to vanish, not just score cancellation.
                    values=[im.get(row,0) for row,weight in t['selected'](depth)]
                    lower_checks+=1
                    if any(values):lower_nonzero.append(values)
    repaired=None
    if overlaps:
        words=list(permutations(range(i,j)));constraints={}
        for pre in permutations(range(i)):
            for post in permutations(range(j,6)):
                for marks in product((0,1),repeat=len(pre)+len(post)):
                    if sum(marks)!=2:continue
                    context=(pre,post,marks)
                    for index,w in enumerate(words):
                        col={(pre+w+post,marks[:len(pre)]+(0,)*len(w)+marks[len(pre):]):1}
                        for key,value in detector_values(col).items():
                            constraints.setdefault((context,key),[0]*len(words))[index]=value
        equations=[[1]*len(words)]+list(constraints.values())
        equations.append([int(w==word) for w in words])
        matrix=s.Matrix(equations);rhs=s.Matrix([0]*(len(equations)-1)+[1])
        try:
            solution,params=matrix.gauss_jordan_solve(rhs)
            solution=solution.subs({p:0 for p in params})
            assert matrix*solution==rhs
            repaired=[{'word':list(w),'coefficient':str(c)} for w,c in zip(words,solution) if c]
        except ValueError:pass
    results.append({'interval':[i,j],'cubic_contexts':contexts,'nonzero_block_contexts':overlaps,
                    'replacement_annihilator':repaired,
                    'lower_contexts':lower_checks,'lower_nonzero':lower_nonzero})
# The common matched test exposes one more shared corner. Keep its signed
# block sum and actual window pair, rather than pretending blocks are rows.
for end in (5,6):
    words=list(permutations(range(2,end)));values=[]
    for w in words:
        col={((0,1)+w+tuple(range(end,6)),(1,1)+(0,)*4):1}
        image=detector_values(col)
        assert all(key[0]=='matched_common_test' for key in image)
        assert all(key[1]==((0,1),(1,3)) for key in image)
        values.append(sum(image.values()))
    canonical=tuple(range(2,end))
    if end==5:
        assert values==[2*int(w==canonical) for w in words]
    else:
        switched=(2,3,5,4)
        assert values==[2*int(w==canonical)-2*int(w==switched) for w in words]
extra_shared=(2,5)
remaining=[r for r in results if tuple(r['interval'])!=extra_shared]
passed=all((not r['nonzero_block_contexts'] or r['replacement_annihilator'] is not None) and not r['lower_nonzero'] for r in remaining)
assert passed
# At the (2,6) corner, inspect the entire minimal all-forgotten I^2 basis.
# The last two events are a forgotten diamond: on I^2 the reversed-last
# coefficient is the negative of the canonical coefficient.
import itertools
pairings=sorted({tuple(tuple(sorted(p[k:k+2])) for k in (0,2)) for p in itertools.permutations(range(2,6))})
for pairs in pairings:
    col=f['multiply'](f['relation'](pairs[0],0),f['relation'](pairs[1],0))
    can=col.get(((2,3,4,5),(0,0,0,0)),0)
    rev=col.get(((2,3,5,4),(0,0,0,0)),0)
    assert rev==-can
# For the other five depth-two corners construct actual I^2 annihilators,
# not merely I-elements of sufficient path length.
depth_two=[]
for r in remaining:
    i,j=r['interval']
    if j-i<4 or (i,j)==(2,6):continue
    factors=[f['relation']((i,i+1),0),f['relation']((i+2,i+3),0)]
    col=f['multiply'](f['multiply'](*factors),{(tuple(range(i+4,j)),(0,)*(j-i-4)):1})
    assert col.get((tuple(range(i,j)),(0,)*(j-i)),0)==1
    for pre in permutations(range(i)):
        for post in permutations(range(j,6)):
            for marks in product((0,1),repeat=len(pre)+len(post)):
                if sum(marks)!=2:continue
                full=f['multiply'](f['multiply']({(pre,marks[:len(pre)]):1},col),{(post,marks[len(pre):]):1})
                assert not detector_values(full)
    depth_two.append([i,j])
assert len(depth_two)==5
D=[tuple(r['interval']) for r in remaining]
assert len(D)==7
left_actions=[];right_actions=[]
for k in range(6):
    left=[(p,(k,p[1])) for p in D if p[0]==k+1]
    right=[(p,(p[0],k+1)) for p in D if p[1]==k]
    assert all(target in D for source,target in left+right)
    left_actions.append({'edge_index':k,'maps':left})
    right_actions.append({'edge_index':k,'maps':right})
ID={(i-2,j) for i,j in D if i>=2}
DI={(i,j+2) for i,j in D if j<=4}
assert ID=={(0,6)} and DI=={(0,5),(0,6)}
result={'passed':passed,'increment_dimension':7,
        'increment_basis_intervals':D,'left_edge_actions':left_actions,'right_edge_actions':right_actions,
        'intrinsic_left_ideal_image':sorted(ID),'intrinsic_right_ideal_image':sorted(DI),'inherited_filtration_dimensions':[7,5,1,0],
        'extra_shared_interval':list(extra_shared),'depth_two_increment_intervals':depth_two,'old_nonvacuum_analytical_blocks':len(selected),
        'shared_intervals':sorted(shared),'candidate_new_intervals':results,
        'scope':'Full declared old union with its signed common matched test, not independently retained analytical blocks. Exclusion witnesses use exact equal-window cancellation; inclusion of the extra shared corner uses the owning nonzero common-window norming response.'}
(ROOT/'research/voevodsky/results/background-two-vacuum-increment-exact.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

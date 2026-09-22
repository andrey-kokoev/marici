"""Compile the three retained ideal cubic frames on the full actual source.

Window responses remain fixed analytical quantities, not independent channels.
No generic rank or independent-coordinate claim is made.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from collections import defaultdict, Counter
import importlib.util
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('private_core',ROOT/'checkers/export_actual_private_observer_core.py')
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
s=core.s


def clean(values):return {key:int(value) for key,value in values.items() if value}


def pairings(items):
    if not items:
        yield ();return
    for pair in combinations(items,2):
        for tail in pairings(tuple(e for e in items if e not in pair)):
            yield (pair,)+tail


def vertices(start,word):
    out=[start]
    for e in word:
        assert not out[-1]&(1<<e)
        out.append(out[-1]|(1<<e))
    return out


def raw_derivative(start,pair,kind):
    result=[]
    for (word,marks),coefficient in s.relation(pair,kind).items():
        states=vertices(start,word)
        for cut in (0,1):
            seam=('e',states[cut],states[cut+1],marks[cut])
            buffers=tuple(tuple((states[k],states[k+1]) for k in indices if marks[k])
                          for indices in (range(cut),range(cut+1,2)))
            result.append(((seam,),buffers,int(coefficient)))
    return result


def join(a,b):
    sa,ba,ca=a;sb,bb,cb=b
    return sa+sb,ba[:-1]+(ba[-1]+bb[0],)+bb[1:],ca*cb


def columns_and_shapes():
    columns=[];shape_rows=defaultdict(dict)
    for pairs in pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            source={((),()):1};start=0;parts=[]
            for pair,kind in zip(pairs,kinds):
                source=s.multiply(source,s.relation(pair,kind))
                parts.append(raw_derivative(start,pair,kind))
                start|=sum(1<<e for e in pair)
            entries=[];seen=set()
            for triple in product(*parts):
                seams,buffers,coefficient=join(join(triple[0],triple[1]),triple[2])
                shape=(seams,tuple(map(len,buffers)))
                assert shape not in seen;seen.add(shape)
                windows=[]
                for i,seam in enumerate(seams):
                    windows.extend(buffers[i])
                    if seam[3]:windows.append((seam[1],seam[2]))
                windows.extend(buffers[-1]);windows=tuple(windows)
                assert len(windows)==2
                entries.append((shape,coefficient,windows))
                shape_rows[shape][len(columns)]=(coefficient,windows)
            assert len(entries)==256
            columns.append({'pairs':pairs,'kinds':kinds,'source':source,'entries':entries})
    assert len(columns)==270 and len(shape_rows)==48960
    return columns,shape_rows


def expand_shape(shape):
    """Inverse of the ordered seam/memory recorder, including ALL buffer orders."""
    seams,degrees=shape;segments=[];cursor=0
    for index in range(4):
        end=seams[index][1] if index<3 else 63
        assert cursor&end==cursor
        events=tuple(e for e in range(6) if (end^cursor)&(1<<e))
        choices=[]
        for word in permutations(events):
            for retained in combinations(range(len(word)),degrees[index]):
                choices.append((word,tuple(int(k in retained) for k in range(len(word)))))
        segments.append(choices)
        if index<3:
            _,a,b,mark=seams[index];event=(a^b).bit_length()-1
            assert a^(1<<event)==b
            segments.append([((event,),(mark,))]);cursor=b
    for pieces in product(*segments):
        word=tuple(e for w,m in pieces for e in w)
        marks=tuple(e for w,m in pieces for e in m)
        assert len(word)==6 and sum(marks)==2
        yield word,marks


def path_windows(path):
    word,marks=path;states=vertices(0,word)
    return tuple((states[k],states[k+1]) for k in range(6) if marks[k])


def potential_polynomial(window_polynomial):
    """Use the REQUIRED additivity W(a,b)=W(0,b)-W(0,a), W(0,0)=0."""
    result=Counter()
    for ((a,b),(c,d)),coefficient in window_polynomial.items():
        for x,sx in ((b,1),(a,-1)):
            for y,sy in ((d,1),(c,-1)):
                if x and y:result[tuple(sorted((x,y)))]+=coefficient*sx*sy
    return clean(result)


def evaluate_component(component,source):
    result=Counter()
    for path,value in source.items():
        if path in component:result[path_windows(path)]+=int(value)*component[path]
    return clean(result)


def polynomial_json(poly):
    return [{'windows':windows,'coefficient':value} for windows,value in sorted(poly.items())]


def frame_definitions(columns,shape_rows):
    two=[{},{}];sixteen=[{},{}]
    for slot,(target,first,second) in enumerate(((0,(0,1),(2,3)),(18,(0,2),(1,3)))):
        start2=sum(1<<e for e in first)
        for p,q,last in product(first,second,(4,5)):
            shape=((('e',0,1<<p,1),('e',start2,start2|(1<<q),1),
                    ('e',15,15|(1<<last),0)),(0,0,0,0))
            assert set(shape_rows[shape])=={target}
            sign,_=shape_rows[shape][target]
            assert abs(sign)==1
            sixteen[slot][shape]=sign
            if (p,q,last)==(first[0],second[0],4):two[slot][shape]=sign
    support={shape for shape,sign,windows in columns[18]['entries']}
    matched={shape:sign for shape,sign,windows in columns[18]['entries']}
    # Preserve the OWNING matching: a fresh greedy run can choose different
    # private corrections merely because source terms have a different order.
    path=ROOT.parent/'grothendieck/results/exact-cubic-norming-rows.json'
    frozen=json.loads(path.read_text())
    def freeze(value):return tuple(map(freeze,value)) if isinstance(value,list) else value
    reserve=freeze(frozen['reserved_positive_shape'])
    assert shape_rows[reserve[0]]=={0:(reserve[1],reserve[2])}
    assert reserve[2]==((0,1),(3,7)) and reserve[0] not in support
    expected={(j,shape) for j,column in enumerate(columns) if j!=18
              for shape,sign,windows in column['entries'] if shape in support}
    visited=set()
    for entry in frozen['correcting_private_rows']:
        j=entry['column'];shape=freeze(entry['shared_shape']);replacement=freeze(entry['private_shape'])
        windows=freeze(entry['ordered_windows']);coefficient=entry['correction_sign']
        assert (j,shape) in expected and (j,shape) not in visited
        visited.add((j,shape))
        sign,actual_windows=shape_rows[shape][j]
        assert actual_windows==windows and set(shape_rows[replacement])=={j}
        replacement_sign,replacement_windows=shape_rows[replacement][j]
        assert replacement_windows==windows
        assert replacement not in matched and replacement!=reserve[0]
        assert coefficient==-matched[shape]*sign*replacement_sign
        matched[replacement]=coefficient
    assert visited==expected and len(visited)==192 and len(matched)==448
    return [('two_private','R',two),('sixteen_private','R',sixteen),
            ('matched_memory','N',[{reserve[0]:reserve[1]},matched])]


def compile_frame(name,mode,blocks,columns):
    components=[];denominators=[];checks=0
    for slot,shapes in enumerate(blocks):
        component=Counter()
        for shape,sign in shapes.items():
            for path in expand_shape(shape):component[path]+=sign
        component=clean(component);components.append(component)
        target=(0,18)[slot]
        # Compute the normalizer independently in the factored cubic record.
        denominator=Counter()
        for shape,sign,windows in columns[target]['entries']:
            denominator[windows]+=shapes.get(shape,0)*sign
        denominator=clean(denominator)
        assert denominator and all(value>0 for value in denominator.values())
        denominators.append(denominator)
        for j,column in enumerate(columns):
            actual=potential_polynomial(evaluate_component(component,column['source']))
            expected=potential_polynomial(denominator) if j==target else {}
            assert actual==expected,(name,slot,j)
            checks+=1
    paths=sorted(set(components[0])|set(components[1]))
    rows={}
    for word,marks in paths:
        coefficients=tuple(component.get((word,marks),0) for component in components)
        windows=path_windows((word,marks))
        for left in range(5):
            for right in range(left+2,7):
                context=(word[:left],marks[:left],word[right:],marks[right:])
                rows.setdefault(context,{})[word[left:right],marks[left:right]]=(windows,coefficients)
    contexts=sorted(rows);index={context:i for i,context in enumerate(contexts)}
    actions=defaultdict(dict);identities=0
    for context in contexts:
        pre,pm,suf,sm=context;row=index[context]
        a=sum(1<<e for e in pre);b=63^sum(1<<e for e in suf)
        groups=defaultdict(dict)
        for (word,marks),value in rows[context].items():
            if len(word)==2:continue # I has no zero- or one-event component.
            groups['left',a,word[0],marks[0]][word[1:],marks[1:]]=value
            groups['right',b^(1<<word[-1]),word[-1],marks[-1]][word[:-1],marks[:-1]]=value
        for (side,start,event,mark),terms in groups.items():
            child=(pre+(event,),pm+(mark,),suf,sm) if side=='left' else (pre,pm,(event,)+suf,(mark,)+sm)
            assert rows[child]==terms
            actions[side,start,event,mark][row]=index[child]
            identities+=1
    commuting=0
    def twice(row,left,right):
        mid=actions.get(left,{}).get(row)
        return None if mid is None else actions.get(right,{}).get(mid)
    for context in contexts:
        pre,pm,suf,sm=context;a=sum(1<<e for e in pre);b=63^sum(1<<e for e in suf)
        terms=rows[context];row=index[context]
        left={('left',a,w[0],m[0]) for w,m in terms}
        right={('right',b^(1<<w[-1]),w[-1],m[-1]) for w,m in terms}
        for le,re in product(left,right):
            assert twice(row,le,re)==twice(row,re,le)
            commuting+=1
    output_rows=[]
    for context in contexts:
        pre,pm,suf,sm=context
        output_rows.append({'context':context,'corner_masks':[sum(1<<e for e in pre),63^sum(1<<e for e in suf)],
            'terms':[{'word':word,'marks':marks,'windows':windows,'component_coefficients':coefficients}
                     for (word,marks),(windows,coefficients) in sorted(rows[context].items())]})
    return {'family':name,'response':mode,'aggregate_seed_count':1,'seed_row':index[((),(),(),())],
        'coefficient_rule':'For each term sum over j=0,1: component_coefficients[j] * S[j] * W(windows[0]) * W(windows[1]) / denominator[j]. One scalar coordinate per row, NOT one per component.',
        'denominators':[polynomial_json(poly) for poly in denominators],
        'selected_blocks':[[{'shape':shape,'sign':sign} for shape,sign in shapes.items()] for shapes in blocks],
        'rows':output_rows,
        'actions':[{'side':side,'start_mask':start,'event_index':event,'retained':mark,
                    'entries':[[row,column,'1'] for row,column in sorted(matrix.items())]}
                   for (side,start,event,mark),matrix in sorted(actions.items())],
        'audit':{'source_paths':len(paths),'contextual_rows':len(rows),'action_coefficient_identities':identities,
                 'commuting_context_checks':commuting,'full_source_top_component_checks':checks}},components


def check_forward_all_paths(definitions,compiled):
    """Independent forward recorder check on ALL 10,800 two-feature paths."""
    weights=defaultdict(list)
    for family_index,(_,_,blocks) in enumerate(definitions):
        for slot,shapes in enumerate(blocks):
            for shape,sign in shapes.items():weights[shape].append((2*family_index+slot,sign))
    components=[component for family in compiled for component in family]
    cuts=list(combinations(range(6),3));checked=0
    for word in permutations(range(6)):
        states=vertices(0,word)
        for retained in combinations(range(6),2):
            marks=tuple(int(i in retained) for i in range(6));prefix=[0]
            for mark in marks:prefix.append(prefix[-1]+mark)
            actual=[0]*6
            for i,j,k in cuts:
                seams=tuple(('e',states[t],states[t+1],marks[t]) for t in (i,j,k))
                degrees=(prefix[i],prefix[j]-prefix[i+1],prefix[k]-prefix[j+1],prefix[6]-prefix[k+1])
                for index,sign in weights.get((seams,degrees),()):actual[index]+=sign
            assert actual==[component.get((word,marks),0) for component in components],(word,marks)
            checked+=1
    assert checked==10800
    return {'all_two_feature_full_corner_paths':checked,'scalar_component_coefficient_identities':6*checked,
            'other_retained_degrees':'zero by the fixed total of two feature slots in every selected shape'}


def main():
    base_path=ROOT/'results/actual-private-core-with-original-cubic.json'
    base=json.loads(base_path.read_text());assert base['schema']=='actual-private-core-with-original-cubic-v1'
    columns,shape_rows=columns_and_shapes();frames=[];summary={};separations=[];compiled=[]
    definitions=frame_definitions(columns,shape_rows)
    monomials={(row['corner_masks'][0],row['corner_masks'][1],tuple(row['terms'][0]['word']),tuple(row['terms'][0]['marks'])):i
               for i,row in enumerate(base['rows']) if len(row['terms'])==1 and row['terms'][0]['coefficient']=='1'}
    # These two readouts observe the whole terminal two-event ideal corner.
    assert (15,63,(4,5),(0,0)) in monomials and (15,63,(4,5),(1,0)) in monomials
    assert s.rank([s.record(15,w,m) for w in permutations((4,5)) for m in product((0,1),repeat=2)])==6
    full_monomials={(word,marks):index for (a,b,word,marks),index in monomials.items() if (a,b)==(0,63)}
    assert len(full_monomials)==270
    pivots=set()
    for column in columns:
        nonzero=[(index,column['source'].get(path,0)) for path,index in full_monomials.items()
                 if column['source'].get(path,0)]
        assert len(nonzero)==1 and nonzero[0][1]==1
        pivots.add(nonzero[0][0])
    assert len(pivots)==270
    original_row=base['rows'][base['seed_indices']['original_cubic']]
    original={(tuple(term['word']),tuple(term['marks'])):core.S.sympify(term['coefficient'],locals={'rho':core.r})
              for term in original_row['terms']}
    assert original==core.original_cubic_terms()
    old_hidden={(tuple(term['word']),tuple(term['marks'])):term['coefficient']
                for term in base['original_frame_identification']['hidden_source']}
    old_hidden={path:core.S.sympify(value) for path,value in old_hidden.items()}
    assert not s.rho_column(0,old_hidden) and all(path not in full_monomials for path in old_hidden)
    assert sum(original.get(path,0)*value for path,value in old_hidden.items())==1
    assert sum(row['corner_masks']==[0,63] for row in base['rows'])==271
    previous_support={(tuple(term['word']),tuple(term['marks'])) for row in base['rows']
                      if row['corner_masks']==[0,63] for term in row['terms']}
    for name,mode,blocks in definitions:
        frame,components=compile_frame(name,mode,blocks,columns)
        compiled.append(components)
        if name=='two_private':
            # Exact full-source equality, not merely equality on cubic products.
            assert all(len(component)==1 for component in components)
            for target,component in zip((0,18),components):
                pairs=columns[target]['pairs'];kinds=columns[target]['kinds']
                pivot=(tuple(e for pair in pairs for e in pair),tuple(m for kind in kinds for m in (kind,0)))
                assert component=={pivot:1}
            frame['full_source_identification']='S[0]*P_0 + S[1]*P_x, exactly on all source paths; redundant in the private core'
            comparison=[]
            for row_index,row in enumerate(frame['rows']):
                a,b=row['corner_masks']
                for term in row['terms']:
                    base_index=monomials[a,b,tuple(term['word']),tuple(term['marks'])]
                    for j,coefficient in enumerate(term['component_coefficients']):
                        if not coefficient:continue
                        assert coefficient==1
                        assert frame['denominators'][j]==[{'windows':term['windows'],'coefficient':1}]
                        comparison.append([row_index,base_index,'S['+str(j)+']'])
            frame['contextual_comparison_to_base']=comparison
        else:
            prefix,marks=(((0,1,3,2),(1,0,1,0)) if name=='sixteen_private' else ((0,1,2,3),(1,1,0,0)))
            positive=(prefix+(4,5),marks+(0,0));negative=(prefix+(5,4),marks+(0,0))
            source={positive:1,negative:-1}
            assert not s.rho_column(0,source)
            assert positive not in previous_support and negative not in previous_support
            responses=[evaluate_component(component,source) for component in components]
            expected=[{path_windows(positive):-2},{}] if name=='sixteen_private' else [{},{path_windows(positive):4}]
            assert responses==expected
            jet=s.record(0,prefix,marks)
            left_word=next(word for word,value in jet.items() if value==1)
            # The canonical tail cut 15->31 occurs only in the positive source term.
            assert vertices(0,positive[0])[4:6]==[15,31]
            separations.append({'added_frame':name,'previous_full_corner_support_size':len(previous_support),
                'source':[{'word':word,'marks':retained,'coefficient':coefficient} for (word,retained),coefficient in source.items()],
                'path_cost':2,'previous_observer_value':'0',
                'new_component_numerators':[polynomial_json(response) for response in responses],
                'nonzero_reason':'Exactly one nonzero component; its coefficient, S[j], the two positive window responses and the positive denominator are all nonzero.',
                'first_jet_witness':{'left_potential_word':left_word,'seam':['e',15,31,0],'right_potential_word':[],'coefficient':1},
                'source_filtration':'I but not I^2',
                'restriction_is_nonsplit':'The already fully observed terminal two-event ideal corner forces the forgotten-tail lift. Left multiplication by the displayed retained prefix is zero in the previous observer but nonzero in the enlarged observer.'})
        previous_support.update(set(components[0])|set(components[1]))
        summary[name]=frame['audit'];frames.append(frame)
    forward_audit=check_forward_all_paths(definitions,compiled)
    # A deliberately omitted memory path passes EVERY cubic-column test.
    # The independent full-source recorder must nevertheless reject it.
    hidden_path=((0,1,2,3,4,5),(1,1,0,0,0,0))
    assert compiled[2][1].get(hidden_path,0)!=0
    assert all(hidden_path not in column['source'] for column in columns)
    mutant=[[dict(component) for component in family] for family in compiled]
    del mutant[2][1][hidden_path]
    rejected=False
    try:check_forward_all_paths(definitions,mutant)
    except AssertionError:rejected=True
    assert rejected
    forward_audit['negative_control_top_invisible_memory_path_omission_rejected']=True
    matching_path=ROOT.parent/'grothendieck/results/exact-cubic-norming-rows.json'
    artifact={'schema':'actual-retained-cubic-observer-union-v1',
        'scope':'Full source-evaluation union of the exported core-plus-original and the three named IDEAL retained frames. Not the rounded numerical implementation protocol.',
        'base':{'path':str(base_path.relative_to(ROOT.parent.parent)).replace('\\','/'),
                'sha256':hashlib.sha256(base_path.read_bytes()).hexdigest(),'ambient_readouts':len(base['rows'])},
        'matching_sha256':hashlib.sha256(matching_path.read_bytes()).hexdigest(),
        'state_space':'IMAGE of the actual source ideal under the concatenated base and aggregate contextual rows. NOT the direct sum of their ambient coordinate spaces.',
        'source':{'events':[2,3,5,7,11,13],'background':2,'ideal':'kernel of the ordered potential-word terminal recorder; same source as base'},
        'fixed_analytical_semantics':{
            'y':3,'gamma_for_new_frame_tests':1,'h':'1/sqrt(8)','L':'xi_prime(7/2)/xi(7/2)',
            'R(a,b)':'sqrt(2)*h*X_[A(a),A(b)]*(mu_[A(a),A(b)]-L)',
            'N(a,b)':'sqrt(2)*X_[A(a),A(b)]*(C_even+h*(mu_[A(a),A(b)]-L))',
            'A(mask)':'2 times the product of the primes selected by mask',
            'window_relations':'R and N are additive interval functionals; W(a,b)=W(0,b)-W(0,a). Their actual X, mu, C_even and L are correlated fixed analytical values, not independent free window parameters.',
            'S':['(1-rho)*(1-sigma)','-rho'],
            'normalization':'All three ideal observers divided by the original positive late/late response, using the rho and sigma of the base artifact.',
            'analytic_assumptions':'The owning window positivity, simultaneous norming-test theorem and ideal calibrations. Numerical enclosures and implementation budgets are not rerun here.'},
        'frames':frames,'full_source_separations':separations,'exhaustive_forward_record_audit':forward_audit,
        'full_corner_dimensions':{'corner_masks':[0,63],'private_core':270,'with_original':271,
            'with_two_private':271,'with_sixteen_private':272,'with_matched_memory':273,
            'reason':'270 exact private pivots; the original and each subsequent separating ideal source add one independent full-corner scalar coordinate; two-private is redundant',
            'scope':'Full six-event corner only, not the total observer dimension or its whole filtration ranks'},
        'restriction_to_base':'retain base coordinates; source-compatible and surjective because both evaluations have the same source ideal',
        'restriction_to_O2':'compose restriction_to_base with the exported base projection to O2',
        'unlisted_prime_actions':'zero; vertex idempotents use the row corner masks; base and each aggregate contextual family use their listed actions',
        'filtration':'F^k = evaluation(I^(k+1)); F^3=0 by the six-event support and the two-event minimum ideal length. No numerical filtration dimensions or independent readout ranks are asserted.',
        'kernel_of_restriction_to_base':'evaluation_union(ker(evaluation_base:I->base)); imposed by the common source, not a free complement of the base coordinates',
        'coherence_status':'Actual frame assembly only. Minimal state/filtration ranks and the six comparisons, four face witnesses and tetrahedral filler are not certified here.',
        'audit':summary}
    out=ROOT/'results/actual-retained-cubic-observer-union.json'
    out.write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'artifact':str(out),'base_readouts':len(base['rows']),
                      'aggregate_seeds_added':3,'ambient_union_readouts':len(base['rows'])+sum(len(frame['rows']) for frame in frames),
                      'frames':summary,'exhaustive_forward_record_audit':forward_audit,
                      'nonsplit_steps':[item['added_frame'] for item in separations]},indent=2))


if __name__=='__main__':main()

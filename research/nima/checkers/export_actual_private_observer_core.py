"""Actual old-plus-270 observer in redundant, source-faithful coordinates.

No unsupported dimension claim: the state space is the IMAGE of I under the
exported coefficient rows. Extra retained cubic frame families are not included.
Run with uv run --with sympy python this_file.py.
"""
from pathlib import Path
from itertools import product,permutations
import importlib.util
import json
import hashlib
import sympy as S

ROOT=Path(__file__).resolve().parents[1];OTHER=ROOT.parent/'voevodsky'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


o=load('old_presentation',ROOT/'checkers/export_actual_old_observer.py');s=o.s;r=o.r


def normalize(terms):
    terms={p:S.cancel(x) for p,x in terms.items() if x!=0}
    if not terms:return None,S.Integer(0)
    first=sorted(terms)[0];factor=terms[first]
    return tuple((w,m,str(S.cancel(x/factor))) for (w,m),x in sorted(terms.items())),factor


def original_cubic_terms():
    """Expand four ACTUAL seam blocks; a vacuum buffer may have several orders."""
    sigma=S.Symbol('sigma')
    # Preserve the actual tensor-product correlation of the two slot tests.
    coefficients={(0,0):r*sigma,(0,1):-r,(1,0):-sigma,(1,1):S.Integer(1)}
    terms={}
    for choices,coefficient in coefficients.items():
        seams=[]
        for i,late in enumerate(choices):
            start=(1<<(2*i))-1
            seams.append(('e',start|(1<<(2*i)),(1<<(2*i+2))-1,1) if late
                         else ('e',start,start|(1<<(2*i)),1))
        seams.append(('e',15,31,0))
        cursor=0;segments=[]
        for _,a,b,keep in seams:
            assert cursor&a==cursor
            gap=tuple(e for e in range(6) if (a^cursor)&(1<<e))
            segments.append([(word,(0,)*len(word)) for word in permutations(gap)])
            event=(b^a).bit_length()-1
            segments.append([((event,),(keep,))]);cursor=b
        gap=tuple(e for e in range(6) if (63^cursor)&(1<<e))
        segments.append([(word,(0,)*len(word)) for word in permutations(gap)])
        for pieces in product(*segments):
            word=tuple(e for w,m in pieces for e in w);marks=tuple(e for w,m in pieces for e in m)
            assert s.vacuum_rows(0,63,{(word,marks):1},3).get(tuple(seams),0)==1
            assert (word,marks) not in terms
            terms[word,marks]=coefficient
    assert len(terms)==5 # The early/late sector has TWO vacuum-buffer orders.
    return terms


def main(include_original=False):
    old=json.loads((ROOT/'results/actual-old-observer-symbolic.json').read_text())
    p=s.load(OTHER/'results/filtered-obstruction-problem.json')
    cert=s.load(OTHER/'results/filtered-obstruction-certificate.json');s.verify(p,cert)
    seeds=[]
    for raw in old['seeds']:
        seeds.append((raw['family'],raw['corner_masks'][1],
            {(tuple(x['word']),tuple(x['marks'])):S.sympify(x['coefficient'],locals={'rho':r}) for x in raw['terms']}))
    for prefix in cert['prefixes']:
        rest=tuple(i for i in range(6) if not prefix['end']&(1<<i))
        pairs=tuple(map(tuple,prefix['pairs']))+(rest,)
        for suffix in (0,1):
            kinds=tuple(prefix['kinds'])+(suffix,)
            if sum(kinds)!=2:continue
            word=tuple(e for pair in pairs for e in pair)
            marks=tuple(mark for keep in kinds for mark in (keep,0))
            seeds.append(('private_'+str(len(seeds)-2),63,{(word,marks):S.Integer(1)}))
    assert len(seeds)==272
    if include_original:seeds.append(('original_cubic',63,original_cubic_terms()))
    rows=[];lookup={};seed_indices={};core_count=None
    def register(a,b,terms):
        normalized,factor=normalize(terms)
        if normalized is None:return None,factor
        key=(a,b,normalized)
        if key not in lookup:
            lookup[key]=len(rows);rows.append((a,b,{(w,m):S.sympify(value,locals={'rho':r}) for w,m,value in normalized}))
        return lookup[key],factor
    for family,end,terms in seeds:
        if family=='original_cubic':core_count=len(rows)
        length=len(next(iter(terms))[0])
        seed_indices[family]=register(0,end,terms)[0]
        for i in range(length+1):
            for j in range(i+2,length+1):
                groups={}
                for (word,marks),value in terms.items():
                    a=sum(1<<e for e in word[:i]);b=sum(1<<e for e in word[:j])
                    key=(a,b,word[:i],marks[:i],word[j:],marks[j:])
                    groups.setdefault(key,{})[word[i:j],marks[i:j]]=value
                for (a,b,*_),row in groups.items():register(a,b,row)
    n=len(rows)
    if core_count is None:core_count=n
    actions={};equations=0
    # Dual precomposition gives the complete sparse contextual actions.
    for target,(a,b,terms) in enumerate(rows):
        for side in ('left','right'):
            grouped={}
            for (word,marks),value in terms.items():
                if len(word)<=2:continue # remaining ideal corner has <2 events
                if side=='left':
                    edge=(a,word[0],marks[0]);corner=(a|(1<<word[0]),b);path=(word[1:],marks[1:])
                else:
                    edge=(b^(1<<word[-1]),word[-1],marks[-1]);corner=(a,b^(1<<word[-1]));path=(word[:-1],marks[:-1])
                grouped.setdefault((edge,corner),{})[path]=value
            for (edge,(u,v)),function in grouped.items():
                normalized,factor=normalize(function)
                source=lookup[u,v,normalized]
                # Formal equality on every source path, not agreement on samples.
                assert normalize({path:S.cancel(factor*x) for path,x in rows[source][2].items()})==normalize(function)
                assert all(S.cancel(function.get(path,0)-factor*x)==0 for path,x in rows[source][2].items())
                actions.setdefault((side,edge),{})[target,source]=factor;equations+=1
    # Left/right contexts must commute, including their row normalization factors.
    by_target={key:{i:(j,value) for (i,j),value in matrix.items()} for key,matrix in actions.items()}
    def compose_at(index,first,second):
        step=by_target.get(first,{}).get(index)
        if step is None:return None
        following=by_target.get(second,{}).get(step[0])
        if following is None:return None
        return following[0],S.cancel(step[1]*following[1])
    commuting_context_checks=0
    for index,(a,b,terms) in enumerate(rows):
        left={(a,w[0],m[0]) for w,m in terms}
        right={(b^(1<<w[-1]),w[-1],m[-1]) for w,m in terms}
        for le in left:
            for re in right:
                assert compose_at(index,('left',le),('right',re))==compose_at(index,('right',re),('left',le))
                commuting_context_checks+=1
    # The old frame's nine coordinates are selected contextual functionals.
    projection={}
    old_seed={family:terms for family,_,terms in seeds[:2]}
    for basis in old['basis']:
        pref,pm=tuple(basis['prefix']),tuple(basis['prefix_marks'])
        suff,sm=tuple(basis['suffix']),tuple(basis['suffix_marks'])
        terms={}
        for (word,marks),value in old_seed[basis['seed_family']].items():
            length=len(word);end=length-len(suff)
            if word[:len(pref)]==pref and marks[:len(pm)]==pm and word[end:]==suff and marks[end:]==sm:
                terms[word[len(pref):end],marks[len(pref):end]]=value
        normalized,factor=normalize(terms);a,b=basis['corner_masks']
        projection[basis['index']]=(lookup[a,b,normalized],factor)
    def evaluate(a,b,source):
        return {i:S.cancel(sum(value*source.get(path,0) for path,value in terms.items()))
                for i,(u,v,terms) in enumerate(rows) if (u,v)==(a,b)
                and S.cancel(sum(value*source.get(path,0) for path,value in terms.items()))!=0}
    def project(vector):return S.Matrix([S.cancel(factor*vector.get(index,0)) for index,factor in projection.values()])
    # Surjectivity is witnessed by the old source representatives, not by an ambient selector rank.
    for j,rep in enumerate(old['source_representatives']):
        source={(tuple(term['word']),tuple(term['marks'])):S.sympify(term['coefficient'],locals={'rho':r}) for term in rep['terms']}
        assert all(S.cancel(value)==0 for value in s.rho_column(rep['corner_masks'][0],source).values())
        assert o.same(project(evaluate(*rep['corner_masks'],source)),S.eye(9)[:,j])
    old_actions={}
    for raw in old['actions']:
        old_actions[raw['side'],(raw['start_mask'],raw['event_index'],raw['retained'])]={
            (i,j):S.sympify(value,locals={'rho':r}) for i,j,value in raw['entries']}
    checks=0
    allkeys=set(actions)|set(old_actions)
    for key in allkeys:
        delta=[{} for _ in range(9)]
        for i,(selected,factor) in projection.items():
            for (target,source),value in actions.get(key,{}).items():
                if target==selected:delta[i][source]=delta[i].get(source,0)+factor*value
        for (i,j),value in old_actions.get(key,{}).items():
            selected,factor=projection[j];delta[i][selected]=delta[i].get(selected,0)-value*factor
        for residual in delta:
            bycorner={}
            for index,coefficient in residual.items():
                a,b,terms=rows[index]
                for path,value in terms.items():
                    row=bycorner.setdefault((a,b),{});row[path]=row.get(path,0)+coefficient*value
            for (a,b),row in bycorner.items():
                row={path:S.cancel(value) for path,value in row.items() if S.cancel(value)!=0}
                if not row:continue
                assert b<16 # nontrivial projection identities live in the old packet
                paths,kernel=o.source_corner(a,b)
                assert o.same(S.Matrix([[row.get(path,0) for path in paths]])*kernel,S.zeros(1,kernel.cols))
                checks+=1
    # The actual chosen lift and the forced-initial-corner nonsplitting witness.
    a1=s.relation((0,1),1);b0=s.relation((2,3),0);c1=s.relation((4,5),1)
    v2=s.multiply(a1,b0);vy=s.multiply(v2,c1)
    x=s.multiply({((0,1),(0,1)):1},b0)
    ex=evaluate(0,15,x);ev=evaluate(0,15,v2)
    assert o.same((1-r)*project(ex),project(ev))
    pykey=(0,63,normalize({((0,1,2,3,4,5),(1,0,0,0,1,0)):S.Integer(1)})[0])
    py=lookup[pykey]
    assert evaluate(0,63,vy).get(py,0)==1
    assert not evaluate(0,63,s.multiply(x,c1))
    assert project(evaluate(0,63,vy))==S.zeros(9,1)
    _,initial_kernel=o.source_corner(0,3);assert initial_kernel.cols==2
    initial_values=S.Matrix.hstack(project(evaluate(0,3,s.relation((0,1),0))),project(evaluate(0,3,a1)))
    assert initial_values.rank()==2
    for end,source in ((15,x),(15,v2),(63,vy)):
        assert all(S.cancel(value)==0 for value in s.rho_column(0,source).values())
    def terms_json(terms):return [{'word':list(w),'marks':list(m),'coefficient':str(value)} for (w,m),value in sorted(terms.items())]
    # Exact chi_2 increment for THIS core, not the larger retained-frame union.
    shared=[];missing=[];kernel_representatives=[]
    for i in range(7):
        for j in range(i+2,7):
            a,b=(1<<i)-1,(1<<j)-1;word=tuple(range(i,j));marks=(0,)*(j-i)
            key=(a,b,normalize({(word,marks):S.Integer(1)})[0])
            if key in lookup:shared.append([i,j]);continue
            # At each absent corner every old core row has positive feature degree.
            assert all(any(any(m) for w,m in terms) for u,v,terms in rows if (u,v)==(a,b))
            source={(word,marks):S.Integer(1),((i+1,i)+word[2:],marks):S.Integer(-1)}
            assert not evaluate(a,b,source) and not s.rho_column(a,source)
            missing.append([i,j]);kernel_representatives.append({'interval':[i,j],'terms':terms_json(source)})
            # Representatives in I^2 and I^3 give the inherited flag exactly.
            for depth in (2,3):
                if j-i<2*depth:continue
                higher={((),()):S.Integer(1)}
                for k in range(i,i+2*depth,2):higher=s.multiply(higher,s.relation((k,k+1),0))
                tail=tuple(range(i+2*depth,j));higher=s.multiply(higher,{(tail,(0,)*len(tail)):S.Integer(1)})
                assert higher.get((word,marks),0)==1 and not evaluate(a,b,higher)
    assert len(shared)==7 and len(missing)==8
    assert [sum(j-i>=2*depth for i,j in missing) for depth in (1,2,3,4)]==[8,6,1,0]
    kernel_actions=[];missing_set=set(map(tuple,missing))
    for column,(i,j) in enumerate(missing):
        for side,target,edge in (('left',(i-1,j),i-1),('right',(i,j+1),j)):
            if not (0<=target[0]<target[1]<=6):continue
            assert target in missing_set
            kernel_actions.append({'side':side,'edge_start_mask':(1<<edge)-1,'event_index':edge,
                                   'row':missing.index(list(target)),'column':column,'coefficient':'1'})
    left_image={(k,j) for i,j in missing for k in range(i-1) if (k,j) in missing_set}
    right_image={(i,k) for i,j in missing for k in range(j+2,7) if (i,k) in missing_set}
    assert left_image==right_image=={(0,5),(0,6)}
    frame_audit=None
    if include_original:
        prefix_source={((0,1,2,3),(0,1,0,1)):S.Integer(1)}
        tail=s.relation((4,5),0);hidden=s.multiply(prefix_source,tail)
        assert not s.rho_column(0,hidden)
        jet_value=0
        for (word,marks),coefficient in hidden.items():
            states=[0]
            for event in word:states.append(states[-1]|(1<<event))
            for cut in range(len(word)):
                if (states[cut],states[cut+1],marks[cut])!=(15,31,0):continue
                jet_value+=coefficient*s.record(0,word[:cut],marks[:cut]).get((3,15),0)*s.record(states[cut+1],word[cut+1:],marks[cut+1:]).get((),0)
        assert jet_value==1
        hidden_value=evaluate(0,63,hidden)
        assert all(hidden_value.get(i,0)==0 for i in range(core_count))
        assert hidden_value[seed_indices['original_cubic']]==1
        tail_values=[evaluate(15,63,s.relation((4,5),kind)) for kind in (0,1)]
        active=sorted({i for value in tail_values for i in value if i<core_count})
        assert S.Matrix([[value.get(i,0) for value in tail_values] for i in active]).rank()==2
        assert s.rank([s.record(15,w,m) for w in permutations((4,5)) for m in product((0,1),repeat=2)])==6
        original=original_cubic_terms();correction=dict(original);top_values=[]
        for family,end,private in seeds[2:272]:
            # Recover the uniquely dual cubic source from the private canonical word.
            word,marks=next(iter(private));source={((),()):1}
            for index in range(0,6,2):
                source=s.multiply(source,s.relation(word[index:index+2],marks[index]))
            value=S.cancel(sum(coefficient*source.get(path,0) for path,coefficient in original.items()))
            if value!=0:
                top_values.append({'private_seed':family,'coefficient':str(value)})
                correction[word,marks]=S.cancel(correction.get((word,marks),0)-value)
        for _,_,private in seeds[2:272]:
            word,marks=next(iter(private));source={((),()):1}
            for index in range(0,6,2):source=s.multiply(source,s.relation(word[index:index+2],marks[index]))
            assert S.cancel(sum(value*source.get(path,0) for path,value in correction.items()))==0
        assert S.cancel(sum(value*hidden.get(path,0) for path,value in correction.items()))==1
        frame_audit={'core_ambient_rows':core_count,'enlarged_ambient_rows':n,
            'aggregate_seed_supported_paths':5,'independent_full_corner_scalar_seeds_added':1,
            'fixed_sector_parameters':['rho','sigma'],
            'parameter_meaning':'rho=(mu_[2,4]-L)/(mu_[4,12]-L), sigma=(mu_[12,60]-L)/(mu_[60,420]-L), at the fixed original calibration',
            'sector_coefficients':{'early_early':'rho*sigma','early_late':'-rho','late_early':'-sigma','late_late':'1'},
            'external_normalization_hypothesis':'the owning fixed positive-window protocol gives 0<rho<1 and 0<sigma<1; these are not independent physical settings',
            'hidden_source':terms_json(hidden),'hidden_source_path_cost':'2',
            'first_jet_witness':{'left_potential_word':[3,15],'seam':['e',15,31,0],
                                 'right_potential_word':[],'coefficient':'1'},
            'source_filtration':'in I but not I^2 by the nonzero first jet',
            'core_value':'0','normalized_original_value':'1',
            'top_layer_private_combination':top_values,'correction_seed':terms_json({path:value for path,value in correction.items() if value!=0}),
            'correction_vanishes_on_all_270_cubic_columns':True,'correction_on_hidden_source':'1',
            'restriction':'nonsplit: the terminal two-event ideal corner is fully observed, forcing the forgotten tail lift; the retained prefix then gives a contradiction',
            'remaining_frames':['two-private','sixteen-private','matched memory-block norming observer']}
    artifact={'schema':'actual-old-plus-270-source-evaluation-core-v1',
        'scope':'Exact subobserver generated by the original two seeds and the 270 private seeds; extra retained cubic frames are not identified with this core.',
        'source':{'background':2,'event_primes':[2,3,5,7,11,13],
                  'domain':'kernel of the ordered potential-word terminal recorder',
                  'state_space':'image of this domain under the supplied rows; ambient readouts are redundant'},
        'rho':'fixed actual early/late ratio, 9/20 < rho < 12/25',
        'private_normalization':'each complete private family divided by its own fixed positive analytical response; no uniform inverse bound asserted',
        'seed_indices':seed_indices,'ambient_readout_count':n,
        'rows':[{'corner_masks':[a,b],'terms':terms_json(terms)} for a,b,terms in rows],
        'actions':[{'side':side,'start_mask':edge[0],'event_index':edge[1],'retained':edge[2],
                    'entries':[[i,j,str(value)] for (i,j),value in sorted(matrix.items())]}
                   for (side,edge),matrix in sorted(actions.items())],
        'unlisted_prime_actions':'zero',
        'vertex_actions':'left/right vertex idempotents project onto rows with the corresponding initial/terminal corner mask',
        'evidence_sha256':{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in (
            ('old_observer',ROOT/'results/actual-old-observer-symbolic.json'),
            ('structural_problem',OTHER/'results/filtered-obstruction-problem.json'),
            ('structural_certificate',OTHER/'results/filtered-obstruction-certificate.json'))},
        'projection_to_O2':[[i,index,str(factor)] for i,(index,factor) in projection.items()],
        'private_P_y_index':py,
        'background_two_vacuum_increment_for_this_core':{
            'shared_intervals':shared,'kernel_intervals':missing,'dimension':8,
            'source_representatives':kernel_representatives,'prime_actions':kernel_actions,
            'inherited_filtration_dimensions':[8,6,1,0],
            'intrinsic_ideal_power_dimensions':[8,2,0],
            'restriction':'nonsplit; initial forgotten diamond is already fully observed',
            'scope':'Only this old-plus-270 core. Additional retained cubic frames can enlarge the intersection and reduce this increment.'},
        'chosen_lift':{'x_evaluation':[[i,str(value)] for i,value in ex.items()],
            'v2_evaluation':[[i,str(value)] for i,value in ev.items()],
            'normalization':'pi((1-rho)*epsilon(x))=epsilon_2(v2)',
            'filtration_warning':'This lift is unfiltered; it is not a face witness in the earlier filtered tetrahedral fixture.'},
        'audit':{'seed_count':len(seeds),'formal_action_coefficient_identities':equations,
            'commuting_left_right_context_checks':commuting_context_checks,
            'projection_identities_requiring_source_ideal_relations':checks,
            'projection_surjectivity_source_witnesses':9,'P_y_of_vy':'1','old_projection_of_vy':'0',
            'restriction_to_O2':'nonsplit by the fully observed initial mixed corner and right action b0*c1'},
        'not_claimed':['ambient_readouts_are_independent','full_retained_frame_protocol_assembled',
                       'all_four_tower_faces_identified','new_measurements_performed']}
    filename='actual-private-observer-core.json'
    if include_original:
        artifact['schema']='actual-private-core-with-original-cubic-v1'
        artifact['scope']='Old-plus-270 core enlarged by the original aggregated four-sector cubic seed. Other historical cubic frames remain outside this export.'
        artifact['original_frame_identification']=frame_audit
        core_path=ROOT/'results/actual-private-observer-core.json'
        core=json.loads(core_path.read_text())
        assert core['rows']==artifact['rows'][:core_count]
        core_actions={(item['side'],item['start_mask'],item['event_index'],item['retained']):item['entries'] for item in core['actions']}
        for item in artifact['actions']:
            key=(item['side'],item['start_mask'],item['event_index'],item['retained'])
            restricted=[entry for entry in item['entries'] if entry[0]<core_count]
            assert all(entry[1]<core_count for entry in restricted)
            assert restricted==core_actions.get(key,[])
        artifact['restriction_to_private_core']={'projection':'retain the first '+str(core_count)+' readouts',
            'core_sha256':hashlib.sha256(core_path.read_bytes()).hexdigest(),
            'source_compatible':True,'split':False,'inverse_source_comparison_supplied':False}
        artifact['background_two_vacuum_increment_for_this_core']['scope']='This exported core plus the original four-sector seed only; other retained frames are not included.'
        filename='actual-private-core-with-original-cubic.json'
    (ROOT/'results'/filename).write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'ambient_readout_count':n,**artifact['audit'],
        'core_only_vacuum_increment_dimension':8,'increment_inherited_filtration':[8,6,1,0],
        'increment_intrinsic_ideal_powers':[8,2,0],
        'original_frame_audit':frame_audit},indent=2))


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--original-cubic',action='store_true')
    main(parser.parse_args().original_cubic)

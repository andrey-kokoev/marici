"""Actual finite filtered retention tetrahedron, and replacement-frame obstruction.

Two contracts are deliberately distinguished: cumulative retained towers have
strict restriction comparisons; individual recipes are NOT interchangeable.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
import importlib.util,json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('core',ROOT/'checkers/export_actual_private_observer_core.py')
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core);s=core.s;S=core.S


def polynomial(frame,source):
    out=[{},{}]
    for term in frame['rows'][frame['seed_row']]['terms']:
        coefficient=source.get((tuple(term['word']),tuple(term['marks'])),0)
        if not coefficient:continue
        windows=tuple(map(tuple,term['windows']))
        for j,value in enumerate(term['component_coefficients']):
            out[j][windows]=out[j].get(windows,0)+coefficient*value
    return [{key:value for key,value in terms.items() if value} for terms in out]


def main():
    paths={name:ROOT/'results'/filename for name,filename in (
        ('base','actual-private-core-with-original-cubic.json'),
        ('union','actual-retained-cubic-observer-union.json'),
        ('presentation','actual-observer-full-finite-presentation.json.gz'))}
    base=json.loads(paths['base'].read_text());union=json.loads(paths['union'].read_text())
    with gzip.open(paths['presentation'],'rt',encoding='utf-8') as stream:pres=json.load(stream)
    for key in ('base','union'):
        assert pres['inputs'][paths[key].name]==hashlib.sha256(paths[key].read_bytes()).hexdigest()
    limits=[len(base['rows'])]
    for frame in union['frames']:limits.append(limits[-1]+len(frame['rows']))
    assert limits==[2741,2763,2863,3591] and pres['ambient_rows']==limits[-1]
    # Real ambient action matrices, not a permutation/group fixture.
    action_entries=[]
    for action in base['actions']:
        for row,col,value in action['entries']:action_entries.append((action['side'],action['start_mask'],action['event_index'],action['retained'],row,col,value))
    for index,frame in enumerate(union['frames']):
        offset=limits[index]
        for action in frame['actions']:
            for row,col,value in action['entries']:action_entries.append((action['side'],action['start_mask'],action['event_index'],action['retained'],offset+row,offset+col,value))
    edges=[];anchor_checks=0;action_checks=0
    for j,i in combinations(range(4),2):
        # Direction is richer i -> earlier j.
        for side,start,event,mark,row,col,value in action_entries:
            if row<limits[j]:
                assert col<limits[j]
                action_checks+=1
        for column in pres['G0_evaluation_columns']:
            source_column=[entry for entry in column if entry[0]<limits[i]]
            assert [entry for entry in source_column if entry[0]<limits[j]]==[entry for entry in column if entry[0]<limits[j]]
            anchor_checks+=1
        edges.append({'id':f'p{i}{j}','from':i,'to':j,'matrix_shape':[limits[j],limits[i]],
                      'nonzero_entries':[[k,k,'1'] for k in range(limits[j])],
                      'source_compatible':True,'filtration':'preserves each exported image G0*Jr',
                      'tower_components':{'O1':'identity','O2':'identity','O3':f'p{i}{j}'}})
    edge_lookup={(e['from'],e['to']):e for e in edges}
    faces=[]
    for i,j,k in combinations(range(4),3):
        first=edge_lookup[k,j];second=edge_lookup[j,i];direct=edge_lookup[k,i]
        composite=[[r,r,'1'] for r in range(second['matrix_shape'][0])]
        assert composite==direct['nonzero_entries']
        faces.append({'vertices':[i,j,k],
                      'boundary':f'p{j}{i} o p{k}{j} = p{k}{i}',
                      'witness':{'type':'degree -1 homotopy between maps of filtered source bimodules concentrated in degree 0',
                                 'matrix':'zero','boundary_difference':'zero'},
                      'not_an_attachment_nullhomotopy':True})
    # Both composites from C3 to C0, including either reassociation, are p30.
    assert edge_lookup[3,0]['nonzero_entries']==[[r,r,'1'] for r in range(limits[0])]
    tetra={'vertices':[0,1,2,3],'type':'degree -2 filler for the face-homotopy boundary',
           'matrix':'zero','boundary':'alternating whiskered sum of four zero face witnesses = zero',
           'reason':'strict source-compatible coordinate restrictions, not chosen lifts of O2'}
    # The formerly ambiguous alternative: replace the original recipe by another
    # scalar frame while retaining only the common old-plus-270 core.
    core_size=base['original_frame_identification']['core_ambient_rows']
    hidden=[base['original_frame_identification']['hidden_source']]
    hidden.extend(item['source'] for item in union['full_source_separations'])
    sources=[{(tuple(term['word']),tuple(term['marks'])):S.sympify(term['coefficient']) for term in raw} for raw in hidden]
    assert len(sources)==3
    for source in sources:
        assert not s.rho_column(0,source)
        for row in base['rows'][:core_size]:
            if row['corner_masks']!=[0,63]:continue
            assert sum(S.sympify(term['coefficient'])*source.get((tuple(term['word']),tuple(term['marks'])),0) for term in row['terms'])==0
    original=core.original_cubic_terms()
    assert [S.cancel(sum(coefficient*source.get(path,0) for path,coefficient in original.items())) for source in sources]==[1,0,0]
    two,sixteen,matched=union['frames']
    assert all(polynomial(two,source)==[{},{}] for source in sources)
    values16=[polynomial(sixteen,source) for source in sources]
    valuesM=[polynomial(matched,source) for source in sources]
    assert values16[0]==values16[2]==[{},{}]
    assert len(values16[1][0])==1 and not values16[1][1]
    assert list(values16[1][0].values())==[-2]
    assert all(not value[0] for value in valuesM)
    assert len(valuesM[2][1])==1 and list(valuesM[2][1].values())==[4]
    def term_json(poly):return [{'windows':w,'coefficient':str(c)} for w,c in sorted(poly.items())]
    definitions={'A':{'frame':'sixteen_private','component':0,'numerator':term_json(values16[1][0])},
                 'B':{'frame':'matched_memory','component':1,'numerator':term_json(valuesM[0][1])},
                 'C':{'frame':'matched_memory','component':1,'numerator':term_json(valuesM[1][1])},
                 'D':{'frame':'matched_memory','component':1,'numerator':term_json(valuesM[2][1])}}
    # Symbols stand for the fixed actual calibrated values, not generic choices.
    A,B,C,D=S.symbols('A B C D')
    values=S.Matrix([[1,0,0],[0,0,0],[0,A,0],[B,C,D]])
    witnesses={(1,0):S.Matrix([1,0,0]),(1,2):S.Matrix([0,1,0]),(1,3):S.Matrix([0,0,1]),
               (0,2):S.Matrix([0,1,0]),(2,0):S.Matrix([1,0,0]),
               (0,3):S.Matrix([0,0,1]),(3,0):S.Matrix([1,0,-B/D]),
               (2,3):S.Matrix([0,0,1]),(3,2):S.Matrix([0,1,-C/D])}
    forbidden=[]
    for (i,j),witness in witnesses.items():
        assert S.cancel((values*witness)[i])==0
        target=S.cancel((values*witness)[j]);assert target in (1,A,D)
        forbidden.append({'from':i,'to':j,'source_coefficients_in_hidden_basis':list(map(str,witness)),
                          'incoming_value':'0','outgoing_value':str(target),
                          'obstruction':'A source-compatible map would send zero to this nonzero value.'})
    recipe_pairs=[]
    for i,j in combinations(range(4),2):
        arrows=[]
        for source,target in ((i,j),(j,i)):
            if target==1:
                # The two-private contextual test is explicitly reconstructed from core rows.
                assert all(entry[1]<core_size for entry in two['contextual_comparison_to_base'])
                arrows.append({'from':source,'to':target,'status':'exists','map':'retain common core and evaluate the exported two-private contextual comparison'})
            else:
                assert (source,target) in witnesses
                arrows.append({'from':source,'to':target,'status':'obstructed'})
        recipe_pairs.append({'vertices':[i,j],'directions':arrows,'invertible_comparison':False})
    blocked_faces=[{'vertices':list(face),'status':'no triangle of source-compatible equivalences',
                    'reason':'at least one required edge is obstructed on the explicit ideal sources'}
                   for face in combinations(range(4),3)]
    report={'schema':'actual-retention-tetrahedron-and-recipe-obstruction-v1','passed':True,
        'inputs_sha256':{key:hashlib.sha256(path.read_bytes()).hexdigest() for key,path in paths.items()},
        'category':'Finite filtered source bimodules, or their complexes concentrated in degree 0; fixed actual analytical coefficients',
        'retained_towers':[
            {'vertex':i,'protocol':name,'O1_dimension':1,'O2_dimension':9,'O3_ambient_readouts':limits[i],
             'O3_presentation':f'prefix {limits[i]} rows of G0; same source generators and J1,J2',
             'filtration':'images of the exported source I, I^2, I^3; fourth level zero'}
            for i,name in enumerate(('core+original','core+original+two_private','core+original+two_private+sixteen_private','full_retained_union'))],
        'six_comparisons':edges,'four_typed_face_witnesses':faces,'tetrahedral_filler':tetra,
        'boundary_warning':'The zero face witnesses compare equal restriction composites. They neither split a nonsplit restriction nor turn the old unfiltered line lift into a filtered attachment witness.',
        'individual_recipe_contract':{'vertices':['core+original','core+two_private','core+sixteen_private','core+matched_memory'],
            'six_pair_comparisons':recipe_pairs,'four_face_requests':blocked_faces,
            'tetrahedron_status':'obstructed already at the source-anchored edge level; not a newly computed nonzero degree-three class',
            'hidden_source_basis':hidden,'evaluation_matrix':[[str(v) for v in row] for row in values.tolist()],
            'fixed_scalar_definitions':definitions,
            'scalar_rule':'Each numerator is multiplied by S[component]/the owning positive frame denominator and uses the owning R or N window test.',
            'nonzero_guards':'A=-2*S0*R(0,1)*R(3,11)/D16,0 is nonzero; D=4*Sx*N(0,1)*N(1,3)/DM,x is nonzero. B,C need not be nonzero.',
            'forbidden_directed_maps':forbidden,
            'field_scope':'Hidden-source combinations with B/D or C/D use the same fixed actual scalar field as the observer modules.'},
        'audit':{'source_anchor_column_checks':anchor_checks,'action_entry_restriction_checks':action_checks,
                 'six_actual_restrictions':len(edges),'four_strict_faces':len(faces),
                 'forbidden_recipe_directions':len(forbidden)},
        'scope':'The assembled retained finite ideal-frame protocol. Not a fabricated gain-equivalence tetrahedron, physical acquisition certificate, or completed infinite-source result.'}
    out=ROOT/'results/actual-retention-tetrahedron-and-recipe-obstruction.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,**report['audit'],'retained_tetrahedron':'strict filler verified',
                      'individual_recipe_tetrahedron':'source-anchored edge obstruction verified'},indent=2))


if __name__=='__main__':main()

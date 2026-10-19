"""Instantiate source provenance and check a retained Bool operation map, read-only on sources."""
import argparse
import copy
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-source-register.v1.json'
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
import pilot_carrier as P


def require(ok,why):
    if not ok: raise ValueError(why)


def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def sha(path):return sha256((ROOT/path).read_bytes()).hexdigest()


def source_paths(c):
    return {CONTRACT,c['interface']}|{p for s in c['sources'] for p in s['evidence']}|{
        r[4] for r in c['ingredient_specs']}|{p for d in c['derivations'].values() for p in d['evidence']}|{
        x['evidence'] for x in c['comparisons']}


def validate(c,pins):
    interface=load(c['interface']); source_contract=interface['source_record_contract']
    require(c['common_carrier_id'] is None and c['common_physical_witness_constructed'] is False
            and c['shared_witness_records']==[],'unconstructed common witness promoted')
    sources={s['id']:s for s in c['sources']}
    require(len(sources)==len(c['sources']),'duplicate source ID')
    require({'native-bool-square-pilot','conditional-six-port-retained-exchange',
             'marked137.T9.exact-domain.v1','scattering.native-pair-orbital.v1'}<=sources.keys(),'missing primary source')
    reviewed=load('research/nima/contracts/physics-control-contribution-review.v1.json')
    require({p['source_id'] for p in reviewed['ports']}<=sources.keys(),'lost reviewed control source')
    fields=('version','source_object','operations','composition','identity_policy','geometry','dynamics',
            'observer','ingredient_records','missing_comparison_ports','evidence')
    for s in sources.values():require(all(s.get(k) for k in fields),'incomplete source interface')
    require(set(pins['source_sha256'])==source_paths(c),'source pin coverage')
    for path,digest in pins['source_sha256'].items():
        require((ROOT/path).resolve().is_relative_to(ROOT) and sha(path)==digest,'source drift: '+path)
    specs={r[0]:r for r in c['ingredient_specs']}
    require(len(specs)==len(c['ingredient_specs']),'duplicate ingredient')
    records=[]
    for rid,sid,role,ingredient,path in c['ingredient_specs']:
        require(sid in sources and role in source_contract['roles'],'untyped ingredient')
        require(role not in ('measured_calibration','fitting_input','held_out_test'),'model input promoted to observations')
        s=sources[sid]
        r=dict(c['record_defaults'],id=rid,source_object=sid,ingredient=ingredient,role=role,
               origin={'source_path_or_external_reference':path,'integrity_or_version':'sha256:'+sha(path),
                       'verification_level':'reviewed source specification/result; independent Bool adapter check where stated'},
               scope=s['source_object']+'; '+s['version'])
        require(r['target_id']=='unselected','register silently selected target')
        require(all(r.get(k) for k in source_contract['required_fields']),'incomplete source record')
        require(all(r['origin'].get(k) for k in source_contract['origin_required_fields']),'incomplete origin')
        if role=='derived_source_data':
            d=c['derivations'].get(rid,{})
            require(d.get('operation') and d.get('evidence') and (d.get('premises') or d.get('supplied_premise')),'unsourced derivation')
            require(set(d.get('premises',[]))<=specs.keys(),'unknown derivation premise')
            r['derivation']=d
        records.append(r)
    require({r['id'] for r in records if r['role']=='derived_source_data'}==set(c['derivations']),'derivation coverage')
    for sid,s in sources.items():
        require(set(s['ingredient_records'])=={r[0] for r in specs.values() if r[1]==sid},'ingredient attachment')
    def visit(key,active):
        require(key not in active,'cyclic ingredient provenance')
        for dep in c['derivations'].get(key,{}).get('premises',[]):visit(dep,active|{key})
    for key in specs:visit(key,set())
    views={v['id']:v for v in c['views']}
    require(len(views)==len(c['views']) and not views.keys()&sources.keys(),'view identity collision')
    require(all(v['source_instance_id'] in sources for v in views.values()),'unknown view source')
    require(len({m['id'] for m in c['maps']})==len(c['maps']),'duplicate map')
    for m in c['maps']:
        require(m['source'] in sources and m['target'] in views,'unknown map endpoint')
        require(views[m['target']]['source_instance_id']==m['source'],'cross-source identity without comparison')
        require(m['status'] in ('constructed_exact_adapter','reviewed_source_result'),'map evidence strength')
        require(all(m.get(k) for k in ('embedding_or_interpretation','preserved_operations','preserved_records',
                                      'observable_transport','residuals')),'incomplete typed map')
    comparisons={x['id']:x for x in c['comparisons']}
    require(len(comparisons)==len(c['comparisons']),'duplicate comparison')
    expected={'bool-exchange':'bounded_obstruction','native-pair-marked':'bounded_obstruction',
              'exact-reader-optical':'versioned_event_change','wg-marked-attachment':'missing_map',
              'scattering-branches':'missing_map','optical-instruments':'missing_map'}
    require({k:v['status'] for k,v in comparisons.items()}==expected,'comparison residual or event version lost')
    for x in comparisons.values():
        require(len(set(x['sources']))==len(x['sources']) and set(x['sources'])<=sources.keys(),'invalid comparison sources')
        require(x['reopening'] and (x['status']=='missing_map' or x['witness']),'unactionable residual')
    bindings=[]
    for sid,s in sources.items():
        maps=[m for m in c['maps'] if m['source']==sid]
        b={'common_carrier_id':None,'source_instance_id':sid,'embedding_or_interpretation':None,
           'preserved_operations':s['operations'],'preserved_records':s['identity_policy'],
           'overlap_maps':[],'observable_transport':s['observer'],'residuals':s['missing_comparison_ports'],
           'same_source_presentation_maps':[m['id'] for m in maps],'status':'candidate_binding_slots_only'}
        require(set(interface['shared_witness_contract']['required_fields'])<=b.keys(),'missing shared-witness slot')
        bindings.append(b)
    return records,bindings


I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
L=((0,0,1,0),(0,0,0,1),(1,0,0,0),(0,1,0,0))
R=((0,1,0,0),(1,0,0,0),(0,0,0,1),(0,0,1,0))
M={P.Operation.LEFT:L,P.Operation.RIGHT:R}
SID='native-bool-square-pilot'

def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))
def mv(a,x):return tuple(sum(row[k]*x[k] for k in range(4)) for row in a)

def word_matrix(word):
    a=I
    for op in word:a=mm(M[op],a)
    return a


def encode(p):
    return {'source_id':SID,'source':p.source,'word':p.operations,'matrix':word_matrix(p.operations),
            'trace':tuple(P.basis(s) for s in p.trace)}


def decode(r):
    require(r['source_id']==SID,'foreign source tag')
    p=P.PathRecord(r['source'],r['word'])
    require(encode(p)==r,'corrupt retained image')
    return p


def compose(a,b):
    # Image composition is partial and retains the word, not just the product matrix.
    p,q=decode(a),decode(b)
    require(p.target==q.source,'source attachment mismatch')
    return {'source_id':SID,'source':p.source,'word':a['word']+b['word'],
            'matrix':mm(b['matrix'],a['matrix']),'trace':a['trace']+b['trace'][1:]}


def algebra():
    counts={'primitive_squares':0,'word_squares':0,'composition_splits':0}
    for op in M:
        require(M[op]==P.native_permutation(op),'native matrix mismatch')
        require(mm(M[op],M[op])==I,'native involution')
        for s in P.LABELS:
            require(mv(M[op],P.basis(s))==P.basis(P.apply(op,s)),'primitive action square')
            counts['primitive_squares']+=1
    for n in range(7):
        for word in itertools.product(tuple(M),repeat=n):
            for s in P.LABELS:
                p=P.PathRecord(s,word);image=encode(p)
                require(decode(image)==p and mv(image['matrix'],P.basis(s))==P.basis(p.target),'word square/inverse')
                counts['word_squares']+=1
                for k in range(n+1):
                    a=P.PathRecord(s,word[:k]);b=P.PathRecord(a.target,word[k:])
                    require(compose(encode(a),encode(b))==encode(a.then(b))==image,'composition square')
                    counts['composition_splits']+=1
    s=(False,False);left,right=P.Operation.LEFT,P.Operation.RIGHT
    lr=P.PathRecord(s,(left,right));rl=P.PathRecord(s,(right,left))
    require(lr.target==rl.target and word_matrix(lr.operations)==word_matrix(rl.operations),'collision premise')
    require(encode(lr)!=encode(rl),'schedule erased')
    empty=P.PathRecord(s,());double=P.PathRecord(s,(left,left))
    require(encode(empty)['matrix']==encode(double)['matrix'] and encode(empty)!=encode(double),'identity trace erased')
    occurrences=(P.Occurrence('first',lr),P.Occurrence('second',lr))
    families=P.promote(occurrences,'target','physics-register-test-v1')
    require(len(families)==1 and families[0].members==occurrences,'occurrence multiplicity erased')
    rejected=[]
    bad=encode(lr);bad['source_id']='conditional-six-port-retained-exchange'
    corrupt=encode(lr);corrupt['trace']=corrupt['trace'][:-1]
    for name,action in (
        ('mixed-source-word',lambda:compose(encode(empty),bad)),
        ('corrupt-image-trace',lambda:decode(corrupt)),
        ('mismatched-attachment',lambda:compose(encode(lr),encode(empty))),
        ('duplicate-occurrence',lambda:P.promote((occurrences[0],occurrences[0]),'target','bad'))):
        try:action()
        except ValueError:rejected.append(name)
        else:raise AssertionError('hostile admitted: '+name)
    return dict(counts,maximum_test_word_length=6,retained_schedule_collision=True,
                retained_identity_collision=True,occurrence_multiplicity=True,rejected_hostiles=rejected,
                all_finite_words_argument='Primitive basis squares extend linearly; matrix composition and retained concatenation give induction on word length.')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT);pinpath=ROOT/c['source_pins']
    if args.pin:
        require(not pinpath.exists(),'refusing implicit re-pin')
        pinpath.write_text(json.dumps({'schema':'marici.physics-source-register.pins.v1',
            'source_sha256':{p:sha(p) for p in sorted(source_paths(c))}},indent=2)+'\n',encoding='utf-8')
    pins=load(c['source_pins']);records,bindings=validate(c,pins);controls=algebra()
    rejected=[]
    for name in ('duplicate-source','missing-operations','false-common-witness','foreign-view','mixed-source-map',
                 'fixture-as-measurement','missing-derivation','cyclic-derivation','promoted-obstruction','collapsed-event-version','stale-pin'):
        b=copy.deepcopy(c);p=copy.deepcopy(pins)
        if name=='duplicate-source':b['sources'].append(b['sources'][0])
        elif name=='missing-operations':b['sources'][0]['operations']=''
        elif name=='false-common-witness':b['common_physical_witness_constructed']=True
        elif name=='foreign-view':b['views'][0]['source_instance_id']='unknown'
        elif name=='mixed-source-map':b['maps'][0]['source']='conditional-six-port-retained-exchange'
        elif name=='fixture-as-measurement':b['ingredient_specs'][0][2]='measured_calibration'
        elif name=='missing-derivation':del b['derivations']['bool-linear']
        elif name=='cyclic-derivation':b['derivations']['bool-linear']['premises']=['bool-linear']
        elif name=='promoted-obstruction':b['comparisons'][0]['status']='constructed'
        elif name=='collapsed-event-version':b['comparisons'][2]['status']='identity'
        else:p['source_sha256'][next(iter(p['source_sha256']))]='0'*64
        try:validate(b,p)
        except ValueError:rejected.append(name)
        else:raise AssertionError('corrupt register accepted: '+name)
    out={'schema':'marici.physics-source-register.result.v1','status':'pass','source_count':len(c['sources']),
         'source_records':records,'candidate_bindings':bindings,'maps':c['maps'],'comparisons':c['comparisons'],
         'independent_bool_adapter':controls,'rejected_corruptions':rejected,'common_physical_witness_constructed':False,
         'source_pin_count':len(pins['source_sha256']),'pins_sha256':sha(c['source_pins']),
         'contract_sha256':sha(CONTRACT),'checker_sha256':sha(Path(__file__)),
         'verification':'Independent exact Bool adapter and register validation; other source results imported at their stated review strength; no owner suites or compiler rerun.'}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','sources':len(c['sources']),'ingredient_records':len(records),
        'presentation_maps':len(c['maps']),'source_pins':out['source_pin_count'],
        'bool_adapter':controls,'rejected_corruptions':rejected,'common_physical_witness_constructed':False},indent=2))

if __name__=='__main__':main()

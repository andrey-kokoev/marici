"""Finite wire-format controls; general/higher proofs are source-bound Agda.
Native interpretation never decodes a legacy AST to evaluate its row schema.
"""
from pathlib import Path
from itertools import product,permutations
from functools import lru_cache
from copy import deepcopy
import hashlib,json,random
BASE=Path(__file__).resolve().parents[1]
ATOMS={'Empty':(), 'Unit':((),), 'Bool':(False,True)}
DECL=('declaration',); ROOT='root'; RNG=random.Random(8812)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def reject(f):
    try:f()
    except (ValueError,KeyError):return
    raise AssertionError('invalid rows accepted')
def entries(rows):
    result={}
    for label,source,target in rows:
        if source!=ROOT or target in result:raise ValueError('bad/duplicate endpoint')
        result[target]=label
    return result
@lru_cache(None)
def old_values(c):
    k=c[0]
    if k=='atom':return ATOMS[c[1]]
    if k in ('E','Pi'):
        _,domain,children=c
        if k=='E':return tuple((i,x) for i,g in zip(domain,children) for x in old_values(g))
        return tuple(product(*(old_values(g) for g in children)))
    if k=='paths':return ((),) if c[2]==c[3] else ()
    if k=='maps':return tuple(product(old_values(c[2]),repeat=len(old_values(c[1]))))
    if k=='equivalences':
        a,b=old_values(c[1]),old_values(c[2])
        return tuple(permutations(b)) if len(a)==len(b) else ()
    if k=='retain':return old_values(c[3])
    if k=='comparison':return tuple((x,c[3][i],()) for i,x in enumerate(old_values(c[1])))
    raise ValueError(k)
def parts(c):
    k=c[0]
    if k=='atom':return (),(),{'atom':c[1]}
    if k in ('E','Pi'):return c[1],c[2],{}
    if k=='paths':return (0,),(c[1],),{'x':c[2],'y':c[3]}
    if k in ('maps','equivalences'):return (0,1),(c[1],c[2]),{}
    if k=='retain':return (0,1),(c[1],c[3]),{'x':c[2]}
    if k=='comparison':return (0,1),(c[1],c[2]),{'e':c[3]}
    raise ValueError(k)
def build(kind,domain,children,**payload):
    # Carrier declarations are part of the header, not inferred from whether
    # a child happens to have any values.
    header={'kind':kind,'ports':tuple(domain),'carriers':tuple(native_values(children[i]) for i in domain),**payload}
    return [(header,ROOT,DECL)]+[({'table':children[i]},ROOT,('child',i)) for i in domain]
def encode(c):
    domain,children,payload=parts(c)
    return build(c[0],domain,{i:encode(g) for i,g in zip(domain,children)},**payload)
def schema(rows):
    es=entries(rows)
    if DECL not in es:raise ValueError('missing declaration')
    h=es[DECL]; k=h['kind']; domain=h['ports']; types=h['carriers']
    extras={'atom':{'atom'},'E':set(),'Pi':set(),'paths':{'x','y'},'maps':set(),
            'equivalences':set(),'retain':{'x'},'comparison':{'e'}}
    if k not in extras or set(h)!={'kind','ports','carriers'}|extras[k]:raise ValueError('invalid header')
    if len(set(domain))!=len(domain) or len(types)!=len(domain):raise ValueError('bad domain')
    if set(es)!={DECL}|{('child',i) for i in domain}:raise ValueError('missing/extra port')
    if k=='atom' and (domain or h['atom'] not in ATOMS):raise ValueError('bad atom')
    if k=='paths' and domain!=(0,):raise ValueError('bad path ports')
    if k in ('maps','equivalences','retain','comparison') and domain!=(0,1):raise ValueError('bad binary ports')
    children=[]
    for i,declared in zip(domain,types):
        if set(es[('child',i)])!={'table'}:raise ValueError('invalid child fields')
        child=es[('child',i)]['table']
        if native_values(child)!=declared:raise ValueError('incompatible attachment carrier')
        children.append(child)
    if k=='paths' and (h['x'] not in types[0] or h['y'] not in types[0]):raise ValueError('bad endpoints')
    if k=='retain' and h['x'] not in types[0]:raise ValueError('bad retained value')
    if k=='comparison':
        if len(h['e'])!=len(types[0]) or len(set(h['e']))!=len(h['e']) or set(h['e'])!=set(types[1]):
            raise ValueError('not an equivalence')
    return h,tuple(children)
def native_values(rows):
    h,children=schema(rows);k=h['kind'];t=h['carriers']
    if k=='atom':return ATOMS[h['atom']]
    if k=='E':return tuple((i,x) for i,a in zip(h['ports'],t) for x in a)
    if k=='Pi':return tuple(product(*t))
    if k=='paths':return ((),) if h['x']==h['y'] else ()
    if k=='maps':return tuple(product(t[1],repeat=len(t[0])))
    if k=='equivalences':return tuple(permutations(t[1])) if len(t[0])==len(t[1]) else ()
    if k=='retain':return t[1]
    if k=='comparison':return tuple((x,h['e'][i],()) for i,x in enumerate(t[0]))
    raise ValueError(k)
def decode(rows):
    h,children=schema(rows);k=h['kind'];cs=tuple(decode(g) for g in children)
    if k=='atom':return k,h['atom']
    if k in ('E','Pi'):return k,h['ports'],cs
    if k=='paths':return k,cs[0],h['x'],h['y']
    if k in ('maps','equivalences'):return k,*cs
    if k=='retain':return k,cs[0],h['x'],cs[1]
    if k=='comparison':return k,*cs,h['e']
    raise ValueError(k)
def shuffled(rows):
    result=deepcopy(rows)
    for label,_,_ in result:
        if 'table' in label:label['table']=shuffled(label['table'])
    RNG.shuffle(result)
    return result

def package_rows(q):
    c,v=q
    return [({'code':encode(c)},ROOT,('code',)),({'carrier':old_values(c),'value':v},ROOT,('value',))]
def package_decode(rows):
    es=entries(rows)
    if set(es)!={('code',),('value',)}:raise ValueError('bad package ports')
    if set(es[('code',)])!={'code'} or set(es[('value',)])!={'carrier','value'}:raise ValueError('bad package fields')
    c=es[('code',)]['code'];v=es[('value',)]
    if v['carrier']!=native_values(c) or v['value'] not in v['carrier']:raise ValueError('bad typed value')
    return decode(c),v['value']

atoms=tuple(('atom',a) for a in ATOMS)
boolc=('atom','Bool');unitc=('atom','Unit')
base=atoms+(('E',(False,True),(boolc,boolc)),('Pi',(False,True),(boolc,boolc)),('E',(),()),('Pi',(),()))
codes=list(base)
for a,b in product(base,repeat=2):
    codes.extend((('maps',a,b),('equivalences',a,b)))
    for x in old_values(a):codes.append(('retain',a,x,b))
    if len(old_values(a))==len(old_values(b)):
        for e in permutations(old_values(b)):codes.append(('comparison',a,b,e))
for a in base:
    for x,y in product(old_values(a),repeat=2):codes.append(('paths',a,x,y))
# Nested path/witness constructors, not just ground endpoints.
pathc=('paths',boolc,False,False)
codes.extend((('paths',pathc,(),()),('retain',('equivalences',boolc,boolc),(True,False),pathc)))
assert {c[0] for c in codes}=={'atom','E','Pi','paths','maps','equivalences','retain','comparison'}
package_count=0
for c in codes:
    rows=shuffled(encode(c))
    assert decode(rows)==c and native_values(rows)==old_values(c)
    for v in old_values(c):
        q=(c,v);wire=package_rows(q);RNG.shuffle(wire)
        assert package_decode(wire)==q
        package_count+=1
# Wrong carrier attachment, absent domains, omitted retain metadata, and
# equal-valued but constructor-distinct packets.
bad=encode(('maps',unitc,unitc))
bad[1][0]['table']=encode(boolc)
reject(lambda:native_values(bad))
reject(lambda:native_values([]))
bad=encode(('Pi',(),()));del bad[0][0]['ports']
reject(lambda:native_values(bad))
assert native_values(encode(('Pi',(),())))==((),)
assert native_values(encode(('Pi',(0,),(('atom','Empty'),))))==()
assert old_values(('atom','Unit'))==old_values(('Pi',(),()))
assert decode(encode(('atom','Unit')))!=decode(encode(('Pi',(),())))
retained=('retain',boolc,False,unitc)
assert native_values(encode(retained))==native_values(encode(unitc))
assert decode(encode(retained))!=decode(encode(unitc))
bad=package_rows((unitc,()));bad[1][0]['carrier']=old_values(boolc)
reject(lambda:package_decode(bad))
# Two equivalences at exactly the same pointed boundary, both compatible.
square=base[3];vs=old_values(square)
e_id=vs;e_swap=tuple((b,a) for a,b in vs)
assert e_id[vs.index((False,False))]==e_swap[vs.index((False,False))]
assert e_id!=e_swap
assert decode(encode(('comparison',square,square,e_id)))!=decode(encode(('comparison',square,square,e_swap)))

# Typed rule parameter codecs. Every original package/code argument is
# recursively encoded; certificates/equivalences/compatibility witnesses are
# retained as supplied payloads. Native operation correctness is checked for
# all parameters in Agda, not inferred from these finite declarations.
SCHEMAS={
 'E':(('I','raw'),('F','family'),('i','raw')),
 'Pi':(('I','raw'),('F','family')),
 'compare':(('a','package'),('b','package'),('e','raw'),('p','raw')),
 'identity':(('a','package'),),
 'inverse':(('a','package'),('b','package'),('e','raw'),('p','raw')),
 'compose':(('a','package'),('b','package'),('c','package'),('e','raw'),('f','raw'),('p','raw'),('q','raw')),
 'higher':(('Q','code'),('x','raw'),('y','raw'),('p','raw'),('q','raw'),('alpha','raw')),
 'reflexivity':(('Q','code'),('x','raw')),
 'path-lift':(('Q','code'),('R','code'),('e','raw'),('x','raw'),('y','raw')),
 'distribution':(('I','raw'),('J','raw'),('F','families'),('v','raw')),
 'E-congruence':(('I','raw'),('F','family'),('G','family'),('e','raw'),('p','raw'),('i','raw')),
 'Pi-congruence':(('I','raw'),('F','family'),('G','family'),('e','raw'),('p','raw')),
}
def encode_arg(t,x):
    if t=='code':return encode(x)
    if t=='package':return package_rows(x)
    if t=='family':return tuple(package_rows(q) for q in x)
    if t=='families':return tuple(tuple(package_rows(q) for q in f) for f in x)
    return deepcopy(x)
def decode_arg(t,x):
    if t=='code':return decode(x)
    if t=='package':return package_decode(x)
    if t=='family':return tuple(package_decode(q) for q in x)
    if t=='families':return tuple(tuple(package_decode(q) for q in f) for f in x)
    return deepcopy(x)
def rule_rows(kind,args):
    spec=SCHEMAS[kind]
    if set(args)!={key for key,t in spec}:raise ValueError('bad rule parameters')
    return [({'kind':kind,'fields':spec},ROOT,DECL)]+[({'value':encode_arg(t,args[key])},ROOT,('parameter',key)) for key,t in spec]
def rule_decode(rows):
    es=entries(rows);h=es[DECL];spec=SCHEMAS[h['kind']]
    if h['fields']!=spec or set(h)!={'kind','fields'}:raise ValueError('bad rule declaration')
    if set(es)!={DECL}|{('parameter',key) for key,t in spec}:raise ValueError('bad rule ports')
    if any(set(es[('parameter',key)])!={'value'} for key,t in spec):raise ValueError('bad parameter fields')
    return h['kind'],{key:decode_arg(t,es[('parameter',key)]['value']) for key,t in spec}
u=(unitc,());sq=(square,(False,False));ident=((),)
fixtures={
 'E':dict(I=(0,1),F=((boolc,False),(boolc,True)),i=0),
 'Pi':dict(I=(0,1),F=((boolc,False),(boolc,True))),
 'compare':dict(a=sq,b=sq,e=e_swap,p=()),
 'identity':dict(a=sq),
 'inverse':dict(a=sq,b=sq,e=e_swap,p=()),
 'compose':dict(a=sq,b=sq,c=sq,e=e_swap,f=e_swap,p=(),q=()),
 'higher':dict(Q=unitc,x=(),y=(),p=(),q=(),alpha=()),
 'reflexivity':dict(Q=unitc,x=()),
 'path-lift':dict(Q=boolc,R=boolc,e=(True,False),x=False,y=True),
 'distribution':dict(I=((),),J=(((),),),F=((u,),),v=(((),()),)),
 'E-congruence':dict(I=((),),F=(u,),G=(u,),e=(ident,),p=((),),i=()),
 'Pi-congruence':dict(I=((),),F=(u,),G=(u,),e=(ident,),p=((),)),
}
for kind,args in fixtures.items():
    wire=rule_rows(kind,args);RNG.shuffle(wire)
    assert rule_decode(wire)==(kind,args)
# Unselected E inputs and actual filler payloads are present in the codec.
r0=rule_rows('E',fixtures['E']);changed=deepcopy(fixtures['E']);changed['F']=((boolc,False),(boolc,False))
assert rule_decode(r0)!=rule_decode(rule_rows('E',changed))
compare2={**fixtures['compare'],'e':e_id}
assert rule_decode(rule_rows('compare',fixtures['compare']))!=rule_decode(rule_rows('compare',compare2))
reject(lambda:rule_decode(rule_rows('compare',fixtures['compare'])[:-1]))

# Native NAND/Wolfram: retain declared empty fibers even when no values exist.
def nand(a,b):
    domain=tuple(product(a,b));empty=encode(('atom','Empty'))
    return native_values(build('Pi',domain,{i:empty for i in domain}))
def word(a,b,c):return nand(nand(nand(a,b),c),nand(a,nand(nand(a,c),a)))
for a,b,c in product(range(4),repeat=3):assert len(word(tuple(range(a)),tuple(range(b)),tuple(range(c))))==int(c>0)
assert len(word((0,),(0,),(0,1)))!=2

# Audit the independent implementation blocks, separately from legacy proofs.
core=(BASE/'agda/IndexedConstructorTables.agda').read_text(encoding='utf-8').split('module Core',1)[1].split('  -- Decoder-only',1)[0]
assert core.count('    table-node :')==1
rules=(BASE/'agda/NativeTableRules.agda').read_text(encoding='utf-8').split('module Native',1)[1].split('  -- Legacy comparison',1)[0]
for text in (core,rules):
    for forbidden in ('Legacy.','O.Code','O.Complete','G.decode','R.Resolve'):assert forbidden not in text
native_jet=(BASE/'agda/NativeTidalTableReadout.agda').read_text(encoding='utf-8').split('-- A declared exact second jet',1)[1].split('-- Compare',1)[0]
for forbidden in ('OldJet.','Old.','G.decode','N.R.'):
    assert forbidden not in native_jet
rp=BASE/'results/agda-NativeTableRegression.json'
r=json.loads(rp.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=('IndexedConstructorTables','NativeTableRules','IndexedResolutionTransport','NativeTableResolution',
         'NativeTableRegression','TableFibrationCycle','WholePackageSigmaPi','WholePackageResolution',
         'NandConstructions','QBooleanity','ProofRelevantCoherenceClosure','BoundaryGeneratedQuestions',
         'NativeTidalTableReadout','NewtonianTidalRoutes','NewtonianTidalKernel','NewtonianTidalFixture',
         'NewtonianPotentialJet','NewtonianTidalCertificate')
for m in modules:assert r['owner_source_inventory_sha256'][m+'.agda']==sha(BASE/f'agda/{m}.agda'),m
fp=BASE/'results/native-table-formal-audit.json'
audit=json.loads(fp.read_text(encoding='utf-8-sig'))
assert audit['positive_receipt_sha256'].lower()==sha(rp)
assert audit['checker_sha256'].lower()==sha(BASE/'checkers/check_native_table_equivalence.ps1')
assert len(audit['controls'])==6
for c in audit['controls']:
    assert c['correctly_rejected'] and c['exit_code']!=0
    assert c['source_sha256'].lower()==sha(BASE/f"agda/negative/{c['module']}.agda")
packet={
 'status':'full-typed-native-table-equivalence-checked',
 'obligations':['forward realization','attachment transport','route/coherencer compatibility','readout descent'],
 'code_forms':8,'rule_schemas':12,'code_roundtrips':len(codes),'value_package_roundtrips':package_count,
 'rule_parameter_roundtrips':len(fixtures),'nand_double_negation_controls':64,'intended_formal_rejections':6,
 'independent_tidal_components_formally_checked':9,
 'formal_receipt_sha256':sha(rp),'formal_audit_sha256':sha(fp),'checker_sha256':sha(Path(__file__).resolve()),
 'source_sha256':{m:sha(BASE/f'agda/{m}.agda') for m in modules},
 'proved':['all-Code syntax equivalence with one-constructor indexed recursive table nodes',
           'full complete-package equivalence, with forward selected values unchanged by refl',
           'all twelve independent native rule schemas equivalent with typed marked port/input/output compatibility',
           'actual full Resolve closure equivalence for arbitrary original seed families, including endpoint square',
           'both retained-derivation inverse laws and no propositional truncation of supplied certificates',
           'actual imported marked-boundary filler equivalence and composition compatibility by refl',
           'independently built native NAND constructor/operation commute by refl and transfer Wolfram double negation',
           'unique-endpoint kernel instances and four-step table-data recovery',
           'independent thirteen-row second-jet arithmetic and tensor projection agree with both actual tidal routes',
           'actual tidal packages, comparison rule and retained history instantiate the native bridge',
           'a first-jet-only readout cannot recover the Hessian for all exact jets'],
 'scope':['intrinsic typed well-founded recursive table schema; arbitrary supplied index types remain allowed',
          'declarations retain active domains, expected attachment carriers and actual witness payloads',
          'atoms and source-policy witnesses remain supplied data as in the original signature'],
 'not_claimed':['arbitrary malformed/unmarked raw table equivalent to a typed constructor',
                'opposite endpoint regrouping alone is Pi',
                'arbitrary supplied atoms/functions generated by grouping',
                'continuum topology or general jet-completion theorem',
                'new physical realization or empirical evidence beyond the existing finite exact fixture'],
}
(BASE/'results/native-table-equivalence.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(f'PASS: all 8 code forms / 12 schemas; {len(codes)} code and {package_count} value-package controls; source-bound full closure proof.')

"""Finite unordered-row controls for the independent recursive E/P tables.
The unrestricted typed and higher-path statements are proved in Agda.
"""
from itertools import product
from pathlib import Path
from copy import deepcopy
import hashlib,json,random
BASE=Path(__file__).resolve().parents[1]
ATOMS={'Empty':(), 'Unit':((),), 'Bool':(False,True)}
RNG=random.Random(417)
DECL=('declaration',)
ROOT='root'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def expect_rejection(f):
    try:f()
    except (ValueError,KeyError):return
    raise AssertionError('malformed table accepted')
def indexed(rows):
    result={}
    for label,source,target in rows:
        if source!=ROOT or target in result:raise ValueError('bad or duplicate endpoint')
        result[target]=label
    if DECL not in result:raise ValueError('missing declaration')
    return result
def shape(rows):
    entries=indexed(rows);head=entries[DECL];kind=head['kind']
    if kind=='atom':
        if set(head)!={'kind','atom'} or set(entries)!={DECL} or head['atom'] not in ATOMS:raise ValueError('bad atom')
        return head,(),{}
    if kind not in ('E','P'):raise ValueError('unsupported constructor')
    if set(head)!={'kind','domain'}:raise ValueError('bad declaration fields')
    domain=head['domain']
    if len(set(domain))!=len(domain):raise ValueError('duplicate index')
    expected={DECL}|{('child',i) for i in domain}
    if set(entries)!=expected:raise ValueError('missing/extra declared port')
    if any(set(entries[('child',i)])!={'table'} for i in domain):raise ValueError('bad child fields')
    children={i:entries[('child',i)]['table'] for i in domain}
    return head,domain,children

def node(kind,domain,children):
    rows=[({'kind':kind,'domain':tuple(domain)},ROOT,DECL)]
    rows += [({'table':children[i]},ROOT,('child',i)) for i in domain]
    return rows

def atom(name):return [({'kind':'atom','atom':name},ROOT,DECL)]

# Reference code AST and its codec. No reference AST is stored in a row label.
def encode(c):
    if c[0]=='atom':return atom(c[1])
    kind,domain,children=c
    return node(kind,domain,{i:encode(g) for i,g in zip(domain,children)})
def decode(rows):
    h,domain,children=shape(rows)
    if h['kind']=='atom':return ('atom',h['atom'])
    return h['kind'],domain,tuple(decode(children[i]) for i in domain)
def old_values(c):
    if c[0]=='atom':return ATOMS[c[1]]
    k,domain,children=c
    if k=='E':return tuple((i,x) for i,g in zip(domain,children) for x in old_values(g))
    return tuple(product(*(old_values(g) for g in children)))

# Native row interpreter: does NOT call decode or old_values.
def values(rows):
    h,domain,children=shape(rows)
    if h['kind']=='atom':return ATOMS[h['atom']]
    if h['kind']=='E':return tuple((i,x) for i in domain for x in values(children[i]))
    return tuple(product(*(values(children[i]) for i in domain)))
def shuffled(rows):
    rows=deepcopy(rows)
    for label,_,_ in rows:
        if 'table' in label:label['table']=shuffled(label['table'])
    RNG.shuffle(rows)
    return rows
atoms=tuple(('atom',n) for n in ATOMS)
codes=atoms
for _ in range(2):
    codes=atoms+tuple((k,tuple(range(n)),children)
                     for k in ('E','P') for n in range(3) for children in product(codes,repeat=n))
assert len(codes)==1745
value_cases=0
for c in codes:
    rows=shuffled(encode(c))
    assert decode(rows)==c and decode(encode(decode(rows)))==c
    assert values(rows)==old_values(c)
    value_cases+=len(values(rows))
# Empty index declaration versus existing index with empty fiber.
p0=node('P',(),{})
p1empty=node('P',(0,),{0:atom('Empty')})
assert values(p0)==((),) and values(p1empty)==()
expect_rejection(lambda:values([]))
expect_rejection(lambda:values(p1empty[:1]))
bad=deepcopy(p0);del bad[0][0]['domain']
expect_rejection(lambda:values(bad))
expect_rejection(lambda:values(p0+p0))
expect_rejection(lambda:values([({'kind':'maps'},ROOT,DECL)]))
assert values(atom('Unit'))==values(p0) and decode(atom('Unit'))!=decode(p0)

# Runtime tables retain complete input runs and supplied certificates.
def literal(table,v,certificate):
    return [({'op':'literal','code':table,'value':v,'certificate':certificate},ROOT,DECL)]
def assemble(op,domain,inputs,chosen=None):
    head={'op':op,'domain':tuple(domain)}
    if op=='E':head['chosen']=chosen
    return [(head,ROOT,DECL)]+[({'run':inputs[i]},ROOT,('input',i)) for i in domain]
def run_shape(rows,admitted):
    entries=indexed(rows);h=entries[DECL]
    if h['op']=='literal':
        if set(h)!={'op','code','value','certificate'} or set(entries)!={DECL}:raise ValueError('extra literal fields/ports')
        if h['certificate'] not in admitted:raise ValueError('unadmitted literal')
        if h['value'] not in values(h['code']):raise ValueError('ill-typed literal')
        return h,(),{}
    if h['op'] not in ('E','P'):raise ValueError('unsupported rule')
    expected_head={'op','domain','chosen'} if h['op']=='E' else {'op','domain'}
    if set(h)!=expected_head:raise ValueError('bad operation fields')
    domain=h['domain']
    if len(set(domain))!=len(domain):raise ValueError('duplicate index')
    if set(entries)!={DECL}|{('input',i) for i in domain}:raise ValueError('missing/extra input')
    if h['op']=='E' and h['chosen'] not in domain:raise ValueError('absent selected index')
    if any(set(entries[('input',i)])!={'run'} for i in domain):raise ValueError('bad input fields')
    return h,domain,{i:entries[('input',i)]['run'] for i in domain}
def execute(rows,admitted):
    h,domain,inputs=run_shape(rows,admitted)
    if h['op']=='literal':return h['code'],h['value']
    outputs={i:execute(inputs[i],admitted) for i in domain}
    code=node(h['op'],domain,{i:outputs[i][0] for i in domain})
    v=(h['chosen'],outputs[h['chosen']][1]) if h['op']=='E' else tuple(outputs[i][1] for i in domain)
    assert v in values(code)
    return code,v

def legacy_rule(kind,domain,qs,chosen=None):
    retained=tuple(('retain',q[0],q[1],q[0]) for q in qs)
    v=(chosen,qs[domain.index(chosen)][1]) if kind=='E' else tuple(q[1] for q in qs)
    return (kind,domain,retained),v
def old_program(rows,admitted):
    h,domain,inputs=run_shape(rows,admitted)
    if h['op']=='literal':
        return {'rule':'seed','output':(decode(h['code']),h['value']),
                'literal_code':decode(h['code']),'value':h['value'],'certificate':h['certificate']}
    kids=tuple(old_program(inputs[i],admitted) for i in domain)
    return {'rule':h['op'],'domain':domain,'chosen':h.get('chosen'), 'premises':kids,
            'output':legacy_rule(h['op'],domain,tuple(k['output'] for k in kids),h.get('chosen'))}
def from_old_program(d):
    if d['rule']=='seed':return literal(encode(d['literal_code']),d['value'],d['certificate'])
    return assemble(d['rule'],d['domain'],{i:from_old_program(k) for i,k in zip(d['domain'],d['premises'])},d['chosen'])
def erase_type_retains(c):
    if c[0]=='retain':return erase_type_retains(c[3])
    if c[0]=='atom':return c
    return c[0],c[1],tuple(erase_type_retains(g) for g in c[2])
def normalize_run(rows,admitted):
    h,domain,inputs=run_shape(rows,admitted)
    if h['op']=='literal':return ('literal',decode(h['code']),h['value'],h['certificate'])
    return h['op'],domain,h.get('chosen'),tuple(normalize_run(inputs[i],admitted) for i in domain)
ADMITTED={'certificate-0','certificate-1'}
leaves=tuple(literal(atom(name),v,certificate) for name in ATOMS
             for v in ATOMS[name] for certificate in sorted(ADMITTED))
runs=list(leaves)
for n in range(3):
    domain=tuple(range(n))
    for children in product(leaves,repeat=n):
        inputs=dict(zip(domain,children))
        runs.append(assemble('P',domain,inputs))
        runs.extend(assemble('E',domain,inputs,i) for i in domain)
# Additional recursive assemblies, not just literal children.
for i in range(100):
    inputs={0:runs[RNG.randrange(len(runs))],1:runs[RNG.randrange(len(runs))]}
    runs.append(assemble('E' if i%2 else 'P',(0,1),inputs,0))
for r in runs:
    r=deepcopy(r);RNG.shuffle(r)
    native_code,native_v=execute(r,ADMITTED)
    d=old_program(r,ADMITTED)
    assert erase_type_retains(d['output'][0])==decode(native_code)
    assert d['output'][1]==native_v
    assert old_program(from_old_program(d),ADMITTED)==d
    assert normalize_run(from_old_program(d),ADMITTED)==normalize_run(r,ADMITTED)
left=literal(atom('Unit'),(),'certificate-0')
right0=literal(atom('Bool'),False,'certificate-0')
right1=literal(atom('Bool'),True,'certificate-0')
e0=assemble('E',(0,1),{0:left,1:right0},0)
e1=assemble('E',(0,1),{0:left,1:right1},0)
assert execute(e0,ADMITTED)==execute(e1,ADMITTED)
assert old_program(e0,ADMITTED)['output']!=old_program(e1,ADMITTED)['output']
assert normalize_run(e0,ADMITTED)!=normalize_run(e1,ADMITTED)
certificate0=literal(atom('Unit'),(),'certificate-0')
certificate1=literal(atom('Unit'),(),'certificate-1')
assert execute(certificate0,ADMITTED)==execute(certificate1,ADMITTED)
assert old_program(certificate0,ADMITTED)!=old_program(certificate1,ADMITTED)
expect_rejection(lambda:execute(certificate0,set()))
empty_run=assemble('P',(),{})
assert execute(empty_run,set())==(p0,())
assert old_program(empty_run,set())['rule']=='P'
missing=deepcopy(left);del missing[0][0]['certificate']
expect_rejection(lambda:execute(missing,ADMITTED))
# NAND uses the native table builder/interpreter only, with declared empty
# fibers at every index. Test the full word, including nonpropositional C.
def n(a,b):
    domain=tuple(product(a,b))
    return values(node('P',domain,{i:atom('Empty') for i in domain}))
def w(a,b,c):return n(n(n(a,b),c),n(a,n(n(a,c),a)))
for a,b,c in product(range(4),repeat=3):assert len(w(tuple(range(a)),tuple(range(b)),tuple(range(c))))==int(c>0)
assert len(w((0,),(0,),(0,1)))!=2

# Fresh formal closure and intended failures are bound to current sources.
rp=BASE/'results/agda-RecursiveTableRegression.json'
r=json.loads(rp.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=('RecursiveConstructorTables','RecursiveTableRuntime','RecursiveTableRegression',
         'TableFibrationCycle','WholePackageSigmaPi','WholePackageResolution','NandConstructions','QBooleanity')
for m in modules:assert r['owner_source_inventory_sha256'][m+'.agda']==sha(BASE/f'agda/{m}.agda'),m
c=json.loads((BASE/'results/recursive-constructor-formal-audit.json').read_text(encoding='utf-8-sig'))
assert c['positive_receipt_sha256'].lower()==sha(rp)
assert c['checker_sha256'].lower()==sha(BASE/'checkers/check_recursive_constructor_tables.ps1')
assert len(c['controls'])==3
for control in c['controls']:
    assert control['correctly_rejected'] and control['exit_code']!=0
    assert control['source_sha256'].lower()==sha(BASE/f"agda/negative/{control['module']}.agda")
# An additional bounded audit of the independent implementation blocks.
core=(BASE/'agda/RecursiveConstructorTables.agda').read_text(encoding='utf-8').split('  data Header',1)[1].split('  -- Decoder',1)[0]
runtime=(BASE/'agda/RecursiveTableRuntime.agda').read_text(encoding='utf-8').split('  data Run',1)[1].split('  -- Legacy decoding',1)[0]
for text in (core,runtime):
    for forbidden in ('Legacy.','O.','R.Resolve','R.Rule'):assert forbidden not in text
packet={
 'status':'independent-recursive-EP-tables-checked',
 'obligations':['forward realization','attachment transport','route/coherencer compatibility','readout descent'],
 'code_roundtrips':len(codes),'value_instances':value_cases,'runtime_roundtrips':len(runs),
 'nand_double_negation_controls':64,'intended_formal_rejections':3,
 'formal_receipt_sha256':sha(rp),'checker_sha256':sha(Path(__file__).resolve()),
 'source_sha256':{m:sha(BASE/f'agda/{m}.agda') for m in modules},
 'coverage':{'independent_code_forms':['atom','E','Pi'],
             'independent_rules':['E-rule','Pi-rule'],
             'source_policy':'arbitrary supplied native Admit family, with actual certificates retained',
             'actual_closure':'Sigma q (Sigma (Resolve Seeds q) OnlyEP)'},
 'proved':['syntax and value-package equivalence for the explicit old atom/E/P fragment',
           'independent retained runtime equivalent to the actual restricted Resolve closure',
           'full original E/P package boundaries including retain metadata commute by refl',
           'native NAND constructor and operation commute by refl; Wolfram double-negation law',
           'empty-domain declarations and proof-relevant admission certificates retained',
           'actual level-polymorphic three-column kernel instances with uniqueness and four-step table-data recovery'],
 'remaining':['five other Code forms with dependent witness attachments',
              'ten other resolution schemas as independent table operations',
              'whole eight-code/twelve-rule representation equivalence',
              'independently defined physical realization/readout compatibility'],
}
(BASE/'results/recursive-constructor-tables.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(codes)} code, {value_cases} value, {len(runs)} runtime controls; exact independent E/P scope.')

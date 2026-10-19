"""One timed solver subprocess, or a small exhaustive encoding-equivalence audit."""
import argparse,json,time,hashlib,random,itertools,ast
from pathlib import Path
import z3
from reference_solver_encodings import MODES,build,validate_selection
parser=argparse.ArgumentParser();parser.add_argument('--input');parser.add_argument('--output',required=True)
parser.add_argument('--mode',choices=MODES,default='baseline');parser.add_argument('--timeout-ms',type=int,default=30000)
parser.add_argument('--seed',type=int,default=0);parser.add_argument('--equivalence',action='store_true')
args=parser.parse_args();started=time.perf_counter()
if args.timeout_ms<=0:raise ValueError('Positive timeout required')
if args.equivalence:
    rng=random.Random(137);fixtures=[]
    for case in range(10):
        ids=list(range(6));edges={(i,j) for i in ids for j in ids if rng.random()<.23}
        if case==0:edges={(0,1),(1,0),(1,2),(2,3),(3,2),(3,5)}
        if case==1:edges={(0,1),(1,5),(2,3),(3,2)}
        if case==2:edges={(0,1),(1,2),(2,5),(3,4),(4,5)}
        if case==3:edges=set(itertools.product(ids,ids))
        p={'packets':ids,'root':0,'exits':[5], 'operations':[{'source':a,'target':b} for a,b in sorted(edges)],
           'conflicts':[[a,b] for a,b in itertools.combinations(ids,2) if rng.random()<.08],
           'bodies':[{'species':'proton','packets':[i]} for i in ids], 'target':{'proton':4},
           'contacts':[{'bodies':[1,2],'links':[[1,2],[2,1]]}] if case%2 else []}
        if case==3:p['conflicts']=[]
        if case==5:
            p['bodies']=[{'species':'proton','packets':[0,1]},{'species':'proton','packets':[2,3]},{'species':'proton','packets':[4,5]}]
            p['target']={'proton':3};p['contacts']=[]
        fixtures.append(p)
    checks=0;satisfying=0
    for p in fixtures:
        models={mode:build(p,mode,5000,0)[:2] for mode in MODES}
        for mask in range(1<<len(p['packets'])):
            selected=[i for i in p['packets'] if mask&(1<<i)];expected=validate_selection(p,selected)
            satisfying+=expected
            for s,x in models.values():
                s.push();s.add(*[x[i] if i in selected else z3.Not(x[i]) for i in p['packets']])
                result=s.check();assert result!=z3.unknown
                assert (result==z3.sat)==expected,(mask,str(result),expected)
                s.pop();checks+=1
    # Compare our baseline assertions to the actual production encoder's AST,
    # stopping before its timed check and any output writes.
    source=Path(__file__).with_name('solve_reference_n14.py')
    body=ast.parse(source.read_text()).body;prefix=[];taking=False
    for statement in body:
        target=statement.targets[0].id if isinstance(statement,ast.Assign) and isinstance(statement.targets[0],ast.Name) else None
        if target=='ids':taking=True
        if target=='start':break
        if taking:prefix.append(statement)
    native=json.loads(Path('research/strominger/results/reference-na23-search/D5-input.json').read_text())
    namespace={'p':native,'z3':z3}
    exec(compile(ast.Module(body=prefix,type_ignores=[]),str(source),'exec'),namespace)
    instrumented,_,_=build(native,'baseline',30000,0)
    assert len(namespace['s'].assertions())==len(instrumented.assertions())
    assert all(a.eq(b) for a,b in zip(namespace['s'].assertions(),instrumented.assertions()))
    result={'status':'pass','fixtures':len(fixtures),'selectionChecks':checks,'satisfyingSelections':satisfying,'modes':MODES,'baseline_assertions_match_production':True}
else:
    raw=Path(args.input).read_bytes();p=json.loads(raw);loaded=time.perf_counter()
    s,x,encoding=build(p,args.mode,args.timeout_ms,args.seed);built=time.perf_counter()
    answer=s.check();solved=time.perf_counter()
    selected=[i for i in p['packets'] if z3.is_true(s.model().eval(x[i],model_completion=True))] if answer==z3.sat else None
    if selected is not None:assert validate_selection(p,selected),'Solver assignment failed direct graph/count/contact validation'
    statistics=s.statistics()
    result={'status':str(answer),'input':args.input,'inputSha256':hashlib.sha256(raw).hexdigest(),
            'mode':args.mode,'seed':args.seed,'timeoutMs':args.timeout_ms,'solver':'z3-'+z3.get_version_string(),
            'parseSeconds':loaded-started,'buildSeconds':built-loaded,'checkSeconds':solved-built,
            'totalSeconds':time.perf_counter()-started,'unknownReason':s.reason_unknown() if answer==z3.unknown else None,
            'selectedPackets':selected,'directSelectionValidation':selected is not None,
            'encoding':encoding,'statistics':{key:statistics.get_key_value(key) for key in statistics.keys()}}
paths=[Path(__file__),Path(__file__).with_name('reference_solver_encodings.py'),Path(__file__).with_name('solve_reference_n14.py')]
result['sourceHashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('selectedPackets','statistics','sourceHashes')},indent=2))

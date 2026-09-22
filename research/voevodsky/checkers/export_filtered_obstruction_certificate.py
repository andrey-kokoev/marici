"""Export discovery-side exact evidence; verification is a separate program."""
from pathlib import Path
from itertools import combinations,product
import hashlib,json,runpy
ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_translated_cubic_observer_growth.py'))
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
f=g['f']
oldrows=[row[0] for row,_ in t['selected'](2)]
target=(('e',0,1,1),('e',3,7,0),('e',15,31,1))
problem={'schema':'marici.filtered-cubic-obstruction.problem.v1',
 'background':2,'event_primes':[2,3,5,7,11,13],
 'source_record':'ordered vertex-potential differences; root potential zero',
 'old_outer':[0,15],'cubic_outer':[0,63],
 'old_seams':oldrows,'private_seams':target,
 'buffers':'vacuum','stage_two':'unchanged original saturated observer',
 'filtrations':{'B':['B','B','B','0'],'A':['A','A','B','0'],
 'G':['G','G','0','0'],'K':['K','N','L','0']},
 'definitions':{'M':'I E','N':'ker(pi) intersect M','L':'I^2 E',
 'f':'source evaluation restricted to G3','level_two_graph_signs':['1','-1']},
 'external_hypotheses':['old gap d2 is nonzero','private response factor Ey is positive',
 'surjective compatible source-bimodule evaluations','levelwise strict filtered category']}
# JSON-normalize tuples before binding the digest.
problem=json.loads(json.dumps(problem))
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def terms(col):
    return [{'word':list(w),'marks':list(m),'coefficient':str(c)} for (w,m),c in sorted(col.items())]
kernels=[]
for pair in combinations(range(6),2):
    rest=[j for j in range(6) if j not in pair]
    for flags in product((0,1),repeat=4):
        start=sum(1<<j for j,b in zip(rest,flags) if b)
        kernels.append({'start':start,'pair':list(pair),'record_rank':6,
                        'relations':[terms(f['relation'](pair,k)) for k in (0,1)]})
prefixes=[];witness=None
for subset in combinations(range(6),4):
    end=sum(1<<j for j in subset)
    rest=tuple(j for j in range(6) if j not in subset)
    for pairs in g['pairings'](subset):
        for kinds in product((0,1),repeat=2):
            col=f['chain_product']([f['relation'](p,k) for p,k in zip(pairs,kinds)])
            im=t['ordered'](0,col,2) if end==15 else {}
            old=[im.get((row,((),)*3),0) for row in oldrows]
            actions=[]
            for kind in (0,1):
                full=f['multiply'](col,f['relation'](rest,kind))
                image=t['ordered'](0,full,3)
                actions.append(str(image.get((target,((),)*4),0)))
            ident=len(prefixes)
            if pairs==((0,1),(2,3)) and kinds==(1,0):witness=ident
            prefixes.append({'id':ident,'end':end,'pairs':[list(p) for p in pairs],
                'kinds':list(kinds),'terms':terms(col),'old_coefficients':list(map(str,old)),
                'right_action_values':actions})
cert={'schema':'marici.filtered-cubic-obstruction.certificate.v1',
 'problem_sha256':digest(problem),'local_kernels':kernels,'prefixes':prefixes,
 'N_prefix_ids':[p['id'] for p in prefixes if p['old_coefficients']==['0','0']],
 'witness':{'prefix_id':witness,'suffix_kind':1,'private_value':'1'}}
folder=ROOT/'research/voevodsky/results'
for name,obj in [('filtered-obstruction-problem.json',problem),('filtered-obstruction-certificate.json',cert)]:
    (folder/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exported':True,'local_kernels':len(kernels),'prefixes':len(prefixes),
 'right_actions':2*len(prefixes),'problem_sha256':digest(problem)},indent=2))

"""Conditional correlated-word fine-edge realization; no analytical filler defaults."""
from pathlib import Path
import hashlib,json,copy
from esd7_strict_parent_evaluation import validate_profile,normalize,transition,equivalent
ROOT=Path(__file__).resolve().parents[3];BASE='research/strominger/'
CONTRACT=BASE+'contracts/f736-correlated-word-edges-attempt.v1.json'
SNAPSHOT=BASE+'contracts/persistent-seam-pe-conjecture-net.snapshot.rev42.json'
OUT=BASE+'results/f736-correlated-word-edges/'
def load(p):return json.loads((ROOT/p).read_text())
def main():
    spec=load(CONTRACT);profile=load(spec['profile']);validate_profile(profile);checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    inputs={CONTRACT,SNAPSHOT,spec['profile'],BASE+'checkers/check_f736_correlated_word_edges.py',BASE+'checkers/esd7_strict_parent_evaluation.py',BASE+'f736-correlated-word-edges-result-v1.md',*profile['sources']}
    for name in ['native-ne-fine-face/verification','esd7-simplicial-refinement-verification','esd7-strict-parent-evaluation-verification','f736-physical-readout/verification']:
        p=BASE+'results/'+name+'.json';r=load(p);inputs.add(p)
        check('live receipt closure: '+name,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==sha for q,sha in r['sourceHashes'].items()));inputs.update(r['sourceHashes'])
    pre=load(SNAPSHOT);node=next(n for n in pre['conjectures'] if n['id']=='f736-correlated-word-edges-attempt')
    check('correlated-word realization registered before execution',node['status']=='open' and node['registration_before_execution'])
    refinement=load(BASE+'results/esd7-simplicial-refinement.json');strict=load(BASE+'results/esd7-strict-parent-evaluation.json');face=load(BASE+'results/native-ne-fine-face/binding.json')['face']
    cells={r['cell']:r for r in refinement['cells']};programs={r['cell']:r for r in strict['cells']};f=cells[spec['face']]
    words={v:cells[v]['parentWord'] for v in face['vertices']}
    check('all three vertex words retain seven occurrences',all(len(w)==7 for w in words.values()) and len(words)==3)
    # The old evaluator outputs whole parent-word paths, not arrows between fine objects.
    first,second=face['sharedEdgeRoute'];failed_program=programs[first]['executionProgram']+programs[second]['executionProgram']
    try:normalize(failed_program,'V1');domain_error=None
    except ValueError as e:domain_error=str(e)
    check('flattened whole-word paths fail as composable fine-edge maps',domain_error=='operator domain mismatch at R1')
    def edge(fid,reverse=False):
        u,v=cells[fid]['fineVertexOrder']
        if reverse:u,v=v,u
        rows=[]
        for k,(i,j) in enumerate(zip(words[u],words[v])):
            p=transition(i,j);normal=normalize(p,'V'+str(i))
            if normal['target']!='V'+str(j):raise AssertionError('wrong component codomain')
            if not equivalent(['S'+str(i)]+p,['S'+str(j)],'D'):raise AssertionError('correlated image not preserved')
            rows.append({'occurrence':k,'sourceChart':i,'targetChart':j,'program':p,'typedReduction':normal})
        return {'edge':fid,'sourceVertex':u,'targetVertex':v,'components':rows,'domain':'Gamma_'+u+'(D)','codomain':'Gamma_'+v+'(D)','orientation':'geometric' if reverse else 'retained-refinement'}
    edges={e:edge(e) for e in [*face['sharedEdgeRoute'],face['directEdge']]}
    inverse_edges={e:edge(e,True) for e in edges}
    check('all42 oriented component maps preserve their correlated source image',sum(len(e['components']) for e in [*edges.values(),*inverse_edges.values()])==42)
    # Retained orientation reverses the geometric triangle: E539 then E514.
    r0,r1=edges[second],edges[first];direct=edges[face['directEdge']]
    check('retained route has matching fine-object domains',r0['targetVertex']==r1['sourceVertex'] and r0['sourceVertex']==direct['sourceVertex'] and r1['targetVertex']==direct['targetVertex'])
    triangles=[]
    for k in range(7):
        a,b,c=(words[v][k] for v in f['fineVertexOrder'])
        composed=r0['components'][k]['program']+r1['components'][k]['program'];p=direct['components'][k]['program']
        check('retained triangle square at occurrence '+str(k),equivalent(composed,p,'V'+str(a)))
        triangles.append({'occurrence':k,'parentVertices':[a,b,c],'degenerate':len({a,b,c})<3,'parentRole':None if len({a,b,c})<3 else 'H'+''.join(map(str,[a,b,c])),'compositeProgram':composed,'directProgram':p})
        back0,back1=inverse_edges[first],inverse_edges[second]
        check('geometric triangle square at occurrence '+str(k),equivalent(back0['components'][k]['program']+back1['components'][k]['program'],inverse_edges[face['directEdge']]['components'][k]['program'],'V'+str(c)))
    adjacency_squares=[]
    for e in [*edges.values(),*inverse_edges.values()]:
        for k in range(6):
            a,b=e['components'][k],e['components'][k+1]
            left=a['program']+transition(a['targetChart'],b['targetChart'])
            right=transition(a['sourceChart'],b['sourceChart'])+b['program']
            assert equivalent(left,right,'V'+str(a['sourceChart']))
            adjacency_squares.append({'edge':e['edge'],'orientation':e['orientation'],'occurrences':[k,k+1],'leftProgram':left,'rightProgram':right})
    check('all36 adjacent-occurrence naturality squares retain the word-chain links',len(adjacency_squares)==36)
    interleaved=[words[v][k] for k in range(7) for v in f['fineVertexOrder']]
    check('component triangles reassemble the full21-position face without erasure',interleaved==f['parentWord'])
    for e in edges:
        for k,row in enumerate(edges[e]['components']):
            assert equivalent(row['program']+inverse_edges[e]['components'][k]['program'],[],'V'+str(row['sourceChart']))
    check('both edge directions are inverses only on the declared correlated images',profile['inverseLawScope']=='on-images-of-the-same-D-only')
    def admit_tuple(word,records):
        if len(records)!=len(word):raise ValueError('occurrence count')
        if any(r['chart']!=chart or r['occurrence']!=k for k,(chart,r) in enumerate(zip(word,records))):raise ValueError('typed occurrence mismatch')
        if len({r['observer'] for r in records})!=1:raise ValueError('independent observer components')
        return True
    w=words[face['vertices'][0]];sample=[{'chart':c,'occurrence':k,'observer':'d'} for k,c in enumerate(w)]
    check('correlated tuple admission retains every occurrence',admit_tuple(w,sample))
    mutations=[sample[:-1],copy.deepcopy(sample),copy.deepcopy(sample)]
    mutations[1][-1]['observer']='different-d';mutations[2][0]['chart']=4
    for label,bad in zip(['erased occurrence','independent observer','wrong chart domain'],mutations):
        try:admit_tuple(w,bad);rejected=False
        except ValueError:rejected=True
        check('reject '+label,rejected)
    nondegenerate=[t for t in triangles if not t['degenerate']]
    check('local H134 labels are retained separately from the computed parent lift',all(c['role']=='H134' for c in face['localContexts']) and len(nondegenerate)==1 and nondegenerate[0]['parentRole']=='H234')
    artifact={'contract':CONTRACT,'face':face,'profile':profile,'vertexWords':words,'edges':edges,'inverseEdges':inverse_edges,'parentTriangles':triangles,'adjacentOccurrenceSquares':adjacency_squares,
        'flattenedProgramFailure':{'attemptedRoute':[first,second],'program':failed_program,'start':'V1','error':domain_error,'missingDatum':'a realization of each seven-occurrence fine vertex as an object and each fine edge as a map between those objects'},
        'conditionalFineEdgeRealizationEstablished':True,'localRegistryRoles':['H134','H134'],'nondegenerateParentRole':nondegenerate[0]['parentRole'],'nondegenerateOccurrence':nondegenerate[0]['occurrence'],
        'intendedHomotopyBindingEstablished':False,'completionExtensionEstablished':False,'fullPbConstructionEstablished':False,
        'remainingObligation':'Compare the intended regulator-dependent local H134 witnesses with this declared correlated-word realization, whose only nondegenerate component triangle is parent H234 at occurrence5. Strict image cancellation does not identify those witnesses. Retain cross-occurrence coherence and regulator data.',
        'scope':spec['scope']}
    (ROOT/OUT).mkdir(parents=True,exist_ok=True);dest=OUT+'realization.json';(ROOT/dest).write_text(json.dumps(artifact,indent=2)+'\n');inputs.add(dest)
    report={'status':'passed','check_count':len(checks),'checks':checks,'face':'F736','orientedComponentMaps':42,'routeSquares':14,'faceOccurrences':21,'adjacentOccurrenceSquares':36,
        'conditionalFineEdgeRealizationEstablished':True,'flattenedProgramCompositionRejected':True,'nondegenerateParentRole':'H234','nondegenerateOccurrence':5,
        'intendedHomotopyBindingEstablished':False,'completionExtensionEstablished':False,'fullPbConstructionEstablished':False,
        'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(inputs)}}
    (ROOT/OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['checks','sourceHashes']}))
if __name__=='__main__':main()

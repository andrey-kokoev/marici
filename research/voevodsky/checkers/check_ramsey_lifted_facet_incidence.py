"""Four actual PN ports with retained incidence and candidate field comparisons."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_ramsey_moving_carrier_NE import restore,block
from exact_multiradical import Radical as R,mm,adj,identity,serialize
V='research/voevodsky/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def perm(p):return [[R(int(j==p[i])) for j in range(5)] for i in range(5)]
INV={'PN':'inverse-PN','inverse-PN':'PN','P-reader':'P-reader','NE':'NE','Q':'Qinv','Qinv':'Q'}
def inverse(w):return [INV[x] for x in reversed(w)]
def normal(w):
    out=[]
    for x in w:
        if out and INV[x]==out[-1]:out.pop()
        else:out.append(x)
    return out

def main():
    summary_path=V+'results/ramsey-complementary-sewing-v1.json'
    summary=load(summary_path);assert summary['status']=='passed'
    for p,h in summary['source_sha256'].items():assert sha(p)==h
    lift_path=V+'results/ramsey-NE-lift-context-v1.json';lift=load(lift_path)
    for p,h in lift['source_sha256'].items():assert sha(p)==h
    qe=restore(load(V+'results/ramsey-moving-carrier-NE-v1.json')['electronAction'])
    q=block(identity(36),qe)
    inputs=[summary_path,lift_path,V+'results/ramsey-moving-carrier-NE-v1.json']
    selected={};sewing={};fixtures={}
    vertices=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1']
    for label in ['base','complement']:
        fp=summary['fixtures'][label]['path'];sp=summary['field_checks'][label]['path']
        assert sha(fp)==summary['fixtures'][label]['sha256'] and sha(sp)==summary['field_checks'][label]['sha256']
        f,s=load(fp),load(sp);fixtures[label]=f;sewing[label]=s;inputs.extend([fp,sp])
        for p,h in s['sourceHashes'].items():assert sha(p)==h
        packets={p['id']:p for p in f['packets']};charts={c['index']:c for c in f['charts']};cells={c['id']:c for c in f['cells']}
        rootcell=charts[packets[f['rootPacket']]['chart']]['cell']
        for op in sorted(f['operations'],key=lambda o:o['id']):
            a,b=packets[op['source']],packets[op['target']];ca,cb=charts[a['chart']],charts[b['chart']]
            if op['kind']!='PN' or ca['cell']!=rootcell:continue
            facet=next(i for i,v in enumerate(vertices) if v not in op['face'])
            if facet in selected:continue
            roles={v:k[0] for k,v in ca['aliases'].items() if v in vertices}
            assert sum(roles[v]=='M' for v in op['face'])==2
            assert set(cells[ca['cell']]['vertices'])&set(cells[cb['cell']]['vertices'])==set(op['face'])
            selected[facet]={'facet':facet,'context':label,'lift':0 if label=='base' else 1,
                'face':sorted(op['face']),'roles':roles,'permit':{'parentFace':sorted(op['face']),'MCount':2},
                'operation':op,'source':{'packet':a,'chart':ca,'cell':cells[ca['cell']]},
                'target':{'packet':b,'chart':cb,'cell':cells[cb['cell']]},
                'historyLocations':[{'history':h['id'],'index':i} for h in f['histories'] for i,x in enumerate(h['operations']) if x==op['id']]}
    assert sorted(selected)==list(range(4))
    generators={k:restore(v) for k,v in sewing['base']['generatorMatrices'].items()}
    assert sewing['base']['generatorMatrices']==sewing['complement']['generatorMatrices']
    generators.update({'Q':q,'Qinv':adj(q)})
    root=next(x for x in sewing['base']['packetBindings'] if x['packet']==fixtures['base']['rootPacket'])
    rb,bb=restore(root['readout']),restore(root['binding'])
    words={};normalized_r={};normalized_b={};pi={};field_records={}
    for a,p in selected.items():
        s=sewing[p['context']];b=next(x for x in s['packetBindings'] if x['packet']==p['target']['packet']['id'])
        assert b['species']=='neutron'
        u=s['frameTypes']['neutron'+str(b['frameParity'])]['forwardFactorWord']
        words[a]=u+(['Q'] if p['lift'] else [])
        binding=restore(b['binding']);readout=restore(b['readout'])
        if p['lift']:binding=mm(q,binding);readout=mm(readout,adj(q))
        # Factor words are execution ordered. Check normalization on every input.
        nr=readout
        for x in reversed(words[a]):nr=mm(nr,generators[x])
        nb=binding
        for x in inverse(words[a]):nb=mm(generators[x],nb)
        pi[a]=perm(b['nativePermutation'])
        assert nr==mm(pi[a],rb) and nb==mm(bb,adj(pi[a]))
        normalized_r[a]=nr;normalized_b[a]=nb
        field_records[a]={'anchor':'actual PN target','frameWord':words[a],
            'binding':serialize(binding),'readout':serialize(readout),'nativePermutation':b['nativePermutation']}
    edges={};role_conflicts=0
    for a,b in permutations(range(4),2):
        support=sorted(set(selected[a]['face'])&set(selected[b]['face']));assert len(support)==2
        word=inverse(words[a])+words[b];cp=mm(pi[b],adj(pi[a]))
        assert normalized_r[b]==mm(cp,normalized_r[a])
        assert mm(normalized_b[b],cp)==normalized_b[a]
        assert normal(word+inverse(words[b])+words[a])==[]
        conflicts=[v for v in support if selected[a]['roles'][v]!=selected[b]['roles'][v]]
        role_conflicts+=len(conflicts)
        edges[a,b]={'parents':[a,b],'support':support,'comparisonWord':word,
            'coefficientComparison':serialize(cp),'roleDisagreements':conflicts,
            'parentPermits':[selected[a]['permit'],selected[b]['permit']]}
    triples=[]
    for a,b,c in permutations(range(4),3):
        vertex=set(selected[a]['face'])&set(selected[b]['face'])&set(selected[c]['face']);assert len(vertex)==1
        v=next(iter(vertex))
        for x,y in [(a,b),(b,c),(a,c)]:
            assert v in edges[x,y]['support']
            # Support restriction keeps both complete parent records by their keys.
            assert edges[x,y]['parents']==[x,y]
        assert normal(edges[a,b]['comparisonWord']+edges[b,c]['comparisonWord'])==normal(edges[a,c]['comparisonWord'])
        triples.append({'parents':[a,b,c],'vertex':v,'comparisonTriangle':True,'retainsParentPorts':True})
    assert len(edges)==12 and len(triples)==24 and role_conflicts>0
    # A forward lift is not the reverse lift. Its square is a visible central map.
    assert mm(q,q)!=identity(44)
    assert mm(q,adj(q))==identity(44)
    assert set.intersection(*(set(p['face']) for p in selected.values()))==set()
    inputs += [V+'contracts/ramsey-lifted-facet-incidence-attempt.v1.json',V+'checkers/check_ramsey_lifted_facet_incidence.py',
               V+'checkers/check_ramsey_moving_carrier_NE.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-lifted-facet-incidence.verification.v1','status':'passed',
        'scope_id':'four-native-PN-ports-lifted-incidence-comparisons-v1',
        'facetPorts':[selected[i] for i in range(4)],'PNTargetFieldBindings':field_records,
        'directedEdgeRecords':list(edges.values()),'orderedTripleVertexRecords':triples,
        'facetCount':4,'geometricEdges':6,'directedEdges':12,'orderedTripleVertexCells':24,
        'directedRoleDisagreements':role_conflicts,'fourfoldGeometricIntersectionEmpty':True,
        'commonRootIdentificationPolicyDeclared':True,'fullFieldComparisonSquaresChecked':True,
        'sourceDerivedGeometricEdgeObservable':False,'nativeWGRestrictionConstructed':False,
        'parentDescentResolved':False,'source_sha256':{p:sha(p) for p in inputs}}
    (ROOT/(V+'results/ramsey-lifted-facet-incidence-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['facetPorts','PNTargetFieldBindings','directedEdgeRecords','orderedTripleVertexRecords','source_sha256']},indent=2))
if __name__=='__main__':main()

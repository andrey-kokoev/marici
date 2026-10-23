"""Audit the proposed direct substitution of parent chart maps on fine edges.
This rejects only a context-free chart-at-each-vertex rule, not a refinement.
"""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
from esd7_attachment_channel import produce,decode

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
SOURCES=[
 'research/voevodsky/consolidated-four-presentation-analytic-pyramid-position.md',
 'research/voevodsky/interior-pyramid-nodes-must-refine-a-homotopy-coherent-diagram-of-four-realization-functors-not-mix-the-presentations-barycentrically.md',
 'research/voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md']


def audit(assembly):
    vertices={v['id']:v for v in assembly['vertices']}
    requirements=defaultdict(list); edges=[]
    for edge in assembly['edges']:
        a,b=edge['vertices']; delta=[y-x for x,y in zip(vertices[a]['barycentric'],vertices[b]['barycentric'])]
        donors=[i+1 for i,x in enumerate(delta) if x==-1]
        recipients=[i+1 for i,x in enumerate(delta) if x==1]
        if not all(x in (-1,0,1) for x in delta) or len(donors)!=len(recipients):
            raise ValueError('invalid lattice transfer')
        row={'edge':edge['id'],'source':a,'target':b,'delta':delta,'donors':donors,'recipients':recipients}
        if len(donors)==1:
            row['parentCandidate']=f'C{donors[0]}{recipients[0]}'
            requirements[a].append({'edge':edge['id'],'endpoint':'source','requiredChart':donors[0]})
            requirements[b].append({'edge':edge['id'],'endpoint':'target','requiredChart':recipients[0]})
        else:
            row['parentCandidate']=None
        edges.append(row)
    rows=[]
    for id,v in sorted(vertices.items()):
        req=requirements[id]; charts=sorted({r['requiredChart'] for r in req})
        rows.append({'vertex':id,'barycentric':v['barycentric'],'requiredCharts':charts,
                     'contextFreeAssignmentPossible':len(charts)==1,'incidenceRequirements':req})
    return {'edges':edges,'vertices':rows}


def reduce_parent(word):
    """Only the source's declared essential-image relation R_i S_i = I."""
    result=[]
    for token in word:
        if result and result[-1][0]=='R' and token[0]=='S' and result[-1][1:]==token[1:]:
            result.pop()
        else:result.append(token)
    return result


def main():
    assembly=decode(produce(7)); result=audit(assembly); checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    vertices={v['vertex']:v for v in result['vertices']}; edges={e['edge']:e for e in result['edges']}
    check('all560 generated edges audited',len(edges)==560)
    check('504 single transfers and56 compound transfers',Counter(len(e['donors']) for e in result['edges'])=={1:504,2:56})
    check('all120 vertex endpoint constraints audited',len(vertices)==120)
    histogram=Counter(len(v['requiredCharts']) for v in result['vertices'])
    check('four unique parent corners and116 conflicting fine vertices',histogram=={1:4,2:36,3:60,4:20})
    check('required parent charts equal positive barycentric support',all(
        v['requiredCharts']==[i+1 for i,n in enumerate(v['barycentric']) if n>0] for v in result['vertices']))
    check('F006 proposed parent edge words are C32 C21 and C31',
          [edges[e]['parentCandidate'] for e in ['E004','E037','E006']]==['C32','C21','C31'])
    check('parent essential-image composite reduces conditionally',reduce_parent(['S1','R2','S2','R3'])==['S1','R3'])
    check('mismatched parent types do not cancel',reduce_parent(['S1','R4','S2','R3'])==['S1','R4','S2','R3'])
    check('concrete V001 donor conflict is witnessed by actual adjacent edges',
          edges['E004']['source']==edges['E003']['source']=='V001' and
          edges['E004']['donors']==[3] and edges['E003']['donors']==[4])
    check('F006 source has retained background rather than being parent corner3',
          vertices['V001']['barycentric']==[0,0,1,6])
    # Every attempted chart label violates at least one of this vertex's edges.
    check('no context-free parent label resolves V001',all(any(
        r['requiredChart']!=candidate for r in vertices['V001']['incidenceRequirements']) for candidate in [1,2,3,4]))
    reverse=dict(assembly,edges=list(reversed(assembly['edges'])))
    other=audit(reverse)
    check('conflict does not depend on edge enumeration order',
          {v['vertex']:v['requiredCharts'] for v in other['vertices']}=={v['vertex']:v['requiredCharts'] for v in result['vertices']})
    artifact=BASE+'esd7-parent-chart-binding-audit.json'
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[*SOURCES,artifact,'research/strominger/checkers/esd7_attachment_channel.py',
            'research/strominger/checkers/check_esd7_parent_chart_binding.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,
            'singleTransferEdges':504,'compoundTransferEdges':56,'conflictingVertices':116,
            'requiredChartHistogram':dict(sorted(histogram.items())),
            'boundedCandidate':'Assign one parent chart to each fine vertex and replace every single unit transfer d_ij(alpha) by the bare parent C_ij.',
            'candidateDisposition':'rejected_context_free_substitution',
            'actualF006ComparisonEstablished':False,'refinementImpossible':False,'full114ChannelEstablished':False,
            'firstMissingDatum':'Source-bound fine-vertex objects X_alpha and incidence maps retaining the background and presentation context; then graph-domain/endpoint intertwiners for F006.',
            'parentFaceReduction':{'word':['S1','R2','S2','R3'],'normalForm':['S1','R3'],
                                   'assumption':'R2 S2 = I on the admitted observer essential image',
                                   'fineVertexIdentificationEstablished':False},
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Finite typing obstruction to bare context-free parent-chart substitution only. Context-dependent refinement, whiskering, or a joint-graph construction is not refuted. No numerical gate data or analytical filler is manufactured.'}
    (ROOT/BASE/'esd7-parent-chart-binding-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','singleTransferEdges','compoundTransferEdges','conflictingVertices','candidateDisposition']}))


if __name__=='__main__':main()

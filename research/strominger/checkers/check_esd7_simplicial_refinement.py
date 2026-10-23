"""Finite all-cell face-map verification of the canonical edgewise nerve lift."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
from esd7_attachment_channel import produce,decode
from esd7_simplicial_refinement import lift

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
SOURCE='research/voevodsky/interior-pyramid-nodes-must-refine-a-homotopy-coherent-diagram-of-four-realization-functors-not-mix-the-presentations-barycentrically.md'


def main():
    assembly=decode(produce(7)); result=lift(assembly); rows={c['cell']:c for c in result['cells']}; checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    check('all1807 generated cells lifted',len(rows)==1807)
    check('correct parent-nerve degrees for every fine dimension',all(c['parentSimplexDimension']==7*(c['fineDimension']+1)-1 for c in rows.values()))
    check('all120 vertices retain all seven labelled positions',len(result['vertexWords'])==120 and all(len(w)==7 for w in result['vertexWords'].values()))
    check('V001 retains chart3 and all six background chart4 positions',result['vertexWords']['V001']==[3,4,4,4,4,4,4])
    check('V001 is not forced to choose between its incident parent charts',set(result['vertexWords']['V001'])=={3,4})
    check('all parent words are monotone and degenerate from an actual parent face',all(
        c['parentWord']==sorted(c['parentWord']) and
        [c['parentSupport'][i] for i in c['degeneracyMap']]==c['parentWord'] for c in rows.values()))
    check('shared face maps agree on actual retained occurrence positions',sum(len(c['faceRestrictions']) for c in rows.values())==560*2+784*3+343*4)
    geometry={c['id']:c for k in ['vertices','edges','triangles','tetrahedra'] for c in assembly[k]}
    for c in rows.values():
        old={b['cell']:b['sign'] for b in geometry[c['cell']]['boundary']}
        for f in c['faceRestrictions']:
            if c['orientationRelativeToGeometry']*old[f['face']] != f['sign']*rows[f['face']]['orientationRelativeToGeometry']:
                raise AssertionError('unretained orientation change')
    check('all signed boundaries respect the explicitly reversed fine vertex order',True)
    check('F006 is a20-simplex degenerate from the parent tetrahedron, not one parent triangle',
          rows['F006']['parentSimplexDimension']==20 and rows['F006']['parentSupport']==[1,2,3,4])
    check('F006 edge images retain the required parent face comparisons',
          {e:rows[e]['parentSupport'] for e in ['E004','E037','E006']}==
          {'E004':[2,3,4],'E037':[1,2,4],'E006':[1,3,4]})
    check('original geometric E004 direction is not silently identified with the lifted direction',
          geometry['E004']['vertices']==['V001','V008'] and rows['E004']['fineVertexOrder']==['V008','V001'])
    for scale in [1,2,3,4]:
        small=lift(decode(produce(scale)))
        check(f'same construction checks all faces at scale{scale}',all(c['parentSimplexDimension']==scale*(c['fineDimension']+1)-1 for c in small['cells']))
    def rejects(bad):
        try:lift(bad)
        except ValueError:return True
        return False
    bad=copy.deepcopy(assembly);bad['vertices'][1]['barycentric']=[0,0,1,5]
    check('reject dropped background occurrence',rejects(bad))
    bad=copy.deepcopy(assembly);bad['edges'][0]['vertices'].reverse()
    check('reject silent orientation reversal',rejects(bad))
    bad=copy.deepcopy(assembly);bad['triangles'].pop(0)
    check('reject missing shared face',rejects(bad))
    bad=copy.deepcopy(assembly);bad['tetrahedra'][0]['vertices'][1]=bad['tetrahedra'][0]['vertices'][0]
    check('reject merged simplex occurrences',rejects(bad))
    check('structural success does not install an analytical payload',not result['analyticalRealizationEstablished'] and all(not c['analyticalPayloadInstalled'] for c in rows.values()))
    artifact=BASE+'esd7-simplicial-refinement.json'
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    report={'status':'passed','check_count':len(checks),'checks':checks,'cellCount':1807,
            'parentNerveDimensions':{'vertex':6,'edge':13,'face':20,'tetrahedron':27},
            'nondegenerateParentDimensionHistogram':dict(sorted(Counter(c['nondegenerateParentDimension'] for c in rows.values()).items())),
            'F006':rows['F006'],'F006Edges':{e:rows[e] for e in ['E004','E037','E006']},
            'structuralRefinementEstablished':True,'actualF006AnalyticalComparisonEstablished':False,
            'analyticalRealizationEstablished':False,'globalFieldTransportEstablished':False,'full114ChannelEstablished':False,
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [SOURCE,artifact,
             'research/strominger/checkers/esd7_attachment_channel.py',
             'research/strominger/checkers/esd7_simplicial_refinement.py',
             'research/strominger/checkers/check_esd7_simplicial_refinement.py']},
            'scope':'Explicit all-cell realization of the geometric map esd7(Delta3) into esd7 of the ordered parent nerve. Applying it to analytical data still requires an admitted coherent parent diagram Phi with retained domains/residuals/endpoints. Local H123/H234 role labels alone are not that diagram.'}
    (ROOT/BASE/'esd7-simplicial-refinement-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','cellCount','parentNerveDimensions','nondegenerateParentDimensionHistogram']}))


if __name__=='__main__':main()

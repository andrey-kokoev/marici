"""Source-parametric symbolic checks, not numerical or analytic proof closure."""
from pathlib import Path
from itertools import product
import copy
import hashlib
import json
from esd7_attachment_channel import produce,decode
from esd7_simplicial_refinement import lift
from esd7_strict_parent_evaluation import evaluate,normalize,transition,equivalent,validate_profile

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
PROFILE='research/strominger/contracts/esd7-strict-parent-profile.v1.json'


def main():
    profile=json.loads((ROOT/PROFILE).read_text()); refinement=lift(decode(produce(7)))
    evaluated=evaluate(refinement,profile); cells={c['cell']:c for c in evaluated['cells']}; checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    check('all1807 cells evaluated on the declared strict parent diagram',len(cells)==1807)
    check('all5421 endpoint and residual readout squares checked',evaluated['counts']['readoutSquares']==5421)
    check('all64 parent triangle identities including degenerate cases',all(
        equivalent(transition(a,b)+transition(b,c),transition(a,c),'V'+str(a)) for a,b,c in product(range(1,5),repeat=3)))
    check('all256 parent tetrahedral route identities including opposite directions',all(
        equivalent(transition(a,b)+transition(b,c)+transition(c,d),transition(a,d),'V'+str(a))
        for a,b,c,d in product(range(1,5),repeat=4)))
    check('F006 retains all21 parent positions',len(cells['F006']['parentOccurrences'])==21)
    check('F006 parent route reduces to S4 R1 in execution order',cells['F006']['reduction']['normalForm']==['R1','S4'])
    check('F006 endpoint and residual observables retain their own source pullbacks',
          [r['normalForm'] for r in cells['F006']['retainedReadoutSquares']]==
          [['R1','F:ell_plus'],['R1','F:ell_minus'],['R1','F:retained_residual']])
    check('background chart4 identities remain as occurrences after normalization',
          sum(p['chart']==4 for p in cells['F006']['parentOccurrences'])==18 and cells['F006']['identitiesSkippedInProgramOnly']==17)
    check('each face restriction checked at internal adjacencies rather than just endpoints',evaluated['counts']['restrictionAdjacencies']>1807)
    check('observable normalization does not equate distinct endpoint coordinates',not equivalent(['R1','F:ell_plus'],['R1','F:ell_minus'],'V1'))
    check('no analytical residual is assumed zero',all(not r['zeroAssumed'] for c in cells.values() for r in c['retainedReadoutSquares']))
    def rejects_profile(bad):
        try:validate_profile(bad)
        except ValueError:return True
        return False
    for name,key,value in [
        ('scalar fourth chart','chart4','scalar-finite-part'),
        ('independent completed bulk','carrierPolicy','independent-bulk-completion'),
        ('unsupported completion extension','completionExtension',True),
        ('inverse outside source image','inverseLawScope','all-geometric-operators'),
        ('dropped endpoint','retainedReadouts',['ell_plus','retained_residual']),
        ('discarded residual','retainedReadouts',['ell_plus','ell_minus'])]:
        bad=copy.deepcopy(profile);bad[key]=value
        check('reject '+name,rejects_profile(bad))
    try:normalize(['R1','S2','R3','S4'],'V1'); rejected=False
    except ValueError:rejected=True
    check('reject ill-typed cancellation across different charts',rejected)
    try:normalize(['R1','S2','R2','S4'],'V3'); rejected=False
    except ValueError:rejected=True
    check('reject wrong initial presentation',rejected)
    bad=copy.deepcopy(refinement)
    face=next(c for c in bad['cells'] if c['cell']=='F006');face['faceRestrictions'][0]['deleteParentPositions']=[]
    try:evaluate(bad,profile);rejected=False
    except ValueError:rejected=True
    check('reject dropped shared-face restriction',rejected)
    check('conditional chart evaluation is not promoted to intended witnesses or native transport',
          not evaluated['intendedAnalyticalWitnessBindingEstablished'] and not evaluated['native44TransportBindingEstablished'])
    artifact=BASE+'esd7-strict-parent-evaluation.json'
    (ROOT/artifact).write_text(json.dumps(evaluated,indent=2)+'\n',encoding='utf-8')
    inputs=[PROFILE,*profile['sources'],artifact,
            'research/strominger/checkers/esd7_attachment_channel.py',
            'research/strominger/checkers/esd7_simplicial_refinement.py',
            'research/strominger/checkers/esd7_strict_parent_evaluation.py',
            'research/strominger/checkers/check_esd7_strict_parent_evaluation.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,'counts':evaluated['counts'],
            'F006':cells['F006'],'conditionalStrictDiagramEvaluationEstablished':True,
            'sourceAnalyticIdentitiesFreshlyProved':False,'intendedAnalyticalWitnessBindingEstablished':False,
            'native44TransportBindingEstablished':False,'full114ChannelEstablished':False,
            'completionExtensionEstablished':False,
            'remainingGate':'Bind the evaluated strict diagram to the intended regulator/face-witness data and native44 transport on admitted joint-graph domains. Equality of recovered observer readouts alone does not identify proof-relevant analytical face modifications.',
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Exact typed symbolic corollary of the declared source inverse identities on correlated essential images. Not numerical operator data, an independent proof of source analytic identities, or the intended native/analytical witness identification.'}
    (ROOT/BASE/'esd7-strict-parent-evaluation-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','counts','conditionalStrictDiagramEvaluationEstablished','intendedAnalyticalWitnessBindingEstablished']}))


if __name__=='__main__':main()

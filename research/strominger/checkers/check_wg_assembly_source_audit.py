"""Root compatibility audit: common schedule/energy source, relation boundary.

This does not declare root assembly from independently passing examples.
"""
import contextlib
from dataclasses import replace
import io
import json
from pathlib import Path
import runpy
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
with contextlib.redirect_stdout(io.StringIO()):
    e=runpy.run_path(str(ROOT/'research/strominger/checkers/check_energy_continuation_instance.py'))
ci=e['interface']; schedule=ci['schedule']; a=schedule['a']; control=e['control']; S=e['S']
from shared_leg_control_ports import vector_legs, response_field

def field(rows):
    return S.ImmutableMatrix([list(sum(r.value,())) for r in rows])

def assignment(legs):
    values=dict(a['values'])
    for role,i,matrix in legs:
        values[f'{role}{i}']=tuple(tuple(matrix[r,c] for c in range(2)) for r in range(2))
    return values

checks={
    'actual137_response_fields_match':field(a['rows'])==e['F'],
    'actual_direct_references_match':a['values']['d']==control['fixture']['m']['values']['d'],
}
commands=[('gain',S.Integer(0)),('gain',S.Rational(1,2)),
          ('gain',S.Rational(2,3)),('gain',S.Integer(1)),('drift',None)]
for policy,nodes in schedule['examples'].items():
    root=nodes[0]
    for command in commands:
        kind,q=command
        leg_operator=control['leg_step'] if kind=='drift' else control['Pleg']+q*control['Qleg']
        legs=vector_legs(leg_operator*control['l0'],control['legs'])
        updated=replace(root,context=replace(root.context,assignment=assignment(legs)))
        right6=schedule['generate'](updated)
        right4=schedule['vertical'](schedule['vertical'](right6))
        terminal=schedule['terminal'](right4)
        rows=a['verify'](terminal.binding)
        lifted=e['source_step'](e['initial'],command)
        assert field(rows)==response_field(legs)==lifted.field
        assert e['project'](lifted)==e['task_step'](e['project'](e['initial']),command)
        assert terminal.binding.direct_value==a['values']['d']
        assert right4.context.policy==policy
        assert a['leaves'](a['unindex'](terminal.view))==rows
    checks[policy+'_same_source_gain_and_drift_square']=True

# Concrete failed common-source candidate: retain schedule/energy fields,
# but replace the relation witness by its terminal recorder value.
r=ci['relation']; v=r['p4'].product
z=r['Arrow'](v.start,v.end,())
def naive_assembly(relation_arrow):
    return (e['initial'].field,a['values']['d'],relation_arrow.start,relation_arrow.end,
            tuple(sorted(r['observe'](relation_arrow).items())))
assert naive_assembly(v)==naive_assembly(z)
probe=v.terms[0][0]
assert dict(v.terms)[probe]!=dict(z.terms).get(probe,0)
checks['observation_only_root_assembly_loses_relation_detector']=True

# These typed-source witnesses still live in different declared source algebras.
# A missing adapter is an explicit obligation, not a universal impossibility.
assert r['actual_action']!=r['graded_action']
checks['relation_adapter_must_preserve_actual_cross_layer_action']=True
assert all(checks.values())
out={'schema':'marici.wg-assembly-source-audit.v1','status':'pass','checks':checks,
     'constructed':'actual schedule/energy source and tested gain/drift square',
     'rejected_candidate':'terminal-observation-only relation attachment in root assembly',
     'root_assembled':False,
     'remaining_obligation':'explicit common-source adapter preserving relation product detector, balancing and cross-layer action alongside the schedule source; no such adapter inferred from shared interface or dimensions',
     'scope':'exact fixture matrices and declared operations; not unique policy or physical calibration'}
(ROOT/'research/strominger/results/wg-assembly-source-audit-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

# /// script
# dependencies = ["sympy"]
# ///
"""Task-level repair of branch-blind promoted means, not endpoint selection."""
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys
import sympy as S

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from branch_response_summary import summarize, combine, read, recover
ROOT=HERE.parent
OUT=ROOT/'results/branch-response-summary.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    task=runpy.run_path(str(HERE/'check_T9_branch_task_binding.py'))
m=task['m']; algebra=m['m']; rows=m['source']; reference=m['physical_reference'].value
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def selector(row): return row.source[0]
def direct(input_rows): return summarize(input_rows,selector,algebra)
def staged(final):
    # Simulates propagation of ADDITIVE statistics, not recovering branches
    # from only final means. The first level reads leaves once.
    first_summaries={}
    for family in final:
        for child in family.members:
            first_summaries[child.label]=direct(m['leaves']((child,)))
    final_summaries=[combine([first_summaries[child.label] for child in family.members],algebra) for family in final]
    return combine(final_summaries,algebra)
check('original-branch-task-audit-fresh',task['result']['verification_status']=='pass')
source_summary=direct(rows); source_read=read(source_summary,reference,algebra)
check('original-masses-unchanged',source_summary.masses==(121,16))
check('new-reader-keeps-existing-J4',source_read['J4']==m['read_at_four'](m['indexed'](rows,'target')))
check('new-reader-recovers-both-original-branch-residuals',dict(zip(('a','s'),source_read['branch_residuals']))==task['original_read'])
check('minimal-interface-recovery',recover(source_read['J4'],source_read['contrast'],source_read['masses'],algebra)==source_read['branch_residuals'])
profiles={}
for policy in ('inherited','common','endpoint-only'):
    final=task['quotient'](rows) if policy=='endpoint-only' else m['incoming_promotion'](m['incoming_promotion'](rows,1,policy),2,policy)
    summary=staged(final)
    check('additive-summary-square/'+policy,summary==source_summary)
    check('outer-reader-square/'+policy,read(summary,reference,algebra)==source_read)
    profiles[policy]={'rows':len(final),'same_outer_branch_readout':True}
# Retained source/target presentations reorder packets but change no statistic.
for column in ('source','target'):
    view=m['indexed'](rows,column)
    check('summary-presentation-square/'+column,combine([direct(group) for group in view.values()],algebra)==source_summary)
# Test the exact earlier shared-leg hostile. Old16 means and J4 agree, new
# contrast exposes its actual branch difference WITHOUT reopening members.
base=read(staged(task['base_final']),reference,algebra)
changed=read(staged(task['changed_final']),reference,algebra)
check('hostile-old-J4-still-identical',base['J4']==changed['J4'])
check('hostile-now-distinguished-at-outer-interface',base['contrast']!=changed['contrast'])
check('hostile-exact-contrast-shift',algebra['add'](changed['contrast'],algebra['scale'](-1,base['contrast']))==algebra['scale'](F(137,440),algebra['I']))
check('hostile-branch-means-recovered',recover(changed['J4'],changed['contrast'],changed['masses'],algebra)==changed['branch_residuals'])
# General positive masses and supplied values, not a weight calibrated to J4.
weighted=tuple(replace(row,mass=1+(i%5)) for i,row in enumerate(rows))
weighted_read=read(direct(weighted),reference,algebra)
check('nonuniform-member-masses-recovery',recover(weighted_read['J4'],weighted_read['contrast'],weighted_read['masses'],algebra)==weighted_read['branch_residuals'])
check('nonuniform-common-promotion-square',staged(m['incoming_promotion'](m['incoming_promotion'](weighted,1,'common'),2,'common'))==direct(weighted))
# For full2x2 matrix branch means the task has8 linear coordinates. J4
# retains4. Each scalar coordinate has the same invertible two-branch map.
w=S.Rational(121,137); one=S.eye(4)
J=S.Matrix.hstack(w*one,(1-w)*one)
D=S.Matrix.hstack(one,-one)
combined=J.col_join(D)
check('J4-rank4',J.rank()==4)
check('branch-task-needs8-independent-linear-coordinates',combined.rank()==8)
check('one-contrast-matrix-is-minimal-linear-completion',combined.det()==1)
check('new-observer-does-not-select-endpoint-policy',all(profile['same_outer_branch_readout'] for profile in profiles.values()))
# A missing branch is not fabricated as zero mean.
try:
    read(direct(tuple(row for row in rows if selector(row)=='a')),reference,algebra)
except ValueError:
    check('empty-branch-mean-rejected',True)
else:
    raise AssertionError('Undefined state mean was fabricated')
def matrix(a): return [[str(v) for v in row] for row in a]
result={
 'schema':'marici.nima.branch-response-summary.v1','verification_status':'pass','checks':checks,
 'original_outer_interface':{'masses':source_read['masses'],'J4':matrix(source_read['J4']),
                             'contrast':matrix(source_read['contrast'])},
 'candidate_profiles':profiles,
 'recovery_formulas':['J_arrow=J4+(m_state/M)*contrast','J_state=J4-(m_arrow/M)*contrast'],
 'minimality':'For the declared unrestricted full matrix branch-mean task, J4 has rank4; one4-coordinate contrast is a minimal linear completion to rank8.',
 'hostile_contrast_shift':'137/440 I',
 'positive_result':'Branch-resolved OUTER response is preserved using additive summaries under all three tested retained endpoint policies.',
 'selection_boundary':'This extends the declared observation interface. It does not identify it with unchanged J4 alone, choose a physical detector, or select T9 wiring.',
 'intended_T9_identified':False,'objective_complete':False,
 'next_input':'If endpoint contexts themselves must be protected, declare that routing contract separately. If only branch mean observations are required, all tested policies now satisfy the outer reader contract.',
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'branch_response_summary.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} additive outer branch-summary checks')
print('J4 plus one contrast matrix recovers both branch means; staged summaries preserve all original masses.')
print('The earlier shared-leg hostile is distinguished, but this observation contract still selects no endpoint policy.')

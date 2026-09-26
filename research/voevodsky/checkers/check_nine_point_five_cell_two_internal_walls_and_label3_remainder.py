"""Five-cell full trace removes both EB internal poles but keeps a nonzero label3 component."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_five_cell_lower_internal_full_trace_cancellation as five
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
trace=five.trace;chamber=five.chamber;prior=five.prior
vars=trace.vars;w2,w4,w5,w6,w7,w8,t,u=vars
upper=chamber.threshold_high
P,root,J=five.inverse_at(upper)
assert all(P[v]!=0 for v in vars[:6]) and P[u]!=0 and P[t]-P[u]!=0 and J!=0
assert any(r['wall']=='upper' and r['other_E_sheet_on_same_source_facet'] for r in prior.rows)
assert any(r['wall']=='lower' and not r['other_E_sheet_on_same_source_facet'] for r in prior.rows)
assert any(r['boundary']=='interior_E_target_lower_wall' for r in five.neighbor.checks)
assert s.factor(five.bir.cell[:,[1,3]].det()-w2*w4/t)==0 # physical 3 and 5 in retained indexing
p=dict(zip(vars,(1,1,1,1,1,1,3,2)))
Y=trace.D.subs(p)*five.Z
H=Y[:,:2];B=H.inv()*Y[:,2:]
h=five.Z[:,:2]
F,rootF,JF=five.inverse_at(s.S.One)
assert JF!=0
rhoF=s.S.One/(s.prod(F[v] for v in vars[:6])*F[u]*(F[t]-F[u]))
minorF=s.factor(five.bir.cell[:,[1,3]].det().subs(F))
Fcomponent=s.factor(rhoF*minorF**4*(five.bir.cell.subs(F)*h).det()**4/JF)
four=s.Rational(next(r['complete_four_cell_chi3_power4_chi5_power4']
                     for r in trace.rows if r['target']=='first'))
five_total=s.factor(four+Fcomponent)
assert Fcomponent!=0 and five_total!=0
report={'schema':'marici.nima.nine-point-five-cell-two-internal-walls-and-label3-remainder.v1',
 'passed':True,'upper_wall_E_family_e':str(upper),
 'upper_wall_F_B_unique_inverse_source':{str(v):str(P[v]) for v in vars},
 'upper_wall_F_B_source_and_target_regular':True,
 'five_cell_meromorphic_simple_superpoles_at_both_EB_internal_walls_cancel':True,
 'arbitrary_Y_common_E_target_e_one':{'four_cell_full_chi3_power4_chi5_power4_trace':str(four),
  'F_B_one_sheet_chi3_power4_chi5_power4_trace':str(Fcomponent),
  'five_cell_full_chi3_power4_chi5_power4_trace':str(five_total),
  'five_cell_trace_nonzero':True},
 'consequence':'Adding the unique F_B rational trace to E,E_B,E_C,E_D cancels the LOWER EB interior full-superform simple pole, while F_B is regular at the UPPER wall where the nonpositive E second sheet already cancels EB. Yet the complete five-cell chi3^4 chi5^4 meromorphic trace is nonzero at an exact positive common target and thus generically nonzero.',
 'scope':'Two exact interior poles on one E target curve and one full label3 witness. Other target poles, cells and the complete n9 canonical form remain unclassified.'}
(OUT/'nine-point-five-cell-two-internal-walls-and-label3-remainder.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'both_internal_EB_poles_cancel_in_five_cell_meromorphic_sum':True,
 'five_cell_full_label3_trace_nonzero':True},indent=2))

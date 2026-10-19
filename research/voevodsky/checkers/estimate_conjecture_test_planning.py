"""Dated assistant elicitation, plus dependency-aware next-test ranking.
Numbers are subjective planning judgments, not scientific receipts.
"""
import json
from check_conjecture_test_planning import MODEL, ROOT, load, validate, PATHS

# accepted, rejected, assistant effort, rationale
ESTIMATES = {
 'parent:formulation-and-quantifiers': (.65,.10,5,'Definitions can be frozen, but infinite coverage and resources require explicit choices.'),
 'parent:common-process-structure': (.35,.25,10,'Concrete constructors exist; native versus imported laws remain the main gap.'),
 'parent:identity-continuation-coherence': (.35,.30,10,'Equal-readout controls exist; dependent and higher transport are substantial missing witnesses.'),
 'parent:mathematical-realization': (.30,.20,12,'Bounded examples are available; dependent and completion overlaps are not assembled.'),
 'parent:uf-and-foundational-recovery': (.15,.25,16,'No completed interpretation; dependent laws and conservativity are expensive gates.'),
 'parent:physical-realization': (.15,.35,16,'Source binding and independent physical justification are missing, beyond analytic constructions.'),
 'parent:same-source-cross-realization': (.25,.30,12,'Shared-source requirements are stronger than separate successful realizations.'),
 'parent:universal-extension-and-assembly': (.10,.30,20,'Finite successes do not supply universal generation or coverage principles.'),
 'parent:common-foundations': (.15,.25,10,'Even conditional on inputs, source bindings and assembly scopes can fail independent review.'),
 'math:stagewise-mathematical-interface': (.65,.10,5,'Existing examples give concrete typing constraints; dependent transport remains unresolved.'),
 'math:finite-domain-wg-example': (.65,.25,3,'Pilot exists; its imported laws can be audited directly rather than regenerated.'),
 'math:rh-mathematical-realization-example': (.65,.20,4,'Operation bridges exist, but overlap and completion conventions require review.'),
 'math:mathematical-realization-example-assembly': (.65,.20,4,'Conditional on reviewed examples, mismatched identity semantics are the main risk.'),
 'compatibility:common-witness-comparison-interface': (.65,.15,5,'Domains and comparison routes can be fixed; physical premises must be separated.'),
 'compatibility:rh-same-source-compatibility-example': (.30,.35,10,'No shared-source continuation/form assembly yet; known kernels stress the comparison.'),
 'compatibility:physical-pilot-comparison-example': (.40,.35,8,'Finite results exist, but failed bridges and carrier incompatibility must survive the audit.'),
 'compatibility:same-source-compatibility-example-assembly': (.50,.25,6,'Conditional overlap review is feasible, but higher compatibility is unfinished.'),
 'rh:rh-stage-dictionary': (.80,.05,2,'Existing stages/maps are explicit; main risk is incomplete indexing or concealed source choices.'),
 'rh:rh-operation-composition-squares': (.65,.20,3,'Finite intertwiners exist, but uncovered compositions may fail.'),
 'rh:rh-identity-continuation-transport': (.50,.30,4,'Retained reconstructions exist; continuation and attachment binding need review.'),
 'rh:rh-analytic-domain-completion-transport': (.45,.25,5,'Domain/topology extension obligations are substantive despite existing analytic constructions.'),
 'rh:rh-stagewise-interface': (.75,.15,2,'Conditional on four constructed children, review overlaps and assemble; child proof effort is excluded.'),
 'rh:channel-carrier-source-map': (.30,.40,8,'No common generator dictionary is established; native ticks are already incompatible.'),
 'rh:one-dimensional-source-selection': (.55,.25,5,'Selection and symmetric quotient can be compared concretely, with explicit kernel accounting.'),
 'rh:successor-form-candidate': (.25,.55,6,'Two independent form obstructions constrain repairs; early rejection is more likely than a justified survivor.'),
 'rh:weil-form-comparison': (.15,.45,12,'Surviving kernels alone do not identify prime/gamma/endpoint terms or completion.'),
 'rh:same-source-continuation-comparison': (.40,.35,8,'Conditional source maps help, but retained-state continuation squares are not supplied.'),
 'rh:rh-math-assembly': (.75,.15,3,'Conditional on the typed interface, this is bounded composition rather than form repair.'),
 'rh:rh-cross-realization-assembly': (.55,.25,5,'Conditional on three constructed witnesses, overlap conventions can still disagree.')}


def main():
    nets = {k: load(p) for k,p in PATHS.items()}
    m = load(MODEL)
    rows = {r['id']:r for r in m['conjectures']}
    open_ids = {k for k,r in rows.items() if r['probability']['status'] != 'not_applicable'}
    assert open_ids <= set(ESTIMATES)
    for key,(a,b,effort,why) in ESTIMATES.items():
        if key not in open_ids:
            continue
        r = rows[key]
        r['test'].update(protocol_status='specified',
            protocol='Within the stated assistant-effort budget, inspect current evidence, attempt the next action, run relevant checks, and review against the recorded acceptance/falsifier. Stop at budget exhaustion; report inconclusive if neither gate is met.',
            stopping_rule='Acceptance witness, scoped counterexample, or exhaustion of assistant-effort budget; no automatic success from dependencies.')
        conditioning='Current recorded evidence; declared prerequisites and external reviewed inputs are assumed available for blocked tasks. One budget-limited attempt, not unlimited research.'
        basis={'estimator':'assistant','date':'2026-10-13','method':'subjective task-scope elicitation, not calibrated frequency','rationale':why}
        r['probability'].update(status='estimated', values={'accepted':a,'rejected':b,'inconclusive':round(1-a-b,2)},
            conditioning=conditioning, uncertainty='Low-confidence forecast; differences below 0.10 should not be treated as robust. Scope changes require re-estimation.', basis=basis,
            reason='Assistant forecast for bounded next test, not theorem confidence.')
        r['test_cost'].update(status='estimated',assistant_effort_units=effort,basis=basis,
            reason='Estimated effort budget for one attempted test, not a promised completion cost.')
    validate(m,nets)
    (ROOT/MODEL).write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
    from check_conjecture_workbench import main as refresh_workbench
    refresh_workbench()


if __name__=='__main__':main()

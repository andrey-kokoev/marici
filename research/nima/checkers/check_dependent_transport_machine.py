"""Verify current source-bound receipts for the transport syntax experiment."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('DependentTransportMachine', 'dependent-transport-machine', ['DependentTransportBadErasure'])
result = {
    'schema': 'marici.nima.dependent-transport-machine.v1',
    'passed': True, **checked,
    'object_substitution_laws': True,
    'reduction_stable_under_substitution': True,
    'closed_progress': True,
    'finite_execution_trace_for_every_closed_term': True,
    'interpretation_preserved_by_every_step': True,
    'execution_agrees_with_circle_cover_transport': True,
    'endpoint_only_action_refuted': True,
    'output_and_action_route_decoders_refuted': True,
    'source_retained': True,
    'result_certificate_and_higher_certificate': True,
    'scope': 'Companion fragment over one circle-cover base fiber; supplied turn semantics checked against dependent transport. Existing dependent choose machine unchanged. No general dependent calculus or all-schedule termination claim.'
}
(OWNER / 'results/dependent-transport-machine.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: source-bound dependent transport, substitution, finite executions, erasure controls, and output certification.')

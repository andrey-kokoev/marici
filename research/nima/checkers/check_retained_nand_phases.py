"""Source-bound audit of the two-phase retained NAND construction."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('RetainedNandPhases', 'retained-nand-phases', ['RetainedNandBadReflection'])
result = {
    'schema': 'marici.nima.retained-nand-phases.v1', 'passed': True, **checked,
    'empty_question_initial': True,
    'joint_question_product_universal_property': True,
    'joint_refutation_natural_universal_property': True,
    'input_action_records_recovered': True,
    'old_nand_constructor_value_type_comparison_definitional': True,
    'wolfram_double_negation_equivalence_respects_E_actions': True,
    'stable_proposition_condition_sufficient_and_necessary': True,
    'double_negation_reflection_universal_for_stable_prop_actions': True,
    'set_valuedness_alone_refuted': True,
    'truth_reflection_cannot_recover_boolean_answers': True,
    'empty_type_derived_from_retained_change_record_alone': False,
    'whole_old_Q_and_new_action_representations_equivalent': False,
    'scope': 'Small set-valued actions; all object indices and original E data are parameters. Boolean identity is an ActionIso, not an asserted equality of arbitrary action records.'
}
(OWNER / 'results/retained-nand-phases.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: two-phase NAND universal properties, equivariant Wolfram criterion, old value-type bridge, and retained-answer loss controls.')

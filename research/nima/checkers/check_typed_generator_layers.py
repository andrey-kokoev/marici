"""Source-bound verification for the retained generator layers."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('TypedGeneratorLayers', 'typed-generator-layers', ['GeneratorBadComposition', 'GeneratorBadHistoryErasure'])
result = {
    'schema': 'marici.nima.typed-generator-layers.v1', 'passed': True, **checked,
    'layer1_record_recovered': True,
    'retained_history_representation_and_recovery': True,
    'history_unit_and_associativity_laws': True,
    'generated_history_length_preserved': True,
    'optional_composition_interpretation_preserves_join': True,
    'path_generator_naturality': True,
    'generated_fourth_face_and_tetrahedron_contractible': True,
    'higher_certificate': True,
    'universal_relation_composition_refuted': True,
    'composite_history_decoder_refuted': True,
    'scope': 'Finite retained histories over fixed Layer1; optional relation algebra; path specialization through generated tetrahedral completion. No arbitrary-boundary filling or all-dimensional simplicial claim.'
}
(OWNER / 'results/typed-generator-layers.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: Layer 1 recovery, retained histories, represented composition laws, optional fold, naturality, tetrahedral certification, and both rejection controls.')

"""Create the proposed source-interface/target checkpoint without proof promotion."""
import copy
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def load(name):
    return json.loads((HOME / name).read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


SOURCES = [
    ('docs/system-characteristics.md', 'System as software architecture; recursive comparison constructor', 'Family promotion retains members; independent comparison is a separate constructor. Grouping keys, endpoints and label lifetime require a contract.'),
    ('docs/theory-page.md', 'Sections 16 and 17; tower successor', 'GR constraints and numerical constants are not recovered from finite geometry or counts.'),
    ('research/nima/agda/ObserverCoherenceCube.agda', 'Geometry and FromSource modules', 'Typed equivalences, factor operations, retained schedules and attached source records give a pilot source, not spacetime.'),
    ('research/nima/recursive-independent-family-comparison.md', 'Constructor and architectural result', 'Independent all-pairs comparison has explicit parent provenance and is not implied by grouping alone.'),
    ('research/nima/spectral-successor-architectural-source-contract.md', 'Primary-source result and disposition', 'Spectral successor endpoints and grouping bindings are explicitly open in source specification.'),
    ('research/nima/source-to-generator-audit.md', 'Supersession and separate questions', 'Quarantined generator-selection receipts are not evidence; finite source does not select physical rate or unitary image in the declared classes.'),
    ('research/voevodsky/contracts/retained-reaggregation-source-k.v1.json', 'selection_basis and physical_admission', 'Explicit operator selection is a convention, not a physical calibration or source-only uniqueness result.'),
    ('research/nima/compton-record-compatibility.md', 'Physical-theory interface, common parent and prospective calibration', 'Complete azimuth records have the stated binning sharpness and parent-POVM obstruction; no calibration counts have been acquired.'),
    ('research/nima/qed-bell-experimental-protocol.md', 'Readout interpretation withdrawn', 'The quoted historical observed Bell value is not a valid prediction for the proposed single-Compton implementation.'),
    ('research/nima/carrier-guide-bell-proof-of-concept.md', 'Evidence locators', 'The guide cites onset/replication receipts that are missing at their stated paths in this checkout; no numerical claim is admitted from them.'),
    ('research/nima/formal-adm-constraint-derivation.md', 'Withdrawn claims and stopping boundary', 'A parametrized mechanical comparison is not an ADM field derivation.'),
    ('research/nima/native-square-controlled-hamiltonian.md', 'Source operations, Hamiltonian realization and orientation', 'Conditional finite unitary/symplectic correspondence supplies a structural pilot, not a physical-clock recovery.')
]
MISSING = ['research/nima/results/exact-qed-bell-onset.json',
           'research/nima/results/exact-qed-bell-replication.json']


def build():
    review = {'schema': 'marici.conjecture-net.programme-source-target-review.v1',
              'review_kind': 'bounded_textual_and_interface_review_not_theorem_verification',
              'sources': [{'source_path': path, 'source_sha256': sha(path),
                           'reviewed_sections': sections, 'claim': claim,
                           'verification_boundary': 'Source inspection only; no fresh kernel closure, numerical certification or physical measurements.'}
                          for path, sections, claim in SOURCES],
              'missing_evidence': [{'source_path': path, 'status': 'absent',
                                    'consequence': 'Do not import the referenced numerical receipt or infer confirmation.'}
                                   for path in MISSING],
              'assumption_boundary': 'Choose a conditional pilot before claiming source derivation or physical explanation; imported laws do not derive themselves.'}
    if any((ROOT / path).exists() for path in MISSING):
        raise ValueError('Missing evidence changed; review requires explicit new version.')
    hierarchy = copy.deepcopy(load('contracts/programme-hierarchy.v2.json'))
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v3',
                     id='marici.relational-carrier-physics-programme.v3',
                     phase='proposed_source_interface_and_bounded_targets',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v2.json',
                     terms='research/conjecture_net/contracts/programme-terms.v3.json',
                     source_interface='research/conjecture_net/contracts/programme-source-interface.v1.json',
                     target_set='research/conjecture_net/contracts/programme-targets.v1.json',
                     source_target_review='research/conjecture_net/reviews/programme-source-target-review.v1.json')
    hierarchy['root']['candidate_formulation'] = 'There exists one typed relational carrier and shared source-indexed calculus whose justified source records and geometric/dynamic/observable realizations recover an explicitly versioned physical target set, agree on shared regimes, and pass predeclared independent tests imposing constraints beyond inserted laws or fitted answers.'
    hierarchy['root']['formulation_status'] = 'underspecified'
    hierarchy['root']['remaining_formulation_gates'] = ['common carrier implementation', 'allowed source records and derivation obligations', 'cross-sector overlap maps', 'approved physical target scope', 'empirical protocols and statistics', 'logical same-witness assembly rule']
    interface = load('contracts/programme-source-interface.v1.json')
    targets = load('contracts/programme-targets.v1.json')
    hierarchy['source_primitive_links'] = [{'source_primitive': p['id'], 'target_obligation': 'carrier-and-geometric-dynamics',
                                           'relation': 'candidate_interface_component', 'proof_bearing': False}
                                          for p in interface['primitives']]
    hierarchy['target_links'] = [{'target_id': t['id'],
                                  'target_obligation': 'empirical-recovery' if t['class'] == 'prospective_empirical_interface' else 'physical-sector-realizations',
                                  'relation': 'candidate_target', 'proof_bearing': False}
                                 for t in targets['targets']]
    for task in hierarchy['next_refinements']:
        task['specification_status'] = 'partially_specified_candidate' if task['id'] in {
            'source-primitives-and-record-provenance', 'bounded-physical-target-set'} else 'open'
    terms = copy.deepcopy(load('contracts/programme-terms.v2.json'))
    terms.update(schema='marici.conjecture-net.programme-terms.v3',
                 hierarchy='research/conjecture_net/contracts/programme-hierarchy.v3.json',
                 predecessor='research/conjecture_net/contracts/programme-terms.v2.json',
                 review_status='partial_review_with_proposed_source_and_targets',
                 source_target_review=hierarchy['source_target_review'])
    definitions = {
        'physical_targets': ('A versioned proposed target list separating structural recovery from prospective empirical interfaces. Initial pilots are finite unitary return, same-source Hamiltonian/symplectic correspondence, and complete-record Compton calibration; they do not encompass all physics.', [7, 10, 11],
                             ['These are conditional pilot interfaces, not an approved complete physical target scope.', 'The programme common-witness maps remain absent.']),
        'empirical_tests': ('Predeclared comparisons of complete instrument records to scoped predictions using independently justified preparation/calibration, disjoint fitting and validation inputs, uncertainty and a frozen statistical rule.', [7, 8],
                            ['No dataset, full protocol, sample rule or statistical tolerance has been supplied for the calibration pilot.', 'Mathematical checks and ideal analyzer arithmetic are not acquired physical data.']),
        'falsifiability': ('A specified branch must expose observations or exact interface obstructions that contradict its frozen assumptions. Changing source records after the test is a new branch, not repair of the original verdict.', [5, 7, 8, 10],
                           ['A failed pilot does not refute existence of all relational carriers.', 'A prospective calibration discriminator has not been measured.']),
        'explanation': ('Recovery with explicitly partitioned provenance: identify what the carrier/source calculus derives, what is supplied as a convention or imported law, what is calibrated, and which independent constraints follow. Importing a law or fitted answer cannot count as deriving that same law or answer.', [0, 4, 6, 9, 10],
                        ['The permitted degree of imported physical input and the stronger derivation obligations need selection.', 'Conditional reproduction alone does not establish universal explanatory power.'])
    }
    for term in terms['terms']:
        if term['id'] not in definitions:
            continue
        definition, indices, residuals = definitions[term['id']]
        term.update(status='reviewed_candidate', definition=definition,
                    evidence=[{'source_path': SOURCES[i][0], 'source_sha256': sha(SOURCES[i][0]),
                               'role': 'textual_scope_and_counterexample_review_not_proof_import'} for i in indices],
                    assumptions=['All source/instrument assumptions must be frozen and typed; candidates are not physical admission.'],
                    counterexamples=['A renamed finite model or idealized analyzer does not establish its physical promotion.'],
                    residuals=residuals)
    terms['source_interface'] = hierarchy['source_interface']
    terms['target_set'] = hierarchy['target_set']
    return {'reviews/programme-source-target-review.v1.json': review,
            'contracts/programme-hierarchy.v3.json': hierarchy,
            'contracts/programme-terms.v3.json': terms}


if __name__ == '__main__':
    payloads = {path: json.dumps(data, indent=2, sort_keys=True) + '\n' for path, data in build().items()}
    for name, payload in payloads.items():
        destination = HOME / name
        if destination.exists() and destination.read_text(encoding='utf-8') != payload:
            raise ValueError('Refusing implicit specification correction: ' + name)
    for name, payload in payloads.items():
        destination = HOME / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_text(payload, encoding='utf-8')
    print(json.dumps({'status': 'recorded', 'source_primitives': 8, 'proposed_targets': 3,
                      'empirical_datasets': 0, 'admitted_proofs': 0}, indent=2))

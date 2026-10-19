"""Materialize the bounded first repository-review checkpoint.

This records textual scope/definitions and candidate links, never proof admission.
Existing versioned checkpoints cannot be silently overwritten.
"""
import copy
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def load(name):
    return json.loads((HOME / name).read_text(encoding='utf-8'))


def pin(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


SOURCES = [
    ('research/nima/bare-carrier-naturality-no-go.md', 'A proper nonzero subspace cannot be selected naturally from bare vector spaces under all linear maps.', 'Bare vector spaces with full naturality; not every enriched relational carrier.', 'Written argument with reported exact finite control; not re-executed here.'),
    ('research/nima/carrier-generated-sector-interface-falsifier.md', 'A shared source-indexed calculus is proposed after bare-carrier sector selection fails.', 'Carrier plus admitted coefficient/support/boundary/pairing records.', 'Written synthesis and proposed surviving conjecture; not a general generation theorem.'),
    ('research/nima/carrier-categorical-self-realization-falsifier.md', 'Readout-only reconstruction fails; joint faithfulness of authorized probes is the surviving candidate.', 'Source-indexed interface category and predeclared probe family.', 'Written proposal and reported counterexamples; no universal reconstruction theorem.'),
    ('research/nima/sector-completeness-needs-carrier-action-observation-and-estimate.md', 'Carrier splitting, action, observation and uniform completion estimates are independent gates.', 'Multisector linear models and declared completion topology.', 'Written exact finite hostiles; no universal physical completeness claim.'),
    ('research/nima/tick-full-structure-classification.md', 'At fixed Bool source, the full existing Tick is equivalent to its two ordered schedule tags.', 'The existing Bool/notEquiv specialization only.', 'Reported fresh safe Agda theorem; not newly kernel-checked by this review.'),
    ('research/nima/uniform-local-core-proof.md', 'A uniform native-flip spectral construction exists after declared complex linearization and analysis.', 'Finite factor involutions, standard complex semantics; existence, not unique selection.', 'Written all-time proof with exact checks. Its old operational-open statement is historical; use the accepted operational export for current status.'),
    ('research/nima/native-square-controlled-hamiltonian.md', 'Hamiltonian realization exists, while corner data do not select a unique generator and return orientation matters.', 'Four-state declared analytic enlargement; dimensionless parameters.', 'Reported formal source audit and exact Hamiltonian checks; no physical clock or energy calibration.'),
    ('research/nima/ten-carrier-spatial-bridge-finding.md', 'Ordered path data carries spatial information lost by the six-slot summary; a direct face-module embedding was withdrawn.', 'Finite occurrence/path model and its specified spatial readout.', 'Reported finite enumeration; no spacetime derivation or general path-to-geometry bridge.'),
    ('research/flavor/flavor-anchored-two-matching-relational-carrier.md', 'Two relations on shared ports remove reflection automorphisms without selecting numerical flavor constants.', 'Anchored three-port matching model.', 'Reported exact symmetry audit; not a microscopic physical flavor selector.'),
    ('research/nima/contracts/completion-refinement-conjecture-net.v1.json', 'The operational whole-return target is recorded ++ at an explicitly accepted mixed level.', 'Native spectral witness operational completion refinement.', 'Source contract record; live export must independently resolve before evidential use.'),
    ('research/nima/contracts/current-problem-conjecture-net.v1.json', 'The clarified local-core plus same-witness external-return existence route is represented in the predecessor net.', 'Declared standard-C4 existence semantics.', 'Source contract record, not fresh theorem verification.'),
    ('research/voevodsky/contracts/retained-reaggregation-conjecture-net.v1.json', 'Neutral retained-record reaggregation comparison is separated from physical admission and selection.', 'Common inputs/reference and distinguishing observable; spacetime and physical seconds excluded.', 'Source contract and objective review; no current outcome inferred.'),
    ('research/flavor/contracts/flavor-interaction-net-state.v1.json', 'The integer/pole branch tracks source, calibration and gain gates rather than a physical selector.', 'The declared flavor branch and instrument interfaces.', 'State-contract review; constructed nodes are not automatically proof-attempt outcomes.'),
    ('research/voevodsky/contracts/theta-rh-cubical-scc-overlay.v1.json', 'The RH overlay distinguishes constructors, open interfaces and realization gates.', 'Arithmetic/theta programme, not itself an empirical physical target.', 'State-contract review; no RH proof or authority/latest-version selection inferred.')
]


def build():
    review = {'schema': 'marici.conjecture-net.programme-term-review.v1',
              'review_id': 'bounded-source-indexed-carrier-review.v1',
              'review_kind': 'textual_repository_review_not_theorem_verification',
              'reviewed_terms': ['carrier', 'geometry', 'dynamics', 'observables'],
              'sources': [{'source_path': p, 'source_sha256': pin(p), 'claim': claim,
                           'scope': scope, 'verification_level': level}
                          for p, claim, scope, level in SOURCES],
              'coherence_obligations': ['attachment transport', 'route/coherencer compatibility', 'readout descent'],
              'boundary': 'Bounded review; no universal source calculus, physical recovery, or proof-supplying net link is admitted.'}
    terms = copy.deepcopy(load('contracts/programme-terms.v1.json'))
    terms['schema'] = 'marici.conjecture-net.programme-terms.v2'
    terms['hierarchy'] = 'research/conjecture_net/contracts/programme-hierarchy.v2.json'
    terms['predecessor'] = 'research/conjecture_net/contracts/programme-terms.v1.json'
    terms['review_status'] = 'partial_candidate_review'
    terms['review'] = 'research/conjecture_net/reviews/programme-term-review.v1.json'
    definitions = {
        'carrier': ('A candidate common typed relational/compositional source, with retained records and admitted equivalences, supporting a shared source-indexed interface calculus. Sector records are indexed inputs whose provenance must be explicit; they are not unrestricted fitted adapters.',
                    [0, 1, 4, 8], ['Bare vector-space naturality is too strong to select nontrivial sector structure.', 'Bool Tick has only its classified tag information at fixed source.', 'Anchored relational chirality does not select flavor constants.'],
                    ['No common carrier for all sectors has been constructed.', 'The primitive relation/composition types and allowed source records remain to be selected.', 'A shared grammar does not yet prove a shared physical witness.']),
        'geometry': ('A candidate family of typed geometric realizations attached to the relational source through explicit maps: topology, metric, differential, causal or spatial structures must each declare whether primitive, derived or added. An external analytic interval is not automatically physical spacetime.',
                     [5, 7], ['A face-indexed summary does not retain all ordered-path spatial information.'],
                     ['No common path-to-spacetime construction is identified.', 'Metric, dimension, Lorentzian/causal structure and their source authority remain open.']),
        'dynamics': ('Candidate admissible source operations, their compositions and retained schedules, together with explicitly declared realization laws. Analytic flow parameters, rates and return orientation are separate from any physical-clock claim.',
                     [4, 5, 6, 9], ['Equal corners allow different Hamiltonians and intermediate images.', 'A reflected return and positive continuation need not agree.'],
                     ['Physical time and energy calibration remain open.', 'Source-only unique generator selection is not established.', 'Cross-sector dynamics and one common witness need transport proofs.']),
        'observables': ('Candidate source-authorized measurement/probe maps on typed interfaces, respecting declared equivalences and transport. Terminal readouts may be quotients; joint faithfulness and cutoff-uniform stability are separate claims, not requirements imposed on every individual scalar.',
                        [1, 2, 3, 12], ['A scalar readout can annihilate independently controlled directions.', 'Finite injectivity can lose its lower bound at completion.', 'Flavor normalization can leave calibration/gain fibers.'],
                        ['The authorized probe family and physical measurement model are not selected.', 'Readout descent, empirical calibration and common-observer compatibility remain open.'])
    }
    for term in terms['terms']:
        if term['id'] not in definitions:
            continue
        definition, indices, counterexamples, residuals = definitions[term['id']]
        term.update(status='reviewed_candidate', definition=definition,
                    evidence=[{'source_path': SOURCES[i][0], 'source_sha256': pin(SOURCES[i][0]),
                               'role': 'textual_scope_and_counterexample_review_not_proof_import'} for i in indices],
                    assumptions=['Declared source/enrichment inputs require provenance; no physical interpretation by analogy.'],
                    counterexamples=counterexamples, residuals=residuals)
    hierarchy = copy.deepcopy(load('contracts/programme-hierarchy.v1.json'))
    hierarchy['schema'] = 'marici.conjecture-net.programme-hierarchy.v2'
    hierarchy['id'] = 'marici.relational-carrier-physics-programme.v2'
    hierarchy['phase'] = 'partial_term_review_candidate_links'
    hierarchy['predecessor'] = 'research/conjecture_net/contracts/programme-hierarchy.v1.json'
    hierarchy['terms'] = terms['hierarchy'].replace('hierarchy', 'terms')
    hierarchy['review'] = terms['review']
    hierarchy['root']['candidate_formulation'] = 'There exists one typed relational carrier and shared source-indexed calculus, with explicitly justified source records, geometric realizations, dynamics and observable maps, recovering a declared set of physical regimes with compatible shared observations and falsifiable constraints.'
    hierarchy['root']['candidate_assumption_boundary'] = 'Which indexed source records are admissible and which must be derived remains unresolved. Inserting measured sector laws into those records cannot count as explaining their origin.'
    links = [
        ('standard-local-existence', SOURCES[10][0], 'source-derived-intermediate-locality-preserving-lift', 'physical-sector-realizations', 'research/nima/contracts/imports/standard-local-lift.pointer.v1.json', 'Existence of one mathematical local/return realization is not recovery of QM or another physical theory.', 'Transport its finite Bool/spectral witness to a specified sector of the common carrier.'),
        ('operational-local-dynamics', SOURCES[9][0], 'operational-spectral-whole-return-certificate', 'carrier-and-geometric-dynamics', 'research/nima/exports/operational-whole-return.pointer.v1.json', 'Fresh operational laws plus accepted written semantics; not kernel semantics or physical dynamics.', 'Identify the native source as an instance of the candidate common carrier and justify its geometric realization.'),
        ('retained-reaggregation-discriminator', SOURCES[11][0], 'conditional-reaggregation-comparison', 'falsifiable-explanatory-constraint', None, 'A conditional same-input discriminator is not an empirical particle or photon prediction.', 'Show that both rules and their common source/reference are authorized instances of the programme witness.'),
        ('flavor-measurement-gates', SOURCES[12][0], 'current_flavor_integer_pole_branch_not_physical_selector', 'empirical-recovery', None, 'State-contract interfaces expose open preparation, clock, calibration and gain gates; not proof ports.', 'Identify shared physical ports and derive their relation to programme observables and calibration.'),
        ('theta-auxiliary-transport', SOURCES[13][0], 'current_rh_programme_not_rh_proof', 'cross-sector-compatibility', None, 'Auxiliary arithmetic/theta interface test only; not a physical-sector recovery or RH proof.', 'Specify whether and how its typed source/calculus maps into the common carrier; no connection is assumed.')
    ]
    hierarchy['existing_net_links'] = [
        {'id': key, 'source_net': source, 'source_sha256': pin(source), 'source_claim': claim,
         'target_obligation': target, 'relation': 'candidate_prerequisite', 'status': 'candidate',
         'outcome_pointer': pointer, 'scope_transport': 'required; not proved in this review',
         'witness_transport': witness, 'verification_boundary': boundary,
         'authority_selection': 'reviewed artifact only; latest/authoritative source selection not inferred',
         'proof_bearing': False} for key, source, claim, target, pointer, boundary, witness in links]
    hierarchy['next_refinements'] = [
        {'id': 'source-primitives-and-record-provenance', 'parent': 'carrier-and-geometric-dynamics', 'kind': 'specification_task', 'outcome': None},
        {'id': 'path-to-geometry-interface', 'parent': 'carrier-and-geometric-dynamics', 'kind': 'specification_task', 'outcome': None},
        {'id': 'dynamics-selection-and-clock-policy', 'parent': 'carrier-and-geometric-dynamics', 'kind': 'specification_task', 'outcome': None},
        {'id': 'authorized-probes-and-readout-descent', 'parent': 'cross-sector-compatibility', 'kind': 'specification_task', 'outcome': None},
        {'id': 'bounded-physical-target-set', 'parent': 'physical-sector-realizations', 'kind': 'specification_task', 'outcome': None}
    ]
    return {'reviews/programme-term-review.v1.json': review,
            'contracts/programme-terms.v2.json': terms,
            'contracts/programme-hierarchy.v2.json': hierarchy}


if __name__ == '__main__':
    documents = build()
    payloads = {name: json.dumps(data, indent=2, sort_keys=True) + '\n' for name, data in documents.items()}
    for name, payload in payloads.items():
        path = HOME / name
        if path.exists() and path.read_text(encoding='utf-8') != payload:
            raise RuntimeError('Refusing implicit review correction: ' + name)
    for name, payload in payloads.items():
        path = HOME / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(payload, encoding='utf-8')
    print(json.dumps({'status': 'recorded', 'reviewed_terms': 4, 'candidate_links': 5,
                      'admitted_links': 0, 'new_proofs': 0}, indent=2))

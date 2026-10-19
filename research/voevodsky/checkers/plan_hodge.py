"""Hodge adapter for the shared dependency-aware workbench, not another scorer."""
import argparse
import copy
import json
from pathlib import Path
from check_conjecture_test_planning import initial, load, sha, require, ROOT
from check_conjecture_workbench import build
from check_hodge_coherence_leads import validate as validate_overlay

PATHS = {'hodge': 'research/conjecture_net/contracts/hodge-coherence-leads.v1.json'}
ESTIMATES = 'research/voevodsky/inputs/hodge-workbench-estimates.v1.json'
CARDS = 'research/voevodsky/inputs/hodge-workbench-action-cards.v1.json'
REPORT = 'research/voevodsky/results/hodge-workbench-v1.json'
VIEW = 'research/conjecture_net/HODGE-WORKBENCH.md'
AUDIT = 'two-cotower-source-interface-audit'
DISPOSITION = 'research/voevodsky/inputs/hodge-two-cotower-audit-disposition.v1.json'


def adapter(c):
    audit_sources = next(n['sources'] for n in c['conjectures'] if n['id'] == 'hodge-barycenter-two-cotower-coherence')
    audit = dict(id=AUDIT, status='open', verdict='open', depends_on=[],
        statement='Bounded audit of the existing RH two-tower source maps against the fixed Hodge cycle-class interface.',
        acceptance='An explicit source/type/map comparison identifying an actual common Hodge interface, with a written proof of its declared scope.',
        falsifier='An incompatible domain, sign convention or operation prevents the proposed binding; missing source data gives inconclusive, not nonexistence.',
        next_action='Read the recovered two-tower and Koszul-normalization sources beside the Hodge cycle-map scope. Write the actual domain/codomain table; test one mixed square only if all maps are supplied. Stop at the first absent map.',
        deliverable='One bounded source-interface audit: constructed binding, rejected proposed binding, or exact missing map. No new hypothetical successor tasks.',
        sources=audit_sources + ['research/voevodsky/hodge-cycle-map-scope-v1.md'])
    if (ROOT/DISPOSITION).exists():
        disposition = load(DISPOSITION)
        require(disposition['task'] == AUDIT and disposition['verdict'] == 'inconclusive', 'audit disposition')
        require(load(disposition['receipt'])['passed'], 'audit receipt failed')
        for path, digest in disposition['source_sha256'].items():
            require(sha(path) == digest, 'audit evidence drift: '+path)
        audit.update(status='resolved', verdict='inconclusive')
    descent_sources = ['research/voevodsky/hodge-zariski-cycle-descent-v1.md', 'research/voevodsky/hodge-cycle-map-scope-v1.md']
    construction_tasks = [dict(
        id='rational-equivalence-witness-descent', status='resolved', verdict='constructed', depends_on=[],
        statement='Construct a witness-retaining algebraic cycle descent interface rather than a presheaf of Chow classes.',
        acceptance='Give actual cycle/rational-function boundary maps, overlap comparison witnesses and one controlled algebraic example; state exactly what higher obstruction remains.',
        falsifier='The proposed boundary maps fail their identities, lose the P1 transition witness, or label an algebraic control nonrealizable.',
        next_action='Starting from the P1 local-Chow loss, retain rational-function equivalence witnesses and their relations; formulate the first cycle-complex descent map and compare it with cohomological realization.',
        deliverable='Typed source maps and an exact known-algebraic gluing control, or a scoped rejection of the chosen complex.', sources=descent_sources + ['research/voevodsky/hodge-rational-equivalence-witness-descent-v1.md']), dict(
        id='higher-cycle-witness-boundary', status='resolved', verdict='constructed',
        depends_on=['rational-equivalence-witness-descent'], required_verdicts={'rational-equivalence-witness-descent':'constructed'},
        statement='Bind rational-function equivalences to actual degree-one chains of a higher cycle complex.',
        acceptance='Construct a properly face-admissible cycle from a rational-function witness, verify its boundary and restriction conventions on an algebraic control, and state the degree-two relation gate.',
        falsifier='A face intersection is improper, its boundary has wrong sign or multiplicity, or a nonzero kernel representative is called an invariant without the allowed witness quotient.',
        next_action='Construct the graph chain of a rational function in the cubical or simplicial higher-cycle model; freeze coordinates and face signs, verify the P1 monomial divisor boundary, and compare the actual relation type with the two-term overlap kernel.',
        deliverable='Actual higher-cycle source chain and boundary certificate; no full motivic comparison or alpha lift assumed.',
        sources=['research/voevodsky/hodge-rational-equivalence-witness-descent-v1.md', 'research/voevodsky/hodge-higher-cycle-graph-boundary-v1.md']), dict(
        id='global-multiplicativity-face-control', status='resolved', verdict='constructed',
        depends_on=['higher-cycle-witness-boundary'], required_verdicts={'higher-cycle-witness-boundary':'constructed'},
        statement='Compute a global nonconstant multiplicativity surface, including its vertical face terms.',
        acceptance='Give the closure equations on P1 times square squared, check every face and corner, and compute the complete boundary without suppressing vertical components.',
        falsifier='An omitted vertical contribution or improper face intersection invalidates the proposed global relation.',
        next_action='Choose explicit nonconstant rational f,g on P1 and close z=(y-fg)/(y-f). Compute all zero/infinity faces scheme-theoretically, compare with Gamma_f+Gamma_g-Gamma_fg, and retain any correction terms.',
        deliverable='A global algebraic relation or a precisely typed admissibility failure with a known control.',
        sources=['research/voevodsky/hodge-higher-cycle-graph-boundary-v1.md', 'research/voevodsky/hodge-global-multiplicativity-faces-v1.md']), dict(
        id='multiplication-associator-control', status='resolved', verdict='constructed',
        depends_on=['global-multiplicativity-face-control'], required_verdicts={'global-multiplicativity-face-control':'constructed'},
        statement='Compare the two associations of the constructed multiplication fillers at chain level.',
        acceptance='Give the closed difference of the two degree-two composites and either an admissible degree-three boundary or a correctly typed residual modulo allowed boundaries.',
        falsifier='The claimed defect is only a removable chain representative, or a proposed degree-three chain fails a face condition.',
        next_action='Start with three explicit nonzero constants and the known multiplication curves. Compute the four-term associator chain with signs; distinguish boundary-zero from boundary-exact before extending to nonconstant supports.',
        deliverable='One actual higher comparison or a bounded typed obstruction; not a new Hodge verdict.',
        sources=['research/voevodsky/hodge-global-multiplicativity-faces-v1.md', 'research/voevodsky/hodge-higher-cycle-graph-boundary-v1.md', 'research/voevodsky/hodge-multiplication-associator-v1.md']), dict(
        id='higher-cycle-codimension-transfer', status='resolved', verdict='constructed',
        depends_on=['multiplication-associator-control'], required_verdicts={'multiplication-associator-control':'constructed'},
        statement='Type the transfer of the explicit field multiplication cells to codimension three on X.',
        acceptance='Give actual external-product maps with supplied codimension-two cycles, check dimensions, boundary and degeneracy compatibility, and state exactly which degree-zero class they can affect.',
        falsifier='Cubical degree is equated with algebraic codimension, an input algebraic support is silently generated, or a rational-equivalence boundary is declared a nonzero Hodge class.',
        next_action='Form W external [a], W external T and W external S for an actual codimension-two support W on the fixed X. Compute the degree-zero boundary and identify whether these operations concern an existing algebraic cycle or existence of a new representative.',
        deliverable='Source-typed codimension transfer and its image/degree-zero limit, with a polarization-cycle control.',
        sources=['research/voevodsky/hodge-multiplication-associator-v1.md', 'research/voevodsky/hodge-cycle-map-scope-v1.md', 'research/voevodsky/hodge-higher-cycle-codimension-transfer-v1.md']), dict(
        id='deligne-lift-versus-algebraic-image', status='resolved', verdict='constructed',
        depends_on=['higher-cycle-codimension-transfer'], required_verdicts={'higher-cycle-codimension-transfer':'constructed'},
        statement='Test whether the degree-six Deligne realization target itself obstructs lifting the fixed rational Hodge class.',
        acceptance='Type the Deligne exact sequence and the rational Hodge projection; distinguish existence of a cohomological lift from the image of the algebraic regulator, with correct degree and coefficients.',
        falsifier='A Deligne lift is silently promoted to an algebraic cycle, or a rational Hodge class is claimed unliftable despite exactness.',
        next_action='Construct the degree-six Deligne/Betti comparison from its cone or exact sequence for smooth projective X; test alpha liftability and identify the remaining algebraic-image requirement.',
        deliverable='An actual realization interface and a scoped verdict on the lift-failure detector, not a cycle existence assertion.',
        sources=['research/voevodsky/hodge-higher-cycle-codimension-transfer-v1.md', 'research/voevodsky/hodge-cycle-map-scope-v1.md', 'research/voevodsky/hodge-deligne-lift-image-v1.md']), dict(
        id='algebraic-support-localization', status='resolved', verdict='constructed',
        depends_on=['deligne-lift-versus-algebraic-image'], required_verdicts={'deligne-lift-versus-algebraic-image':'constructed'},
        statement='Test algebraic support localization as a source-specific degree-six necessity condition.',
        acceptance='Type H_Z^6(X) to H^6(X), identify its image for codimension-at-least-three algebraic supports including singular/reducible supports, and distinguish a finite constructor audit from all-support exclusion.',
        falsifier='Topological support is mistaken for algebraic support, singular supports are silently omitted, or finite divisor support coverage is assumed universal.',
        next_action='Use localization and purity or Borel-Moore duality to compute the degree-six support image. Test actual complete intersections and contrast the proposed alpha support requirement with the already unresolved cycle image.',
        deliverable='A geometric support criterion with an explicit algebraic control and no assumed universal exclusion.',
        sources=['research/voevodsky/hodge-deligne-lift-image-v1.md', 'research/voevodsky/hodge-cycle-map-scope-v1.md', 'research/voevodsky/hodge-algebraic-support-localization-v1.md']), dict(
        id='smooth-ample-envelope-control', status='resolved', verdict='constructed',
        depends_on=['algebraic-support-localization'], required_verdicts={'algebraic-support-localization':'constructed'},
        statement='Test the support image of a smooth ample divisor and the limits of enclosing prescribed algebraic supports in it.',
        acceptance='Compute the degree-six Gysin image using weak Lefschetz, test the primitive alpha, and distinguish smooth general divisors from divisors forced to contain a prescribed base locus.',
        falsifier='Bertini is used to erase singularities on a prescribed support without checking hypotheses, or a restriction for smooth envelopes is asserted for every algebraic support.',
        next_action='For smooth D in class mE, compute H4(D) to H6(X) via restriction and Gysin. Compare with primitive alpha, then audit the claim that any codimension-three support fits inside such a smooth D.',
        deliverable='A geometric envelope restriction with a known algebraic control and an explicit singular-envelope residual.',
        sources=['research/voevodsky/hodge-algebraic-support-localization-v1.md', 'research/voevodsky/hodge-fixed-sixfold-quadratic-pairing-v1.md', 'research/voevodsky/hodge-smooth-ample-envelope-v1.md']), dict(
        id='singular-envelope-normal-jet-control', status='resolved', verdict='constructed',
        depends_on=['smooth-ample-envelope-control'], required_verdicts={'smooth-ample-envelope-control':'constructed'},
        statement='Construct and classify generic singular envelopes of the known algebraic complete-intersection support.',
        acceptance='Justify generation and transversality of normal derivative sections for sufficiently high degree, compute the local Hessian at a transverse zero, and separate top Chern obstruction from an actual singularity count.',
        falsifier='A nonzero top Chern number alone is called a count of nodes, or singularities of a known algebraic control are promoted to a Hodge obstruction.',
        next_action='For Z=CI(kE,kE,kE), use the ideal/conormal sequence and high-degree vanishing to control the normal derivative of a containing divisor. Test generic zeros and the local Hessian, including smoothness away from Z.',
        deliverable='A calibrated singular-envelope construction with a justified singularity count/type or a precisely scoped failure.',
        sources=['research/voevodsky/hodge-smooth-ample-envelope-v1.md', 'research/voevodsky/hodge-algebraic-support-localization-v1.md', 'research/voevodsky/hodge-singular-envelope-normal-jets-v1.md']), dict(
        id='nodal-link-localization-control', status='resolved', verdict='constructed',
        depends_on=['singular-envelope-normal-jet-control'], required_verdicts={'singular-envelope-normal-jet-control':'constructed'},
        statement='Type the local-to-global support contribution of the constructed nodal envelopes.',
        acceptance='Compute rational link groups for a complex five-dimensional node and the exact sequence for H4 of the nodal divisor and its smooth locus; retain the global connecting map before claiming independent support classes.',
        falsifier='N local nodes are counted as N independent global classes, or smooth-divisor purity is applied at a singular point.',
        next_action='Compute the node link using its sphere-bundle or Milnor model. Insert the local groups into the localization sequence for the divisor and its finite singular locus, and compare with degree-six support duality in X.',
        deliverable='An actual local-to-global interface with exact degrees and a stated global-relation residual.',
        sources=['research/voevodsky/hodge-singular-envelope-normal-jets-v1.md', 'research/voevodsky/hodge-algebraic-support-localization-v1.md', 'research/voevodsky/hodge-nodal-link-localization-v1.md']), dict(
        id='known-cycle-nodal-residue-control', status='resolved', verdict='constructed',
        depends_on=['nodal-link-localization-control'], required_verdicts={'nodal-link-localization-control':'constructed'},
        statement='Compute actual nodal residues of the known algebraic support and their ambient primitive image.',
        acceptance='Retain the embedded threefold in the node normal form, compute its local residue using the projective quadric or link, and compare its global residue vector with its ambient polarization class.',
        falsifier='A formal nonzero residue fixture is substituted for the actual cycle, or a residue killed by ambient pushforward is called an obstruction to algebraicity.',
        next_action='Put the pair (D,Z) locally in the form sum x_i y_i=0 with Z:y=0. Compute the ruling-plane class in link cohomology, then use the global class of Z to test gamma and psi on the resulting residue vector.',
        deliverable='An actual algebraic residue control for both global maps, with signs or generator choices stated.',
        sources=['research/voevodsky/hodge-nodal-link-localization-v1.md', 'research/voevodsky/hodge-singular-envelope-normal-jets-v1.md', 'research/voevodsky/hodge-known-cycle-nodal-residue-v1.md']), dict(
        id='complete-intersection-envelope-blowup', status='resolved', verdict='constructed',
        depends_on=['known-cycle-nodal-residue-control'], required_verdicts={'known-cycle-nodal-residue-control':'constructed'},
        statement='Compute the entire global residue rank for the known complete-intersection envelope family.',
        acceptance='Type the blowup of X along Z, the smooth ample strict transform and its exceptional fibers; use exact purity and blowup degrees to calculate H4(U) and K_D, then evaluate the ambient primitive image.',
        falsifier='Exceptional fibers over nodes are confused with those over the smooth locus, or cohomology ranks are subtracted without a valid blowup/purity comparison.',
        next_action='Blow up X along Z and inspect the strict transform of a general high-degree containing divisor. Compare H4 of the strict transform with its complement of exceptional node fibers and with the blowup of U along Z minus Sigma.',
        deliverable='A complete rank and ambient-image calculation for this specific family, not a universal support theorem.',
        sources=['research/voevodsky/hodge-known-cycle-nodal-residue-v1.md', 'research/voevodsky/hodge-nodal-link-localization-v1.md', 'research/voevodsky/hodge-ci-envelope-blowup-v1.md']), dict(
        id='smooth-center-envelope-image', status='resolved', verdict='constructed',
        depends_on=['complete-intersection-envelope-blowup'], required_verdicts={'complete-intersection-envelope-blowup':'constructed'},
        statement='Determine which envelope conclusions persist for an arbitrary supplied smooth codimension-three center.',
        acceptance='Recheck generic nodality and both blowup comparisons without the complete-intersection hypothesis; compute the residue quotient and its ambient map in terms of the actual center class, retaining the singular-center limitation.',
        falsifier='The center class is silently assumed to be a polarization multiple, or arbitrary singular cycles are assumed to admit smooth embedded representatives.',
        next_action='Repeat the normal-bundle and blowup argument for a supplied smooth connected threefold Z in X. Track b2(Z) through both decompositions and evaluate the generator of the residue quotient under ambient pushforward.',
        deliverable='A general smooth-center formula with an explicit residual for singular supports, not an all-cycle annihilation theorem.',
        sources=['research/voevodsky/hodge-ci-envelope-blowup-v1.md', 'research/voevodsky/hodge-known-cycle-nodal-residue-v1.md', 'research/voevodsky/hodge-smooth-center-envelope-image-v1.md']), dict(
        id='singular-cycle-resolution-pushforward', status='resolved', verdict='constructed',
        depends_on=['smooth-center-envelope-image'], required_verdicts={'smooth-center-envelope-image':'constructed'},
        statement='Cover singular cycle generators by smooth proper-map sources without asserting embedded smoothability.',
        acceptance='Type the resolution fundamental class and its proper pushforward to X, account for exceptional components and verify an explicit singular algebraic control; state why the embedded-center envelope theorem does not automatically apply.',
        falsifier='A resolution map is treated as an embedding into the unchanged X, or lower-dimensional exceptional images are counted as new threefold cycle classes.',
        next_action='Resolve an irreducible algebraic threefold support and compute its fundamental-class pushforward. Use a nodal complete-intersection control to check local exceptional geometry, then compare proper-map and embedded-center source types.',
        deliverable='An all-generator proper-map interface with a concrete singular control and a retained embedded-center gap.',
        sources=['research/voevodsky/hodge-smooth-center-envelope-image-v1.md', 'research/voevodsky/hodge-algebraic-support-localization-v1.md', 'research/voevodsky/hodge-singular-cycle-resolution-v1.md']), dict(
        id='proper-map-graph-sixfold-reduction', status='resolved', verdict='constructed',
        depends_on=['singular-cycle-resolution-pushforward'], required_verdicts={'singular-cycle-resolution-pushforward':'constructed'},
        statement='Convert a smooth proper-map source into an embedded center on a controlled auxiliary sixfold.',
        acceptance='Construct the graph in X times projective space, justify a smooth sixfold complete intersection through it including the normal rank-drop locus, and type the projection pushforward of the auxiliary Lefschetz sector.',
        falsifier='Bertini is applied blindly along the graph, or the auxiliary polarization sector is silently identified with the one on X.',
        next_action='Embed Y by a very ample line bundle and take its graph in X times P^N. Analyze N sufficiently positive hypersurfaces through that graph, then use weak Lefschetz and projective-bundle integration to compare their sixfold with X.',
        deliverable='An actual graph/auxiliary-ambient construction with controlled pushforward, not a new Hodge candidate.',
        sources=['research/voevodsky/hodge-singular-cycle-resolution-v1.md', 'research/voevodsky/hodge-smooth-center-envelope-image-v1.md', 'research/voevodsky/hodge-proper-map-graph-sixfold-v1.md']), dict(
        id='auxiliary-primitive-pullpush', status='resolved', verdict='constructed',
        depends_on=['proper-map-graph-sixfold-reduction'], required_verdicts={'proper-map-graph-sixfold-reduction':'constructed'},
        statement='Transport the fixed primitive candidate through the constructed auxiliary projection without changing the algebraicity question.',
        acceptance='Use adjoint pairings to test primitivity for the auxiliary polarization, compute the trace and polarized norm, and type Chow pullback/pushforward with the correct degree and hypotheses.',
        falsifier='Generically finite is treated as everywhere finite/etale, pullback is assumed to preserve primitive classes without the sector calculation, or an auxiliary lift is called an algebraic representative.',
        next_action='For g:M to X from the graph construction, compute ell cup g*alpha by duality with H4(M), then g_*g*alpha and its degree-six pairing. Compare algebraicity of alpha and its pullback using rational Chow pull-push.',
        deliverable='A verified primitive-class transport and a scoped verdict on whether this auxiliary construction changes the unresolved cycle-image gate.',
        sources=['research/voevodsky/hodge-proper-map-graph-sixfold-v1.md', 'research/voevodsky/hodge-fixed-sixfold-quadratic-pairing-v1.md', 'research/voevodsky/hodge-auxiliary-primitive-pullpush-v1.md']), dict(
        id='source-complete-weil-reader-audit', status='resolved', verdict='constructed',
        depends_on=['auxiliary-primitive-pullpush'], required_verdicts={'auxiliary-primitive-pullpush':'constructed'},
        statement='Compose the constructed all-generator interfaces into a genuine source-complete Weil reader and audit its remaining necessity condition.',
        acceptance='Give the two-component reader on every smooth proper-map source, prove class descent and resolution/auxiliary-choice compatibility, and distinguish complete source coverage from universal annihilation.',
        falsifier='Source completeness or positive norm is used to assume vanishing on all algebraic cycles, or the old projector condition is relabeled a new theorem.',
        next_action='Define the reader by integrals of f*R and f*I on Y. Compare its normalized values with Weil coordinates of f_*(1_Y), compose the auxiliary graph/envelope maps, and record exactly which universal equation is still unproved.',
        deliverable='A source-complete diagram and scoped conjecture disposition with no inferred Hodge verdict.',
        sources=['research/voevodsky/hodge-auxiliary-primitive-pullpush-v1.md', 'research/voevodsky/hodge-singular-cycle-resolution-v1.md', 'research/voevodsky/hodge-weil-projector-v1.md', 'research/voevodsky/hodge-source-complete-weil-reader-v1.md']), dict(
        id='product-fiber-witness-deformation', status='resolved', verdict='constructed',
        depends_on=[],
        statement='Test deformation of the actual known-algebraic product-fiber witness, independently of the exhausted reader reformulation.',
        acceptance='Choose a legitimate infinitesimal Weil-family direction, compute the linearized Hodge condition on the displayed divisor factors and determinant class, and distinguish witness-factor failure from nonexistence of any algebraic realization.',
        falsifier='Flatness of the determinant class is treated as transport of its divisor witnesses, or failure of chosen divisors to deform is promoted to universal nonalgebraicity.',
        next_action='Read the fixed Weil period chart at its product origin. Choose an admissible tangent direction and compute the first-order type of r_j,s_j versus R,I using the native complex structure and polarization constraints.',
        deliverable='A geometric first-order witness-transport test, not another source-reader or norm identity.',
        sources=['research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-middle-hodge-kernel-v1.md', 'research/voevodsky/hodge-weil-projector-v1.md', 'research/voevodsky/hodge-product-witness-first-order-v1.md']), dict(
        id='fixed-divisor-witness-hodge-locus', status='resolved', verdict='constructed',
        depends_on=['product-fiber-witness-deformation'], required_verdicts={'product-fiber-witness-deformation':'constructed'},
        statement='Determine the simultaneous Hodge locus of the six fixed product-fiber divisor factors.',
        acceptance='Compute the full-chart tangent constraints and justify any claimed exact locus, with a positive subfamily control; distinguish preservation of this witness from existence of all algebraic witnesses.',
        falsifier='One tangent direction is mistaken for the complete Hodge locus, or exclusion of the fixed factors is promoted to nonalgebraicity of the determinant class.',
        next_action='Analyze D_J b_j=0 for all three decomposable native two-forms throughout the positive-plane chart. Compare the full tangent constraints with diagonal period matrices and test whether nonlinear off-diagonal solutions remain.',
        deliverable='An exact or explicitly first-order witness locus, not a universal cycle exclusion.',
        sources=['research/voevodsky/hodge-product-witness-first-order-v1.md', 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-fixed-divisor-witness-locus-v1.md']), dict(
        id='degree-six-witness-deformation-cancellation', status='resolved', verdict='constructed',
        depends_on=['fixed-divisor-witness-hodge-locus'], required_verdicts={'fixed-divisor-witness-hodge-locus':'constructed'},
        statement='Test the actual codimension-three witness summands rather than only their divisor factors.',
        acceptance='Compute the first-order Hodge operator on the four signed product classes giving R, determine the kernel on their span and explain exactly what cancellation does and does not imply for deforming algebraic cycles.',
        falsifier='Failure of factors alone is declared failure of their product class, or Hodge cancellation of a signed sum is declared a constructed family of cycles.',
        next_action='Use the prior admissible off-diagonal direction and exact exterior forms to differentiate each degree-six product in the R identity. Compare individual type failures with the total class and with an actual algebraic control at the product point.',
        deliverable='A degree-six witness transport test with explicit cancellation and a scoped deformation residual.',
        sources=['research/voevodsky/hodge-product-witness-first-order-v1.md', 'research/voevodsky/hodge-fixed-divisor-witness-locus-v1.md', 'research/voevodsky/hodge-weil-projector-v1.md', 'research/voevodsky/hodge-degree-six-witness-cancellation-v1.md']), dict(
        id='joint-family-divisor-product-control', status='resolved', verdict='constructed',
        depends_on=['degree-six-witness-deformation-cancellation'], required_verdicts={'degree-six-witness-deformation-cancellation':'constructed'},
        statement='Test whether the separately available divisor witnesses extend to their joint two-parameter family.',
        acceptance='Specify a small algebraically independent pair in P11=s,P12=t, certify its rational divisor Hodge space using exact constraints and matching invariance proofs, and test the degree-six divisor-product span against K1,K2.',
        falsifier='Axis witnesses are assumed compatible on the joint family, finite samples are treated as a genericity proof alone, or non-divisor-generation is declared nonalgebraicity.',
        next_action='Use the exact native chart for P11=s,P12=t. Compute common degree-two Hodge constraints, justify evaluation at an algebraically independent pair, and compare triple divisor products with the preserved degree-six kernel classes.',
        deliverable='A joint-family divisor-generation certificate or a precisely typed computational residual, not an all-cycle verdict.',
        sources=['research/voevodsky/hodge-degree-six-witness-cancellation-v1.md', 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-joint-family-divisor-products-v1.md']), dict(
        id='joint-family-odd-sector-correspondence', status='resolved', verdict='constructed',
        depends_on=['joint-family-divisor-product-control'], required_verdicts={'joint-family-divisor-product-control':'constructed'},
        statement='Type the non-divisor correspondence source for the preserved odd-sector classes in the joint-family control.',
        acceptance='Identify the active determinant rank-two Hodge structure, its weight-one Tate twist and a compatible CM elliptic source; compute the required correspondence codimension and separate its Hodge class from an actual algebraic cycle.',
        falsifier='A rational Hodge isomorphism is declared an algebraic correspondence without a theorem or construction, or the control fiber replaces the original sixfold.',
        next_action='Compute the types and K action on the determinant of native coordinates1,2,4. Compare its Tate twist with an elliptic H1, and construct the cohomological tensor defining an H1-to-H3 correspondence on the elliptic curve times the active threefold.',
        deliverable='A precise lower-dimensional correspondence interface and its algebraic-realization gate on the control family.',
        sources=['research/voevodsky/hodge-joint-family-divisor-products-v1.md', 'research/voevodsky/hodge-cycle-map-scope-v1.md', 'research/voevodsky/hodge-joint-odd-sector-correspondence-v1.md']), dict(
        id='split-fourfold-correspondence-theorem-audit', status='resolved', verdict='constructed',
        depends_on=['joint-family-odd-sector-correspondence'], required_verdicts={'joint-family-odd-sector-correspondence':'constructed'},
        statement='Audit exact algebraicity theorem coverage for the split Weil-fourfold correspondence control.',
        acceptance='Read an actual theorem statement and match dimension, imaginary quadratic field, Hermitian discriminant, polarization and generic/special or decomposable hypotheses to C times A and gamma; distinguish theorem-backed existence from explicit cycle construction.',
        falsifier='A split theorem is transferred to the original nonsplit sixfold, a generic theorem is silently applied to a decomposable fiber, or a citation title replaces a theorem statement.',
        next_action='Inspect retained Weil-algebraicity literature and its primary-source theorem statements for the split fourfold C times A. Verify whether both determinant components including gamma are covered, and record an applicable theorem or the precise remaining hypothesis.',
        deliverable='A source-grounded applicability verdict for the control correspondence, with no inferred fixed-sixfold Hodge verdict.',
        sources=['research/voevodsky/hodge-joint-odd-sector-correspondence-v1.md', 'research/voevodsky/hodge-literature-boundary-audit-v1.md', 'research/voevodsky/hodge-split-fourfold-correspondence-audit-v1.md']), dict(
        id='joint-control-algebraic-correspondence-transfer', status='resolved', verdict='constructed',
        depends_on=['split-fourfold-correspondence-theorem-audit'], required_verdicts={'split-fourfold-correspondence-theorem-audit':'constructed'},
        statement='Transfer the theorem-backed algebraic correspondence to the joint-family degree-six control classes.',
        acceptance='Specify the map from A times B to C times A, the CM transform for both determinant components, and actual Chow pullbacks/products with inactive divisors; verify K1,K2 coefficients and factor-order signs.',
        falsifier='A Hodge tensor is substituted for the imported algebraic cycle, factor permutation signs are dropped, or algebraicity of this control is transferred to the original fixed sixfold.',
        next_action='Use the inactive elliptic coordinate to define a holomorphic map to C with the correct conjugation. Pull back Gamma_alg and its CM transform, multiply the r3,s3 divisor classes, and compare their exact degree-six classes with K1,K2.',
        deliverable='Theorem-backed rational cycle expressions for the non-divisor-generated control classes, with scope explicitly restricted to the joint family.',
        sources=['research/voevodsky/hodge-split-fourfold-correspondence-audit-v1.md', 'research/voevodsky/hodge-joint-odd-sector-correspondence-v1.md', 'research/voevodsky/hodge-degree-six-witness-cancellation-v1.md', 'research/voevodsky/hodge-joint-correspondence-transfer-v1.md']), dict(
        id='complementary-threefold-correspondence-composition', status='resolved', verdict='constructed',
        depends_on=['joint-control-algebraic-correspondence-transfer'], required_verdicts={'joint-control-algebraic-correspondence-transfer':'constructed'},
        statement='Extend the algebraic control to two varying complementary-signature threefold factors by composing correspondences.',
        acceptance='Type both elliptic-to-threefold correspondences with their CM choices and Hermitian discriminants, verify theorem coverage for any nonsplit fourfold, and compute the codimension-three composition and determinant signs.',
        falsifier='The fixed inactive elliptic projection is used after that factor varies, a split-only theorem is applied to a nonsplit fourfold, or the decomposable control replaces the original target.',
        next_action='Replace the inactive projection by a correspondence for a varying threefold of signature(1,2). Form the intersection of the two pulled-back codimension-two correspondences on C times A times B and push along C; compute both determinant components.',
        deliverable='A larger decomposable-family algebraic control with exact correspondence composition, not a result for the original full-period sixfold.',
        sources=['research/voevodsky/hodge-joint-correspondence-transfer-v1.md', 'research/voevodsky/hodge-split-fourfold-correspondence-audit-v1.md', 'research/voevodsky/hodge-complementary-threefold-composition-v1.md']), dict(
        id='fixed-source-isogeny-decomposition-barrier', status='resolved', verdict='constructed',
        depends_on=['complementary-threefold-correspondence-composition'], required_verdicts={'complementary-threefold-correspondence-composition':'constructed'},
        statement='Test hidden abelian product decompositions of the original source, not just its displayed coordinate chart.',
        acceptance='Use the certified rational Picard rank, isogeny pullback and Poincare reducibility to decide whether the source can be a nontrivial product up to isogeny; keep nonlinear algebraic supports outside that exclusion.',
        falsifier='Absence of a block decomposition in one marking is declared intrinsic simplicity, or absence of abelian subvarieties is confused with absence of all algebraic threefold cycles.',
        next_action='Prove the rational Neron-Severi comparison under an isogeny and the independent product-polarization classes. Apply the rank-one certificate of the unchanged X, then state exactly which correspondence-control transport routes are excluded.',
        deliverable='An intrinsic source-decomposition verdict with an explicit remaining nonlinear-cycle boundary.',
        sources=['research/voevodsky/hodge-complementary-threefold-composition-v1.md', 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-fixed-source-isogeny-barrier-v1.md']), dict(
        id='period-genericity-cycle-spread-audit', status='resolved', verdict='constructed',
        depends_on=['fixed-source-isogeny-decomposition-barrier'], required_verdicts={'fixed-source-isogeny-decomposition-barrier':'constructed'},
        statement='Audit whether the fixed period independence certificate licenses algebraic cycle spreading or only rational-in-period Hodge equations.',
        acceptance='Separate the period chart, algebraic moduli base and relative cycle parameter images; identify the exact dominance or deformation hypotheses needed to transport special-fiber cycles, with a control against confusing analytic and algebraic genericity.',
        falsifier='Polynomial independence in period coordinates is silently converted into genericity for algebraic moduli coordinates or dominance of a cycle family.',
        next_action='Trace the actual use of Lindemann-Weierstrass in the fixed-source certificate, compare it with a relative Chow/Hilbert spreading argument, and test the inference across a nonalgebraic analytic coordinate map before applying it to the supplied period.',
        deliverable='A precise genericity/spreading scope statement and a noncircular next geometric gate, not an assumed deformation of the control cycles.',
        sources=['research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-fixed-source-isogeny-barrier-v1.md', 'research/voevodsky/hodge-complementary-threefold-composition-v1.md', 'research/voevodsky/hodge-period-genericity-spread-audit-v1.md']), dict(
        id='control-locus-relative-cycle-spread', status='resolved', verdict='constructed',
        depends_on=['period-genericity-cycle-spread-audit'], required_verdicts={'period-genericity-cycle-spread-audit':'constructed'},
        statement='Construct a relative rational cycle witness on the decomposable control locus, without claiming dominance of the full Weil moduli.',
        acceptance='Specify the level/monodromy cover, countable signed cycle parameter spaces and dominance argument over the control base; construct a finite multisection and normalized trace with a precise dense-open scope.',
        falsifier='Pointwise cycle choices are treated as a relative family without a dominance argument, denominators or trace degrees are omitted, or dominance over the product locus is promoted to dominance over the full base.',
        next_action='Use pointwise algebraicity of the two determinant classes on the product control base. Apply countability and the uncountability/Baire argument to obtain a dominating cycle-parameter component there, then spread and trace universal signed cycles after finite base change on a dense open.',
        deliverable='A theorem-backed relative rational Chow construction on a specified dense open of the control locus, with no claimed transport to the original fixed point.',
        sources=['research/voevodsky/hodge-period-genericity-spread-audit-v1.md', 'research/voevodsky/hodge-complementary-threefold-composition-v1.md', 'research/voevodsky/hodge-control-relative-cycle-spread-v1.md']), dict(
        id='control-spread-specialization-boundary', status='resolved', verdict='constructed',
        depends_on=['control-locus-relative-cycle-spread'], required_verdicts={'control-locus-relative-cycle-spread':'constructed'},
        statement='Distinguish extension across omitted control fibers from extension into transverse Weil deformation directions.',
        acceptance='Use Chow localization or cycle closures and refined fiber restriction on the same smooth control base, then track the codimension of a pushforward into the full-family total space; do not assert new dominance.',
        falsifier='Closure is assumed flat without proof, ordinary intersection is used at an excess fiber, or a cycle supported over a codimension-five base locus is called a relative codimension-three cycle on the full family.',
        next_action='Extend the dense-open relative Chow classes over the smooth control base and check their fiber classes by cycle-class compatibility and flat local-system continuation. Compare the result with any attempted pushforward along the control-base inclusion into full Weil moduli.',
        deliverable='A precise specialization result and transverse-extension barrier with correct total-space and fiber degrees.',
        sources=['research/voevodsky/hodge-control-relative-cycle-spread-v1.md', 'research/voevodsky/hodge-period-genericity-spread-audit-v1.md', 'research/voevodsky/hodge-control-specialization-boundary-v1.md']), dict(
        id='transverse-cycle-infinitesimal-interface', status='resolved', verdict='constructed',
        depends_on=['control-spread-specialization-boundary'], required_verdicts={'control-spread-specialization-boundary':'constructed'},
        statement='Compare actual embedded first-order cycle lifting with its cohomological Hodge condition.',
        acceptance='Type the Kodaira-Spencer obstruction for a supplied smooth embedded cycle and its semiregularity/Hodge image, state hypotheses before using normal bundles, and supply an actual complete-intersection lifting control.',
        falsifier='Zero Hodge derivative is declared zero embedded obstruction without injectivity, or a normal-bundle formula for a smooth cycle is silently applied to an unspecified singular correspondence representative.',
        next_action='For a smooth codimension-three subvariety of a sixfold, construct the first-order obstruction from ambient Kodaira-Spencer classes to H1 of its normal bundle and compare with the Hodge derivative. Test high-degree complete intersections in a polarized abelian family using actual section extension.',
        deliverable='A source-typed infinitesimal extension interface and positive geometric control, with the unresolved kernel clearly retained.',
        sources=['research/voevodsky/hodge-control-specialization-boundary-v1.md', 'research/voevodsky/hodge-control-relative-cycle-spread-v1.md', 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-transverse-infinitesimal-interface-v1.md']), dict(
        id='complete-intersection-semiregularity-map', status='resolved', verdict='constructed',
        depends_on=['transverse-cycle-infinitesimal-interface'], required_verdicts={'transverse-cycle-infinitesimal-interface':'constructed'},
        statement='Compute the actual semiregularity map for the smooth complete-intersection lifting control.',
        acceptance='Track the defining-section space through Koszul and Serre duality, determine rank/kernel with a geometric justification, and compare ambient obstruction values with polarized directions.',
        falsifier='Source/target dimensions are used to infer rank without constructing the map, or a calculation for the ample complete intersection is assigned to the unknown Weil-cycle representative.',
        next_action='Use the Koszul identification of H1 of the normal bundle and changes of basis of the three defining sections to compute the semiregularity map. Compare it with contraction of the ample class under ambient Kodaira-Spencer deformation.',
        deliverable='An actual rank/kernel calculation on the positive control with an explicit separation of obstruction space, obstruction value and Hodge image.',
        sources=['research/voevodsky/hodge-transverse-infinitesimal-interface-v1.md', 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-complete-intersection-semiregularity-v1.md']), dict(
        id='control-bundle-quadratic-obstruction', status='resolved', verdict='constructed',
        depends_on=['complete-intersection-semiregularity-map'], required_verdicts={'complete-intersection-semiregularity-map':'constructed'},
        statement='Construct a nonzero trace-invisible quadratic bundle obstruction and audit its relationship to embedded-cycle deformation.',
        acceptance='Use actual Dolbeault or Cech bundle deformation classes and noncommuting matrices, prove nonzero obstruction in cohomology, and separately justify or delimit any transfer to the complete-intersection Hilbert problem.',
        falsifier='A nonzero matrix is called a geometric obstruction without checking its cohomology class, or an isomorphism of obstruction spaces is treated as compatibility of obstruction operations.',
        next_action='Choose matrix-valued H1(O_X) classes for E=L tensor C^3 with a nonzero commutator obstruction in H2(End E). Check trace invisibility and the obstruction to extending the defining section, then audit the comparison with an embedded first-order deformation of its zero locus.',
        deliverable='A genuine quadratic bundle-deformation obstruction plus a precisely scoped embedded-cycle comparison.',
        sources=['research/voevodsky/hodge-complete-intersection-semiregularity-v1.md', 'research/voevodsky/hodge-transverse-infinitesimal-interface-v1.md', 'research/voevodsky/hodge-control-quadratic-obstruction-v1.md']), dict(
        id='control-formal-commuting-matrix-model', status='resolved', verdict='constructed',
        depends_on=['control-bundle-quadratic-obstruction'], required_verdicts={'control-bundle-quadratic-obstruction':'constructed'},
        statement='Determine the formal local control deformation model beyond its primary quadratic obstruction.',
        acceptance='Verify the invariant-Dolbeault multiplicative comparison, retain gauge and section parameters, and justify the pair-to-Hilbert formal comparison before asserting all-order sufficiency of commuting equations.',
        falsifier='Quadratic obstruction equations alone are declared a complete local model, or quotienting bundle automorphisms drops the defining section and changes the deformation problem.',
        next_action='Compare the End(E) Dolbeault deformation algebra with invariant forms on the abelian sixfold. Analyze commuting six-tuples of matrices, the smooth section-lifting directions and the zero-locus comparison to obtain or precisely delimit the completed local Hilbert model.',
        deliverable='A justified formal control model with correct gauge and tangent dimensions, or an explicit remaining comparison obstruction.',
        sources=['research/voevodsky/hodge-control-quadratic-obstruction-v1.md', 'research/voevodsky/hodge-complete-intersection-semiregularity-v1.md', 'research/voevodsky/hodge-control-formal-model-v1.md']), dict(
        id='control-unipotent-arc-algebraization', status='resolved', verdict='constructed',
        depends_on=['control-formal-commuting-matrix-model'], required_verdicts={'control-formal-commuting-matrix-model':'constructed'},
        statement='Algebraize a nontrivial commuting control arc and compute its Weil-plane readout.',
        acceptance='Specify the nilpotent matrices, section lifting and proper formal existence argument over C[[t]], then use the unipotent filtration to compute the zero-locus class without confusing formal existence with a finite-type algebraic curve.',
        falsifier='An integrable formal arc is called an explicit finite-type family without algebraization, or its unchanged divisor-cube class is promoted to a Weil representative.',
        next_action='Use M1=tJ for a regular nilpotent matrix J and the other matrices zero. Lift the defining section, algebraize over the complete base using proper formal existence, and compute Chern and Weil-projection classes from the bundle filtration.',
        deliverable='A nontrivial algebraized control family over the complete base with exact cycle-class scope and Weil readout.',
        sources=['research/voevodsky/hodge-control-formal-model-v1.md', 'research/voevodsky/hodge-control-quadratic-obstruction-v1.md', 'research/voevodsky/hodge-unipotent-arc-algebraization-v1.md']), dict(
        id='semihomogeneous-bundle-readout-boundary', status='resolved', verdict='constructed',
        depends_on=['control-unipotent-arc-algebraization'], required_verdicts={'control-unipotent-arc-algebraization':'constructed'},
        statement='Audit the Weil readout of simple semihomogeneous bundles and an explicitly generated class of bundle constructions.',
        acceptance='State and justify the precise Chern-character formula and its simple-bundle hypotheses, use the fixed Picard-rank-one certificate, and prove closure only under explicitly listed operations.',
        falsifier='The simple semihomogeneous formula is applied to every algebraic bundle, or annihilation of a generated construction class is promoted to universal cycle annihilation.',
        next_action='Audit ch(F)=rank(F) exp(c1(F)/rank(F)) for simple semihomogeneous bundles. Track degree-three Chern characters and Chern classes under sums, extensions, tensor products and duals on the unchanged fixed X, keeping the resulting source class strictly bounded.',
        deliverable='A theorem-backed generated-bundle readout boundary with exact hypotheses and no universal algebraicity verdict.',
        sources=['research/voevodsky/hodge-unipotent-arc-algebraization-v1.md', 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md', 'research/voevodsky/hodge-semihomogeneous-readout-boundary-v1.md']), dict(
        id='cycle-sheaf-terminal-syzygy-audit', status='resolved', verdict='constructed',
        depends_on=['semihomogeneous-bundle-readout-boundary'], required_verdicts={'semihomogeneous-bundle-readout-boundary':'constructed'},
        statement='Locate the unconstrained terminal bundle in an ample-twist resolution of a cycle sheaf.',
        acceptance='Construct a bounded-length presentation using Serre generation and regularity of the sixfold, track leading ch3 and signs, and compare with a genuine complete-intersection Koszul resolution.',
        falsifier='The final locally free syzygy is assumed a sum of line bundles, or the resulting reformulation of the cycle gate is presented as a new universal obstruction.',
        next_action='Resolve an arbitrary codimension-three cycle sheaf by ample-twist sums until the final kernel is locally free. Compute the terminal kernel Weil readout from the K-theory relation and ch3(O_Z), with no claim that the kernel belongs to the bounded generated class.',
        deliverable='An explicit source-typed terminal-syzygy reduction and a precise explanation of why the bounded bundle audit is not source-complete.',
        sources=['research/voevodsky/hodge-semihomogeneous-readout-boundary-v1.md', 'research/voevodsky/hodge-unipotent-arc-algebraization-v1.md', 'research/voevodsky/hodge-cycle-sheaf-terminal-syzygy-v1.md']), dict(
        id='degree-three-Adams-normalization', status='resolved', verdict='constructed',
        depends_on=['cycle-sheaf-terminal-syzygy-audit'], required_verdicts={'cycle-sheaf-terminal-syzygy-audit':'constructed'},
        statement='Construct an explicit rational algebraic K-operation isolating a supplied primitive degree-three readout.',
        acceptance='Build the polynomial in psi2 using weights 2^j for j0 through6, prove the degree selector and divisor subtraction, and test the actual Koszul control while retaining virtual/rational and Chow/cohomology distinctions.',
        falsifier='A rank-zero virtual output is called an actual nonzero vector bundle, a zero cohomological readout is asserted to be zero in Chow, or normalization is claimed to supply an absent cycle input.',
        next_action='Construct the degree-three Adams projector, combine it with a normalized divisor-cube K-class and compute the resulting primitive readout. Verify the operator exactly on all seven Chern-character degrees and on the complete-intersection class.',
        deliverable='An exact rational K-theory normalization operator and scoped control test, without a new algebraicity verdict.',
        sources=['research/voevodsky/hodge-cycle-sheaf-terminal-syzygy-v1.md', 'research/voevodsky/hodge-semihomogeneous-readout-boundary-v1.md', 'research/voevodsky/hodge-degree-three-Adams-normalization-v1.md']), dict(
        id='polystable-bundle-realization-boundary', status='open', verdict='open',
        depends_on=['degree-three-Adams-normalization'], required_verdicts={'degree-three-Adams-normalization':'constructed'},
        statement='Audit actual polystable bundle realizations of normalized virtual data under a discriminant equality.',
        acceptance='State positive rank, local freeness, polarization and polystability explicitly; derive the projective-flatness consequence of vanishing discriminant degree and its higher Chern-character readout, without applying stability to a virtual class.',
        falsifier='Adding formal rank to a K-class is asserted to produce a polystable vector bundle, or a conditional discriminant equality is imposed on every possible cycle realization.',
        next_action='Use the Hermitian-Einstein/Chern-Weil equality case for an actual H-polystable bundle with discriminant pairing against E^4 equal to zero. Compare its degree-three character with a proposed rank plus primitive degree-three virtual character and retain all missing existence hypotheses.',
        deliverable='A precise conditional positive-rank realization boundary, not a universal Hodge obstruction.',
        sources=['research/voevodsky/hodge-degree-three-Adams-normalization-v1.md', 'research/voevodsky/hodge-semihomogeneous-readout-boundary-v1.md']), dict(
        id='cycle-pairing-faithfulness', status='resolved', verdict='constructed', depends_on=[],
        statement='Identify the actual quadratic pairing on the fixed degree-six Hodge space and distinguish norm faithfulness from route-phase blindness.',
        acceptance='Specify the polarization, domain, degree and pairing; prove or refute a nonzero radical on that domain and keep phase loss separate.',
        falsifier='An asserted positive pairing is indefinite or a claimed dark vector has nonzero norm; an invertible route-phase ambiguity is mislabeled a kernel.',
        next_action='Compare the fixed sixfold polarization/intersection pairing with the Hodge-Riemann positive form on the declared primitive sector, using the known Weil basis; do not infer a quadratic Hodge stage from the RH Pauli fixture.',
        deliverable='Source-defined pairing and exact radical/sign test, not an assumed algebraic obstruction.',
        sources=['research/voevodsky/hodge-weil-projector-v1.md', 'research/voevodsky/hodge-two-cotower-source-audit-v1.md', 'research/voevodsky/hodge-fixed-sixfold-quadratic-pairing-v1.md'])]
    nodes = [audit] + construction_tasks
    for n in c['conjectures']:
        prerequisite = 'cycle-pairing-faithfulness' if n['id']=='hodge-quadratic-dark-mode-erasure' else 'polystable-bundle-realization-boundary'
        nodes.append(dict(id=n['id'], status='open', verdict='open',
            statement=n['statement'], acceptance=n['acceptance'], falsifier=n['falsifier'],
            next_action=n['next_test'], deliverable='Source-bound test with all-cycle necessity and rational class descent, or scoped failure.',
            sources=n['sources'], depends_on=[prerequisite], required_verdicts={prerequisite:'constructed'},
            requires=['independent-necessity-after-projector-equivalence'] if n['id']=='hodge-quadratic-dark-mode-erasure' else []))
    ids = [n['id'] for n in c['conjectures']]
    # The objective is testing all registered alternatives, NOT requiring all to be true.
    nodes.append(dict(id='coherence-candidate-triage', status='open', verdict='open',
        statement='Record scoped dispositions of the four alternative conjecture tests.',
        acceptance='Each registered candidate has a reviewed scoped disposition; no logical conjunction of the alternatives is inferred.',
        falsifier='A source-blocked or untested candidate is counted as resolved.',
        next_action='Aggregate reviewed dispositions only after their tests.',
        deliverable='Candidate triage, not counterexample assembly.',
        sources=[c['guide']], depends_on=ids))
    return {'hodge': {'conjectures': nodes, 'interfaces': [],
                      'objective': {'target':'coherence-candidate-triage'}}}


def make_cards(nets):
    cards = []
    for n in nets['hodge']['conjectures']:
        if n['status'] != 'open':
            continue
        cards.append(dict(id='hodge:'+n['id'], first_action=n['next_action'],
            deliverable=n['deliverable'], acceptance=n['acceptance'], falsifier=n['falsifier'],
            reuse_sources=n['sources'], reuse_policy='Bind actual source operations; analogous scalar values are not source maps.',
            stop_rule='One bounded audit/test; stop at missing source data without treating it as a rejection.',
            review_promotion='Planning supplies no mathematical verdict or authority.'))
    return {'schema':'marici.conjecture-action-cards.v1', 'cards':cards,
            'source_sha256':{p:sha(p) for p in PATHS.values()}}


def render(r):
    lines = ['# Hodge workbench', '', 'Generated by the shared workbench through its Hodge adapter.', '',
        '**Numerical efficiency recommendation:** '+str(r['recommendation']),
        '**Unique ready action (structural, not a numerical ranking):** '+str(r['unique_ready_action']), '',
        r['score'], '', '**Source audit:** '+r['audit_disposition'], '',
        'The inconclusive RH cotower audit is not a universal prerequisite. Algebraic source-map construction is research work, not an externally supplied authority gate. The ready tasks below use independently specified cycle restriction and polarization operations.', '', '## Ready actions']
    for row in r['frontier']:
        card = row['action_card']
        lines += ['', '### '+row['id'], '', card['first_action'], '', '**Deliverable:** '+card['deliverable'],
                  '', '**Acceptance:** '+card['acceptance'], '', '**Falsifier:** '+card['falsifier'],
                  '', '**Sources:**'] + ['- `'+p+'`' for p in card['reuse_sources']]
    lines += ['', '## Blocked tests']
    for row in r['blocked']:
        lines.append('- `'+row['id']+'`: '+', '.join(b['id'] for b in row['blockers']))
    lines += ['', 'The four conjectures are alternatives. The triage objective is not their conjunction and is not the base counterexample-assembly theorem. A rejected construction does not unlock its selected downstream test. Dependencies select concrete research routes, not necessary implications between the full existential conjectures. New source construction remains executable. The quadratic binding has been merged with the base all-cycle projector gate; its external-prefixed dependency denotes an unproved mathematical premise, not an operator-supplied resource. A distinct argument can reopen it, but the identical norm reformulation is not a fresh task.', '',
        'Estimates are unknown until explicitly supplied; no invented probabilities, costs or information gain. Priorities in the lead register are not numerical forecasts.', '',
        'Edit `research/voevodsky/inputs/hodge-workbench-estimates.v1.json` and `hodge-workbench-action-cards.v1.json` for planning inputs. Source changes require reviewed input refresh rather than silent hash rebasing.', '',
        'Run `python research/voevodsky/checkers/check_conjecture_workbench.py --programme hodge`; add `--check` for freshness verification without output writes.', '']
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', action='store_true')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--record-audit-disposition', action='store_true')
    parser.add_argument('--refresh-topology', action='store_true')
    args = parser.parse_args(argv)
    require(not (args.record and args.check), 'choose record or check')
    c = load(PATHS['hodge']); validate_overlay(c)
    nets = adapter(c)
    if args.record:
        require(not (ROOT/ESTIMATES).exists() and not (ROOT/CARDS).exists(), 'refusing planning input overwrite')
        for path, data in ((ESTIMATES, initial(nets, PATHS)), (CARDS, make_cards(nets))):
            (ROOT/path).parent.mkdir(parents=True, exist_ok=True)
            (ROOT/path).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    planning, cards = load(ESTIMATES), load(CARDS)
    if args.record_audit_disposition:
        require(not args.check and not args.record and (ROOT/DISPOSITION).exists(), 'disposition refresh scope')
        fresh = initial(nets, PATHS)
        replacement = next(r for r in fresh['conjectures'] if r['id']=='hodge:'+AUDIT)
        planning['conjectures'] = [replacement if r['id']=='hodge:'+AUDIT else r for r in planning['conjectures']]
        cards['cards'] = [r for r in cards['cards'] if r['id']!='hodge:'+AUDIT]
        for path, data in ((ESTIMATES, planning), (CARDS, cards)):
            (ROOT/path).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    if args.refresh_topology:
        require(not args.check and not args.record and not args.record_audit_disposition, 'topology refresh scope')
        fresh = initial(nets, PATHS)
        old = {r['id']:r for r in planning['conjectures']}
        for i, row in enumerate(fresh['conjectures']):
            prior = old.get(row['id'])
            if prior is not None:
                require(prior['test']['acceptance']==row['test']['acceptance'] and prior['test']['falsifier']==row['test']['falsifier'], 'review changed planning gate')
                if row['probability']['status'] != 'not_applicable':
                    fresh['conjectures'][i] = prior
        planning = fresh
        fresh_cards = make_cards(nets)
        old_cards = {r['id']:r for r in cards['cards']}
        fresh_cards['cards'] = [old_cards.get(r['id'],r) for r in fresh_cards['cards']]
        cards = fresh_cards
        for path, data in ((ESTIMATES, planning), (CARDS, cards)):
            (ROOT/path).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    sources = [*PATHS.values(), c['relation_contract'], c['base_contract'], c['base_pins'], ESTIMATES, CARDS,
               'research/voevodsky/checkers/plan_hodge.py',
               'research/voevodsky/checkers/check_conjecture_workbench.py',
               'research/voevodsky/checkers/check_conjecture_test_planning.py']
    sources += sorted({p for n in nets['hodge']['conjectures'] for p in n['sources']})
    completed = (ROOT/DISPOSITION).exists()
    if completed:
        sources += [DISPOSITION, *load(DISPOSITION)['source_sha256']]
    r = build(nets, planning, cards, paths=PATHS, source_paths=sources)
    expected_ready = {'hodge:polystable-bundle-realization-boundary'}
    if not completed: expected_ready.add('hodge:'+AUDIT)
    require({x['id'] for x in r['frontier']} == expected_ready, 'construction frontier drift')
    # A rejected audit cannot satisfy a constructed-witness prerequisite.
    rejected = copy.deepcopy(nets)
    for node in rejected['hodge']['conjectures']:
        if node['id'] in ('polystable-bundle-realization-boundary','cycle-pairing-faithfulness'):
            node.update(status='resolved', verdict='rejected')
    from check_conjecture_workbench import blockers, index
    for n in c['conjectures']:
        require(any(b['gate']=='constructed_witness' for b in blockers('hodge:'+n['id'], index(rejected), rejected)), 'rejection unlocked binding')
    # Even an extreme synthetic score must not promote a blocked conjecture.
    hostile = copy.deepcopy(planning)
    target = next(x for x in hostile['conjectures'] if x['id']=='hodge:'+c['conjectures'][0]['id'])
    target['test']['protocol_status']='specified'
    target['probability'].update(status='estimated', values={'accepted':1,'rejected':0,'inconclusive':0}, basis='synthetic control', conditioning='synthetic', uncertainty='synthetic')
    target['test_cost'].update(status='estimated', assistant_effort_units=.001, basis='synthetic control')
    hr = build(nets, hostile, cards, paths=PATHS, source_paths=sources)
    require(target['id'] not in {x['id'] for x in hr['frontier']}, 'score bypasses blocker')
    r['unique_ready_action'] = r['frontier'][0]['id'] if len(r['frontier']) == 1 else None
    r['audit_disposition'] = 'completed_inconclusive' if completed else 'not_yet_run'
    r['validation_controls'] = ['source-construction-is-executable', 'rejection-cannot-supply-binding', 'score-cannot-bypass-blockers']
    text = render(r)
    if args.check:
        require(load(REPORT)==r and (ROOT/VIEW).read_text(encoding='utf-8')==text, 'Hodge workbench stale')
    else:
        (ROOT/REPORT).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
        (ROOT/VIEW).write_text(text,encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('passed','recommendation','unique_ready_action','coverage','validation_controls')}, indent=2))


if __name__ == '__main__':
    main()

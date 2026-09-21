# Three-prime balanced counit with relation-depth seam filtration

## Constructed synthesis

The three-prime Clark attachment is obtained by composing four existing layers:

1. the external pointed multi-input receiver;
2. the balanced derived counit with opposite prefix action;
3. the typed interval attachment and its Green mate;
4. the source relation filtration `I ⊃ I^2 ⊃ ...`.

No monoidal one-input shortcut is used.

For the layered three-prime graph, the degree-zero seam incidence complex has 12 edges and 8 vertices. Its incidence rank is 7, hence

    dim H_1(seam)=5.

These five seam cycles are distinct from the two marginal record ghosts. The latter belong to the joint-cut observation quotient; the former survive in the derived balanced composition before terminal compression.

## Relation layers

For the four-event source packet the exact coefficient calculation gives

    source dimension       384,
    terminal image rank    150,
    dim I                  234,
    dim I^2                 24,
    dim I/I^2              210.

Thus the derived negative layer detects the 210-dimensional conormal quotient, while the first multiplicative seam layer contributes 24 additional source relations. A faithful closure object must retain both layers and their multiplication map; `Tor_1` alone is insufficient.

## Required three-prime object

For each typed cut tree `T`, retain the complex

    C_T^(-1)=P tensor_B K_T tensor_B Q,
    C_T^0   =P tensor_B Q,

with

    d(p tensor k tensor q)=pk tensor q-p tensor kq.

The counit

    mu_T:C_T -> R

is balanced for the right-action/prefix-action pair. Its mate is the split-and-copy Green map. Cut coactions act on the typed source before applying `mu_T`; terminal memory is only the final quotient.

The three-prime construction must therefore carry the joint cut labels, the five-dimensional incidence seam space, the two marginal ghost directions, and the relation-depth filtration. Opposite reversal acts contravariantly on all of them.

## Verified boundaries

Passed exact fixtures establish:

- common-capacity all-state balancing and associativity;
- nonzero diamond seam class and two-endpoint boundary pushout;
- typed-unit readout without Hilbert--Schmidt prefix overcount;
- both three-prime marginal ghosts surviving projective attachment;
- terminal annihilation only after record compression;
- signed mates and cochain dual signs;
- independent four-event `I^2` products.

This synthesis does not claim a derived equivalence, a positive terminal metric, physical inverse events, or an infinite analytical completion. Its purpose is to fix the source-derived object that the full Clark comparison must act on.

Verification commands:

    uv run --with sympy python research/nima/checkers/check_typed_seam_composition.py
    uv run --with sympy python research/nima/checkers/check_joint_record_interval_attachment.py
    uv run --with sympy python research/grothendieck/checkers/check_source_relation_conormal_layer.py
    uv run --with sympy python research/nima/checkers/check_three_prime_seam_cycle.py

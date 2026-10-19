# Fixed mediator gates cannot faithfully replace the six exchange updates

## Result

**12 exact checks pass**, after freshly rebuilding the exchange comparison and
its source bindings. The simplest proposed contact/record identification fails
at composition, not merely at dimensions:

- the existing signed gates for one fixed contact projector commute;
- the six existing exchange updates do not;
- their commutator images span **all six evolving mismatch directions**.

Consequently any single global linear map intertwining every exchange port
with commuting target gates must erase the entire mismatch response. On the
full 22-coordinate exchange carrier it can retain only a function of the
16 conserved anchor coordinates.

This rules out that shortcut. It does not rule out the full contact model or
an endpoint-dependent, history-dependent or richer operation binding.

## Existing target law

For the existing fixed contact-singlet projector P and mediator flip X:

    R_plus  = (I-P) tensor I + P tensor X,
    R_minus = -(I-P) tensor I + P tensor X.

Exact rational matrices verify both involutions, their commutation, and the
previous positive-generator identity

    (I-R_plus)/2 + (I-R_minus)/2 = I - P tensor X.

These identities are checked in both contact and separated sectors. Every word
in this same two-gate family belongs to a commuting algebra. Choosing different
words for different proton ports does not remove the obstruction below.

## Source-side certificate

Let T_i be the already derived six-coordinate mismatch update at port i. Form
all fifteen commutators

    C_ij = T_i T_j - T_j T_i.

The matrix obtained by concatenating their columns has exact rank six. The
receipt exports an invertible six-column minor and its exact determinant.
The analogous commutators of the full 22-row exchange operators have rank six,
and the anchor map annihilates all of them. Its sixteen independent rows span
the entire common left annihilator.

This tests operator laws on the full carrier. A pair of ports in a commutator
need not be a valid sequential endpoint word. Therefore the conclusion is
specifically about a **single global intertwiner** of all six port operators,
not a proof against every typed path-dependent interpretation.

## Intertwiner obstruction

Suppose a linear map L satisfies L T_i = V_i L for every port and the target
operators V_i commute. Then

    L C_ij = (V_i V_j - V_j V_i) L = 0.

Since the images of C_ij span the entire mismatch space, L=0 on that space.
For the full exchange carrier the same argument says L factors through its
conserved anchor. This may preserve an inactive summary, but cannot preserve
the active exchange response demonstrated by the closed-word collision.

The result holds irrespective of target dimension or which commuting gate word
is assigned to a port. It does not assume a particular assignment and then tune
one to fail.

## Why this does not dispose of the contact Hamiltonian

The existing mediator also has an occupation operator n. Its commutator with X
is nonzero, checked explicitly. Thus the complete occupation-plus-contact
Hamiltonian is not restricted to the commuting signed-gate algebra above.
Port-dependent control projectors could also create noncommuting operations.
Neither extension comes with a supplied assignment from the six exchange ports
in this test.

Likewise, different maps at different geometric endpoints need not obey the
single-map intertwining equations used in the argument. Those alternatives
remain legitimate further tests, not established repairs.

## Structural consequence

The retained interface must not replace all six active mismatch records with
one fixed controlled flip while claiming operation preservation. The missing
contact adapter must account for noncommuting response, either through the
already present occupation/contact operations, additional justified controls,
or a genuinely typed family of maps. Merely retaining the common anchor would
hide the very response the previous synthesis recovered.

No new interaction, physical schedule, scalar coupling or contact policy was
introduced.

## Reproduction

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_exchange_contact_gate_comparison.py

Receipt: `results/exchange-contact-gate-comparison.json`.
The target gate equations are freshly checked with exact rational arithmetic;
the full contact energy/embedding producer is not rerun. Source files are hashed
and no owner contact receipt is modified.

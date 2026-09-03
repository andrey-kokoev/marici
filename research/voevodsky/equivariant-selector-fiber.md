# Equivariant selector fiber

## Question

How does reciprocal symmetry refine the distinction between existence and uniqueness of a filler selection?

## Claim boundary

The finite result classifies selectors for the declared reciprocal \(\mathbb Z/2\) fixture. It does not establish completed cutoff coherence.

## General classification

For an equivariant surjection

\[
B:X\to Y,
\]

any two equivariant right inverses differ by an element of

\[
\operatorname{Hom}_G(Y,\ker B).
\]

When an equivariant selector exists, its fiber is therefore an affine torsor over this intertwiner space. Existence requires one equivariant splitting; uniqueness additionally requires the intertwiner space to vanish.

## Exact fixture

Grothendieck's closure of the labelled filler fixture under reciprocal reflection gives:

- boundary rank 3;
- kernel dimension 7;
- reciprocal-even kernel dimension 4;
- reciprocal-odd kernel dimension 3.

The endpoint boundary representation is one-dimensional odd. Hence

\[
\dim\operatorname{Hom}_{\mathbb Z/2}(Y_{-},\ker B)=3.
\]

Our direct selector proves nonemptiness, but the three-dimensional torsor proves nonuniqueness. Equivariance removes some hidden directions without selecting one filler.

## Representative-change correction

The three-dimensional count is the strict chain-selector ambiguity. After adding the four reflection-closed representative-change triangles, their image has reciprocal character dimensions \((2,2)\). Therefore

\[
\dim H_1^+=4-2=2,
\qquad
\dim H_1^-=3-2=1.
\]

For odd endpoint output, invariant relative-class ambiguity is one-dimensional, not three-dimensional. A kernel-only count overstates invariant ambiguity by retaining cycles already killed by declared 2-cells.

## Completion consequence

At each cutoff, the selector set can be nonempty while carrying a positive-dimensional ambiguity torsor. Completed selection requires a compatible point across the cutoff system; cutoffwise existence alone does not construct one.

## Disposition

Representative-change 2-cells are structural, not optional bookkeeping. The apparatus must record the selector torsor and its transition maps, not only a Boolean existence certificate.

## Verification

- `research/voevodsky/equivariant-selector-fiber-contract-v2.json`
- `research/voevodsky/checkers/check_equivariant_selector_fiber_contract_v2.py`
- `research/voevodsky/results/equivariant_selector_fiber_contract_v2.json`
- `research/grothendieck/results/voevodsky-fixture-kernel-characters.json`
- `research/grothendieck/results/voevodsky-fixture-homology-characters.json`

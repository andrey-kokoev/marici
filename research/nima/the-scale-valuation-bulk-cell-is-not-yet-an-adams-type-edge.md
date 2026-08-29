# The scale-valuation bulk cell is not yet an Adams type edge

## Closest source candidate

The source records do contain a primitive-to-square construction, but it is not one of the missing Adams type-fiber edge maps.

For \(L=\log p\), compactified scale pullback and valuation transport commute up to the Gaussian bulk 2-cell
\[
\beta_{p,k}=W_{kL}-W_L.
\]
Adjacent depth cells are
\[
\alpha_{p,j}=W_{(j+1)L}-W_{jL},
\]
and telescope:
\[
\beta_{p,k}=\sum_{j=1}^{k-1}\alpha_{p,j}.
\]

For the primitive-to-square step,
\[
\alpha_{p,1}=W_{2L}-W_L.
\]

This is source-derived, coherent in valuation depth, and trivial on the compactified boundary.

## Why it does not fill the typed grade-six diamond

The missing Adams edge has type
\[
A_{2;p,1}:F_{p,1}\to F_{p,2}.
\]

The bulk cell \(\alpha_{p,1}\) instead compares two composites:

- scale pullback followed by valuation/Fock transport;
- valuation/Fock transport followed by scale pullback.

It is a 2-cell between functorial routes, not an object-level map between the primitive and square type fibers.

Conflating these would collapse:

- grade change;
- scale change;
- valuation pushforward;
- bulk comparison.

Therefore the current status remains that \(A_{2;p,1}\) is not constructed.

## Source-derived lax square

The correct source shape is a pseudocommutative square
\[
\begin{array}{ccc}
\mathcal F_{p,1}&\xrightarrow{\mathrm{scale}}&
\mathcal F_{p,1}^{(2L)}\\
\downarrow\mathrm{val}&&\downarrow\mathrm{val}\\
\mathcal F_{p,2}&\xrightarrow{\mathrm{scale}}&
\mathcal F_{p,2}^{(2L)}
\end{array}
\]
with comparison cell \(\alpha_{p,1}\).

The notation is schematic until all four corners are extracted from the source records. What is authorized is the existence and formula of the bulk comparison, not a strict square or a diagonal grade map.

This suggests that the Adams type lift may have to be a lax or correspondence-valued functor rather than a family of ordinary bounded maps.

## Filtration identity

The arithmetic side supplies
\[
E_p-I+N_p
=
\sum_{k\ge2}P_{p^k\mid n}.
\]
This identifies the square-and-higher remainder after primitive projection.

It supplies a filtration decomposition, not a canonical map from the primitive quotient into the square remainder.

A filtration step gives:

- a subobject or quotient relation;
- an exact or extension class;
- possibly a connecting morphism after additional boundary data.

It does not automatically give an invertible grade-change arrow.

## Operator-topology obstruction

The grade classes have distinct analytic status:

- primitive: continuous on the test rigging and not Hilbert–Schmidt on the unweighted prime Hilbert space;
- square: Hilbert–Schmidt;
- connected: nuclear.

An everywhere-defined invertible bounded map preserving these operator-ideal labels is not source-expected.

The candidate edge may instead be:

- a closable relation;
- a correspondence;
- a boundary connecting morphism;
- a map between defect spaces rather than full grade spaces.

This changes the typed diamond problem substantially: path comparison may live in a bicategory of correspondences, not an ordinary category of invertible operators.

## Closability gate

The existing rigged sewing criterion states that a proposed primitive-to-square incidence relation \(\Gamma_0\) must be closable. Its adjoint domain must be dense.

Only after closability may its mixed form be represented by a contraction
\[
W:\mathcal K_2\to\mathcal K_1,
\qquad
\|W\|\le1.
\]

This gives a concrete construction ladder:

1. derive \(\Gamma_{2;p,1}\) from the scale-valuation bulk cell and boundary identity;
2. prove it is densely defined and closable;
3. pass to defect spaces;
4. prove the normalized coupling is contractive;
5. decide whether the result defines an Adams edge, a correspondence, or only a comparison 2-cell.

## Revised four-edge request

Before demanding ordinary maps, classify each grade-change constructor
\[
1\to2,\quad1\to3,\quad2\to6,\quad3\to6
\]
as one of:

- bounded map;
- closed operator;
- closable relation;
- correspondence;
- higher comparison cell.

Both grade-six routes must then compose in one admitted bicategorical typing.

If one path composes operators and the other composes correspondences, an explicit comparison functor is required before the diamond is meaningful.

## Source-supported first edge packet

For \(1\to2\), the currently available packet is:

- arithmetic filtration remainder;
- Gaussian bulk cell \(\alpha_{p,1}\);
- compactified boundary triviality;
- proposed rigged incidence relation;
- closability criterion;
- contraction criterion on defect spaces.

Missing:

- the exact relation \(\Gamma_{2;p,1}\) derived from these pieces;
- proof of closability;
- proof of contractivity;
- declaration of its categorical edge type.

Thus even the first typed edge is one source derivation short of existence.

## New hostile

Take the source-derived bulk cell \(\alpha_{p,1}\) and declare it directly as
\[
A_{2;p,1}.
\]
This passes a scalar scale-difference observer, but its domain is a comparison of routes rather than \(F_{p,1}\), and its codomain is a Gaussian bulk space rather than \(F_{p,2}\).

The checker must reject this as an ill-typed promotion, not as a bad holonomy.

## Next exact construction

The next calculation should build the graph boundary identity
\[
q_{\mathrm{completed}}
=
q_1\oplus q_2+\partial_\Gamma J
\]
using the explicit bulk cell
\[
\alpha_{p,1}=W_{2\log p}-W_{\log p}.
\]

From this identity, extract the proposed relation \(\Gamma_{2;p,1}\), then verify:

- dense adjoint domain;
- closability;
- reciprocal compatibility;
- normalized coupling norm at most one;
- source and target defect-space typing.

Success constructs the first primitive-to-square edge as a contractive boundary correspondence. Only then should the remaining three grade-six edges be attacked by telescoped bulk cells.

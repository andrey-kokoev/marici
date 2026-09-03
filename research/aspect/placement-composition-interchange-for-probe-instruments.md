# Placement–composition interchange for probe instruments

## Question

How should simultaneous placement of instruments be separated from ordered composition of their state transformers?

## Claim boundary

This packet gives a strict finite tensor-product model and a hostile coupled fixture. Composition order is algebraic workflow order, not physical time. The construction does not assert that every coherence pyramid is monoidal or that every interaction admits a tensor factorization.

## Two independent directions

Use horizontal juxtaposition for independently placed instruments and vertical composition for compatible transformers. For two placement loci with transformers \(A_i\) and \(B_i\), horizontal placement is represented by tensor product:

\[
A_i\mathbin{\square}B_i=A_i\otimes B_i.
\]

Vertical composition is ordinary map composition. The interchange comparison is

\[
(A_2\otimes B_2)(A_1\otimes B_1)
\longrightarrow
(A_2A_1)\otimes(B_2B_1).
\]

For independent tensor factors this comparison is equality. It is the strict interchange law

\[
(A_2\otimes B_2)(A_1\otimes B_1)
=(A_2A_1)\otimes(B_2B_1).
\]

This separates two questions:

1. which instruments are jointly placeable;
2. how each placed instrument composes with compatible transformers.

Joint placeability does not imply that vertical compositions commute. In general \(A_2A_1\ne A_1A_2\).

## Coupled square

Insert a coupling map \(K\) between the two compositional layers:

\[
(A_2\otimes B_2)K(A_1\otimes B_1).
\]

If this differs from \((A_2A_1)\otimes(B_2B_1)\), the square is not an independent interchange square. The difference is an additive residual only because the example lives in integer matrices. Categorically, the coupled route requires its own comparison 2-cell; it cannot be silently treated as tensor-factorized placement.

The coupling may still be a lawful joint instrument. Failure of strict interchange diagnoses dependence between loci, not invalidity of the joint operation.

## Finite witness

The diagnostic chooses noncommuting exact integer \(2\times2\) matrices for the \(A\)-locus and compatible matrices for the \(B\)-locus. It verifies strict tensor interchange, dimension and identity laws, and noncommutativity of vertical composition. A non-product \(4\times4\) coupling produces a nonzero interchange residual.

## Interaction Net interpretation

- horizontal wires encode jointly placed, interface-independent instruments;
- vertical wire concatenation encodes typed transformer composition;
- an empty square claims strict or witnessed interchange;
- a coupled cell carries the comparison between the joint route and the factorized route;
- erasing that cell is valid only when the interchange comparison is invertible in the admitted equivalence class.

## Falsifiers

1. A shared-state coupling rejects tensor-independent placement.
2. Joint admissibility does not authorize swapping composition order.
3. Equal terminal scalar records do not establish equality of transformer squares.
4. A matrix difference is unavailable outside an additive target; a generic comparison cell must be used instead.
5. Algebraic composition order has no physical-time interpretation without a separate map to a physical-time object.

## Disposition

A strict double-direction prototype exists: tensor juxtaposition models independent placement and vertical map composition models instrument chaining. Interchange holds exactly for independent factors and fails with a typed nonzero residual under coupling. This gives SCC a criterion for when two placed instruments may be compiled separately and when a joint interaction cell is required.

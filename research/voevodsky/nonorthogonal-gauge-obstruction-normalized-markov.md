# Nonorthogonal gauge obstruction for normalized Markov kernels

## Question

Can arbitrary invertible fiber maps be added as gauge-like vertical automorphisms of normalized operator-valued Markov objects?

## Claim boundary

This is a no-go theorem for vertical automorphisms acting by block congruence on normalized kernels with diagonal blocks \(I_{H_i}\). It does not rule out a larger category with metric data, unnormalized covariance blocks, or noninvertible stochastic morphisms.

## Obstruction

Let a vertex map \(S_i:H_i\to H_i\) act on a block kernel by congruence:

\[
K_{ij}\longmapsto S_iK_{ij}S_j^T.
\]

Since every normalized object satisfies \(K_{ii}=I_{H_i}\), its transformed diagonal block is

\[
S_iI_{H_i}S_i^T=S_iS_i^T.
\]

The transformed object remains normalized exactly when

\[
S_iS_i^T=I_{H_i}.
\]

For invertible square maps this is precisely orthogonality. Therefore the orthogonal gauge groupoid is not an arbitrary restriction: it is the maximal congruence automorphism groupoid preserving the current object signature.

## Hostile fixtures

A rational shear and a nonunit diagonal scaling both preserve dimension and invertibility but change the diagonal covariance block. Applying the usual transformed-edge formula cannot repair this defect because edge data do not alter \(K_{ii}\).

## Consequence for equipment

Freely adjoining companions for such nonorthogonal maps would create horizontal arrows whose alleged targets are absent from the normalized object class. Unit and counit cells cannot fix a missing target object. An extension must instead enlarge objects to pairs \((H_i,M_i)\) with positive metric/covariance blocks and type transport by

\[
M_i\longmapsto S_iM_iS_i^T.
\]

That enlarged construction requires new positivity, composition, Beck–Chevalley, and completion proofs.

## Disposition

Arbitrary invertible vertical gauges are falsified for the normalized Markov equipment. Orthogonal gauges exhaust normalized congruence automorphisms. General vertical maps remain a distinct proposed extension, not an omitted case of the current theorem.

## Verification

- `research/voevodsky/checkers/check_nonorthogonal_gauge_obstruction.py`
- `research/voevodsky/results/nonorthogonal_gauge_obstruction.json`

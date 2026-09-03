# Coherent finite Gram certificates are the positive meta-observers

## Question

What should an order-enriched meta-observer return, beyond a scalar inequality, so that infinitely many finite observations assemble into one positive source object?

## Finite observer category

Fix one Gaussian width. Let an object `I` be a finite translate packet

\[
I=(a_1,\ldots,a_n).
\]

Morphisms are inclusions, permutations, and repetitions of packets. The completed source identities determine a Hermitian matrix

\[
G_I=(K_\sigma(a_i-a_j))_{i,j}.
\]

Conformance under a packet map `r:I->J` requires

\[
G_I=r^*G_Jr,
\]

with the corresponding convention for restriction or repetition.

## Certificate-valued observers

A positivity meta-observer should not return only the proposition `G_I>=0`. It should return a factorization certificate

\[
G_I=R_I^*R_I
\]

in a source-typed pre-Hilbert object. For every packet map, there must be an isometry between certificate spaces making the factorization natural:

\[
R_I=U_{JI}R_Jr,
\qquad
U_{JI}^*U_{JI}=1.
\]

The isometries must compose on triples. These cells are the conformance identities of the positive certificates themselves.

## Assembly theorem

If such certificates exist coherently for every finite packet, their directed colimit constructs a pre-Hilbert space `H` and vectors `v_a` satisfying

\[
K_\sigma(a-b)=\langle v_a,v_b\rangle_H.
\]

Completion gives the Kolmogorov decomposition of the full difference kernel. Translation of packet labels induces an isometric representation because the kernel depends only on differences. The spectral theorem then gives a positive Fourier measure, and Gaussian division recovers positivity of the completed Weil distribution.

Conversely, any positive Fourier measure supplies the coherent family by

\[
v_a(u)=e^{-iau}
\]

in the Gaussian-weighted `L^2` space. Thus coherent finite certificate data are equivalent to the missing global positive constructor.

## Relation to the lower pyramids

The lower prime and completion pyramids already determine the entries of every `G_I`. Their conformance observers prevent changing cutoffs or normalizations with `I`. The new requirement is stronger: the same source calculus must determine `R_I` and the comparison isometries, not merely `G_I`.

This gives the operator's “observers observing observers” a precise role. First-level observers produce finite source matrices. Second-level observers compare their positive certificates under every refinement. The infinite colimit is the positive apex.

## Strongest falsification attempt

Independent Cholesky factorizations do not qualify. They exist exactly when each finite matrix is already known PSD and carry arbitrary unitary choices. Without source-derived comparison isometries they do not define a common constructor and merely restate the target.

Likewise, observer-dependent regularization can make each bounded packet positive while failing composition under inclusion. One failed certificate square localizes the inconsistency.

## Disposition

Replace “prove infinitely many inequalities” by “construct a coherent Kolmogorov system from the lower source pyramids.” This does not weaken RH, but it names the exact higher object that would prove every observer inequality simultaneously and makes compatibility mechanically falsifiable at finite overlaps.

# Theta centered prime incidence is an independent arithmetic-staircase readout

## Status

Exact observation-rank theorem. The absolutely convergent centered
prime-interval incidence can be rewritten as a half-Mellin transform of the
theta source multiplied by a cumulative prime-power staircase.

This staircase is nonconstant and discontinuous at logarithmic prime-power
locations. Consequently the centered incidence is independent of the old
half-amplitude, every fixed finite spectral-jet family, and every fixed finite
seam-jet family on the ambient source module.

This is the first completed multiplicative boundary port in the current lane
with genuine observation-rank increment. Its orientation remains unproved.

## Centered interval sum

For prime-power displacement

\[
\ell_{p,k}=k\log p,
\]

the centered interval current is

\[
\widetilde B_{p,k}[A](z)
=-\int_{k\log p}^{\infty}A(v)e^{izv}\,dv.
\]

Let (w_{p,k}\) be either an authorized finite packet or one of the completed
arithmetic weight systems for which the centered series converges. Define

\[
\widetilde{\mathcal I}_w[A](z)
=\sum_{p,k}w_{p,k}\widetilde B_{p,k}[A](z).
\]

Absolute convergence permits exchanging the sum and integral.

## Arithmetic staircase

Define

\[
W_w(v)
=\sum_{p,k:\,k\log p\leq v}w_{p,k}.
\]

For each finite (v\), only finitely many prime powers occur. Then

\[
\widetilde{\mathcal I}_w[A](z)
=-\int_0^\infty
W_w(v)A(v)e^{izv}\,dv.
\]

Thus the centered incidence is the half-Mellin readout of the source after
multiplication by the arithmetic staircase (W_w\).

For logarithmic-derivative normalization,

\[
W_{\mathrm{LD}}(v)
=\sum_{p^k\leq e^v}
(\log p)p^{-k/2}.
\]

For Euler-log normalization,

\[
W_{\log}(v)
=\sum_{p^k\leq e^v}
\frac1k p^{-k/2}.
\]

Primitive, square, and higher channels correspond to restricting the staircase
to (k=1\), (k=2\), and (k\geq3\), respectively.

## Discontinuity structure

The staircase jumps at every admitted logarithmic prime-power location

\[
v=k\log p.
\]

The jump size is exactly (w_{p,k}\), with coincident labels combined according
to the typed arithmetic source. This preserves prime-power provenance after
completion.

Between jumps, (W_w\) is constant. It is neither a global constant nor a
polynomial in (v\) for any nontrivial infinite arithmetic packet.

## Independence from the half-amplitude

The old half-amplitude is

\[
H_A(z)=\int_0^\infty A(v)e^{izv}\,dv.
\]

If the staircase readout were a scalar multiple of (H_A\) for all test
sources, then multiplication by (W_w\) would equal a constant almost
everywhere. The prime-power jumps rule this out.

The observation-rank increment over the half-amplitude is therefore one for a
single nontrivial staircase row.

## Independence from finite spectral jets

Spectral differentiation gives

\[
\partial_z^jH_A(z)
=\int_0^\infty(iv)^jA(v)e^{izv}\,dv.
\]

A finite linear combination of spectral jets corresponds to multiplication by
a polynomial in (v\). Since (W_w\) is a discontinuous staircase, it cannot
equal such a polynomial almost everywhere.

Therefore the centered incidence is independent of every fixed finite
spectral-jet packet.

## Independence from finite seam jets

Seam jets depend only on the germ of (A\) at (v=0\). Choose smooth test
sources supported inside two small intervals away from the seam and lying on
opposite sides of one prime-power jump. Their seam jets all vanish, while the
staircase acts by different constants on the two supports.

No finite seam-jet combination can reproduce the staircase readout.

The same support argument proves independence from the combined span of finite
spectral and seam jets.

## Source-module qualification

The rank theorem is proved on an ambient test-source module rich enough to
localize around prime-power jumps. On the single fixed theta source, every
readout is merely one scalar function of (z\), and algebraic dependence can be
manufactured by division. Such pointwise ratios carry no authority.

The correct claim is that the staircase row is an independently constructed
source functional before evaluation on theta. Its restriction to a narrower
source-generated module must retain rank through an explicit kernel test.

## Reciprocal pair

The two reciprocal staircase currents are

\[
\widetilde{\mathcal I}_w^\pm[A](z)
=-\int_0^\infty
W_w(v)A(v)e^{\pm izv}\,dv.
\]

For real (A\) on the seam they are conjugate. Their symmetric and
antisymmetric combinations are weighted cosine and sine readouts.

They add two arithmetic transverse channels before scalar aggregation, but
conjugacy and positivity of (W_wA\) do not forbid either transform from
vanishing.

## Orientation boundary

If the arithmetic weights are positive, (W_w\) is nonnegative and
nondecreasing. Hence

\[
-\widetilde{\mathcal I}_w[A](0)>0
\]

for positive nonzero (A\). At nonzero spectral phase, oscillatory cancellation
remains possible.

No universal sign or half-plane exclusion follows merely from monotonicity of
the staircase. A hostile test must preserve the same staircase and alter the
archimedean source within the admitted source class.

## Finite matrix falsifier

Choose test atoms supported in intervals separated by one prime-power jump.
The old amplitude row assigns both atoms the same local coefficient after
normalization, while the staircase row assigns coefficients differing by the
jump weight.

The resulting (2\times2\) observation minor is nonzero. This is the smallest
finite witness of rank increment.

Conversely, any proposed factorization through finite jets is killed by the
same two-support minor.

## Consequence

The multiplicative boundary branch has passed its first decisive gate:

- its new centered current completes absolutely;
- it retains typed prime-power jumps;
- it is not a graph coordinate over any finite additive jet state;
- it adds genuine observation rank before theta evaluation.

The next RH-bearing test is now sharply finite in type, though infinite in
arithmetic content: derive the completed reciprocal Green identity containing
the staircase pair and determine whether its contribution to the transverse
(X/Y\) channel has a source-fixed sign, phase sector, or conservation law. A
single hostile source with the same staircase and an off-seam scalar zero would
close orientation while preserving the incidence theorem.

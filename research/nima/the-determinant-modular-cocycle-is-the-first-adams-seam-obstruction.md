# The determinant modular cocycle is the first Adams-seam obstruction

## First source-specific filter

Before solving the full common-metric equations
\[
T_e^*G_tT_e=G_s,
\]
take determinants. For an edge \(e:s\to t\) between \(d\)-dimensional fibers,
\[
|\det T_e|^2\det G_t=\det G_s.
\]
Therefore
\[
\log\det G_s-\log\det G_t
=
2\log|\det T_e|.
\]

Define the modular edge cochain
\[
\mu(e)=\log|\det T_e|.
\]
A necessary condition for simultaneous unitarization is that \(\mu\) be an exact edge potential:
\[
\mu(e)=\phi(s)-\phi(t),
\qquad
\phi(s)=\tfrac12\log\det G_s.
\]

## Cycle character

For every authorized cycle \(\gamma\),
\[
\sum_{e\in\gamma}\mu(e)=0.
\]
Equivalently,
\[
|\det H_\gamma|=1.
\]

This is the determinant character of the holonomy representation. Any nonzero cycle sum is an immediate scalar obstruction to a common positive invariant metric.

The determinant filter is cheap and must precede spectral, Jordan, and common-metric tests.

## Exactness versus finite cycle neutrality

On a finite connected graph, vanishing on a cycle basis implies algebraic exactness: choose a base vertex and integrate \(\mu\) along tree paths to define \(\phi\).

At completion, however, finite exactness is insufficient. The potentials may drift:
\[
\sup_s|\phi_X(s)|\to\infty.
\]
Then the determinant metric scale
\[
\det G_{X,s}=e^{2\phi_X(s)}
\]
is not uniformly equivalent to the source determinant scale.

Thus the completion criterion is a bounded coboundary:
\[
\mu_X=d\phi_X,
\qquad
\sup_{X,s\in C}|\phi_X(s)|<\infty
\]
after one frozen normalization, such as \(\phi_X(s_0)=0\).

Both \(\phi\) and \(-\phi\) are controlled by the absolute bound.

## Adams-seam decomposition

Suppose a typed edge factors as
\[
T_e=A_eU_e,
\]
where \(U_e\) is moving-seam geometric transport and \(A_e\) is the weighted Adams/type-fiber coefficient.

If \(U_e\) is unitary in the source metric,
\[
|\det U_e|=1,
\]
so
\[
\mu(e)=\log|\det A_e|.
\]

If \(A_e=a(e)I\) on a \(d_e\)-dimensional fiber,
\[
\mu(e)=d_e\log a(e).
\]
The fiber dimension and grade are part of the label. Using only \(\log a(e)\) loses multiplicity.

If seam transport changes fiber metrics or dimensions, its determinant contribution must be included rather than declared zero.

## Moving-seam cancellation

The source-specific question is whether Adams accumulation is exactly cancelled by a seam metric potential:
\[
\log|\det A_e|
+
\log|\det U_e|_{\mathrm{source\ frames}}
=
\phi(s)-\phi(t).
\]

“Unitary geometric transport” proves the second determinant is zero only in authorized orthonormal source frames. Nonunitary trivializations can move modular weight between the two factors.

Therefore \(\mu\) must be computed from the full authorized edge matrix in frozen source frames.

## Three coefficient lenses

### Additive lens

Records the logarithmic accumulation
\[
\sum_e\mu(e).
\]
It exposes where positive scales are gained or lost along a path.

### Determinant lens

Records the multiplicative cycle character
\[
\chi(\gamma)=|\det H_\gamma|
=
\exp\!\left(\sum_{e\in\gamma}\mu(e)\right).
\]
It detects scalar holonomy obstruction.

### Ordered lens

After determinant cancellation, records the residual matrix holonomy in \(SL\)-type directions. It detects noncommutative spectral, Jordan, and common-metric failures invisible to determinants.

These lenses are noninterchangeable.

## Minimal hostile I: cycle defect

Take a one-dimensional cycle with edge weights \(a_1,\ldots,a_n\) and
\[
\prod_ja_j\neq1.
\]
Then
\[
\sum_j\mu(e_j)\neq0.
\]
No positive metric can unitarize the transport.

## Minimal hostile II: bounded cycles, unbounded potential

Take a path of length \(n\) with
\[
\mu(e_j)=\log c,\qquad c>1,
\]
and close the cycle with
\[
\mu(e_{\mathrm{close}})=-n\log c.
\]
Every cycle sum vanishes. The normalized potential is
\[
\phi(j)=-j\log c,
\]
whose oscillation grows like \(n\log c\).

Finite exactness holds, but no uniformly bounded completion potential exists.

## Minimal hostile III: determinant passes, ordered holonomy fails

Use the two-involution example where each generator has determinant \(-1\), so the product has determinant \(1\), but the product is a nontrivial unipotent Jordan block.

The modular cocycle vanishes. Simultaneous unitarization still fails at the ordered lens.

This demonstrates that determinant exactness is necessary, not sufficient.

## Finite algorithm

For each cutoff:

1. build the authorized directed transport graph;
2. compute full typed edge matrices in frozen source frames;
3. record
   \[
   \mu(e)=\log|\det T_e|;
   \]
4. choose a spanning tree and integrate a normalized potential \(\phi_X\);
5. test every non-tree edge for cycle residual;
6. report the shortest nonzero cycle sum;
7. if exact, record the oscillation
   \[
   \operatorname{osc}\phi_X
   =
   \max\phi_X-\min\phi_X.
   \]

The potential is unique up to an additive constant on each connected component, so oscillation is gauge-invariant.

## Completion algorithm

Track, on each compact off-seam region,
\[
\sup_X\operatorname{osc}\phi_X.
\]
A finite bound gives a uniformly bounded determinant-scale reweighting. Divergence proves completion instability at the modular level.

For projective seminorm families, repeat the calculation for each determinant-grade block or finite-dimensional quotient used by the constructor. Infinite-dimensional determinants require a separately authorized regularized determinant; they cannot be inserted formally.

## Cheap obstruction hierarchy

The concrete Adams-seam audit now proceeds:

1. determinant modular cocycle;
2. holonomy word spectra and Jordan forms;
3. common positive invariant metric;
4. uniformly bi-bounded conjugators;
5. compatibility with source authority and restricted-product completion.

Failure at an earlier stage blocks every later claim.

## Next source calculation

Extract the exact weighted Adams edge coefficients and seam-frame determinants from the constructed SCC inhabitants. For every grade block, compute:

- \(d_e\log a(e)\);
- seam determinant contribution;
- cycle residuals;
- normalized potential oscillation;
- cutoff and reciprocal/Real naturality.

If the bounded-potential test passes, the remaining obstruction is genuinely noncommutative and belongs to the ordered holonomy audit.

# Operator-log metric control replaces determinant-potential bounds at completion

## Correction

The finite determinant character remains a valid cycle obstruction, but the scalar determinant potential is not the correct completion norm when fiber dimension grows.

For example,
\[
G_X=2I_{n_X}
\]
satisfies the uniform metric equivalence
\[
2I\le G_X\le2I,
\]
while
\[
\log\det G_X=n_X\log2\to\infty.
\]
Thus divergence of a raw finite-rank log determinant can reflect only growing dimension, not metric degeneration.

## Correct completion criterion

The invariant metrics must satisfy
\[
mI\le G_X\le MI
\]
with \(0<m\le M<\infty\) uniform over cutoff, constructor depth, and compact off-seam regions.

Equivalently,
\[
\|\log G_X\|_{\mathrm{op}}\le C.
\]

This controls the extremal logarithmic scale per direction rather than the sum of scales over an increasing number of directions.

If
\[
G_X=S_X^*S_X,
\]
the criterion is equivalent, after a frozen normalization, to separate uniform bounds on \(S_X\) and \(S_X^{-1}\).

## Finite determinant character

At finite rank, define
\[
\mu_X(e)=\log|\det T_{X,e}|.
\]
For every finite authorized cycle \(\gamma\),
\[
\sum_{e\in\gamma}\mu_X(e)=0,
\]
equivalently
\[
|\det H_{X,\gamma}|=1.
\]

This remains a cheap necessary test for finite simultaneous unitarizability.

It does not supply the completion metric bound.

## Why scalar potentials fail with growing rank

From
\[
T_e^*G_tT_e=G_s
\]
one obtains
\[
\log\det G_s-\log\det G_t
=
2\log|\det T_e|
\]
only in finite dimension.

Writing
\[
\phi_X(s)=\tfrac12\log\det G_{X,s}
\]
aggregates all eigenvalue logarithms:
\[
\phi_X(s)=\tfrac12\sum_{j=1}^{n_X}\log\lambda_j(G_{X,s}).
\]
Even if every eigenvalue lies in \([m,M]\), this sum can grow linearly with \(n_X\).

Therefore bounded \(\phi_X\) is too strong and can falsely reject uniformly equivalent metrics.

## Operator-valued logarithmic potential

The completion object is
\[
L_{X,s}=\log G_{X,s},
\]
defined by functional calculus for positive \(G_{X,s}\).

Uniform equivalence is exactly
\[
-CI\le L_{X,s}\le CI.
\]

The metric transport equation can be retained in multiplicative operator form:
\[
T_e^*e^{L_t}T_e=e^{L_s}.
\]
No additive identity
\[
L_s-L_t=\cdots
\]
is available in general because of noncommutativity.

Hence the operator-log potential belongs to the ordered lens, not merely the additive determinant lens.

## Four typed determinant regimes

### Finite determinant character

Ordinary determinants are authorized on finite-rank cutoff fibers and provide necessary cycle tests.

### Relative determinant line

If holonomy is determinant-class relative to a declared reference, for example
\[
H-I\in\mathcal S_1,
\]
a Fredholm or relative determinant may be available. The ideal class, reference operator, and multiplicativity domain must be explicit.

### Regularized determinant

A higher regularized determinant may be used only when the corresponding Schatten ideal and anomaly terms are source-authorized. It cannot silently replace an unavailable Fredholm determinant.

### No determinant

When no determinant-class structure exists, retain the full operator holonomy and operator-log metric. Do not invent an infinite determinant.

## Relative determinant warning

Even when a Fredholm determinant exists,
\[
|\det_FH_\gamma|=1
\]
is only a determinant-line necessary condition. It does not imply spectral semisimplicity, compact holonomy closure, or a common positive metric.

Regularized determinants may also carry multiplicative anomalies. These belong to typed coherence data and cannot be ignored.

## Corrected hostile I: valid frame with divergent determinant

Take
\[
G_X=2I_{n_X},\qquad n_X\to\infty.
\]
Then
\[
\|\log G_X\|_{\mathrm{op}}=\log2
\]
uniformly, while
\[
\log\det G_X=n_X\log2\to\infty.
\]

A determinant-potential completion test rejects this valid frame incorrectly. The operator-log test passes.

## Corrected hostile II: hidden one-direction degeneration

Let
\[
G_X=\operatorname{diag}(e^{-X},1,\ldots,1).
\]
Then the normalized average log determinant can become small when dimension grows faster than \(X\), yet
\[
\|\log G_X\|_{\mathrm{op}}=X\to\infty.
\]
The lower metric bound collapses in one direction.

Thus averaged or dimension-normalized determinant data can also miss genuine degeneration.

## Correct hierarchy

The Adams-seam audit is now:

1. finite determinant character on each finite cycle;
2. word spectra and Jordan form;
3. one common positive invariant metric;
4. operator-log bound
   \[
   \sup\|\log G_X\|_{\mathrm{op}}<\infty;
   \]
5. separate uniform conjugator bounds;
6. source authority and completion compatibility.

At infinite rank, insert a relative determinant step only when ideal-class authority exists.

## Revised finite-to-complete certificate

For each finite cutoff, record:

- rank and grade decomposition;
- ordinary determinant character of cycle holonomies;
- one common invariant metric \(G_X\);
- extremal eigenvalues of \(G_X\);
- \(\|\log G_X\|_{\mathrm{op}}\);
- conjugator norms;
- any declared determinant-class relation to a reference.

Across cutoff, test spectral envelopes rather than raw log determinants.

## Source-specific next calculation

The Adams coefficient still contributes to finite determinants grade by grade. Use those determinants only to reject nonunit-modulus finite cycle characters.

If they pass, solve the common metric equations and track
\[
\lambda_{\min}(G_X),\qquad
\lambda_{\max}(G_X).
\]
Only these spectral quantities determine uniform metric equivalence.

For any proposed infinite determinant line, first prove trace-class or other declared ideal membership of the relative holonomy. Without it, the ordered matrix/operator audit is the sole authorized continuation.

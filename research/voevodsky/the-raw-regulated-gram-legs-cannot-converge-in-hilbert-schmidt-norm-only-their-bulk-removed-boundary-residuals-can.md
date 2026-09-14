# The raw regulated Gram legs cannot converge in Hilbert--Schmidt norm; only their bulk-removed boundary residuals can

## Raw strong-limit proposal

A proposed positive regulator criterion asked for

\[
B_{\Lambda,R,N,\chi}
\to
B_\chi^{rel},
\qquad
C_{\Lambda,R,N,\chi}
\to
C_\chi^{rel}
\]

in ordinary Hilbert--Schmidt norm.

This is impossible for the raw outside/annular leg as `R -> infinity` whenever the observer has nonzero Plancherel density.

## Translation-model obstruction

Let `A_k` be convolution by a nonzero `L2` kernel `k` and let

\[
P_{L,M}^{ann}
=1_{(L,M]}.
\]

Before the Fourier cutoff modifies boundary terms,

\[
\|A_kP_{L,M}^{ann}\|_{HS}^2
=
(M-L)\|k\|_2^2.
\]

More generally, for a Fourier projection that converges to the identity in bulk density,

\[
\boxed{
\|Q_\Lambda
P_{L,M}^{ann}A_k\|_{HS}^2
=
(M-L)\tau(A_k^*A_k)
+o(M-L).
}
\]

Thus

\[
\|C_{\Lambda,R}\|_{HS}
\asymp
\sqrt{
\log R-
\log\Lambda
}
\]

for nonzero observer density.

No family with diverging norm can converge in Hilbert--Schmidt space.

## Consequence

The raw strong criterion

\[
B_\alpha\to B^{rel},
\qquad
C_\alpha\to C^{rel}
\quad\text{in }\mathcal L^2
\]

is falsified for the positive completion.

The second cutoff makes the Gram matrix legitimate at each finite `R`; it does not make the raw outside feature convergent as the cutoff is removed.

## Required bulk removal

Let

\[
\Pi_{in,\alpha}^{bulk},
\qquad
\Pi_{ann,\alpha}^{bulk}
\]

be the cutoff-dependent orthogonal projections onto the two channelwise Plancherel bulk modules. Define residual legs

\[
\boxed{
\widetilde B_\alpha
=
(I-\Pi_{in,\alpha}^{bulk})
B_\alpha,
}
\]

\[
\boxed{
\widetilde C_\alpha
=
(I-\Pi_{ann,\alpha}^{bulk})
C_\alpha.
}
\]

Each residual must also be transported by endpoint recentering maps

\[
R_{in,\alpha},
\qquad
R_{ann,\alpha}
\]

into fixed boundary Hilbert spaces.

The viable positive criterion is

\[
\boxed{
R_{in,\alpha}
\widetilde B_\alpha
\longrightarrow
B^{bdry},
\qquad
R_{ann,\alpha}
\widetilde C_\alpha
\longrightarrow
C^{bdry}
}
\]

in Hilbert--Schmidt norm.

## Positive residual Gram matrix

At finite regulator, orthogonal bulk removal preserves positivity. The residual Gram matrix is

\[
\boxed{
\widetilde{\mathcal G}_\alpha
=
\begin{pmatrix}
\langle\widetilde B_\alpha,
\widetilde B_\alpha\rangle&
\langle\widetilde B_\alpha,
\widetilde C_\alpha\rangle\\
\langle\widetilde C_\alpha,
\widetilde B_\alpha\rangle&
\langle\widetilde C_\alpha,
\widetilde C_\alpha\rangle
\end{pmatrix}
\succeq0.
}
\]

If the recentered residual legs converge, then

\[
\widetilde{\mathcal G}_\alpha
\longrightarrow
\begin{pmatrix}
\langle B^{bdry},B^{bdry}\rangle&
\langle B^{bdry},C^{bdry}\rangle\\
\langle C^{bdry},B^{bdry}\rangle&
\langle C^{bdry},C^{bdry}\rangle
\end{pmatrix}
\succeq0.
\]

This is the correct positive boundary limit.

## Why raw product convergence can still hold

The signed sewing product

\[
B_\alpha^*C_\alpha
\]

may have a trace-norm or relative-trace limit even though both factors diverge in Hilbert--Schmidt norm. Bulk contributions can cancel because the inner and annular windows are orthogonal or because the product cutoff observes only one row.

Therefore the minimal signed criterion remains possible:

\[
B_\alpha^*C_\alpha
\to
T^{rel}
\quad\text{in }\mathcal L^1
\]

or in an admitted relative trace topology.

But it does not produce a positive Gram limit.

## The one-sided inner channel

For Connes's actual half-line physical cutoff, the inner raw leg may itself fail to be Hilbert--Schmidt before the Fourier projection is included. Its bulk projection cannot be defined by finite-window right compression alone.

Thus `Pi_(in,alpha)^bulk` must be constructed from the positive time--frequency operator

\[
P_\Lambda Q_\Lambda P_\Lambda
\]

and its Plancherel density, while the annular bulk can be modeled by finite right compression.

The two channel bulk projections have different constructions and must be compared only after entering the common regulated Gram space.

## Corrected regulator theorem

The positive regulator comparison now has four steps:

1. construct the inner time--frequency bulk projection;
2. construct the annular right-compression bulk projection;
3. subtract both orthogonally at finite `(Lambda,R,N)`;
4. recenter and prove Hilbert--Schmidt convergence of the residual legs with a square-summable angular majorant.

The resulting limiting off-diagonal Gram entry must then be identified with the Tate relative projection trace.

## Revised acceptance criteria

### Signed `C_34`

Prove convergence of the combined product in trace norm or relative trace:

\[
\boxed{
B_\alpha^*C_\alpha
\to
T^{rel}.
}
\]

### Positive `C_34`

Construct bulk projections and prove

\[
\boxed{
R_{in,\alpha}
(I-\Pi_{in,\alpha}^{bulk})B_\alpha
\to B^{bdry},
}
\]

\[
\boxed{
R_{ann,\alpha}
(I-\Pi_{ann,\alpha}^{bulk})C_\alpha
\to C^{bdry}.
}
\]

Only the second criterion yields a positive limiting Gram feature.

## Refinement impact

Bulk removal and endpoint recentering are independent semantic operations:

\[
\text{regulated Gram leg}
\to
\text{bulk projection}
\to
\text{orthogonal residual}
\to
\text{recentered boundary leg}.
\]

They should remain separate nodes in the positive nonuniform refinement.

## Disposition

The raw Hilbert--Schmidt leg convergence criterion is impossible:

\[
\boxed{
\|C_{\Lambda,R}\|_{HS}^2
\sim
(\log R-
\log\Lambda)
h(1)
\to\infty.
}
\]

The positive boundary problem must be posed for bulk-removed and recentered residual legs. Signed product convergence remains a weaker independent possibility.

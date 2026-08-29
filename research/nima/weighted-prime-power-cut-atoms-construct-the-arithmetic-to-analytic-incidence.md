# Weighted prime-power cut atoms construct the arithmetic-to-analytic incidence

## Source atoms

For every prime-power label \((p,k)\), set

\[
a_{p,k}=k\log p
\]

and define the exact tail–seam cut atom

\[
u_{p,k}
=
\begin{pmatrix}
g_{a_{p,k}}\\
h_{a_{p,k}}
\end{pmatrix},
\]

where

\[
g_a(t)=\Phi(t+a),
\qquad
h_a(t)=\mathbf 1_{t\le a}\Phi(a-t).
\]

The cut identity gives

\[
\lVert u_{p,k}\rVert^2
=
\lVert g_{a_{p,k}}\rVert^2
+
\lVert h_{a_{p,k}}\rVert^2
=
\lVert\Phi\rVert_2^2.
\]

Thus every labelled source atom has the same total analytic norm before Euler weighting.

## Arithmetic incidence

Use the source-derived Euler coefficient

\[
w_{p,k}=\frac1k p^{-k/2}.
\]

For a finite typed coefficient packet \(c=(c_{p,k})\), define

\[
\mathcal I c
=
\sum_{p,k}
c_{p,k}w_{p,k}u_{p,k}.
\]

This is the missing valuation/Fock-to-tail–seam incidence on the finite source core.

For every finite packet,

\[
\lVert\mathcal I c\rVert
\le
\lVert\Phi\rVert_2
\sum_{p,k}|c_{p,k}|w_{p,k}.
\]

Since \(w_{p,k}\le1\), the map extends continuously from the projective arithmetic test algebra into

\[
\mathcal H_{\mathrm{tail}}
\oplus
\mathcal H_{\mathrm{seam}}.
\]

It is source-derived from three already authorized ingredients:

- prime-power labels;
- Euler half-density weights;
- the exact theta cut decomposition.

## Grade decomposition

Write

\[
\mathcal I
=
\mathcal I_1
\oplus
\mathcal I_2
\oplus
\mathcal I_{\ge3}
\]

according to prime-power grade.

### Primitive grade

For the standard orthonormal prime basis,

\[
\sum_p
\lVert \mathcal I_1e_p\rVert^2
=
\lVert\Phi\rVert_2^2
\sum_p p^{-1}
=
\infty.
\]

Therefore any Hilbert-space extension agreeing with these atoms is not Hilbert–Schmidt. The test-algebra map remains continuous.

### Square grade

For \(k=2\),

\[
\sum_p
\lVert \mathcal I_2e_p\rVert^2
=
\frac{\lVert\Phi\rVert_2^2}{4}
\sum_p p^{-2}
<
\infty.
\]

Hence \(\mathcal I_2\) is Hilbert–Schmidt from the unweighted square coefficient module.

### Connected grades

For \(k\ge3\),

\[
\sum_p\sum_{k\ge3}
\lVert \mathcal I_ke_{p,k}\rVert
=
\lVert\Phi\rVert_2
\sum_p\sum_{k\ge3}
\frac1k p^{-k/2}
<
\infty.
\]

The connected synthesis is nuclear by its explicit rank-one expansion.

This reproduces the arithmetic three-grade filtration at the actual crossing into the analytic colligation:

- primitive: continuous on the test rigging, not Hilbert–Schmidt;
- square: Hilbert–Schmidt;
- connected: nuclear.

## Induced analytic coupling

Composing \(\mathcal I\) with the tail and seam projections gives the two source-derived observer lifts

\[
J_{\mathrm{tail}}=\pi_{\mathrm{tail}}\mathcal I,
\qquad
J_{\mathrm{seam}}=\pi_{\mathrm{seam}}\mathcal I.
\]

Their shared synthesis induces the cross-covariance

\[
J_{\mathrm{tail}}J_{\mathrm{seam}}^*
\]

where the relevant adjoints are defined on the declared Hilbert or rigged domains.

This is the arithmetic attachment to the analytic tail–seam coupling. It does not yet include the endpoint and archimedean channels.

## What remains open

The construction proves incidence and grade-wise operator classes. It does not prove:

- a bounded primitive extension on the unweighted coefficient Hilbert space;
- closability of seam reconstruction from the tail;
- Fourier–Poisson naturality of the full typed incidence;
- endpoint or gamma compatibility;
- the doubled Green cancellation;
- an RH-bearing positivity law.

The next exact square is the Fourier–Poisson naturality diagram for \(\mathcal I\). Each grade must commute before scalar aggregation.

## Falsifiers

1. Erasing \(k\) destroys the distinct operator classes.
2. Treating \(\mathcal I_1\) as Hilbert–Schmidt contradicts prime-harmonic divergence.
3. Treating \(\mathcal I_2\) as merely formal misses its convergent Hilbert–Schmidt norm.
4. Promoting \(\mathcal I_{\ge3}\) to the low-grade topology erases its nuclear gain.
5. Inferring endpoint or archimedean incidence from \(\mathcal I\) expands the source.

## Verdict

The valuation/Fock-to-analytic crossing exists on the projective source core and has the exact primitive–square–connected ideal filtration. The first previously missing source incidence is constructed. The frontier moves to grade-wise Fourier–Poisson naturality and the endpoint–archimedean extension.

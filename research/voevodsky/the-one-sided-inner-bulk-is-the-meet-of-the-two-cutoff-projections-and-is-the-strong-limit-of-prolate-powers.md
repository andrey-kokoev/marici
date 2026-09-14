# The one-sided exact intersection is the projection meet, but it is not the full asymptotic near-one bulk

## Compact and one-sided geometries differ

For compact physical and frequency windows on the real line, the inside--inside intersection vanishes by analytic uncertainty:

\[
\operatorname{Ran}P
\cap
\operatorname{Ran}Q
=
\{0\}.
\]

Connes's actual physical cutoff is not compact in logarithmic coordinates. It is the half-line

\[
P_L
=1_{(-\infty,L]}.
\]

After Mellin transform it becomes a Hardy projection. The Fourier-conjugate cutoff is another translated/scattered Hardy projection.

Two Hardy half-lines can have an infinite-dimensional intersection. Therefore compact-window uncertainty cannot be imported into the one-sided semilocal carrier.

## Pure translation model

Let `Pi_-` be projection onto a Fourier half-line and let

\[
\sigma_L(s)
=e^{2iLs}.
\]

Then

\[
\Pi_{\sigma_L}
=M_{\sigma_L}
\Pi_-
M_{\sigma_L}^*
\]

is a translated half-line projection in the dual coordinate.

Depending on orientation, either

\[
\operatorname{Ran}\Pi_{\sigma_L}
\subset
\operatorname{Ran}\Pi_-
\]

or the reverse inclusion holds. In either case,

\[
\boxed{
\operatorname{Ran}\Pi_-
\cap
\operatorname{Ran}\Pi_{\sigma_L}
\]

is an infinite-dimensional Hardy half-line.

Thus the pure cutoff pair already carries an exact eigenvalue-one sector.

## Projection meet

For arbitrary orthogonal projections `P,Q`, their meet is the orthogonal projection onto the closed intersection:

\[
\boxed{
E
=P\wedge Q
=P_{\operatorname{Ran}P
\cap
\operatorname{Ran}Q}.
}
\]

Let

\[
B=PQP
\]

on `ran P`. Spectral calculus gives

\[
\boxed{
E
=P_{\{1\}}(B).
}
\]

Moreover, since `0<=B<=I`,

\[
\lambda^m
\longrightarrow
1_{\{1\}}(\lambda)
\]

pointwise and boundedly on `[0,1]`. Therefore

\[
\boxed{
E
=
\operatorname*{s-lim}_{m\to\infty}
B^m.
}
\]

This is the classical alternating-projections construction of the meet.

## Canonical one-sided inner bulk

For the semilocal cutoff pair, define

\[
\boxed{
E_{\Lambda}^{bulk}
=P_\Lambda
\wedge
Q_\Lambda
=
P_{\{1\}}(B_{\Lambda,S}),
\qquad
B_{\Lambda,S}
=P_\Lambda Q_\Lambda P_\Lambda.
}
\]

This is an orthogonal projection defined directly on the actual one-sided carrier. It requires neither:

- a finite lower cutoff;
- a compact time--band window;
- a bare transition trace;
- a choice of prolate eigenbasis.

It is the canonical inner time--frequency bulk projection sought by the positive construction.

## Exact orthogonal bulk removal

The positive triple feature admits the orthogonal two-slot realization

\[
\boxed{
B_\Lambda^{1/2}A_g
\rightsquigarrow
\left(
E_\Lambda^{bulk}A_g,
(B_\Lambda-E_\Lambda^{bulk})^{1/2}A_g
\right).
}
\]

This arrow is a norm-preserving feature dilation, not equality of vectors in the original carrier. Explicitly,

\[
\boxed{
\|B_\Lambda^{1/2}A_g\|_{HS}^2
=
\|E_\Lambda^{bulk}A_g\|_{HS}^2
+
\|(B_\Lambda-E_\Lambda^{bulk})^{1/2}A_g\|_{HS}^2.
}
\]

Indeed `E_bulk` commutes with `B_Lambda`, and

\[
B_\Lambda
=E_\Lambda^{bulk}
+
(B_\Lambda-E_\Lambda^{bulk})
\]

is an orthogonal spectral decomposition.

Define the physical inside residual

\[
\boxed{
R_\Lambda^{in}g
=
(B_\Lambda-E_\Lambda^{bulk})^{1/2}A_g.
}
\]

This is positive and bulk-removed at every finite cutoff.

## Dyadic realization of the residual

The exact defect identity becomes

\[
\boxed{
B_\Lambda-E_\Lambda^{bulk}
=
\sum_{j\ge0}
B_\Lambda^{2^j}
(I-B_\Lambda^{2^j}).
}
\]

Therefore

\[
\boxed{
\|R_\Lambda^{in}g\|_{HS}^2
=
\sum_{j\ge0}
\|[B_\Lambda^{2^j}
(I-B_\Lambda^{2^j})]^{1/2}A_g\|_{HS}^2.
}
\]

The growing dyadic depth resolves the near-one boundary cloud after the exact atom has been removed.

## Interpretation in the pure Hardy model

For `gamma=1`, the meet is exactly the common translated Hardy half-line. Its observer-weighted trace carries the universal volume proportional to

\[
2Lh(1).
\]

The generic defect occurs at the finite strip between the two Hardy boundaries. Its trace density is the linear spectral-flow interval.

Once Tate scattering is inserted,

\[
\sigma_{L,\chi}
=e^{2iLs}
\gamma_\chi(s),
\]

the exact meet need not remain a literal interval projection, but the meet definition remains valid. The gamma phase changes its boundary by a relative Hardy projection pair.

## Bulk versus spectral-flow warning

The exact meet and the relative spectral-flow interval are complementary pieces of the nested pure Hardy pair. Which one carries the displayed `2L h(1)` term depends on whether the regulated trace measures:

- the common half-line after center-volume localization;
- the finite difference strip;
- or their oriented relative difference.

Thus identifying `E_bulk` as the orthogonal bulk projection does not by itself fix the scalar subtraction. The earlier Mellin calculation fixes that subtraction at the relative-trace level.

The regulator theorem must verify the same assignment for the exact product cutoff.

## Not the Sonin projection

The meet is

\[
E_\Lambda^{bulk}
=P_{H_{11,\Lambda}}.
\]

The standard Sonin projection is

\[
P_{H_{00,\Lambda}}
=(I-P_\Lambda)
\wedge
(I-Q_\Lambda).
\]

They are distinct. In the one-sided model both may be nonzero and infinite-dimensional.

Accordingly:

\[
\boxed{
H_{11}
=
\text{inner common bulk},
\qquad
H_{00}
=
\text{outer Sonin sector}.
}
\]

## Complementary outside bulk

For

\[
B_\Lambda^{out}
=(I-P_\Lambda)
(I-Q_\Lambda)
(I-P_\Lambda),
\]

define

\[
\boxed{
E_\Lambda^{Sonin}
=(I-P_\Lambda)
\wedge
(I-Q_\Lambda)
=P_{\{1\}}(B_\Lambda^{out}).
}
\]

The outside residual is

\[
R_\Lambda^{out}
=
(B_\Lambda^{out}-E_\Lambda^{Sonin})^{1/2}.
\]

Halmos polar sewing identifies the generic parts of the inside and outside residuals; it does not identify their exact meet projections.

## Cutoff variation

The maps

\[
\Lambda
\longmapsto
E_\Lambda^{bulk}
\]

need not be monotone because both `P_Lambda` and `Q_Lambda` vary and do not commute. Therefore the meet solves fixed-cutoff orthogonal bulk removal but not cutoff-direction comparison.

Observer-labelled correspondences remain necessary across cutoffs.

## Convergence target

The physical absolute-Gram form is now concrete:

\[
\boxed{
K_\Lambda^{in}(g,h)
=
\operatorname{Tr}
\left(
A_h^*
(B_\Lambda-E_\Lambda^{bulk})
A_g
\right).
}
\]

No scalar subtraction occurs inside this positive form; bulk removal is implemented by an orthogonal spectral projection.

The remaining positive theorem is convergence, after the correct boundary recentering and inclusion of the opposite polarization, of this residual Gram form to

\[
\langle
\mathcal M_Sg,
|A_S|
\mathcal M_Sh
\rangle
\]

plus any separately retained Sonin mass.

## Practical approximation

Although `E_bulk` is defined by an infinite strong limit, the dyadic powers provide monotone spectral approximants:

\[
B_\Lambda^{2^n}
\xrightarrow[s]{n\to\infty}
E_\Lambda^{bulk}.
\]

At the joint cutoff scale, choose `n(Lambda)` with

\[
2^{n(\Lambda)}
\varepsilon_\Lambda
\asymp1.
\]

This approximates the meet only down to the selected near-one resolution. Exact fixed-cutoff bulk removal requires `n->infinity`; scaling-limit boundary extraction requires the joint path. These are different limits and must remain distinct.

## Subsequent correction

The meet below constructs only the exact inside--inside atom. It need not contain the extensive near-one spectral cloud that carries asymptotic volume. The full bulk requires a joint threshold `1_[1-delta_Lambda,1](B_Lambda)` or soft dyadic filter. See `correction-the-projection-meet-removes-only-the-exact-intersection-while-the-asymptotic-bulk-is-a-near-one-spectral-cloud.md`.

## Disposition

The exact intersection projection is constructed exactly:

\[
\boxed{
E_\Lambda^{bulk}
=P_\Lambda\wedge Q_\Lambda
=
P_{\{1\}}(P_\Lambda Q_\Lambda P_\Lambda)
=
\operatorname*{s-lim}_{m\to\infty}
(P_\Lambda Q_\Lambda P_\Lambda)^m.
}
\]

It is the inside--inside Hardy bulk, not the Sonin space. Orthogonal removal gives the positive residual `B_Lambda-E_bulk`; the remaining gate is its observer-weighted absolute-Gram limit after boundary recentering.

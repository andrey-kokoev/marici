# Fourier sewing does not uniquely determine the theta-history Green polarization

## Question

Can the missing relative theta-history Green form be recovered uniquely from the now complete Fourier response operator, maximal-isotropic sewing graph, and Gaussian response table?

## Claim boundary

No. Fourier invariance constrains a Green metric to commute with the quarter turn, but the commutant contains infinitely many positive operators. Even fixing one wall normalization does not remove this freedom. Therefore the target polarization is genuinely independent source data and cannot be reconstructed from sewing coherence alone.

## Response identification

On the complete response essential image, first-coordinate recovery identifies

$$
\mathcal H_{\rm resp}\simeq L^2(\mathbb R),
$$

and the response quarter turn is conjugate to additive Fourier:

$$
\mathbb T=\mathscr R\mathcal F\mathscr R^{-1}.
$$

A positive response metric represented by a positive self-adjoint operator \(G\) is Fourier invariant exactly when

$$
\mathcal F^*G\mathcal F=G.
$$

## Infinite metric family

The harmonic oscillator

$$
\mathsf H=-\partial_x^2+4\pi^2x^2
$$

commutes with Fourier. Therefore every positive Borel function \(h\) gives a Fourier-invariant form

$$
\mathfrak G_h(f,g)
=\langle f,h(\mathsf H)g\rangle
$$

on its natural form domain.

Examples include

$$
G=I,
\qquad
G=1+\mathsf H,
\qquad
G=(1+\mathsf H)^N,
$$

and bounded positive choices such as

$$
G=I+c(1+\mathsf H)^{-1},
\qquad c>0.
$$

All make Fourier unitary and produce the same maximal-isotropic sewing graph, but they give different pairings of \(f_0,f_1,f_2,f_3\) and their translates.

## Character-block freedom

Equivalently, decompose into Fourier character spaces

$$
L^2
=H_1\oplus H_{-1}\oplus H_i\oplus H_{-i}.
$$

Any positive operator that is block diagonal in this decomposition commutes with Fourier. Thus sewing fixes the character splitting but not the positive metric within any multiplicity space. This is exactly the unsupported block-unitary/metric freedom that source typing was meant to forbid.

## Wall normalization is insufficient

Suppose a declared wall vector \(w\) is normalized by

$$
\langle w,Gw\rangle=1.
$$

This is one scalar constraint. Choose a nonzero bounded self-adjoint Fourier-commuting operator \(K\) with

$$
\langle w,Kw\rangle=0.
$$

For sufficiently small real \(\varepsilon\),

$$
G_\varepsilon=G+\varepsilon K
$$

remains positive, Fourier invariant, and preserves the wall norm, while changing at least one fourth-grade or mixed pairing. Hence the fixed even wall scale does not determine the full polarized cell.

## Response-coordinate illustration

On the response image,

$$
A'=B=g,
\qquad
C'=-2\pi iQ=-2\pi i\widehat g.
$$

Consequently a diagonal derivative metric

$$
\alpha\|B\|^2+
\beta\|Q\|^2+
\gamma\|A'\|^2+
\frac\delta{4\pi^2}\|C'\|^2
$$

collapses by Plancherel to

$$
(\alpha+\beta+\gamma+\delta)\|g\|^2.
$$

Only the sum of four weights is visible on the essential image; endpoint and cross terms introduce further independent parameters. The complete response vectors therefore do not themselves specify how Green energy is distributed among ports.

## Consequence for the first-Adams test

The four Gaussian response coordinates and translated \(L^2\) Gram are sufficient inputs once \(\mathfrak G_p^\theta\) is declared. They cannot select that form. Defining

$$
\mathfrak G_p^\theta
=(Q_p^{\rm lin})_*\mathfrak G_p^{\rm St}
$$

or choosing a commuting \(G\) to force the four matrix identities would be a fitted pullback metric, not an independently sourced G4 construction.

## Disposition

There is a formal nonuniqueness theorem: Fourier sewing, maximal isotropy, cutoff covariance, response completeness, and wall normalization do not determine the theta-history Green polarization. An explicit source declaration of that form—or an independent representation theorem deriving it—is logically necessary before the Evans residual can be evaluated.
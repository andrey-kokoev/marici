# Archimedean boundedness is closed; normalized assembly is not

## Question

Does the missing compact-support source identity also leave the weighted Birman-Schwinger factorization analytically undefined?

## Claim boundary

This packet separates existence of the bounded remainder from source-correct assembly of its matrix entries.

## Boundedness already established

Prior research proves the principal boundary comparison. On the half-line, the cosine--sine logarithmic imbalance is minus the Carleman operator,

\[
\int_0^\infty\log\xi\,
\bigl(|C\phi|^2-|S\phi|^2\bigr)d\xi
=-\iint_{(0,\infty)^2}
\frac{\phi(x)\overline{\phi(y)}}{x+y}\,dx\,dy,
\]

whose norm is \(\pi\). The exact digamma-minus-log difference is bounded, low-frequency regularization is bounded, and the interval localization commutators have a directed finite Fourier-moment bound. The explicit angular IMS partition now supplies the previously absent proper-support localization data.

Therefore the analytic statement

\[
\Gamma_L-
\log(1+\sqrt{-\Delta_D})
\in\mathcal B(L^2(-L,L))
\]

has a complete route. The weighted operator

\[
K=A^{-1/2}BA^{-1/2}
\]

is well typed and compact whenever all other declared terms of \(B\) are bounded.

## What remains missing

Boundedness does not identify the matrix. The unresolved source gate is narrower:

- the overall normalization of the compact-support Weil form;
- the sign and prefactor assigned to each prime translation and adjoint;
- the exact polar/endpoint rank terms;
- the correspondence between the source Fourier convention and the interval basis.

These data determine the signed entries of \(B\). Norm bounds, Gaussian fixtures, and the Carleman comparison cannot reconstruct them.

## Disposition

Do not report the weighted factorization as analytically blocked: its compactness and finite Schur architecture are established. Report matrix assembly and positivity certification as source-blocked at the normalized signed identity. This distinction prevents an authority blocker from erasing proved analytic structure.

## Evidence

- `research/grothendieck/half-line-logarithmic-cosine-sine-imbalance-is-the-bounded-carleman-operator.md`
- `research/grothendieck/explicit-uniform-digamma-minus-log-bound.md`
- `research/voevodsky/log-multiplier-localization-commutator-bound.md`
- `research/voevodsky/angular-ims-directed-interval-integration.md`
- `research/voevodsky/weighted-birman-schwinger-finite-certificate.md`

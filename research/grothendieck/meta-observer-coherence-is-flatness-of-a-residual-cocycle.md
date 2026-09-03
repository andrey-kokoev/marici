# Meta-observer coherence is flatness of a residual cocycle

## Question

If nonzero residuals persist, what equation replaces the demand that every observed difference vanish?

## Edge residuals

Let the lower-pyramid category have presentations `X_i` and transforms

\[
f:X_i\longrightarrow X_j.
\]

Before global descent, let `K_i` be local affine representatives with transition residual

\[
\Omega_f=K_j-f_*K_i.
\]

For composable arrows `f` and `g`, direct calculation gives

\[
\Omega_{g\circ f}
=
\Omega_g+g_*\Omega_f.
\]

This is the cocycle law. A nonzero family `Omega` can therefore be coherent. If the `K_i` are already globally compatible elements of one transported coefficient system, however, `Omega` is tautologically their coboundary; nontrivial cohomology is possible only for local representatives or coefficient transports whose descent remains unproved.

## Curvature rather than residual

For parallel paths `p,q:X_i->X_j`, define the cell curvature

\[
\kappa_{p,q}=\Omega_p-\Omega_q.
\]

Meta-observer conformance requires

\[
\kappa_{p,q}=0
\]

for every declared coherence cell. It does not require `Omega_p=Omega_q=0`. Thus the correct image is a flat affine residual system, not a zero residual system.

At finite arithmetic cutoff, the observed curvature may be nonzero. Its norm must be bounded by the transported tail residual and tend to zero under source completion.

## Completion as a trivialization

For the prime-to-completed arrow,

\[
\Omega_{\rm comp}
=
K_{\rm endpoint}+K_\Gamma.
\]

Endpoint and gamma data provide a declared trivialization of the prime-only anomaly. The test is whether this residual obeys the cocycle law under Mellin, heat, Fourier, and observer restriction maps. Calling completion coherent does not mean deleting the anomaly; it means every route transports the same anomaly.

A local transition family that violates the cocycle equation is a normalization or source-typing defect. Local residual data not trivialized by the admitted endpoint--gamma input leave an unresolved completion obstruction. Once one global completed kernel has been constructed, this descent question is discharged and must not be reintroduced as a nontrivial cohomology claim.

## Positive residual section

The Douglas defect

\[
\mathfrak R=A^*A-B^*B=D^*D
\]

is a cone-valued section over the observer category. For restriction `r:I->J`, it satisfies

\[
\mathfrak R_I=r^*\mathfrak R_Jr.
\]

The edge cocycle controls affine route differences; the cone section controls order. Meta-coherence consists of flatness of the former and naturality plus positivity of the latter.

## Exact meta-observer output

For each cell and observer packet, return

\[
(\Omega_p,\Omega_q,\kappa_{p,q},
\text{tail bound},\mathfrak R_I,
\text{cone disposition}).
\]

The admissible conditions are:

- prescribed edge residuals;
- zero completed curvature, or finite-cutoff curvature within its tail bound;
- natural residual transport;
- positive cone membership of `R_I`.

## Disposition

Replace “coherence means zero residual” by “coherence means a flat residual cocycle with a natural positive defect section.” This retains endpoint--gamma completion data and the nonzero Weil form while localizing genuine inconsistency in curvature.

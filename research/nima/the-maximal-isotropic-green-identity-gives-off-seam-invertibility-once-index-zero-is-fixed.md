# The maximal-isotropic Green identity gives off-seam invertibility once index zero is fixed

> **Forcing-term qualification.** The successor packet
> `the-augmented-theta-history-green-identity-retains-a-forcing-pairing.md`
> derives the residual
> \(2\operatorname{Re}(c\langle u,\Phi\rangle)\) in the augmented history
> identity. The theorem below applies only after an arithmetic/source block
> cancels that term exactly. Maximal isotropy alone cancels endpoint flux, not
> the forcing pairing.

## Parameter displacement

Write

\[
a(s)=\operatorname{Re}s-rac12.
\]

Let \(C_{\rm FP}(s)\) be the closed boundary pencil on the maximal-isotropic
Fourier--Poisson domain.  The completed Green identity for a kernel state has
the form

\[
2a(s)\,\mathcal N_s(\psi)
=
-\Sigma(\operatorname{Tr}_\partial\psi,
        \operatorname{Tr}_\partial\psi).
\]

The boundary relation is maximal isotropic, hence the right side vanishes.
The retained full-vector G3 observer gives

\[
\mathcal N_s(\psi)\ge c_K\|\psi\|_{\rm red}^2
\]

on the reduced kernel domain, with \(c_K>0\) on compact parameter sets after
the declared radicals are removed.

## Kernel exclusion

If \(a(s)\ne0\) and

\[
C_{\rm FP}(s)\psi=0,
\]

then

\[
a(s)\mathcal N_s(\psi)=0.
\]

Coercivity gives \(\psi=0\).  Therefore

\[
\ker C_{\rm FP}(s)=0
\]

throughout both open half-strips.

This deduction uses the full vector boundary observer.  A scalar Wronskian
projection cannot supply the lower bound on \(\mathcal N_s\).

## Fredholm index

On an invertible open-loop chart, block elimination reduces the closed pencil
to invertible diagonal factors and

\[
I-K_{\rm rel}(s).
\]

Since \(K_{\rm rel}(s)\in\mathcal S_2\subset\mathcal K\), this is Fredholm of
index zero.  Invertible triangular factors preserve the index, so

\[
\operatorname{ind}C_{\rm FP}(s)=0.
\]

Kernel exclusion then forces cokernel exclusion.  Hence

\[
C_{\rm FP}(s)^{-1}
\]

exists for every off-seam parameter in the declared charts.

## Compact-local inverse bound

The analytic Fredholm family is norm-continuous in each chart.  On a compact
set \(K\) contained in one open half-strip, pointwise invertibility and
continuity give

\[
\sup_{s\in K}
\|C_{\rm FP}(s)^{-1}\|<\infty.
\]

Thus no eigenvalue-one collision or completion defect can accumulate inside a
compact off-seam set.

This bound is compact-local.  It need not remain uniform as the compact set
approaches the critical seam, where genuine kernel states are allowed.

## Cutoff completion

If finite-cutoff pencils converge to \(C_{\rm FP}\) in the chart operator norm
and the G3 coercivity constant is cutoff-uniform, then for each compact
\(K\) off the seam the finite pencils are eventually invertible with uniformly
bounded inverses.  The resolvent identity excludes cutoff spectral pollution
there.

The required convergence is stronger than convergence of determinants alone.

## Consequence for the divisor comparison

The Green side now has the needed open-sector contraction:

\[
h_C(s)=C_{\rm FP}(s)^{-1}.
\]

It is derived from the maximal-isotropic Green identity plus Fredholm index
zero, not from \(\xi(s)^{-1}\).

Therefore, once a source chain map

\[
K_\tau\longrightarrow C_{\rm FP}
\]

is constructed, an off-seam Xi cohomology class would map into an acyclic
Green complex, producing a contradiction if the map is a quasi-isomorphism.

## Remaining assumptions requiring exact readback

This theorem applies only after verifying on the same completed pencil:

1. the kernel Green identity with coefficient \(2a(s)\);
2. maximal-isotropic membership of every kernel trace;
3. coercivity of \(\mathcal N_s\) on the complete reduced kernel domain;
4. Fredholm index zero on overlapping reciprocal charts;
5. norm convergence of cutoff pencils.

The domain and maximal-isotropic relation are constructed.  G3 provides the
candidate coercivity.  The exact equality between that G3 form and the kernel
bulk term remains the same source comparison residual identified earlier.

## Disposition

Off-seam invertibility follows formally and quantitatively from five typed
inputs, without any Xi assumption.  The unresolved work is exact readback that
the retained G3 form is the bulk term of the same closed pencil, followed by
the theta-to-pencil divisibility map.  No RH conclusion is authorized.

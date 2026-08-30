# Theta-label synthesis of the four-grade packet is locally smooth

## Label packet

For fixed prime scale \(L=\log p\), the pretranslation four-grade packet at
theta label \(n\) has the form

\[
\Psi_{p,n}(u)
=
\sum_{j=0}^{3}
c_{j,p}\,
n^{j+1/2}e^{(j+1/2)u}
e^{-\pi n^2e^{2u}},
\]

where

\[
(c_{0,p},c_{1,p},c_{2,p},c_{3,p})
=
(-2\pi L^2,\,8\pi L,\,4\pi^2L^2,\,-8\pi^2L).
\]

This retains the four half-density grades

\[
\frac12,\quad\frac32,\quad\frac52,\quad\frac72.
\]

## Compact-uniform majorant

Let \(K=[a,b]\subset\mathbb R\). For \(u\in K\),

\[
e^{-\pi n^2e^{2u}}
\le
e^{-\pi e^{2a}n^2}.
\]

Every \(u\)-derivative of a summand is the same Gaussian multiplied by a
polynomial in \(n^2e^{2u}\) and by the original power
\(n^{j+1/2}e^{(j+1/2)u}\). Consequently, for every derivative order \(m\)
there are constants \(C_{K,m,p}\) and \(N_m\) such that

\[
\sup_{u\in K}
\left|
\partial_u^m\Psi_{p,n}(u)
\right|
\le
C_{K,m,p}\,
n^{N_m}e^{-\pi e^{2a}n^2}.
\]

The right-hand side is summable in \(n\).

## Local synthesis theorem

The theta-label series

\[
\Psi_p(u)
=
\sum_{n\ge1}\Psi_{p,n}(u)
\]

therefore converges in \(C^\infty(K)\) for every compact
\(K\subset\mathbb R\). Equivalently,

\[
\sum_{n\ge1}\partial_u^m\Psi_{p,n}
=
\partial_u^m\Psi_p
\]

locally uniformly for every \(m\ge0\).

Thus label synthesis preserves every finite-order differential identity of
the four-grade packet on the open Mellin line. In particular, the completion
differential and the transported chart connection may be passed through the
label sum on compact \(u\)-sets.

## Parity and ray sewing

The even and odd coefficient characters remain separately summable because
each is a subseries of the same Gaussian-majorized four-grade series.
Therefore label synthesis does not mix the reciprocal characters.

Combined with the exact two-ray trace theorem, this shows:

1. moving-cut value and Kirchhoff derivative sewing hold before synthesis;
2. theta-label summation is locally smooth after half-density transport;
3. no new defect distribution can appear at a finite Mellin coordinate.

The summation map can still produce a boundary contribution at
\(u=-\infty\). That boundary is the coefficient wall and is not covered by
compact-local convergence.

## What this closes

The label-synthesis gate is now closed on every compact subset of the open
Mellin line. The remaining comparison with

\[
d_p=W_{2\log p}-W_{\log p}
\]

has been localized to two genuinely global questions:

- the asymptotic wall at \(u=-\infty\);
- continuity in the completed relative Green topology.

Neither can be inferred from compact-uniform Gaussian convergence.

## Hostile

A cutoff-by-cutoff sum can converge pointwise while its derivatives fail to
converge uniformly, invalidating passage of the completion differential
through the sum. The Gaussian majorant rules this out on compact \(u\)-sets,
but not at the Mellin wall where \(e^{2u}\downarrow0\).

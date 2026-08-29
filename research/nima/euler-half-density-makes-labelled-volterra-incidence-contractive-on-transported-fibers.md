# Euler half-density makes labelled Volterra incidence contractive on transported fibers

## Labelled source atoms

For a prime power \(p^k\), let

\[
L_{p,k}=k\log p,
\qquad
a_{p,k}=\frac1k p^{-k/2}.
\]

Starting from the bilateral completed theta forcing \(\Phi\), define the labelled translated packet

\[
\Phi_{p,k}(u)
=
a_{p,k}\Phi(u+L_{p,k}).
\]

The label \((p,k)\) is retained as a carrier idempotent; translation acts only inside that fiber.

## Transported source and history norms

Let \(\mathcal E_{w,L}\) and \(\mathcal H_{\mathrm{rel},L}\) use the translated weight

\[
w_L(u)=w(u+L).
\]

Translation by \(L\) is isometric from the seam fiber to the \(L\)-fiber. Therefore

\[
\|\Phi_{p,k}\|_{\mathcal E_{w,L_{p,k}}}
=
|a_{p,k}|\,
\|\Phi\|_{\mathcal E_w}.
\]

The Volterra lift is translation-covariant up to its endpoint coordinates, and those endpoint coordinates scale by the same arithmetic coefficient. Hence

\[
\|H_+\Phi_{p,k}\|_{\mathrm{rel},L_{p,k}}
=
|a_{p,k}|\,
\|H_+\Phi\|_{\mathrm{rel},0}.
\]

The same holds for the reflected, even, and odd histories.

## Uniform contraction

For all primes and positive grades,

\[
|a_{p,k}|
=
\frac1k p^{-k/2}
\le
2^{-1/2}.
\]

Thus the complete labelled history incidence has a cutoff-independent upper bound and in fact contracts along every Adams ray.

Raw exponential displacement creates no order loss because it is absorbed by the object-indexed transported topology. The only remaining grade dependence is the source Euler half-density, which improves the norm.

## Direct-sum assembly

Let

\[
\mathscr E
=
\bigoplus_{p,k}\mathcal E_{w,L_{p,k}}^{(p,k)}
\]

and similarly define the relative history sum. If the label idempotents are orthogonal and the Volterra constructor intertwines them, then the assembled incidence is diagonal:

\[
P_{q,\ell}H_+P_{p,k}=0
\qquad
((q,\ell)\ne(p,k)).
\]

Its direct-sum operator norm is the supremum of the local norms, hence uniformly bounded by the base Volterra norm times \(2^{-1/2}\).

This proves analytic boundedness conditional on typed label preservation; it does not derive that preservation from scalar Mellin orthogonality.

## Lower-bound qualification

Euler contraction also means there is no uniform lower bound on the raw incidence amplitudes as \(p^k\to\infty\). This is not a failure if the arithmetic source norm carries the same coefficient and each fiber is compared after source normalization.

A claimed global observability lower bound must therefore be stated relative to the weighted arithmetic domain. In an unweighted label \(\ell^2\) norm, the incidence necessarily loses its lower frame bound.

## Remaining authority gate

The analytic order profile is now harmless. The unresolved point is exact prime-label authority:

- either the valuation/Fock carrier supplies orthogonal idempotents directly;
- or the Fourier--Bohr invariant-mean construction must prove that the Volterra lift intertwines its spectral projections.

Without this theorem, the bounded diagonal model is only a typed candidate, and coherent cross-prime rows remain possible.

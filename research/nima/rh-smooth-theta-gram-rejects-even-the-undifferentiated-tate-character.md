# The smooth theta Gram carrier rejects even the undifferentiated Tate character

## Native small-shift law

The full tail–seam kernel is the autocorrelation of the bilateral completed
theta source \(\Phi\):

\[
A(h)=\langle\Phi,\tau_h\Phi\rangle.
\]

The completed theta source is smooth and has a nonzero derivative in
\(L^2\). Therefore translation differentiability gives

\[
\frac{\lVert\tau_h\Phi-\Phi\rVert_2}{|h|}
\longrightarrow
\lVert\Phi'\rVert_2.
\]

Since

\[
\lVert\tau_h\Phi-\Phi\rVert_2^2
=2\bigl(A(0)-A(h)\bigr),
\]

the native adjacent-atom distance is linear rather than square-root in the
logarithmic displacement:

\[
\lVert u_n-u_{n-1}\rVert
\sim
\lVert\Phi'\rVert_2
\log\frac{n}{n-1}.
\]

## Prime-power comparison

Set \(n=p^k\). Then

\[
\log\frac{p^k}{p^k-1}\sim p^{-k}.
\]

The undifferentiated order-\(k\) Tate logarithm has coefficient proportional
to

\[
\frac1k p^{-k/2}.
\]

For a typed adjacent difference supported at \(p^k\) and \(p^k-1\), its
coefficient-to-Gram-norm ratio grows as

\[
\frac{p^{k/2}}{k\lVert\Phi'\rVert_2}.
\]

It diverges. Spectral differentiation adds \(\log p\) and diverges still
faster.

Thus neither the undifferentiated prime-power anomaly character nor its
logarithmic current extends continuously from finite labelled packets through
the pure analytic tail–seam Gram completion.

## Architectural consequence

The preceding cusp prototype identified a borderline possibility, but the
native smooth theta source lies on the excluding side of that threshold. The
two anomaly characters cannot be recovered as continuous functionals of the
analytic tail–seam state alone.

They require an independently retained arithmetic carrier, such as the
valuation/Fock constructor module. The completed object must therefore remain
a coupled fiber product of:

- the analytic tail–seam realization;
- the typed arithmetic valuation realization;
- their source-derived boundary incidence map.

A scalar determinant may be formed only after that incidence map has supplied
the two linear anomaly traces. Quotienting to the analytic Gram state first
irreversibly erases them.

## Finite falsifier

For any proposed continuous anomaly trace on the analytic Gram carrier, use
the two-label packet

\[
e_{p^k}-e_{p^k-1}.
\]

Its analytic norm is asymptotic to \(p^{-k}\), while its typed Tate value is
of order \(p^{-k/2}\). The domination ratio diverges. This is a direct
continuity falsifier requiring no zero information and no scalar positivity
criterion.

## DPC verdict

The native theta autocorrelation is too smooth to retain the Tate anomaly
characters. Their existence forces a discrete arithmetic port and a
source-derived incidence into the determinant boundary object. Analytic
completion followed by arithmetic reconstruction is impossible.

## Verification

`check_rh_smooth_gram_tate_character_no_go.py` uses a smooth Gaussian
autocorrelation to verify the exact adjacent-label scaling and divergence of
both undifferentiated and differentiated Tate ratios for prime-power orders
one through three.

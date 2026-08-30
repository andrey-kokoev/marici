# Theta half-line prime-translation defect is the missing boundary-incidence cocycle

## Status

Exact nonlocal incidence theorem. Translation in logarithmic scale is a scalar
multiplier under the full-line transform. On the half-line, forward translation
fails to be a pure multiplier by an explicit interval current.

For arithmetic displacement \(\ell=k\log p\), this interval current is a
source-derived map from prime-power transport into the additive boundary
object. It is not determined by any finite seam-jet packet and satisfies an
exact cocycle law under composition of translations.

This constructs the type of the previously missing valuation/Fock-to-boundary
incidence. It does not yet orient the resulting complex current.

## Half-line transform

Let

\[
H_A(z)=\int_0^\infty A(u)e^{izu}\,du
\]

for a rapidly decaying source (A\). For \(\ell>0\), define forward scale
translation by

\[
(S_\ell A)(u)=A(u+\ell).
\]

Then substitution (v=u+\ell\) gives

\[
\begin{aligned}
H_{S_\ell A}(z)
&=\int_0^\infty A(u+\ell)e^{izu}\,du\\
&=e^{-iz\ell}
\left[
H_A(z)-B_\ell[A](z)
\right],
\end{aligned}
\]

where

\[
B_\ell[A](z)
=\int_0^\ell A(v)e^{izv}\,dv.
\]

The interval functional (B_\ell\) is the exact half-line translation defect.

## Comparison with causal backward shift

Define the delayed causal shift

\[
(C_\ell A)(u)
=\mathbf1_{u\geq\ell}A(u-\ell).
\]

Its half-line transform is the pure multiplier

\[
H_{C_\ell A}(z)=e^{iz\ell}H_A(z).
\]

Thus the two directions have different boundary types:

- causal delay retains the whole source and adds no interval defect;
- forward translation discards the initial interval and must emit its boundary
  current.

This is an ordered-port distinction. Treating both translations as invertible
Mellin multipliers erases the boundary incidence.

## Prime-power incidence

For a prime power (p^k\), set

\[
\ell_{p,k}=k\log p.
\]

The associated boundary port is

\[
B_{p,k}[A](z)
=\int_0^{k\log p}A(v)e^{izv}\,dv.
\]

Given an authorized finite prime-power packet with weights \(w_{p,k}\), its
incidence into the additive boundary object is

\[
\mathcal I_w[A](z)
=\sum_{p,k}w_{p,k}B_{p,k}[A](z).
\]

At finite support this is an exact linear map. Primitive, square, and higher
prime-power channels remain separately typed through their weights and interval
lengths.

## Translation cocycle

The boundary current obeys

\[
B_{\ell_1+\ell_2}[A](z)
=B_{\ell_1}[A](z)
+e^{iz\ell_1}B_{\ell_2}[S_{\ell_1}A](z).
\]

Indeed, the first term integrates over \([0,\ell_1]\), while the transported
second term integrates over \([\ell_1,\ell_1+\ell_2]\).

This is the exact coherence relation for staged multiplicative transport. The
boundary incidence is a one-cocycle for the forward translation semigroup with
coefficients in half-line transform functionals.

For prime products, the cocycle records the ordered decomposition of
\(\log(pq)=\log p+\log q\) while producing the same total interval current.
Any compiler coherence cell must derive this equality rather than fit endpoint
agreement.

## Why finite additive jets cannot reconstruct it

For analytic (A\), the interval current has the formal expansion

\[
B_\ell[A](z)
=\sum_{m\geq0}\frac{A^{(m)}(0)}{m!}
\int_0^\ell v^me^{izv}\,dv.
\]

It generally depends on the entire seam germ, not on any fixed finite jet. On a
smooth source it depends on the full interval and need not be determined by the
seam germ at all.

Therefore the all-orders finite differential graph theorem does not eliminate
this port. It is genuinely nonlocal in additive scale.

## Reciprocal reflection

Under (z\mapsto-z\), the interval current becomes

\[
B_\ell[A](-z)
=\int_0^\ell A(v)e^{-izv}\,dv.
\]

For real (A\) on the critical seam, the two are conjugate. Off the seam they
are reciprocal analytic channels but need not be conjugate or have a fixed
relative phase.

Thus reciprocal sewing types the two incidence ports but does not orient their
scalar combination.

## Positivity boundary

If (A(v)>0\), then at (z=0\),

\[
B_\ell[A](0)>0.
\]

For complex (z\), the exponential phase can produce cancellation within the
interval. Source positivity alone gives no universal nonvanishing or phase
sector for (B_\ell[A](z)).

The port is new, but its RH-bearing orientation remains unproved.

## Completion gate

For the full arithmetic incidence, one must determine whether

\[
\sum_{p,k}w_{p,k}B_{p,k}[A](z)
\]

converges in the chosen boundary topology. The primitive and square currents
may require separate distributional or renormalized treatment, while the
higher tail may be continuous or trace-class.

The incidence map must be constructed before scalar prime summation. Typed
cancellation between divergent channels is permitted only through a declared
completion relation.

## Finite falsifiers

Any proposed incidence map fails if:

- it treats forward translation as a pure Mellin multiplier;
- it omits the interval (B_\ell\);
- it identifies primitive, square, and higher weights before boundary mapping;
- its staged composition violates the cocycle law;
- it reconstructs (B_\ell\) from a fixed finite seam jet on arbitrary smooth
  sources;
- it assigns a complex sign to (B_\ell(z)\) from positivity of (A\) alone.

The smallest witness is one displacement \(\ell\): direct quadrature of the
initial interval measures the exact multiplier defect.

## Consequence

The previously missing arithmetic-to-boundary arrow now has a canonical local
formula at every finite prime-power packet. This is the first new port to
survive the finite additive graph-closure theorem.

The decisive next step is to insert the actual primitive, square, and higher
prime-power weights, prove the typed completion of their interval currents, and
test whether modular reciprocal sewing imposes a source-specific law on the
resulting transverse current. Failure of orientation would close the remaining
finite transport branch while preserving this incidence theorem as arithmetic
provenance.

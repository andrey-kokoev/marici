# The Two-Prime Cross Term Forces Seam Synthesis Before Squaring

## The smallest audit

For a finite prime packet \(c=(c_p)\), the universal image channel from Entry
3931 is

\[
S(c)=\sum_p\frac{c_p}{\sqrt p}.
\]

Its boundary energy is

\[
B(c)=|S(c)|^2.
\]

For two distinct primes \(p,q\),

\[
B(c_p,c_q)
=\frac{|c_p|^2}{p}+\frac{|c_q|^2}{q}
+2\operatorname{Re}
\frac{\overline{c_p}c_q}{\sqrt{pq}}.
\]

The coefficient \(1/\sqrt{pq}\) is unavoidable.  It is the smallest witness
that the seam boundary is global in the prime labels.

## Prime-local currents cannot produce it

Every quadratic current assembled as a direct sum of independent prime-local
forms has the shape

\[
B_{\mathrm{loc}}(c)=\sum_p b_p|c_p|^2.
\]

Its polarization between distinct prime axes vanishes:

\[
B_{\mathrm{loc}}(e_p,e_q)=0,
\qquad p\ne q.
\]

By contrast, the seam form has

\[
B(e_p,e_q)=\frac1{\sqrt{pq}}.
\]

Therefore no sum of primitive, prime-square, or connected-tail currents that
remains diagonal in the prime label can reconstruct the seam image.  The
missing operation is not another local coefficient.  It is coherent synthesis
across labels before quadratic observation.

## The noncommuting square

Let \(D\) apply the half-density weights,

\[
D(c)_p=\frac{c_p}{\sqrt p},
\]

let \(A\) be the codiagonal amplitude synthesis,

\[
A(d)=\sum_pd_p,
\]

and let \(N\) take squared norm.  There are two orders:

\[
N\circ A\circ D(c)
=\left|\sum_p\frac{c_p}{\sqrt p}\right|^2,
\]

whereas primewise squaring followed by addition gives

\[
A_{\mathbb R_+}\circ N^{\oplus}\circ D(c)
=\sum_p\frac{|c_p|^2}{p}.
\]

Their difference is exactly the off-diagonal seam coherence:

\[
\sum_{p\ne q}
\frac{\overline{c_p}c_q}{\sqrt{pq}}.
\]

Thus completion and scalar observation fail to commute already on two prime
labels.  Squaring first produces only the scalar prime-square current.
Synthesizing first retains the full rank-one boundary state.

## Typed consequence

In the defect compiler, seam retention is not a boundary correction that may
be appended after local prime-current evaluation.  It must be an amplitude
level operation preceding every norm, trace, or scalar diagonalization.  The
order is labelled half-densities, then global seam amplitude, then boundary
energy.

The prime-square current is the diagonal decategorification of this process.
It is insufficient as an input from which the global seam state can be
recovered.

This identifies a precise dependency among the earlier operations.  If
\(S\) denotes global seam synthesis and \(Q\) denotes square-current
observation, then \(S\) precedes \(Q\).  Reversing them has the typed residual

\[
R_{S,Q}(c)
=\sum_{p\ne q}
\frac{\overline{c_p}c_q}{\sqrt{pq}}.
\]

The residual is not noise.  It is the capability of comparing distinct prime
labels at the common seam.

## Falsifier and next gate

Take \(c_p=c_q=1\).  The required seam energy is

\[
\frac1p+\frac1q+\frac2{\sqrt{pq}},
\]

while every diagonal prime-square aggregation returns only

\[
\frac1p+\frac1q.
\]

Any theta--Tate boundary construction that returns the second value after
claiming to retain the full seam has failed the smallest two-prime test.

The next gate is to locate the source-authorized codiagonal \(A\) in the
completed theta--Tate object.  It must be derived before scalar Euler
aggregation and must carry the endpoint orientation and phase needed to fix
the sign of every cross term.

# The Cross-Face Orientation Is a Two-Port Endpoint–Wronskian Instrument

## Exact decomposition

Let `D=-partial_q` on the outgoing half-line graph domain and assume `K`
vanishes at infinity.  Put

\[
C(K)=\langle DK,K\rangle.
\]

Integration by parts fixes its real part:

\[
\operatorname{Re}C(K)
=
\frac12|K(0)|^2.
\]

Its imaginary part remains an independent bulk current:

\[
J(K)=\operatorname{Im}C(K).
\]

For `z=a+it`, the cross-face difference is therefore

\[
\begin{aligned}
\Delta_{\mathrm{face}}
&=
\|(D+z)K\|^2-\|(D-z)K\|^2\\
&=
4\operatorname{Re}\langle DK,zK\rangle\\
&=
2a|K(0)|^2+4tJ(K).
\end{aligned}
\]

Thus orientation is measured by two real ports:

1. the endpoint amplitude `|K(0)|^2`;
2. the bulk Wronskian or phase current `J(K)`.

## Geometric meaning

If

\[
K(q)=\rho(q)e^{i\theta(q)},
\]

then

\[
J(K)
=
-\int_0^\infty\rho(q)^2\theta'(q)\,dq.
\]

It records weighted phase transport through the scale bulk.  Endpoint
amplitude cannot reconstruct it.  Conversely, a constant-phase state has
`J=0` while retaining nonzero endpoint amplitude.  The two ports are
independent.

In geometric algebra they are the scalar and oriented bivector components of
the comparison between `DK` and `zK`.  The tight-frame sum retained only their
unoriented metric norm.

## Reciprocal parity

Under conjugate reciprocal transport, endpoint amplitude is even while the
Wronskian current is odd:

\[
|K(0)|^2\longmapsto|K(0)|^2,
\qquad
J(K)\longmapsto-J(K).
\]

At the same time `a` changes sign and `t` is retained under
`z -> -conjugate(z)`.  Consequently the complete interference observable
changes sign, as an oriented comparison should.

This is the first nontrivial representation carried by the outer `+2`: the
two directed faces require a two-component instrument, not one summed energy.

## Why neither port proves RH

The decomposition is universal.  Generic complex sources can vary `J`
independently of the endpoint amplitude.  The anti-diagonal completed zero
condition controls endpoint traces but does not by itself control the phase
current.

The theta-specific theorem must therefore identify `J(K)` with a declared
arithmetic or modular current.  Candidate sources are:

- the primitive sheet-odd current;
- the prime-square phase/incidence packet;
- the odd tail–principal-value plane of the external five-cell;
- a mixed seam current produced by Poisson sewing.

The required identity must be derived before assuming a zero and must persist
at every finite cutoff.

## Falsifier

Construct two admissible source packets with the same endpoint amplitude and
the same tight-frame sum but opposite phase current.  Any proposed instrument
that cannot distinguish them is orientation-blind.

## Result

The missing cross-face instrument has minimal real rank two.  Its endpoint
port is fixed by integration by parts; its Wronskian port records unresolved
bulk phase transport.  RH-bearing work has reduced to identifying and
orienting this sheet-odd Wronskian current through theta arithmetic.


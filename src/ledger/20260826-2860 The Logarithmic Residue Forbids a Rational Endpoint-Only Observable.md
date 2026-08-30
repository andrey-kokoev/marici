# 2860 — The Logarithmic Residue Forbids a Rational Endpoint-Only Observable

## Final scalar-readout test

Entry 2858 identified the intrinsic Stokes object as a two-port cospan. A source-defined scalar endpoint observable could nevertheless exist if the frozen bulk density were an exact \(\xi\)-derivative with a rational primitive.

After suppressing factors independent of \(\xi\), the density has type

\[
\frac{d\xi}{(\xi+1)\sqrt{K_{\rm exc}(a,\kappa,\xi)}}.
\]

At a generic bulk point,

\[
K_{\rm exc}(a,\kappa,-1)\ne0.
\]

Thus the Cayley–Menger factor is a unit at the marked endpoint, while the \(q_{g1}\) factor produces a genuine simple logarithmic pole.

## Local-order obstruction

Suppose a rational primitive had the form

\[
\frac{F(\xi)}{\sqrt{K_{\rm exc}}}.
\]

Its derivative is

\[
d_\xi\left(\frac{F}{\sqrt K}\right)
=
\frac{1}{\sqrt K}
\left(
F'-\frac{K'}{2K}F
\right)d\xi.
\]

Because \(K\) is a unit at \(\xi=-1\), \(K'/K\) is regular there.

If \(F\) is regular, the parenthesized coefficient is regular and cannot reproduce the simple source pole.

If \(F\) has pole order \(m>0\), then \(F'\) has pole order \(m+1\), while \((K'/2K)F\) has only order \(m\). The leading pole cannot cancel. The result has order at least two and again cannot reproduce the source pole of order one.

Therefore no rational local primitive exists.

## Consequence

The frozen bulk observable does not collapse to a rational scalar difference of its two endpoint values. The intrinsic source object remains

\[
\Gamma_\xi\longrightarrow E_+\oplus E_-.
\]

A logarithmic or twisted primitive may be introduced only with additional branch, regulator, and relative-cycle data. No such endpoint cocycle is declared by the frozen source packet.

Accordingly, the rational scalar endpoint-combination hypothesis is retired. The surviving physical observable is the bulk relative period together with its labelled endpoint cospan—not an endpoint sum.

This does not claim that every analytically continued or regulator-enhanced observable is impossible. Reopening requires a source-derived twisted primitive and proof that its branch dependence cancels in the physical pairing.

## Durable artifacts

- research/benincasa/check_soft_endpoint_rational_stokes_primitive.py
- research/benincasa/soft-endpoint-rational-stokes-primitive.json


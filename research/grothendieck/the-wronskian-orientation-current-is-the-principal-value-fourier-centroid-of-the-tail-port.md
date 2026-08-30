# The Wronskian Orientation Current Is the Principal-Value Fourier Centroid of the Tail Port

## Fourier representation

Let `K` be an outgoing half-line state and extend it by zero to the full scale
line.  Use the Fourier convention

\[
\widehat K(\xi)
=
\int_{\mathbb R}K(q)e^{-2\pi iq\xi}\,dq.
\]

For `D=-partial_q`, the bulk Wronskian current is

\[
J(K)=\operatorname{Im}\langle DK,K\rangle_{(0,\infty)}.
\]

The zero extension has a jump at the seam.  Its distributional derivative
therefore contains the endpoint delta, which accounts for the real boundary
term `|K(0)|^2/2`.  The imaginary part is unaffected by that real trace and
obeys

\[
J(K)
=
-2\pi\operatorname{pv}
\int_{\mathbb R}\xi|\widehat K(\xi)|^2\,d\xi.
\]

The principal value is essential.  A nonzero endpoint jump gives
`|Khat(xi)|^2` a `xi^-2` tail, so its first moment need not be absolutely
integrable.

## Exact one-mode witness

For

\[
K(q)=e^{(-\alpha+i\beta)q},
\qquad q\ge0,
\]

one has

\[
\widehat K(\xi)
=
\frac1{\alpha+i(2\pi\xi-\beta)}.
\]

Directly,

\[
J(K)=-\frac\beta{2\alpha}.
\]

The principal-value centroid is

\[
\operatorname{pv}
\int_{\mathbb R}
\frac{\xi\,d\xi}
{\alpha^2+(2\pi\xi-\beta)^2}
=
\frac\beta{4\pi\alpha},
\]

which reproduces the Wronskian identity exactly.

## Identification with the five-cell

Multiplication by the half-line step has Fourier transform containing a delta
part and an odd principal-value part.  The delta contribution records the
endpoint amplitude.  The odd principal-value contribution records the
spectral centroid above.

Therefore the two-port orientation instrument from the preceding result is
already present in the external five-cell:

- constant–delta plane: endpoint amplitude and its Fourier mate;
- odd tail–principal-value plane: Wronskian orientation current.

No sixth linear boundary generator is needed.  The missing operation was the
correct quadratic readout on the existing odd port.

## What remains theta-specific

The five-cell now faithfully records orientation, but does not select its
sign.  A generic half-line state can have either sign of the PV centroid while
retaining the same endpoint amplitude and tight-frame energy.

The RH-bearing theorem has therefore narrowed again.  Theta/Poisson sewing
must impose a source-derived relation between:

\[
|K(0)|^2
\quad\leftrightarrow\quad
\operatorname{pv}\int\xi|\widehat K(\xi)|^2d\xi,
\]

with the second expression understood as mathematics only; in prose, it is
the odd spectral centroid.  This relation must make the total cross-face
orientation incompatible with an anti-diagonal zero away from the seam.

The relation cannot follow from Fourier closure alone: changing `beta` to
`-beta` preserves the endpoint amplitude and all unoriented energies while
reversing the PV centroid.

## Result

The unresolved Wronskian current is not a new channel.  It is exactly the
principal-value Fourier centroid of the existing odd tail port.  The
architecture is now observationally complete at this level.  The remaining
problem is a theta-specific sign or conservation law coupling the even
endpoint port to the odd PV port.

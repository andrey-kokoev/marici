# Moving-weight fibers make the Mellin filling unitary

## The apparent obstruction

On one fixed unweighted `L^2` space, multiplication by

\[
e^{aq}
\]

is unbounded for nonzero real `a`. It would therefore be tempting to say that
the canonical Mellin-orbit filling fails completion away from the critical
seam.

That conclusion compares different spectral presentations inside the wrong
single fiber.

## Source-derived Hilbert bundle

For real `a`, define the weighted fiber

\[
\mathcal H_a
=
L^2(\mathbb R,e^{2aq}\,dq)
\]

or the corresponding half-line fiber when a polarized chart is intended.
For two weights `a` and `b`, define

\[
U_{a\to b}f(q)=e^{(a-b)q}f(q).
\]

Then

\[
\|U_{a\to b}f\|_{\mathcal H_b}^2
=
\int |f(q)|^2e^{2aq}\,dq
=
\|f\|_{\mathcal H_a}^2.
\]

Hence `U_(a->b)` is unitary between the correctly typed fibers. It obeys

\[
U_{b\to c}U_{a\to b}=U_{a\to c},
\qquad
U_{a\to a}=I.
\]

The real Mellin flow is therefore a flat unitary transport on a moving
Hilbert bundle, even though it is unbounded when forced to act within one
fixed `L^2` coordinate space.

## Reciprocal exchange

Scale reflection

\[
(Sf)(q)=f(-q)
\]

is unitary from `H_a` to `H_-a`:

\[
\|Sf\|_{\mathcal H_{-a}}=\|f\|_{\mathcal H_a}.
\]

Thus the two open half-plane sectors are naturally different weighted fibers
of one reciprocal bundle. On the critical seam `a=0`, the reciprocal fibers
coincide and reflection becomes a unitary endomorphism of the same fiber.

This explains the seam without using zeros, but it does not confine zeros.

## Correction to the completion target

The Mellin-orbit filling from `a` to `-a` does survive Hilbert completion when
it is typed as transport across the bundle. Its apparent unboundedness is a
coordinate artifact.

Therefore a genuine completion class cannot be claimed merely from growth of
`e^(aq)` in a fixed norm. It must occur where the bundle transport meets a map
that is not automatically continuous or exact, such as:

- endpoint evaluation at `q=0`;
- intersection of the plus and minus endpoint domains;
- a primitive or square boundary functional;
- restricted-product assembly of those traces;
- determinant compression of the resulting relation.

## The new first analytic gate

Point evaluation is not continuous on bare `L^2`. It becomes continuous only
after a source-derived graph or Sobolev domain is specified. Let `D_a` be the
weighted tail differential and equip its domain with

\[
\|f\|_{\mathcal H_a}^2+\|D_af\|_{\mathcal H_a}^2.
\]

The next exact question is whether the endpoint map

\[
\operatorname{ev}_0:\operatorname{Dom}D_a\longrightarrow\mathbb C
\]

is continuous uniformly under the Mellin transport and Euler cutoff, and
whether the plus and minus endpoint domains form a strict pullback.

This is a real domain theorem. It cannot be answered by the scalar transform
alone.

## Finite and analytic falsifiers

1. A finite model that reports exponential-growth instability while using
   one fixed metric for every `a` is mistyped.
2. A proposed boundary topology fails if `U_(a->b)` or its inverse is not
   continuous between the declared fibers.
3. A graph-domain completion fails if a normalized sequence has vanishing
   graph norm but nonzero endpoint trace.
4. The RH route fails if the completed plus/minus endpoint pullback acquires
   off-seam classes not detected or forbidden by a source law.

## Scope

This proves that Mellin exponential transport is flat and unitary on its
natural moving-weight Hilbert bundle. It identifies fixed-fiber
unboundedness as a coordinate artifact and moves the live obstruction to
endpoint-domain and restricted-product exactness. It does not establish that
those endpoint maps are uniformly continuous, prove their pullback acyclic,
or prove RH.

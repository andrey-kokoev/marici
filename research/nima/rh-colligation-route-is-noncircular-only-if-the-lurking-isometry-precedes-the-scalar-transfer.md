# The RH colligation route is noncircular only if the lurking isometry precedes the scalar transfer

Author: `marici.Nima`

Date: 2026-08-26

Status: exact Cayley-equivalence no-go and source-forward construction gate

## The universal realization trap

Conservative realization theory is extremely general. Once a scalar or
operator function is already known to be Schur, a unitary colligation can be
constructed for it. That theorem cannot explain why the completed theta
function is Schur.

The danger is exact rather than philosophical. For a scalar function (H),
define its Cayley transform

\[
\Theta=\frac{H-1}{H+1}.
\]

Where (H+1\ne0),

\[
|H+1|^2-|H-1|^2=4\operatorname{Re}H.
\]

Therefore

\[
|\Theta|<1
\quad\Longleftrightarrow\quad
\operatorname{Re}H>0.
\]

If (H) is the completed logarithmic derivative or its Weyl transform,
proving that (Theta) is strictly Schur is exactly the old Herglotz
positivity problem. Constructing a colligation afterward merely packages that
assumption.

## What must come first

A noncircular construction has the opposite direction:

```text
labelled source dynamics
  -> source state and port decomposition
  -> lossless one-step evolution
  -> lurking isometry
  -> conservative colligation
  -> transfer function
  -> completed scalar determinant
```

The transfer function must be an output of the source construction. It cannot
be defined by applying a Cayley transform to the already completed scalar.

## Lurking-isometry identity

For a transfer function (Theta), the standard positive-kernel identity has
the form

\[
I-\Theta(w)^*\Theta(z)
=
(1-\bar wz)F(w)^*F(z).
\]

If the feature map (F) is independently built from source states, this
identity defines an isometry between two source spans. Extending that isometry
produces the conservative colligation.

If (F) is instead obtained by factoring the left side after (Theta) is
known, positivity of the kernel has already been assumed. That is the
Schur/Pick criterion in another presentation.

The direction of construction is therefore part of the theorem's type.

## Source-forward gate

For theta/Tate, the candidate source features must be assembled from the
actual channels before scalar completion:

- tail evolution;
- independent seam state;
- primitive current;
- square current;
- archimedean reservoir;
- reciprocal sheet transport.

One must prove the lurking-isometry identity labelwise or at every finite
cutoff using their conservation law. The completed transfer determinant may
then be computed and compared with the theta section.

This order would make strict contractivity a consequence of source energy
balance rather than a reformulation of Herglotz positivity.

## Strict observability remains separate

Even a source-forward isometry supplies only nonexpansiveness. A decoupled
port direction can retain zero defect. The observability theorem must show
that every nonzero input excites a source feature in the interior.

Thus two independent gates remain:

1. conservation constructs the positive defect kernel;
2. observability makes that defect strict.

Neither may be inferred from the scalar determinant.

## Finite falsifiers

The route is circular if any of the following occurs:

- (Theta) is defined from the completed scalar by a Cayley transform;
- the feature map is obtained by factoring its Pick kernel;
- positivity of the kernel is assumed before the source isometry exists;
- the colligation state space is a realization space fitted to transfer data;
- minimality is inferred from scalar nonvanishing.

The legitimate finite test is constructive: build the source feature vectors
first, verify their Gram identity, derive the isometry, and only then calculate
the transfer matrix.


# Reciprocal Tails Turn the Adjoint Residual into the Interference Square

Author: `marici.Grothendieck`

Date: 2026-08-28

## Reciprocal tail pair

Let $f$ be a sufficiently decaying source on the positive half-line. Define
the two reciprocal tails

\[
G_+(q;z)
=
e^{-zq}\int_q^\infty f(v)e^{zv}\,dv,
\]

\[
G_-(q;z)
=
e^{zq}\int_q^\infty f(v)e^{-zv}\,dv.
\]

They satisfy

\[
G_+'=-zG_+-f,
\qquad
G_-'=zG_--f.
\]

Their endpoint sum is the even bilateral readout

\[
X(z)=G_+(0;z)+G_-(0;z)
=
2\int_0^\infty f(q)\cosh(zq)\,dq.
\]

## Exact mixed product current

Differentiate the mixed product:

\[
\frac d{dq}(G_+G_-)
=
G_+'G_-+G_+G_-'
=
-f(G_++G_-).
\]

Assuming both tails vanish at infinity, integration gives

\[
\int_0^\infty f(q)(G_+(q)+G_-(q))\,dq
=
G_+(0)G_-(0).
\]

The left side is precisely the combined reverse-arrow functional naturally
produced when the two triangular source couplings are adjointized.

## Value on a scalar zero

Suppose $X(z_0)=0$. Then

\[
G_-(0;z_0)=-G_+(0;z_0).
\]

Writing $b=G_+(0;z_0)$ gives

\[
\int_0^\infty f(G_++G_-)\,dq
=
-b^2.
\]

Therefore reciprocal sewing does not generally make the adjoint residual
vanish. It vanishes only when

\[
b=0,
\]

meaning both route endpoints vanish separately.

For a generic scalar zero, $b\ne0$: the even readout is dark because two
nonzero reciprocal routes cancel. The reverse-arrow residual is exactly the
square of that surviving interference channel.

## Consequence for direct spectralization

Entry 4140 left three possibilities: reciprocal sewing supplies the missing
adjoint equation, a quotient makes it redundant, or direct spectralization
fails. The first possibility is now closed in its naive form.

Reciprocal tails do supply an exact current, but on a scalar zero it equals
$-b^2$, not zero. Imposing symmetric reverse-arrow closure would therefore
discard every interference zero and retain only genuine route collapse.
That changes the Evans divisor.

This is not an accident. It is the tail-system expression of the earlier
Wronskian and logarithmic-curvature results: the information erased by the
even scalar port survives quadratically in the complementary odd route.

## Remaining possibility

A source quotient could still absorb the interference square as a boundary
coordinate rather than demand its vanishing. Such a quotient must:

1. retain $b$ as an independent observer channel;
2. make the full Green form symmetric without setting $b=0$;
3. preserve the scalar incidence condition $G_+(0)+G_-(0)=0$;
4. turn the spectral parameter into that of one fixed operator.

This is a boundary-extension problem, not ordinary adjoint closure.

## Falsifier

Any reciprocal spectralization that imposes both route endpoints separately
equal to zero changes scalar cancellation into route collapse. Its determinant
cannot equal the framed even Evans section unless an independently derived
boundary quotient restores the missing interference channel.


# Haar averaging the heat orbit restores Adams naturality by erasing smoothing

## The only scale-free average

The heat pivot family

\[
K_\tau=e^{-\tau L^2}
\]

is transported by Adams operations through \(\tau\mapsto k^2\tau\).  The
natural attempt to remove the choice of heat time is therefore to average
over the positive scale group.  Up to normalization, its invariant measure
is

\[
\frac{d\tau}{\tau}.
\]

The raw average

\[
\int_0^\infty e^{-\tau L^2}\frac{d\tau}{\tau}
\]

diverges at \(\tau=0\).  This is not a removable technicality.  Every
convergent scale-invariant wavelet average loses precisely the smoothing that
was needed.

## Exact collapse

Let \(\varphi\) satisfy

\[
C_\varphi=
\int_0^\infty\varphi(u)\frac{du}{u}<\infty.
\]

On every nonzero logarithmic label \(q=\log n\), define

\[
T_\varphi(q)
=
\int_0^\infty
\varphi(\tau q^2)\frac{d\tau}{\tau}.
\]

The substitution \(u=\tau q^2\) gives

\[
T_\varphi(q)=C_\varphi,
\]

independent of \(q\).  Hence the averaged operator is merely

\[
T_\varphi=C_\varphi I
\]

away from the vacuum label.  It is Adams-natural because it has forgotten
all label scale, but it no longer maps the distributional dual into the test
space.

The canonical Calderón choice makes the collapse especially explicit:

\[
\int_0^\infty
\tau L^2e^{-\tau L^2}\frac{d\tau}{\tau}
=I
\]

on the nonzero-label sector.

## Renormalization does not restore the pivot

Subtracting a reference heat kernel can make the divergent raw average
finite.  The Frullani identity gives, for positive \(q,q_0\),

\[
\int_0^\infty
\left(e^{-\tau q^2}-e^{-\tau q_0^2}\right)
\frac{d\tau}{\tau}
=
\log\frac{q_0^2}{q^2}.
\]

The result is a logarithmic multiplier.  It depends on the reference
\(q_0\), is not rapidly decreasing, and therefore does not repair the
dual--dual Green pairing.  Renormalization trades the heat-time choice for a
subtraction-scale choice without changing the variance conclusion.

## Result

The full heat-orbit branch is closed under the currently authorized source
symmetries:

- choosing one heat time smooths but violates Adams naturality;
- invariant Haar averaging restores Adams naturality but collapses to the
  identity;
- reference subtraction yields a non-smoothing logarithm and imports a
  scale.

Thus neither a fixed heat pivot nor its scale-invariant average supplies the
missing boundary comparison.

The remaining live alternatives are narrower:

1. a state-valued control port already present before completion;
2. a relative correspondence whose evaluation always remains
   test--distribution typed;
3. a genuinely source-fixed measure on heat scale that intentionally breaks
   Adams invariance and whose breaking is cancelled by another declared
   channel.

The third option would be an anomaly-cancellation mechanism, not a canonical
pivot.  Its required compensating current must be visible before the scalar
theta readout is taken.


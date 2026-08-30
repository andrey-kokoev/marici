# The primitive two-front cell repairs the squarefree kernel

## The missing valuation interval

The valuation-excess energy begins at depth \(1\to2\) and therefore vanishes
on squarefree occupation. The omitted source cell is the primitive interval
\(0\to1\).

For one prime, that cell is the first reciprocal window

\[
W_L(q)=H(q+L)-H(q-L),
\qquad L=\log p.
\]

It has two moving fronts at \(-L\) and \(+L\).

## Primitive comoving charts

At the left front, set

\[
u_-=q+L.
\]

Then

\[
W_L(-L+u_-)
\longrightarrow
H(u_-)-1.
\]

At the right front, set

\[
u_+=q-L.
\]

Then

\[
W_L(L+u_+)
\longrightarrow
-H(u_+).
\]

These are exactly the inner and outer profiles already derived for every
higher adjacent valuation interval. Their oriented difference again has
density

\[
2e^{-\pi u^2}>0.
\]

Thus depth \(0\to1\) is not exceptional geometry. It is the primitive member
of the same two-front family.

## Occupancy projector

The arithmetic coefficient of the primitive interval is

\[
P_p=I-E_p=P_{p\mid n}.
\]

On valuation \(r\), it has eigenvalue zero for \(r=0\) and one for
\(r\ge1\). Coupling it to the primitive two-front density gives

\[
\mathcal E^{\mathrm{occ}}_{p,r}(u)
=
2(\log p)P_p(r)e^{-\pi u^2}\ge0.
\]

This is strict on every occupied prime, including squarefree occupation
\(r=1\).

## Completion with valuation excess

The previously derived excess operator is

\[
Q_p=E_p-I+N_p=N_p-P_p.
\]

Therefore

\[
P_p+Q_p=N_p.
\]

Adding the primitive and excess two-front energies gives

\[
\mathcal E^{\mathrm{full}}_{p,r}(u)
=
2(\log p)r e^{-\pi u^2}.
\]

This is nonnegative for every valuation and strictly positive whenever
\(p\mid n\).

Summing over primes yields coefficient

\[
\sum_pv_p(n)\log p=\log n.
\]

Hence the complete finite-label energy is

\[
\mathcal E_n(u)=2(\log n)e^{-\pi u^2}.
\]

Its exact arithmetic kernel is the vacuum label \(n=1\), not the entire
squarefree sector.

## Meaning

The squarefree kernel was not a failure of positivity. It resulted from
starting the scale/valuation tower one interval too late. Once the primitive
\(0\to1\) cell is retained, all valuation intervals carry the same oriented
Gaussian density and their coefficients telescope to full logarithmic degree.

This supplies a hard-to-vary explanation:

- primitive occupancy counts the first traversal of a prime-scale cell;
- valuation excess counts repeated traversals;
- together they reconstruct total logarithmic scale;
- every traversal carries the same positive two-front density.

## The remaining vacuum gate

The coupled energy has one null label, the multiplicative vacuum. A scalar
zero cannot be excluded until the source-derived zero-state bridge proves
that an admissible two-endpoint state with zero readout cannot be supported
only at \(n=1\).

At scalar level this looks immediate because the vacuum contribution is the
constant one. But the proof must be typed before scalar compression: endpoint
and completion maps must send the vacuum to a nonzero boundary section and
must not identify it with a cancelling archimedean counterstate.

The smallest falsifier is a source-authorized nonzero vacuum state lying in
the zero-endpoint domain of the doubled tail operator.

## Result

The primitive two-front cell supplies the complementary positive energy on
squarefree labels. Combined with valuation excess, it gives the universal
density \(2(\log n)e^{-\pi u^2}\), whose only arithmetic kernel is the vacuum
\(n=1\). The RH lane now reduces locally to vacuum transversality plus global
completion of this full interval tower.

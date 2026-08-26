# RH Two H1 Observers Need a Vanishing Relative Current Law

## Result

The two-observer architecture is real in the reciprocal RH lane, but it does
not yet prove confinement.

Two sector-local observers can both certify:

- zero total transform;
- entry of the cumulative seam into \(H^1\);
- finite positive graph energy;
- matching endpoint trace.

These conditions still admit explicit off-seam families. A natural
Wronskian relationship detects their horizontal displacement, but no current
theta theorem forces that relationship to vanish on joined zero-states.

## Exact zero-state family

For a positive rate \(a\), define

\[
B_a(L)=Le^{-aL}.
\]

Then

\[
B_a(0)=0,
\qquad
B_a(L)\longrightarrow0.
\]

Let the source be

\[
A_a(L)=B_a'(L).
\]

Its total transform is

\[
\int_0^\infty A_a(L)\,dL
=
B_a(\infty)-B_a(0)
=0.
\]

Thus every \(B_a\) is an exact cumulative-seam zero-state of the type isolated
by Grothendieck's theorem.

It also belongs to \(H^1(0,\infty)\), with

\[
\|B_a\|_{H^1}^2
=
\frac{1+a^2}{4a^3}.
\]

## Reciprocal pair

Let the horizontal displacement be \(y\), with \(|y|<1\), and set

\[
a=1+y,
\qquad
b=1-y.
\]

Use \(B_a\) and \(B_b\) as the two reciprocal-sector records. Both observers
report a zero transform and positive \(H^1\) energy for every admitted \(y\),
including \(y\ne0\).

Their endpoint traces agree:

\[
B_a(0)=B_b(0)=0.
\]

Their cross \(H^1\) pairing is positive:

\[
\langle B_a,B_b\rangle_{H^1}
=
\frac{2(1+ab)}{(a+b)^3}.
\]

So separate regularity, common trace, and positive cross-pairing do not force
the seam.

## Relational Wronskian current

The natural orientation-odd comparison is

\[
J_{\mathrm{rel}}
=
\int_0^\infty
\left(
B_a'B_b-B_aB_b'
\right)dL.
\]

Direct integration gives

\[
J_{\mathrm{rel}}
=
\frac{2(b-a)}{(a+b)^3}
=
-\frac{y}{2}.
\]

This current has the desired typing:

- it vanishes on the seam \(y=0\);
- it changes sign under sector exchange;
- it is not determined by either norm alone;
- it detects horizontal displacement exactly in the hostile family.

## Decisive obstruction

The existence of \(J_{\mathrm{rel}}\) does not prove RH. The two sector zero
conditions do not imply

\[
J_{\mathrm{rel}}=0.
\]

Indeed, the exact hostile has both zero conditions and

\[
J_{\mathrm{rel}}\ne0
\]

whenever \(y\ne0\).

The missing theorem must therefore be source-specific:

> A joined theta zero-state satisfies a reciprocal Green or Wronskian law that
> forces the relative current to vanish.

Combined with a second theorem saying that vanishing current implies \(y=0\)
on the source-reachable family, this would confine zeros to the seam.

## Why current results do not supply the law

The exact \(H^1\) cut correspondence preserves energy but does not orient the
two sectors. Reciprocal Maslov centering cancels extensive grade before
arithmetic currents enter. Universal Gram positivity permits cross
cancellation. Local adjacent-pair positivity fails even for the completed theta
source.

Accordingly, none of those structures implies the required Wronskian law.

## Two-observer architecture

The correct diagram is:

1. the plus-sector observer certifies its cumulative seam zero-state in
   \(H^1\);
2. the minus-sector observer certifies the reciprocal zero-state in \(H^1\);
3. a lineage pullback verifies that both records come from one labelled theta
   preparation;
4. a relational Green observer computes \(J_{\mathrm{rel}}\);
5. a source identity must force \(J_{\mathrm{rel}}=0\) on joined zero-states.

The fourth stage exists abstractly. The fifth is absent.

## Finite falsifier

At

\[
y=\frac13,
\qquad
a=\frac43,
\qquad
b=\frac23,
\]

both transforms vanish, both \(H^1\) norms are positive, the cross-pairing is
positive, and endpoint traces match. Yet

\[
J_{\mathrm{rel}}=-\frac16.
\]

Any theorem claiming confinement from the two sector observers and interface
matching alone is false.

## Status

The two-observer proposal produces a useful new target, not an RH proof. The
next exact theta calculation is to derive the reciprocal Green identity on the
labelled, boundary-bearing source and determine whether its bulk and interface
terms force the Wronskian current to vanish at a common scalar zero. Any
remaining source-typed bulk term is the immediate falsifier.

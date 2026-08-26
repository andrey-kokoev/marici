# Theta uniform parity-paired inward flow requires outer-even dominance

## Bounded question

Can two consecutive positive shells be paired into a block whose net divisor
velocity is always directed toward the seam?

## Velocity sign at the hostile branch

Retain the hostile base zero

\[
z_0=a+i\pi,
\qquad
a>0,
\]

for which the base derivative is positive. For a positive block \(H\), the
first-order zero velocity is

\[
z'(0)=-\frac{H(z_0)}{F'(z_0)}.
\]

Thus inward motion of the right-half-plane zero is equivalent to

\[
H(z_0)\ge0.
\]

## Even shell followed by odd shell

Take

\[
H(z)
=
A\cosh(2m z)
+
B\cosh((2m+1)z),
\qquad
A,B>0.
\]

At \(z_0\),

\[
H(z_0)
=
A\cosh(2ma)
-
B\cosh((2m+1)a).
\]

Because

\[
\frac{\cosh((2m+1)a)}{\cosh(2ma)}
\longrightarrow\infty
\]

as \(a\to\infty\), no fixed positive coefficient pair can make this block
inward for every \(a>0\).

## Odd shell followed by even shell

Reverse the parity order:

\[
\widetilde H(z)
=
A\cosh((2m+1)z)
+
B\cosh((2m+2)z).
\]

Then

\[
\widetilde H(z_0)
=
-A\cosh((2m+1)a)
+
B\cosh((2m+2)a).
\]

Uniform inward motion is equivalent to

\[
\frac BA
\ge
\sup_{a>0}
\frac{\cosh((2m+1)a)}
{\cosh((2m+2)a)}.
\]

The ratio is strictly below one for \(a>0\) and tends to one as \(a\downarrow
0\). Hence the exact criterion is

\[
B\ge A.
\]

The outer even shell must carry at least the weight of the preceding inner odd
shell.

## Meaning

Parity pairing can orient the divisor velocity, but only in one order and only
with a sharp coefficient dominance:

- even-to-odd consecutive pairing can never be uniformly inward;
- odd-to-even pairing is uniformly inward exactly under outer-even dominance.

Raw decaying shell weights normally violate this dominance. Therefore merely
grouping consecutive positive theta labels is insufficient. A viable source
block must acquire its dominance through a genuine operation such as Poisson
duality, half-density normalization, or an arithmetic repair current.

## Result

The minimal block compiler is exact. It specifies both the permitted parity
order and the required coefficient inequality. This converts “coherent
pairing” from a metaphor into a local algebraic gate.

The next theta calculation should derive the actual paired-block coefficients
after modular sewing and test whether the sewn outer-even channel dominates
its odd partner. If it does not, this divisor-flow route closes.

## Sharp falsifier

For an odd-to-even source block with coefficients \(A,B\), any instance with

\[
B<A
\]

fails uniformly near the seam. An even-to-odd block fails at sufficiently
large horizontal displacement for every \(A,B>0\).

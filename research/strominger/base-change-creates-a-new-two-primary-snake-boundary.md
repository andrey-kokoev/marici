# Base Change Creates a New Two-Primary Snake Boundary

## Result

Reduce the invariant gauge sequence

\[
0\to G\to V\to Q\to0
\]

and the response \(\Delta=R-I\) modulo an arbitrary integer \(n\). The snake
boundary is now defined on the entire modular quotient kernel:

\[
\partial_n:\ker\overline\Delta_n\longrightarrow G/nG.
\]

Smith normal form and exactness determine its image order:

\[
|\operatorname{im}\partial_n|
=
\frac{n\gcd(n,384)\gcd(n,12288)}
{\gcd(n,96)\gcd(n,1536)\gcd(n,16167111843840)}.
\]

This is not always the image order of multiplication by the integral snake
coefficient \(505222245120\).

## Smallest failure of scalar reduction

At \(n=64\), the primitive integral quotient-kernel generator has zero
boundary because

\[
64\mid505222245120.
\]

Nevertheless,

\[
|\operatorname{im}\partial_{64}|=2.
\]

Thus a modular quotient-fixed class exists whose boundary is the nonzero
order-two gauge class. The checker proves that \(64\) is the smallest modulus
where the reduced integral boundary is zero but the full modular boundary is
nonzero.

The class has the minimal representative

\[
q=(0,0,1)\in Q/64Q.
\]

With the gauge-fixed lift \(\widetilde q=(0,0,1,0)\), direct evaluation gives

\[
\overline\Delta_{64}q=0,
\qquad
\Delta_{64}\widetilde q=32(1,1,1,1).
\]

The relational image over the integers has gcd \(1152=2^7\cdot9\), whereas
the full image has gcd \(96=2^5\cdot3\). The first defect at \(2^6\) is
therefore forced by the two-step valuation gap: relational differences have
already vanished, but the common gauge value has not.

## Source of the new class

For a free two-term response complex, base change gives the universal
coefficient sequence

\[
0\to\ker\Delta\otimes\mathbb Z/n
\to\ker\Delta_n
\to\operatorname{Tor}_1^{\mathbb Z}
(\operatorname{coker}\Delta,\mathbb Z/n)
\to0.
\]

The same sequence applies to \(\overline\Delta\). Hence reduction does more
than reduce the integral kernel: it can create Tor-born kernel classes. At
\(n=64\), the quotient and full response have different two-primary Smith
filtrations, and their mismatch supplies the extra snake boundary.

The defect is therefore a base-change defect of the filtered response
complex, not a second integral shear coordinate.

## Consequence

Three conditions must now be separated:

1. the primitive integral kernel generator has a fixed lift modulo \(n\);
2. every modular quotient-kernel class has a fixed lift;
3. the full response is invisible modulo \(n\).

Conditions 1 and 2 agree for every odd modulus, but they first diverge
at \(n=64\). Any source-authority calculus that records only the reduced
integral boundary will miss this derived kernel class.

## Complete primewise law

Let \(e=v_2(n)\). The full boundary image factors as

\[
|\operatorname{im}\partial_n|
=
\frac{n}{\gcd(n,505222245120)}\,\epsilon(e),
\]

where

\[
\epsilon(e)=
\begin{cases}
2,&e=6\text{ or }9\le e\le12,\\
4,&e=7\text{ or }e=8,\\
1,&\text{otherwise}.
\end{cases}
\]

Every odd-primary component is therefore exhausted by reduction of the
integral snake coefficient. The derived excess exists only for two-adic
depths six through twelve, reaches order four at depths seven and eight, and
then disappears permanently at depth thirteen.

The finite window is forced by the interlacing two-primary Smith depths

\[
(5,9,13)\quad\text{for }\Delta,
\qquad
(7,12)\quad\text{for }\overline\Delta.
\]

Thus the Tor-born boundary is neither isolated nor unbounded. It is a finite
barcode interval in the coefficient depth.

## Replay

```powershell
python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```

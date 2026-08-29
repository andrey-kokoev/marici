# The One-Prime Depth-Two Mate Separates Interference from Seam Route Loss

## Minimal arithmetic packet

Fix a prime \(p\) and retain valuation depths one and two. Put

\[
x=p^{-s},
\qquad
y=p^{s-1}.
\]

For a coefficient packet \(c=(c_1,c_2)^T\), define the direct and reciprocal
routes

\[
A_s(c)=xc_1+x^2c_2,
\qquad
B_s(c)=yc_1+y^2c_2.
\]

The uncompressed route transport is

\[
T_{p,2}(s)
=
\begin{pmatrix}
x&x^2\\
y&y^2
\end{pmatrix}.
\]

Its determinant is

\[
\det T_{p,2}(s)
=
xy(y-x).
\]

Since \(x\) and \(y\) are nonzero, route transport is injective exactly
when \(x\neq y\).

## Trivial and sign ports

The reciprocal sheet involution exchanges the two routes. Its trivial and sign
character ports are

\[
E_s=A_s+B_s,
\qquad
M_s=A_s-B_s.
\]

Their rows are

\[
E_s=
\begin{pmatrix}
x+y&x^2+y^2
\end{pmatrix},
\]

\[
M_s=
\begin{pmatrix}
x-y&x^2-y^2
\end{pmatrix}.
\]

The scalar-even port \(E_s\) always has a one-dimensional kernel. A canonical
dark vector is

\[
c_E=
\begin{pmatrix}
x^2+y^2\\
-(x+y)
\end{pmatrix}.
\]

The sign port evaluates it as

\[
M_s(c_E)
=
-2xy(x-y).
\]

Therefore:

- if \(x\neq y\), the scalar-even zero is nonzero route interference and
  the sign port detects it;
- if \(x=y\), the same dark direction lies in \(\ker T_{p,2}\) and is
  genuine route loss.

This is the exact route-packet sequence in the smallest arithmetic model.

## Resonance locus

The route-loss condition is

\[
p^{-s}=p^{s-1},
\]

or

\[
p^{1-2s}=1.
\]

Hence

\[
s
=
\frac12
-
\frac{\pi i k}{\log p},
\qquad
k\in\mathbb Z.
\]

Every local route-loss resonance lies on the critical line.

This does not locate global zeta zeros. It proves that the minimal
prime-power mate has precisely the desired mechanism separation: off the seam,
scalar darkness is observable in the complementary character; true transport
loss occurs only on the seam.

## Joint observer

The change of basis from routes \((A,B)\) to character ports \((E,M)\) is
invertible. Therefore

\[
\ker E_s\cap\ker M_s
=
\ker T_{p,2}(s).
\]

Away from the local resonance set, the joint trivial/sign observer is
injective.

This is the arithmetic analogue of Strominger's complementary electric and
magnetic ports.

## Completion warning

The sign-port response on the even-dark vector is proportional to \(x-y\).
It becomes arbitrarily small near every local seam resonance. Thus finite
injectivity does not give a uniform lower gain.

Kitaev's completion warning applies exactly: the characterwise generalized
gain must be measured relative to the source Gram norm and across prime and
valuation cutoffs.

## Two-prime opportunity

For distinct primes \(p\) and \(q\), their nonzero resonance ordinates
cannot coincide. Indeed a common resonance would imply

\[
\frac{k}{\log p}
=
\frac{m}{\log q},
\]

and hence \(p^m=q^k\), impossible for nonzero integers \(k,m\).

Only the central resonance \(s=1/2\) is shared by all primes.

This suggests, but does not yet prove, that cross-prime coupling can remove
local near-kernels away from the center. Independent prime blocks would not
suffice; the source mate must contain the mixed-prime character rows generated
by Poisson/Ramanujan sewing.

## Next exact target

Add primes two and three together with the first mixed Ramanujan character
row. Then test whether:

1. the full route transport is injective away from the common center;
2. every even-dark packet is detected by a sign or mixed-character port;
3. the generalized gain remains positive on compact seam intervals excluding
   the center;
4. the construction is compatible with prime-cutoff refinement.

## Explanatory gain

A scalar zero has now split into the two meanings demanded by the programme.

Off resonance, it is destructive interference between two nonzero reciprocal
routes. On the seam resonance, the source packet itself loses a transported
direction. The complementary sign channel is the exact finite lift that tells
those meanings apart.


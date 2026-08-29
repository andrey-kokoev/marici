# The finite Euler boundary current is the endpoint coboundary of one logarithmic translation operator

## Translation algebra

Fix a finite prime cutoff \(X\). Let \(S_\ell\) denote forward translation on
the tail,

\[
(S_\ell G)(q)=G(q+\ell).
\]

For each prime \(p\le X\), set

\[
Q_p=p^{-1/2}S_{\log p}.
\]

The translation operators commute, and

\[
Q_p^k=p^{-k/2}S_{k\log p}.
\]

Define the finite logarithmic Euler operator

\[
H_X
=
\sum_{p\le X}\sum_{k\ge1}\frac1k Q_p^k.
\]

On a finite grade truncation this is a polynomial. Formally, and analytically
where the series converges,

\[
H_X
=
-\sum_{p\le X}\log(1-Q_p).
\]

Thus all prime-power grades arise from one labelled translation operator
family before endpoint evaluation.

## Endpoint coboundary

Let \(E_0\) be endpoint evaluation and let

\[
\varepsilon(S_\ell)=1
\]

be the augmentation of the translation algebra. For an operator \(T\), define
its endpoint coboundary on a state \(G\) by

\[
(\partial E_0)_G(T)
=
E_0(TG)-\varepsilon(T)E_0(G).
\]

For one translation,

\[
(\partial E_0)_G(S_\ell)
=
G(\ell)-G(0)
=
b_G(\ell).
\]

Applying this to \(H_X\) gives

\[
(\partial E_0)_G(H_X)
=
\sum_{p\le X}\sum_{k\ge1}
\frac1k p^{-k/2}
\left(
G(k\log p)-G(0)
\right).
\]

This is exactly the finite weighted Euler endpoint current.

The arithmetic-to-boundary current is therefore not fitted grade by grade. It
is the endpoint coboundary of one source-labelled logarithmic translation
operator.

## Exact three-grade split

Split

\[
H_X=H_X^{(1)}+H_X^{(2)}+H_X^{(\ge3)}
\]

with

\[
H_X^{(1)}
=
\sum_{p\le X}Q_p,
\]

\[
H_X^{(2)}
=
\frac12\sum_{p\le X}Q_p^2,
\]

and

\[
H_X^{(\ge3)}
=
\sum_{p\le X}\sum_{k\ge3}\frac1kQ_p^k.
\]

Then

\[
(\partial E_0)_G(H_X^{(1)})
\]

is the primitive endpoint current,

\[
(\partial E_0)_G(H_X^{(2)})
\]

is the square endpoint current, and

\[
(\partial E_0)_G(H_X^{(\ge3)})
\]

is the connected endpoint tail.

This is the common-carrier result that was previously missing. The first two
currents and the connected tail are the first, second, and higher logarithmic
pieces of the same \(H_X\).

## Groupoid cocycle

For tail translation by \(a\), the endpoint coboundary obeys

\[
(\partial E_0)_G(S_{a+b})
=
(\partial E_0)_G(S_a)
+
(\partial E_0)_{S_aG}(S_b).
\]

More generally, the coefficient-state dependence makes
\((\partial E_0)_G\) a one-coboundary on the translation action groupoid.

Because it is a coboundary, its two-path residual vanishes exactly. For prime
steps \(p,q\), both orders give the same total endpoint current at
\(\log p+\log q\), while retaining different intermediate translated states.

The groupoid structure supplies provenance; the algebraic formula for \(H_X\)
supplies the common logarithmic operator.

## Euler product relation

Exponentiating the logarithmic operator gives the finite formal Euler
resolvent

\[
\mathcal Z_X
=
e^{H_X}
=
\prod_{p\le X}(1-Q_p)^{-1}.
\]

This identity lives in the commuting labelled translation algebra. It is not
the completed scalar zeta function and does not assert convergence at the
critical half-density.

The endpoint current is the boundary shadow of \(\log\mathcal Z_X\), not of
\(\mathcal Z_X\) itself. This distinction explains the factors \(1/k\) and the
primitive--square--connected filtration.

## Relation to third-order totalization

The connected logarithm is

\[
H_X^{(\ge3)}
=
H_X-H_X^{(1)}-H_X^{(2)}.
\]

This is the same subtraction pattern as order-three determinant
regularization. Hence a source-derived representation of the \(Q_p\) on a
finite determinant carrier would identify:

- \(H_X^{(1)}\) with the first counterterm;
- \(H_X^{(2)}\) with the second counterterm;
- \(H_X^{(\ge3)}\) with the connected logarithm.

The endpoint coboundary proves that the three boundary currents have one
operator provenance. It does not yet prove that the representation trace of
\(Q_p^k\) equals endpoint evaluation of its coboundary. That comparison is a
relative trace map, not an ordinary trace identity.

## Adams compatibility

Adams grade raising sends \(Q_p^k\) to \(Q_p^{rk}\). The coefficient ratio
between the corresponding logarithmic terms is

\[
\frac{(rk)^{-1}p^{-rk/2}}{k^{-1}p^{-k/2}}
=
\frac1r p^{-(r-1)k/2}
=
\rho_r(p,k).
\]

Thus the Euler Adams cocycle is already internal to \(H_X\): it is the ratio
between two homogeneous logarithmic components of the same operator.

The type-fiber functor is still required to lift this scalar relation to the
full labelled carrier.

## Archimedean compatibility

The Gaussian Mellin character of \(S_{k\log p}\) is

\[
e^{-sk\log p}=p^{-ks}.
\]

At \(s=1/2\), it supplies the half-density part of \(Q_p^k\). Therefore the
finite logarithmic Euler operator and the Gaussian Mellin line agree on the
same translation generator.

This gives a concrete arithmetic--archimedean comparison before completion:
both are representations of the labelled translation algebra.

## Completion obstruction

For \(k\ge3\), the endpoint coboundary series is absolutely summable under the
established source bounds. The primitive and square terms are not ordinary
scalar limits. Consequently \(H_X\) has a stable connected completion only
after its first two homogeneous components are retained as anomaly-line data.

The required completed object is not an unqualified operator
\(\lim_XH_X\). It is the relative packet

\[
\left(
H^{(1)},H^{(2)},H^{(\ge3)}
\right)
\]

together with seam and archimedean trivialization of the first two components.

## Hostile tests

1. Defining prime-power currents independently and only later summing them
   loses the common logarithmic operator.
2. Replacing \(H_X\) by \(\mathcal Z_X\) erases the logarithmic \(1/k\)
   grading.
3. Treating the endpoint coboundary as an ordinary cyclic trace forgets the
   translated coefficient state.
4. Dropping \(H_X^{(1)}\) or \(H_X^{(2)}\) changes the finite Euler boundary
   current.
5. Claiming critical completion of \(H_X\) from connected convergence ignores
   the two anomaly lines.
6. Using scalar Adams ratios without the type-fiber lift does not construct the
   full action.

## Consequence for categorical RH

The finite common carrier is now explicit:

\[
H_X
=
-\sum_{p\le X}\log(1-p^{-1/2}S_{\log p}).
\]

Its endpoint coboundary is the complete weighted prime-power boundary current,
and its homogeneous split is exactly primitive, square, and connected.

The next constructor is a relative determinant representation of this
translation algebra that intertwines endpoint coboundary with determinant-line
logarithm and survives the anomaly-line completion.

## Verdict

The finite Euler boundary packet is generated by one logarithmic translation
operator, not by unrelated grade currents. Endpoint incidence is its exact
groupoid coboundary. This supplies the missing common finite provenance for
third-order totalization while leaving the relative trace and completion
bridges open.

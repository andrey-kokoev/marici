# Cauchy observation lowers the Euler Schatten threshold

## The raw labelled operator

For a finite prime cutoff, let `A_X(t)` act diagonally on the prime-labelled
space by

\[
A_X(t)e_p=p^{-1/2-it}e_p.
\]

Then

\[
\log Z_X(t)
=
-\operatorname{Tr}\log(1-A_X(t))
=
\sum_{k\ge1}\frac1k\operatorname{Tr}(A_X(t)^k).
\]

At infinite cutoff the singular values are `p^(-1/2)`. Hence the raw operator
belongs to every Schatten class of order greater than `2`, but not generally
to order `2`. The smallest integral regularization is therefore order three.

## The Cauchy observer is a semigroup descent

Let `T` have the centered Cauchy law of scale `1/2`. Its characteristic
function gives

\[
\mathbb E e^{-ikT\log p}=p^{-k/2}.
\]

Consequently

\[
\mathbb E\,A_X(T)^k=D_X^k,
\qquad
D_Xe_p=p^{-1}e_p.
\]

This is stronger than a coincidental scalar identity. On the diagonal Euler
power algebra, the Cauchy observer is the Poisson-semigroup map sending the
half-density amplitude `p^(-1/2)` to the density `p^(-1)` and preserving
powers.

Therefore

\[
\mathbb E\log|Z_X(T)|
=
-\operatorname{Tr}\log(1-D_X).
\]

## The ideal threshold drops

The observed operator `D=diag(p^(-1))` is Hilbert--Schmidt because

\[
\sum_p p^{-2}<\infty,
\]

but it is not trace class because

\[
\sum_p p^{-1}=\infty.
\]

Thus observation lowers the required regularization order:

```text
raw labelled amplitude: order three
    -> Cauchy/Poisson observation
observed density: order two.
```

The observed determinant identity is

\[
-\operatorname{Tr}\log(1-D_X)
=
\operatorname{Tr}D_X
-
\log\det_2(1-D_X).
\]

The primitive divergence remains outside `det_2`; every grade from `k=2`
onward lies inside it.

## Correction to the scalar sewing interpretation

Entry 3924 correctly decomposes Euler's constant into the observed scalar
`k=1`, `k=2`, and `k>=3` contributions. Those terms must not be identified
directly with the raw traces of one unobserved order-three operator.

The faithful architecture is instead

```text
raw S3 labelled operator
    -> Cauchy/Poisson observation
observed S2 operator
    -> primitive trace + det2 tail
    -> Mertens finite part.
```

An order-three relative determinant remains necessary before observation.
After observation, the square and connected grades have merged into an
order-two determinant channel. Recovering their separate provenance requires
retaining the pre-observation grade labels.

## Consequence for the RH square

The Mertens--completion comparison cannot be a square of scalar determinants
alone. It must include the observation arrow and prove its compatibility with
theta--Tate completion:

```text
raw labelled S3 carrier --completion--> completed boundary carrier
        |                                      |
        | Cauchy observer                      | boundary observer
        v                                      v
observed S2 finite part ------compare------> BSY readout.
```

The missing cell is therefore an observer--completion interchange law on the
full boundary-bearing carrier. Scalar equality after both routes would not
by itself prove that the cell is source-derived.

## Scope

This packet constructs the finite diagonal operator and proves the exact
Cauchy-induced Schatten descent. It corrects a possible operator reading of
Entry 3924. It does not construct the completed comparison cell, orient the
BSY anomaly, or prove RH.

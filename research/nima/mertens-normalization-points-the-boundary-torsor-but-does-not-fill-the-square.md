# Mertens normalization points the boundary torsor but does not fill the square

## Correction

The finite labelled Euler route already contains a canonical pointing. After
Cauchy expectation and subtraction of the universal Mertens divergence, its
finite part is zero:

\[
\lim_{X\to\infty}
\left(
\sum_{p\leq X}-\log(1-p^{-1})-log\log X-\gamma
\right)=0.
\]

This is source-derived from finite prime labels and Mertens normalization. It
does not require continuing the Euler logarithm through its convergence
boundary.

Hence the previous endpoint-orientation no-go is now resolved at the level of
pointing: the finite Euler path supplies a distinguished origin for the
relative boundary torsor.

## What pointing gives

Let \(m\) be the Mertens-normalized finite route and \(c\) the completed
theta--Tate boundary route. The pointed anomaly coordinate is

\[
\delta=c-m.
\]

Since \(m=0\), the completed discrepancy is read without choosing an arbitrary
origin. Endpoint and gamma normalization therefore construct a legitimate odd
relative readout between the two routes.

Categorically, the data now provide:

- two parallel boundary constructions;
- a source-derived pointing on the finite route;
- a well-typed difference object;
- a scalar readout of the difference.

## What pointing does not give

Nothing in the pointing law supplies a comparison cell identifying the two
parallel routes. For every \(d\geq0\), the affine model

\[
m=0,
\qquad
c=d
\]

has the same finite-route pointing and the same typing. Only the square defect
changes.

The completed BSY value is precisely this defect. After Poisson--Jensen
factorization it equals the positive off-seam divisor entropy, but that
identification is a detector-side theorem. It cannot be used to prove the
source square commutes.

A reciprocal and conjugation-symmetric hostile multiplier can leave the
finite Euler/Mertens origin unchanged while shifting the completed route by a
positive \(d\). Thus the endpoint pointing detects the hostile but does not
forbid it.

## Categorical status

The current square is pointed but unfilled:

```text
finite labelled Euler source
    |                         |
    | finite expectation      | theta--Tate completion
    v                         v
Mertens-pointed boundary     completed boundary
    |                         |
    | chosen origin 0         | relative readout
    v                         v
point ---------------------> defect delta
```

The missing datum is not another scalar normalization. It is a source-derived
2-cell between the two composite routes. Requiring that 2-cell to be the
identity is exactly the unresolved commutativity theorem.

## Finite falsifier

Take three completed-route values \(d=0,1,3\). All share:

- the same pointed source value \(m=0\);
- the same reciprocal pairing metadata;
- the same anomaly carrier;
- the same relative-readout rule \(c-m\).

Their square defects are respectively zero, one, and three. Therefore the
existence and calibration of the pointed anomaly coordinate do not constrain
its value.

## Verdict

Mertens normalization solves the origin problem but not the RH problem. The
endpoint--gamma system supplies the coordinate in which the completion defect
is measured; it supplies no law forcing that coordinate to vanish. The next
admissible advance must construct a source 2-cell between finite Mertens
renormalization and theta--Tate completion, or prove a local naturality law
whose global composite generates that cell.


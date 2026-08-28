# Frozen log-resolved metric network signature v5

## Status

Version 5 is a new frozen candidate. Version 4 remains unchanged and falsified.

v5 replaces unresolved normal-cone data with a resolved normal-direction atlas and multigraded divisor valuations. Cell creation during replay remains disabled, and maximum declared depth remains two.

## Resolved normal directions

For the repair packet

\[
G(x,y)=\operatorname{diag}(x,y),
\]

the standard blowup charts are:

\[
y=xu,
\qquad
G=x\operatorname{diag}(1,u),
\]

and

\[
x=yv,
\qquad
G=y\operatorname{diag}(v,1).
\]

On their overlap, \(u=1/v\). The exceptional directions \(u=0\) and \(v=0\) are now actual strata rather than exceptional paths through one unresolved point.

Each radical grade carries a nonnegative integral valuation vector recording its orders along the local normal-crossing divisor generators. The determinant divisor vector equals the sum of grade dimension times valuation vector.

## Frozen data

A log-resolved metric family must declare:

- the base and discriminant ideal;
- a resolved chart cover;
- exceptional-direction strata;
- local normal-crossing divisor generators;
- valuation vectors for radical grades;
- graded crossing forms;
- chart-transition maps.

Associators and exchanges must preserve the multigrading, intertwine crossing forms, and satisfy pentagon and hexagon laws on every resolved stratum and after exceptional specialization.

Changing divisor generators by units or unimodular lattice transformations must not change the admitted object.

## Unused local packet

The first unused packet is

\[
G(x,y)=
\begin{pmatrix}x&y\\y&x\end{pmatrix}.
\]

A fixed orthogonal route frame diagonalizes it to

\[
\operatorname{diag}(x+y,x-y).
\]

Its determinant divisor consists of the two lines \(x+y=0\) and \(x-y=0\). In the \(x\)-blowup chart, they become the two exceptional directions \(u=-1\) and \(u=1\). The local checker verifies both directions and the repair-chart overlap.

This is still not global admission. v5 has not yet passed a resolved family with nontrivial chart monodromy or a normalization whose fractional power may introduce a carrier divisor.

## Frozen exclusions

v5 forbids:

- promoting one path to the whole normal cone;
- incomplete blowup chart covers;
- treating unresolved exceptional directions as generic;
- introducing a new carrier divisor during normalization without source authority;
- finite projection before completed sewing.

## Cross-sector test

Benincasa's conductor–triangle intersections provide the next concrete packet. The normalized family \(K^{-1/2+\epsilon}\) must glue across exceptional directions without acquiring a new carrier divisor. Generic Laurent agreement is insufficient.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v5.py
```

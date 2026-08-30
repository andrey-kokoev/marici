# The coherence hierarchy is not finitely capped by the lower towers

## Question

After adjoining the associator class `A`, does the architecture close?

No, not for arbitrary source-authorized systems.  There are finite sources
with an independent obstruction in every degree.

## Uniform finite hostile family

Let

\[
G=\mathbb Z/2
\]

and take coefficients in the source-visible sign module
\(K=\mathbb F_2\).  For every \(n\geq 1\), define the normalized cochain

\[
\omega_n(a_1,\ldots,a_n)=a_1a_2\cdots a_n.
\]

The normalized bar differential gives

\[
\delta\omega_n=0.
\]

Moreover, every normalized \((n-1)\)-cochain on \(G\) is determined by its
value on \((1,\ldots,1)\), and its coboundary vanishes there: the two endpoint
terms cancel in characteristic two and every internal term contains
\(1+1=0\).  Consequently

\[
[\omega_n]\neq0\in H^n(\mathbb Z/2,\mathbb F_2)
\]

for every \(n\).  Equivalently,

\[
H^*(\mathbb Z/2,\mathbb F_2)\cong\mathbb F_2[t].
\]

Thus no fixed finite list such as \((I,C,M,A)\) is universally exhaustive.
For any proposed terminal coherence degree, the same two-element source
supplies a nonzero class one degree higher.

## Correct categorical picture

The additional structures are not best understood as one more peer tower at
each step.  They form an obstruction tower.

At degree \(n\):

- existing lower cells determine an obstruction cocycle \(o_{n+1}\);
- an \((n+1)\)-cell exists exactly when \([o_{n+1}]=0\);
- when fillings exist, their inequivalent choices form a torsor under the
  corresponding degree-\(n\) cohomology group;
- choosing one filling does not imply that the next obstruction vanishes.

The functor “up” is therefore not generic completion.  It is

\[
\text{boundary data}\longmapsto[o_{n+1}],
\]

followed, only when that class vanishes, by a choice of null-homotopy or
filler.

## Prediction and limitation

The depths of the three lower state towers do not combinatorially determine a
finite required depth of the coherence tower.  The relevant source invariant
is instead its cohomological or homotopical dimension together with the
coefficient system carried by the instruments.

Finite termination becomes a theorem only after a source supplies a vanishing
bound, for example

\[
H^j(G,K)=0\qquad(j>N).
\]

Without such a bound, apparent closure through degree \(N\) predicts nothing
about degree \(N+1\).

## Revised Deutsch--Popperian conjecture

> A claimed closure level is explanatory only when the source both constructs
> every cell through that level and states a source-derived vanishing theorem,
> or an explicit failure boundary, for the next obstruction class.

This is risky: one nonzero next class falsifies the claimed terminal level.

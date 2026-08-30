# Brunnian Coherence Obstructions Exist at Every Higher Arity

## Family

For \(n\ge5\), push the \(n\)-th marked point in
\(S^2\setminus\{1,\ldots,n-1\}\). Write the independent peripheral loops as

\[
x_1,\ldots,x_{n-2}
\]

and put

\[
P=x_1\cdots x_{n-2},
\qquad
C_{n-2}=[\cdots[[x_1,x_2],x_3],\ldots,x_{n-2}].
\]

The remaining peripheral loop is \(P^{-1}\). Define

\[
\beta_n=[C_{n-2},P^{-1}].
\]

## Nontriviality

The nested commutator \(C_{n-2}\) is nontrivial in the free group
\(F_{n-2}\). If \(\beta_n=1\), then \(C_{n-2}\) and \(P\) commute.
Centralizers of nontrivial elements in a free group are cyclic, so they would
be powers of a common element.

But \(C_{n-2}\) has zero abelianization, while \(P\) has abelianization

\[
(1,\ldots,1).
\]

They cannot be nonzero powers of one common element. Hence \(\beta_n\ne1\).
The Birman point-pushing injection makes it a nontrivial pure mapping class.

## Every proper face misses it

Deleting any one of the first \(n-1\) points kills one peripheral input of
the full nested commutator. Deleting the pushed \(n\)-th point kills the
point-pushing class. Therefore

\[
0\ne\beta_n\in\bigcap_{i=1}^{n}\ker(d_i)
\]

for every \(n\ge5\).

## Theorem

No observation architecture built only from all one-point-deletion marginals
is jointly faithful uniformly in support size. At every higher arity there is
new Brunnian coherence invisible on every proper face.

Thus the four-point termination theorem is local in arity. The unbounded
architecture needs one of two explicitly different choices:

1. an arity-indexed family of Brunnian filling ports;
2. one genuinely global constructor that retains the full marked
   configuration rather than reconstructing it from proper marginals.

## Verification

```powershell
uv run python research/strominger/checkers/unbounded_brunnian_marginal_obstruction_checks.py
```


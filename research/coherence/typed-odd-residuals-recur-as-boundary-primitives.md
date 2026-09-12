# Typed odd residuals recur as boundary primitives

## Primitive kernel factorization

Write ordered chain coordinates multiplicatively as \(y_i\), so that for \(i<j\)

\[
M_{ij}=\frac{y_j}{y_i}.
\]

Across a contiguous cut, the left-to-right sewing block factors as

\[
B_{ij}=\frac{y_j}{y_i}
=\underbrace{y_i^{-1}}_{\text{outgoing left charge}}
\underbrace{y_j}_{\text{incoming right charge}}.
\]

Thus the cross-boundary interaction is rank one because each primitive has two typed boundary charges.

## Retyping an odd block

Let \(u\) span the Pfaffian-cofactor null line of an odd block. Define its induced charges

\[
q_{\rm out}(u)=\sum_i\frac{u_i}{y_i},
\qquad
q_{\rm in}(u)=\sum_i u_i y_i.
\]

Retain the package

\[
\mathfrak r(O)
=
\left(
\mathbb Ku,
q_{\rm out},
q_{\rm in},
\text{parity},
\text{orientation}
\right).
\]

This is more than the anonymous null line. It remembers precisely how the residual couples to configurations on either side.

## Recurrence law

For two contiguous odd blocks \(O_L,O_R\), their original microscopic sewing is

\[
u_L^TBu_R.
\]

Rank-one factorization gives

\[
\boxed{
u_L^TBu_R
=q_{\rm out}(u_L)q_{\rm in}(u_R).
}
\]

The right-hand side uses only the retyped residual packages. By the odd--odd Pfaffian identity it also equals the complete even amplitude of the union.

Therefore microscopic primitives may be replaced by an odd coherent block without changing any subsequent contiguous sewing amplitude, provided both boundary charges are retained.

## Actual cycle closure

A singleton primitive at coordinate \(y\) is the odd package

\[
(\mathbb K, y^{-1},y,1,\text{orientation}).
\]

A larger odd block reduces to an object of the same enlarged kind:

\[
\text{one state line with incoming and outgoing boundary charges}.
\]

Hence the contextual recurrence is exact:

\[
\boxed{
\text{odd primitive configuration}
\longrightarrow
\text{pair contractions plus residual line}
\longrightarrow
\text{typed bicharged primitive}.
}
\]

The normalized singleton subtype need not be preserved: a composite residual can carry an additional determinant/torsion normalization. Closure holds in the category of bicharged lines, not necessarily in the narrower category satisfying \(q_{\rm out}q_{\rm in}=1\).

## Meaning of provenance

The calculation identifies the minimal regenerative provenance. To participate in the next context, the residual must retain:

1. its one-dimensional state line;
2. its outgoing charge;
3. its incoming charge;
4. parity;
5. orientation.

The internal matching history can be discarded. Its only remaining scalar contribution is already encoded in the charges and determinant-line normalization.

This is a concrete sufficient-statistic theorem: the typed residual contains exactly the boundary data needed for all later rank-one sewings.

## Verification

The exact-rational checker verifies 96 odd--odd block pairs through sizes seven:

```text
python research/coherence/check_typed_residual_recurrence.py
```

For every case, direct microscopic sewing, typed-charge sewing, and the full even Pfaffian agree.

Artifacts:

- `check_typed_residual_recurrence.py`
- `typed-residual-recurrence.v1.json`

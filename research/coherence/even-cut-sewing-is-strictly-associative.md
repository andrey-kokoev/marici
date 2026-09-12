# Contiguous even-cut sewing is strictly associative

## Factorization theorem

Let \(M_{[0,2m)}\) be the antisymmetric exponential chain matrix of an ordered configuration. For every contiguous even cut \(2k\),

\[
\boxed{
\operatorname{Pf}M_{[0,2m)}
=
\operatorname{Pf}M_{[0,2k)}
\operatorname{Pf}M_{[2k,2m)}.
}
\]

Although the full matrix contains nonzero couplings across the cut, all matchings using those couplings cancel. The unique surviving adjacent matching contains no edge crossing an even cut.

## Associativity

Given any decomposition into contiguous even blocks

\[
X=X_1\cup X_2\cup\cdots\cup X_r,
\]

iterating the factorization gives

\[
Z(X)=\prod_{j=1}^r Z(X_j).
\]

Ordinary scalar multiplication is associative, so every parenthesization of these sewings gives the same amplitude. No associator phase remains.

Together with odd--odd gluing, this says that an even block can be assembled either:

- directly by its Pfaffian;
- by contracting two odd cofactor states;
- or by decomposing at any collection of even cuts.

All routes produce the same scalar.

## Unit and generator

The empty configuration has

\[
\operatorname{Pf}(\varnothing)=1,
\]

so it is the sewing unit. A two-point interval is the elementary even generator:

\[
Z(a_0,a_1)=e^{-t(a_1-a_0)}.
\]

Every ordered even amplitude factors into these adjacent generators:

\[
Z(a_0,\ldots,a_{2m-1})
=
\prod_{r=0}^{m-1}Z(a_{2r},a_{2r+1}).
\]

This is a strict monoidal law on the subcategory whose cuts preserve even parity.

## Boundary of the result

This does not yet prove arbitrary bordism functoriality. Odd cuts expose state lines rather than scalars, and their composition with neighboring even blocks requires an explicit even--odd module map. Noncontiguous sewing also need not inherit the ordered-chain factorization.

What is established is the strict associativity, unit, and generator law for all contiguous even sewings, plus the previously established contraction law for a pair of contiguous odd blocks.

## Verification

The exact-rational checker verifies 180 cuts in chain sizes four through twelve:

```text
python research/coherence/check_pfaffian_even_cut_sewing.py
```

Artifacts:

- `check_pfaffian_even_cut_sewing.py`
- `pfaffian-even-cut-sewing.v1.json`

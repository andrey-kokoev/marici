# Sourced embedding into the nonorthogonal full-Gram realization

## Question

Which current sourced sectors enter the finite full-Gram realization while preserving their declared structure?

## Claim boundary

This packet proves an exact embedding for the scalar enlarged Green fixture and identifies the first missing datum for the gauge quotient. It does not infer an analytic form on the gauge sequence from its algebraic exactness.

## Enlarged Green embedding

The sourced scalar fixture has cyclic block \(A=2\), auxiliary block \(D=1\), and cross block \(C=1/2\):

\[
G=\begin{pmatrix}2&1/2\\1/2&1\end{pmatrix}.
\]

Its leading principal determinants are \(2\) and \(7/4\), so it is a full-Gram object. The cyclic under-arrow is the principal-block inclusion and preserves \(A\) exactly. Eliminating the cyclic tag induces the auxiliary quotient form

\[
D-C^{\mathsf T}A^{-1}C=1-\frac18=\frac78.
\]

Eliminating the auxiliary tag instead induces the cyclic Schur form

\[
A-CD^{-1}C^{\mathsf T}=2-\frac14=\frac74.
\]

Thus the fixture embeds without orthogonalization, and both directional Schur certificates are retained.

## Gauge obstruction

The sourced gauge packet supplies the exact sequence

\[
0\longrightarrow\mathcal G\longrightarrow\mathcal A_P
\longrightarrow\mathcal A_P/\mathcal G\longrightarrow0
\]

and identifies its kernel. It explicitly supplies no canonical section. More fundamentally for this comparison, it supplies no positive Gram form on \(\mathcal A_P\), no quotient form, and no assertion that the quotient is a Schur complement.

Therefore the gauge sequence is a valid algebraic over-arrow but is not an object of the analytic full-Gram realization. Choosing an inner product or gauge fixing would insert unsourced structure.

## Disposition

The sourced enlarged Green fixture embeds fully. The gauge sequence does not fail algebraically; its comparison is undefined because the analytic Gram datum required by the target model is absent. This proves that one homogeneous full-Gram equipment cannot represent both sourced sectors without adding structure.

The next executable branch is a heterogeneous analytic/algebraic equipment: full-Gram objects and exact-sequence objects remain distinct, while mixed cells require an explicit form-compatible comparison map.

## Verification

- `research/voevodsky/checkers/check_sourced_full_gram_embedding.py`
- `research/voevodsky/results/sourced_full_gram_embedding.json`
- `research/voevodsky/gauge-quotient-over-extension-audit.md`

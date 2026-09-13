# Constructive finite boundary-Pfaffian chain

## Scope

`agda/BoundaryPfaffianFiniteChain.agda` constructs the first concrete algebraic instance behind the abstract rank-reset skeleton over an arbitrary commutative ring.

## Three-point residual

For adjacent chain weights \(x,y\), the skew matrix is represented rowwise by

\[
\begin{pmatrix}
0&x&xy\\
-x&0&y\\
-xy&-y&0
\end{pmatrix}.
\]

The module constructs its canonical cofactor residual

\[
v=(y,-xy,x)
\]

and proves all three kernel equations by commutative-ring normalization.

The `ThreeChainResidual` record retains:

- all three residual coordinates;
- their identification with the canonical cofactors;
- all three row-vanishing certificates.

## Localized three-point normal form

`SelectedGapUnit x` stores an explicit inverse and proof \(x^{-1}x=1\). Under exactly this hypothesis, the module constructs the determinant-one triangular replacement

\[
e_2' = e_2+x^{-1}y\,e_0-y\,e_1.
\]

Agda proves that \(e_2'\) pairs trivially with both \(e_0\) and \(e_1\), leaving the selected block \(H(x)\) and one zero line. This is a concrete localized hyperbolic normal-form witness.

No unit witness is used by the earlier cofactor kernel equations. The module therefore keeps ring-generic Pfaffian algebra and unit-dependent contractible minimalization formally separate.

The same construction is now proved for an arbitrary remote chain vector with suffix profile \(s\):

\[
e_s'=e_s+x^{-1}s\,e_0-s\,e_1.
\]

Agda proves that every such vector becomes orthogonal to the selected first pair. It also expands the pairing of two transformed remote vectors and proves that all correction terms cancel, leaving their original suffix pairing unchanged.

This is the size-independent elimination step needed for induction: one localized hyperbolic pair splits off, and the remaining chain form is preserved exactly.

## Four-point closure

For adjacent weights \(x,y,z\), the module defines the complete four-point Pfaffian expression

\[
xz-(xy)(yz)+(xyz)y
\]

and proves constructively that the two non-adjacent terms cancel:

\[
xz-(xy)(yz)+(xyz)y=xz.
\]

This is the rank-four adjacent-matching law over any commutative ring, without positivity, ordering, real analysis, or division assumptions.

## Concrete residual sewing

The cross-block column from the three-point block to a fourth singleton is

\[
(xyz,yz,z)^T.
\]

Pairing it with the residual gives

\[
(y,-xy,x)
\begin{pmatrix}xyz\\yz\\z\end{pmatrix}
=xz.
\]

`oddOddSewingIsFourAmplitude` proves this equality. `finiteRankResetTriangle` then proves that microscopic four-point Pfaffian closure and residual-to-singleton sewing produce the same certificate.

This is the first concrete commuting rank-reset diagram in Agda: an odd residual is sufficient to reconstruct the next even closure.

The module also contracts two independent three-point residuals across a separating gap. Starting from all nine microscopic cross-block terms, `twoOddResidualsGiveSixAmplitude` proves

\[
\operatorname{Sew}(u_{x,y},u_{u,v};g)=xgv,
\]

which is the six-point adjacent amplitude. Thus residual sufficiency survives a nontrivial odd-block/odd-block composition rather than only sewing to a singleton.

`sixChainPfaffian` independently encodes the complete 15-matching six-point Pfaffian through its five first-row minor groups. Agda normalizes that full polynomial to \(xgv\). `sixRankResetTriangle` then proves

\[
\operatorname{Pf}(M_6)
=
\operatorname{Sew}(u_{x,y},u_{u,v};g).
\]

This strengthens the earlier sewing calculation: the microscopic side is now the complete six-point Pfaffian, not only the cross-block contraction formula.

## Significance

The module separates the universal algebraic mechanism from the half-line selection theorem:

- multiplicative chain incidence forces Pfaffian cancellation algebraically;
- half-line order explains why the chain weights arise from metric gaps;
- no analytic premise is needed once the chain relations are supplied.

It is a genuine finite instance rather than a record containing the desired theorem as a field.

## Verification

Checked with Agda 2.8.0.1 and Cubical 0.9:

```text
agda --transliterate \
  -i research/voevodsky/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/voevodsky/agda/BoundaryPfaffianFiniteChain.agda
```

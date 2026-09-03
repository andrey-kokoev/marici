# Gauge quotient descent and displayed-univalence falsifier

## Question

What does the completed gauge quotient actually support before a displayed-univalence principle is introduced?

## Claim boundary

This packet tests an exact finite-dimensional model of the sourced gauge sequence. It establishes the quotient universal property and falsifies literal set-level displayed univalence. It does not rule out a univalent completion, Rezk completion, or higher quotient.

## Quotient model

Let

\[
E=\mathbb Q^3,
\qquad
G=\langle e_1\rangle,
\qquad
q(x_1,x_2,x_3)=(x_2,x_3).
\]

Then

\[
0\longrightarrow G\longrightarrow E
\overset q\longrightarrow\mathbb Q^2\longrightarrow0
\]

is exact.

## Descent theorem

A linear observable \(f:E\to W\) descends uniquely through \(q\) exactly when it annihilates \(G\).

For the tested observable

\[
f(x_1,x_2,x_3)=2x_2-x_3,
\]

the descended map is \(\bar f(y_1,y_2)=2y_1-y_2\), and \(f=\bar f q\).

The hostile observable

\[
f_{\rm bad}(x_1,x_2,x_3)=x_1+2x_2-x_3
\]

fails descent because representatives differing by \(e_1\) have different values.

This is the executable precursor to physical presentation independence.

## Displayed-univalence falsifier

There is a nonidentity automorphism over the fixed quotient:

\[
h(x_1,x_2,x_3)=(x_1+x_2,x_2,x_3),
\qquad qh=q.
\]

Thus the presentation \(q:E\to X\) has a nontrivial vertical automorphism. In an ordinary set-valued displayed category, literal equality of this presentation with itself has no corresponding distinct equality for every such automorphism. Therefore the map from equality to structured isomorphism is not surjective: naive displayed univalence fails.

The automorphism is gauge-valued shear. Quotient observables cannot detect it, which is precisely why it survives over \(X\).

## Required repair

A displayed-univalence claim needs one of:

- a univalent universe of quotient presentations;
- Rezk completion of the displayed category;
- a higher quotient identifying gauge-valued vertical automorphisms with paths;
- extra rigidifying data that kills all vertical automorphisms, with proof that the rigidification is source-authorized.

The exact sequence alone supplies none of these.

## Disposition

Gauge descent passes; literal displayed univalence fails. The operating architecture may use the quotient fibration and its universal property, but must label any univalence layer as an additional completion or axiom.

## Verification

- `research/voevodsky/checkers/check_gauge_quotient_descent_univalence.py`
- `research/voevodsky/results/gauge_quotient_descent_univalence.json`
- `research/voevodsky/gauge-quotient-over-extension-audit.md`

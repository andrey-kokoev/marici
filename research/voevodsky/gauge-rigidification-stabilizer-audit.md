# Gauge rigidification and vertical stabilizers

## Question

Which additional data eliminate the vertical automorphisms that falsify naive displayed univalence for quotient presentations?

## Claim boundary

This packet computes the automorphism stabilizer of a split finite-dimensional quotient. It identifies sufficient rigidifying data but does not authorize a physical gauge fixing for the completed radiative sector.

## General split model

Write a split extension as

\[
E=G\oplus X,
\qquad q(g,x)=x.
\]

Every linear automorphism over \(X\) has block form

\[
h(g,x)=(Ag+Lx,x),
\]

where \(A\in\operatorname{Aut}(G)\) and \(L\in\operatorname{Hom}(X,G)\). Hence the vertical automorphism group is

\[
\operatorname{Hom}(X,G)\rtimes\operatorname{Aut}(G).
\]

The shear from the previous falsifier is the \(L\)-component.

## Successive rigidifications

Choose the section

\[
s(x)=(0,x).
\]

Requiring \(hs=s\) forces \(L=0\), but leaves every kernel automorphism \(A\). A gauge section alone therefore does not make the displayed fiber rigid.

Also retain a pointwise kernel framing

\[
i:G\to E,
\qquad i(g)=(g,0),
\]

and require \(hi=i\). This forces \(A=1_G\). Preserving both \(s\) and \(i\) leaves only the identity vertical automorphism.

## Interpretation

The pair consisting of a section and kernel framing is sufficient to rigidify this split linear model. It converts the quotient presentation into a chosen decomposition, not merely a gauge-invariant observable object.

For the completed gauge sector, a section is gauge fixing and a pointwise kernel frame chooses coordinates on gauge redundancy. Neither follows from the quotient exact sequence. Adding them for categorical convenience would alter the structured object and may insert presentation data into the physical layer.

## Univalence consequence

Rigid fibers remove the exhibited automorphism obstruction, but rigidity is weaker than displayed univalence. One must still prove that isomorphic rigidified presentations are identified by the chosen equality notion. The calculation supplies a necessary automorphism test, not a universe-level identity theorem.

## Disposition

- quotient alone: stabilizer \(\operatorname{Hom}(X,G)\rtimes\operatorname{Aut}(G)\);
- section only: stabilizer \(\operatorname{Aut}(G)\);
- section plus pointwise kernel framing: trivial stabilizer.

The minimal tested rigidification is therefore section plus kernel framing. Promotion is blocked until a source explains why both choices are canonical or physically irrelevant after a separately defined higher quotient.

## Verification

- `research/voevodsky/checkers/check_gauge_rigidification_stabilizers.py`
- `research/voevodsky/results/gauge_rigidification_stabilizers.json`
- `research/voevodsky/gauge-quotient-descent-and-univalence-falsifier.md`

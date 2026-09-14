# The descent residual represents the induced homology map

## Question

What does the contraction-descent residual prove, and which stronger interpretations are invalid?

## Claim boundary

This is a chain-homotopy theorem. It gives a necessary obstruction to a nonzero Carrier-derived homology map. A nonzero residual as a chain-level matrix is not sufficient: it must represent a nonzero target homology class under a source-derived sector map.

## Theorem

Let \((C,d_C)\) admit a contraction

\[
d_Ch_C+h_Cd_C=1_C,
\]

and let \(F:C\to S\) be a chain map. For any degree-one candidate \(h_S\) on \(S\), define

\[
\mathcal O_F
=F-d_Sh_SF-h_SFd_C.
\]

For every cycle \(z\in C\),

\[
\mathcal O_F(z)=F(z)-d_Sh_SF(z).
\]

Therefore

\[
[\mathcal O_F(z)]=[F(z)]
\]

in \(H(S)\). The residual represents exactly the induced homology map \(F_*\).

If the contraction descends, meaning

\[
h_SF=Fh_C,
\]

then

\[
\mathcal O_F
=F-F(d_Ch_C+h_Cd_C)=0.
\]

Hence a nonzero Carrier-derived target class is impossible when the contraction descends.

## Necessary, not sufficient

The converse fails at chain level. Choosing an incorrect candidate such as \(h_S=0\) can make \(\mathcal O_F=F\neq0\) even when the target is acyclic and \(F_*=0\). Thus the admissible obstruction is not matrix nonvanishing but the homology class represented by the residual, together with the proof that \(F\) is a source-derived chain map.

## Risky consequences

1. Every contraction-preserving sector map induces the zero map on positive homology.
2. For any source cycle, the residual and its sector image define the same homology class.
3. A nonzero matrix residual with zero target homology is rejected as a bad homotopy choice, not promoted to sector content.
4. Skeletal truncation exposes classes because its graded projection is not a chain map; it is a diagnostic boundary case rather than a physical sector map.

## Exact audit

On the canonical six-cube attachment, reconstruct the integral contraction. Verify zero residual for the identity chain map with the descended contraction. Set the candidate target homotopy to zero and verify a nonzero residual while target homology remains zero. Recheck the skeletal projections as non-chain-map boundary cases.

## Computed audit

For the identity chain map with the transported six-cube contraction, the residual vanishes in every degree. With the deliberately wrong choice \(h_S=0\), residual ranks become the full chain dimensions

\[
(1,5,11,14,11,5,1),
\]

while every target Betti number remains zero. The skeletal boundary cases again have defect ranks \((1,4,7,7,4,1)\), exactly the omitted boundary ranks.

## Disposition

The theorem and its limits are verified exactly. A descended contraction forces zero induced homology. The residual represents the induced class on cycles, but raw residual nonvanishing is not sufficient evidence: a bad homotopy choice can make it maximal on an acyclic target. Physical verification still requires the first missing typed object, a source-derived physical sector chain map with declared target differential and readout authority.

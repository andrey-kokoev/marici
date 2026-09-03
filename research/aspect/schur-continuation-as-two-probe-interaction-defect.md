# Schur continuation as a two-probe interaction defect

## Question

Does an existing Interaction Net formula instantiate the probe-configuration semantics with a nonzero joint defect that is absent from both unary placements?

## Claim boundary

This packet instantiates the semantics on the Schur reduction already derived in `schur-first-jet-as-interaction-net.md`. It proves an exact scalar and additive-categorical witness. It does not establish that SCC currently stores this semantics, nor that all matrix-valued SCC cells admit the required inverses or source maps.

## Source formula

The existing Interaction Net has retained response \(A\), new-cell response \(E\), and typed incidence wires \(B,C\). Eliminating the retained block gives

\[
S=E-CA^{-1}B.
\]

Treat the entry and exit incidence placements as probes \(P_B\) and \(P_C\). In an additive constraint category define the effective response assignment

\[
F(\varnothing)=E,
\qquad
F(P_B)=E,
\qquad
F(P_C)=E,
\qquad
F(P_B,P_C)=E-CA^{-1}B.
\]

The binary Möbius cross-effect is

\[
\operatorname{cr}_{B,C}F
=F(P_B,P_C)-F(P_B)-F(P_C)+F(\varnothing)
=-CA^{-1}B.
\]

Thus neither incidence placement alone changes the effective cell. Their joint placement closes a continuation route through the retained net and produces exactly the Schur residue. This is the additive analogue of the finite-set Segal defect: factorization predicts \(F(P_B,P_C)=E\), while the actual joint object differs by the cross-effect.

## Exact witness

Choose rational scalar data

\[
A=2,
\quad B=3,
\quad C=4,
\quad E=5.
\]

Then the unary responses are both \(5\), while

\[
S=5-4\cdot 2^{-1}\cdot 3=-1,
\qquad
\operatorname{cr}_{B,C}F=-6.
\]

Erasing either incidence wire makes the residue vanish. Erasing the retained response makes the expression undefined rather than zero because \(A^{-1}\) is no longer typed.

## First-jet refinement

For a deformation coordinate \(u\), with no temporal interpretation, differentiation gives

\[
S'=E'-C'A^{-1}B+CA^{-1}A'A^{-1}B-CA^{-1}B'.
\]

The four terms distinguish internal-cell, exit-incidence, retained-response, and entry-incidence contributions. With

\[
A'=1/2,
\quad B'=0,
\quad C'=2,
\quad E'=0,
\]

one obtains \(S'=-3/2\), although the local shadow \(E'\) is zero. Joint placement therefore carries first-order constraint information absent from the local new-cell probe.

## Proof-representation correspondence

| Net construction | Mathematical witness |
|---|---|
| both incidence wires connected through retained cell | composite \(CA^{-1}B\) |
| local elimination rewrite | Schur identity \(S=E-CA^{-1}B\) |
| erase either incidence wire | cross-effect becomes zero |
| erase retained cell while preserving the route | ill-typed inverse/composite |
| differentiated redexes | four-term derivative identity |
| terminal current | requires a separately typed trace and invertible \(S\) |

This gives a concrete proof-bearing net fragment: the rewrite is warranted by the Schur identity, while the cross-effect detects the semantic information lost by replacing the joint fragment with the unary shadow \(E\).

## Falsifiers

1. If \(B=0\) or \(C=0\), the proposed two-probe interaction must vanish.
2. If \(A\) is noninvertible, the Schur interaction is undefined; assigning it zero is rejected.
3. A claimed local first-jet explanation is rejected when \(E'=0\) but \(S'\ne0\).
4. A net rewrite is rejected if its recorded effective response differs from direct block elimination.
5. This construction does not prove SCC-wide soundness: another cell without a source formula remains unmatched.

## Disposition

The Schur Interaction Net is an inhabited instance of the probe-configuration proposal in an additive constraint category. The joint residue is exactly the binary cross-effect. This advances the proposal from a synthetic finite example to one existing mathematical Interaction Net fragment. SCC representation remains a separate implementation and audit gate.

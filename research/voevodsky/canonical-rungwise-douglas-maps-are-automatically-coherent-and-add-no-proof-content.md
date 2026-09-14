# Canonical rungwise Douglas maps are automatically coherent and add no proof content

## Question

Does requiring compatible contractions across the forward Gaussian rungs strengthen separate finite Gram positivity enough to provide a construction mechanism?

Let

\[
M_1\subset M_2\subset\cdots
\]

and let `A_S,A_B` be fixed linear feature maps on their union. At stage `N`, define the canonical comparison on the feature range by

\[
C_N(A_Sf)=A_Bf,
\qquad f\in M_N.
\]

## Well-definedness is already a positivity consequence

If

\[
\|A_Bf\|^2\le\|A_Sf\|^2
\qquad(f\in M_N),
\]

then `A_Sf=0` implies `A_Bf=0`. Hence `C_N` is well-defined. The same inequality immediately gives

\[
\|C_N\|\le1.
\]

Thus stagewise positivity constructs the stagewise contraction without any additional choice.

## Coherence is automatic

For `f in M_N subset M_{N+1}`,

\[
C_{N+1}(A_Sf)=A_Bf=C_N(A_Sf).
\]

Therefore

\[
\boxed{
C_{N+1}|_{A_S(M_N)}=C_N.
}
\]

No Cholesky gauge or unitary alignment problem occurs for the canonical Douglas map. Such problems arise only if one factors each positive Gram matrix through unrelated auxiliary coordinates. Once both sides use the fixed feature maps `A_S` and `A_B`, compatibility follows from their definitions.

## Direct-limit contraction

If every finite stage is positive, define

\[
C_\infty(A_Sf)=A_Bf,
\qquad f\in\bigcup_NM_N.
\]

The stagewise inequalities imply

\[
\|C_\infty v\|\le\|v\|
\]

on its domain. It therefore extends uniquely to a contraction on the closure of `A_S(M_infinity)`. Hence

\[
\boxed{
\text{positivity at every finite rung}
\Longrightarrow
\text{one coherent direct-limit Douglas contraction}.
}
\]

Conversely, restricting a global contraction proves every finite inequality. These are equivalent statements.

## Consequence

The proposed coherence upgrade does not add proof content:

\[
\boxed{
\{G_{S,N}-G_{B,N}\succeq0\text{ for all }N\}
\iff
\{C_N\text{ coherent contractions for all }N\}.
}
\]

Forward compatibility is valuable for rejecting arbitrary independent Gram factorizations, but it cannot prove cone admission when the feature maps are already global and fixed.

## Where genuine extra structure could enter

A non-tautological construction must define a contraction on an ambient source carrier **before** the Weil/Blaschke feature maps are compared. Specifically, one needs

\[
C_{src}:\mathcal H_{src}\to\mathcal H_{src}
\]

with `||C_src||<=1` proved from an independent operation, together with intertwining maps satisfying

\[
A_B=J_BC_{src}A_{src},
\qquad
A_S=J_SA_{src},
\]

and a source identity comparing `J_B` and `J_S`. The norm bound must come from, for example, conditional expectation, orthogonal projection, a Markov transfer, or an isometric correspondence.

Defining `C_src` only by the requirement `A_B=C_src A_S` returns to the canonical map above and is equivalent to positivity.

## Source-only recovery of the defect is a separate issue

The Blaschke factor `B` was introduced through the forbidden divisor. In principle it can be recovered from the boundary symbol `Theta` by canonical Wiener--Hopf/inner--outer factorization when the required bounded-type hypotheses hold. That would make the negative feature space intrinsic to the source boundary function rather than dependent on a listed zero set.

But canonical recovery of `B` does not supply domination. It merely computes `A_B`. The inequality

\[
A_B^*A_B\preceq A_S^*A_S
\]

remains exactly the target.

Accordingly there are two independent tasks:

1. derive the Krein--Langer factors from the completed source without zero enumeration;
2. construct an independently contractive operation dominating the recovered negative factor.

Only the second could prove positivity.

## Disposition

The coherent-rung formulation is an exact organizational restatement, not a new mechanism. Canonical Douglas maps are automatically coherent whenever the finite inequalities hold. The search must return to an ambient source operation with a pre-existing contraction theorem; no manipulation of finite feature maps can manufacture the needed norm bound.

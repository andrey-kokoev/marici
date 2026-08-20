# 1090 — The First Rank-Twelve Exceptional Center Forces a Joint Rees Lattice

## Record

Entry 1089 showed that direct specialization of the generic rank-twelve
source torsor fails at ((u,v)=(0,2)).  Expanding the frozen source geometry at
that center now determines the missing Rees object without fitting.

Sequence claim: `seqclaim-2d92ad0f703708ebf5c887ad`.

## Frozen local coordinates

Set

\[
p=u,\qquad q=v-2,\qquad A=a,\qquad B=b+1.
\]

The marked walls become exactly

\[
L_1=B-p,
\qquad
L_2=A+\frac{q-p}{2}.
\]

At the center,

\[
K|_{p=q=0}=A^4,
\qquad
L_1|_{p=q=0}=B,
\qquad
L_2|_{p=q=0}=A.
\]

Thus this is a simultaneous parameter--fiber collision, not a degeneration
that can be resolved by blowing up the base ideal ((p,q)) alone.

## Source-derived Newton orders

Exact Symbolica expansion gives the joint ideal

\[
J=(p,q,A,B)
\]

and orders

\[
\boxed{
\nu_J(K)=4,\qquad
\nu_J(K_1)=3,\qquad
\nu_J(L_1)=\nu_J(L_2)=1.
}
\]

The quartic initial form of (K) is nonzero and does not factor over the
rational conventions used by the checker.  The cubic initial form of the
double-pole numerator is

\[
\operatorname{in}_J(K_1)
=
-p\left(
-6pq-4pB+4qB+5p^2+q^2-4A^2
\right).
\]

Hence (K_1), but not the branch quartic itself, has a distinguished
(p=0) component on the exceptional divisor.

## The twelve source-form shifts

For a relative form

\[
\frac{n\,dA\wedge dB}
{L_1^{s_1}L_2^{s_2}K^{h/2}},
\]

the joint exceptional order is

\[
\nu_J(n)+2-s_1-s_2-2h.
\]

In the fixed source ordering

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9),
\]

the orders are

\[
\boxed{
(-2,-1,-1,2,1,0,1,0,-1,0,2,2).
}
\]

The generic basis is therefore not a lattice at this center.  Its direct
specialization necessarily loses primitive-independent coordinates, exactly
as observed in Entry 1089.

## Deutsch--Popperian verdict

The base-only repair

\[
\operatorname{Bl}_{(p,q)}
\]

is falsified by the frozen source expansion.  The minimal homogeneous repair
is the ordinary joint Rees blowup

\[
\boxed{
\operatorname{Bl}_{(p,q,A,B)}
}
\]

together with the twelve nonuniform source-form shifts above.

This introduces no new incidence equation: (A=0), (B=0), (p=0), and
(q=0) are the already labelled marked-wall and exceptional-center normals.
The new datum is a coefficient lattice on their existing joint resolution.

## Classification

- carrier: existing signed-energy/marked-wall intersection;
- required geometry: joint parameter--fiber blowup;
- coefficient datum: nonuniform twelve-class Rees lattice;
- distinguished supported component: (p=0) in the double-pole numerator;
- new carrier stratum: none.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u0v2_newton.rs`;
- `research/benincasa/rank12-u0-v2-joint-rees.json`;
- exact source formulas from the rank-twelve four-stratum reducer;
- exact Symbolica expansion and nonzero initial-form assertions.

Epistemic graph admission:
`ev-000000000785-5fb99c83-7acd-45ba-beae-cc7b5f461bb1`.

## Next falsifier

Normalize every master and exact primitive by its derived (J)-order on the
four affine charts of the joint blowup.  Recompute the saturated exceptional
quotient and its connection.  If the normalized charts fail to glue to a
finite logarithmic rank-twelve object, the existing marked-wall carrier is
insufficient at this center.  If they glue, Entry 1089's rank loss is fully
explained as degeneration of the generic coefficient lattice.

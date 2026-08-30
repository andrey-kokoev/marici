# The rational-Weyl-fixed theta state is not cyclic

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact correction to the cyclic-stabilization proposal

## Adelic stabilization is real

Let the adelic theta comb be the distribution

\[
\Delta_{\mathbb Q}=\sum_{r\in\mathbb Q}\delta_r.
\]

Translation by a rational number permutes its summands. Modulation by a
rational number acts trivially on every rational support point because the
global additive character is trivial on \(\mathbb Q\). Thus the rational
phase lattice fixes the comb under both Weyl directions.

This supplies the stabilization equation sought in the preceding packet,
but it destroys cyclicity for the same algebra.

## Exact incompatibility

Let \(M\) be a unital operator algebra and suppose

\[
A\Omega=\Omega
\]

for every generator \(A\) of \(M\). Then every algebra word also fixes
\(\Omega\), and

\[
\overline{M\Omega}=\mathbb C\Omega.
\]

If the representation space has dimension greater than one, \(\Omega\) is
not cyclic. The conclusion is unchanged in a rigged representation: the
algebraic orbit is still one-dimensional even when \(\Omega\) is
distributional.

## Consequence

The phase-rigidity theorem from cyclic stabilization cannot be applied with
the same rational Weyl algebra supplying both words. The completed theta comb
is a fixed boundary state, not a cyclic full-support state for that action.

This does not erase the positive insight. It retypes it:

- the rational lattice supplies a stabilizer algebra;
- a noncommuting transverse comparison algebra must supply cyclic generation; and
- phase rigidity, if it survives, must come from their joint action or a
  standard-form separating property.

The missing channel is therefore genuinely a second algebraic action, not
another scalar observable inside the first maximal abelian algebra.

## Stronger candidate

The full adelic Weyl representation contains two complementary roles. The
rational subgroup fixes the theta distribution, while operators transverse
to that subgroup move it through nontrivial states. Because the rational
boundary algebra is intended to be maximal abelian, its commutant is itself.
No second commuting algebra can restore cyclicity. The transverse action must
be a genuinely noncommuting complementary Weyl polarization.

The correct target is a pair

\[
(M_{\mathrm{stab}},N_{\mathrm{trans}})
\]

such that \(\Delta_{\mathbb Q}\) is fixed by \(M_{\mathrm{stab}}\) and cyclic
for the noncommutative algebra generated jointly with
\(N_{\mathrm{trans}}\).

Any boundary phase must then be selected by a compatibility condition between
the two actions. Neither action can do both jobs alone.

## Cheapest falsifier

Construct the smallest completed source module, verify that the rational
stabilizer is maximal abelian, and derive its conjugate Weyl polarization.
If their joint orbit of the theta comb is not dense, distinct phase selectors
will remain invisible. If it is dense, test whether the Heisenberg
commutation law uniquely determines the boundary relation.

## Scope

Rational Weyl invariance and the fixed-vector noncyclicity theorem are exact.
The existence of a canonical transverse algebra with the needed separating
property remains conjectural.

## Verification

The checker represents a nontrivial boundary algebra with a common fixed
vector, verifies that its algebra orbit has rank one, and shows that a
noncommuting cyclic shift generates the full module.

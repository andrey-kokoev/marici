# Local polynomial CP portal (WP378)

## Locality obstruction

On the nondegenerate flavor stratum, define the real CP-odd commutator
invariant \(C\) by

\[
C=-i\det[H_u,H_d]=2J\Delta_u\Delta_d.
\]

The WP360--WP377 portal uses normalized \(J^2\):

\[
J^2=\frac{C^2}{4\Delta_u^2\Delta_d^2}.
\]

It is weak-basis invariant but rational in polynomial flavor invariants and is
undefined when either spectral discriminant vanishes. Consequently
\((J^2-\alpha\rho)^2\), with \(\rho=Q/M^2\), is not a globally polynomial
local flavor potential.

## Denominator-cleared completion

The exact polynomial completion of the shell is

\[
F=C^2-4\alpha\rho\Delta_u^2\Delta_d^2.
\]

On \(\Delta_u\Delta_d\ne0\),

\[
F=0
\quad\Longleftrightarrow\quad
J^2=\alpha\rho.
\]

Every factor is a full weak-basis invariant, so a positive potential
\(V_F=\lambda F^2\) descends without a texture chart or reference port.

## Degenerate hostile stratum

If \(\Delta_u=0\), the Jarlskog identity forces \(C=0\). Then

\[
F=0
\]

for every \(\rho\), and

\[
\frac{\partial F}{\partial\rho}
=-4\alpha\Delta_u^2\Delta_d^2=0.
\]

The polynomial completion is regular there but loses selector authority. Two
source values \(\rho_1\ne\rho_2\) become indistinguishable on the same
degenerate flavor packet. This is the exact first nonfaithful boundary of the
denominator-cleared portal.

## Operator-degree gate

Treating \(H_u,H_d\) as degree-one Gram variables, both \(C^2\) and
\(\Delta_u^2\Delta_d^2\) have degree twelve. Hence \(F^2\) has Gram degree
twenty-four. With \(H_a=\Phi_a\Phi_a^\dagger\), this is field degree
forty-eight. The direct positive-square portal is therefore an extremely
high-degree EFT operator, not a renormalizable microscopic action.

Clearing denominators repairs polynomial locality only on the algebraic
level. It does not derive the relative coefficient \(\alpha\), a stabilizing
completion, or a mediator grammar capable of generating the operator.

## Disposition

WP378 supplies a full weak-basis-descending polynomial shell selector on the
nondegenerate stratum. It also strengthens the negative WP377 disposition:
the normalized portal cannot simply be promoted to a fundamental local
potential, and its polynomial replacement becomes blind at spectral
degeneracy and is far above renormalizable field degree.

The smallest exact falsifier is \(\Delta_u=C=0\), where all \(\rho\) satisfy
the polynomial constraint. The remaining constructive gate is a microscopic
mediator completion deriving \(F\), its sign and normalization, with source
support bounded away from degeneracy and without fitting \(\alpha\).

Run `uv run --with sympy python
research/flavor/checkers/wp378_local_polynomial_cp_portal.py` to regenerate the
exact result.

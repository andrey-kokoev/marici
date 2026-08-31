# The oriented ratio cocycle is the unique zero-initial solution of a first-order Stokes equation

## Question

Does the finite ratio-segment correction have an intrinsic differential
characterization compatible with an ordered Stokes construction?

## Claim boundary

Yes. After restoring the ratio character, the correction is the unique
zero-initial solution of a first-order equation whose forcing is the localized
correlation kernel. This makes the proposed linking comparison precise. It
does not prove that the current wall/incidence linking port carries this
solution.

## Oriented cocycle

For one shell object \([A,B]\), define

\[
 J(z;d)=\int_0^d e^{-zw}K_{[A,B]}(w)\,dw.
\]

Restore the ratio character by setting

\[
 C(z;d)=e^{zd}J(z;d).
\]

Then

\[
 C(z;0)=0.
\]

## First-order equation

Differentiation in the ratio coordinate gives

\[
 \partial_dC(z;d)
 =zC(z;d)+K_{[A,B]}(d).
\]

Therefore

\[
 (\partial_d-z)C(z;d)=K_{[A,B]}(d),
 \qquad
 C(z;0)=0.
\]

The coordinate \(d\) is logarithmic ratio separation, not physical time.

The zero-initial condition selects the unique solution

\[
 C(z;d)
 =\int_0^d e^{z(d-w)}K_{[A,B]}(w)\,dw.
\]

## Composition law

For oriented increments \(d_1,d_2\),

\[
 C(z;d_1+d_2)
 =e^{zd_2}C(z;d_1)
 +\int_0^{d_2}
 e^{z(d_2-q)}K_{[A,B]}(q+d_1)\,dq.
\]

Thus composition is a semidirect cocycle: the second segment uses the
translated correlation forcing. Plain scalar additivity is insufficient once
the ratio character is restored.

## Ordered reversal

For negative \(d\), the oriented integral gives the same unique solution. Pair
swap reverses \(d\) and transports the shell fibre. Consequently the reciprocal
comparison must intertwine this equation with the base reflection identity

\[
 K_{[A,B]}(-d)=K_{[A-d,B-d]}(d).
\]

## Comparison with the existing Stokes port

The retained ordered Stokes construction supplies:

- a continuous wall trace;
- an incidence scalar;
- an antisymmetric linking polarization;
- reciprocal sign reversal.

To realize the ratio cocycle, its incidence coordinate must be enlarged or
identified so that the pullback linking section obeys

\[
 (\partial_d-z)C=K
\]

with \(C(0)=0\) on every ordered label pair and shell.

Boundedness of the scalar polarization does not establish this differential
identity.

## Minimal comparison square

Let \(\mathcal G_{\rm ratio}\) be the graph of \(\partial_d-z\) with retained
value at \(d=0\). A candidate comparison must provide

\[
 \mathcal T_{\rm ratio\to link}:
 \mathcal G_{\rm ratio}\longrightarrow
 \mathcal G_{\rm wall,inc}
\]

such that:

1. the forcing coordinate maps from \(K_{[A,B]}\);
2. the zero-initial value maps to the diagonal-label wall condition;
3. ratio reversal maps to reciprocal slot reversal;
4. shell transport commutes with the comparison;
5. the analytic-transpose Laplace sign is preserved.

## Hostile

A linking proposal that has the correct odd sign but satisfies

\[
 (\partial_d-z)C-K\ne0
\]

at one generic pair and shell fails the source comparison before any Xi zero
is inspected.

## Disposition

The finite ratio correction is now characterized as a source-forced Stokes
resolvent in ratio space. Candidate one requires a typed map from this graph to
the G4 linking graph. That map is not present in the current declaration. No RH
conclusion is authorized.

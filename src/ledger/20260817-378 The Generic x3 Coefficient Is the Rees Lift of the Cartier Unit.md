# The Generic x3 Coefficient Is the Rees Lift of the Cartier Unit

## Result

The apparent conflict between the generic one-road incidence calculation and
the closed Cartier unit is resolved by the \(x_3\)-Rees filtration.

The generic unlocalized chain equation does not admit coefficient \(1\).
Its primitive solution is

\[
\boxed{
k=x_3,\qquad a=-\frac{X_{D03}}{u_{D03}}.
}
\]

This solution does not kill the generic \(Q\)-leg: multiplication by \(x_3\)
is nonzero over the established polynomial coefficient domain.  At the first
conormal associated grade, however,

\[
\operatorname{gr}_{x_3}^{1}(x_3)=
[x_3]\in (x_3)/(x_3^2),
\]

and positive Cartier coorientation evaluates \([x_3]\) to \(+1\).  That is
exactly the unit selected independently by Entries 131, 176, and 377.

Thus the generic coefficient \(x_3\) and the closed coefficient \(1\) are not
competing answers.  They are the pre-Cartier and Cartier grades of one strict
filtered coefficient map.

## Generic chain equation

On the source one-road shadow, the actual loaded relation has the common
spectator factor

\[
dH_{\rm Morse}=q_J-x_3\widetilde\xi.
\]

On the target extended-Cech shadow, the \(D03\) normal differential has
coefficient \(X_{D03}/u_{D03}\).  A chain map with generic coefficient \(k\)
on \(q_J\) and lower coefficient \(a\) must satisfy

\[
x_3a+\frac{X_{D03}}{u_{D03}}k=0.
\]

The checked monomial divisibility calculation gives the smallest integral
solution

\[
a=-\frac{X_{D03}}{u_{D03}},
\qquad
k=x_3.
\]

No \(x_3\), monodromy parameter, or integer is inverted.  The factor
\(u_{D03}^{-1}\) is legal because it occurs on the already constructed
target extended-Cech side, not in the scalar source ring.

## The generic leg remains nonzero

The acceptance condition from Entries 131, 143, and 160 is a nonzero generic
\(Q\)-leg, not a unit coefficient before Cartier specialization.  Since the
coefficient ring is a domain and \(x_3\neq0\),

\[
x_3[q_{03}^{Q}]\neq0
\]

whenever the retained \(Q\)-generator is \(x_3\)-torsion-free.  The
Entry-143 finite \(Q\) carrier is free and saturated over the incidence
coefficient lattice, so its one-road generator has this property.

Consequently the generic map with \(k=x_3\) passes the nonvanishing test.  A
generic coefficient \(1\) was an unnecessarily strong and incompatible
requirement.

## Closed conormal grade

Filter the target top line one step more deeply than its lower tag line:

\[
F_T^p(\text{top})=x_3^{p+1}R\langle q_{03}^{Q}\rangle,
\qquad
F_T^p(\text{lower})=x_3^pT_{03}.
\]

This order shift is not fitted solely for the generic equation.  Its local
finite model is Entry 131's actual packet

\[
P_3=
[A\langle g_3,h_3\rangle
\xrightarrow{(x_3,u_3)}
A\langle p_3\rangle],
\]

whose radial differential already has filtration order one in \(x_3\).

The first Rees symbol of the generic coefficient is

\[
[x_3]\otimes q_{03}^{Q}.
\]

The oriented Cartier evaluation

\[
(x_3)/(x_3^2)\otimes\operatorname{or}(x_3)\longrightarrow A/(x_3)
\]

sends \([x_3]\) to \(+1\).  Entry 377 then identifies the resulting closed
map with

\[
\operatorname{cap}_{\rm norm}\otimes
\operatorname{pur}_{x_3,\partial}^{\rm PC}.
\]

## One-road coefficient-level Beck--Chevalley result

At the coefficient/incidence level, the generic and closed arrows now form
one strict filtered map:

\[
\begin{array}{ccc}
q_J &\longmapsto& x_3q_{03}^{Q}\\
\downarrow\operatorname{gr}_{x_3}^{1}
&&\downarrow\operatorname{gr}_{x_3}^{1}\\
-\widetilde\xi&\longmapsto&
\operatorname{cap}_{176}^{\rm PC}.
\end{array}
\]

The chain equation supplies the compatibility before specialization, and
the conormal evaluation supplies the positive closed unit.  Therefore the
one-road Beck--Chevalley obstruction vanishes on this coefficient/incidence
shadow.

This is stronger than separately knowing a nonzero generic map and a local
unit: it identifies them as two filtered grades of the same forced
coefficient solution.

## Remaining typing boundary

The result does not yet construct the full primal trace

\[
\mathcal S_{\rm sh}^{\rm norm,reg}
\otimes^L
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\longrightarrow\mathbf1_{\chi_N}.
\]

In particular, the following remain:

1. derive the filtered top/lower placement simultaneously from the complete
   normalization-sheet graph DNC, not only its one-road coefficient shadow;
2. lift the marked gallery-to-tag incidence correspondence through all
   lower Cech terms;
3. construct the actual homotopy in the common mixed-variance mapping
   complex;
4. attach both endpoints;
5. assemble the \(D_3\) orbit and reflection square.

Thus the coefficient-level obstruction is closed, while the full geometric
carrier and primal-trace construction remain open.

## Evidence boundary

\`research/voevodsky/check_d03_rees_generic_closed_bridge.rs\` verifies the
monomial chain equation, generic nonvanishing, conormal order one, and
positive leading coefficient.  The inputs are the exact generic incidence
equation already checked by
\`check_d03_generic_incidence_pairing_obstruction.rs\`, Entry 131's finite
Cartier packet, and Entry 377's unit lift.  No full normalization-sheet
correspondence or endpoint-pointed trace is claimed.

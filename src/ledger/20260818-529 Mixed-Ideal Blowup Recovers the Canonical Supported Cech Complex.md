---
authors:
  - marici.Nima
date: 2026-08-18
---
# Mixed-Ideal Blowup Recovers the Canonical Supported Cech Complex

## Scope

Work in the regular local model

\[
A=R[x,u],\qquad I=(x,u),\qquad
\pi:Y=\operatorname{Bl}_I\operatorname{Spec}A\longrightarrow\operatorname{Spec}A.
\]

This is the local model for the (D03) mixed occurrence/normal pair.  The
claim concerns only exceptional-support pushforward.  It does not identify
an exceptional generator with an Entry-143 physical cell.

## Two charts

The blowup is covered by

\[
U_x=\operatorname{Spec}R[x,t],\qquad u=xt,
\]

and

\[
U_u=\operatorname{Spec}R[s,u],\qquad x=su.
\]

On the overlap (s=t^{-1}).  The exceptional divisor is (x=0) on
(U_x) and (u=0) on (U_u).  Its complement is canonically the inverse
image of

\[
D(x)\cup D(u)=\operatorname{Spec}A\setminus V(I).
\]

Thus no global inversion of (x) or (u) occurs; each inversion belongs to
its own Čech chart.

## Exceptional-support pushforward

Let (j:Y\setminus E\hookrightarrow Y).  By definition,

\[
R\Gamma_E(\mathcal O_Y)
=
\operatorname{fib}
\left(
\mathcal O_Y\longrightarrow Rj_*\mathcal O_{Y\setminus E}
\right).
\]

The blowup of a regular two-generated ideal satisfies

\[
R\pi_*\mathcal O_Y\simeq A,
\]

and (pi) is an isomorphism away from (V(I)).  Applying (R\pi_*) to
the localization triangle gives the canonical equivalence

\[
\boxed{
R\pi_*R\Gamma_E(\mathcal O_Y)
\simeq
R\Gamma_I(A).
}
\]

Using the two affine charts, the right-hand side is represented by the
unaugmented Čech complex

\[
\boxed{
A\longrightarrow A_x\oplus A_u\longrightarrow A_{xu},
}
\]

with differentials

\[
a\longmapsto(a,a),
\qquad
(b,c)\longmapsto b-c
\]

up to one global orientation reversal.  The overlap transition (s=t^{-1})
is precisely the tautological-line transition; it is not a free global
Koszul generator.

## Consequence for the local Beck--Chevalley problem

The mixed-ideal blowup therefore supplies a canonical supported source for
the one-road comparison.  Any proposed local physical map must factor as

\[
R\Gamma_I(A)
\xleftarrow{\sim}
R\pi_*R\Gamma_E(\mathcal O_Y)
\longrightarrow
E_{03}^{\rm phys}.
\]

The first arrow is now geometric and canonical.  The second arrow remains
unconstructed.  In particular, the equivalence does not by itself provide
a nullhomotopy of

\[
\operatorname{ob}_{03}(k,b)
=
k[1](\kappa_A\otimes1)
-b[1](1\otimes\kappa_E).
\]

It only fixes the source, the chart transition, and the allowed homotopy
class in which such a cell must live.

## Negative controls

The construction does not permit:

- replacing the tautological transition by a global scalar cell;
- inverting (x) or (u) globally;
- deleting the overlap term (A_{xu});
- identifying the exceptional divisor with a pre-existing (Q) generator;
- inferring a physical pairing from the abstract localization triangle.

## Corrected frontier

Construct the variance-correct map

\[
R\pi_*R\Gamma_E(\mathcal O_Y)
\longrightarrow E_{03}^{\rm phys}
\]

from the literal occurrence-line radial maps and endpoint corestrictions.
Then test its compatibility with the two localization triangles.  Rotation
can be applied only after this one-road map and its Beck--Chevalley mate are
derived.

## Evidence

- Entry 160: universal one-road obstruction;
- Entry 163: mixed-ideal blowup provenance boundary;
- Entry 177: generic incidence-pairing no-go;
- standard two-chart Rees presentation
  (\operatorname{Rees}_A(I)=A[G,H]/(uG-xH)).

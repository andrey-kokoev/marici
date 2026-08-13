# Three Derived Normal Sectors

## Purpose

This entry records the inherited NLSM, Yang–Mills, and gravity constructions in one place while
keeping their extraction mechanisms distinct. It also marks which parts are working structure,
which parts are conjectural classification claims, and which parts remain open.

## NLSM: associated grade at a rank jump

The NLSM branch is organized by

\[
\mathrm{NLSM}
\sim
\operatorname{gr}_R(\mathrm{Scalar}),
\]

where \(R\) is a distinguished rank-jump stratum. The inherited geometric interpretation is that
a scalar kinetic operator degenerates and exposes a light sector. At a two-eigenvalue rank jump,
homotopy transfer is claimed to give a Grassmannian Goldstone theory.

A mixed Kähler/Jordan polarization then strictifies the usual infinite two-derivative interaction
tower to

\[
\mathcal L
=
\langle\partial\psi^+,\partial\psi^-\rangle
+
\left\langle
\partial\psi^+,
Q_{\psi^-}(\partial\psi^+)
\right\rangle.
\]

For a rectangular-matrix Jordan pair,

\[
Q_p(x)=pxp,
\]

and the inherited color-ordered quartic rule is

\[
V_4(+,-,+,-)=-2k_1\!\cdot k_3.
\]

The proposed classification

> same-spectrum, bi-polar, homogeneous Kähler quartic strictifiability is equivalent to
> Jordan-pair or 3-graded geometry

remains conjectural. Its claimed obstruction is the Jordan defect: a generic quartic tensor does
not close under the complementary nonlinear symmetry, while the Jordan identity supplies the
closure condition. This classification needs a precise category of admissible polarizations and
equivalences before it can be proved or falsified globally.

Entry 16 sharpens the typing. QTDS gives a uniform quartic presentation only after a cyclic order,
its alternating polarity lift, and a Jordan realization are retained. Permutation symmetry
obstructs a bare-class operation that chooses one such presentation from
\(\mathsf J=[(\operatorname{Pf}'A)^2]\). The surviving target is a Jordan-colored cyclic
resolution over the full alternating-order cover.

## Yang–Mills: first jet followed by gauge descent

The Yang–Mills branch is organized by

\[
\mathrm{YM}
=
H_{\rm gauge}\!\left(J_F^1\mathrm{Scalar}\right),
\]

where \(F\) is a fusion stratum. The first normal jet contains the prospective polarization data
but also gauge redundancy. Physical Yang–Mills is therefore assigned to the cohomological descent,
not to the raw jet.

This mechanism is structurally different from the NLSM rank-jump associated grade. It rejects the
earlier universal-mechanism hypothesis that every daughter theory should arise from the same kind
of rank degeneration. The retained principle is weaker and more useful: different theories may
occupy different normal layers and require different physical quotients.

The identification of the physical first-jet half-object with the CHY class of
\(\operatorname{Pf}'\Psi\) is inherited working structure and must eventually be tied to explicit
normal-coordinate and gauge-complex definitions.

## Gravity: primitive symmetric retract of the doubled first jet

Let \(V\) be the physical Yang–Mills first-jet fiber and let

\[
W=V\otimes V.
\]

The scalar-derived transverse metric is claimed to provide a swap \(\tau\), evaluation, and
coevaluation. If \(d=\dim V\), these define

\[
P_B=\frac12(1-\tau),
\]

\[
P_\phi=\frac1d\operatorname{coev}\circ\operatorname{ev},
\]

and

\[
P_E
=
\frac12(1+\tau)
-
\frac1d\operatorname{coev}\circ\operatorname{ev}.
\]

Thus

\[
\operatorname{im}P_E=\operatorname{Sym}_0^2V
\]

is the pure-graviton state space. The tree-level proposal is

\[
\mathrm{GR}_{\rm tree}
=
\operatorname{PrimSym}_g^2\!\left(J^1\mathrm{Scalar}\right)
\quad\text{paired by}\quad
I_{\rm scalar}^{-1}.
\]

The primitive-symmetric operation is intended to be intrinsic to the scalar-derived metric rather
than borrowed from an Einstein–Maxwell–scalar parent. Such a parent may realize the construction
without defining it.

## Sewing order and the quantum distinction

The retained quantum ordering is

\[
W
\xrightarrow{P_E}
G
\xrightarrow{\operatorname{Mod}}
\mathrm{GR}_{\rm quantum},
\]

not

\[
W
\xrightarrow{\operatorname{Mod}}
\mathrm{NSNS}_{\rm quantum}
\xrightarrow{\text{external }P_E}
\mathrm{GR}.
\]

The induced graviton retract is claimed to carry its own evaluation and coevaluation. On that
assumption, generalized cuts can sew only pure-graviton internal states. The unwanted dilaton and
two-form states are absent from this induced sewing; they are not asserted to be ghosts, BRST-exact
states, or terms that cancel after ambient sewing.

Generalized-cut closure determines an amplitude or integrand equivalence class. It does not choose
a preferred off-shell propagator, vertex set, or loop-integrand representative. Constructing a
canonical cyclic strong-deformation retract on the first-jet chain complex is a separate Frost-side
problem.

## Common scalar pairing

The three branches use a nondegenerate multiparticle pairing denoted

\[
I_{\rm scalar}.
\]

Its inverse is intended to be the intrinsic KLT/CHY pairing kernel. The claim needed by Nima is
stronger than numerical invertibility in a chosen ordering basis: the pairing must descend to the
correct quotient, be independent of basis, and intertwine the scalar boundary-gluing maps.

## Status table

| Sector | Extraction | Additional operation | Current perimeter |
| --- | --- | --- | --- |
| NLSM | \(\operatorname{gr}_R\) | order-enriched Jordan/QTDS resolution | half-object established; relative tree lift passes; cyclic resolution and classification open |
| Yang–Mills | \(J_F^1\) | gauge cohomology | intrinsic CHY-class derivation still to be recorded |
| Gravity | doubled first jet | \(\operatorname{PrimSym}_g^2\) and scalar pairing | tree selector and induced cuts retained; canonical cyclic lift open |

## Prohibited collapse

Do not describe all three theories as the same kind of boundary face. Do not omit gauge descent
from Yang–Mills. Do not identify a pure external graviton projection with pure internal sewing. Do
not promote Jordan strictification from an amplitude-preserving presentation to a classification
theorem without stating its hypotheses.

## Decision

Keep associated grades, jets, cohomological descent, idempotent splitting, strictification, and
modular completion as distinct typed operations. The immediate Nima test is whether the NLSM
associated grade produces a factorization-compatible half-object before a Parke–Taylor factor is
attached.

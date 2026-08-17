---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Smooth Opposite-Cut Nearby Cycles Do Not Retract to Support

## Question

Entry 360 reduced cross-sector descent to a missing specialization from a
full sector coefficient object to the common extraordinary overlap object.
The hard-to-vary claim tested here is

\[
\boxed{
\text{deformation to the opposite-Cut normal canonically supplies that
retraction.}
}
\]

The test uses the frozen source pole exponents, principal normal equations,
purity shift, and occurrence boundaries. No Thom class or double pole is
inserted.

## Frozen local normal model

Inside the (q_{\mathcal G_{12}})-residue surface, take

\[
v=q_{\mathcal G_{23}}=E+a
\]

as transverse coordinate to the common curve. The sector-12 source summands
contain (q_{\mathcal G_{12}}^{-1}), but no factor
(q_{\mathcal G_{23}}^{-1}). Therefore their opposite-Cut pole exponent is
zero. Cyclically, the sector-23 summands have exponent zero along
(q_{\mathcal G_{12}}=0).

On the generic common open, away from the frozen branch and marked divisors,
the coefficient local system is consequently smooth across (v=0).

## Nearby cycles versus the costalk

For a smooth coefficient object,

\[
\psi_v\mathcal L_{12}\simeq i^*\mathcal L_{12}
\]

in ordinary degree. But codimension-one purity gives

\[
i^!\mathcal L_{12}
\simeq i^*\mathcal L_{12}[-2](-1).
\]

Thus the canonical nearby-cycle specialization lands in ordinary
restriction, not in the shifted extraordinary costalk needed by Entry 360.
In the local free model, a degree-zero map from the smooth object to this
negative shift would lie in a negative Ext group and vanishes.

## Euler-class check

The normal divisor is principal, globally trivialized on the local model by
(v=q_{\mathcal G_{23}}). Its ordinary normal line is therefore trivial and

\[
c_1(N_i)=0.
\]

Hence the ordinary self-intersection Euler class cannot convert (i^*) into
(i^!) or split the localization counit. The available canonical arrow keeps
the opposite variance:

\[
i_!i^!\mathcal L_{12}\longrightarrow\mathcal L_{12}.
\]

The proposed retraction is not produced by deformation to the normal cone,
ordinary nearby cycles, or the ordinary Euler class.

## Narrow result

\[
\boxed{
\text{smooth opposite-Cut specialization}
\not\Rightarrow
\text{retraction onto overlap support}.}
\]

This falsifies the tested claim without falsifying the supported cospan of
Entry 360. A nonzero reverse arrow would require secondary supported/excess
data beyond ordinary smooth nearby cycles. None is inferred here.

## Classification

| Datum | Classification |
|---|---|
| opposite-Cut exponent zero | frozen sector coefficient data |
| smooth nearby cycles | ordinary coefficient restriction |
| ([-2](-1)) | shared purity calculus |
| trivial normal line | existing principal carrier normal |
| ordinary Euler class | zero |
| missing reverse arrow | secondary supported/excess datum |
| new carrier stratum | none |

## Evidence

- `research/benincasa/marici-gm/src/bin/overlap_normal_specialization_gate.rs`;
- `research/benincasa/overlap-normal-specialization-gate-certificate.json`;
- the frozen six source occurrences of Entry 229;
- Entries 357--360.

## Next falsifier

Test the only remaining source-native candidate: the two-normal derived
self-intersection for

\[
(q_{\mathcal G_{12}},q_{\mathcal G_{23}}).
\]

Construct its unlocalized Koszul object with the frozen ordered normals and
ask whether its top determinant class maps to the common extraordinary
costalk while remaining compatible with the singly polar six-term source.

If the determinant class requires multiplication by the absent joint pole
(1/(q_{\mathcal G_{12}}q_{\mathcal G_{23}})), it is not source realized and
the descent transition fails. If the source boundary-value/Cousin complex
realizes it without changing pole order, it supplies the secondary excess
class excluded from the ordinary nearby-cycle test.

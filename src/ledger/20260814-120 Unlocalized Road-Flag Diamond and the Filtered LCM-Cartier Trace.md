# Unlocalized Road-Flag Diamond and the Filtered LCM--Cartier Trace

## Record

Date: 2026-08-14

Status: proved finite unlocalized carrier/occurrence/normal theorem.  The
full two-route road flag, its principal-lcm Alexander--Whitney cap, the
adjacent \(\operatorname{Tor}_0\) and \(\operatorname{Tor}_1\) grades, and
their graph-Cartier extension square are all integral and explicit.  A
ringed six-functor realization and the supported target-side
Koszul--Cech comparison remain unconstructed.

This entry answers the anti-circular rank test of entry 119.  The answer is
not that every relevant group has rank one.  The normalized filtered map has
a unique degree-zero line, while its first and second coherence groups have
rank profile

\[
(1,2,1).
\]

The two middle directions are retained and identified: one is the endpoint
occurrence extension and the other is the repeated-normal excess line.

## The full two-route road flag

The smallest unlocalized occurrence carrier at the marked \(D03\) endpoint
is not one route.  It is the full Koszul diamond

\[
K_{03}^{\rm occ}:
R\langle F_{03}\rangle
\xrightarrow{(x_3,-x_1)^T}
R\langle Z_3,Z_1\rangle
\xrightarrow{(x_1,x_3)}
R\langle v_{10}\rangle .
\]

Its square is the commutative cancellation

\[
x_1x_3-x_3x_1=0.
\]

Either individual route has nonzero square.  Thus the inherited \(x_3\)
mark is a cap/cochain on the two-route object, not permission to delete the
other route before forming the differential.

This diamond is the algebraic shadow of the closed barycentric road star

\[
F_{03}>\{Z_1,Z_3\}>v_{10}.
\]

The unit incidence column and row are primitive, so the carrier is saturated
and has no hidden integral index.

## Principal-lcm normalization and the AW cap

Up to the common \(D03\) occurrence line, use the principal labels

\[
m_{F}=1,
\qquad m_{Z_3}=x_3,
\qquad m_{Z_1}=x_1,
\qquad m_v=x_1x_3.
\]

For every radial generization \(S\subset S\cup\{a\}\),

\[
X_a m_S=m_{S\cup\{a\}}.
\]

Hence the principal lines \(Rm_S\) form a strict weighted subcomplex, and
their chosen geometric generators conjugate the weighted radial differential
to ordinary cellular incidence without inverting an occurrence variable.
The ordinary barycentric Alexander--Whitney diagonal therefore lifts to
these labelled lines.

At the nontransverse central edge this says explicitly that, for

\[
m=x_1x_3,
\qquad
\bar e_c=m e_c,
\qquad
\bar b=X_{03}m v_{10},
\qquad
\bar a=x_5m v_+,
\]

the weighted boundary becomes

\[
d\bar e_c=\bar b-\bar a
\]

and the normalized line-valued AW formula is

\[
\boxed{
\Delta_{\rm lcm}(\bar e_c)
=\bar a\otimes\bar e_c+\bar e_c\otimes\bar b.
}
\]

With the endpoint counit equal to one on \(\bar a,\bar b\), the chain
identity \(d\Delta_{\rm lcm}=\Delta_{\rm lcm}d\) is the ordinary interval
identity in principal bases.  This uses dualizable labelled lines; it is not
an ambient functional \(R\to R\) dividing by their monomials.

After the positive \(x_3\)-Thom evaluation, the selected road coefficient is

\[
(x_3x_1)/x_3=+x_1.
\]

Consequently the endpoint-relative carrier map is

\[
\boxed{
C_{\rm AW}^{\rm lcm}:
[Re_3\xrightarrow{-x_1}Rq_0]
\longrightarrow
[RF_{03}\xrightarrow{+x_1}R\tau_0],
\qquad (e_3,q_0)\longmapsto(F_{03},-\tau_0).
}
\]

The only scalar chain equation is

\[
(+x_1)(+1)=(-1)(-x_1).
\]

Thus the generic coefficient, endpoint sign, and occurrence factor are all
derived from the lcm/AW geometry.

## The complete local derived profile

The endpoint occurrence mapping complex has one torsion-free copy of
\(R/(x_1)\) in each of degrees zero and one.  Its change to the two standard
summands is unimodular.

For the repeated normal,

\[
D_3=K(u_3^\vee)\otimes K(u_3),
\qquad u_3^\vee=-q_3^{-1}u_3,
\]

entry 100 gives

\[
0\longrightarrow E[1]
\xrightarrow{i}D_3
\xrightarrow{\pi}E
\longrightarrow0,
\]

where

\[
i(1)=\eta_{3,\rm mix}=(-q_3,-1)
\]

and the marked excess retraction satisfies

\[
\operatorname{tr}^{\rm ex}i=\operatorname{id}_E.
\]

The quotient and excess bases have determinant \(-1\), a Laurent unit.
Therefore both \(\operatorname{Tor}_0\) and
\(\eta_{3,\rm mix}\operatorname{Tor}_1\) are primitive integral lines.

Taking the occurrence and normal factors together gives the torsion-free
profile

\[
\boxed{
H^0=E,
\qquad H^1=E\oplus E,
\qquad H^2=E.
}
\]

Here \(E\) denotes the residual supported coefficient module; the ranks are
relative to it.  The \(x_3\)-Cartier direction is a filtration and
Bockstein, not a second freely tensor-added Koszul factor.  Adding such an
independent factor would double-count the same support and change the rank
profile.

The two degree-one summands have different provenance:

\[
H^1=
E\,\epsilon_{x_1}
\oplus E\,\eta_{3,\rm mix}.
\]

The first is the occurrence/recollement extension.  The second is the
repeated-normal excess.  A rank-one result obtained by deleting either one
is inadmissible.

## The filtered LCM--Cartier trace

On the graph

\[
q_3-1=t_3x_3,
\]

the normalized repeated-normal top satisfies

\[
\boxed{
\beta_{x_3}(q_3z)=[t_3]\eta_{3,\rm mix}.
}
\]

Thus the filtered Bockstein of \(D_3\) is

\[
B_{D_3}=i\circ([t_3]\operatorname{id}_E).
\]

Give

\[
W=\omega_{(\operatorname{Gal}_{03},\partial)}
\widehat\otimes(E\oplus E[1])
\]

the corresponding target Bockstein

\[
B_W=[t_3]\operatorname{id}_E.
\]

The two associated-grade components are then forced:

\[
\boxed{
\Theta_{03,\rm flag}^{(0)}
=C_{\rm AW}^{\rm lcm}\widehat\otimes\pi,
\qquad
\Theta_{03,\rm flag}^{(1)}
=C_{\rm AW}^{\rm lcm}\widehat\otimes
\operatorname{tr}^{\rm ex}.
}
\]

The only new filtered extension equation closes exactly:

\[
\begin{aligned}
\Theta^{(1)}B_{D_3}
&=C_{\rm AW}^{\rm lcm}
\operatorname{tr}^{\rm ex}([t_3]\eta_{3,\rm mix})\\
&=[t_3]C_{\rm AW}^{\rm lcm}\\
&=B_W\Theta^{(0)}.
\end{aligned}
\]

The radial equations are the lcm-AW chain identities, the normal equations
are those of \(\pi\) and \(\operatorname{tr}^{\rm ex}\), and the mixed
square vanishes by the Koszul totalization sign.  Both Tor grades are
retained.  No new generator, inverse occurrence variable, or numerical
denominator is used.  The physical normal remains the independent factor

\[
\operatorname{ev}_{[dX_{03}]}=+1.
\]

This proves the minimal filtered cellular/recollement trace once its
explicit lcm road-flag coefficient system is fixed.  It is not yet the full
six-functor map denoted schematically by \(p^*(-)\otimes q^!(-)\).

## Exact boundary and corrected comparison

Three statements remain outside the theorem.

1. No ringed spatial correspondence with projections \(p,q\), extraordinary
   pullback, and relative-dualizing trace has yet been constructed.  The
   calculation proves its finite cellular/coefficient normal form, not its
   global PC provenance.
2. No target-side Koszul--Cech comparison has yet identified this
   unlocalized flag trace with the entry-97/100 Cousin trace.
3. No physical-Cut square or extension over the remaining \(q_2/a\) arm is
   claimed.

Entry 119's phrase “later localization recovers entry 97” must be read in a
support-sensitive, one-sided sense.  Literal common-base localization is
impossible:

\[
K_0\simeq0,
\qquad D_3\simeq0
\]

after inverting \(x_1\) and \(u_3\).  The correct next comparison keeps the
source and excess support unlocalized, applies the lcm cap first, and only
then applies the target Koszul--Cech map:

\[
\boxed{
\kappa_{Q_{03}}\circ
\Theta_{03,\rm flag}^{\rm fil}
\stackrel?\simeq
\Theta_{03}^{\rm loc}.
}
\]

The equality must include the residue

\[
\eta_{3,\rm mix}
\longmapsto
\left[\frac1{u_0u_1u_3u_5}\right]
\]

and the occurrence endpoint, twist, and physical-normal lines.  It may not
be replaced by tensoring the entire endpoint kernel with the Laurent ring.

## Evidence

New exact certificate:

- `research/voevodsky/check_d03_unlocalized_road_flag_aw.rs`, SHA-256
  `9911ef21323f7e5bf4ab965b7fea7f6219eef10b7b35956619fc97e54b6bb253`.

It verifies the two-route weighted square, primitive unit incidence,
principal-lcm quotients, endpoint AW chain identity, occurrence Ext profile,
normal Tor profile and unimodular basis, Kunneth ranks, graph Bockstein,
filtered component equations, total mixed sign, and explicit localization
contractions.

## Outcome contract

```json
{
  "claim": "The unlocalized D03 road-flag algebraic shadow is the full two-route lcm-weighted Koszul diamond. Its normalized AW cap, repeated-normal Tor filtration, and graph-Cartier Bockstein canonically define a minimal filtered cellular trace with torsion-free rank profile (1,2,1).",
  "status": "proved",
  "assumptions": [
    "The road flag is retained as the full two-route diamond before the inherited x3 mark is applied.",
    "Principal occurrence ideals are kept as labelled dualizable lines; no ambient occurrence inverse is used.",
    "The theorem is scoped to the finite cellular/recollement coefficient model, with the entry-100 marked excess normalization."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_unlocalized_road_flag_aw.rs",
    "ledger entries 100, 105, 118, and 119"
  ],
  "factorization_test": {
    "two_route_d_squared": "passed integrally",
    "principal_lcm_AW": "passed without occurrence inversion",
    "occurrence_Ext": "ranks (1,1), torsion-free",
    "normal_Tor": "ranks (1,1), eta primitive",
    "total_loaded_shadow": "ranks (1,2,1), torsion-free",
    "graph_Cartier": "beta_x3(top)=[t3] eta_3,mix",
    "filtered_extension_square": "passed",
    "whole_base_localization": "contractible negative control",
    "six_functor_provenance": "unconstructed",
    "target_Koszul_Cech_comparison": "unconstructed"
  },
  "counterevidence": [
    "A one-route deletion is not a chain complex.",
    "The two middle derived directions are independent before the filtered attachment and neither may be discarded.",
    "Literal common-base localization erases the supported endpoint and excess classes."
  ],
  "next_experiment": "Construct the ringed road-flag correspondence and prove the one-sided target Koszul-to-Cech comparison kappa_Q03 Theta_flag = Theta_03^loc, including occurrence endpoints, reciprocal/BM variance, eta residue, and [dX03]=+1."
}
```

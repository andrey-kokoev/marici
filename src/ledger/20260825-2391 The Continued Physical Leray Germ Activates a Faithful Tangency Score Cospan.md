---
authors:
  - marici.Benincasa
date: 2026-08-25
---
# 2391 — The Continued Physical Leray Germ Activates a Faithful Tangency Score Cospan

## Hard-to-vary claim

Entry 2390's (g_1,g_2) recovery ports are not merely formal algebraic
functionals.  They belong to the canonical analytically continued physical
Leray germ already derived from the Bunch--Davies boundary value.  Their
Tate-regularized leading weights are nonzero on the positive nonsoft
total-energy boundary.  Consequently the physical continued residue germ,
unlike the literal positive-chain boundary, activates a jointly faithful
three-port score cospan through second source-word order.

## Frozen physical continuation

Two prior source results are retained without modification.

1. Entry 180 proves that the negative-imaginary Bunch--Davies prescription
   and positive Cayley--Menger chain uniquely determine the local Leray
   residue germ, including sheet, orientation, Jacobian, and multiplicity.
2. Entry 675 proves that the resulting physical wall cocycle occupies all
   six labelled reduced-tangency coordinates with nonzero residues away
   from the established signed-energy conductor support.

This is analytic continuation of the source chain.  It is distinct from a
literal boundary incidence of the starting positive chamber, which Entries
365 and 555 correctly show to be zero.

## Total-energy limits of the labelled ports

For each nonramified port (g_1,g_2), the raw oriented root difference has
ordinary order (-1) in (E=E_T).  Multiplication by the forced Tate factor
(E) gives the same nonzero leading trace:

\[
\boxed{
\left.E(\rho_+-\rho_-)\right|_{E=0}
=-\frac{3}{8xy}.
}
\]

Their tangency discriminants have leading value

\[
\boxed{\Delta_{g_1}(0)=\Delta_{g_2}(0)=4x^2y^2.}
\]

Hence the two normalized ports extend as nonzero coefficient lines on

\[
xy(x+y)\ne0.
\]

In particular they remain nonzero at both positive roots of Entry 2390's
(g_3) blind polynomial.

## Physical score cospan

Let (H_i) be the (3\times3) total-energy score Hankel matrix for the
labelled port (g_i), acting on

\[
\mathcal S_2=\langle S,D_ES,D_E^2S\rangle.
\]

The continued physical wall cocycle supplies the labelled map

\[
\mathcal O_{m phys}^{(2)}:
\mathcal S_2
\longrightarrow
\operatorname{im}H_{g_1}
\oplus\operatorname{im}H_{g_2}
\oplus\operatorname{im}H_{g_3}.
\]

Entry 2390 proves that both (H_{g_1}) and (H_{g_2}) have rank three for
(x,y>0).  Multiplication by the nonzero physical residue weights preserves
their kernels.  Therefore

\[
\boxed{
\ker\mathcal O_{m phys}^{(2)}=0
\qquad(x>0, y>0).
}
\]

At the two points where (ker H_{g_3}\ne0), either nonramified labelled
port still reconstructs the complete source-word packet.  No fitted
projector or additional support summand is used.

## Classification

- literal positive-chain incidence with the walls: zero;
- canonical continued physical Leray germ: source-derived and unique;
- (g_1,g_2) total-energy limit: ordinary Tate-regularized coefficient
  lines;
- (g_3) limit: ramified Kummer coefficient line;
- combined physical continued score kernel through grade two: zero;
- new Carrier support: none;
- marked-wall and tensor/polarization completion: not included.

Thus contextual faithfulness survives the first total-energy-supported
scalar interacting staircase test:

\[
\boxed{
\text{one port can become blind, while the source-labelled physical
continuation remains jointly faithful.}
}
\]

This is not yet the full objective's tensor theorem.  The frozen scalar
integrand still does not determine the finite-(q) tensor vertex or both
polarization ports.

## Next falsifier

Move to the first intersections where the present proof's nonzero weights
can fail:

\[
x=0,qquad y=0,qquad x+y=0,
\]

and to the signed-energy conductor collisions of Entry 675.  Construct the
supported cones and test whether marked-wall score ports recover every
nearby class.  A class surviving all source-derived continued ports would
be a sector-specific coefficient obstruction; only support outside the
frozen arrangement would threaten H2 at Carrier level.

## Evidence

- `research/benincasa/check_total_energy_tangency_port_recovery.py`;
- `research/benincasa/total-energy-tangency-port-recovery.json`;
- Entries 180, 365, 555, 675, and 2390;
- allocator claim `seqclaim-8761479d9dc53d7baae97eef`.

## Outcome contract

~~~json
{
  "claim": "The g1 and g2 recovery ports of Entry 2390 lack source-derived physical activation.",
  "status": "falsified for the canonical analytically continued Leray germ",
  "literal_positive_chain_wall_incidence": 0,
  "continued_leray_germ_canonical": true,
  "regularized_g1_leading": "-3/(8*x*y)",
  "regularized_g2_leading": "-3/(8*x*y)",
  "physical_continued_grade2_kernel_dimension": 0,
  "new_carrier_datum": false,
  "tensor_completion": "absent from the frozen scalar source"
}
~~~

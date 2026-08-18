---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 687 — The Kummer Tangency Costalk Has Zero Direct Elliptic Nearby Image

## Hard-to-vary claim

The normalized total-energy Kummer line of Entries 683--684 is a conductor
costalk supported in the finite fiber chart. Its support closure remains
disjoint from the infinity divisor through the generic nonsoft
\(E=0\) degeneration. Therefore its direct morphism to the elliptic
infinity nearby-cycle quotient is canonically zero.

This is a support-base-change statement. It does not choose a lift into the
nine-master module and does not identify the physical functional with an
absolute master vector.

## Frozen projective support test

Let \(h_3(t;E)=0\) be the source-derived reduced \(g_3\) tangency cover
after

\[
z=E-x-y.
\]

Homogenize it in \([T:S]\). Its value on the fiber infinity section
\(S=0\) is

\[
\overline h_3(T,0;E)
=(E-x-y)T^2.
\]

At total energy zero,

\[
\overline h_3(T,0;0)=-(x+y)T^2.
\]

Thus on

\[
xy(x+y)\ne0
\]

the conductor support does not meet fiber infinity in a neighborhood of
\(E=0\). Meanwhile the ramified special fiber is

\[
h_3(t;0)=-(x+y)(t-y)^2,
\]

so its unique limiting point is the finite point

\[
[T:S]=[y:1].
\]

## Typed comparison

Let \(i_C\) include the conductor support and \(j_\infty\) include the
elliptic infinity boundary. The relevant Cartesian pullback is empty over
the stated generic neighborhood. Proper/support base change, followed by
nearby cycles, gives

\[
\boxed{
j_\infty^*\psi_E i_{C!}=0.
}
\]

The Kummer residue line

\[
\mathcal K_{\rm phys}=\langle\epsilon\rho_3\rangle
\]

is a costalk of \(i_{C!}\). Consequently its canonical direct infinity
component vanishes:

\[
\boxed{
\mathcal K_{\rm phys}
\longrightarrow
\psi_E\mathbb V_{\rm ell}(-1)
\quad\text{is zero at the support-restriction grade.}
}
\]

This supplies the typed zero that Entry 685 could not obtain from an
arbitrary identification with \(e_6\) or \(v_{\rm alg}\).

## What remains open

Zero direct support restriction does not imply that the full localization
extension splits. A nonzero physical coupling can still occur as the
connecting morphism in a morphism of localization triangles:

\[
\mathcal K_{\rm phys}
\longrightarrow
\psi_E\mathcal T_7[1]
\quad\text{or its equivalent extension class.}
\]

Therefore no scalar master-coordinate connection is inferred, and
\(\mathcal Q\) is not declared absent from the extension class.

## Classification

- Kummer conductor costalk: sector-specific coefficient data;
- direct elliptic infinity image: zero;
- algebraic/relative extension: uncomputed;
- existing energy/Cut carrier: unchanged;
- new carrier datum: none;
- possible \(\mathcal Q\)-home: only the supported connecting morphism,
  not direct infinity restriction.

## Next falsifier

Construct the local two-term localization triangle at the ramified
\(g_3\) conductor point, retain the physical orientation and
\(E=\epsilon^2\) deck character, and compute its connecting class into
the algebraic Gysin kernel. Test that class, rather than a chosen scalar
lift, for \(\mathcal Q\)-valuation.

## Evidence

- `research/benincasa/check_g3_nearby_support_at_infinity.py`;
- `research/benincasa/g3-nearby-support-at-infinity.json`;
- Entries 595 and 683--685;
- allocator claim `seqclaim-a479b7dd92bca9ecc5350c3c`.

## Outcome contract

~~~json
{
  "claim": "The physical total-energy Kummer costalk may couple directly to the elliptic infinity quotient by support restriction.",
  "status": "falsified",
  "support_meets_infinity_near_E_zero": false,
  "direct_elliptic_nearby_image_rank": 0,
  "arbitrary_master_lift_used": false,
  "extension_class_computed": false,
  "new_carrier_datum": false,
  "next_experiment": "Compute the oriented local localization connecting class into the algebraic Gysin kernel."
}
~~~

---
authors:
  - marici.Nima
date: 2026-08-18
---
# 1066 — The Moving-Wall Correction Makes Connection and Residue Commute Strictly

> Numbering repair (2026-08-19): relocated from filename 949 and conflicting
> heading 667 under allocator claim `seqclaim-bc4d6970479ffe0657563197`.
> The evidential content and scope are unchanged.

## Hard-to-vary claim

On the literal physical source, the bulk parameter connection and the three
shared-wall Poincaré residues commute strictly once the mandatory moving-wall
double-pole contribution is included.  The ordinary algebraic
residue--Čech calculus therefore supplies no secondary correction capable of
cancelling the rank-three first jet found in Entries 1068 and 1064.

## Typed source square

For a shared wall \(q=0\), write the bulk coefficient locally as

\[
\frac{G}{q}.
\]

Parameter differentiation at fixed bulk coordinates gives

\[
\partial_\xi\frac{G}{q}
=
\frac{\partial_\xi G}{q}
-
\frac{G\,\partial_\xi q}{q^2}.
\]

The second term cannot be discarded.  Its residue is the normal derivative

\[
-(\partial_\xi q)\,\partial_qG|_{q=0}.
\]

Since the wall moves with normal velocity

\[
\partial_\xi q_{\rm wall}=-(\partial_\xi q),
\]

the induced wall connection gives exactly

\[
\nabla_\xi^{W}\operatorname{Res}_q(\Omega)
=
\left(partial_\xi G-(\partial_\xi q)\partial_qG\right)_{q=0}
=
\operatorname{Res}_q(\nabla_\xi^{\rm bulk}\Omega).
\]

Thus the square commutes without a fitted homotopy.

## Exact gate

The checker retains separate bulk and wall degrees and evaluates the source
coefficient

\[
\frac{q_{g_{23}}+q_{g_{31}}}
{K_E^\gamma\prod_{i=1}^5q_i}
\]

on all three shared walls, in the \(x\) and \(y\) directions, at three
generic kinematic points and multiple generic tangent samples.  Polynomial
derivatives are exact degree-four derivatives over \(\mathbb Q\).

For \(\gamma=0,1,5\), the gate records

\[
84\text{ legal source squares},
\qquad
84\text{ zero commutators}.
\]

Thirty squares have a nonzero moving-wall correction.  Hence strict
commutation is not a consequence of testing only stationary walls; it uses
the double-pole term essentially.

The independently retained pair-intersection checker again gives

\[
d_{\rm Cech}\rho_{\rm phys}=0.
\]

## Consequence

Entry 1064 left open whether the localization boundary contributes a
secondary algebraic term that cancels the two transverse derivatives of the
unsplit source.  The typed source square falsifies that mechanism.  Standard
Poincaré residue transports the source connection to the wall connection;
it does not project away its transverse directions.

This does not invalidate the physical wall cocycle or its relative lift.
It says only that a small flat coefficient line is not produced by the
ordinary algebraic residue--Čech differential.

The remaining candidates are now narrower:

1. the regulator-finite-part specialization of Entries 649--650;
2. a physical relative-chain pairing or Stokes datum;
3. an independently sourced Gysin kernel beyond ordinary residue.

The Källén cover of Entry 660 may type the coefficient cover on which such
data live, but does not itself alter this commutative square.

## Scope

The check constructs the bulk-to-wall source square and reuses the verified
pair Čech degree.  It does not yet construct the complete bulk exact
generator module or a regulator-specialized chain homotopy.  The conclusion
is therefore about the literal source and ordinary algebraic residue, not
every possible derived or analytic realization.

## Evidence

- `research/benincasa/physical_bulk_wall_connection_residue.py`;
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`;
- Entries 648--650, 1068, 1064, and 1065.

## Outcome contract

~~~json
{
  "claim": "The ordinary localization boundary contributes a nonzero algebraic connection-residue commutator that can cancel the unsplit source first jet.",
  "status": "falsified",
  "source_square_checks": 84,
  "zero_commutators": 84,
  "nonzero_moving_wall_corrections": 30,
  "cech_boundary_closed": true,
  "regulator_specialization_tested": false,
  "physical_chain_pairing_tested": false,
  "next_experiment": "Compute the epsilon-zero finite part of the source IBP primitive and test path and representative independence."
}
~~~

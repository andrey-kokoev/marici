---
authors:
  - marici.Nima
date: 2026-08-18
---
# 701 — The Remaining Comparison Is Derived Pushforward Base Change

## Correction after Entry 700

Entry 699 located a missing comparison between adjoining the fifth pole and
homogeneous specialization. Entry 700 constructs the generic five-pole
twisted de Rham complex and proves that the elementary comparison is already
strict:

\[
i^*\operatorname{Loc}_{q_G} C^{\rm gen}
\cong
\operatorname{Loc}_{i^*q_G}i^*C^{\rm gen}.
\]

Indeed, with

\[
I=(\nu_1,\nu_2,\nu_3),\qquad \nu_i=P_i^2-X_i^2,
\]

the source equation satisfies

\[
\partial_{\nu_i}q_{\mathcal G_{12}}=0.
\]

Localization therefore preserves each labelled generator

\[
\nu_1\nu_2,\qquad \nu_1\nu_3,\qquad \nu_2\nu_3
\]

of the square-free part of \(I^2/I^3\). There is no chain-level
Beck--Chevalley obstruction and no place for \(\mathcal Q\) in that
commutator.

## The genuinely open square

The nontrivial operation is integration, not localization. Let \(\pi\) be
the generic fiber projection and let \(i\) denote homogeneous
specialization. The remaining comparison is

\[
\boxed{
\beta_{\rm GM}:\quad
Li^*R\pi_*\operatorname{Loc}_{q_G}(C^{\rm gen})
\longrightarrow
R\pi_{{\rm hom},*}
\operatorname{Loc}_{i^*q_G}(Li^*C^{\rm gen}).
}
\]

Entry 700 proves only that the inputs commute before \(R\pi_*\). It does
not imply that derived direct image is flat across the homogeneous
discriminant. Higher Tor, vanishing cycles, or a failure of cohomological
base change can still appear after integration.

## Acceptance contract

A proposed computation of \(\beta_{\rm GM}\) is typed only if:

1. the generic five-pole complex and its differential are explicit;
2. the maps \(\pi\) and \(i\) form the declared Cartesian square on a
   stated locus;
3. every derived functor has a declared source and target category;
4. the three normal labels remain separate through \(I^2/I^3\);
5. the comparison is constructed before ranks, determinants, or
   \(\mathcal Q\)-valuations are taken;
6. any claimed homotopy is explicit, source-derived, and compatible with
   the differential.

The resulting comparison has exactly four admissible classifications:

- **strict:** the two derived chain maps agree;
- **homotopy:** their difference is exact in the derived Hom complex, with
  an explicit admissible homotopy;
- **obstructed:** the difference defines a nonzero derived-Hom class whose
  support is located;
- **untyped:** a corner, functor, comparison map, or coefficient category
  is absent.

The rank identity \(35=15+20\), a fitted quotient, saturation, or an
unlabelled specialization cannot supply the cell.

## Gate for the quartic

Only after \(\beta_{\rm GM}\) and its cone are typed may \(\mathcal Q\) be
tested. Intrinsic tests include the support or annihilator of obstruction
cohomology, choice-independent Fitting ideals, and valuations of invariant
minors after lattices and bases are frozen. These must distinguish

\[
\text{carrier support},\qquad
\text{coefficient support},\qquad
\text{extension support}.
\]

A factor of \(\mathcal Q\) in an arbitrary matrix coordinate is not such a
test.

## Meta-level consequence

The search has moved one categorical level upward:

\[
\boxed{
\text{normal grading commutes with localization, but integration may fail
to commute with specialization.}
}
\]

Thus the next calculation is not another local denominator audit. It is a
derived Gauss--Manin base-change calculation for the generic five-pole
family. A filtered-derived or nearby-cycle specialist becomes useful only
after the four corners and chain maps exist and the remaining ambiguity is
the realization of \(\beta_{\rm GM}\).

## Evidence

- Entries 698--700;
- `research/benincasa/check_second_normal_localization_bc.py`;
- `research/benincasa/check_derived_pushforward_base_change_contract.py`;
- `research/benincasa/derived_pushforward_base_change_contract.json`;
- allocator claim `seqclaim-e0413e246d841b8053ba42d2`.

## Next falsifier

Construct a finite, source-labelled model of the generic five-pole derived
direct image and compute the cone of \(\beta_{\rm GM}\) on each of
\(\nu_1\nu_2\), \(\nu_1\nu_3\), and \(\nu_2\nu_3\). If its cohomology
vanishes, this route to \(\mathcal Q\) closes. If it does not, its intrinsic
support is the first admissible place to compare with \(\mathcal Q=0\).

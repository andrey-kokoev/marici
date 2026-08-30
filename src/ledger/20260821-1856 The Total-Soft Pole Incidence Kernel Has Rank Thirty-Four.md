# 1856 — The Total-Soft Pole Incidence Kernel Has Rank Thirty-Four

## Frozen incidence map

Before introducing any coefficient differential, map each of Entry 1855's
fifty physical pole occurrences to its surviving source label:

\[
\partial_{\rm occ}:
\mathbb Q^{50}_{\rm pole\ occurrences}
\longrightarrow
\mathbb Q^{16}_{\rm source\ labels}.
\]

Every target label occurs, so

\[
\operatorname{rank}\partial_{\rm occ}=16,
\qquad
\operatorname{coker}\partial_{\rm occ}=0.
\]

Therefore

\[
\boxed{
\dim\ker\partial_{\rm occ}=50-16=34.
}
\]

This kernel measures only repeated labelled occurrences across charts.  It is
not yet coefficient cohomology.

## Cyclic representation

The occurrence space is ten regular (C_5)-orbits:

\[
\chi_{\rm occ}=(50,0,0,0,0).
\]

The sixteen-label target consists of the fixed total-energy line and three
regular five-label orbits:

\[
\chi_{\rm label}=(16,1,1,1,1).
\]

Hence

\[
\boxed{
\chi_{\ker}=(34,-1,-1,-1,-1).
}
\]

Over (mathbb Q), this is

\[
\boxed{
\ker\partial_{\rm occ}
\simeq
6\mathbb Q_{\rm triv}
\oplus
7\mathbb Q(\zeta_5).
}
\]

## Cancellation layer remains separate

Entry 1854 removed ten ambient occurrences through five chartwise
pair/four-site cancellations.  Those five relations precede the physical
fifty-to-sixteen incidence map and are not part of its rank-thirty-four kernel.
Combining the two stages without this distinction would mix coefficient
cancellation with occurrence redundancy.

## Narrow result

The surviving label map is already surjective.  Thus no missing carrier label
or support cell can be inferred from the total-soft occurrence assembly.  Any
nontrivial next class must arise from a typed coefficient differential on the
rank-thirty-four occurrence kernel.

## Next falsifier

Derive the actual overlap/restriction differential between the five physical
residue charts.  Test its action on

\[
6\mathbb Q_{\rm triv}\oplus7\mathbb Q(\zeta_5)
\]

without replacing it by the bare incidence projection.  If no source-derived
overlap map exists, stop at the incidence kernel rather than naming it
cohomology.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_total_soft_incidence_kernel.py`
- `research/benincasa/results/five-site-region-pair-total-soft-incidence-kernel.json`
- Entries 1854--1855
- allocator claim: `seqclaim-908a3085bd5a47f4c2ac2926`

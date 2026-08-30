# 1855 — The Corrected Total-Soft Support Has Fifty Pole Occurrences

## Occurrence transport

Transport Entry 1854's restricted packet through the five labelled
region-pair charts.  Each chart begins with twelve ambient residual labels.
One pair-wall label and one four-site label restrict to the same hyperplane and
cancel there, leaving ten physical pole occurrences per chart.

The cyclic census is therefore

\[
\boxed{
5\times12
=
60\ \text{ambient residual occurrences},
}
\]

\[
\boxed{
60-10
=
50\ \text{physical pole occurrences}.
}
\]

The ten removed occurrences are two labelled occurrences in each chart, not
ten carrier labels.

## Label-level image

After forgetting chart occurrence, the fifty poles use sixteen distinct
source labels:

- the total-energy label (G);
- all five (G_{-e}) labels;
- all five singleton-region labels;
- all five four-site-region labels.

The entire pair-wall orbit

\[
g_{12},g_{23},g_{34},g_{45},g_{15}
\]

is absent from the physical pole divisor.  Each pair-wall occurrence cancels
against a chart-specific four-site occurrence, while every four-site label
survives in two other charts.

Accordingly the surviving multiplicities are

\[
10\ \text{(G_{-e}) and four-site labels of multiplicity }2,
\]

and

\[
6\ \text{total-energy and singleton labels of multiplicity }5.
\]

## Architectural meaning

This is why labelled occurrences are not replaceable by an unlabelled set of
hyperplanes.  The same four-site carrier label can be cancelled in one chart
and support a genuine pole in another.  Cancellation is a property of the
coefficient occurrence, not deletion of the carrier label.

No new carrier datum appears.

## Scope

The census does not yet define sewing maps between chart occurrences.  The
fifty-dimensional occurrence set is not being asserted as a cohomology rank.

## Next falsifier

Construct the cyclic incidence matrix from the fifty pole occurrences to the
sixteen source labels, retaining the ten cancelled pair/four-site relations.
Compute its kernel and cokernel before adding any coefficient differential.
Retain separately the five chartwise cancellations, each involving two
labelled occurrences; do not miscount the ten removed occurrences as ten
independent relations.
This will separate pure occurrence redundancy from genuine derived
coefficient extension.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_total_soft_occurrence_support.py`
- `research/benincasa/results/five-site-region-pair-total-soft-occurrence-support.json`
- Entries 1830 and 1854
- allocator claim: `seqclaim-b774a4d8c5c58e923a9a9cd4`

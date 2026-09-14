# Additive 3-horns for one coherence pyramid

## Question

Can the four planes of one pyramid be encoded so that a missing face is derived rather than freely postulated?

## Claim boundary

This packet treats an additive 3-truncated shadow with rational plane labels. It does not construct the full coherence-pyramid infinity-category.

For the four oriented plane labels, impose

\[
h_{234}-h_{134}+h_{124}-h_{123}=0.
\]

A 3-horn supplies three labels and omits the fourth. Since each omitted label has coefficient \(1\) or \(-1\), the equation determines a unique rational filler.

For example,

\[
h_{123}=2,
\qquad
h_{124}=-3,
\qquad
h_{134}=5
\]

forces

\[
h_{234}=10.
\]

The checker solves all four horn orientations and recovers the declared tetrahedron exactly.

## Existence depends on admissibility

Unique algebraic recovery does not guarantee an admitted filler. If admissible labels are restricted to

\[
\{-1,0,1\},
\]

then the required value \(10\) is an obstruction: the rational filler exists, but no admissible filler exists.

## Uniqueness depends on faithful readout

If the missing integral label is observed only through parity, then the readout is not faithful. Within the bounded test set from \(-4\) through \(4\), the same even readout admits five candidates:

\[
-4,-2,0,2,4.
\]

The compressed horn therefore has multiple compatible fillers even though the strict rational horn has one.

## Disposition

The additive shadow distinguishes three cases without changing the horn equation:

1. strict rational labels give a unique filler;
2. an admissibility predicate can refuse that filler;
3. a nonfaithful readout can leave multiple fillers.

The next construction must replace additive labels by actual planes and replace the alternating boundary equation by equality of the two pasted 2-arrows. Until then, this is a finite 3-truncated diagnostic, not an infinity-categorical horn theorem.

## Verification

```text
python research/voevodsky/checkers/check_coherence_pyramid_3_horns.py
```

Artifacts:

- `research/voevodsky/checkers/check_coherence_pyramid_3_horns.py`
- `research/voevodsky/results/coherence_pyramid_3_horns.json`

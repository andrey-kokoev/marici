# Every New Grade Adds Exactly Two Extremal Endpoint Ports

## Endpoint filtration

Fix source spin (s\geq1). The grade-(r) ladder cokernel is

\[
E_{s,r}=\mathcal H_{s+r-1}^{(s+r-1)},
\]

with dimension

\[
\dim E_{s,r}=2s+2r-1.
\]

The axis-marked correspondence injects each endpoint into the next:

\[
E_{s,r}\hookrightarrow E_{s,r+1}.
\]

Its quotient is always the pair of new extremal weights

\[
m=\pm(s+r).
\]

Therefore the endpoint tower has a two-dimensional successive quotient at every grade.

## Minimal filtered chart

Begin with all (2s+1) weights of the base endpoint (E_{s,1}=\mathcal H_s^{(s)}). At each later grade, retain only the two new extremal source ports and transport every earlier weight through the axis-marked injections.

At grade (r), the required port count is

\[
(2s+1)+2(r-1)=2s+2r-1,
\]

exactly the target endpoint dimension. The supports are disjoint by axial weight, so deleting any selected port removes one target coordinate.

This yields the constructive filtration

```text
all base weights
  + next extremal pair
  + next extremal pair
  + ...
  = complete final endpoint
```

## Spin-two grade three

For (s=2,r=3), the nested chart is

\[
5+2+2=9.
\]

Concretely:

- five (l=2) source ports provide weights (-2,\ldots,2);
- the extremal (l=3) ports provide weights (-3,3);
- the extremal (l=4) ports provide weights (-4,4).

Transporting the earlier weights produces all nine coordinates of (mathcal H_4^{(4)}).

The previously derived (7+2) chart is the same filtration started one rung later: use all seven grade-two endpoint coordinates, then add the final extremal pair.

## Why 21 and 9 are both correct

The complete grade-three source kernel contains three independent harmonic blocks and has dimension

\[
5+7+9=21.
\]

Observing that entire direct sum requires 21 ports. Observing only the final endpoint, while remembering how it is assembled from prior endpoints, requires nine ports.

In general,

\[
\dim\ker\mathcal A_{s,r}=r(2s+r),
\]

whereas

\[
\dim E_{s,r}=2s+2r-1.
\]

These answer different questions:

- the first counts all independently available low source modes;
- the second counts the final target obstruction representation.

Their difference is not lost information. It is information outside the declared final-endpoint target.

## Categorical interpretation

The endpoint sequence is a filtered object whose associated graded pieces are

\[
\operatorname{gr}_1 E\cong\mathcal H_s^{(s)},
\qquad
\dim\operatorname{gr}_1E=2s+1,
\]

followed by two-dimensional extremal packets:

\[
\dim\operatorname{gr}_rE=2,
\qquad r\geq2.
\]

The marked axis supplies the splitting. Without the axis, the full (SO(3)) irreducibles at adjacent grades do not embed.

## Evidence replay

The checker verifies the filtration, port count, nonzero source and transport coefficients, and the distinction from the full kernel for (1\leq s,r\leq10).

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/general_two_extremal_per_grade_filtration_checks.py
```

Machine-readable results are written to `research/strominger/results/general_two_extremal_per_grade_filtration_checks.json`.

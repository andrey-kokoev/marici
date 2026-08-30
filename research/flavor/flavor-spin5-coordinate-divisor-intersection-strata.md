# Coordinate-Divisor Intersections Stack Port Kernels and Lose Canonical Branch Frames

## Exact stratum table

Continue with the \(8\times8\) Completion-B block \(K\) from WP889. On the
fixed nonzero Higgs-vacuum slice, set subsets of the four coordinate factors
\(y_1,y_2,y_3,y_6\) to zero while leaving \(y_4,y_5\) generic. Exact symbolic
ranks give:

| Vanishing coordinates | \(\operatorname{rank}K\) | \(\operatorname{corank}K\) |
|---|---:|---:|
| none | 8 | 0 |
| \(y_1\) | 6 | 2 |
| \(y_2\) | 6 | 2 |
| \(y_3\) | 7 | 1 |
| \(y_6\) | 7 | 1 |
| \(y_1,y_2\) | 3 | 5 |
| \(y_1,y_3\) | 5 | 3 |
| \(y_1,y_6\) | 5 | 3 |
| \(y_2,y_3\) | 5 | 3 |
| \(y_2,y_6\) | 5 | 3 |
| \(y_3,y_6\) | 6 | 2 |
| \(y_1,y_2,y_3\) | 2 | 6 |
| \(y_1,y_2,y_6\) | 2 | 6 |
| \(y_1,y_3,y_6\) | 4 | 4 |
| \(y_2,y_3,y_6\) | 4 | 4 |
| \(y_1,y_2,y_3,y_6\) | 1 | 7 |

The full symmetric mass matrix has twice each displayed corank.

## Additive rule and coherent excess

Away from \(y_1=y_2=0\), the port coranks add:

\[
d(y_1)=d(y_2)=2,
\qquad d(y_3)=d(y_6)=1.
\]

For example \(d(y_1,y_3,y_6)=2+1+1=4\). But setting both \(y_1\) and
\(y_2\) to zero also forces

\[
y_1y_5-y_2y_4=0.
\]

It therefore adds the WP889 coherent kernel:

\[
d(y_1,y_2)=2+2+1=5.
\]

All larger intersections containing \(y_1=y_2=0\) retain this one-unit
coherent excess.

## Static and dynamic frames

At a generic simple divisor, the kernel line or plane can be transported as a
total projector. At an intersection of corank greater than one, that total
kernel projector remains basis independent, but a decomposition into named
one-dimensional branches is not canonical. Its internal frame is acted on by
the appropriate unitary group of the degenerate kernel.

Consequently:

- static restriction supplies the total kernel projector;
- dynamic continuation supplies a connection on that kernel bundle;
- choosing branch-by-branch frames requires extra splitting data;
- a relational reference cell compares those two arrows but is not part of
  the original mass readout.

The rank table alone does not force a recursive branch architecture. It shows
exactly where such an architecture would require additional source-derived
splitting projectors.

## Selector consequence

Every coordinate divisor is reached by setting an allowed Yukawa coefficient
to zero. No declared source principle forces or excludes these strata. Their
kernel dimensions classify mass failures; they do not select a Yukawa point,
mass ratio, or portal magnitude.

## Verdict

The divisor arrangement has additive port failures plus one coherent excess
on the \(y_1=y_2=0\) locus. The physical total-projector grammar remains
well-defined, while branch frames become noncanonical at higher corank. The
next admissible dynamic calculation would require a declared loop and
connection in a chosen higher-corank stratum; inventing branch anchors from
the rank table is prohibited.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp890_spin5_coordinate_divisor_intersection_strata.py
~~~

# Prolate near-one asymptotics force growing dyadic depth, so no fixed finite positive edge subdivision can be complete

## Exact dyadic rule

The positive defect tower resolves a near-one eigenvalue gap `epsilon_Lambda` at depth

\[
\boxed{
2^{n(\Lambda)}
\varepsilon_\Lambda
\asymp1,
}
\]

so

\[
\boxed{
n(\Lambda)
=
\log_2
\frac1{\varepsilon_\Lambda}
+O(1).
}
\]

This rule is unconditional functional calculus.

## Classical prolate calibration

For a one-dimensional time--band concentration operator with large time--band product `c`, classical prolate asymptotics place the largest eigenvalues exponentially close to one. Qualitatively,

\[
1-\lambda_{max}(c)
=
\operatorname{poly}(c)
e^{-\kappa c}

\]

for a positive convention-dependent constant `kappa`.

The repository's previous compact-window audit records the resulting extremely small coercivity margins and explicitly warns that they collapse at a prolate/Landau--Widom rate. Its quoted numerical constants are authority-limited, but the qualitative exponential near-one scale is the only fact used here.

Set

\[
\varepsilon_c
=
1-\lambda_{max}(c).
\]

Then

\[
\begin{aligned}
n(c)
&=
\log_2
\frac1{\varepsilon_c}
+O(1)\\
&=
\frac{\kappa}{\log2}
c
+O(\log c).
\end{aligned}
\]

Thus

\[
\boxed{
n(c)\asymp c.
}
\]

## Relation to the cutoff parameter

In the ordinary real model with physical and Fourier windows both of radius `Lambda`, the time--band product is proportional to

\[
c_\Lambda
\asymp
\Lambda^2
\]

under the displayed Fourier normalization. Hence the depth required to resolve the extremal near-one mode is

\[
\boxed{
n(\Lambda)
\asymp
\Lambda^2,
}
\]

up to normalization and lower logarithmic corrections.

If the semilocal radial reduction uses a different effective parameter, the exact growth changes, but `n(Lambda)` still diverges whenever the relevant gap tends to zero.

## Fixed-depth obstruction

Fix any finite dyadic depth `n_0`. The soft bulk filter is

\[
\lambda^{2^{n_0}}.
\]

For eigenvalues satisfying

\[
1-\lambda
\ll
2^{-n_0},
\]

one has

\[
\lambda^{2^{n_0}}
=1-o(1).
\]

As the cutoff grows, prolate eigenvalues enter this unresolved band arbitrarily close to one. Therefore every fixed `n_0` eventually fails to separate concentrated near-one modes from the exact eigenvalue-one/Sonin sector.

Thus

\[
\boxed{
\text{no fixed finite number of dyadic defect stages resolves the full cutoff limit}.}
\]

## Consequence for the ten-node proposal

The earlier ten-node positive refinement was a finite semantic sketch containing one generic "prolate/radical conditioning" stage. It remains useful as a macro-level diagram, but it cannot be a complete microscopic subdivision if conditioning means resolving the full near-one spectrum.

The provisional count

\[
9^3=729
\]

therefore counts only cells in a finite macro-refinement. It is not the count of the complete positive coherence object.

The complete positive edge must contain a filtered tower

\[
\boxed{
\cdots
\to
B^{2^3}
\to
B^{2^2}
\to
B^2
\to
B,
}
\]

or the oppositely oriented ind/pro system, together with all positive defect layers.

## Correct categorical object

For each finite cutoff `Lambda`, the dyadic tower is indexed by

\[
j\in\mathbb N.
\]

The cutoff limit requires a cofinal joint system

\[
\boxed{
(\Lambda,j)
\in
\mathbb R_+
\times
\mathbb N
}
\]

with admissible paths satisfying

\[
2^j\varepsilon_\Lambda
\asymp1.
\]

Hence the positive refinement is naturally a filtered/pro-simplicial diagram, not one finite edgewise subdivision of `Delta^3`.

Finite truncations remain useful computational approximations, but coherence must include transition maps between depths.

## Sonin atom versus near-one cloud

At each fixed cutoff,

\[
B^m
\to
P_{\{1\}}(B)
\]

as `m->infinity`. But taking `Lambda->infinity` first creates an increasing cloud of eigenvalues exponentially close to one.

Therefore the limits do not commute without a uniform spectral gap:

\[
\boxed{
\lim_{\Lambda\to\infty}
\lim_{m\to\infty}
B_\Lambda^m


e
\lim_{m\to\infty}
\lim_{\Lambda\to\infty}
B_\Lambda^m.
}
\]

The joint scale `m=2^(n(Lambda))` is not optional; it is the data selecting how the near-one cloud is separated from the exact Sonin atom.

## Positivity implication

Any proof that replaces the growing dyadic tower by one fixed spectral projection must supply a cutoff-uniform gap

\[
1-\lambda
\ge
\varepsilon_0>0
\]

away from the exact intersection sector. Classical prolate behavior rules out such a gap in the ordinary model.

Thus a finite positive filler cannot be justified by compactness or a fixed Douglas contraction constant.

## Revised cell counts

The signed asymptotic realization remains a finite seventh edgewise subdivision with

\[
343
\]

elementary tetrahedra.

For positive coherence:

- `729` is the count of a ten-node macro-truncation;
- each prolate-conditioning cell expands into an unbounded dyadic tower;
- the complete number of finite-dimensional cells is countably infinite before taking the continuous cutoff parameter into account.

Therefore the honest count is

\[
\boxed{
0
\text{ certified cells in the complete filtered positive refinement},
}
\]

not `0/729` as though `729` were a final denominator.

## Source boundary

This conclusion uses only:

1. the exact dyadic scale rule;
2. qualitative prolate eigenvalues approaching one;
3. absence of a cutoff-uniform near-one gap.

It does not rely on the authority-limited numerical margins recorded in the prior compact-window audit.

## Disposition

The positive coherence geometry cannot be a fixed finite edgewise subdivision:

\[
\boxed{
\text{signed coherence: finite }343\text{-cell object},
}
\]

\[
\boxed{
\text{positive coherence: filtered/pro-simplicial dyadic object}.
}
\]

The next construction must define transition maps and coherence between dyadic depths, then choose a source-derived cofinal joint path `(Lambda,n(Lambda))` from observer-weighted prolate gap asymptotics.

# The local Weil negative index is monotone in support scale

## Question

How do the fixed-support semibounded Weil operators assemble as the support window grows?

## Nested form domains

For `0<L_1<L_2`, extension by zero embeds the smooth reciprocal core on `[-L_1,L_1]` into the core on `[-L_2,L_2]`. The completed explicit formula gives the same quadratic value to the same test: enlarging the ambient support window does not alter endpoint, archimedean, or prime evaluations of that test.

After closure in the natural logarithmic form norms, this gives a form-compatible isometric inclusion of the smaller local domain into the larger one. This is workflow/support-scale order, not physical time.

## Negative index

Let

`nu(L)=max dimension of a subspace on which Q_L is negative definite`.

Because `W_L` is semibounded with compact resolvent, `nu(L)` is finite and equals the number of negative eigenvalues counted with multiplicity.

Nested test spaces imply

`nu(L_1)<=nu(L_2)`.

This is the variational monotonicity of inertia: every negative subspace available at smaller support remains available after extension by zero.

## RH criterion as a monotone defect function

Weil's criterion becomes

`RH iff nu(L)=0 for every finite L`.

If RH is false, some compactly supported test has negative Weil square, so `nu(L)>=1` for every sufficiently large window containing that test. Therefore failure appears at a finite support scale even though no universal finite scale is known in advance.

Define the first-instability scale

`L_*=inf{L:nu(L)>0}`.

This is a support threshold, not a physical event parameter. The infimum need not be attained without continuity of the moving-domain family.

## Arithmetic stratification

The prime part visible on a window changes when `2L` crosses `log n`, because convolution support reaches the prime-power location. Between these thresholds the list of prime atoms is fixed, although their matrix elements still change with the moving domain and basis. Thus the support-scale family has a discrete arithmetic stratification superimposed on continuous archimedean/domain variation.

This suggests a certified search organized by prime-power intervals:

1. fix a window interval between adjacent half-log prime powers;
2. construct lower eigenvalue enclosures uniformly over that interval;
3. propagate the nonnegative verdict until the next atom enters;
4. update by the new finite prime perturbation.

## Limitation

Monotonicity is one-sided. Verifying `nu(L)=0` up to any finite `L` does not control larger support. Nor does the finite negative index at each window give a uniform bound on `nu(L)` as `L` grows.

## Disposition

The global problem is organized by a monotone integer-valued defect function with finite local values. A counterexample is discoverable at finite support; a proof still needs a uniform mechanism preventing the first index jump at every prime-power stratum.

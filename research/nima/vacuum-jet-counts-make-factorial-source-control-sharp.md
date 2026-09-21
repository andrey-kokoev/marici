# Vacuum jet counts make factorial source control sharp

## Status

Voevodsky's concurrent `../voevodsky/factorial-fox-summability-has-a-vacuum-necessity-test-and-compatible-filtered-exactness.md` closes factorial necessity on the forgotten sector and transfers finite filtered exactness and bounded-limit reconstruction to the stronger domain.

This note supplies independent exact normal-form counts, a two-sided vacuum norm comparison, and an explicit discontinuity test. It supplements that result rather than claiming a new general necessity theorem for retained-feature coefficients.

## 1. Exact path and relation counts

Use the prescribed unit vacuum/Omega norms, cut-l1 shapes, and graph multiplier

`b_s(k)=t^k k!`, where `t=2 lambda s>=2`.

For one all-forgotten path w of length n, every choice of k distinct ordered event positions gives a different ordered edge record. All buffers are vacuum. Hence

`||D_k(w)||_unweighted=binomial(n,k)`.

Put

`S_n(t)=sum_(k=0)^n t^k k! binomial(n,k)`.

Its full summed norm is exactly S_n(t).

Now let v_n be a forgotten two-event diamond difference followed by a fixed forgotten suffix of length n-2. The two paths share all suffix edges and have distinct diamond edges. Selections avoiding the first two events cancel: their edge records, buffer endpoints and vacuum values coincide. Every selection meeting the diamond retains an edge unique to its branch, and cannot cancel. Thus

`||D_k(v_n)||_unweighted
 =2 [binomial(n,k)-binomial(n-2,k)]`,

with out-of-range binomial coefficients zero. In particular D_0(v_n)=0 and the top jet has norm two. The exact summed norm is

`||D(v_n)||_(s,b)=2 [S_n(t)-S_(n-2)(t)] >= 2 n! t^n`.

No spectral evaluation, retained feature, or theta estimate enters these formulas. The feature radius b is irrelevant.

## 2. A two-sided norm comparison on the whole forgotten sector

For any signed forgotten-path vector x_c in an endpoint corner of length n, the top jet retains its entire ordered path. Distinct paths therefore have disjoint top-jet coordinates, even when lower jets cancel. Consequently

`||D_n(x_c)||_unweighted=||x_c||_path`.

The triangle inequality and the exact single-path count give an upper bound S_n(t)||x_c||_path for all its jets together. Since

`S_n(t)=n! t^n sum_(j=0)^n t^(-j)/j! <=2 n! t^n`,

retaining outer endpoints and summing yields

`sum_c n(c)! t^(n(c)) ||x_c||_path
 <= ||D(x)||_(s,b)
 <= 2 sum_c n(c)! t^(n(c)) ||x_c||_path`.

This applies to arbitrary forgotten coefficient vectors, including the all-forgotten part of the relation ideal. The upper estimate is a statement about the forgotten sector; it is not an upper estimate for general marked vectors after discarding their retained coefficients.

Because the radii t=2 lambda s are cofinal among positive radii, the domain of all-depth summed jets on this sector is exactly its factorial all-radius source space. The fixed letter constant A in the earlier factorial source definition is absorbed by this cofinality.

On this restricted sector the full summed-jet topology is equivalent to the factorial source topology. This does not restore a continuous inverse for general retained-feature data. It also does not contradict instability of a single associated-layer observer or a product-topology jet family: the norm now includes every jet order, including the highest one.

## 3. An explicit relation outside the summed domain

Use distinct endpoint corners of lengths 2m and define

`x=sum_(m>=1) v_(2m)/m!`.

For every fixed p and C, its common-path norm is bounded by

`sum_(m>=1) 2(1+2m)^p C^(2m)/m! < infinity`.

The ratio of successive scalar summands tends to zero. Thus x lies in the earlier all-exponential-radius relation ideal, even with every fixed polynomial path weight imposed.

Its length-2m top-jet contribution is

`2 (2m)! t^(2m)/m! >= 2 m! t^(2m)`.

These terms do not tend to zero, so the full family is not in any of the declared depth-summed receiver spaces. Each fixed jet does exist: its coefficient bound grows only polynomially in m, which is summable against 1/m!.

This is the same obstruction as Voevodsky's sqrt(n!) counterexample, expressed using rational coefficients at even event lengths. It is a failure of full-jet summability, not a failure of bounded filtered reconstruction or a nonzero analytical kernel.

## 4. No continuous extension from the old source topology

Fix a target parameter t and set

`u_n=v_n/[2 n! t^n]`.

Every fixed old source seminorm tends to zero on u_n:

`(1+n)^p C^n ||u_n||_path
 =(1+n)^p (C/t)^n/n! ->0`.

But the target top-jet norm of u_n is one. Therefore the full jet map on finite sources has no continuous extension from the old all-radius common-path topology into that summed receiver.

More generally, if a scalar path-length weighted l1 norm with weight w(n) bounded the full jet map on the forgotten relation ideal with constant M, testing v_n would force

`n! t^n <= M w(n)`, for every n>=2.

Thus factorial-order growth, up to exponential radius factors, is necessary for that class of uniform source norms. This is not a classification of optimal anisotropic norms on general feature-bearing sources.

## 5. Disposition

The factorial strengthening in `factorial-path-scales-sum-the-full-fox-jet-family.md` addresses a genuine obstruction. It is sharp up to constants and radius changes on the forgotten sector. Voevodsky's supplied note additionally proves compatibility of finite filtered exactness and bounded inverse-limit reconstruction on the factorial domain; those transfers are not reproved here.

The remaining boundary is general retained-feature conditioning and dual/derived comparison, not whether the old entire exponential-radius source already admits the full summed Fox realization: it does not.

## Verification

`uv run python research/nima/checkers/check_factorial_jet_necessity.py`

Artifact: `results/factorial-jet-necessity.json`.

Passed 88 actual single-path cut counts, 88 diamond-suffix cut counts, 12 signed vacuum norm comparisons, and 15 exact source-series ratio checks. Top-jet growth was also checked with rational arithmetic. Infinite convergence and the topology conclusions follow from the proofs above.

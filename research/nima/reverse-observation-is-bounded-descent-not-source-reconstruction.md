# Reverse observation is bounded descent, not source reconstruction

## Result

A reverse observer is precisely a bounded descent of a specified source functional through a forward measurement. It need not reconstruct the source. Kernel compatibility alone is insufficient: continuity must hold in the actual measured norm.

This supplies a directional test for productization arrows. On the corrected frame images the reverse exists, with the previously computed conditioning. Across filtration restriction it fails for new-layer detectors. Across the frame-discrepancy map it exists for discrepancy tests, but not for a nonzero common-state observation.

No universal adjoint, tensor-dual surjectivity or direction-independent observer realization is inferred.

## 1. Exact bounded-descent criterion

Let F:X->Y be the declared bounded linear forward map between normed spaces, and let ell be a linear source functional. Use a consistent conjugation for first-slot Hermitian observations. Define

`C_F(ell)=sup_(Fx!=0) |ell(x)|/||Fx||_Y`,

with value infinity if ell is nonzero on ker F. Zero quotients are otherwise omitted.

There exists a bounded functional lambda on the genuine measured image F(X) such that lambda F=ell if and only if

`ker F subset ker ell` and `C_F(ell)<infinity`.

When it exists it is UNIQUE on F(X), with norm exactly C_F(ell). Define lambda(Fx)=ell(x); the kernel condition proves well-definedness and the displayed bound proves continuity. Necessity is immediate.

It extends uniquely to the closure of F(X). Hahn--Banach gives some norm-preserving extension to all Y, but that last existence statement does NOT mechanically admit the extension as a physical test, a balanced tensor observer or a source-equivariant map. Such admission requires the owning response surface. Our concrete examples below use already supplied tests.

For an all-radius source/receiver scale, state the boundedness at specified seminorms with any radius losses. A single norm theorem must not be silently applied uniformly to a Frechet intersection.

## 2. A kernel-free map can still have no bounded reverse observer

For a simple exact model take X=Y=l2 and F(x)_n=x_n/n. It is injective and bounded. The bounded source functional

`ell(x)=sum_(n>=1) x_n/n`

has coefficient sequence (1/n) in l2. Its formal measured-image representative has constant coefficient one, which is not in l2.

More explicitly take x^(N)=(1,2,...,N,0,...). Then Fx^(N) has its first N entries one, so

`|ell(x^(N))|/||Fx^(N)||=sqrt(N)`.

Thus C_F(ell)=infinity despite ker F=0. This example explains the continuity gate; it is not substituted for an arithmetic source.

## 3. Actual positive case: the cubic source functional

On the actual cubic homogeneous I^3 corner, let ell=L_A be the original residual-gap functional. The old four-sector measurement F_4 and the private-sector measurement F_p have kernels contained in ker ell. Their admitted ideal tests prove bounded descent at every fixed admitted frame with nonzero calibration denominators.

The supplied sharp norm results quantify its price:

`C_(F_4)(ell) has order A^(-2y-5) exp(901pi A^2)`,

and, with the additional existing private row available, the reverse observer has sharp norm order

`A^(-2y-5) exp(101pi A^2)`.

The original coefficient representation had the larger exponent 904. These statements concern recovery of ONE functional on the actual cubic source image, not recovery of all source coefficients or a uniformly stable inverse in A.

The private representative agrees with ell on I^3 but not with its old extension to the whole J_1/J_4. The lower-filtration correction theorem identifies the missing information. A reverse observer must always specify which source domain its factorization covers.

## 4. Actual negative case: reverse filtration observation

Let q_m:E_(m+1)->E_m be the source filtration restriction. The next detector ell_(m+1) satisfies

`q_m(v_(m+1))=0`, `ell_(m+1)(v_(m+1))=d_(m+1)>0`.

It therefore cannot be represented by ANY functional on E_m, even discontinuously. This is a kernel obstruction before any norm or numerical issue.

Likewise, in the saturated observer tower, restriction pi_m:O_(m+1)->O_m loses a nonzero new witness state. A scalar test detecting that state cannot descend through pi_m. Particular older tests do descend, by construction. Thus reverse observability is a property of the requested functional, not a yes/no property of the tower alone.

Splitting a transition, where it exists, merely selects a lift. It does not recover arbitrary information in its kernel. The split-first/nonsplit-later theorem must not be read as reversing every observation at the first transition.

## 5. What can be recovered from the consistency observer

At one rung write the corrected frame-state space as C^0=direct_sum_f O^f and let Delta:C^0->C^1 be the reference-frame discrepancy map. Its kernel is the synchronized diagonal.

A functional ell on C^0 is recoverable from discrepancy data only if it vanishes on that diagonal. In this finite-dimensional setting the kernel condition is also sufficient for bounded descent, since Delta is onto a finite-dimensional space.

For example tests of a selected frame disagreement descend. A nonzero observation G of the common synchronized state does NOT: on the tuple (T^(f<-0)z)_f, discrepancy is zero but the common-state value may be nonzero.

There is a precise augmented reverse. Retain BOTH the reference state and all discrepancies:

`A((y_f))=(y_0,(T^(0<-f)y_f-y_0)_(f!=0))`.

This map is invertible, with

`y_0=z`, `y_f=T^(f<-0)(z+d_f)`.

It reconstructs the frame-state tuple, not an underlying source. With reference-aligned maximum norms, the forward norm is at most two and the inverse norm is at most two. In native frame norms the inverse additionally pays max_f ||T^(f<-0)||. The formulas commute with tower restriction when the corrected frame transitions do.

Thus the consistency tower alone has no common-state reverse, whereas the reference-plus-discrepancy tower has an explicit bounded stagewise reverse. Adding a reference is additional information, not an observer capable of detecting shared bias from disagreement alone.

## 6. Direction and composition along productization arrows

For X --F--> Y --G--> Z and a bounded test chi on Z, the pullback is chi G F. This always respects composition, with its declared forward norm bounds.

For a specified ell on X, a reverse representative on Z exists exactly when it is bounded in the composite measured norm ||GFx||. Recoverability on F(X) alone does not ensure recoverability after G: G may erase a direction seen by ell.

Conversely a representative on the composite image gives one on F(X) by composition with G, with

`C_F(ell)<=||G|| C_(GF)(ell)`.

There is no reciprocal inequality without additional information. Equal observations on genuine images also do not require chosen ambient extensions to agree on noisy off-image records.

Accordingly, productization is direction-sensitive. Corrected frame coherence identifies legitimate routes on their common visible state, while bounded descent determines which specified observations can be run backwards and at what noise cost.

## 7. Scope

Established: the exact reverse-observer criterion; its continuity obstruction; actual cubic and filtration applications; and an explicit reverse for the reference-plus-discrepancy tower.

Not claimed: a source inverse, an admitted observer from Hahn--Banach alone, a reverse for arbitrary quotient data, a uniform all-depth norm, or automatic source realizability of reconstructed observer states. Common-state bias and the source summability gates remain external to internal consistency checks.

## Verification

`uv run python research/nima/checkers/check_reverse_observation.py`

Exact fixtures verify kernel and norm obstructions, the augmented consistency inverse and its restriction compatibility, and loss of a functional under a further quotient. Actual cubic conditioning and new-layer nonvanishing use their supplied source proofs.

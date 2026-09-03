# The first two-translate spline hostile has an explicit seven-shift vector

## Setup

The repaired spline is

`f(x)=sum_(m=-2)^2 c_m k_7(x/2+m a)`,

with `a=2 log 2` and symmetric coefficients

`(c_2,c_1,c_0,c_-1,c_-2)=(1,-5,33/4,-5,1)`.

Its Fourier transform is nonnegative, so `f` is an autocorrelation of a compactly supported packet after spectral square-root factorization. Consequently evaluations of the explicit-formula functional on translates of `f` are Gram entries for translates of that underlying packet.

## First aligned translation

Choose physical translation

`delta=2a=4 log 2`.

Since `u=x/2`, this shifts the spline coordinate by one unit `a`. The Hermitian real cross kernel is represented by

`f_delta^sym(x)=(f(x-delta)+f(x+delta))/2`.

It is again a finite cardinal-spline combination, now with shifts `m=-3,...,3` and coefficients

`d_m=(c_(m-1)+c_(m+1))/2`,

where missing `c` values are zero. In descending shift order these are

`(d_3,d_2,d_1,d_0,d_-1,d_-2,d_-3)`

`=(1/2,-5/2,37/8,-5,37/8,-5/2,1/2)`.

Thus the first two-translate determinant requires only one new seven-shift evaluation in the already repaired explicit-formula machinery.

## Hostile determinant

Let `L` denote the declared executable explicit-formula functional. The baseline certificate gives

`L(f)` in `[1.1790450740e-5,1.1906013635e-5]`.

The two-translate Gram condition is

`L(f)^2-L(f_delta^sym)^2>=0`.

Equivalently,

`|L(f_delta^sym)|<=L(f)`.

Because the certified diagonal margin is small, this is a sensitive convention and positivity test. A violation gives the explicit negative combination of two translates. Passing one translation does not prove positive definiteness; it validates only the first nontrivial Gram minor.

## Source-normalization update

`research/nima/completed-zeta-to-spline-convention-map.md` now internally derives the checker tuple from the declared completed-zeta factorization and transform pairing. This narrows the earlier blocker. External source authority and the fully checked contour theorem remain absent, so the determinant is initially a theorem about the declared executable form.

## Acceptance test

Extend the existing interval checker without changing its conventions:

1. admit arbitrary finite symmetric shift/coefficient lists;
2. evaluate the seven-shift vector above with complete prime-power enumeration and the same archimedean tail proof;
3. interval-enclose the determinant;
4. reverse the prime sign and require a disjoint residual;
5. retain the baseline result unchanged as a regression fixture.

## Disposition

The abstract translate-Gram proposal now has a concrete cheapest falsifier. Ownership remains with the Nima spline checker; no cross-locus edit is authorized.

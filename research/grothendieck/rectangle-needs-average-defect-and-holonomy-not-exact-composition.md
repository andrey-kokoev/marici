# Mixed-prime rectangles require both average defect and holonomy

## Falsification of exact correlation composition

Let `k(a)` be any continuous normalized scalar cross correlation obtained from a reciprocal-centered translation-invariant source form, so `k(0)=1` and `k(-a)=k(a)`.

If exact forest correlation composition held on the multiplicative translation group,

`k(a+b)=k(a)k(b)`,

then continuity would make `k` an exponential character. Reciprocal evenness forces that character to be trivial:

`k(a)=1` for every `a`.

The complete Weil cross kernel is nonconstant; the prime-two block is a strict contraction on nontrivial directions, and separated test translates do not all have unit correlation. Therefore exact correlation composition cannot be the mixed-prime source law. Exact translation of vectors does not imply multiplication of their compressed correlations.

This falsifies the composition-average assumption `a=rs` used in the first holonomy-budget specialization.

## General rectangle defects

For the real normalized rectangle, retain

`a=(c+d)/2`,

`h=(c-d)/2`,

and define the average composition defect

`delta=a-rs`.

Parity decomposition gives

`D_+=(1+c)(1+d)-(r+s)^2`,

`D_-=(1-c)(1-d)-(r-s)^2`.

Substituting `c=rs+delta+h` and `d=rs+delta-h` yields

`D_+=(1-r^2)(1-s^2)+2 delta(1+rs)+delta^2-h^2`,

`D_-=(1-r^2)(1-s^2)-2 delta(1-rs)+delta^2-h^2`.

Thus the mixed rectangle has two independent cycle channels:

1. `delta`, the failure of direct correlation to equal the product of forest correlations;
2. `h`, the oriented route holonomy.

The prior single inequality is valid only on the special locus `delta=0`.

## Revised finite gate

A source-derived forest--cycle factorization must control both parity budgets. The exact scalar test is

`D_+>=0` and `D_->=0`,

with the diagonal bounds. Neither path commutation nor a single positive cycle norm suffices.

The average defect is not an error to eliminate: for a nontrivial stationary kernel it is unavoidable. A viable source mechanism must derive its sign and magnitude from the complete archimedean, endpoint, seam, and prime cross terms.

## Disposition

The exact-composition holonomy conjecture is rejected as a global mechanism. The general two-defect parity theorem survives. The next executable object remains the complete normalized four-cell Weil Gram; it must report `r,s,delta,h,D_+,D_-` rather than only a Brehmer or holonomy defect.

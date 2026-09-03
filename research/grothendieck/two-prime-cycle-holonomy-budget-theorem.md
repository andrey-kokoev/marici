# Two-prime cycle holonomy is bounded by the product of forest defect reserves

Status: exact theorem only on the special composition-average locus; not a valid global Weil mechanism. Superseded by `rectangle-needs-average-defect-and-holonomy-not-exact-composition.md`.

## Question

What is the exact first mixed-cycle inequality predicted by the forest--cycle factorization?

## Real scalar rectangle

For normalized vertices `1,p,q,pq`, write the Gram matrix

`G=[[1,r,s,c],[r,1,d,s],[s,d,1,r],[c,s,r,1]]`.

Here `r` and `s` are the forest edge correlations, while `c` and `d` are the two oriented diagonal route correlations. Parity decomposition gives

`D_+=(1+c)(1+d)-(r+s)^2`,

`D_-=(1-c)(1-d)-(r-s)^2`.

## Composition-average and holonomy

Separate the diagonal data into

`a=(c+d)/2`,

`h=(c-d)/2`.

The forest composition law predicts the route average

`a=rs`,

while `h` is the rectangle holonomy retained by the cycle port. Therefore

`c=rs+h`,

`d=rs-h`.

Substitution gives the exact identity

`D_+=D_-=(1-r^2)(1-s^2)-h^2`.

Consequently, assuming the diagonal bounds and `|r|,|s|<=1`, rectangle positivity is equivalent to

`|h| <= sqrt((1-r^2)(1-s^2))`.

## Interpretation

Each one-prime edge has defect reserve `1-r^2` or `1-s^2`. The mixed cycle may carry nonzero route holonomy, but its squared magnitude must fit inside the product of those two reserves. Exact coprime interchange is the special case `h=0`.

This is the first explicit forest--cycle Schur pivot:

`cycle_pivot=(1-r^2)(1-s^2)-h^2`.

It is not positivity under another name at this finite stage. It predicts exactly how much mixed-prime route mismatch the already measured one-prime contraction margins can absorb.

## Falsifier

On a common short-support Weil vector or finite local basis:

1. compute normalized prime-two and prime-three edges `r,s`;
2. compute both complete route correlations `c,d` to the log-six block;
3. test the composition-average residual `a-rs`;
4. if that vanishes, test the directed cycle pivot above.

A nonzero average residual falsifies the proposed forest composition law. A negative pivot falsifies positive cycle gluing even when both prime edges are individually contractive.

## Operator-valued target

For operator-valued transfers, `h^2` is replaced by the appropriate Schur/defect operator on the cycle fiber. The scalar theorem is mandatory on every one-dimensional compression. Therefore one scalar negative pivot already kills any operator-valued forest--cycle factorization.

## Disposition

The algebraic identity is exact conditional on `a=rs`. That condition is incompatible with any nonconstant continuous reciprocal-even stationary correlation if imposed globally. The general rectangle requires both the average defect `delta=a-rs` and route holonomy `h`; see the superseding packet.

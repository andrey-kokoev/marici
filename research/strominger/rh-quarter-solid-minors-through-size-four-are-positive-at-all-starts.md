# Quarter solid minors through size four are positive at all starts

## Question

Does the size-four Newton certificate extend from bounded row and column starts to arbitrary nonnegative starts?

## Claim boundary

The result proves positivity for contiguous minors of sizes at most four and integer shift. It does not cover noncontiguous minors or larger sizes.

## Disposition

The unchanged Newton gate passes for 64 polynomial minor families through size four. More strongly, every solid minor satisfies

\[
M_{r,c,k}(a)=
\left(\prod_{i=0}^{k-1}W_c(a+r+i)\right)
M_{0,0,k}(a+r+c),
\]

with positive row weights. The identity was checked exactly in 256 cases with a missing-shift control rejected. Because the leading minors have nonnegative Newton coefficients and positive constants, every solid minor of size at most four is strictly positive for arbitrary nonnegative integer row start, column start, and shift. The next executable leaf is `quarter-leading-minor-newton-size-eight`, where the reduction leaves only one leading-minor family per new size.

# Fixed-eight Gale Hall cuts have strictly positive exact slack

## Question

What is the minimum nonempty weighted Hall slack, and which connected negative-label shape attains it?

## Claim boundary

An exact forced-mincut census performed 54,261 optimizations across all 3,584 terminal cases. Every nonempty cut has positive slack. The global minimum is

\[
173128894788823002045153347095720653253538049525067890664833571380705089247431640160967511427579545063832250601442204754359467410921070802043574520259005920123563488051200000000.
\]

It occurs for base labels \(\{1,2,3,5,6\}\), exchanged labels \((i,j)=(7,0)\), and the connected negative pair

\[
\{0,2,3,4,5,7\},\qquad \{0,2,3,5,6,7\}.
\]

Forcing every negative label is exhaustive: each nonempty subset contains a forced label; min-cut minimizes Hall slack among subsets containing it. The connected-cut reduction ensures a global minimizing component is connected. This is a finite \(k=8\) theorem, not an all-order bound, and raw slack magnitudes are normalization-dependent.

## Disposition

The fixed-eight certificate is strict rather than merely feasible. The next local target is to factor the extremal two-label slack into source-minor terms and determine which comparable positive labels form its neighborhood. That finite identity is the narrowest candidate pattern for an all-order inequality.

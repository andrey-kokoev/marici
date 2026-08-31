# The seven resolved Bockstein images are p-tangent

The length-one Rees signal was resolved at the syzygy level rather than by
quotienting all raw derivative rows. At ambient degrees 8, 10, 12, and 14, over both `F_32003` and `F_32009`,
special relation syzygies produce first-derivative image ranks `7,7,11,15`.

At every cutoff the derivative along the p-tangent direction `(1,-1,0)`
produces exactly the same subspace as either unit p-normal. The combined
normal/tangent rank never exceeds the single-image rank. Therefore

\[
\operatorname{im}(\beta_{p\text{-normal}})/
\operatorname{im}(\beta_{p\text{-tangent}})=0
\]

at all four tested degrees and both primes.

This explains both earlier observations: the seven length-one Rees summands
are real, while the normal quotient contains no horn line. The result is more
precise than the raw-row quotient because it first resolves dependencies among
special relation generators.

Unbounded stabilization is not proved, but further cutoff growth alone is not
a lift mechanism. The remaining internal task is a moving-relation/Euler
coherence proof of normal–tangent image equality.
No tau lift or period is constructed.

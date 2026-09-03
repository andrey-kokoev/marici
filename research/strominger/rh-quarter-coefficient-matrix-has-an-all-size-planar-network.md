# Quarter coefficient matrix has an all-size planar network

## Question

Can nonnegativity of every coefficient-matrix minor be proved at all sizes rather than sampled?

## Claim boundary

The planar-network argument proves total nonnegativity of the monomial-coefficient matrix and hence Schur nonnegativity of leading-minor quotients. Promotion from positive solid minors to every source-matrix minor is a separate criterion.

## Disposition

Factor

\[
p_{j+1}(x)=p_j(x)
\prod_{s\in\{1,5/4,3/2,7/4\}}(x+s+j).
\]

Represent each linear factor by one planar layer with a level edge of weight \(s+j>0\) and a rising edge of weight one. Path weights from stage \(j\) to degree \(m\) are exactly the coefficient of \(x^m\) in \(p_j\). Lindström–Gessel–Viennot makes every ordered coefficient minor a nonnegative sum of disjoint-path weights at arbitrary size. Exact reconstruction through stage eight and 1,284,591 tested minors verify the orientation; a reversed sink order is negative. Cauchy–Binet therefore gives an all-size Schur-nonnegative expansion, with a positive term, for each leading-minor quotient. Combined with the positive-weight start reduction, every solid source minor is positive at every size and nonnegative integer shift. The next leaf is `quarter-total-positivity-fekete-lift`, checking the precise solid-minor criterion needed to promote this result to strict total positivity of the full source matrix.

# The consistent c=1 repair is positive on the first three-translate span

## Three-translate fixture

Let `g_j=tau_(j delta)g` for `j=0,1,2` and `delta=4 log 2`. The Gram matrix is Toeplitz:

`G_3=[[d,c_1,c_2],[c_1,d,c_1],[c_2,c_1,d]]`.

The lag-two cross packet is obtained by multiplying the baseline Laurent shift polynomial by

`(z^2+z^(-2))/2`.

This retains the baseline pole-annihilator and produces an explicit nine-shift septic packet.

## c=1 scout

Under the coherent convention `f(x)=profile(x)`, direct quadrature and complete prime enumeration give

`d approximately 2.12511463965`,

`c_1 approximately -0.846660221734`,

`c_2 approximately 1.50462976096`.

The three eigenvalues are approximately

`0.620484878687`,

`1.46334156617`,

`4.29151747409`.

Thus the repaired form remains positive on the first three translates, although the smallest margin decreases from the two-translate minimum `1.27845` to `0.62048`.

## Claim boundary

This is high-precision reconnaissance, not an interval theorem. Positivity at rank three does not imply positivity of the full translation kernel. The decreasing minimum indicates that higher Toeplitz ranks remain a meaningful hostile test.

## Disposition

After c=1 interval regeneration, compute lag values and certified Toeplitz minima incrementally. Stop at the first negative minor or continue only while each new rank adds a distinct constraint.

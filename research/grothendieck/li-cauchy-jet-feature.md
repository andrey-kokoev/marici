# Li features are uniform Cauchy-jet cocycles, but not yet source norms

## Uniform source-linear family

Define

`V_n(s)=1-(1-1/s)^n`.

The binomial theorem gives

`V_n(s)=sum_(j=1)^n (-1)^(j+1) binom(n,j) s^(-j)`.

If `C_w(s)=1/(s-w)` is the Mellin Cauchy mode, then

`s^(-j)=1/(j-1)! partial_w^(j-1) C_w(s)|_(w=0)`.

Therefore every `V_n` is obtained by one uniform finite operation on the
source-derived Cauchy-jet family. No zero location or multiplicity enters this
definition. This is the correct source-linear candidate underlying Li's
spectral feature.

## Cocycle structure

Writing `u=1-1/s`, the features obey

`V_(m+n)=V_m+u^m V_n`.

Thus `V_n` is a cocycle for the multiplicative iterates of the Cayley-like
coordinate `u`. This supplies more structure than a separate fitted vector
for each `n` and is a plausible interface to a source correspondence or
semigroup.

## Remaining quadratic gate

Li's coefficient is the regularized linear spectral trace

`lambda_n=sum_rho V_n(rho)`.

On the critical line, functional-equation pairing converts this into the
squared feature described in `li-spectral-norm-target.md`. Off the critical
line, the unitary identification fails by the already computed residual

`|u|^2-1=(1-2 Re(rho))/|rho|^2`.

Consequently the Cauchy-jet construction solves the uniform source-linear
part of Gate C, but not its positive Gram part. The remaining theorem must
derive an involution and positive pairing on these source jets before
evaluation at zero fibres. Applying the fibrewise critical-line conjugation
would be circular.

## Scope

This is an exact algebraic construction of the Li feature family and its
cocycle law. It does not prove that the features belong to the completed Weil
domain, construct their positive source Gram matrix, prove Li positivity, or
prove RH.

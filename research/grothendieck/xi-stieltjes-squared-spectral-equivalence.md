# RH as a Stieltjes property of the squared centered logarithmic derivative

## Squared coordinate

Put `w=s-1/2`. Completed xi is even in `w`, so its logarithmic derivative is
odd. Define the single-valued meromorphic function of `x=w^2`

`S(x)=[xi'/xi(1/2+sqrt(x))]/[2sqrt(x)]`.

The apparent square-root dependence cancels because the numerator is odd.

## Conditional spectral representation

If the nontrivial zeros are `1/2 +/- i gamma` with multiplicities
`m_gamma`, the paired Hadamard logarithmic derivative gives

`S(x)=sum_(gamma>0) m_gamma/(x+gamma^2)`

with the canonical convergence normalization inherited from completed xi.

Thus `S` is a Stieltjes transform of the positive squared-ordinate measure

`nu=sum m_gamma delta_(gamma^2)`.

Its poles lie on the negative real axis and have positive integer residues.

## Converse

Conversely, if the meromorphic function `S` is a Stieltjes transform with the
completed-xi growth and normalization, every pole of `S` lies at
`x=-gamma^2<=0` with positive residue. Pulling back by `x=w^2` places every
zero of xi at `w=+/- i gamma`, hence on the critical line. Residues recover
divisor multiplicities directly.

Accordingly RH is equivalent to the appropriate global Stieltjes property of
`S`.

## Complete-monotonicity shadow

For `x>0`, a Stieltjes representation gives

`(-1)^n S^(n)(x)=n! sum_gamma m_gamma/(x+gamma^2)^(n+1) >=0`.

This all-order real-axis hierarchy is a necessary shadow of RH and is more
structured than coefficientwise Li positivity. Complete monotonicity by
itself is not asserted sufficient without the meromorphic continuation,
growth, and Stieltjes pole conditions.

## Hostile-quartet rejection

The earlier hostile factor contributes

`1/(x-a^2)+1/(x-conjugate(a)^2)`

to the squared logarithmic derivative. For a genuine off-line quartet,
`a^2` is not confined to the negative real axis. Hence the Stieltjes pole
condition rejects exactly the deformation that symmetry and boundary sign
could not detect.

## Operator meaning

`S(x)` is the conditional trace of the resolvent of the squared
Hilbert--Pólya operator:

`S(x)=Tr[(x+H^2)^(-1)]`,

with multiplicities, subject to the appropriate trace/regularization
statement. This formulation retains multiplicity as positive residues,
avoiding the scalar-GNS eigenspace ambiguity until an operator realization is
constructed.

## New attack direction

Construct the Stieltjes representation from arithmetic source data. Possible
routes are:

1. prove the full complete-monotonicity hierarchy from the completed
   prime/gamma germ and then control analytic continuation;
2. construct a positive measure through a source-side Laplace transform;
3. identify `S` as a Weyl--Titchmarsh function of a source-canonical positive
   operator or canonical system.

This is an RH-equivalent target, not an RH proof.

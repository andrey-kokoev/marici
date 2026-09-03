# Dilation covariance of the explicit formula fixes every spline scale factor

## Canonical test variable

Let `phi` denote the single logarithmic test function appearing in a fixed explicit-formula convention. Its arithmetic and archimedean cells have the schematic form

`P(phi)=-2 sum_(p^m) log(p)/sqrt(p^m) phi(log(p^m))`,

`A(phi)=-(gamma+log pi)phi(0)`

`+sum_(n>=0)[phi(0)/(n+1)-integral_0^infinity phi(x)e^(-(n+1/4)x)dx]`,

with pole cells kept separately.

## Dilation theorem

For `c>0`, define

`D_c phi(x)=phi(c x)`.

Then every scale factor is forced:

`P(D_c phi)=-2 sum log(p)/sqrt(p^m) phi(c log(p^m))`,

and

`integral D_c phi(x)e^(-b x)dx`

`=c^(-1) integral phi(u)e^(-b u/c)du`.

Jets obey

`(D_c phi)^(r)(0)=c^r phi^(r)(0)`.

The support endpoint scales by `c^(-1)`, so the complete prime-power cutoff scales exponentially with that endpoint.

These identities are elementary changes of variables and do not depend on Fourier-sign convention. A published theorem is still needed to choose the undilated canonical `phi`, but once `c` is declared no independent adjustment of prime arguments, Laplace exponents, jets, or cutoffs is permitted.

## Classification of the hybrid checker

Taking the stored spline profile as `phi`:

- the prime branch implements `D_1 phi`;
- the archimedean branch implements `D_(1/2) phi`, because it integrates `phi(x/2)`, uses exponent `2b` after substitution, outer factor `2`, and jets `2^(-r)`.

Thus the defect is exactly a mixed-dilation functional

`P(D_1 phi)+A(D_(1/2)phi)`.

It is not a subtle Fourier-normalization ambiguity.

## Repair options

A repaired checker should accept one explicit scale `c` and derive all cells from it:

1. prime argument `c log(q)`;
2. Laplace prefactor `1/c` and exponent `b/c`;
3. jet factor `c^r`;
4. support-derived prime cutoff;
5. pole characters evaluated after the same dilation.

Run at least `c=1` and `c=1/2` as distinct valid test functions. Their energies need not agree; dilation is not claimed to preserve the Weil functional.

## Disposition

The normalization defect now has a complete algebraic repair contract. Source authority must choose the canonical undilated test convention, but implementation can no longer mix scales silently.

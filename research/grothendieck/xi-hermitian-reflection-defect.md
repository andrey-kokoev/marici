# A convergent Hermitian reflection defect equivalent to RH

For each nontrivial zero `rho=beta+i gamma`, define

```
h(rho) = (beta-1/2)^2 / (1+|rho-1/2|^2).               (1)
```

Summing with multiplicity gives

```
H_Xi = sum_rho m_rho h(rho).                           (2)
```

Because nontrivial zeros lie in `0<beta<1`, the numerator is at most `1/4`.
The Riemann--von Mangoldt counting bound then implies absolute convergence:
the tail is dominated by a constant times

```
sum_rho (1+|Im rho|^2)^(-1).
```

Every summand is nonnegative, and therefore

```
H_Xi = 0  iff  Re rho=1/2 for every nontrivial zero
        iff  RH.                                       (3)
```

Equivalently, in the zero coordinate `rho=1/2+i zeta`, the summand measures
the failure of `zeta` to be real:

```
h(rho) = (Im zeta)^2/(1+|zeta|^2).                     (4)
```

## Why this is not a proof

Equation (3) is a convergent spectral restatement of RH, not an explanation.
Unlike a Weil explicit-formula statistic, `h(rho)` depends on both `rho` and
its complex conjugate. It is not a holomorphic linear divisor functional.
The open-mapping no-go shows that this Hermitian dependence is unavoidable
for positivity across off-line configurations.

The actual research target is therefore precise:

> Construct a source-side paired correspondence whose norm or trace equals
> `H_Xi`, or a comparable reflection defect, without assuming RH.

Such a construction must be quadratic (or sesquilinear) in spectral data.
A single ordinary explicit-formula test cannot suffice. This is exactly the
place where a coefficient--Betti Mackey object, pull--push norm, or doubled
explicit formula could add content.

## Small hostile quartet

For an off-line quartet with zeros

```
beta +- iT,  1-beta +- iT,
```

the contribution is strictly positive and equals

```
4 (beta-1/2)^2/[1+(beta-1/2)^2+T^2]                   (5)
```

when all four zeros are simple. Thus the defect detects the smallest
functional-equation-compatible violation that defeated boundary skewness.


# Prime product-system conjecture for the unbounded Weil identity

Status: rejected as stated; superseded by the joint-coinvariant coextension target in `prime-product-system-conjecture-first-falsification.md`.

The defect is exact: compression `C_n=J*V_nJ` of a semigroup representation need not preserve composition unless the local block is jointly coinvariant or an equivalent coextension law is imposed.

## Problem

The current route has three coupled gaps: prime-power transfer composition, mixed-prime double commutation, and completion without a new radical. Treating them separately risks proving incompatible local statements.

## Bold conjecture

Let `H_0` be the radical-reduced unconditional short-support Weil block. Let `P` be the free commutative monoid on intrinsic primes. The complete normalized prime transfers on `H_0` admit a **minimal faithful regular dilation**

`C:P -> B(H_0)`,

`V:P -> B(H_infinity)`,

with isometric embedding `J:H_0->H_infinity`, such that:

1. `C_n = J* V_n J` for every `n` in `P`;
2. `V_m V_n = V_(mn)`;
3. for coprime `m,n`, `V_m* V_n = V_n V_m*`;
4. the complete Weil cross form satisfies

   `W(tau_m f * (tau_n g)*) = <V_m Jf, V_n Jg>`

   on all finite prime translates of the local core;
5. `H_infinity` is the closure of the span of `V_n JH_0`;
6. the induced map from the algebraic Weil radical quotient into `H_infinity` is injective.

Here `tau_n` is logarithmic translation by the tangent-normalized internal height `log n`. The dilation must be constructed from the complete prime, gamma, endpoint, seam, and mixed source form; it may not be defined from zero locations or assumed Weil positivity.

## Why one conjecture solves all three gaps

- Prime-power composition follows from `V_m V_n=V_(mn)` and compression.
- The `2 x 3` rectangle follows from regular double commutation for coprime generators.
- Minimality gives density of finite prime translates, while injectivity of the Weil quotient excludes a new completed radical.
- The displayed coefficient identity makes every finite Weil Gram matrix positive. Density and closedness then give unbounded Weil positivity on the full authorized domain, hence RH by the Weil criterion.

The common mechanism is not three coincidences. Unique factorization makes prime transport a free commutative product system; regular dilation is precisely the structure that turns its local contractions into one positive global coefficient kernel.

## Named rivals

1. Independent one-prime dilations with incompatible mixed-prime phases.
2. Merely commuting transfers without adjoint commutation.
3. A positive finite Gram tower whose completion acquires a new radical.
4. A dilation fitted to the zero divisor rather than derived from source channels.
5. A scalar Euler product lacking the complete archimedean and endpoint form.

## Risky consequences

The conjecture predicts:

- every one-prime Schur defect is contractive;
- the first mixed `2 x 3` Brehmer/Nica defect is positive;
- all coprime rectangle holonomies vanish in the regular dilation;
- finite translate kernels are compatible under inclusion;
- no norm-zero sequence with nonzero algebraic Weil class appears at completion.

## Strongest falsification attempt

Compute the complete normalized transfers on one fixed short-support block and evaluate the mixed-prime defect

`Delta_(2,3)=I-C_2* C_2-C_3* C_3+(C_2 C_3)*(C_2 C_3)`.

This is the two-generator Brehmer defect for the declared forward-transfer convention. A negative direction disproves the conjecture before any global limit. If this passes, test equality of the two paths to the grade-six translate and then search for a finite-core sequence whose local Weil norm tends to zero while its algebraic quotient class remains nonzero.

## Disposition

Rejected as stated. A unitary three-cycle compressed to one orbit vector is minimal, regular, and injective but has `C_1=C_2=0` and `C_3=I`, so compression does not inherit semigroup composition. The surviving replacement requires a minimal faithful regular **coextension** with joint coinvariance of the local block, plus the Weil coefficient identity and radical-stable dense completion.

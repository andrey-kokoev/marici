# Physical archimedean cutoff entries: rigorous off-diagonal enclosures

## Result

The actual spatial/Fourier cutoff pair is now evaluated in one concrete sector: the real archimedean even sector. All20 off-diagonal entries of the declared five-packet matrix have rigorous analytic enclosures at Lambda=2,4,8. No numerical quadrature or synthetic cutoff matrices are used.

The common diagonal, its finite-part subtraction, other semilocal sectors and the full analytical filler remain open. These are bounds on physical operator entries, not claimed exact numerical values.

## Carrier, normalization and actual regulator

Work on `H=L2(R_+,dx)`, equivalent to the even subspace of `L2(R,dx)`. The additive Fourier transform there is the unitary cosine transform

    C f(x) = 2 integral_0^infinity cos(2 pi x xi) f(xi) dxi.

Set

    P_Lambda = 1_(0,Lambda],
    Q_Lambda = C P_Lambda C*,
    Z_R = P_R, R>=Lambda.

These are the physical cutoff operators, not a convenient symmetric Mellin window. The correctly cycled regulated trace contains `Z_R^2 P_Lambda=P_Lambda`; no commutation with an observer is needed.

Use explicitly normalized dilations

    U_t f(x)=t^(-1/2) f(x/t),
    A_j=integral p_j(log t) U_t dt/t.

Under the unitary logarithmic coordinate map `f(x)->exp(u/2)f(exp u)`, U_t is translation. Thus A_j's multiplier is exactly the declared Mellin/Fourier transform of p_j.

There is an important normalization distinction in source formulas: bare dilation `V_t f(x)=f(x/t)` is not unitary on this dx carrier. Our same A_j is equivalently

    A_j=integral f_j(t) V_t dt/t,
    f_j(t)=t^(-1/2)p_j(log t).

This is precisely the candidate's physical half-density. The half-density factor cannot be omitted when moving between bare and unitary dilation conventions. Their convolution involutions must be transported with it.

## Continuum kernel derivation

Let

    k_Lambda(s)=sin(2 pi Lambda s)/(pi s),

with its continuous value at zero. The cosine cutoff has kernel

    Q_Lambda(x,y)=k_Lambda(x-y)+k_Lambda(x+y).

The kernel of U_r is `sqrt(r) delta(y-r z)`. Therefore, integrating the diagonal over0<x<=Lambda,

    Tr(P_Lambda Q_Lambda U_r)
      = K_Lambda(r)
      = sqrt(r)/pi * [Si(2 pi Lambda^2(1-r))/(1-r)
                     +Si(2 pi Lambda^2(1+r))/(1+r)].

The apparent singularity at r=1 is removable at finite Lambda, but its large-Lambda asymptotics are not uniform there.

These traces are ordinary finite traces. One justification is the absolutely summable rank-one Taylor expansion of the Fourier kernel on a bounded spatial interval and bounded frequency interval: `P_Lambda Q_Lambda` is trace class. Multiplication by a unitary dilation preserves trace class, and integration against the compact L1 observer amplitudes preserves the trace identity.

For the real packet basis,

    T_ij(Lambda)=Tr(Z_R P_Lambda Q_Lambda A_i A_j* Z_R)
      = double integral p_i(u) p_j(v) K_Lambda(exp(u-v)) du dv.

The matrix is Toeplitz because `A_j=U_(4^j) A_0`, and all scaling-convolution observers commute with dilations. This does not imply finite-cutoff Hermiticity: ordered entries i,j and j,i are bounded separately.

## Inversion reference and volume term

Retain the reflection in the reference explicitly:

    J_0 f(x)=x^(-1) f(1/x),
    Q_Lambda^0=J_0 P_Lambda J_0=1_[Lambda^(-1),infinity).

The reference overlap is the physical annulus `[Lambda^-1,Lambda]`, hence

    Tr(P_Lambda Q_Lambda^0 A_i A_j*)
      = 2 log(Lambda) integral p_i(u) p_j(u) du.

Distinct translated packet supports are disjoint. Thus every off-diagonal reference/volume entry is exactly zero. The bounds below are consequently also bounds on the off-diagonal physical/reference difference for this explicitly defined inversion reference. No unproved same-polarization Hardy shortcut is used.

## Rigorous bounds without quadrature

For x!=0, integration by parts gives

    |Si(x)-sign(x) pi/2| <= 2/|x|.

Away from r=1,

    K_infinity(r)=sqrt(r)/2 * [1/|1-r|+1/(1+r)],
    |K_Lambda(r)-K_infinity(r)|
      <= sqrt(r)/(pi^2 Lambda^2)
         *[(1-r)^(-2)+(1+r)^(-2)].

K_infinity is invariant under r->1/r. For0<r<1 it equals `sqrt(r)/(1-r^2)`, which is strictly increasing.

For i<j, put d=j-i. The packet support gives

    r in [1/(2*4^d), 2/4^d], d=1,...,4.

The reverse entry uses the reciprocal interval. These supports are separated from1. Both orders therefore converge to the same limiting entry with explicit O(Lambda^-2) errors; their finite ordered difference is bounded by the sum of those errors, not set to zero.

For the packet's unknown positive normalization, put `c=integral phi/A`. Evenness and the support radius imply

    1 <= A/integral phi <= cosh(log2/4) < 11/10,
    10/11 < c <= 1.

The last rational bound follows from `(6/5)^4>2` and `2^(-1/4)<1`. Consequently the limiting packet entry lies between the minimum kernel times `(10/11)^2` and its maximum kernel. The checker encloses square roots by exact integer arithmetic and uses pi>3 for the error bound.

All60 reported finite enclosures are strictly positive. Subtracting the already evaluated endpoint entry `2^d+2^-d` gives a strictly negative enclosure. This subtraction is a defined difference—not a proof that the remainder equals the entire intended regular or mixed polarization.

## Excluded shortcut

For the diagonal, r ranges across1. The off-diagonal bound is rejected there. The five diagonal entries coincide, but their one common centered finite part still requires a separate calculation. Neither a convenient point value nor the off-diagonal limit can supply it.

## Reproduce and next task

```sh
python research/strominger/checkers/check_archimedean_cutoff_entry.py
```

The checker verifies rational enclosure arithmetic, support separation, live input hashes and claim boundaries. The continuum derivation above supplies the analytic justification; this is not a proof-assistant certification of that derivation.

- [Frozen physical sector and normalization](contracts/archimedean-cutoff-entry.v1.json).
- [All60 finite enclosures and limiting/error bounds](results/archimedean-cutoff-entry.json).
- [Verification receipt](results/archimedean-cutoff-entry-verification.json).

Next evaluate the common diagonal with its actual volume counterterm and control the centered limit, then compare the resulting packet form with the retained analytical witnesses. Do not promote this one-sector, off-diagonal calculation to all semilocal data, native implementation of a complete cutoff observable, or the114-record construction.

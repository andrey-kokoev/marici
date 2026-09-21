# Clark sewing to the endpoint–gamma–prime Green kernel

## Result

The full sewn source form B+R from the preceding computation has an explicit arithmetic expression. Its elementary completed terms give exactly the two-endpoint swap pairing; its remaining terms are the gamma logarithmic derivative and the Euler prime-power current. This establishes a signed scalar-kernel crosswalk on the common Euler chart and by meromorphic continuation.

It does not establish equivalence of completed operator domains or a positive Gram representation. Those strengths exceed equality of the polarized scalar kernels.

## 1. Frozen spectral and normalization conventions

Set s_z=1/2-i z and X(z)=xi(s_z). Define E=X+iX' and E_star=X-iX', where the prime is differentiation in z. X is real entire in z under the completed functional equation and conjugation conventions.

Use

K(w,z)=[conjugate(E(w))E(z)-conjugate(E_star(w))E_star(z)]/[-i(z-conjugate(w))].

This is the preceding packet's kernel convention; a de Branges convention with 2 pi in the denominator multiplies everything here by 1/(2 pi). Any different constant normalization of the theta transform multiplies K by the squared modulus of that constant.

Expanding E gives

K(w,z)=2 conjugate(X(w))X(z)
 [m(z)-conjugate(m(w))]/[z-conjugate(w)],

m=-X'/X=i L(s_z), L(s)=xi'(s)/xi(s).

Because s_z+conjugate(s_w)-1=-i(z-conjugate(w)), this becomes

K(w,z)=2 conjugate(X(w))X(z)
 [L(s_z)+conjugate(L(s_w))]/[s_z+conjugate(s_w)-1].

The logarithmic expression is first taken away from zeros. Multiplication by the displayed X factors and continuation recover the original entire numerator with its removable divided differences.

## 2. Arithmetic expansion on the Euler chart

For Re s>1,

L(s)=1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2)-sum_(n>=2) Lambda(n)n^(-s).

Let s=s_z, t=conjugate(s_w), and d=s+t-1. Then

K=2 conjugate(X(w))X(z) [K_end(s,t)+K_gamma(s,t)+K_prime(s,t)],

K_gamma=[-log pi+(psi(s/2)+psi(t/2))/2]/d,

K_prime=-sum_(n>=2) Lambda(n)[n^(-s)+n^(-t)]/d.

The prime sum is absolutely convergent on this chart. It includes prime powers with their von Mangoldt coefficients. Outside this chart the logarithmic derivative supplies the continuation; the raw Dirichlet sum is not claimed convergent there.

## 3. The endpoint attachment is the swap form

A rational identity gives

[1/s+1/(s-1)+1/t+1/(t-1)]/[s+t-1]
 =1/[s(t-1)]+1/[(s-1)t].

Therefore

K_end(s,t)=a(s)b(t)+b(s)a(t),

a(s)=1/s, b(s)=1/(s-1).

On the endpoint vector (a,b), this is precisely the matrix [[0,1],[1,0]]. Passing to parity coordinates e=(a+b)/sqrt(2), o=(a-b)/sqrt(2) yields

K_end(s,t)=e(s)e(t)-o(s)o(t).

Thus the independent endpoint swap signature appears with its exact sign and normalization in the sewn Clark kernel. The negative odd endpoint square is retained in the formula.

## 4. Identifying the full source row

The preceding tail calculation proves K=(B+R)/[-i(z-conjugate(w))], with

R(w,z)=2i integral_0^infinity A(d)[sin(conjugate(w)d)-sin(zd)]dd,

A(d)=integral_0^infinity (x+d)Phi(x)Phi(x+d)dx.

Combining the two derivations gives an explicit equality between this full source-polarized expression and the endpoint–gamma–prime formula above, provided Phi is normalized to the declared X.

Individual assignments R=prime or B=gamma have not been derived. The identity compares their complete sum. Splitting the source forcing reservoir into placewise arithmetic channels is stronger and needs its own source-level construction.

## 5. Positive attachment obligation in these coordinates

For a finite spectral packet away from the removable singularities, the diagonal X factors act by a diagonal congruence. The signed endpoint–gamma–prime matrix must be tested on the same coefficient packet. In endpoint parity coordinates its positive-completion inequality has the explicit shape

K_gamma+K_prime+e e* >= o o*.

Every term is now specified on the Euler chart. The inequality is a positive-semidefinite matrix statement for arbitrary finite spectral packets, not a pointwise comparison of scalar diagonal values. Continuation of the signed identity does not establish continuation of this inequality.

This recovers the prior odd-endpoint leverage problem in the exact normalization of the current Clark construction. It identifies the arithmetic form being compared without introducing a new operator family.

## 6. Numerical and exact checks

`uv run --with sympy --with mpmath python research/grothendieck/checkers/check_clark_arithmetic_green_crosswalk.py`

The endpoint swap identity is checked exactly by symbolic rational algebra. Two complex/real Euler-chart fixtures compare the direct xi Clark kernel with its full logarithmic-derivative expression at 60-digit precision.

The prime series is truncated at N=2000. Since Lambda(n)<=log n and log(x)x^(-sigma) decreases beyond this cutoff, the absolute tail is bounded by

N^(1-sigma)[log N/(sigma-1)+1/(sigma-1)^2].

Both observed errors lie below the propagated two-source tail bound. These are numerical regression checks with an analytic truncation bound, not interval-certified evaluation of every special function or a positivity certificate.

## Status

Constructed: explicit signed crosswalk of the sewn theta kernel to the elementary endpoint swap, gamma term, and prime-power current.

Open: operator/domain identification at completion, prime-resolved realization of the mixed source row, and the full finite-packet odd-endpoint domination inequality. The crosswalk supplies the actual arithmetic entries for that next test.

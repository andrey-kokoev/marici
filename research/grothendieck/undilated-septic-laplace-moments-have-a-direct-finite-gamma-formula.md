# Undilated septic Laplace moments have a direct finite gamma formula

## Kernel to rebuild

For the coherent `c=1` repair, each archimedean term needs

`I_b(phi_a)=integral_0^infinity phi_a(x)e^(-b x)dx`,

where `b=n+1/4` and

`phi_a(x)=sum_m c_m k_7(x+m a)`.

No `x/2` substitution is present.

## One truncated-power cell

Write

`k_7(u)=1/7! sum_(j=0)^8 (-1)^j binom(8,j)(u+4-j)_+^7`.

For

`s=m a+4-j`,

the cell integral is

`J_b(s)=1/7! integral_0^infinity (x+s)_+^7 e^(-b x)dx`.

Changing variable `y=x+s` gives

`J_b(s)=e^(b s)/7! integral_(max(s,0))^infinity y^7e^(-b y)dy`

`=e^(b s)/(7! b^8) Gamma(8,b max(s,0))`.

Since the shape is the integer eight,

`Gamma(8,z)=7! e^(-z) sum_(r=0)^7 z^r/r!`.

Therefore every cell reduces to a finite polynomial and one exponential interval:

`J_b(s)=e^(b(s-max(s,0))) b^(-8)`

`*sum_(r=0)^7 (b max(s,0))^r/r!`.

The complete moment is

`I_b(phi_a)=sum_(m,j)c_m(-1)^j binom(8,j)J_b(m a+4-j)`.

## Exact exponential structure at a=2 log 2

For `b=n+1/4`, shift exponentials satisfy

`e^(b m a)=2^(2mn+m/2)`.

Thus they use integer powers of two and the already available directed square-root interval for two. Knot exponentials `e^(b(4-j))` use quarter-integer exponents and can be assembled from directed intervals for `e^(1/4)` or by the existing exponential routine.

## Jets and tail

The undilated zero jets are

`phi_a^(r)(0)=sum_m c_m k_7^(r)(m a)`

with no factor `2^(-r)`. The Euler--Maclaurin/Hurwitz tail should then be regenerated from these jets. The signed atomic eighth-derivative remainder retains atoms at

`x=2(j-4-m a)`

only in the old dilated variable; for `c=1` the physical atom locations are instead

`x=j-4-m a` up to the fixed translation orientation. Reusing the old atom code is prohibited.

## Acceptance tests

1. Enclose the direct high-precision quadrature values for baseline and lag-one cross.
2. Deliberately insert the old factor two and require disjoint intervals.
3. Verify the support-derived prime cutoff independently.
4. Recompute pole annihilation before omitting pole cells.

## Disposition

The unavailable `d` retuning is unnecessary. The undilated kernel has a direct finite incomplete-gamma formula suitable for rational interval implementation.

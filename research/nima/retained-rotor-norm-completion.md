# Norm completion of the selected rotor packet

Active SCC obligations: completion, comparison sewing and noncollapse. This
leaf completes the specific rational rotor series from the preceding formal
construction. It does not evaluate the entire formal-series ring at real time.
The Clifford product and norm remain declared realization data; native admission
is the separate open owner handoff.

## The completion is specified

On the rational even plane a+bJ, use the reversion norm squared a^2+b^2.
Its Archimedean metric completion is the completed even coefficient plane.
For estimates, the rational coefficient bound |a|+|b| dominates that norm.
Multiplication on the even plane is norm-multiplicative, and multiplication by
any signed source unit preserves the reversion norm. Complete only the
coefficient-sequence coordinate of a packet (history, signed center, sequence).
The Cauchy equivalence requires equality of the history and center labels as
well as a coefficient difference tending to zero. Thus neither label is
quotiented merely because endpoint matrices agree.

This metric completion is different from the x-adic inverse limit of formal
jets. The evaluated objects below are actual partial-sum polynomials over the
rationals, not ring evaluations of nilpotent quotient classes.

## Explicit all-order tails

Let P_N(x) be the degree-N polynomial with the previously constructed
coefficients J^n/n!. For rational R>=0 and N+2>R define

\[
B_N(R)=\frac{R^{N+1}}{(N+1)!}
\frac{1}{1-R/(N+2)}.
\]

For every later term its ratio to the preceding term is at most R/(N+2).
The geometric majorant therefore gives, uniformly for |x|<=R,

\[
\sum_{n>N}\frac{|x|^n}{n!}\leq B_N(R),
\qquad \|E(x)-P_N(x)\|\leq B_N(R).
\]

For fixed R this bound tends to zero. It constructs a unique selected limit in
the declared norm completion. Finite polynomial difference bounds supply a
uniform local Lipschitz majorant given by the convergent scalar factorial sum.
This extends the construction from rational parameters to their real completion
before using differentiation of the real limit.

Because P_N'=J*P_(N-1), the derivative tail is B_(N-1)(R), when N+1>R.
Uniform derivative convergence on compact intervals gives E'=J*E. Absolute
convergence permits the coefficient Cauchy product, so the formal coefficient
identities now imply ACTUAL completed identities

\[
E(x)E(y)=E(x+y),\qquad E(-x)=E(x)^\top=E(x)^{-1}.
\]

The group law gives norm one and the derivative then has norm one. Thus

\[
\|E(x)-E(y)\|\leq |x-y|.
\]

These deductions occur after the completion proof; they are not assumptions
used to replace the formal series by a trigonometric function.

## Transport and numerical defects are controlled

For signed centers g,h and orientation o(g), the completed charts obey

\[
(E(x)g)(E(y)h)=E(x+o(g)y)gh.
\]

The finite polynomial approximants need not obey this exactly. Writing
b_x=B_N(|x|), and similarly for y and x+o(g)y, their defect is bounded by

\[
b_x+b_y+b_xb_y+b_{x+o(g)y}.
\]

The checker compares squared reversion norms with the square of this rational
bound for all 64 signed-center pairs at its sampled rational parameters.
It also checks orthogonality defects, derivative defects and Cauchy blocks.
No normalization is applied to hide a finite-cutoff defect.

## The clock boundary is handled without an invalid derivative limit

On 0<=t<=1 the clock partial sums are

\[
\ell_M(t)=2\sum_{n=0}^M\frac{(-1)^n t^{2n+1}}{2n+1}.
\]

The alternating terms decrease, giving the UNIFORM value bound

\[
|\ell(t)-\ell_M(t)|\leq\frac{2t^{2M+3}}{2M+3}.
\]

The rational integral kernel provides the same limit:

\[
\ell(t)=2\int_0^t\frac{du}{1+u^2}.
\]

This follows by integrating the finite geometric sum and bounding its remainder.
It proves strict increase and continuity up to t=1. Differentiation of the
series is justified locally inside |t|<1, not at its boundary: ell_M'(1)
alternates between 2 and 0, while the rational kernel has value 1 there.
The checker retains this failure as a negative control.

For 0<=t<1, the completed E(ell(t)) and the rational Cayley matrix V(t) satisfy
the same linear ODE and initial condition, so they agree. Continuity extends
the equality to t=1; no termwise boundary differentiation is used.

## Recover the actual finite witnesses

Define a as the completed clock value ell(1), without inserting a numerical
value of pi. The preceding construction gives

\[
E(a)=J,\qquad E(2a)=-1,\qquad E(4a)=1.
\]

On 0<t<1 the Cayley scalar and J coefficients are both positive, so this
parameter interval covers the open first quadrant. The group law supplies the
other three quadrants. Consequently 4a is the least positive lift period;
2a is the adjoint period. In the conventional radian notation a is pi/2, but
that number was not an input to the construction or numerical checker.

There is also an explicit rational certificate. Set a_M=ell_M(1); then
4/3<=a_M<=2. For k=1,2,3,4,

\[
\|P_N(k a_M)-J^k\|
\leq B_N(2k)+\frac{2k}{2M+3}.
\]

The right side can be made arbitrarily small by increasing BOTH cutoffs. At a
fixed clock cutoff its remaining error does not disappear merely by increasing
the rotor order. Exact rational checks verify these bounds at 32 cutoff/return
combinations, without floating-point trigonometry.

The separation between J and -J, and between 1 and -1, still has squared norm
four. The return at 4a does not identify its retained history with the empty
history. The completion therefore preserves the tested lift distinction while
remaining a many-to-one reading of complete source records.

## Outcome and remaining gate

The selected rational packet now has a continuous, differentiable realization
in the declared norm completion; its generator, all signed chart comparisons,
and finite retained returns are controlled. This removes the need to assume a
real exponential for THIS packet. It does not select the norm/product from the
native source, authorize an active physical evolution, or calibrate time.

The next existing frontier is the owner-directed native Cayley-admission
handoff. Its exact product/readout question remains unchanged by convergence:
V(1/2) still fails the unchanged pointwise source product. No silent promotion
from analytic existence to source admission is permitted.

Verification:

```text
python research/aspect/scc/scc.py check nima-retained-rotor-norm-completion
```

`checkers/check_retained_rotor_norm_completion.py` uses exact rational
arithmetic for all finite certificates. The all-order analytic proof is the
geometric-majorant and continuity argument above, not a fresh Agda
formalization of real analysis. The actual rational coefficient proof from the
preceding leaf is retained and hash-checked. Receipt:
`results/retained-rotor-norm-completion.json`.

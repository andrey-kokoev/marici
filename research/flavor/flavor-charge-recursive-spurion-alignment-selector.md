# Charge-Recursive Spurion Potential Selects the Equal-VEV Orbit

## Question

Can the two-dimensional VEV-alignment fiber of WP848 be removed by a source
potential whose minima do not depend on tuned coefficient ratios?

## Gauge-invariant positive potential

Let (s_j) have (U(1)) weight (-j), let (v>0), and take positive
coefficients (lambda_1,lambda_2,lambda_3). Define

\[
\begin{aligned}
V={}&\lambda_1(|s_1|^2-v^2)^2\\
&+\lambda_2v^2\left|s_2-\frac{s_1^2}{v}\right|^2\\
&+\lambda_3v^2\left|s_3-\frac{s_1s_2}{v}\right|^2.
\end{aligned}
\]

Every term is gauge invariant: (s_2) and (s_1^2) have weight (-2),
while (s_3) and (s_1s_2) have weight (-3). With dimension-one scalar
fields, the displayed factors make every term dimension four.

## Unique zero orbit

Because all coefficients are positive, the global minimum is zero exactly
when

\[
|s_1|=v,
\qquad
s_2=\frac{s_1^2}{v},
\qquad
s_3=\frac{s_1^3}{v^2}.
\]

Writing (s_1=ve^{-i\theta}) gives

\[
(s_1,s_2,s_3)
=v(e^{-i\theta},e^{-2i\theta},e^{-3i\theta}).
\]

This is one (U(1)) orbit. Gauge fixing \(\theta=0\) gives the unique
representative

\[
s_1=s_2=s_3=v.
\]

The zero locus is independent of the numerical positive
(lambda_i). Hence the alignment is coefficient-robust.

## Local stability and recovered ray

For real gauge-fixed variables (u_i=s_i/v), the three constraints have
Jacobian at (u=(1,1,1))

\[
J=
\begin{pmatrix}
2&0&0\\
-2&1&0\\
-1&-1&1
\end{pmatrix}.
\]

The Hessian of the unit-weighted sum of squares is (2J^TJ), which is
positive definite. Positive (lambda_i) preserve positive definiteness.

Substitution into WP848's kernel gives

\[
k(s)=v^2(1,2,3)^T.
\]

The dimensionful scale cancels from the projective ray. Thus this potential
genuinely selects the desired spurion alignment and primitive kernel direction
inside the declared charged-spurion model.

## Remaining authority boundaries

The result is conditional on admitting this particular potential. The charge
recursion makes its form natural and hard to vary, but no prior topological or
microscopic theorem currently forces these three squares or excludes other
gauge-invariant terms that move the vacuum.

It also does not repair WP848's groupoid change: the nonzero VEV orbit has
trivial stabilizer. Representation-valued threshold memory must therefore be
transported by an independently derived defect or equivariant index across
symmetry breaking. The diameter-normalized beta law, finite matching, and
holonomy-resolved `physical16` instrument remain separate gates.

## Disposition

Progressive conditional source selector. For every positive coefficient
packet, the charge-recursive potential uniquely selects the equal-VEV gauge
orbit, has a stable gauge-fixed minimum, and recovers the primitive ray
without fixing it by coefficient ratios. Source authority for the potential,
RG completion, threshold character transport, and physical instrumentation
remain open.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp849_charge_recursive_spurion_alignment_selector.py
```

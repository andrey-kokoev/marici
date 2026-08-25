# Kernel birth at completion depends on weak, strong, and distributional topology

## 1. Two closures of finite atomic packets

Let `A_fin` be the finite signed atomic measures on `S^2`.

Its total-variation closure is the space of countably atomic measures with
absolutely summable weights. It does not contain a nonzero smooth density. If
`mu_n` is atomic and `rho dOmega` is nonatomic with equal total mass, their
supports are mutually singular and the variation norm of the difference does
not tend to zero.

By contrast,

\[
 \overline{\mathcal A_{\rm fin}}^{w^*}=\mathcal M(S^2).
\]

Quadrature and empirical packets can therefore converge weak-* to the smooth
hard fluxes that construct the `l=2,3,4` kernel. The physical kernel is born in
the weak-* continuum completion, not in the total-variation atomic completion.

## 2. Continuity of the source/readout pipeline

Weak-* convergence of uniformly bounded measures implies distributional
convergence. Differential operators are continuous on `D'`, and the normalized
sphere Green pseudoinverse is continuous between the corresponding Sobolev or
distribution scales after its finite zero modes are removed. Hence

\[
 \mu_N\to\mu\quad\Longrightarrow\quad
 \mathcal A_3\mathcal G\mu_N
 \to\mathcal A_3\mathcal G\mu.
\]

If `mu` is a low harmonic source, the right side is zero even though every
finite atomic `mu_N` has a nonzero local response. The responses converge to
zero distributionally. Injectivity on the dense finite subset is not bounded
below in the weak topology.

The Fredholm estimate explains the limit: after removing the low kernel, a
small output forces the source/shear to approach that kernel.

## 3. Accumulating atoms

A fixed countable packet

\[
 \sum_i e_i\delta_{\xi_i},\qquad \sum_i|e_i|<\infty,
\]

defines a finite measure even if the punctures accumulate. Its singular
support may be infinite, but it remains in the total-variation atomic closure.
It cannot equal a nonzero smooth low harmonic density, so it does not become
an exact low-mode kernel merely through spatial accumulation.

Non-absolutely-summable weights do not define a finite signed measure without
additional conditional summation authority.

## 4. Collision jets require stronger topology

Derivative delta functions arise from rescaled signed collisions:

\[
 \frac{\delta_{\epsilon}-\delta_0}{\epsilon}
 \longrightarrow-\partial_x\delta_0
\]

distributionally. Their total variation grows as `2/|epsilon|`. More generally,
an order-`k` collision jet requires weights of size `epsilon^{-k}` and leaves
every bounded-total-variation set.

For the nonuniform stencil,

\[
 \epsilon^{-2}
 (\delta_0-3\delta_\epsilon+2\delta_{3\epsilon/2})
 \longrightarrow\frac34\partial_x^2\delta_0.
\]

Thus `(1,-3,2)` is a distributional blow-up coordinate. It is not a bounded
measure completion and cannot silently enter a finite-flux source category.

## 5. Infinite jet order

The order-`k` point jet belongs to `H^{-s}` only for `s>k+1`. No fixed
negative Sobolev space contains all orders. An infinite formal jet belongs to
the product dual of the LF jet space, not to its LF union, and generally not
to `D'` unless its coefficients satisfy a finite-order continuity bound.

Therefore there are three distinct enlargement events:

- weak-* continuum flux: admits smooth low-mode kernels;
- distributional collision blow-up: admits finite higher jets with norm blow-up;
- formal infinite-jet product: usually not a distribution and remains
  unauthorized.

## 6. Stable-limit law

| limiting regime | exact new kernel class |
|---|---|
| bounded TV, countably atomic | none beyond atomic packet theorem |
| weak-* Radon closure | smooth `l=2,3,4` source kernel appears |
| strong Sobolev completion | same closed finite-dimensional low kernel |
| distributional collision scaling | finite jet records, still detected by paired grade three unless low-smooth |
| infinite formal product | not source-authorized |

## Evidence

`checkers/accumulation_infinite_collision_checks.py` verifies `l1` convergence,
the atomic/nonatomic variation obstruction, exact weak moment recovery,
first- and second-jet collision limits with norm divergence, Sobolev order
escape, and spectral approach to the low kernel.

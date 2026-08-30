# Spacelike threshold context: WP691

## Why momentum can be a physical context

WP690 showed that renormalization-scale variation is not an experiment. A
physical momentum transfer is different: it labels externally prepared and
measured kinematics. However, two momentum bins are complementary only if the
source response retains a nonlocal momentum dependence.

The smallest exact threshold model is the equal-mass, once-subtracted
Euclidean two-propagator kernel

\[
\Phi(z)=\int_0^1\log(1+z x(1-x))\,dx,
\qquad z=Q^2/M^2\geq0.
\]

Its derivative is

\[
\Phi'(z)=\int_0^1
\frac{x(1-x)}{1+z x(1-x)}\,dx>0.
\]

Thus distinct spacelike momenta give distinct kernel values. For a response

\[
R(Q)=a+b\Phi(Q^2/M^2),
\]

the two-bin Jacobian with respect to \((a,b)\) has determinant

\[
\Phi(Q_2^2/M^2)-\Phi(Q_1^2/M^2),
\]

which is nonzero when \(Q_1\ne Q_2\). The boundary contribution \(a\) drops
out of the bin difference.

## Hostile local limit

If the heavy messenger is replaced by a strictly local portal coefficient,
the response is momentum independent and every bin lies in one contextual
equivalence class. The two-bin Jacobian then has rank one. Consequently the
nonlocal threshold shape, not a change of renormalization convention, is the
information-bearing operation.

## Authority boundary

The kernel above is the minimal equal-mass two-propagator threshold model. It
does not stand in for the complete messenger-induced Higgs/exit-flavon
four-point function, which depends on the Mandelstam variables and source
tensor contractions. Nor is the exit flavon presently bound to a calibrated
detector final state.

WP691 therefore establishes a physical-context rank mechanism and its exact
falsifier, not a flavor selector or physical instrument. The next constructor
must derive the complete four-point form factor, identify an observable final
state, and propagate it through two calibrated kinematic bins.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp691_spacelike_threshold_context.py

Generated result: results/wp691_spacelike_threshold_context.json.

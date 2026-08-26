# Mediator-mass threshold knob (WP368)

## Bounded constructor

Replace WP367's direct quartic intervention by a heavy real mediator \(S\)
with controlled positive mass-squared

\[
L(\epsilon)=L+k\epsilon,
\qquad L>0,quad \mu k\ne0,
\]

and source potential terms

\[
V_S=\frac{L(\epsilon)}2S^2+\frac\mu2St^2.
\]

For canonically normalized four-dimensional scalars, \(St^2\) is a
superrenormalizable interaction. The mediator equation gives

\[
S_\star=-\frac{\mu t^2}{2L(\epsilon)}.
\]

Substitution produces

\[
\Delta V=-\frac{\mu^2}{8L(\epsilon)}t^4,
\qquad
U_{\mathrm{eff}}(\epsilon)
=U_0-\frac{\mu^2}{2L(\epsilon)}.
\]

Thus the threshold-mass control induces the WP367 quartic response

\[
h_{\mathrm{eff}}
=\left.\frac{dU_{\mathrm{eff}}}{d\epsilon}\right|_0
=\frac{\mu^2k}{2L^2}.
\]

## Common response and deletion

On the conditional portal shell,

\[
y=-\frac1{U_{\mathrm{eff}}},
\qquad
x=J^2=\alpha y.
\]

The induced responses satisfy

\[
q=\frac{h_{\mathrm{eff}}}{U_{\mathrm{eff}}(0)^2},
\qquad
p=\alpha q,
\qquad
\frac pq=\alpha.
\]

Deleting the mediator coupling by setting \(\mu=0\), or deleting the control
by setting \(k=0\), kills both responses. Taking \(L\) to infinity restores
\(U_0\) and sends the intervention strength to zero. The constructor therefore
has an exact causal deletion test and decoupling limit.

## Physical boundary

This is a concrete tree-level threshold constructor for the common
perturbation. It does not yet provide a laboratory knob. Such a knob requires
a physical background or control field that changes \(L\) without introducing
untracked direct changes in the flavor portal. Finite mediator width, mixing,
loop matching, wave-function renormalization, stability of the complete
potential, and detector resolution remain outside the tree-level packet.

The operation is source-derived conditional on the displayed mediator action
and descends because the mediator is a weak-basis singlet and the flavor port
is \(J^2\). It still measures \(\alpha\) rather than selecting it and leaves
the fifteen CP-even `physical16` directions unresolved.

The smallest exact falsifier is \(\mu=0\), which removes the threshold shift
and both responses. The remaining instrument gate is a calibrated physical
control of the mediator pole mass together with a finite-width threshold
measurement of both relational ports.

Run `uv run --with sympy python
research/flavor/checkers/wp368_mediator_mass_threshold_knob.py` to regenerate
the exact result.

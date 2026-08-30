# Target-coded invariant potential (WP301)

## Candidate source selector

On a local weak-basis-invariant `physical16` slice, consider

\[
V(x)=\frac12x^TAx-b^Tx,
\qquad A>0.
\]

This action descends to the quotient when $x$ consists of declared physical
invariants. Its unique global minimum is

\[
x_*=A^{-1}b.
\]

It is therefore a genuine mathematical point selector once $A$ and $b$
are fixed.

## Authority inversion

The selector equation can be inverted:

\[
b=Ax_*.
\]

Thus an arbitrary desired point can be installed by choosing the linear source
after the target is known. The exact hostile pair holds
$A=\operatorname{diag}(2,3)$ fixed. Sources $b=(2,6)$ and $b=(4,3)$ select
$(1,2)$ and $(2,1)$,
respectively. Convexity rigidifies the minimum but does not authorize its
numerical location.

## Classification

This operation is a quotient-descending point selector if its coefficients are
derived independently from flavor-source fields, symmetries, normalization,
and matching. If $b$ is fitted from the desired `physical16` point, it is an
answer-coded selector and carries no predictive authority.

The next gate is therefore coefficient provenance, not another minimization
calculation. A progressive UV constructor must produce $A$ and $b$ before
flavor readout and survive stability, RG, threshold, and instrument tests.

Run `uv run --with sympy python
research/flavor/checkers/wp301_target_coded_invariant_potential.py` to
regenerate the exact authority audit.

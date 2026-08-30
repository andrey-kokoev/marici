# Dissipative preparation resource bound (WP273)

## Unique-vacuum dynamics

Write \(z\) for deviation from a proposed unique flavor vacuum and take

\[
\frac{dz}{dt}=-\gamma z,
\qquad
z(t)=A e^{-\gamma t}.
\]

At every finite time, the derivative with respect to the initial amplitude is
\(e^{-\gamma t}>0\). The map remains injective and is not an exact finite-time
selector.

Operational preparation within tolerance \(\epsilon\) is possible on a bounded
initial domain \(|A|\leq A_{\max}\). The required runtime is

\[
T\geq\frac{1}{\gamma}
\log\frac{A_{\max}}{\epsilon}.
\]

This is a conditional approximate selector only after the domain, rate,
tolerance, and runtime are physically admitted.

## Exact bounded and hostile packets

For \(\gamma=1\), \(A_{\max}=10\), and \(\epsilon=1/100\), runtime
\(T=\log1000\) reaches the tolerance exactly. At the same runtime, amplitude
20 leaves residual \(1/50\) and fails the instrument contract.

More generally, for any finite runtime choose

\[
A=2\epsilon e^{\gamma T}.
\]

The terminal residual is then \(2\epsilon\). No finite runtime uniformly
prepares an unbounded amplitude domain.

## Classification

A unique dissipative vacuum supplies conditional approximate preparation, not
an exact finite-time selector. The first nonfaithful arrow is from asymptotic
uniqueness to uniform finite-resource preparation. A physical flavor
instrument must derive the initial-domain bound, damping rate, noise floor,
stopping rule, stabilization, and reset/degradation budget from one source.

Run `uv run --with sympy python
research/flavor/checkers/wp273_dissipative_preparation_resource_bound.py` for
the exact flow, injectivity, runtime bound, and unbounded-domain adversary.

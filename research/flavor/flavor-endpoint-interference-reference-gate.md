# Endpoint-interference reference gate: WP683

## Noncommuting source algebra

The full grammar contains a noncommuting operator after all. The entrance
projector

\[
P_A=\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]

does not commute with the balanced mass-mixing tensor

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

This algebraic fact does not by itself make the phase observable.

## Two-pole propagator

Writing (x) for the common inverse-propagator coordinate and (m) for real
mixing,

\[
(xI-mX)^{-1}=\frac{xI+mX}{x^2-m^2}.
\]

The cross-endpoint amplitude is

\[
G_{AB}=\frac{m}{x^2-m^2}.
\]

It changes sign under (m\to-m), but its isolated probability does not. For
complex Hermitian mixing, the isolated rate depends only on (|m|^2). Pole
interference inside this single transition therefore does not supply a phase
reference.

## Missing constructor

If an independently normalized amplitude (r) reached the same external
state, coherent interference would produce a sign-odd difference proportional
to

\[
\frac{4mr}{x^2-m^2}.
\]

No such direct (QH\to Xq) reference amplitude is admitted in the current
grammar. Algebraic noncommutation is therefore not executable phase control.

## Disposition

The endpoint algebra is promising but insufficient. The next admissible
constructor must generate a coherent amplitude into exactly the same external
channel, with independently fixed normalization and absorptive phase. Without
that object, the two-pole line shape remains phase nonfaithful.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp683_endpoint_interference_reference_gate.py

Generated result: results/wp683_endpoint_interference_reference_gate.json.

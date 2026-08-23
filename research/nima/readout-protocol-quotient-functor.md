# Readout protocols canonically generate their sufficient quotient objects

Let \(\mathcal R\) be a declared family of linear readouts on \(V\), and set

\[
K_{\mathcal R}=\bigcap_{r\in\mathcal R}\ker r,
\qquad
Q_{\mathcal R}=V/K_{\mathcal R}.
\]

If \(\mathcal R\subseteq\mathcal S\), then

\[
K_{\mathcal S}\subseteq K_{\mathcal R},
\]

so there is a canonical surjection

\[
Q_{\mathcal S}\twoheadrightarrow Q_{\mathcal R}.
\]

Identity and composition follow from quotient universality. Thus the poset of
readout protocols generates a contravariant diagram of minimal sufficient
objects:

\[
Q_{(-)}:\operatorname{Readout}(V)^{\rm op}longrightarrow
\operatorname{Quot}(V).
\]

Adding a required readout refines the sufficient object; forgetting a readout
canonically coarsens it. No external choice of complement is involved.

## D12 control

Each of the Bell and transfer readouts on the two-dimensional QED coefficient
plane has a one-dimensional sufficient quotient. Their kernels are distinct.
The joint protocol has zero kernel and therefore generates the full
two-dimensional plane, with canonical surjections to both one-readout
quotients.

This is a small exact model of recursive action authority: the operational
requirements determine the object on which they can be faithfully realized,
and changes in those requirements generate canonical transformations among
the resulting objects. It does not prove that every Marici support or
coherence rule arises this way.

## Nonlinear and derived frontier

For general sectors, readouts are supported functors rather than linear
functionals. The required replacement is the effective quotient by their
joint kernel pair, retained with connection, support, and physical-chain
coherence. The construction fails if those kernel pairs do not admit a common
effective quotient or if protocol transport does not preserve their typing.

Artifacts:

- `research/nima/checkers/check_readout_protocol_quotient_functor.py`
- `research/nima/results/readout_protocol_quotient_functor.json`

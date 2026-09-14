# The retained joint graph forces local primitive-square Schwarz but not the Weil gate

## Existing common carrier

The retained G1 architecture already constructs, for each prime-labelled strict primitive/square packet,

\[
E_{p,12}=\mathbb Ce_{p,1}\oplus\mathbb Ce_{p,2}
\]

and retains its common labelled source through the closed joint graph

\[
x\longmapsto(x,A_{p,12}x,C_{p,12}x).
\]

The recorded construction supplies:

- the source orientation \(S_{12}=\operatorname{diag}(-1,+1)\);
- primitive and square grade labels;
- continuous polarized forms on the common retained graph;
- zero radical;
- cutoff naturality;
- a uniform positive margin greater than \(0.244\).

Thus, inside this strict local analytic cell, primitive and primitive-square observations are genuinely realized in one positive carrier rather than supplied as unrelated scalars.

## Local rung-four consequence

Let \(\Phi_p(x)\) denote the retained-graph realization. Its observation square is a Gram square:

\[
S_p(x,y)=
\begin{pmatrix}
\langle\Phi_p(x),\Phi_p(x)\rangle&
\langle\Phi_p(x),\Phi_p(y)\rangle\\
\langle\Phi_p(y),\Phi_p(x)\rangle&
\langle\Phi_p(y),\Phi_p(y)\rangle
\end{pmatrix}.
\]

Consequently

\[
S_p(x,y)\succeq0
\]

and its Schwarz determinant is nonnegative. The intended principle is therefore valid on the constructed strict primitive/square analytic line:

> coexistence in the retained common positive carrier forces rung-four positivity.

## Why this does not yet prove RH

The existing packet explicitly leaves G2--G4 open. In particular, it does not construct a form-preserving source map

\[
\iota:\mathcal A_{\mathrm{Gauss}}
\longrightarrow
\Gamma_{12}\oplus\Gamma_{\ge3}
\]

satisfying

\[
L(q^*p)=\langle\iota(q),\iota(p)\rangle
\]

for the fully coupled endpoint–gamma–prime Weil observer and every finite composite Gaussian primitive.

The strict carrier is prime-labelled and local. The RH gate requires all of the following extensions:

1. glue the prime-labelled strict cells without losing their labels or positive form;
2. include the connected \(k\ge3\) tail coherently;
3. place endpoint and gamma contributions on the same closed positive carrier;
4. prove the exact polarized source identity with the Gaussian Weil kernel;
5. extend from strict primitive/square generators to every finite composite primitive;
6. pass faithfully to the completed Schwartz domain.

## Correct frontier

The common-carrier argument is not hypothetical: its local G1 instance exists and forces a local Schwarz square. The first missing RH-bearing arrow is the full form-preserving comparison

\[
\boxed{
L(q^*p)=\langle\iota(q),\iota(p)\rangle.
}
\]

This must be derived from the coupled source before invoking positivity. If constructed on the composite Gaussian closure, universal rung-four positivity and RH would follow immediately.

## Durable inputs

- `research/voevodsky/retained_joint_graph_supersedes_endpoint_cross_port_mate_gate_20260908.md`
- `research/voevodsky/four_front_odd_line_closes_endpoint_trace_faithfulness_20260908.md`
- `research/voevodsky/Mobius-channel-symmetry-does-not-imply-Weil-positivity.md`

# Spin(7) Parent Branching Narrows but Does Not Select the Completion

Work package: WP921

## Question

Does the smallest natural simple parent

\[
\mathrm{Spin}(7)\supset\mathrm{Spin}(5)\times\mathrm{Spin}(2)
\]

produce exactly Completion A or B? The Spin(2) factor supplies the candidate
(U(1)) charge.

## Exact bounded branching packet

Normalize Spin(2) charge so vector singlets carry charges (\pm1) and
spinors carry (\pm1/2). The fundamental parent branches are

\[
8\longrightarrow4_{+1/2}\oplus4_{-1/2},
\]

\[
7\longrightarrow5_0\oplus1_{+1}\oplus1_{-1}.
\]

Since (21=\Lambda^2 7), the adjoint branching follows exactly:

\[
21\longrightarrow10_0\oplus1_0\oplus5_{+1}\oplus5_{-1}.
\]

The calculation uses the standard low-dimensional Spin(7) representations
and the subalgebra-decomposition framework implemented in
[LieART 2.0](https://doi.org/10.1016/j.cpc.2020.107490). The displayed adjoint
rule is also derived directly by taking the exterior square of the displayed
vector rule, so the checker does not depend on a numerical branching table.

## Charge-pair obstruction for Completion B

The Weyl group of type (B_3) contains total weight negation. Therefore the
restriction of every complete finite-dimensional Spin(7) representation to
the chosen Spin(2) has equal multiplicities at charges (q) and (-q).

The shared portal plus Completion B is

\[
4_{-1/2}\oplus5_{+1}\oplus4_{-3/2}
\oplus1_0\oplus1_{+1}\oplus1_{+2}.
\]

It is not charge-pair closed. Hence it cannot be the exact branching image of
a complete Spin(7) representation. Additional conjugate states or a
projection that changes the low-energy category would be required.

## Neutral-surplus obstruction for Completion A

The shared portal plus Completion A is charge-pair closed:

\[
4_{-1/2}\oplus4_{+1/2}\oplus5_{+1}\oplus5_{-1}.
\]

The smallest fundamental carrier containing these types is (8\oplus21).
But its exact image is

\[
4_{-1/2}\oplus4_{+1/2}\oplus5_{+1}\oplus5_{-1}
\oplus10_0\oplus1_0.
\]

Thus the desired charged packet has dimension (18), while its smallest
bounded parent carrier has dimension (29). The neutral (10_0\oplus1_0)
is not optional inside the complete adjoint.

## Verdict

Spin(7) supplies genuine explanatory pressure: charge-pair closure excludes
exact Completion B and makes A the compatible charged pattern. It still does
not produce A as a singleton exact low-energy image. The parent operation is
a constraint and charge-pair rigidifier, not yet a completion selector or a
physical16 selector.

The smallest exact falsifier of an exact-A claim is the forced neutral surplus
(10_0\oplus1_0). Removing it requires a new source-authorized projection,
boundary condition, or localization index. Such an operation changes the
admitted low-energy category and cannot be chosen merely because it leaves the
desired packet.

The sharp successor is to test an orbifold or domain-wall parity whose origin
is independent of flavor fitting and whose zero-mode index retains both
charged pairs while removing exactly the neutral surplus. The parity must
also constrain the surviving three-family Yukawa tensors; otherwise it solves
only the census gate.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp921_spin7_parent_branching_singleton_audit.py
~~~

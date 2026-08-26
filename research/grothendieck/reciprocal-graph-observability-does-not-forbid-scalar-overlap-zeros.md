# Reciprocal graph observability does not forbid scalar overlap zeros

## Question

Reciprocal graph pairing replaces independent sheets by

\[
x\longmapsto(Tx,T^*x)
\]

and measures them with

\[
G=T^*T+TT^*.
\]

Does a positive lower bound for \(G\) exclude a zero of the scalar theta
readout?

## Minimal hostile model

Let the state space be \(\mathbb R^2\), let \(e_1\) be the distinguished
vacuum, and let

\[
T_\theta
=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
\]

The scalar overlap is

\[
\sigma(\theta)
=
\langle e_1,T_\theta e_1\rangle
=
\cos\theta.
\]

At \(\theta=\pi/2\),

\[
\sigma(\theta)=0.
\]

But \(T_\theta\) is unitary, so

\[
T_\theta^*T_\theta
+T_\theta T_\theta^*
=
2I.
\]

The reciprocal source graph has a uniform gap of two and no kernel at the
exact scalar zero.

## Meaning of the counterexample

Reciprocal graph pairing answers an observability question: simultaneous
equations \(Tx=0\) and \(T^*x=0\) should imply \(x=0\).

It does not answer the transversality question

\[
\langle\Omega,T\Omega\rangle=0.
\]

The latter can occur because two fully visible nonzero states become
orthogonal.  No kernel, cokernel, loss of range, or completion defect is
required.

Thus reciprocal graph observability and scalar divisor confinement are
logically independent until a source theorem identifies the scalar section
with a determinant, index, or kernel condition of the graph operator.

## Application to the theta programme

The completed theta scalar has repeatedly appeared as a source overlap or
matrix coefficient.  Kitaev's reciprocal graph construction can repair
one-sided blindness of the underlying labelled transport, but its Gram gap
alone cannot exclude a zero of that overlap.

The missing bridge must have one of two forms:

1. Determinant bridge: derive a Fredholm comparison \(T_z\) for which
   \(\Xi(z)\) is its determinant section up to a nowhere-zero unit.
2. Acute-pairing bridge: derive a source cone forcing the distinguished
   overlap to remain nonzero off the seam.

The second route has already failed in several local and hostile models.
Therefore the determinant/kernel bridge is again the only structurally live
route, but now with a precise reciprocal graph substrate available.

## No circular construction

Defining

\[
T_z=\Xi(z)I
\]

would make the bridge tautological.  The operator must be derived from the
labelled theta/Tate constructors before the scalar section is evaluated.
Likewise, adjoining a rank-one Koszul factor carrying a chosen hostile divisor
is prohibited unless it has an independent source lift.

Let \(\mathcal S_{\mathrm{label}}\) denote the labelled source graph.  The
acceptance test is the derivational chain

\[
\mathcal S_{\mathrm{label}}
\longrightarrow
T_z
\longrightarrow
\det_{\mathrm{rel}}T_z
=
u(z)\Xi(z),
\]

with \(u\) nowhere zero and every arrow defined without zero data.

## Completion gates

Even after the determinant bridge is built, reciprocal graph faithfulness
must survive completion.  The required gates remain:

- stability of the finite-core kernel under closure;
- positive reduced minimum modulus on each fixed off-seam compact set;
- explicit seam/index stabilization when an inverse or determinant is used.

These gates become relevant only after the scalar zero has been proved to
mean operator noninvertibility.  Applying them directly to an overlap is a
type error.

## Result

Perfect reciprocal graph observability is compatible with an exact scalar
overlap zero.  The graph construction repairs state detection, not scalar
transversality.  The next indispensable theorem is a noncircular
cohomology--section or determinant--section bridge for the labelled theta
source graph.

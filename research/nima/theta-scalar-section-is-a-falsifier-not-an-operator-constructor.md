# The scalar Tate section is a falsifier, not an operator constructor

## Question

Can a completed scalar section determine the ordered tail–seam operator that
produces it?

The answer is no without an additional source-derived identifiability theorem.
Scalar agreement is a necessary test of a proposed lift, but it is not an
operator construction.

This packet concerns determinant-like aggregate scalarization. A full scalar
characteristic transfer can determine a minimal rank-one realization up to
port gauge under additional controllability, observability, and simplicity
hypotheses. That distinct case is typed in the companion control-identifiability
packet.

## Finite nonidentifiability theorem

Let \(V\) have dimension at least two and let \(U(s)\in GL(V)\) be a
holomorphic operator family. For every holomorphic family

\[
S(s)\in SL(V),
\]

the modified family

\[
\widetilde U(s)=S(s)U(s)
\]

has the same determinant:

\[
\det\widetilde U(s)=\det U(s).
\]

It consequently has the same determinant divisor and the same logarithmic
determinant current wherever these are defined:

\[
\partial_s\log\det\widetilde U(s)
=
\partial_s\log\det U(s).
\]

The determinant fiber is therefore already infinite-dimensional at the level
of holomorphic families. Neither the Product lens nor its Sum shadow identifies
the Endo object.

The smallest witness is the determinant-one shear

\[
S_t=
\begin{pmatrix}
1&t\\
0&1
\end{pmatrix}.
\]

For \(t\ne0\), \(S_tU\ne U\) generically although every scalar determinant
readout agrees.

## Exact identifiability gate

Let \(\mathfrak L_{\mathrm{src}}\) be the class of source-admissible ordered
lifts, let

\[
\Sigma:\mathfrak L_{mathrm{src}}\longrightarrow\mathfrak S
\]

be scalarization, and let \(\sim_{\mathrm{auth}}\) denote independently
authorized boundary equivalence. The scalar section determines the ordered
lift only if

\[
\Sigma(L_1)=\Sigma(L_2)
\quad\Longrightarrow\quad
L_1\sim_{mathrm{auth}}L_2
\]

for all \(L_1,L_2\in\mathfrak L_{\mathrm{src}}\).

This implication is the missing identifiability theorem. It cannot be obtained
by declaring all equal-scalar lifts equivalent: the equivalence must already
come from source geometry, domains, covariance, and boundary incidence.

## Control interpretation

The ordered lift is a state-transition realization. Its scalarization is an
aggregate output such as volume gain, determinant phase, or a distinguished
overlap. Distinct realizations can have the same aggregate output while
differing in mode mixing, seam action, sheet character, domains, and
conditioning.

Accordingly, the valid inference direction is

\[
\text{source incidence}
\longrightarrow
\text{ordered lift}
\longrightarrow
\text{scalar Tate section}
\longrightarrow
\text{logarithmic currents}.
\]

The reverse arrows require separate identifiability constructors and are not
provided by scalar agreement.

## Completion hostile

Scalar nonvanishing at every finite stage does not control inverse norms. The
family

\[
U_N=
\begin{pmatrix}
N&0\\
0&N^{-1}
\end{pmatrix}
\]

satisfies

\[
\det U_N=1
\]

for every \(N\), while

\[
\sigma_{min}(U_N)=N^{-1}\longrightarrow0.
\]

Thus the Product and Sum lenses can remain exact while strict invertibility is
lost at completion. The RH-bearing gate must exclude normalized escape states

\[
\|v_N\|=1,
\qquad
\|U_Nv_N\|\longrightarrow0,
\]

or its rigged-correspondence analogue.

## Programme consequences

1. Construct the partial source-to-boundary correspondence before using the
   scalar completed section.
2. Freeze its domain, adjoint domain, seam incidence, sheet covariance, and
   primitive/square topology.
3. Prove closability independently of scalar Tate convergence.
4. Test finite injectivity and completion-stable observability separately.
5. Derive the scalar section from the lift and use mismatch as a rejection
   test.
6. Classify the scalarization fiber modulo authorized equivalence before making
   any uniqueness claim.

## Finite falsifiers

A claimed scalar-to-operator reconstruction fails if any of the following is
exhibited:

- a determinant-one shear with different seam action;
- two lifts with equal scalar section but different sheet character;
- equal determinant divisors with different adjoint domains;
- finite nonvanishing with minimum singular value tending to zero;
- scalar cancellation between nonzero primitive, square, or seam residual
  matrices;
- uniqueness obtained only by defining unauthorized lifts to be equivalent.

## Disposition

The completed scalar Tate section is a strong falsifier of proposed ordered
lifts and a valid invariant of an already constructed source object. It is not
the constructor of that object. The live theorem is source-level existence,
identifiability up to authorized equivalence, and completion-stable
observability of the tail–seam correspondence.

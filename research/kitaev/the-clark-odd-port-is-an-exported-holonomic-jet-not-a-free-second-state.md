# The Clark odd port is an exported holonomic jet, not a free second state

## Question

Does the pinned Clark derivative remain internal to the bulk, or is it
exported to a boundary observation? If exported, what is its correct state
typing?

## Finite endpoint export is established

For a finite transfer coefficient \(F\), the two Clark endpoint rows are

\[
O_+=\begin{pmatrix}1&F+iaF'\end{pmatrix},
\qquad
O_-=\begin{pmatrix}1&F-iaF'\end{pmatrix}.
\]

Their joint Gramian is

\[
W_a
=O_+^*O_++O_-^*O_-
=2
\begin{pmatrix}
1&F\\
\overline F&|F|^2+a^2|F'|^2
\end{pmatrix},
\]

so

\[
\det W_a=4a^2|F'|^2.
\]

At a simple scalar zero, \(F=0\) and \(F'\ne0\), the odd first jet remains
visible at the endpoint. Thus the Clark odd coordinate is not merely an
internal quadratic diagnostic: it has a source-derived finite boundary
readout.

This proves observability of a simple transmission zero. It does not exclude
the zero.

## The two derivative directions have different jobs

The endpoint trace is controlled by the scale-flow graph norm. The source
equation has the form

\[
(\partial_q+s)G=-f.
\]

The exact first-order estimate for \(G+f\) controls \(G(0)\) in the open
strip. By contrast, \(\partial_zG\) differentiates in the spectral parameter
and detects transverse multiplicity. It was not derived as the endpoint
trace norm.

Therefore:

- \(\partial_q\) controls existence and continuity of the boundary trace;
- \(\partial_z\) supplies the odd transverse observation at scalar silence.

Substituting one derivative for the other is a typing error.

## Source-derived jet prolongation

Differentiate the scale-flow equation with respect to \(z\). With
\(\partial_zs=i\),

\[
(\partial_q+s)\partial_zG+iG=-\partial_zf.
\]

On the prolonged state

\[
\Psi=
\begin{pmatrix}
G\\
\partial_zG
\end{pmatrix},
\]

the homogeneous generator is triangular:

\[
\partial_q\Psi=
\begin{pmatrix}
-s&0\\
-i&-s
\end{pmatrix}\Psi
+
\begin{pmatrix}
-f\\
-\partial_zf
\end{pmatrix}.
\]

For the scaled odd coordinate \(Y=a\,\partial_zG\), the lower-left entry is
\(-ia\). Reversing the Clark sheet changes its sign. Hence the two chart
generators obey covariance under sheet exchange rather than commuting with a
fixed character involution inside one chart.

This is an authorized source mixing term. It was not added to repair
observability.

## Holonomicity constraint

The prolonged pair is not an arbitrary vector in a product space. It lies in
the first jet of one parameter-dependent source family:

\[
J^1G=(G,\partial_zG).
\]

A nominal ambient state with \(G=0\) and \(\partial_zG\ne0\) at one parameter
can occur at a scalar zero. But an arbitrary \(q\)-trajectory in the second
coordinate need not be the derivative of any common source family.

Thus the admissible state space is a holonomic jet module, not the free
direct sum of two unrelated tail spaces. Any PBH or Gramian audit on the
ambient product may report modes that violate mixed-derivative compatibility,
cutoff naturality, or common-source dependence.

The correct observability question is:

> Does the endpoint observation separate admissible source jets, with a
> completion-stable norm on the holonomic jet module?

## Higher multiplicity

If

\[
F=F'=0,
\]

the first-jet Gramian is singular. A zero of multiplicity \(r\) requires the
jet tower through order \(r\):

\[
J^rF=(F,F',\ldots,F^{(r)}).
\]

Repeated differentiation gives the triangular prolongation law

\[
(\partial_q+s)\partial_z^kG
+ki\,\partial_z^{k-1}G
=-\partial_z^kf.
\]

The coefficients \(ki\) are source-forced. They define a nilpotent Jordan
connection on the jet tower.

For a declared maximum jet order \(r\), endpoint faithfulness at a zero is
equivalent to at least one authorized derivative through order \(r\) being
nonzero. Uniform completion requires quantitative lower bounds, not merely
finite nonvanishing.

## Why this does not become an infinite sensor licence

One may not append derivatives until a desired zero becomes visible.
Admissible jet order must be supplied by the source constructor. Otherwise
the observation family depends on the unknown multiplicity it is intended to
detect.

Three possibilities remain:

1. the source supplies a finite closed jet module and a multiplicity bound;
2. the source supplies a nuclear infinite jet module with controlled
   topology;
3. no authorized jet tower is complete, leaving higher-multiplicity states
   outside the observation theorem.

## Relation to the sheet-character no-go

The earlier no-go assumed one return operator commuting with a fixed sheet
involution. The Clark prolongation instead gives a covariant pair of chart
generators whose off-diagonal jet connection reverses with \(a\).

This avoids the claim that every repeated even observation must remain
even. It does not automatically make the odd jet dissipative. One must still
show that:

- the odd endpoint row is continuous in the completed jet topology;
- it enters an exact passive or energy-balance identity;
- the admissible odd jet sector has a uniform observability margin.

## Minimal hostile

Take scalar functions

\[
F_\epsilon(z)=\epsilon z.
\]

At \(z=0\), every member has a simple zero and the finite Clark Gramian is
positive for \(\epsilon\ne0\), but

\[
\det W_a=4a^2\epsilon^2\longrightarrow0.
\]

Thus finite simple-zero observability can collapse in completion even with
the correct odd endpoint port.

A second hostile treats \((G,J)\) as a free product state and inserts an
arbitrary \(J\) trajectory not equal to \(\partial_zG\). It may create a PBH
kernel that is absent from the holonomic source module. This is a typing
falsifier, not a physical hidden mode.

## Disposition

The Clark odd derivative is exported at finite endpoints, and its dynamics
has an exact source-derived Jordan coupling to the scale-flow state. The
remaining problem is not construction of an odd coordinate. It is:

1. defining the completed holonomic jet topology;
2. proving continuity of the odd endpoint row there;
3. deriving its role in the boundary energy balance;
4. obtaining a cutoff-independent observability margin.

This narrows the fifth-level sewing constructor to a jet-trace correspondence,
not an arbitrary new sensor.

## Claim boundary

This packet combines pinned finite endpoint and source-flow identities. It
does not prove a completed jet trace theorem, bound zero multiplicity, or
establish passive boundary sewing.

# The source gives one physical cycle and two labelled coefficient channels

> **Retrospective status.** This is a hostile replication packet, not a new
> generic-\(\mathcal Q\) frontier. Ledger Entries 181, 183, and 212 already
> prove trivial generic physical variation, and Entry 718 closes the later
> second-normal reopening. The transport-rank census below independently
> agrees with that verdict.

## Question

Can the determinant mechanism

\[
\det
\begin{pmatrix}
2A&A+B-E^2\\
A+B-E^2&2B
\end{pmatrix}
=\mathcal Q
\]

be typed as a response matrix of the physical five-pole residue system?

## Frozen source data

The \(q_{\mathcal G_{12}}\)-residue has orientation
\(da\wedge db\) and the source combination

\[
\omega_{23}+\omega_{31},
\]

where the two labelled summands have denominator sets

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{g_{23}}\},
\qquad
\{q_{g_1},q_{g_2},q_{g_3},q_{g_{31}}\}.
\]

The source supplies one Bunch--Davies relative contour, not two independently
normalized contours.  Therefore a matrix with rows indexed by invented cycles
\(\Gamma_{23},\Gamma_{31}\) is not source-typed.

The complete common marked presentation does contain two canonical rank-20
face subobjects whose intersection is the rank-15 double deletion.  This does
**not** supply projections from their sum back to either face.  A decomposition
of a common cohomology class into face components is ambiguous by the rank-15
intersection.

Consequently a response written using assumed projections

\[
R_{\alpha i}
=
\operatorname{Per}_{\Gamma_{\rm BD}}
\bigl(\rho_\alpha(\Theta_i s)\bigr),
\qquad
\alpha\in\{23,31\},\quad i\in\{u,v\},
\]

where \(\rho_{23},\rho_{31}\) must be the source-derived face maps inside the
common localization complex is still untyped: the source presently provides
face inclusions, not such retractions.

The only admissible two-channel candidate is instead to retain the two
summands before assembly and differentiate each through the same moving
localization construction:

\[
\Theta_i^{(\alpha)}
=dF_i^{(\alpha)}
+A_{\rm common}F_i^{(\alpha)}
-F_i^{(\alpha)}A_{\rm absolute},
\qquad \alpha\in\{23,31\},
\]

then require

\[
\Theta_i^{(23)}+\Theta_i^{(31)}=\Theta_i.
\]

Only after this identity and representative independence hold may one define

\[
R_{\alpha i}
=\operatorname{Per}_{\Gamma_{\rm BD}}
\bigl(\Theta_i^{(\alpha)}s\bigr).
\]

The two rows are source-summand coefficient channels evaluated against the
same cycle; they are neither two cycle choices nor projections chosen after
cohomological reduction.

## Typing gate

The rank identities

\[
\dim F_{23}=\dim F_{31}=20,
\qquad
\dim(F_{23}\cap F_{31})=15
\]

do not themselves define \(\rho_\alpha\) on mixed curvature or on the relative
de Rham--Betti complex.  Nor may the previously constructed independent
quotient-face maps be reused: those maps were rejected as noncanonical outside
the common presentation.

Before taking a determinant one must derive and verify:

1. branchwise moving maps derived from the two frozen source summands;
2. additivity to the already certified assembled mixed curvature;
3. independence from the rank-15 intersection ambiguity;
4. horizontality with the common Gauss--Manin connection;
5. descent to the relative Leray pairing with the single oriented physical
   contour;
6. invariance under admissible changes of common primitive representatives.

## Narrow conclusion

The toy determinant remains a valid mechanism witness, but its physical
realization is not yet established.  It has survived in one strictly narrower
hypothetical form before imposing that prior theorem:

\[
\boxed{
\mathcal Q\text{ may be the degeneracy divisor of the two source-summand
responses of one physical cycle.}
}
\]

This is distinct from a self-pairing on the mixed-curvature image and from two
independent physical cycles. In the frozen system the hypothesis is retired;
the paragraph records its typing only to prevent later reintroduction in an
invalid form.

## First transport-rank falsifier

The two literal source vectors can be differentiated without choosing a face
projection.  At the generic control point and at six generic
\(\mathcal Q=0\) points split across \(\mathbf F_{32003}\) and
\(\mathbf F_{32009}\), the stable physical half-twist presentation gives

\[
\operatorname{rank}\{\nabla_u s_{23},\nabla_v s_{23}\}=2,
\qquad
\operatorname{rank}\{\nabla_u s_{31},\nabla_v s_{31}\}=2,
\]

and

\[
\operatorname{rank}
\{\nabla_u s_{23},\nabla_v s_{23},
  \nabla_u s_{31},\nabla_v s_{31}\}=4.
\]

The branchwise derivatives add exactly to the derivative of the assembled
source.  No tested rank changes on \(\mathcal Q=0\).

Therefore \(\mathcal Q\) is not a generic cohomological rank-loss divisor of
the two labelled source transports in this presentation.  The simple
transport-caustic hypothesis is closed in the tested finite models. Entries
181 and 183 additionally close downstream relative-cycle variation at generic
nonsoft \(\mathcal Q\), so no generic physical home survives in this
homogeneous system. The new census is replicated finite-field evidence
consistent with that characteristic-zero geometric theorem.

# The ambient Mellin connection exists but the source Riesz compression does not

## Correction to the first source audit

The prior audit stopped at an “absent parameter connection.” That statement was too coarse. The theta source already supplies an exact ambient connection on the finite labelled arithmetic module:
\[
Qe_n=(\log n)e_n,
\qquad
\nabla_a^{\mathcal H}=\partial_a+Q,
\qquad
\nabla_t^{\mathcal H}=\partial_t+iQ.
\]
Its transport is
\[
U_{(a_1,t_1),(a_0,t_0)}
=
e^{-((a_1-a_0)+i(t_1-t_0))Q}.
\]
This connection is source-derived, canonical under diagonal label naturality, and flat.

Accordingly, the first absent constructor is not the ambient parameter connection. It is the source-authorized spectral compression that turns the ambient connection into a connection on the reduced Riesz/defect carrier.

This record supersedes that part of the prior absent-parameter-connection record.

## Ambient source theorem already available

At finite cutoff \(X\), the labelled carrier
\[
\mathcal H_X=\operatorname{span}\{e_n:n\in X\}
\]
is a fixed ambient trivialization over the Mellin parameter patch. The finite generator
\[
Q_X=\operatorname{diag}(\log n)_{n\in X}
\]
gives exact parallel transport. Cutoff inclusions are compatible because
\[
\iota_{X,Y}Q_X=Q_Y\iota_{X,Y}
\]
when old labels and rates are preserved. Hence
\[
\iota_{X,Y}U_X(\gamma)=U_Y(\gamma)\iota_{X,Y}.
\]

The reciprocal Real exchange reverses the centered normal direction and conjugates spectral height. On the paired finite carrier it satisfies the declared dihedral covariance with Mellin transport. This ambient loop is flat and source-blind; it contains no RH force by itself.

## Missing compressed constructor

To obtain defect transport one needs a source-derived projection
\[
P_X(s):\mathcal H_X\longrightarrow\mathcal D_X(s)
\]
onto the finite Riesz defect complex, or an equivalent source-defined subbundle. Then the induced connection is
\[
\nabla^{\mathcal D}_X
=
P_X\nabla^{\mathcal H}_X P_X.
\]
In a declared frame with \(\nabla^{\mathcal H}=d+A_{\mathcal H}\), set
\[
D^{\mathcal H}P_X=\dot P_X+[A_{\mathcal H},P_X].
\]
The covariant Kato transport satisfies
\[
\dot W
=
\bigl([D^{\mathcal H}P_X,P_X]-A_{\mathcal H}\bigr)W.
\]
Equivalently one may first pass to an ambient horizontal frame, where \(A_{\mathcal H}=0\), and use
\[
\dot W=[\dot P_X,P_X]W.
\]
The convention must be declared, since mixing these formulas double-counts the ambient connection.

The inspected source records do not yet jointly supply:

1. a common graph domain for the completed or reduced theta Fredholm pencil;
2. norm-\(C^1\) dependence of its resolvent on the parameter;
3. a uniform contour gap around the selected spectral point;
4. the resulting norm-\(C^1\) Riesz projection \(P_X(s)\);
5. proof that \(P_X(s)\) is the projection selected by source incidence rather than by the desired zero set;
6. cutoff and reciprocal naturality of that projection.

Therefore the missing port is:

    first_absent_constructor: source_riesz_projection_bundle
    ambient_parameter_connection: present
    induced_defect_connection: blocked_by_missing_projection
    first_failed_degree: null
    equation_evaluation_started: false

## Required analytic gate

Let \(T_X(s)\) be a closed Fredholm pencil on a common graph domain. On a parameter patch \(U\), require:

- \(s\mapsto T_X(s)\) is graph-norm \(C^1\);
- one contour \(\Gamma\) lies in \(\rho(T_X(s))\) for all \(s\in U\);
- the resolvent and its derivative are uniformly bounded on \(\Gamma\times U\).

Then
\[
P_X(s)
=
\frac{1}{2\pi i}\int_\Gamma(z-T_X(s))^{-1}\,dz
\]
is norm-\(C^1\), with
\[
\dot P_X(s)
=
\frac{1}{2\pi i}
\int_\Gamma
(z-T_X)^{-1}\dot T_X(z-T_X)^{-1}\,dz.
\]
Only this theorem licenses compression of the ambient Mellin connection.

## Naturality gates

Cutoff naturality requires more than ambient parallelity:
\[
\iota_{X,Y}P_X(s)=P_Y(s)\iota_{X,Y}.
\]
Together with parallelity of \(\iota_{X,Y}\), this implies naturality of compressed transport.

Reciprocal naturality requires the Real map \(J_X(s)\) to intertwine both the pencil and ambient connection:
\[
J_X(s)P_X(s)=P_X(\rho(s))J_X(s),
\]
and
\[
J_X\nabla^{\mathcal H}
=
\nabla^{\mathcal H,\rho}J_X,
\]
with conjugation and path orientation explicitly included. Only then does
\[
J_X(s_1)W_X(\gamma)
=
W_X(\rho\gamma)J_X(s_0)
\]
follow.

## Why pointwise matrices remain insufficient

The old finite equalizer matrices are pointwise and source-typed, while the ambient Mellin connection is also source-typed. But these two facts do not identify a Riesz subbundle. Many moving projections inside the same flat labelled bundle are compatible with the same ambient transport, and they produce inequivalent compressed holonomies.

The missing datum is therefore genuinely geometric: the source incidence must select the moving spectral subspace before the connection can be compressed.

## Revised decisive theorem

Construct from the complete theta boundary incidence a reduced Fredholm pencil \(T_X(s)\) on the fixed Mellin-labelled Hilbert bundle such that:

1. its graph domain is parameter-independent;
2. its contour resolvent is norm-\(C^1\) with a uniform gap;
3. its Riesz projection is source-selected;
4. cutoff inclusion intertwines the projection;
5. reciprocal Real transport intertwines the projection and ambient connection.

The ambient connection is already available and flat. The unresolved RH-bearing geometry is exactly the moving source projection and its compressed curvature
\[
P_X[dP_X,dP_X]P_X.
\]
If the projection cannot be constructed before scalar completion, the connection route remains non-source-local.

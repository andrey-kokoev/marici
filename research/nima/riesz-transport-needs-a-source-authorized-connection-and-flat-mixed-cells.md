# Riesz transport needs a source-authorized connection and flat mixed cells

## Correction

A family of Riesz ranges supplies fibers, not canonical transport. The statement
\[
\mathcal D:(X,s)\longmapsto \operatorname{ran}P_X(s)
\]
becomes a functor only after every generating edge is equipped with a source-authorized connection and the generating two-cells satisfy coherence.

Let \(\mathcal P_\Gamma^{(2)}\) have three edge generators:

1. cutoff inclusion \(c_{XY}:(X,s)\to(Y,s)\);
2. parameter continuation \(a_\gamma:(X,s_0)\to(X,s_1)\);
3. reciprocal transport \(r_X:(X,s)\to(X,1-s)\).

Besides ordinary identity and composition cells, require mixed cells for cutoff/parameter, cutoff/reciprocal, and parameter/reciprocal commutation.

## Local edge transport

For nearby orthogonal Riesz projections \(P,Q\) with \(\lVert P-Q\rVert<1\), the Sz.-Nagy operator
\[
W(Q,P)=\bigl(QP+(I-Q)(I-P)\bigr)
       \bigl(I-(P-Q)^2\bigr)^{-1/2}
\]
is unitary and satisfies \(WPW^{-1}=Q\). Its restriction gives a canonical local isomorphism
\[
W(Q,P)|_{\operatorname{ran}P}:\operatorname{ran}P\to\operatorname{ran}Q.
\]
This formula is only admissible after the ambient reduced carriers have been source-authorized and identified.

Along a differentiable parameter path of projections, use Kato transport:
\[
\dot U(t)=[\dot P(t),P(t)]U(t),\qquad U(0)=I.
\]
Then \(U(t)P(0)=P(t)U(t)\). A cutoff edge instead uses its declared carrier comparison, corrected locally by the polar intertwiner when necessary. A reciprocal edge uses the declared reciprocal intertwiner restricted to the Riesz range.

## Mixed-cell curvature

For a generating square with edge transports \(T_1,T_2,T_3,T_4\), define its residual
\[
\Omega_\square=T_4T_3(T_2T_1)^{-1}.
\]
Strict Riesz transport requires \(\Omega_\square=I\). If every mixed residual and composition residual vanishes, edge products depend only on the fundamental-path-groupoid class and yield
\[
\operatorname{Hol}_{\mathcal D}:\Pi_1(|\mathcal P_\Gamma^{(2)}|)
\longrightarrow \mathrm{Iso}(\mathrm{FinVect}).
\]
If all residuals are central phases, transport is only projective. A noncentral residual is a genuine failure of the proposed categorical comparison.

The three hostile mixed residuals are explicit:

- \(\Omega_{c,a}\): cutoff inclusion versus parameter continuation;
- \(\Omega_{c,r}\): cutoff inclusion versus reciprocal transport;
- \(\Omega_{a,r}\): parameter continuation versus reciprocal transport.

Their first nonidentity value is a finite-dimensional, computable witness of incoherent completion.

## Zero-charge correction

On the desired RH component,
\[
q=0\quad\Longrightarrow\quad \mathcal D=0.
\]
Consequently all Riesz-range holonomy there is tautologically trivial. Riesz holonomy cannot carry the RH-bearing phase on the zero-defect region. Its role is instead hostile-sector classification: it records how nonzero defect modes are transported, mixed, or permuted and prevents an illicit declaration that equal ranks imply coherent identification.

The surviving phase must live on a separate line, naturally the determinant line of the complement or reduced Green carrier. Write
\[
\mathcal L_{X,s}=\det(\mathcal H^{\mathrm{red}}_{X,s}/\mathcal D_{X,s})
\]
at finite cutoff, with regularized replacement in the limit. The complete transport therefore has two layers:

- defect transport \(\mathcal D\), whose rank is the integer charge;
- complement determinant transport \(\mathcal L\), which can remain nontrivial when \(\mathcal D=0\).

The RH certificate must show zero defect charge while retaining coherent, nondegenerate determinant transport. Trivial defect holonomy is then a consequence, not the source of the analytic phase.

## Next constructor

Construct a coupled connection
\[
(\nabla^{\mathcal D},\nabla^{\mathcal L})
\]
on the parameter-cutoff-reciprocal two-complex. Prove strict flatness for \(\nabla^{\mathcal D}\) on admitted cells and identify the curvature of \(\nabla^{\mathcal L}\) with the regularized Green/determinant anomaly. Reciprocal symmetry should send that line curvature to its prescribed dual character. This places the integer obstruction and the analytic phase in their correct, noncompeting categorical fibers.

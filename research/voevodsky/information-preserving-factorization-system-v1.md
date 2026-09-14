# Information-preserving factorization system v1

## Question

How should coherent symmetry descent, stable bulk observation, finite residual repair, and relational-moduli readout compose without allowing one constructor role to impersonate another?

## Claim boundary

This packet defines a typed four-role factorization architecture and assigns the Green--Real radial constructors to it. “Factorization system” here means a typed decomposition of an observation design; no orthogonal factorization-system lifting axiom or Quillen weak-factorization structure is asserted. The master lower-bound theorem and the product bulk--moduli theorem are subsequent obligations.

## 1. Typed observation context

An observation context is

\[
\mathfrak X=(X,V,p,Y,\mathcal G,M),
\]

where:

- \(X\) is the declared Hilbert or graph Hilbert source rung;
- \(V\subseteq X\) is a closed vertical subspace of distinctions erased by descent;
- \(p:X\to Y\) is a bounded descent map with \(V=\ker p\);
- \(Y\) is the descended carrier, equipped with the quotient norm when \(p\) is a quotient map;
- \(\mathcal G\) is the groupoid of admitted symmetry, Real, gauge, and metric-rung comparisons;
- \(M\) is a separately declared moduli object, not inferred from \(Y\) or from dimension counting.

The degenerate case \(V=0\) covers comparison without information loss. Subgroup restriction changes the acting group but need not define a nonzero vertical subspace. Genuine quotient descent must identify its kernel.

A reconstruction objective is part of the type:

\[
\mathsf{Objective}=\mathsf{Quotient}(Y)\sqcup\mathsf{Source}(X)\sqcup\mathsf{Product}(X\times M).
\]

A claim about one summand does not promote to another.

## 2. Four constructor classes

### 2.1 Coherent descent

A coherent descent constructor is

\[
\mathsf d=(p,\rho_X,\rho_Y,\eta),
\]

where \(p:X\to Y\), \(\rho_X\) and \(\rho_Y\) are the relevant actions, and \(\eta\) records the required equivariance, Real, gauge, domain, and metric-rung comparison cells.

Its obligations are:

1. declare whether it is restriction, comparison, quotient descent, ordinary lift, projective lift, or gauge quotient;
2. identify \(V=\ker p\) for genuine descent;
3. specify every variance sign;
4. transport domains and metrics explicitly;
5. avoid any claim of a positive lower bound unless one is proved independently.

A coherent descent may erase information. It cannot certify source reconstruction.

### 2.2 Essential bulk observer

Relative to \(V\), an essential bulk observer is a bounded map

\[
D:X\to Z
\]

whose restriction to the vertical bulk has positive essential lower margin. When \(V\) is itself a Hilbert rung, this is expressed by

\[
q_V\bigl((D|_V)^*(D|_V)\bigr)>0
\]

in the Calkin algebra of \(V\). If the observer is intended to control all of \(X\), use \(V=X\).

This is a relative notion: a descended analytic channel may already control horizontal directions in \(Y\), while \(D\) controls only directions killed by \(p\). Cross terms and the choice of a horizontal lift are theorem obligations, not part of the role declaration.

### 2.3 Finite-defect repair

Given a bounded row operator \(T_0:X\to Z_0\) with closed range and finite-dimensional kernel

\[
N=\ker T_0,
\]

a finite-defect repair is a bounded map

\[
K:X\to Z_1
\]

such that \(K|_N\) is injective. Then \((T_0,K)^\top\) is bounded below.

The role requires the finite-dimensional residual \(N\) to be derived from the preceding observer, not selected retrospectively to fit \(K\). A compact channel may occupy this role. It cannot supply an essential margin on an infinite-dimensional source.

### 2.4 Moduli observer

A moduli observer is a map

\[
\Psi:M\to R
\]

on a separately constructed relational quotient. Its obligations are:

1. define the moduli equivalence relation;
2. prove gauge invariance;
3. specify the metric or uniform structure used for stability;
4. prove injectivity or a lower-Lipschitz estimate on its stated domain;
5. avoid counting finite moduli control as an essential bulk margin.

For a finite graph, the radial sewing moduli are represented by

\[
M=H^1(\Gamma;U(1)).
\]

## 3. Admitted compositions

The architecture admits the following ordered constructions.

### Quotient reconstruction

\[
X\overset p\longrightarrow Y\overset B\longrightarrow Z_Y.
\]

The composite \(Bp\) reconstructs only the quotient objective. It is allowed to vanish on \(V\).

### Source reconstruction

\[
X\longrightarrow Z_Y\oplus Z_V\oplus Z_F,
\qquad
x\longmapsto(Bpx,Dx,Kx).
\]

Here \(Bp\) controls descended directions, \(D\) supplies vertical essential control, and \(K\) repairs the resulting finite kernel. A uniform lower bound is not automatic from the role declarations; it is the Phase 2 theorem obligation.

### Product reconstruction

\[
X\times M\longrightarrow Z_X\oplus R,
\qquad
(x,m)\longmapsto(T_Xx,\Psi(m)).
\]

This requires an explicit product metric. Bulk and moduli constants remain separately visible.

### Comparison transport

For an admitted comparison \(C:X\to X'\), observers transport contravariantly by

\[
T' = TC^{-1}
\]

when \(C\) is invertible. Exact lower-margin invariance requires unitary \(C\); boundedly invertible \(C\) introduces condition-number bounds.

## 4. Forbidden promotions

1. Coherent descent \(\not\Rightarrow\) essential observation.
2. Quotient reconstruction \(\not\Rightarrow\) source reconstruction when \(V\ne0\).
3. Injectivity \(\not\Rightarrow\) stable lower bound.
4. A finite-rank boundary trace \(\not\Rightarrow\) essential graph-domain control.
5. Finite-defect repair \(\not\Rightarrow\) essential control.
6. Gauge fixing \(\not\Rightarrow\) gauge-invariant moduli observation.
7. Moduli injectivity \(\not\Rightarrow\) bulk coercivity.
8. Equal dimensions or equal scalar responses \(\not\Rightarrow\) equality of constructor roles.
9. A unitary presentation lift \(\not\Rightarrow\) improved lower modulus.
10. Graph adjoint \(\not\Rightarrow\) ambient adjoint.

## 5. Green--Real radial assignment

Let the boundary fiber be \(\mathbb C^2\), with Green form

\[
J_\partial=\operatorname{diag}(-1,1).
\]

The reciprocal wall comparison is

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix},
\qquad
W_u^*J_\partial W_u=-J_\partial.
\]

The fixed-fiber Real comparison is

\[
J_u=\operatorname{diag}(1,u^2)K.
\]

Their role assignment is:

| Constructor | Role | What it does not establish |
|---|---|---|
| \(C_uF^2=W_uC_u\) | subgroup restriction plus comparison cell | quotient descent from \(C_4\) |
| \(W_u\) | Green comparison cell of degree \((-,-)\) | positive observation margin |
| \(J_u\) | antilinear Real comparison | bulk coercivity |
| phase gauge \(G_{u\to v}\) | degree \((+,+)\) comparison | physical distinction of isolated wall phases |
| boundary trace \(\gamma\) | graph-to-boundary domain constructor | essential graph observer |
| thick \(D_w^+\) | reciprocal-even Real essential bulk observer | moduli reconstruction |
| compact analytic channel \(A\) | finite-defect repair after an essential complement | essential Calkin margin |
| loop holonomy | moduli constructor | bulk state |
| phase quadratures \((P,Q)\) | finite relational moduli observer | infinite-domain stability |

Thus the radial system already realizes all four roles, but only after boundary sewing, bulk state, and loop moduli are kept as different typed objects.

## 6. Acceptance audit

### Unique role assignment

Each primitive constructor above has one primary role. A composite may carry several roles only by exposing separate components. For example,

\[
(A,D_w^+,P,Q)
\]

is not one overloaded constructor: it is a product row containing finite repair, essential bulk observation, and moduli observation.

### Multi-role independence

If one implementation object is claimed to satisfy two roles, each role retains its own acceptance test. Unitarity cannot discharge a Gramian lower bound; injectivity cannot discharge gauge invariance; finite-dimensional phase reconstruction cannot discharge a Calkin condition.

### First-failure order

Candidate substitution is checked in this order:

1. source and target;
2. arity and variance;
3. support and labels;
4. required cells;
5. numeric equality.

A failure at an earlier gate blocks later scalar comparison.

## 7. Exact next obligations

1. Prove the source-reconstruction block-Gramian theorem without assuming an orthogonal splitting of \(X\).
2. Distinguish the case where \(Bp\) is bounded below on the quotient from the case where its horizontal lift has only closed range.
3. Derive finite repair from the exact residual kernel of the bulk row.
4. Equip \(X\times M\) with an explicit metric and prove the product lower bound.
5. Extend the machine-readable contract and hostile checker with reconstruction-objective types.

## Disposition

The four-role architecture is defined and the principal worked example passes the role-assignment audit at the level of typed signatures. The architecture clarifies the emerging division: descent decides which distinctions are retained, essential observation controls infinite bulk directions required by the objective, compact channels repair finite residue, and moduli observers recover gauge-invariant relational data. The lower-bound compositions remain theorem obligations rather than consequences of naming the roles.

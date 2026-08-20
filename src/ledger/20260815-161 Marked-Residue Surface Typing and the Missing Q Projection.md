---
authors:
  - marici.Benincasa
---
# Marked-Residue Surface Typing and the Missing Q Projection

## Record

Date: 2026-08-15

Status: proved narrow negative direct-collision result and pure elliptic
nearby-cycle result; the full marked-relative coefficient object and the
provenance of \(\mathcal Q\) remain open.

This is the Deutsch--Popperian outcome of the marked-relative attack after
entries 150, 152, and 155. It freezes the primary three-site integrand before
importing Marici notation. It adds no carrier cell, fitted section, support
summand, or post hoc gauge.

The hostile review run-c4bd3bfb86aa4a47b3ac902c90e29b78 returned the
controlling verdict:

\[
\text{FAIL as a full marked-relative theorem;}
\qquad
\text{PASS as a narrow negative collision certificate}
\]
\[
\text{plus a pure elliptic-quotient nearby-cycle result.}
\]

## Frozen primary source

The immutable source is Benincasa--Brunello--Mandal--Mastrolia--Vazão,
*On one-loop corrections to the Bunch-Davies wavefunction of the universe*,
arXiv:2408.16386v2.

Equation (6), PDF page 3, gives

\[
\mathcal I_{\mathcal G}[\alpha,\beta;\mathcal X]
\sim
\int_{\mathbb R_+^{n_s}}
\prod_{s\in\mathcal V}
\left[\frac{dx_s}{x_s}x_s^{\alpha_s}\right]
\int_\Gamma
\prod_{e\in\mathcal E^{(L)}}
\left[\frac{dy_e}{y_e}y_e^{\beta_e}\right]
\mu_d
\frac{\mathfrak n_\delta}
{\prod_{\mathfrak g\subseteq\mathcal G}
q_{\mathfrak g}^{\tau_{\mathfrak g}}}.
\]

Equation (7), PDF page 3, fixes the Cayley--Menger measure

\[
\mu_d
=
c_{d,n_e^{(L)},L}
\left[
\frac{
\operatorname{Vol}^2
\{\Sigma_{n_e^{(L)}}(y^2,P_{i\ldots j}^2)^2\}
}{
\operatorname{Vol}^2
\{\Sigma_{n_e^{(L)}-L}(P_{i\ldots j}^2)\}
}
\right]^{(d-n_s-L)/2}.
\]

The domain \(\Gamma\) is fixed by nonnegativity of this volume and all face
volumes in every codimension. Equations (13)--(14), PDF page 5, give

\[
\mathcal I_{\{\tau_{\mathfrak g}\}}^{(j)}
=
\int_\Gamma u\,\varphi,
\qquad
\varphi
=
\frac{\prod_{e\in\mathcal E^{(L)}}dy_e}
{\prod_{\mathfrak g\in\mathfrak G^{(j)}\cup\{e\}}
q_{\mathfrak g}^{\tau_{\mathfrak g}}},
\]

\[
u=\mu_d=\kappa_0\mathcal K^\gamma,
\qquad
\gamma=\frac{d-n_s-L}{2}.
\]

For one external state at each site, equation (51), PDF page 10, is

\[
\boxed{
\begin{aligned}
\mathcal I_{\{1\}}^{(3,1)}
={}&
\kappa_0\int_\Gamma
\prod_{e=12,23,31}[dy_e\,y_e]\,
\frac{\mathcal K^\gamma}
{q_{\mathcal G}q_{\mathfrak g_1}
 q_{\mathfrak g_2}q_{\mathfrak g_3}}
\\
&\times
\left[
\frac1{q_{\mathcal G_{12}}}
\left(\frac1{q_{\mathfrak g_{23}}}
+\frac1{q_{\mathfrak g_{31}}}\right)
+
\frac1{q_{\mathcal G_{23}}}
\left(\frac1{q_{\mathfrak g_{31}}}
+\frac1{q_{\mathfrak g_{12}}}\right)
\right.
\\
&\hspace{25mm}\left.
+
\frac1{q_{\mathcal G_{31}}}
\left(\frac1{q_{\mathfrak g_{12}}}
+\frac1{q_{\mathfrak g_{23}}}\right)
\right].
\end{aligned}}
\]

The measure here is literally \(\prod_e dy_e\,y_e\), not
\(\prod_e dy_e/y_e\).

Equation (52), PDF page 10, literally prints \(q_{\mathcal G}\),
\(q_{\mathfrak g_j}\), and \(q_{\mathcal G_{j,j+1}}\). Figure 3, PDF page
11, states that there are ten denominators. The \(q_{\mathfrak g_{ij}}\)
below are derived from the preceding source rule

\[
q_{\mathfrak g}
=
\sum_{s\in\mathcal V_{\mathfrak g}}x_s
+
\sum_{e\in\mathcal E_{\mathfrak g}^{\rm ext}}y_e,
\]

not quoted as additional terms printed in equation (52).

Put

\[
x=X_1,\qquad y=X_2,\qquad z=X_3,\qquad E=x+y+z.
\]

The ten denominators are

\[
q_{\mathcal G}=E,
\]

\[
q_{\mathfrak g_1}=x+y_{12}+y_{31},\quad
q_{\mathfrak g_2}=y+y_{12}+y_{23},\quad
q_{\mathfrak g_3}=z+y_{23}+y_{31},
\]

\[
q_{\mathfrak g_{12}}=x+y+y_{23}+y_{31},
\]

\[
q_{\mathfrak g_{23}}=y+z+y_{12}+y_{31},\quad
q_{\mathfrak g_{31}}=z+x+y_{12}+y_{23},
\]

\[
q_{\mathcal G_{12}}=E+y_{12},\quad
q_{\mathcal G_{23}}=E+y_{23},\quad
q_{\mathcal G_{31}}=E+y_{31}.
\]

In particular,

\[
\boxed{q_{\mathcal G_{12}}=E+y_{12}}
\]

is retained literally; no factor \(2\) is inserted.

Equations (57)--(58), PDF page 11, define the
\(q_{\mathcal G_{12}}\) sector and nine masters. The final four are

\[
e_6=\varphi_{002},\qquad
e_7=\varphi_{001},\qquad
e_8=y_{23}^2\varphi_{001},\qquad
e_9=y_{31}^2\varphi_{001}.
\]

Page 12 reports \(\mathcal L_3=\mathcal L_1\mathcal L_2\), and equation
(59) prints \(\mathcal L_2\). Equation (63) prints \(\mathcal Q\), but not
the companion \(P\), generic \(\mathcal L_1\), coefficients of
\(\mathcal L_3\), or the \(9\times9\) and final \(4\times4\) connections.

## Actual marked divisor

Take the literal residue

\[
y_{12}=-E,\qquad a=y_{23},\qquad b=y_{31}.
\]

The Cayley--Menger residue is the surface

\[
S_E:\qquad w^2=K_0(a,b),
\]

with the entry-150 degree-two del Pezzo compactification
\(\overline S_E\) and anticanonical boundary \(D_\infty=\{s=0\}\).

The full ten-denominator union leaves eight nonconstant source lines:

\[
\begin{array}{c|c}
q_{\mathfrak g_1}&b-y-z=0\\
q_{\mathfrak g_2}&a-x-z=0\\
q_{\mathfrak g_3}&a+b+z=0\\
q_{\mathfrak g_{12}}&a+b+x+y=0\\
q_{\mathfrak g_{23}}&b-x=0\\
q_{\mathfrak g_{31}}&a-y=0\\
q_{\mathcal G_{23}}&a+E=0\\
q_{\mathcal G_{31}}&b+E=0.
\end{array}
\]

The literal \(q_{\mathcal G_{12}}\)-polar contribution has only the
active-five union

\[
\boxed{
q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathfrak g_3},
q_{\mathfrak g_{23}},q_{\mathfrak g_{31}}.
}
\]

The last two occur in separate summands, so each summand has four finite
poles. The full-eight and active-five unions must remain distinct.

The signed Cayley--Menger face lines are

\[
a-E\pm y=0,\qquad a+E\pm y=0,
\]

\[
b-E\pm x=0,\qquad b+E\pm x=0,
\]

\[
a+b\pm z=0,\qquad a-b\pm z=0.
\]

The frozen boundary also retains \(AB=0\),

\[
a=0,\quad b=0,\quad E=0,\quad x=0,\quad y=0,\quad z=0,
\]

and \(D_\infty\).

These marks are curves on a two-dimensional residue surface, not merely
points on the elliptic curve. The elliptic curve is the anticanonical
boundary and the entry-150 Gysin quotient. Therefore

\[
R^1\pi_*(E_X\setminus D_X)
\]

with \(D_X\) treated only as points on \(E_X\) is mistyped as a candidate
for the full object.

The surviving typing candidate is a log/relative or Borel--Moore
Gauss--Manin object of

\[
(\overline S_E,D_{\rm pole},D_{\rm minor}\cup D_\infty;
\widetilde\Gamma).
\]

This is not a theorem. Its variance, physical-chain lift, labelled
multiplicities, sheets, orientations, and log resolution remain
unconstructed. Entry 150 stays fixed:

\[
0\longrightarrow\mathcal T_7
\longrightarrow\mathcal M_q^{(9)}
\xrightarrow{R_\infty}\mathbb V_{\rm ell}(-1)
\longrightarrow0.
\]

## Direct \(\mathcal Q\)-collision test

Write

\[
A=\ell_1\ell_2,\qquad B=\ell_3\ell_4,\qquad
\mathcal Q=4AB-(A+B-E^2)^2.
\]

The exact checker is
research/benincasa/check_marked_relative_q.rs, with SHA-256

\[
\texttt{c9ed2b8ae22ee8e340708dc5c7872eaf57e3395bbcad175112f0e603bc4f85f3}.
\]

A warnings-denied Rust build passed all \(340\) fail-closed assertions.

On \(x=1,y=2\),

\[
\mathcal Q_s(z)
=
-5z^4-36z^3-70z^2+12z+35,
\]

and

\[
\operatorname{Res}(\mathcal Q_s,\mathcal Q_s')
=
2^{24}\cdot5\cdot283,
\]

so \(\mathcal Q_s\) is square-free.

The frozen linear census has \(41\) candidates:

- eight line/branch derivative resultants;
- twelve reduced signed-face/branch derivative resultants;
- twenty-one nonparallel source-line pair evaluations.

All have nonzero exact remainder modulo \(\mathcal Q_s\). If multivariate
\(\mathcal Q\) divided a tested collision polynomial \(P\), then
\(\mathcal Q_s\mid P_s\). Thus

\[
\boxed{\mathcal Q\nmid P}
\]

for every tested candidate.

This does not prove \(\gcd(\mathcal Q_s,P_s)=1\), multivariate
irreducibility of \(\mathcal Q\), absence of isolated or higher-codimension
intersections, full multivariate factorization, or completeness beyond the
frozen linear marks and faces.

The sharp outcome is

\[
\boxed{
\text{no whole }\mathcal Q\text{ divisor factor is generated by the}
\text{ frozen direct denominator/CM-face collision geometry}.
}
\]

The auxiliary quadratic

\[
M_A(u)=Au^2-(A+B-E^2)u+B
\]

satisfies

\[
\operatorname{Res}(M_A,M_A')=A\mathcal Q,
\]

with \(B\mathcal Q\) in the reciprocal chart. This formal identity is not
source provenance. Neither the companion \(P\) nor a canonical map from a
denominator, minor, kernel line, or extension to \(M_A\) is known.

Entry 149's abstract marked-section construction is therefore only an
auxiliary model. At present

\[
\boxed{
\mathcal Q=
\text{source-printed algebraic-letter radicand/presentation datum}
}
\]

whose support placement is unresolved. It is not proved coefficient support
and does not define a carrier stratum.

## Nearby cycles and second normal order

The corrected presentation is

\[
B^{-1/2}\otimes\mathbb H_{\rm Leg}(A/B),
\]

equivalently

\[
A^{-1/2}\otimes\mathbb H_{\rm Leg}(B/A).
\]

At \(E=0\), genericity is

\[
xy(x+y)\neq0,
\]

which excludes all three site-soft loci because \(z=-(x+y)\).

For the rank-two elliptic quotient, \(m=A/B\to\infty\), and

\[
T_{\rm Leg}=-\exp N_0,\qquad
\operatorname{rank}N_0=1,\qquad N_0^2=0.
\]

The Kummer line has \(T_{\rm Kum}=-1\). Hence

\[
\boxed{
T=\exp N,\qquad \operatorname{rank}N=1,\qquad N^2=0.
}
\]

In an integral \(I_2\) basis the off-diagonal has magnitude \(2\); a
normalized complex Frobenius basis may show \(1\).

At \(E=0\),

\[
F_0(t)=(xt^2+y)^2.
\]

The raw infinity fiber is type \(I_2\), two rational components meeting at
two nodes. The whole compactified residue surface obeys

\[
\overline K_0=R^2,\qquad
R=x\alpha^2+y\beta^2-xy(x+y)s^2,
\]

so the central surface is \(W=R\cup W=-R\). The marks collide with signed
boundaries at \((a,b)=(\pm y,\pm x)\), and

\[
R|_{q_{\mathfrak g_3}}=(x+y)(a-y)^2
\]

shows a tangency. These facts do not determine full marked-relative nearby
cycles. That requires the physical relative/Borel--Moore chain, variance,
sheets, orientations, multiplicities, and a semistable/log resolution.

Finally,

\[
B=2(x+y)E-E^2
\]

has a linear term, while

\[
\boxed{
\mathcal Q=-16x^2y^2-8xyE^2+8(x+y)E^3-5E^4.
}
\]

Thus

\[
\mathcal Q_0=-16x^2y^2,\qquad
\mathcal Q-\mathcal Q_0=0\cdot E-8xyE^2+O(E^3).
\]

The first normal Taylor coefficient vanishes and the second is

\[
\boxed{-8xy}.
\]

The shorthand
\(\operatorname{gr}^{(2)}_E\mathcal Q=-8xy\) means the second normal
deformation grade after subtracting \(\mathcal Q_0\). Literally, the
\(E\)-adic initial form of \(\mathcal Q\) is degree zero. This second
coefficient does not control the first-order elliptic degeneration created
by \(B\).

## Classification

Existing carrier:

- sourced energy/Cut base and signed-energy arrangement;
- total-energy boundary \(E=0\);
- site-soft loci \(xyz=0\);
- graph homology \(H_1(G)\), kept as rational-integrand topology.

Sector-specific coefficient geometry and data:

- Cayley--Menger residue surface;
- pole divisors and signed minor boundaries;
- \(D_\infty\) and the Legendre/Kummer quotient;
- rank-seven algebraic kernel and unresolved extension;
- physical relative/Borel--Moore chain.

Unresolved coefficient-letter datum:

\[
\mathcal Q
\]

is a printed radicand; its support placement is not proved.

Genuinely new carrier datum:

\[
\boxed{\text{none found}.}
\]

Graph \(H_1(G)\) and elliptic \(H^1(D_\infty)\) remain distinct types.

## Boundary and prohibited repairs

Do not:

- change \(q_{\mathcal G_{12}}=E+y_{12}\);
- conflate the full-eight and active-five sets;
- fit elliptic points to replace the surface divisors;
- promote the formal \(M_A\) resultant to source provenance;
- call \(\mathcal Q=0\) proved coefficient support;
- infer no intersections from \(\mathcal Q\nmid P\);
- assign elliptic Tate ranks to the full relative object;
- identify graph \(H_1\) with elliptic \(H^1\);
- add carrier cells, support summands, or post hoc gauges.

Entries 150 and 155 remain unchanged. This entry does not compute generic
\(\mathcal L_1\), companion \(P\), the nine-master connection, or the
physical relative chain.

## Consequence and next falsifier

Two stronger candidates fail narrowly:

\[
\boxed{\text{the full coefficient object is not merely a punctured elliptic curve};}
\]

\[
\boxed{\text{the direct frozen linear marked geometry does not derive a whole }
\mathcal Q\text{ divisor}.}
\]

H2 survives only as an open refined hypothesis:

\[
\boxed{
\text{shared existing energy/Cut carrier}
+
\text{shared support-sensitive derived/six-functor calculus}
+
\text{sector-specific surface-level relative/log coefficients}.
}
\]

The elliptic \(H^1\) is the infinity-Gysin quotient, not the full object.
The negative factor test is not positive evidence for \(\mathcal Q\)-support.

The next finite falsifier is:

1. construct the source-defined log/Borel--Moore pair and lifted physical
   chain for the nine equation-(58) masters;
2. derive its exact relative Gauss--Manin connection;
3. compute local residue and monodromy on one generic transverse
   \(\mathcal Q=0\) slice.

If there is no nontrivial \(\mathcal Q\)-supported extension or
half-character, the remaining marked-relative \(\mathcal Q\) hypothesis is
falsified. A surviving canonical class must also expose the missing generic
\(\mathcal L_1\) or companion-\(P\) projection.

## Evidence

- arXiv:2408.16386v2, equations (6), (7), (13), (14), (51), (52),
  (57)--(59), and (63);
- research/benincasa/check_marked_relative_q.rs at SHA-256
  c9ed2b8ae22ee8e340708dc5c7872eaf57e3395bbcad175112f0e603bc4f85f3;
- Narada runs run-6a344537606246e6bdec13ec1bde7689,
  run-65877a0dc8244419a27d5543103687ea,
  run-17c67923c8cb4047b17d04d8020a6a6d,
  run-66ed86e70f914366bf610121762a3392,
  run-6cc82ba9a75d41f7b14a67c0739f18fe,
  run-f26a7ee359b445a1ba903fa7889497fc, and
  run-c4bd3bfb86aa4a47b3ac902c90e29b78.

## Outcome contract

~~~json
{
  "claim": "On the literal q_G12 Cayley-Menger residue surface, none of the 41 frozen direct linear collision candidates has the full source quartic Q as a divisor factor; separately, the corrected rank-two infinity-Gysin quotient has unipotent generic total-energy monodromy with rank N=1 and N^2=0.",
  "status": "proved_narrow",
  "assumptions": [
    "The arXiv:2408.16386v2 normalization and q_G12=E+y12 are frozen.",
    "The census is limited to eight source lines, twelve reduced signed faces, and twenty-one nonparallel source-line pairs.",
    "The nearby-cycle statement is restricted to the rank-two elliptic quotient on xy(x+y)!=0."
  ],
  "evidence_refs": [
    "arXiv:2408.16386v2 equations (6), (7), (13), (14), (51), (52), (57)-(59), and (63)",
    "research/benincasa/check_marked_relative_q.rs at SHA-256 c9ed2b8ae22ee8e340708dc5c7872eaf57e3395bbcad175112f0e603bc4f85f3",
    "ledger entries 150 and 155",
    "Narada exact-check, nearby-cycle, and hostile-review runs recorded in Evidence"
  ],
  "factorization_test": {
    "full_eight_restricted_lines": "frozen",
    "active_five_poles": "distinguished",
    "signed_CM_faces": 12,
    "nonparallel_source_line_pairs": 21,
    "tested_collision_candidates": 41,
    "Q_divides_any_tested_candidate": false,
    "formal_M_A_resultant": "A Q, without a source-fixed projection",
    "pure_elliptic_monodromy": "unipotent, rank N=1, N^2=0",
    "full_marked_relative_nearby_cycles": "open"
  },
  "counterevidence": [
    "The marks are divisors on a surface, not merely points on the infinity elliptic curve.",
    "The formal M_A resultant is not attached to a printed source denominator or companion P.",
    "The slice test excludes a whole Q factor but not isolated intersections or nonlinear and extension realizations.",
    "The physical relative/Borel-Moore chain and semistable log model are not constructed."
  ],
  "next_experiment": "Construct the source-fixed nine-master log/Borel-Moore pair and physical chain, derive its relative Gauss-Manin connection, and compute its residue and monodromy on a generic transverse Q=0 slice."
}
~~~


# Flavor nine-link conventions (marici.Figueiredo)

Source: N. Arkani-Hamed, C. Figueiredo, L. J. Hall, C. A. Manzari,
*The Very Nearly Right Theory of Flavor*, arXiv:2607.27315v1 (2026-07-29).
Local copy of the arXiv HTML text extraction:
`research/flavor/sources/2607.27315v1.txt` (equation numbers below are the
paper's; `S`-numbers are its appendices).

This document fixes the conventions used by all marici flavor checkers.
It records only what the source states, with the source's own qualifications.

## 1. Nodes and edges

- Nine field nodes: left-handed doublets $q_i$ and right-handed singlets
  $u^c_j$, $d^c_j$, with $i,j\in\{1,2,3\}$.
- Up-type edge $(i,j)$ exists iff $Y^u_{ij}\neq 0$; it connects $q_i$ to
  $u^c_j$. Down-type edge $(i,j)$ exists iff $Y^d_{ij}\neq 0$; it connects
  $q_i$ to $d^c_j$. Row index = doublet ($q$) index in both sectors.
- The link diagram is the graph on nine nodes with one edge per nonzero
  Yukawa entry; up-type and down-type edges are distinguished (in the
  paper's figures by placement: $u^c$ nodes one side, $d^c$ the other).

## 2. Nine-link textures

- A nine-link texture is a pair of full-rank $3\times3$ matrices
  $(Y_u,Y_d)$ with **nine total nonzero entries** and a **single closed
  loop** carrying the single rephasing invariant (main text; App. V.a).
- Scan restrictions used by the paper: entry splits $4{+}5$, $5{+}4$,
  $6{+}3$, $3{+}6$ between $Y_u$ and $Y_d$; $(3,3)$ entries of both
  matrices nonzero; the loop has $4$ or $6$ links, contained in one matrix
  or spanning both.
- Flavor space: $Y_{u,d}$ have $36$ real d.o.f.; the physical quotient by
  $U(3)_Q\times U(3)_{u^c}\times U(3)_{d^c}$ leaves
  $36-3\cdot 9+1=10$ observables (6 eigenvalues, 3 CKM angles, 1 CKM
  phase). Nine entries plus one phase $=10$ parameters: the textures are
  designed as full parametrizations, "by design all equivalent under
  $U(3)^3$ rotations" (main text).

## 3. Rephasing action

- Node rephasing = independent $U(1)$ phase per field:
  $q_i\to e^{i\alpha_i}q_i$, $u^c_j\to e^{i\beta_j}u^c_j$,
  $d^c_j\to e^{i\gamma_j}d^c_j$, inducing
  $Y^u_{ij}\to e^{i\alpha_i}Y^u_{ij}e^{-i\beta_j}$,
  $Y^d_{ij}\to e^{i\gamma'_i}Y^d_{ij}e^{-i\delta_j}$ with
  $\alpha=\gamma'$ on shared $q$ nodes.
- By node rephasings every link can be made real and positive except one
  link in the closed loop, which carries $e^{i\varphi}$ (main text;
  App. V.a).
- Phase-placement rule used by the paper for definiteness: the
  phase-carrying entry is the down-type loop entry with smallest row and
  column index; if the loop has no down-type entry, the smallest up-type
  entry (App. V.a, footnote 7).

## 4. Loop monomial and its phase

- Orient the closed loop; the rephasing invariant is the product of loop
  entries, a given link appearing **conjugated if its arrow points towards
  a $q$ node** (App. V.a). The two orientations differ by
  $\varphi\to-\varphi$.
- Example (Fig. 2, left):
  $\varphi=\operatorname{Arg}\bigl(Y^u_{12}\,Y^{u\star}_{22}\,Y^d_{22}\,Y^{d\star}_{12}\bigr)$.
- Quotation convention: throughout the paper $\varphi$ is quoted up to
  complex conjugation and up to adding/subtracting $\pi$ (footnote 4).
- Rephasing invariance holds because each node appears equally often as
  source and sink of oriented loop edges — verified symbolically in the
  checker.

## 5. Cycle rank

- For a connected graph with $V=9$ nodes and $E=9$ edges,
  $b_1=E-V+1=1$: a unique independent cycle. The checker verifies
  connectivity and $b_1$ for each test texture and audits
  disconnected/exceptional cases separately (they are not valid nine-link
  textures: disconnected with full rank is possible only with a loop-free
  component, in which case there is no phase or the texture fails the
  single-loop requirement).

## 6. Perfect matchings and determinants

- Each term of $\det Y$ is a perfect matching of the bipartite graph of
  $Y$ (edges touching all nodes exactly once); the matching's sign is the
  permutation sign.
- Fig. 2 texture: single perfect matching in each sector,
  $\det Y_u=Y^u_{11}Y^u_{22}Y^u_{33}$,
  $\det Y_d=Y^d_{12}Y^d_{21}Y^d_{33}$ (Eq. 8).
- Source claim: in almost all nine-link textures each sector has a single
  perfect matching, so the phase can be placed on a loop link belonging to
  no determinant matching, giving $\arg\det(Y_uY_d)=0$. Of the
  $29+35+35$ fixed-phase textures only $5$ fail this, all diagonal in one
  sector (main text, "Spontaneous CP violation and Strong CP").
- Scope: graph-combinatorial reality of the determinant only. The paper
  itself notes a full strong-CP solution additionally requires spontaneous
  CP violation and UV completion; radiative stability is not established.

## 7. Equivalence relations (keep distinct)

1. **Diagonal rephasings** ($U(1)^9$ on nodes): preserve the chart and
   $\varphi$.
2. **Row/column permutations** $S_3^Q\times S_3^{u^c}\times S_3^{d^c}$:
   map textures to textures; the paper's numerical class identification
   requires entry magnitudes to match to $5\%$ and $|\varphi|$ to
   $0.1^\circ$ (App. V.a).
3. **Texture-chart transitions**: different zero patterns representing the
   same physical point. The source asserts all nine-link textures are
   $U(3)^3$-equivalent as parametrizations, but a generic $U(3)^3$
   rotation does not preserve a zero pattern and "might not preserve
   $\varphi$" (main text, "Fixing the Yukawa rephasing invariant").
4. **Full $U(3)^3$ weak-basis equivalence**: preserves the 10 physical
   observables; preserves neither the chart nor, in general, $\varphi$.
   After fixing $\varphi$, the paper mods out only by the residual
   rotations that do preserve $\varphi$ (App. V.b).
5. **Weak-basis invariants**: singular values of $Y_u,Y_d$; CKM data;
   $J$; equivalently traces of words in $H_u=Y_uY_u^\dagger$,
   $H_d=Y_dY_d^\dagger$ and $\det[H_u,H_d]$.

## 8. Yukawa triangle and CKM map

- Ratios along the loop define complex numbers, e.g. class 4
  ($\varphi=\pi/2$, Fig. 2):
  $U_{12}=Y^u_{12}/Y^u_{22}$, $D_{12}=Y^d_{12}/Y^d_{22}$, and at leading
  order (Eq. 6)
  $\dfrac{V_{td}V^*_{tb}}{V_{ud}V^*_{ub}}\sim\dfrac{D_{12}}{U_{12}}$.
- The **Yukawa triangle** is the triangle with sides defined by such loop
  ratios; at leading order in small flavor parameters it coincides with
  the unitarity triangle in most classes; corrections are calculable
  (App. III).
- Ratios
  $R_\alpha=-\frac{V_{td}V^*_{tb}}{V_{ud}V^*_{ub}}$,
  $R_\beta=-\frac{V_{cd}V^*_{cb}}{V_{td}V^*_{tb}}$,
  $R_\gamma=-\frac{V_{ud}V^*_{ub}}{V_{cd}V^*_{cb}}$
  (Eqs. 1, 5). Fixed-Yukawa-triangle fits use
  $|R_\alpha|=1/\tan(\pi/8)$, $|R_\beta|=1/\cos(\pi/8)$,
  $|R_\gamma|=\cos(3\pi/8)$ (main text; App. V.c).
- Leading-order monomials per equivalence class are tabulated in the
  paper's Tab. S3. Three $3\pi/8$ classes (a, b, c) are accidental, not
  structural.

## 9. Fit inputs (App. V.a, Tab. S2, at $M_Z$)

Six Yukawa singular values, six CKM magnitudes, three angles, plus ratios
$y_u/y_d=0.473\pm0.017$ and $y_s/\bar y_{ud}=27.30\pm0.08$; Gaussian
$\chi^2$ over 17 observables; exact CKM unitarity imposed. Key central
values: $y_u=7.04\times10^{-6}$, $y_c=3.56\times10^{-3}$, $y_t=0.967$,
$y_d=1.54\times10^{-5}$, $y_s=3.06\times10^{-4}$, $y_b=1.630\times10^{-2}$,
$|V_{us}|=0.22517$, $|V_{ub}|=0.003763$, $|V_{cb}|=0.04189$,
$|V_{cd}|=0.22503$, $|V_{td}|=0.00863$, $|V_{ts}|=0.04117$,
$\alpha=84.1^\circ\pm3.7^\circ$, $\beta=22.6^\circ\pm0.5^\circ$,
$\gamma=66.4^\circ\pm2.8^\circ$.

## 10. Worked examples used by the checkers

- **Example I** (Eq. S38, $\varphi=\pi/2$, class 4 / Fig. 2):
  $Y_u$ nonzero at $(1,2),(2,1),(2,2),(3,3)$;
  $Y_d$ nonzero at $(1,2),(2,1),(2,2),(2,3),(3,3)$.
- **Example II** (Eq. S43, $\varphi=-\pi/8$):
  $Y_u$ at $(1,1),(1,3),(2,2),(3,3)$;
  $Y_d$ at $(1,1),(1,3),(2,3),(3,2),(3,3)$.
- **Example III** (Eq. S48, $\varphi=5\pi/8$):
  $Y_u$ at $(1,1),(2,2),(2,3),(3,3)$;
  $Y_d$ at $(1,2),(1,3),(2,2),(3,1),(3,3)$.
- **$\pi/4$ example** (Eq. S53): $Y_u$ at $(1,1),(2,2),(2,3),(3,3)$;
  $Y_d$ at $(1,3),(2,1),(2,2),(3,2),(3,3)$; the $\pi/4$ peak is an
  accident tied to
  $\frac{y_s^2}{y_b^2}\bigl|\frac{V_{us}}{V_{ub}}\bigr|^2\simeq\sqrt2$
  (Eqs. S56–S59), not a triangle identity.

## 11. What the source does and does not claim

- Established in-source: empirical clustering of fitted $\varphi$ near
  multiples of $\pi/8$; leading-order identification of one CKM angle with
  $\varphi$ in most classes; calculable subleading deviations.
- Not claimed in-source: a UV symmetry derivation of the phases;
  invariance of $\varphi$ under the full $U(3)^3$; a complete strong-CP
  solution.

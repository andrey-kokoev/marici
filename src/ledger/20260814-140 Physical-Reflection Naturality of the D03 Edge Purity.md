# Physical-Reflection Naturality of the D03 Edge Purity

## Record

Date: 2026-08-14

Status: exact scoped target theorem. The physical reflection \(f_3\) acts
strictly on the established absolute support-PC target and exchanges the
\(D03\) \(x_3\)- and \(x_4\)-edge purity packets. This removes target purity
as an independent source of the binary obstruction of entries 138--139. It
does not construct the endpoint-coherent source connector whose square
defines that obstruction.

## The target reflection is strict

Let

\[
P_j=
\left[
A\langle g_j,h_j\rangle
\xrightarrow{(x_j,u_j)}
A\langle p_j\rangle
\right],
\qquad j=3,4,
\]

be the two Cartier edge packets extracted from the entry-105 absolute
oriented-boundary-blowup complex. The physical reflection fixes \(D03\) and
acts on the short labels by

\[
x_0\leftrightarrow x_1,\qquad
x_2\leftrightarrow x_5,\qquad
x_3\leftrightarrow x_4.
\]

Exact enumeration of all 215 loaded generators proves that this permutation
extends to a semilinear chain involution of the absolute complex. In the
oriented local bases of \(P_3\) and \(P_4\), its matrix is

\[
f_3|_{P_3}=-I_3,
\qquad
f_3|_{P_4}=-I_3,
\qquad
f_3^2=1.
\]

The sheet vertices and the two endpoint pairs are exchanged as required:

\[
v_+\leftrightarrow v_-,
\qquad
v_{00}\leftrightarrow v_{11},
\qquad
v_{10}\leftrightarrow v_{01}.
\]

The full absolute differential is covariant generator by generator and
monomial by monomial, not merely on homology.

## Purity, Tor, and Cousin terms are natural

The entry-131 finite Cartier identification

\[
E_{j,\mathrm{src}}\otimes\operatorname{or}(x_j)[-1]
\simeq
R\!\operatorname{Hom}_A(A/(x_j),P_j)
\]

is natural under \(f_3\). The filtration-preserving endomorphism calculation

\[
f_1=
\begin{pmatrix}a&b\\0&e\end{pmatrix},
\qquad f_0=e,
\]

still has the exact Bockstein constraints \(a=e\) and \(b=0\). Thus the
normalized purity line is carried from \(j=3\) to \(j=4\), and back, with
square one.

The repeated-normal data are retained with their labels:

\[
\eta_3=(-q_3,-1)
\longmapsto
\eta_4=(-q_4,-1),
\]

\[
[t_3]\eta_3
\longmapsto
[t_4]\eta_4.
\]

Both \(\operatorname{Tor}_0\) and \(\operatorname{Tor}_1\) are transported
rather than projected away. The reciprocal-regular/original-Borel--Moore
pairing is likewise preserved with its Laurent unit:

\[
\beta_j(p_j,h_j^\vee)=1,
\qquad
\beta_j(h_j,p_j^\vee)=-q_j.
\]

The occurrence endpoint ideals and the full four-normal residue ideal are
permuted functorially. Exact exterior-incidence checks include every lower
Koszul--Cech term, not only the top fractions:

\[
(x_0,x_3)\leftrightarrow(x_1,x_4),
\qquad
(x_1,x_3)\leftrightarrow(x_0,x_4),
\]

\[
(u_0,u_1,u_3,u_5)
\leftrightarrow
(u_0,u_1,u_2,u_4).
\]

The positive physical normal \([dX_{03}]\) remains a separate line.

## Consequence for the reflection obstruction

Entry 138 proves that the road orientation and the once-retained polarity
line are both odd under \(f_3\). Their relative product is therefore even:

\[
(-1)_{\mathrm{road}}\,
(-1)_{\mathrm{pol}}=+1.
\]

Together with the strict target involution, this proves

\[
\boxed{
\Omega^{\mathrm{target}}_{03}=1.
}
\]

This is a reduction theorem, not the conclusion
\(\omega_{\mathrm{load}}(f_3,f_3)=0\). The global reflection square compares
two loaded endpoint-coherent two-extension maps. Only the target-side purity
comparison is now strict. The source/support-Yoneda connector, including its
nonzero generic \(Q\)-leg and endpoint two-cells, is still absent.

The next experiment is therefore smaller and sharper: construct the
\(f_3\)-paired source connector, compare it to this fixed strict target
involution, and evaluate the remaining square modulo two. Any odd defect
must now come from that source/endpoint comparison rather than from local
target purity.

## Evidence

Exact certificate:

- research/voevodsky/check_d03_physical_reflection_edge_purity.rs
- SHA-256
  23be01f0619b4813956c9d65f08aaa1ead6ff0cca6abaac7ae4234806646a89e

Verification:

~~~text
rustfmt --edition 2021 --check
rustc --edition 2021 -D warnings -O
executable exit 0
JSON output parses with status=proved
~~~

## Boundary

The theorem is scoped to the entry-105 absolute complex and the entry-131
definitionally scoped road-face Cartier purity. It does not provide:

- the endpoint-coherent support/Yoneda-to-Tate connector;
- a nonzero generic \(Q\)-leg;
- the global value of \(\omega_{\mathrm{load}}\);
- the scalar total-specialization differential \(d_{\mathrm{sp,sc}}\);
- the full \(G_{03}^{\mathrm{Cousin}}\) chain map.

No numerical denominator, rational splitting, fitted transition, or new
generator is used.

Epistemic-graph admission remains pending while the Marici loader transport
is closed. The registered worker-delegation, delegated-task, and
epistemic-graph surfaces were confirmed through the registrar; no graph or
MCP configuration file was edited manually.

## Outcome contract

~~~json
{
  "claim": "The entry-105 absolute support-PC target and the definitionally scoped D03 Cartier edge purity admit a strict semilinear physical f3 involution exchanging x3 and x4. Both repeated-normal Tor grades, the graph Bockstein, reciprocal/BM pairing, endpoint maps, and all lower Koszul--Cech terms are natural. With the once-retained polarity line, the target-side reflection square is +1.",
  "status": "proved",
  "assumptions": [
    "The entry-105 universal absolute differential and labelled cellular orientations are used.",
    "The entry-131 source is the independently assembled x_j Thom-plus-original/BM packet.",
    "The graph relation u_j=t_j*x_j is retained without globally inverting x_j or u_j.",
    "Entry 138 supplies the separate road-orientation and polarity characters."
  ],
  "factorization_test": {
    "absolute_generators": "215 with ranks 14,63,93,45",
    "absolute_d_squared": "pass",
    "physical_f3_covariance": "pass on every loaded generator and monomial",
    "edge_exchange": "x3<->x4 with local action -Id",
    "cartier_purity": "strictly natural",
    "tor0_tor1": "both retained and label-covariant",
    "graph_bockstein": "[t3]eta3 -> [t4]eta4",
    "reciprocal_BM_pairing": "(1,-q3) -> (1,-q4)",
    "lower_koszul_cech": "all subset differentials commute",
    "endpoint_exchange": "v00<->v11 and v10<->v01",
    "loaded_target_square": "+1"
  },
  "counterevidence": [
    "A strict target involution is not a path between the global loaded support/Yoneda and Tate/Cartier two-extensions.",
    "The nonzero generic Q leg and endpoint connector two-cells remain absent.",
    "The global omega_load is still undefined; target strictness alone cannot decide its parity."
  ],
  "next_experiment": "Construct the f3-paired endpoint-coherent source connector with its nonzero Q leg and compare its square against the strict target involution. Then evaluate omega_load(f3,f3) mod 2."
}
~~~

# Two-Support MV Excess and the Missing D03 Chart/Generic Leg

## Record

Date: 2026-08-15

Status: proved coefficient and finite-label obstruction theorem. The
two-support Mayer--Vietoris packet and the actual endpoint-relative corridor
have matching primitive rank-one shadows, but the packet has neither the
middle \(D03\) support labels nor a legal BM--Cech representative of either
repeated-\(u_3\) Tor grade. No graph admission or global nonexistence theorem
is claimed.

## The canonical two-support MV triangle

Work over the unlocalized normal coefficient ring and put

\[
I_+=(u_1,u_3,u_5),
\qquad
I_{03}=(u_0,u_3),
\qquad
J=I_++I_{03}=(u_0,u_1,u_3,u_5).
\]

For the fixed Koszul/Cech convention, define the two-support overlap object

\[
\mathcal M_{+,03}
:=operatorname{Cone}\!\left(
K(I_+)\oplus K(I_{03})
\xrightarrow{\rho_+-\rho_{03}}
K(J)
\right)[-1].
\]

It sits in the canonical Mayer--Vietoris triangle

\[
\boxed{
\mathcal M_{+,03}
\longrightarrow K(I_+)\oplus K(I_{03})
\xrightarrow{\rho_+-\rho_{03}}K(J)
\longrightarrow\mathcal M_{+,03}[1].
}
\]

The two ideals share exactly the factor \(u_3\). The excess exterior
generator for this repeated normal gives

\[
\operatorname{Tor}_0=R/J,
\qquad
\operatorname{Tor}_1=R/J,
\qquad
\operatorname{Tor}_{k>1}=0.
\]

Both grades are primitive and there is no integer torsion. This is the
coefficient-level repeated-\(u_3\) excess; it is not yet a spatial
Mayer--Vietoris square in the associahedral support category.

## Entry-100 residue as an overlap class

Entry 100's reciprocal/original bivariant evaluation gives the local excess
residue on the overlap summand. In the Mayer--Vietoris cone it has the form

\[
\eta_{\rm mix}in H^*(\mathcal M_{+,03}),
\qquad
\eta_{\rm mix}|_{I_+}=0,
\qquad
\eta_{\rm mix}|_{I_{03}}=0.
\]

Thus the residue is an overlap class with zero arm restrictions. The
reciprocal lines and wedge evaluation reproduce its coefficient and sign
pattern without putting inverse normals on the source. This proves a local
coefficient compatibility only. It does not provide an ordinary BM--Cech
representative in entry 143's face-indexed target.

## The actual four-edge corridor

The endpoint-relative marked \(D03\) corridor is

\[
v_+\xrightarrow{e_0}m_+
\xrightarrow{e_1}c
\xrightarrow{e_2}m_-
\xrightarrow{e_3}v_-.
\]

After quotienting the endpoints, its boundary matrix is

\[
\partial_{m rel}
=
\begin{pmatrix}
1&-1&0&0\\
0&1&-1&0\\
0&0&1&-1
\end{pmatrix}.
\]

Therefore

\[
H_1(C_{\rm corr},\{v_+,v_-\};\mathbb Z)
=\mathbb Z\langle(1,1,1,1)\rangle.
\]

The route line is primitive and saturated; unit maximal minors show that it
has no integer torsion. This agrees numerically with the rank-one
\(\operatorname{Tor}_1\) excess shadow.

The agreement of ranks is not a labelled map. The middle edges carry

\[
e_1:\{D03,x_3\},
\qquad
e_2:\{D03,x_0\},
\]

including the \(X_{D03}\) occurrence line, the \(u_{D03}\) normal line, and
the \(D03\) circle state. None occurs in \(I_+\), \(I_{03}\), or \(J\).
Label preservation forces the middle coefficients to vanish; the three
boundary equations then force all four edge coefficients to vanish. Hence

\[
\operatorname{Hom}_{\rm strict,label}^{\rm unnorm}
(C_{\rm corr},\mathcal M_{+,03})=\{0\},
\]

while the endpoint-normalized graded-map space is empty.

The first strict obstruction is therefore absence of an object in either
middle \(D03\)-labelled edge grade. It occurs before Laurent localization,
torsion, residue normalization, or parity.

## Five-chart nerve audit

Retain all five corridor charts \(S_0,\ldots,S_4\), not only the four route
edges. Their route-pair intersections are

\[
S_{01},\quad S_{12},\quad S_{23},\quad S_{34},
\]

and the additional nonconsecutive pair intersections are

\[
S_{02}=\{x_3\},
\qquad
S_{13}=\{D03\},
\qquad
S_{24}=\{x_0\}.
\]

The nonempty triple intersections are

\[
S_{012}=\{x_3\},
\qquad
S_{123}=\{D03\},
\qquad
S_{234}=\{x_0\}.
\]

Restriction of the full target \(E=F_K/F_V\) to this nerve is tautological:
each face-indexed state restricts only along actual inclusions of its support
and retains its circle set. This full nerve does not repair the two-support
packet. The excess generator \(\eta_{\rm mix}\) is legal in no vertex,
pair-overlap, triple-overlap, or circle summand of the ordinary target-side
BM--Cech diagram. In particular, neither \(\operatorname{Tor}_0\) nor
\(\operatorname{Tor}_1\) has an ordinary BM--Cech representative.

This is the coefficient/variance gate: the abstract overlap class exists,
but a reciprocal line-dual extraordinary comparison is required to place it
against the original-BM target without forbidden circle denominators.

## Why the gallery shadow still fails generically

Entries 106--110 provide the positive lcm-kernel shadow and marked local
gallery data. They do not supply the missing \(D03\) chart. Their gallery is
supported in \(F_1\), so its image in

\[
Q=F_K/F_B
\]

is zero. After the coefficient/variance gate, the first generic chain
equation is still

\[
dH=q_J-x_3\widetilde\xi_{03}.
\]

The local gallery can retain the Cartier term
\(-x_3\widetilde\xi_{03}\), but it has killed or quotiented the generic
\(q_J\) leg. Consequently it cannot realize a chain-level comparison that
is simultaneously nonzero on \(Q\) and equal to the entry-100 overlap
residue.

The order matters:

1. the two-support MV object first fails to contain the \(D03\)-labelled
   middle chart and a legal representative of either Tor grade;
2. after an extraordinary coefficient repair, the spatial gallery still
   lies in \(F_1\) and maps to zero in \(Q\); and
3. only a new spatial correspondence can join the retained generic leg to
   the overlap residue.

## The exact missing logarithmic BC arrow

The required new datum is not another unlabelled rank-one identification.
It is a support-typed logarithmic Beck--Chevalley morphism

\[
\boxed{
\operatorname{BC}^{\log}_{+;03}:
\mathcal S^{\rm preQ}_{+;03}
\longrightarrow
\mathcal E^{\rm BM,\check C}_{+;03}
}
\]

in a ringed correspondence category. Its source must contain an exceptional
long-\(D03\) chart and both incidence maps to the middle corridor edges. It
must:

- retain the pre-quotient generic generator \(q_J\) and map it nontrivially
  to the fixed entry-143 \(Q03\) leg;
- restrict on the overlap to the entry-100 class \(\eta_{\rm mix}\);
- retain both repeated-\(u_3\) grades \(\operatorname{Tor}_0\) and
  \(\operatorname{Tor}_1\);
- distribute the lower terms across the actual five-chart nerve with legal
  reciprocal/BM variance;
- reproduce the local Cartier specialization
  \(-[\widetilde\xi_{03}]\); and
- provide the entry-160 localization-triangle homotopy
  \[
  \delta_E\alpha_U(q_J)
  \simeq
  \alpha_Z[1]\delta_S(q_J).
  \]

No existing two-support MV arrow, lcm kernel, or corridor carrier constructs
\(\operatorname{BC}^{\log}_{+;03}\). Its overlap residue, local Cartier
value, and generic \(Q\) value are acceptance tests, not definitions.

## Consequence for the framed mapping fiber

Without \(\operatorname{BC}^{\log}_{+;03}\), the global branch-to-\(Q\)
component and its endpoint coherences are absent. Therefore the framed
endpoint/\(Q\) mapping fiber of entries 158 and 164 remains uninstantiated,
and reflection parity remains undefined.

## Anti-circularity controls

- Do not identify the primitive corridor line with the primitive
  repeated-\(u_3\) Tor line by rank alone.
- Do not erase the \(D03\) occurrence, normal, or circle labels on the two
  middle edges.
- Do not regard the abstract overlap class as a legal target BM--Cech
  representative.
- Do not omit the non-route pair and triple intersections of the five-chart
  nerve.
- Do not fill \(q_J\), set its \(Q\) image to zero, or derive it from the
  desired residue.
- Do not infer graph admission, a ringed DNC chart, Beck--Chevalley, endpoint
  pointing, or parity from the rank-one shadows.
- Do not invert a polynomial source parameter or an integer.

## Falsifiers and scope

The strict label obstruction would be falsified by an actual object in the
two-support MV diagram carrying both middle-edge \(D03\) occurrence and
normal-circle labels, together with a nonzero endpoint-normalized strict
route map. The BM--Cech obstruction would be falsified by a legal existing
vertex/overlap/circle summand representing \(\eta_{\rm mix}\) in both Tor
grades.

The geometric boundary would be crossed by an independently constructed
exceptional \(D03\) chart and ringed spatial incidence maps whose proper
extraordinary push--pull yields \(\operatorname{BC}^{\log}_{+;03}\), retains
\(q_J\), and passes the local residue and localization tests.

No general no-go is claimed after adjoining such geometry. In particular,
the theorem does not exclude a three-support or logarithmically expanded
correspondence.

## Exact certificate

The exact checker is

- `research/voevodsky/check_d03_corridor_two_support_mv_label_gate.rs`.

Its SHA-256 hash is

`e6ba0f0a2535f4338b9027124cb3d834d45161cb41c2b55f93d44baaede1ad8b`.

It verifies the saturated primitive corridor line, the two-support ideals
and repeated-\(u_3\) Tor ranks, every missing middle-edge label, the zero-only
unnormalized strict map, and emptiness of the endpoint-normalized map space.
The five-chart nerve and BM--Cech legality audit above use the fixed
entry-143 face/circle restriction rule and do not claim an additional
checker.

## Next experiment

Adjoin one exceptional long-\(D03\) chart with its occurrence and circle
lines and construct its two ringed incidence maps to the middle corridor
edges. Recompute the full five-chart hypercover and build the extraordinary
overlap comparison retaining both Tor grades. Then test whether the induced
\(\operatorname{BC}^{\log}_{+;03}\) maps the retained \(q_J\) nontrivially
to \(Q03\), restricts to \(\eta_{\rm mix}\), and satisfies the entry-160
localization square. Only afterward assemble endpoints or evaluate parity.

## Outcome contract

~~~json
{
  "claim": "The actual endpoint-relative D03 corridor and the two-support MV excess have matching primitive rank-one shadows, but no strict label-preserving realization exists: the MV packet lacks both middle D03 grades, and neither repeated-u3 Tor grade has an ordinary representative in the legal five-chart target BM-Cech nerve.",
  "status": "falsified",
  "scope": "strict line-labelled realization by the two-support MV packet and ordinary target-side BM-Cech representatives only; no no-go after adding an exceptional D03 chart and spatial extraordinary correspondence",
  "assumptions": [
    "I_plus=(u1,u3,u5), I_03=(u0,u3), and J=(u0,u1,u3,u5) remain unlocalized polynomial support ideals.",
    "The actual four-edge corridor labels and entry-143 face/circle BM-Cech rules remain fixed.",
    "The generic q_J leg and local Cartier class are retained as independent acceptance data.",
    "No exceptional D03 chart, fitted filler, or graph admission is adjoined."
  ],
  "factorization": {
    "MV_triangle": "M_(+,03) -> K(I_plus)+K(I_03) -> K(J) -> M_(+,03)[1]",
    "common_normal": "u3",
    "Tor0": "R/J, primitive rank one",
    "Tor1": "R/J, primitive rank one",
    "higher_Tor": "zero",
    "entry100_eta_mix": "abstract overlap class with zero arm restrictions",
    "corridor": "v_plus -> m_plus -> c -> m_minus -> v_minus",
    "relative_H1": "Z generated primitively by (1,1,1,1)",
    "middle_edge_labels": [["D03", "x3"], ["D03", "x0"]],
    "missing_labels": ["X_D03 occurrence", "u_D03 normal", "D03 circle"],
    "unnormalized_strict_maps": "zero only",
    "endpoint_normalized_maps": "empty",
    "five_chart_pair_intersections": ["S01", "S12", "S23", "S34", "S02={x3}", "S13={D03}", "S24={x0}"],
    "five_chart_triple_intersections": ["S012={x3}", "S123={D03}", "S234={x0}"],
    "target_E_restriction": "tautological face/circle restriction",
    "eta_mix_legal_BM_Cech_summands": "none",
    "ordinary_BM_Cech_Tor_representatives": "absent for Tor0 and Tor1",
    "gallery_support": "F1 and therefore Q-zero",
    "first_generic_equation": "dH=q_J-x3*xi_03",
    "BC_log_plus_03": "unconstructed",
    "global_framed_mapping_fiber": "uninstantiated",
    "parity": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_corridor_two_support_mv_label_gate.rs",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md",
    "src/ledger/20260814-107 Integral Ambient Log-Blowup Invariance and the Persistent Bivariant Q-Leg Gap.md",
    "src/ledger/20260814-108 Local D03 Exit Class and the Generic-Q Kernel Criterion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-160 Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell.md",
    "src/ledger/20260815-165 dP6 Common Refinement and the Log-Boundary Gysin Gate.md"
  ],
  "checker_sha256": "e6ba0f0a2535f4338b9027124cb3d834d45161cb41c2b55f93d44baaede1ad8b",
  "counterevidence": [
    "Rank-one corridor and Tor shadows do not carry the same support labels.",
    "The two middle corridor edges require D03 occurrence and circle grades absent from the MV ideals.",
    "The full five-chart nerve has no legal ordinary BM-Cech summand for eta_mix in either Tor grade.",
    "The established galleries lie in F1 and have zero image in the fixed Q quotient."
  ],
  "next_experiment": "Adjoin one exceptional long-D03 chart, construct its two ringed middle-edge incidence maps and full five-chart hypercover, then build BC_log_(+;03) retaining q_J, eta_mix, both Tor grades, and the local Cartier residue before endpoint or parity assembly."
}
~~~

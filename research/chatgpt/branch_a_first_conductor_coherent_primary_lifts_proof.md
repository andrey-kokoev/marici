# Branch A — first-conductor-weight coherent primary lifts

Date: 2026-09-07.

## Result and scope

The occurrence-weight-zero primary-fixed comparison space remains contractible in the tested coefficient model. At the first six conductor occurrence weights, it is no longer contractible. This remains true after strengthening the preceding endpoint-top frame to retain all endpoint states and their incoming differential equations.

In the regulator-normal grade of the recorded packet, the six component lattices have ranks

\[
(9,9,7,7,9,19)
\]

in the ordered short-coordinate list \((02,04,13,15,24,35)\). Their direct sum has rank sixty. Every connected component is contractible. Forgetting the chosen primary-comparison homotopy detects thirty-six of these directions and kills twenty-four.

These are exact calculations in a specified coefficient category. They do not construct the physical conductor–Morse comparison or select a value of \(\Delta_J\). The word “first” refers to the six fine occurrence weights \(\epsilon_d\), with coefficients constrained to the conductor ideal. We do **not** replace the whole complex by its first associated grade \(I/I^2\); higher-order coefficients needed for the lower chain equations remain.

## 1. Source, coefficient ring, and weights

Use the ordered diagonals

\[
\mathcal D=(02,03,04,13,14,15,24,25,35)
\]

and the coefficient ring

\[
R=\mathbb Z[\beta,X_d:d\in\mathcal D]
 / (X_eX_o:e\in\{02,04,24\},\ o\in\{13,15,35\}).
\]

Write

\[
I=(X_{02},X_{04},X_{13},X_{15},X_{24},X_{35}),
\qquad \Lambda=\mathbb Z[\beta].
\]

The complete corrected complex \(C_\beta\) has 430 states

\[
[F,H,\varepsilon],\qquad H\subseteq F,\quad\varepsilon\in\{0,1\},
\]

where \(F\) is any noncrossing dissection. Their homological degrees are

\[
3-|F|+|H|+\varepsilon.
\]

The radial term adds \(d\) to \(F\) with its cellular incidence sign and coefficient \(X_d\). Removing the native mark \(h\) contributes \(\beta X_h\) and the ordered Koszul sign. Removing the independent occurrence partner contributes \(X_{35}\), with the tensor sign. The native 35-circle and the occurrence partner remain different states.

Both endpoint packets are retained:

\[
V_-=\{02,04,24\},\qquad V_+=\{13,15,35\}.
\]

Their combined size is 32. The short-boundary subcomplex has 416 states. Its quotient \(Q\) has fourteen states, including the independent occurrence factor. Every differential column, support inclusion, and square-zero identity is reconstructed directly.

This is the integral unit-normalized coefficient family associated with

\[
u_d=e^{\beta X_d}-1=\beta X_dv_d,
\qquad v_d(0)=1.
\]

The formal exponential interpretation requires characteristic zero. The source's geometric purity theorem assumes nonzero \(\beta\); its extension to regulator zero is not inferred here.

Assign native marks regulator-normal weight one, \(\beta\) weight one, and the occurrence partner weight zero. A state contributes to occurrence weight \(m\) exactly when its coefficient exponents

\[
m+\mathbf 1_F-\mathbf 1_H-\varepsilon\mathbf 1_{35}
\]

are nonnegative, survive the two-sheet relations, and contain at least one short occurrence when conductor-relative coefficients are required. The remaining arbitrary coefficient is a polynomial in \(\beta\). Thus the calculations are exhaustive over \(\Lambda\), rather than bounded searches in regulator degree.

The last condition matters at \(m=\epsilon_{35}\): an occurrence-partner state can absorb the external occurrence weight without having a conductor coefficient. Those states are excluded from \(IC_\beta\). Treating all states in that occurrence slice as conductor-valued would give a different result.

## 2. A complete endpoint/Q frame as a genuine quotient

Let \(v\) be the graded projection onto all 32 endpoint states, and let \(q\) be the genuine chain projection onto \(Q\). The projection \(v\) alone need not be a chain map, because radial arrows enter endpoints.

Define

\[
N_n=\{c\in (IC_\beta)_n:q(c)=0,\ v(c)=0,\ v(dc)=0\}.
\]

This is a subcomplex: \(q\) commutes with the differential, and \(d^2=0\). It is the largest subcomplex contained in the graded kernel of the endpoint and Q evaluations.

The actual boundary object and its projection are

\[
\mathcal B=(IC_\beta)/N,
\qquad \rho:IC_\beta\longrightarrow\mathcal B.
\]

Unlike a projection onto the full endpoint packet, \(\rho\) is a chain map. The quotient retains all endpoint coefficients, the necessary incoming endpoint equations, and the complete Q quotient. It is an explicitly chosen coefficient frame, not an asserted description of the as-yet-unconstructed geometric frame.

The coherent boundary fibre is

\[
\mathcal F=\operatorname{fib}(\rho).
\]

On each computed occurrence component, the incoming endpoint equations have signed-unit coefficients and disjoint pivot columns. The checker constructs a saturated integral basis of their kernel and a complementary basis. In these coordinates,

\[
d=\begin{pmatrix}d_N&\alpha\\0&d_{\mathcal B}\end{pmatrix}.
\]

The fibre has coordinates \((n,b,h)\), with \(h\in\mathcal B_{k+1}\) in degree \(k\). Its projection to \(N\) is

\[
(n,b,h)\longmapsto n-\alpha h.
\]

The homotopy sends \((n,b,h)\) to \((0,h,0)\). Direct multiplication verifies the retract identity on every column. Consequently

\[
\mathcal F\simeq N.
\]

All boundary-comparison homotopies are included in this calculation. The reduction does not assume their absence or contract them by inverting a regulator.

## 3. Keep the primary-comparison homotopy

Use the two-term supported source

\[
S_\beta=[Re\xrightarrow{\beta}Rp],
\qquad |e|=3,\quad |p|=2,
\]

with regulator-normal weights three and two. Let \(P=Rp\subset S_\beta\).

The primary-fixed deformation complex is

\[
\mathcal T=\operatorname{fib}\left(
\operatorname{Hom}(S_\beta,N)\longrightarrow\operatorname{Hom}(P,N)
\right).
\]

The bounded free sources justify these Hom models for derived maps. For a nonzero chosen primary and a chosen lift, the same complex controls differences between lifts.

In homological degree \(n\), write a cochain as

\[
(a,b,h)\in N_{n+2}\oplus N_{n+3}\oplus N_{n+3}.
\]

Here \(a\) and \(b\) are the values on \(p,e\), and \(h\) is the primary-comparison homotopy. Its normal weight is measured against \(p\), not against \(e\).

The complete differential is

\[
D(a,b,h)=\bigl(da,\ db-(-1)^n\beta a,\ a-dh\bigr).
\]

There is an explicit cochain projection

\[
\Pi_n(a,b,h)=b-(-1)^n\beta h,
\]

onto \(\operatorname{Hom}(R[3],N)\). The inclusion sends \(c\) to \((0,c,0)\), and the contracting homotopy is

\[
\mathscr H(a,b,h)=(h,0,0).
\]

The checker verifies

\[
D\mathscr H+\mathscr HD=1-\iota\Pi,
\qquad \Pi\iota=1
\]

with the literal polynomial powers, including all negative internal-Hom degrees. Thus

\[
\mathcal T\simeq\operatorname{Hom}(R[3],N).
\]

For the associated coherent mapping space,

\[
\pi_i\mathscr T\cong H_{3+i}(N),\qquad i\ge0.
\]

In degree zero, the class of a primary-framed point is therefore determined by the closed chain

\[
b-\beta h.
\]

An ordinary homotopy of \((a,b)\) cannot be used without also tracking its effect on \(h\).

## 4. Complete first-conductor-weight calculation

The following are the entire kernel components over \(\Lambda\). Torsion entries refer to \(\beta\), not to integer primes.

| Occurrence weight | Kernel ranks in degrees 0,1,2,3 | Free \(H_3(N)\) rank | Minimal regulator grades of top generators |
|---|---|---:|---|
| \(\epsilon_{02},\epsilon_{04},\epsilon_{24}\), separately | \((3,25,60,46)\) | 9 | Six of grade 3, three of grade 2 |
| \(\epsilon_{13},\epsilon_{15}\), separately | \((3,25,60,44)\) | 7 | Six of grade 3, one of grade 2 |
| \(\epsilon_{35}\) | \((3,29,97,90)\) | 19 | Six of grade 3, twelve of grade 2, one of grade 1 |

There is no degree-four term in any of these conductor-relative components. Hence a nonzero top cycle is not a boundary, and all higher homotopy groups of the primary-fixed mapping space vanish.

The lower homology normal forms are also exported:

* For each negative-sheet direction: \(H_2=\Lambda\oplus(\Lambda/(\beta))^7\), \(H_1=(\Lambda/(\beta))^2\).
* For 13 and 15: \(H_2=\Lambda\oplus(\Lambda/(\beta))^9\), \(H_1=(\Lambda/(\beta))^2\).
* For 35: \(H_2=(\Lambda/(\beta))^{20}\), with no additional free lower group.

Every top generator has minimal regulator grade at most three. Multiplying it by the uniquely required nonnegative power of \(\beta\) gives a generator at the recorded primitive's grade three. The resulting connected-component lattice is

\[
\pi_0\mathscr T_{\epsilon_{02},3}\cong\mathbb Z^9
\]

and similarly has ranks nine, seven, seven, nine, nineteen at the other listed weights. Their direct sum is \(\mathbb Z^{60}\). Every connected component is contractible; the whole space is not.

The count nineteen at 35 does not assert a symmetry breaking in an independently specified physical theory. The tested complex has a distinguished occurrence-35 factor. Moving that factor under a polygon symmetry gives a different labelled complex and requires its transport map. No artificial rotation within one fixed correction is used here.

### Forgetting the primary comparison

For each of the six occurrence weights, the ordinary supported-map group at the recorded regulator grade is \(\mathbb Z^{12}\). Six directions change the primary class; the other six preserve it.

The forgetful map from primary-framed differences has rank six in every case. Its kernel ranks are three, three, one, one, three, thirteen in the order \((02,04,13,15,24,35)\).

Combining these independent fine weights gives the exact sequence of integral lattices

\[
0\longrightarrow\mathbb Z^{24}
\longrightarrow\mathbb Z^{60}
\longrightarrow\mathbb Z^{72}
\longrightarrow\mathbb Z^{36}
\longrightarrow0.
\]

The middle arrow forgets the primary-comparison homotopy. The last arrow records the primary class. The checker computes both matrices; their product is zero, their ranks are complementary, and signed-unit elimination proves saturated images. This establishes exactness without rationalizing.

The twelve-dimensional ordinary count at each weight is only the fixed regulator-grade piece. The complete \(\Lambda\)-module normal forms, including generators in other grades, remain in the certificate.

## 5. Two explicit D03 gallery examples

Put

\[
F=\{03,13,35\},\qquad E=\{13,35\}.
\]

The first example is

\[
Y_{02}=X_{02}\bigl([F,F,0]-\beta[E,E,0]\bigr).
\]

Its regulator-normal grade is three. The full differential of the bracket has coefficients only in the positive-sheet ideal; multiplication by \(X_{02}\) kills them by the actual normalization relations. Therefore

\[
dY_{02}=0,\qquad v(Y_{02})=q(Y_{02})=0.
\]

It gives the supported-map difference

\[
D_Y(p)=0,\qquad D_Y(e)=Y_{02}.
\]

The polynomial normal form detects a nonzero free top coordinate. Its ordinary supported-map coordinate is also nonzero. This is one of the six directions visible after forgetting the primary comparison.

The second example replaces the native 35-mark by the independently retained occurrence partner:

\[
O_{02}=X_{02}\bigl(
[F,\{03,13\},1]
-\beta[E,\{13\},1]
\bigr).
\]

The checker verifies \(dO_{02}=0\), zero endpoint and Q components, and regulator-normal grade two. The grade-preserving difference is

\[
D_O(p)=0,\qquad D_O(e)=\beta O_{02}.
\]

This is an ordinary boundary: the homotopy \(U(p)=O_{02}, U(e)=0\) satisfies

\[
\delta U=D_O.
\]

It is not a nullhomotopy with the primary comparison left fixed. The two primary-framed points have different coordinates:

\[
\Pi(0,\beta O_{02},0)=\beta O_{02}\ne0,
\]

\[
\Pi(0,\beta O_{02},O_{02})=0.
\]

The first is nonzero because \(H_3(N)\) is free over \(\Lambda\) in this occurrence component. The second has the explicit nullhomotopy supplied by the displayed fibre contraction. They have the same ordinary map and different primary-comparison data.

### Nonzero primary control

The checker also reconstructs the earlier fifteen-term primitive \(H_\beta\) and its nonzero primary \(A_\beta\), deriving

\[
dH_\beta=\beta A_\beta,\qquad dA_\beta=0
\]

from the full 430-state differential. It checks the three maps with common bottom value \(X_{02}A_\beta\) and top values

\[
X_{02}H_\beta,
\qquad X_{02}H_\beta+Y_{02},
\qquad X_{02}H_\beta+\beta O_{02}.
\]

All three have identical full endpoint coefficients, full Q coefficients, and primary chain. Their normal grades agree. Thus the comparison-space calculation is applicable over a nonzero primary, not only over the zero map.

## 6. Why this does not contradict the preceding rigidity result

The preceding coherent computation was in occurrence weight zero. This checker reruns the stronger full-endpoint frame in that same weight and again obtains no top homology.

Positive conductor coefficients change the module equations: products between the two normalization sheets vanish. This allows closed mixed-gallery chains such as \(Y_{02}\). Removing their conductor factors destroys closure. The new classes are not obtained by transporting the earlier weight-zero result across an invertible scalar.

The refinement also avoids retaining only endpoint-top rows. For example, an occurrence-partner endpoint component that escaped that smaller frame is now constrained, together with its incoming differential. The kernel ranks above were computed after this strengthening.

## 7. Verification and limits

The standalone checker:

1. reconstructs the complete differential and support labels;
2. constructs all six conductor-relative fine components directly from their exponent conditions;
3. builds the full endpoint/Q boundary quotient and verifies its coherent fibre contraction;
4. builds and contracts the primary homotopy fibre, with its additional comparison component;
5. computes full integral polynomial normal forms of the target and supported Hom complexes;
6. exports every top cycle in the original 430-state basis;
7. computes saturated forgetful and primary-readout matrices; and
8. verifies both explicit gallery examples and the nonzero-primary control.

There is no truncation in powers of \(\beta\), no discarded endpoint state, no inverse occurrence variable, and no division by a nonunit regulator. The certificate records 226,245 exact checks. The normalized polynomial identities hold over the displayed integral model; the physical exponential interpretation remains within its stated characteristic-zero formal scope.

This calculation gives a concrete first-conductor coefficient deformation space. It does not choose the conductor-source image, impose unstated lower-support comparison constraints, prove a stratum-preserving spatial lift, or identify a basis vector with the physical \(\Delta_J\). Selecting that image requires an independently defined normalization–conductor comparison with its primary homotopy retained.

## Sources and replay

Repository commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

* `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: signed radial/native differential and support labels.
* `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the two-sheet coefficient ring and conductor relations.
* `research/voevodsky/check_d03_formal_support_purity.rs`: physical graph formula and its fixed-nonzero-regulator scope.
* Stacks Project tags `0A8H`, `014D`, `064B`, and `0117`: Hom signs, fibre/cone constructions, derived maps from projective complexes, and connecting exact sequences.

The checked local predecessor files are `branch_a_coherent_endpoint_q_primary_frame_checker.py` and `branch_a_first_conductor_degree_framed_deformations_checker.py`. The new checker is standalone: it imports neither of them and reads no companion data file.

Run:

```bash
python branch_a_first_conductor_coherent_primary_lifts_checker.py \
  --output branch_a_first_conductor_coherent_primary_lifts_certificate.json
```

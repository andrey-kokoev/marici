# Branch A: first-conductor-degree deformations with identical primary, endpoint, and Q data

Date: 2026-09-07.

## Result

Endpoint-fixed rigidity in occurrence weight zero does not extend to the entire coefficient object. At occurrence weight epsilon_02, the complete polynomial family has nine independent degree-three cycles with zero endpoint components. All nine also have zero Q component. Six determine independent, nonzero regulator-supported map classes at the regulator-normal grade of the recorded packet; the other three become explicit ordinary homotopy boundaries after the required regulator-grade adjustment.

A two-term example lies on the actual first D03 flip edge and its mixed vertex. It yields two maps with the same nonzero primary chain, identical endpoint and Q components, and the same regulator-normal grading. Their ordinary derived difference has exact annihilator (beta,X13,X15,X35).

This does not identify the physical conductor–Morse difference. It establishes that the previous weight-zero uniqueness test cannot be extended to first conductor order without an additional source condition.

## 1. The complete coefficient family

Use the ordered diagonals

\[
(02,03,04,13,14,15,24,25,35)
\]

and the normalization coefficient ring

\[
R=\mathbb Z[\beta,X_{02},X_{03},X_{04},X_{13},X_{14},X_{15},X_{24},X_{25},X_{35}]
 /(X_eX_o:e\in\{02,04,24\},\ o\in\{13,15,35\}).
\]

The mixed-product relations are the normalization–conductor relations of Entry 93. Denote the two short-variable ideals by

\[
I_-=(X_{02},X_{04},X_{24}),\qquad I_+=(X_{13},X_{15},X_{35}).
\]

The 430 states are

\[
[F,H,\epsilon],\qquad H\subseteq F,\quad \epsilon\in\{0,1\},
\qquad |[F,H,\epsilon]|=3-|F|+|H|+\epsilon.
\]

Here F is an actual noncrossing dissection. The radial differential inserts an unmarked diagonal with coefficient X_a; the native normal differential has coefficient beta X_h; the independent occurrence partner has coefficient X35 and the tensor sign. No native circle is identified with the occurrence partner.

The complete support counts are 32 endpoint states, 416 short-boundary states, 430 total states, and fourteen Q states. Both endpoints are retained:

\[
V_-=(02,04,24),\qquad V_+=(13,15,35).
\]

This is the unit-normalized coefficient family underlying the formal expression

\[
u_d=e^{\beta X_d}-1=\beta X_dv_d,\qquad v_d(0)=1.
\]

Only the units v_d have been absorbed into normal frames. The source's geometric purity statement is scoped to fixed nonzero beta. The present calculation retains beta zero algebraically and does not assert that geometric purity extends there.

## 2. A two-term cycle with zero endpoint and Q components

Let

\[
E=[\{13,35\},\{13,35\},0],\qquad
B=[\{03,13,35\},\{03,13,35\},0],
\]

and put

\[
Y_{02}=X_{02}(B-\beta E).
\]

Both states have homological degree three. They are the fully native-marked first gallery edge and its mixed D03 vertex, not new carrier states.

Writing U=B-beta E, the complete differential is

\[
\begin{aligned}
dU={}&\beta X_{35}[\{03,13,35\},\{03,13\},0]
-\beta X_{13}[\{03,13,35\},\{03,35\},0]\\
&+\beta X_{15}[\{13,15,35\},\{13,35\},0]\\
&+\beta^2X_{13}[\{13,35\},\{35\},0]
-\beta^2X_{35}[\{13,35\},\{13\},0].
\end{aligned}
\]

Every coefficient lies in I_+. Multiplying by X02 kills all five terms by the actual normalization relations. Therefore

\[
dY_{02}=0,\qquad
\operatorname{pr}_{V_-}Y_{02}=\operatorname{pr}_{V_+}Y_{02}=0,
\qquad \pi_QY_{02}=0.
\]

The last assertions are literal state identities. The cycle is contained entirely in the existing short-boundary support, away from the two endpoint faces. Its incoming endpoint-connector contribution also vanishes, because its full differential vanishes and it has no endpoint component.

The factor X02 is essential. U itself is not closed over R. Removing that factor would change the coefficient problem.

## 3. Nonvanishing in the full complex

For F=(03,13,35), the two states

\[
[F,F,0],\qquad[F,F,1]
\]

form a genuine quotient of the complete 430-state complex:

\[
Q_F=[R\xrightarrow{-X_{35}}R]
\]

in degrees four and three. No discarded radial or native column enters a fully marked maximal face. The checker verifies the quotient identity against every column of the full differential.

The quotient sends Y02 to X02. Consequently

\[
\operatorname{Ann}_R[Y_{02}]=I_+.
\]

For completeness, write an element of the two-sheet ring as a common coefficient plus a negative-sheet polynomial and a positive-sheet polynomial, with both branch-polynomial constant terms zero. Its product with X02 is zero exactly when its common and negative components vanish. The same condition holds after quotienting by X35, because a nonzero negative-sheet polynomial cannot become a multiple of X35. Thus the quotient detector proves the converse annihilator containment, not merely the displayed annihilation.

The state class survives beta specialization or beta inversion as long as X02 remains nonzero on the negative coefficient sheet. No claim about a physical support-changing realization follows from this coefficient statement.

## 4. Two actual maps with the same primary and boundary data

Retain the recorded chains A_beta,H_beta, whose full equations are reconstructed by the checker:

\[
dA_\beta=0,\qquad dH_\beta=\beta A_\beta.
\]

Use the two-term source

\[
S_\beta=[Re\xrightarrow{\beta}Rp]
\]

in homological degrees three and two. Define

\[
\begin{array}{c|cc}
 & p & e\\\hline
\mathcal F_0 & X_{02}A_\beta & X_{02}H_\beta\\
\mathcal F_1 & X_{02}A_\beta & X_{02}H_\beta+Y_{02}.
\end{array}
\]

Both are chain maps. Their common primary has fifteen nonzero terms. Their two top components have fifteen and seventeen terms, respectively. They agree on the complete endpoint and Q components, not only on scalar residues or homology classes.

The difference is the map

\[
\mathcal D(p)=0,\qquad\mathcal D(e)=Y_{02}.
\]

The above vertex quotient gives

\[
\operatorname{Hom}(S_\beta,Q_F)=
\left[
R\xrightarrow{(-X_{35},-\beta)^T}R^2
\xrightarrow{(\beta,-X_{35})}R
\right]
\]

in cohomological degrees minus two, minus one, and zero. Hence

\[
H^0\operatorname{Hom}(S_\beta,Q_F)=R/(\beta,X_{35}),
\qquad [\pi_F\mathcal D]=[X_{02}]\ne0.
\]

The source is bounded free, so ordinary Hom computes derived maps. The resulting full-target class has exact annihilator

\[
\operatorname{Ann}_R[\mathcal D]=(\beta,X_{13},X_{15},X_{35}).
\]

All positive-sheet generators kill the representative. The beta-annihilating homotopy is explicit:

\[
\mathcal H(p)=Y_{02},\qquad\mathcal H(e)=0,
\qquad \delta\mathcal H=\beta\mathcal D.
\]

The quotient detector excludes any additional annihilator. In particular, the two maps remain distinct even after allowing arbitrary ordinary supported-map homotopies, before beta is inverted. Any stricter frame that admits both maps cannot make this nonzero ordinary class zero.

The maps do change lower-support homotopy components. A condition fixing those components pointwise would exclude the modification. That is stronger than fixing the primary chain, the full endpoint coefficients, and the full Q components considered here.

## 5. The regulator-normal grading has not been discarded

Assign regulator-normal weight one to beta and every native circle, and weight zero to the occurrence partner and to occurrence variables. Every differential preserves this weight: native deletion replaces one circle by one beta, radial insertion does not change marks, and the occurrence differential has no beta.

The recorded source packet has weights

\[
|p|_\beta=2,\qquad |e|_\beta=3,
\qquad |A_\beta|_\beta=2,\qquad |H_\beta|_\beta=3.
\]

Both terms of Y02 have regulator-normal weight three. Therefore the displayed two maps preserve the actual weights of the recorded packet. Their nonvanishing is not obtained by changing this grading.

Inverting beta contracts S_beta. Accordingly the ordinary supported-map class [D] vanishes at fixed nonzero beta. This does not contradict nonvanishing of the state cycle [Y02]. Homotopies of supported maps may have a nonzero p-component, whereas homotopies fixing that entire comparison component pointwise may not. The two statements concern different mapping problems.

## 6. Exhaustive polynomial classification at occurrence weight epsilon_02

For occurrence weight m, a state contributes exactly when

\[
m+\mathbf1_F-\mathbf1_H-\epsilon\mathbf1_{35}
\]

has nonnegative entries and the resulting monomial survives the mixed-sheet ideal. Beta powers remain unrestricted.

At m=epsilon_02, the entire component has ranks

\[
(4,29,69,56)
\]

in homological degrees zero through three, and no degree-four term.

To impose zero endpoint coefficients correctly, first take the complement of the endpoint state summands. Then impose zero incoming endpoint boundary. Writing the support block differential as

\[
d=\begin{pmatrix}d_V&\kappa\\0&d_E\end{pmatrix},
\]

the relevant subcomplex is ker(kappa) inside the labelled complement. Each incoming endpoint column has at most one endpoint row, with coefficient +1 or -1 in this homogeneous component. This yields a saturated integral kernel basis directly.

Its complete ranks are

\[
(3,25,63,50).
\]

At beta=1, sixty-six integral unit cancellations reduce it to nine degree-three generators and no other homology. The certificate contains all projection, inclusion, and homotopy matrices.

Transporting the resulting cycles polynomially gives nine cycles Y_i. There are 34 terms across their complete basis. Their coefficients on the nine selected labelled rows are exactly the identity matrix. All nine cycles have zero Q component as well as zero endpoint component.

The coordinate rows, using the certificate's full state enumeration, are

```text
279 284 311 316 332 364 412 423 428
```

The sample Y02 is the cycle whose coordinate row is 316.

The conclusion is

\[
\{Y\in(C_\beta)_3{}_{\epsilon_{02}}:dY=0,\ Y_V=0\}
=\bigoplus_{i=1}^9\mathbb Z[\beta]Y_i,
\qquad (Y_i)_Q=0.
\]

There are no degree-four chains of this occurrence weight, so these cycle directions cannot be removed by state-chain boundaries.

### Completeness for arbitrary beta powers

The polynomial comparison multiplying each native-mark state by beta^{|H|} intertwines the beta-family differential and the beta-one differential. After inverting beta for the proof, it identifies the complete cycle kernel with the integral nine-generator kernel just computed.

Each transported cycle is normalized so that one of the nine coordinate rows has coefficient one, and the other eight coordinate rows have coefficient zero. For any polynomial cycle, these coordinate values are polynomials in beta. Subtracting the corresponding polynomial combination of the nine cycles is zero after beta localization. The chain modules are beta-torsion-free, so the equality already holds polynomially.

No constructed map or primitive uses beta inverse. This argument, together with the integer contraction and identity coordinate minor, proves completeness without a beta cutoff.

### Fixed regulator grade

Six basis cycles have regulator-normal weight three; three occurrence-partner cycles have weight two. At the source packet's fixed top weight three, the latter must be multiplied by beta. Thus the raw same-primary, endpoint/Q-zero variation lattice in this bidegree has nine integer directions:

- six native weight-three cycles;
- beta times three weight-two occurrence cycles.

The last three are explicit ordinary supported-map boundaries by the homotopies sending p to the corresponding weight-two cycles. The remaining six classes are independently detected by their six fully native-marked nonendpoint vertex rows modulo beta.

Therefore the ordinary supported-map differences represented by fixed-primary, endpoint/Q-zero maps at these occurrence and regulator weights form an integral rank-six lattice. This is not a computation of a stronger physical mapping fibre that fixes all source comparison homotopies.

## 7. The complete negative-sheet nonnegative-weight sector

Define

\[
R_-=\mathbb Z[\beta,X_{02},X_{04},X_{24},X_{03},X_{14},X_{25}].
\]

Consider all nonnegative occurrence weights with zero X13,X15,X35 weights and with at least one of the X02,X04,X24 weights positive. Arbitrary long-coordinate weights are allowed.

Every such component has the same state set and the same matrix over Z[beta] as the epsilon_02 component. Positive negative-sheet weight forces all positive-sheet coefficient exponents to vanish; higher negative or long exponents introduce no new survival condition. The checker exhausts the seven negative support patterns and the eight long support patterns. The exponent formula proves stability for every higher power.

Every displayed cycle factors as

\[
Y_i=X_{02}U_i,
\]

where U_i has no occurrence-variable coefficient and dU_i has coefficients in I_+. The complete cycle module in this cone is therefore

\[
\mathscr Z_-\cong I_-^{\oplus9}
\]

as a graded R_--module. The displayed factorization is coefficient extraction on already divisible expressions; U_i need not be closed before multiplication by I_-.

As unrestricted ordinary supported-map differences represented by (0,Y), the corresponding classes are

\[
(\mathscr Z_-/\beta\mathscr Z_-)
\cong(I_-/\beta I_-)^{\oplus9}.
\]

Indeed, there are no degree-four states in this entire occurrence cone. A homotopy killing (0,Y) must have a closed p-component A with Y=beta A. Because beta is injective on each chain module, zero endpoint/Q components of Y force the same conditions on A. This proves both directions of the quotient statement.

Before ordinary supported-map homotopies, first conductor order gives 27 independent cycle symbols: nine for each of the three negative normal directions. At the regulator grade of the recorded packet, eighteen supported-map classes remain: six for each negative normal. Neither count is a claim that the physical source selects all of them.

The native/occurrence distinction is visible in three exact relations. On each of the three pairs of basis cycles carrying 35, the replacement operator sends the native cycle to beta times its occurrence-partner cycle. Thus the two kinds of normal states cannot be identified uniformly across beta=0.

## 8. What has changed, and what has not

The former calculation correctly established rigidity in occurrence weight zero. The present computation reproduces that zero kernel independently.

The first negative conductor degree has nonzero primary-preserving variations with identical endpoint and Q coefficients. The simplest one is supported on the original D03 first-flip edge and mixed vertex, and is visible to an actual nonendpoint quotient of the full complex. This is not a scalar normalization imposed on a missing map.

Every new cycle carries a genuine conductor factor. Ordinary restriction to the conductor kills that representative; its first conormal symbol retains the factor as a conormal line. It may not be cancelled to claim a weight-zero or scalar-unit result.

These classes still have zero Q projection, and they have not been identified with the physical Delta_J. To make that identification, the normalization-source construction must select a combination, retain the associated conormal lines, and determine whether the changed lower-support homotopy components are allowed. The present result removes a specific alleged obstruction—endpoint rigidity in all coefficients—without supplying those missing physical maps.

## 9. Verification and provenance

Run the standalone checker with

```sh
python branch_a_first_conductor_degree_framed_deformations_checker.py \
  --output branch_a_first_conductor_degree_framed_deformations_certificate.json
```

The checker uses only the Python standard library and reads no companion input. It reconstructs the complete differential, support subcomplexes, homogeneous components, endpoint-kernel bases, polynomial cycles, nine-coordinate classification, the actual reference and modified maps, both annihilator witnesses, and the regulator-grade conditions.

It verifies 24,417 exact identities. A clean run from a directory containing only the checker reproduces the certificate byte-for-byte.

The unbounded claims use the polynomial basis proof, the exact coefficient normal form, and the stabilization criterion; sample high-degree monomials are controls, not proofs of completeness.

Repository inputs are pinned to commit

```text
d1947b67a60d3e88ba77f4ca60ea02c2a306ee61
```

Relevant source files:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: radial/native differential, ordered face incidences, and support subcomplexes.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: the separate occurrence-Koszul correction.
- `research/voevodsky/check_d03_formal_support_purity.rs`: the formal normal graph and its fixed-nonzero-beta geometric scope.
- Entry 93, `Alternating Fusion Normalization-Conductor Square`: the mixed-sheet coefficient relations.
- Entry 106, `Marked Log Gallery Secondary Class and the Global Yoneda Gap`: the actual first-flip edge and mixed vertex used in the two-term example.
- Previous artifact `branch_a_regulator_supported_vertex_decomposition_checker.py`: labelled first primitive embedded in the present checker; its needed differential identities are reconstructed, not assumed.

General conventions: Stacks Project, tags 0A8H (Hom complexes), 0621 (Koszul complexes), and 064B (bounded-above projective sources compute derived maps). These references justify the sign conventions and derived-map interpretation, not the new matrix computations.

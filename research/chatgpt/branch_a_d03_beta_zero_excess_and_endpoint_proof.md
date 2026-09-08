# Branch A: the D03 packet at regulator zero, its excess line, and its endpoint-detected comparison

Date: 2026-09-07.

## Result and scope

Extend the prescribed exponential coefficient graph over a formal parameter `beta`, without inverting `beta`. The complete 430-state coefficient complex and the previously recorded four chains admit this extension.

The calculation distinguishes three objects:

1. The transported primary chain is exact and divisible by `beta`. Its divided chain represents a primitive `beta`-torsion class.
2. The difference of its two recorded annihilating primitives is a degree-three cycle `Z_beta` with exact cyclic homology module `R/(X35)`. It has no `beta` torsion and has a nonzero negative-endpoint component.
3. The two genuine maps from the single-normal source `K(beta)[2]` have a nonzero difference class with exact cyclic module `R/(beta,X35)`. This is a supported comparison class, not the homology class in item 2. It is detected at the negative endpoint, so it is not an ambiguity remaining after that endpoint frame is fixed.

The older ordered pair `(t04,t35)` pulls back to two multiples of the same `beta` divisor. Its Koszul complex retains a rank-one excess class. A proposed two-normal map retaining the two computed primitives is obstructed already on the first infinitesimal thickening of `beta=0`.

These statements concern the explicitly defined coefficient family. The source's fixed-nonzero-beta geometric purity theorem is not assumed to extend to beta zero. No physical conductor–Morse class is identified by this calculation.

## 1. The formal family and the retained normal lines

Use the ordered diagonals

\[
\mathscr D=(02,03,04,13,14,15,24,25,35),
\]

with short-diagonal sheets

\[
S_+=(13,15,35),\qquad S_-=(02,04,24),
\qquad L=(03,14,25).
\]

The starting ring is the polynomial coefficient subring

\[
B=\mathbb Z[X_d,t_s,u_l]/(X_eX_o:e\in S_-,\ o\in S_+).
\]

The physical graph has the formal extension

\[
u_d=e^{\beta X_d}-1=\beta X_dv_d,
\qquad
v_d=\sum_{n\geq0}\frac{(\beta X_d)^n}{(n+1)!},
\qquad v_d|_{\beta=0}=1.
\]

Thus

\[
X_d\mapsto X_d,\qquad t_s\mapsto\beta v_s,
\qquad u_l\mapsto\beta v_lX_l.
\]

The `v_d` are units even at beta zero. The `g_d=beta v_d` used in the preceding fixed-beta calculation are not units there.

For exact polynomial verification, first work over

\[
R=\mathbb Z[\beta,X_d,v_d^{\pm1}]/(X_eX_o).
\]

Then substitute the displayed formal series over characteristic zero. The proofs use identities over this universal unit ring; a truncated series control is not the justification for an all-order assertion. Any required monodromy units are present after the actual formal substitution.

The source's order of operations remains unchanged: this regulates the already extracted scalar coefficient complex. It does not exponentiate an unextracted shifted family containing `X+sigma/t`.

Each state is

\[
[F,H,\epsilon],\quad H\subset F,\quad\epsilon\in\{0,1\},
\qquad |[F,H,\epsilon]|=3-|F|+|H|+\epsilon.
\]

`F` is an actual noncrossing dissection. The last bit is the distinct occurrence-35 Koszul factor, whose differential is `X35`. It is not another native normal.

Rescale native marks only by the genuine units:

\[
\Phi_v[F,H,\epsilon]
=\left(\prod_{h\in H}v_h\right)[F,H,\epsilon].
\]

This identifies the graph-pulled complex with `C_beta`, whose radial differential has coefficient `X_d`, native normal differential has coefficient `beta X_d`, and occurrence-partner differential has coefficient `X35`. The matrix equation is

\[
d_\beta\Phi_v=\Phi_vd_{\rm graph}.
\]

No basis change uses beta inverse. In particular, replacing a native circle differential by `X_d` at beta zero would be an invalid further conjugacy.

All 430 states remain; the endpoint, short-boundary, and quotient counts are 32, 416, and 14. The matrices retain every lower correction and both endpoint packets. Bounded freeness makes termwise coefficient change a model of derived coefficient change; see Stacks Project, tag 064K.

## 2. Factor the original packet without discarding beta orders

Let `rho_beta=Phi_v phi_beta`. Write

\[
a=v_{02}v_{04}v_{13},\qquad
b=v_{03},\qquad
c=v_{15}v_{24}v_{14}v_{25},\qquad
Y=X_{14}X_{25}.
\]

The original identities are

\[
d\Omega=0,\quad dW_u=u_{03}\Omega,
\quad dW_\mu=\mu\Omega,
\quad\Theta=u_{03}W_\mu-\mu W_u,
\]

where `mu=t15 t24 u14 u25`.

The complete transported chains have the exact factorizations

\[
\begin{aligned}
\rho_\beta(\Omega)&=a\,\beta A_\beta,\\
\rho_\beta(W_u)&=ab\,\beta X_{03}H_\beta,\\
\rho_\beta(W_\mu)&=ac\,\beta^4Y\,G_\beta,\\
\rho_\beta(\Theta)&=abc\,\beta^5X_{03}Y\,Z_\beta.
\end{aligned}
\]

Their identities are

\[
d_\beta A_\beta=0,\qquad
 d_\beta H_\beta=d_\beta G_\beta=\beta A_\beta,
\qquad Z_\beta=G_\beta-H_\beta,
\qquad d_\beta Z_\beta=0.
\]

The respective term counts of `A_beta,H_beta,G_beta,Z_beta` are 21, 15, 30, and 45. Factoring the displayed beta and occurrence factors is an exact operation on these particular divisible chains. It is not localization, nor a definition of division on arbitrary homology classes.

The exact beta orders of the four raw transported chains are

\[
(1,1,4,5)
\]

in the order `(Omega,Wu,Wmu,Theta)`. All four raw chains are therefore zero under literal substitution `beta=0`. Their factored chains and associated symbols must be recorded separately.

## 3. A primitive beta-torsion class is present

The divided primary `A_beta` is closed and is annihilated by beta through the recorded primitive `H_beta`.

At beta zero its leading chain is

\[
\begin{aligned}
A_0={}&X_{03}[\{02,03,04\},\{02,04\},0]\\
&+X_{14}[\{04,13,14\},\{04,13\},0].
\end{aligned}
\]

The negative and positive short variables still satisfy the normalization cross-product relations. No such relation removes either displayed term.

Define an integral functional on degree-two chains of `C_0` by extracting the coefficient of `X03` from row

\[
[\{02,03,04\},\{02,04\},0]
\]

and the coefficient of `X24` from row

\[
[\{02,04,24\},\{02,04\},0],
\]

then adding the two numbers. The only radial boundary reaching these two monomials has entries `(-X03,+X24)`. Native normal boundaries are zero at beta zero. Occurrence boundaries carry `X35`, which cannot contribute either selected monomial without a forbidden inverse. Therefore

\[
\ell(d_0v)=0,\qquad \ell(A_0)=1.
\]

This also applies to formal coefficients by extracting the same finite monomial coefficients. It proves primitive nonvanishing for all polynomial degrees, not just for a chosen representative search.

The checker independently contracts the complete occurrence-weight-zero central component, with chain ranks `(8,59,108,56)` in degrees zero through three. Its integral homology has ranks `(0,6,21,14)`. The projection of `A_0` has coordinates `(1,1)` in two of the degree-two residual generators.

Consequently

\[
\mathbb Z[\beta]\,[A_\beta]\cong\mathbb Z[\beta]/(\beta)
\]

inside this homogeneous component. After rational formal coefficient extension, the analogous beta-adic statement holds. No full annihilator over the entire occurrence ring is claimed for this primary class.

The first beta-Bockstein satisfies

\[
b_\beta[H_0]=b_\beta[G_0]=[A_0].
\]

This follows from the complete equations `dH_beta=dG_beta=beta A_beta`. In an invariant normal-line formulation, the conormal symbol `[beta]` accompanies the connecting class. This is not an identification of beta with an independent short Rees coordinate.

## 4. The difference persists across the beta family

Define

\[
\Psi_\beta=
\sum_F(-1)^{|F|(|F|+1)/2}\beta^{3-|F|}[F,F,0].
\]

Define `P_beta` to be the identity on states without the native mark `35`, zero on states containing both the native mark and the occurrence partner, and

\[
P_\beta[F,H,0]
=\beta[F,H\setminus\{35\},1]
\quad(35\in H).
\]

The coefficient beta is forced by `d h35_native=beta X35` and `d h_occ=X35`. The diagonal `35` is last in the fixed normal ordering, so no additional reordering sign occurs in this formula. The full matrix verifies

\[
d_\beta P_\beta=P_\beta d_\beta,\qquad
P_\beta^2=P_\beta,\qquad
Z_\beta=P_\beta\Psi_\beta.
\]

No two normal factors are silently identified.

The beta expansion

\[
Z_\beta=Z_0+\beta Z_1+\beta^2Z_2+\beta^3Z_3
\]

has term counts `(9,21,13,2)`. With `d_beta=d_0+beta d_1`, every coefficient equation

\[
d_0Z_0=0,\qquad d_0Z_k=-d_1Z_{k-1},\qquad d_1Z_3=0
\]

is verified. Thus `Z_0`, unlike `H_0` and `G_0` separately, has a full polynomial closed lift.

Its central value is

\[
Z_0=\sum_{\substack{|F|=3\\35\notin F}}[F,F,0].
\]

There are nine such triangulations. The two central primitives are separately retained:

\[
H_0=-[\{02,03,04\},\{02,03,04\},0]
-[\{03,04,13\},\{03,04,13\},0],
\]

and `G_0` is the seven-term complement, so `G_0-H_0=Z_0`.

## 5. An endpoint quotient proves the exact cyclic support

Let

\[
E_-=[S_-,S_-,0],\qquad E_{-,\mathrm{occ}}=[S_-,S_-,1].
\]

Projection onto these two fully marked endpoint rows is a chain map to

\[
E_-^{\rm top}=[R\xrightarrow{-X_{35}}R]
\]

in homological degrees four and three. No radial or native-normal differential from a discarded state can enter a fully marked maximal face. The only retained entering arrow is the occurrence boundary.

Let `S35` be exterior multiplication by the occurrence partner with the tensor sign. The complete complex satisfies

\[
d_\beta S_{35}+S_{35}d_\beta=X_{35}\,\mathrm{id}.
\]

The maps

\[
q_3\mapsto Z_\beta,\qquad q_4\mapsto-S_{35}Z_\beta
\]

give a strict chain section of this endpoint quotient. It follows that

\[
R[Z_\beta]\cong R/(X_{35})\subset H_3(C_\beta),
\]

with exact annihilator `(X35)`. This cyclic summand has no beta torsion. The actual two-term summand also retains

\[
H_4(E_-^{\rm top})=\operatorname{Ann}_R(X_{35})
=(X_{02},X_{04},X_{24}).
\]

It is not a free resolution of its lower homology module.

This section is an ordinary coefficient splitting. Its image spans several supports; it is not asserted to be an endpoint-local geometric inverse.

## 6. Two genuine supported maps have a computed nonzero difference

Place the single-normal Koszul complex `K_R(beta)` in homological degrees three and two:

\[
S_\beta=[Re\xrightarrow{\beta}Rp].
\]

The original packet supplies two chain maps

\[
F_{03},F_\mu:S_\beta\longrightarrow C_\beta,
\]

with

\[
F_{03}(p)=F_\mu(p)=A_\beta,
\qquad F_{03}(e)=H_\beta,
\qquad F_\mu(e)=G_\beta.
\]

Their literal difference is

\[
D_\beta(p)=0,\qquad D_\beta(e)=Z_\beta.
\]

This is a comparison of actual maps in one complete complex. It does not introduce an unspecified realization functor.

Projecting to `E_-^{top}` computes the entire relevant small Hom complex. In cohomological degrees minus two, minus one, and zero its matrices are

\[
R\xrightarrow{(-X_{35},-\beta)^T}R^2
\xrightarrow{(\beta,-X_{35})}R.
\]

The projected difference is the degree-zero coefficient `1`. Thus

\[
H^0\operatorname{Hom}(S_\beta,E_-^{\rm top})
=R/(\beta,X_{35}),
\qquad [\pi_-D_\beta]=1.
\]

This proves that the full difference cannot be nullhomotopic.

Its exact cyclic annihilator is also computed. A homotopy sending `p` to `Z_beta` and `e` to zero has boundary `beta D_beta`. A second homotopy sending `e` to `S35 Z_beta` and `p` to zero has boundary `X35 D_beta`. Projection proves that there is no further annihilator. Therefore

\[
R\,[F_\mu-F_{03}]\cong R/(\beta,X_{35})
\]

inside `Hom_{D(R)}(S_beta,C_beta)`.

This supported morphism class and the class `[Z_beta]` have different supports because they belong to different mapping problems. The former vanishes after beta is inverted, since its source then contracts. The latter persists after beta is inverted unless `X35` is also inverted.

The comparison is endpoint-visible. `F03` has zero endpoint coefficients, whereas the top image of `Fmu` contains `E_-+beta E_{+,occ}`. The computed difference is therefore not a residual deformation of a fixed-endpoint comparison.

## 7. The regulator changes the support of the old Gysin inputs

The older ordered pair pulls back to

\[
(t_{04},t_{35})\mapsto(\beta v_{04},\beta v_{35}).
\]

After only the invertible normal-line changes, its complex is

\[
K_R(\beta,\beta)\cong K_R(\beta)\otimes\Lambda(\eta),
\]

where

\[
e=e_{04}/v_{04},\qquad
\eta=e_{35}/v_{35}-e_{04}/v_{04},
\qquad de=\beta,\qquad d\eta=0.
\]

The ordered determinant is retained:

\[
e\wedge\eta=(v_{04}v_{35})^{-1}e_{04}\wedge e_{35}.
\]

Because beta is a nonzero divisor,

\[
H_0=R/(\beta),\qquad
H_1=R/(\beta)\eta,\qquad H_2=0.
\]

Thus the two Rees divisors have one common Cartier support and a retained excess line. The codimension-two regular-purity formula cannot simply be reused at beta zero. For nonzero invertible beta this complex contracts, recovering the preceding fixed-beta result.

For completeness, the old annihilator pair becomes, after its unit factors are retained separately,

\[
(\beta X_{03},\beta^4X_{14}X_{25}).
\]

Its first syzygy is

\[
\rho=-\beta^3X_{14}X_{25}e_u+X_{03}e_\mu,
\qquad d(e_u\wedge e_\mu)=\beta\rho.
\]

The pair `(X03,beta^3 X14 X25)` is regular: these are independent long variables and the beta parameter over the short-variable normalization ring. Its Koszul exactness shows that all syzygies are multiples of the displayed one. Hence the homology of the original pair is

\[
H_0=R/(\beta X_{03},\beta^4X_{14}X_{25}),\qquad
H_1=R/(\beta)\rho,\qquad H_2=0.
\]

Again, the retained source is not a regular codimension-two resolution.

## 8. The recorded two-primitive assignment fails to lift from beta zero

Consider the algebraic attempt to encode the two recorded beta-annihilating homotopies by `K(beta,beta)[2]`. This is a test of a proposed packaging, not an assertion that their geometric normal labels have already been identified with `(04,35)`.

Assign

\[
p\mapsto A_\beta,\qquad e_1\mapsto H_\beta,\qquad
 e_2\mapsto G_\beta.
\]

The top equation would require a degree-four chain `Y` satisfying

\[
d_\beta Y=\beta G_\beta-\beta H_\beta=\beta Z_\beta.
\]

The negative-endpoint quotient forces

\[
-X_{35}\,y=\beta.
\]

This has no solution. In particular, modulo `(X35,beta^2)` its left side is zero and its right side is a nonzero first-order parameter.

At beta zero the four source differentials vanish, and assigning the central values `(A0,H0,G0,0)` does define a chain map. It does not lift even to the first infinitesimal beta thickening while retaining the two central primitive images. Higher endpoint terms cannot repair the obstruction because the endpoint quotient is a chain map on the complete complex.

Equivalently, the excess generator of `K(beta,beta)` is beta-torsion, whereas `[Z_beta]` is not. A map sending that excess generator directly to `[Z_beta]` is therefore impossible. The separately computed supported morphism difference lives instead in `R/(beta,X35)`; no identification of these differently typed objects is assumed.

## 9. The endpoint and Q orders remain distinct

The complete restrictions are

\[
\operatorname{pr}_VZ_\beta=E_-+\beta E_{+,\mathrm{occ}},
\]

\[
\pi_QZ_\beta=\beta^2(\beta T-h_{03}-h_{14}-h_{25}),
\]

\[
\pi_QH_\beta=\beta^2h_{03},\qquad
\pi_QA_\beta=\beta^2X_{03}p_{03}.
\]

At beta zero the secondary leading chain is nonzero on the negative endpoint but has zero complete Q-projection. Its first nonzero Q-symbol occurs at beta order two; its top-cell coefficient occurs at beta order three.

Returning to the actual exponential normal frames, the endpoint coefficients of `Phi_v^{-1}(a Z_beta)` are

\[
v_{13}/v_{24},\qquad
\beta v_{02}v_{04}/v_{15}.
\]

They specialize to `(1,0)`, not two equal unit endpoints. No determinant factor of beta has been discarded. The separate occurrence-35 line remains explicit throughout.

The generic top quotient of the endpoint section is multiplication by `beta^3`. A scalar rescaling of this chosen section to top coefficient one would require beta inverse cubed. No such rescaling extends over beta zero.

## 10. Verification and remaining physical question

The self-contained checker reconstructs five complete differentials: the input polynomial model, its graph pullback, the beta family, its beta-zero fibre, and the beta-one control. It checks the four original witnesses, full normal-line comparison, endpoint and Q terms, the exact factorizations, the closed beta lift, strict endpoint summand, both supported maps and their annihilating homotopies, complete central homogeneous contraction, and both excess Koszul computations.

It verifies 13,406 exact identities. The series inverse is checked through order thirteen as an implementation control; all-order invertibility uses the constant coefficient one. An isolated replay using a copied checker reproduced the certificate byte-for-byte.

Run:

```sh
python branch_a_d03_beta_zero_excess_and_endpoint_checker.py \
  --output branch_a_d03_beta_zero_excess_and_endpoint_certificate.json
```

There are no dependencies beyond the Python standard library, no network calls, and no required companion input files. The inherited input chains are embedded and their full differential identities are reverified.

Certificate content hash, excluding its own hash field:

```text
c4f86de61ab08f7a95c454582f548f9dbba6df42aee4872c299f6f25308ded64
```

Repository provenance, pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: labelled radial/native-normal differential.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: independent occurrence-Koszul correction.
- `research/voevodsky/check_d03_formal_support_purity.rs`: exponential coefficient graph and the scope of fixed-beta normal purity.
- Entry 38, *Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem*: order of scalar extraction and regulator.
- Entry 93, *Alternating Fusion Normalization-Conductor Square*: the two-sheet monomial coefficient ring.

Mathematical conventions:

- Stacks Project, tag 0621: Koszul complexes, parameter homotopies, and unit changes of generators.
- Stacks Project, tag 064K: K-flatness of bounded complexes of flat modules.
- Stacks Project, tag 0A8H: Hom-complex degrees and homotopies.
- Stacks Project, tag 0B4B: effective-Cartier duality and the normal line; no codimension-two purity is claimed for the collapsed pair.

The new nonzero class is the explicitly defined supported morphism difference `[F_mu-F03]`, detected at an endpoint. It is not the physical endpoint-fixed `Delta_J`. The physical comparison would have to explain how this endpoint discrepancy is handled and how the two-normal excess is placed in the appropriate mapping complex. Coincidence of beta supports or a successful central-fibre assignment alone does not supply that comparison.

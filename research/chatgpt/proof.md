# Normalization-kernel conductor homotopy and its endpoint comparison

## Result

There is now an explicit conductor nullhomotopy on the normalization kernel's own source, after the already specified endpoint Čech promotion and the previously specified short-normal graph pullback. It is derived by extending the endpoint unit across the two normalization sheets. Its definition does not use a desired residue or a desired value for the physical secondary class.

Before that target promotion, the normalization connecting class has a nonzero image in **each complete eight-state native endpoint complex**. The entire coefficient line is detected. Thus the localization stage is mathematically essential; the kernel cannot simply be declared contractible over the original node ring.

When a Morse trivialization is composed with this globally defined kernel homotopy, their resulting secondary difference is explicitly exact in the coefficient mapping complex. This is a scoped statement about this construction. It is not an assignment of a value to the physical Delta_J: the source-to-Q comparison and the admissibility of its resulting primitive in the complete physical frame remain unconstructed.

## 1. Coefficient rings and conventions

Let C denote the polynomial spectator coefficient ring, including the six independent Rees parameters and the independent long occurrence and monodromy variables. Localizations of long monodromy units can be included. Write

\[
(x_1,x_2,x_3)=(X_{13},X_{15},X_{35}),\qquad
(y_1,y_2,y_3)=(X_{02},X_{04},X_{24}).
\]

Set

\[
B_+=C[x_1,x_2,x_3],\quad B_-=C[y_1,y_2,y_3],\quad
B=B_+\times_C B_-
  =C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j).
\]

Both maps to C evaluate all short occurrences to zero. Let I_+ and I_- be the respective positive-degree ideals and I=I_+\oplus I_-. The diagonal embedding of C into B is the supplied spectator structure, not a selected normalization sheet.

The short-normal graph is imposed only where explicitly stated:

\[
u_i^+=a_i x_i,\qquad u_j^-=b_j y_j,
\]

with a_i,b_j the corresponding t-parameters. No relation between the long normal u03 and X03 is imposed. Localizing the factors 1+a_i x_i and 1+b_j y_j, which reduce to one on the conductor, preserves the arguments. No Rees parameter is inverted in the base ring.

Homological complexes P_n and V_n are regarded as cohomological complexes in degree -n. For a degree-r cochain F the Hom differential is

\[
\delta F=d_VF-(-1)^rF d_P.
\]

The formulae below fix the sign of the normalization connecting class by its displayed plus-sheet representative. The maps are chain-degree-correct coefficient maps. No global source occurrence-grade shift or comparison of all physical staggered Rees lattices is inferred from these formulas; those would require the source-frame comparison explicitly excluded in Section 6.

## 2. The normalization kernel supplies an actual one-extension

The source-defined sequence is

\[
0\longrightarrow B\xrightarrow{\nu}B_+\oplus B_-
\xrightarrow{\epsilon_+-\epsilon_-}C\longrightarrow0.
\]

This is not the nested-subobject two-extension previously proved to be zero. Its class

\[
\vartheta_\nu:C\longrightarrow B[1]
\]

is nonzero.

A free resolution of C starts as

\[
P_2=B^{24}\longrightarrow P_1=B^6
\xrightarrow{(x_1,x_2,x_3,y_1,y_2,y_3)}P_0=B\longrightarrow C.
\]

The 24 relation columns are the three Koszul syzygies within each sheet and the eighteen mixed syzygies

\[
y_j e_i^+,\qquad x_i e_j^-.
\]

These generate the complete kernel of d1: restrict any relation to the two polynomial sheets, use their ordinary Koszul relations, and then collect the coefficient components belonging to the opposite sheet. This gives exactly the displayed generators. Continue by any free resolution in higher degrees. No truncated resolution is asserted to compute all higher Ext groups.

Two representatives of the connecting class are

\[
\chi_+(e_i^+)=x_i,\quad\chi_+(e_j^-)=0,
\]

\[
\chi_-(e_i^+)=0,\quad\chi_-(e_j^-)=-y_j.
\]

They vanish on the 24 relations, and all other cochain components are zero. Their signs arise from the two coefficient-linear lifts of the conductor unit, (1,0) and (0,-1), under epsilon_+-epsilon_-. These lifts are not B-linear sections of the conductor quotient.

Their difference is

\[
\chi_+-\chi_-=-\delta(1).
\]

The exact class calculation is

\[
\operatorname{Hom}_B(C,B)=0,\qquad
\operatorname{Ext}^1_B(C,B)=C\langle[\vartheta_\nu]\rangle.
\]

Proof: an element annihilated by both sheet ideals is zero. A B-linear map I to B carries I_+ into I_+ and I_- into I_-. On each polynomial sheet a module endomorphism of the three-variable augmentation ideal is multiplication by one polynomial. This follows from the same-sheet syzygies and coprimality of the variables. Therefore Hom_B(I,B)=B_+\oplus B_-. The image of Hom_B(B,B)=B consists of pairs having the same conductor value. Its cokernel is C under the prescribed difference. This proves the assertion for arbitrary polynomial degree, not just a truncation.

An equivalent unit detector on degree-one cocycles is the coefficient of x1 in the e1+ component minus the coefficient of y1 in the e1- component, evaluated on the conductor. It sends both representatives to one and annihilates all boundaries. The exact annihilator of the class in B is I. For a positive-sheet coefficient a in I_+, a chi_+ is the boundary of -a; for a in I_- the representative a chi_+ is already zero.

## 3. Its endpoint-valued native image is nonzero

Use the actual finite endpoint packets

\[
V_+^{\mathrm{fin}}=K_B(a_1x_1,a_2x_2,a_3x_3),\qquad
V_-^{\mathrm{fin}}=K_B(b_1y_1,b_2y_2,b_3y_3).
\]

All eight states of each packet remain. Let p_+,p_- be their unmarked degree-zero states. The bottom-unit maps are

\[
v_\pm^{\mathrm{fin}}:B\longrightarrow V_\pm^{\mathrm{fin}},\qquad 1\longmapsto p_\pm.
\]

Each pushforward of the normalization class generates an injected submodule

\[
C\hookrightarrow\operatorname{Hom}_{D(B)}
(C,V_\pm^{\mathrm{fin}}[1]).
\]

This is not a classification of the entire derived Hom group.

Here is a detector proving the positive-endpoint statement even against arbitrary higher homotopies. A degree-one cochain F has components F1:P1→V0 and F2:P2→V1. Write h1 for the first positive normal state and m=y1 e1+ for the mixed relation. Define

\[
\ell_+(F)=[x_1]F_1(e_1^+)-[y_1]F_1(e_1^-)
+a_1[y_1]\bigl(F_2(m)_{h_1}\bigr).
\]

The coefficient notation extracts the first occurrence coefficient and leaves all spectator variables unspecialized.

For F=delta S, let c be the conductor constant of S0(1), and let A be the conductor constant of the h1 coefficient of S1(e1+). The three displayed terms are respectively a1 A-c, -c, and a1(-A); their signed sum is zero. The dV S2 contribution contains only positive occurrence coefficients and has no y1 coefficient. Higher components do not enter this identity. But ell_+(v_+ chi_+)=1. Thus the class is nonzero. Any scalar lambda in C is detected as lambda. The explicit I-annihilating homotopies from the preceding section remain valid after multiplication by p_+.

For the negative endpoint, the analogous detector is

\[
\ell_-(F)=[x_1]F_1(e_1^+)-[y_1]F_1(e_1^-)
-b_1[x_1]\bigl(F_2(x_1e_1^-)_{k_1}\bigr),
\]

where k1 is the first negative normal state. It has the same value one. This proves the exact annihilator I for each injected class.

In particular, a native B-linear nullhomotopy of these endpoint-valued classes does not exist. It would contradict the detector, regardless of how the other normal states are used.

## 4. The prescribed endpoint Čech promotion changes this answer

For a positive marked subset H, the target coefficient module is

\[
B[(u_i^+)^{-1}:i\notin H],
\]

and the normal differential removes a mark with coefficient one and its exterior sign. The negative endpoint is analogous. The finite-to-Cech map multiplies a state by the product of inverse u_i over its unmarked coordinates. This is the existing target-side rule, not a new global source localization.

Put

\[
U_+=u_{13}u_{15}u_{35},\qquad
U_-=u_{02}u_{04}u_{24},\qquad
v_+=U_+^{-1}p_+,\quad v_-=U_-^{-1}p_-.
\]

In the positive bottom target module all negative occurrence variables act by zero: inverting any a_i x_i makes x_i invertible there, and x_i y_j=0. Similarly, every positive occurrence kills the negative bottom target module.

Consequently there is a B-linear extension of the two endpoint units:

\[
G:B_+\oplus B_-\longrightarrow V_+^{\check C}\oplus V_-^{\check C},
\qquad
G(f_+,f_-)=f_+v_++f_-v_-.
\]

It satisfies G nu = v, where v(b)=b(v_++v_-). The two target components have not been identified. In sheet order (+,-), the coefficient matrix is diagonal in the normalized frames v_+,v_-. In the independently prescribed ray order (D03,13), composing with the source's endpoint swap gives the off-diagonal unit matrix. This checks the label convention; it is not a derivation of a new Q roof.

The normal graph relations are essential. With independent u_i, the element y1/(u1u2u3) is nonzero. For example set all positive occurrences to zero, y1=1, and the independent normals to one. This is a valid specialization in the independent-normal ring. In that model G on the plus sheet fails B-linearity. Thus one must not infer this extension just from the formal word 'Cech'.

## 5. An explicit kernel-side homotopy, with both endpoints retained

Represent C by the two-term complex

\[
T=[B\xrightarrow{\nu}B_+\oplus B_-]
\]

in cohomological degrees -1,0. Its augmentation to C is a quasi-isomorphism. The normalization connecting class is represented by the degree-one cochain

\[
\theta:T\longrightarrow B,\qquad\theta|_{T^{-1}}=1.
\]

The extension G gives the explicit degree-zero cochain

\[
H_\nu|_{T^0}=-G,\qquad H_\nu|_{T^{-1}}=0,
\]

and

\[
\delta H_\nu=v\theta.
\]

No image was assigned from its required residue. The homotopy is forced by the two actual sheet projections and the target normalizations.

On the free conductor resolution, the two section conventions give

\[
h_+(1)=(-v_+,0),\qquad h_-(1)=(0,v_-),
\]

with all higher components zero. They satisfy

\[
\delta h_+=v\chi_+,\qquad \delta h_-=v\chi_-.
\]

Their raw difference is not a secondary cocycle: the boundaries use different cochain representatives chi_+ and chi_-. The exact correction is

\[
h_+-h_-=-v,
\qquad
h_+-(h_--v)=0.
\]

Thus aligning the boundaries using the actual section-change cochain gives a **strictly zero** difference. This does not identify either section with the Morse construction.

## 6. What this implies for the conductor–Morse proposal

Shift the source T by one. The same H_nu becomes a degree-one cochain k_nu:T[1]→V, with

\[
\delta k_\nu=e_\nu,
\qquad e_\nu=v[2]\vartheta_\nu[1].
\]

This is now the degree pattern requested for a conductor trivialization, on the normalization kernel's actual source.

Suppose a separately constructed comparison supplies a closed map a:J→T[1], a Morse cochain h with delta h=a, and the identification of the physical composite with e_nu a. The homotopy supplied by this kernel construction is then

\[
H_{\mathrm{cond}}^{\nu}=k_\nu a.
\]

The corresponding secondary difference is exactly

\[
H_{\mathrm{cond}}^{\nu}-e_\nu h
=k_\nu a-e_\nu h
=-\delta(k_\nu h).
\]

The primitive -k_nu h is explicit once the comparison is supplied. This is not a residue-matching argument and is not a choice to set the difference to zero. It follows from the graded Leibniz rule.

Its physical scope has three boundaries:

1. The physical Q is the support quotient, not automatically the normalization conductor C[1]. No comparison identifying these has been constructed here.
2. The ordinary coefficient primitive can fail additional support, Q-framing, or Rees constraints on admissible homotopies. This computation does not assume it is admissible.
3. The source's unquotiented Morse chain satisfies dH_M=q_J-X3 xi. The usable nullhomotopy is the corrected one H_M tensor p - xi tensor h_occ, whose boundary includes -(d xi) tensor h_occ. Dropping that endpoint term would compare different equations.

The constructed kernel homotopy is endpoint-valued, with zero generic Q component. It cannot by itself supply the missing support-changing comparison. Nor does it identify the previously found mixed native tau class with the physical Delta_J.

## 7. Verification and provenance

The checker is standalone and uses exact integral sparse polynomial arithmetic with the mixed-sheet ideal reduced before every equality. Negative exponents occur only in their declared endpoint target summands. It verifies the 24 relation columns, both connecting representatives, their section-change cochain, explicit ideal annihilators, the sixteen-state endpoint differentials, the finite-to-Cech maps, both native boundary detectors, and the complete Cech conductor homotopies. Its detector identities hold with arbitrary polynomial spectators by linearity; the proof above supplies the unbounded-degree argument.

The sixteen native endpoint columns are extracted from the preceding native matrix file, whose SHA-256 is recorded in native_endpoint_input.json. They are compared after the same short-normal graph pullback. This does not rely on an assertion that a physical connector is already constructed.

Primary source definitions, all at commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61 of andrey-kokoev/marici:

- src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md: the two polynomial sheets and the difference exact sequence.
- research/voevodsky/check_normalization_conductor_bimodule_kernel.py: the source kernel and retained two endpoints.
- research/voevodsky/check_global_k6_koszul_cech_promotion.rs: the precise summandwise normal localizations and diagonal finite-to-Cech comparison.
- research/voevodsky/check_d03_pabs_morse_pullback.rs: the endpoint-corrected Morse identity; the code does not supply H_cond.

Homological conventions and categorical facts: Stacks Project tags 06XP (Yoneda classes), 0A5W (derived Hom using bounded-above projective resolutions), and 0A8H (Hom differential and composition).

Reproduce:

```sh
python check_conductor_kernel_homotopy.py
```

The certificate records the checks actually executed. It marks physical_H_cond_constructed and physical_Delta_value_assigned as false, distinguishing the explicit kernel homotopy from the unconstructed physical source comparison.

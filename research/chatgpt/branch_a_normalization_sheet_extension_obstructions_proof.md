# Branch A — extension across the normalization sheets

Date: 2026-09-07.

## Result and scope

The preceding calculation classified a rank-forty integral lattice of maps from the conductor ideal, with rank thirteen under the stated reflection and rotation transport. This calculation tests whether those maps extend across the actual normalization inclusion. It retains the source relation homotopies rather than testing only the six generator images.

In the same occurrence-map degree zero, output regulator-normal grade three, and homological placement of the ideal in degree three, the result is

\[
0\longrightarrow\mathbb Z^9\longrightarrow\mathbb Z^{40}
\longrightarrow\mathbb Z^{31}\longrightarrow0.
\]

The first term consists of coherent extensions of the two-step source filtration. The last term is the exact obstruction lattice. All image lattices in this sequence are saturated. Under the previously specified symmetry,

\[
0\longrightarrow\mathbb Z^3\longrightarrow\mathbb Z^{13}
\longrightarrow\mathbb Z^{10}\longrightarrow0
\]

is also exact and saturated. There is no index-two or index-three defect in this sequence.

A strict extension has only the zero solution. The nine nonzero coherent directions use nonzero homotopies for the normalization restriction; their normalization-sheet map itself is zero in this degree. Each component of the coherent extension space is contractible.

All six previous relation-only maps, including the two invariant directions invisible on the scalar conductor symbol, have nonzero extension obstructions. By contrast, evaluation on the scalar conductor symbol detects every one of the nine coherent directions.

These are coefficient and source-diagram results. The shift of the ideal, the regulator family, and the target frame are the preceding declared comparison problem. No new geometric Gysin placement, physical conductor–Morse identification, or regulator-zero purity theorem is asserted. The three coherent equivariant directions are not a selected physical map.

## 1. Coefficients, normalization, and the two target filtrations

Let

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/
(X_aX_b:a\in\{02,04,24\},\ b\in\{13,15,35\}),
\]

\[
I_+=(X_{13},X_{15},X_{35}),\quad
I_-=(X_{02},X_{04},X_{24}),\quad I=I_+\oplus I_-,\quad A=R/I.
\]

The normalization modules are

\[
R_+=R/I_-,\qquad R_-=R/I_+,\qquad\widetilde R=R_+\oplus R_-.
\]

The actual conductor inclusion gives the exact sequence

\[
0\longrightarrow I\xrightarrow{j}\widetilde R
\longrightarrow A\oplus A\longrightarrow0.
\]

The doubled quotient is essential. It is the inverse image of the conductor on the two normalization sheets, not the single conductor quotient of the separate difference sequence \(0\to R\to\widetilde R\to A\to0\).

The target is the complete 430-state complex \(C_\beta\) with basis \([F,H,\varepsilon]\), where \(F\) is a noncrossing hexagon dissection, \(H\subseteq F\), and \(\varepsilon=0,1\). Its homological degree is \(3-|F|+|H|+\varepsilon\). Its three differential contributions are the signed radial coefficient \(X_d\), the signed native-circle coefficient \(\beta X_d\), and the separate occurrence coefficient \(X_{35}\). The checker reconstructs and checks every column.

Let \(v\) be graded projection to both complete endpoint packets and \(q\) the actual chain projection to the fourteen-state short-boundary quotient. Define

\[
K_n=\{c\in C_{\beta,n}:q(c)=0,\ v(c)=0,\ v(dc)=0\},
\qquad N=K\cap IC_\beta.
\]

Both are actual subcomplexes. The last condition on \(v(dc)\) retains the incoming endpoint equations; no false chain projection onto the complete endpoint subcomplex is used. The checker constructs saturated component bases and the contraction of the corresponding quotient-map homotopy fibre onto each kernel.

The distinction between \(N\) and \(K\) is necessary for the source-filtration test. A conductor element must map into \(N\). An extension over a normalization-sheet unit, and its restriction homotopy, may have coefficients outside \(I\), but must still preserve the same complete endpoint and \(Q\) frame, hence lie in \(K\).

## 2. Resolve the actual normalization inclusion

The ideal resolution starts

\[
\cdots\longrightarrow R^{92}\longrightarrow R^{24}\longrightarrow R^6
\longrightarrow I\longrightarrow0.
\]

For source generators \(a_i\mapsto X_i\), the twenty-four first relations are

\[
dk_{ij}=X_i a_j-X_j a_i,\qquad dm_{ni}=X_n a_i.
\]

The first formula applies to the six same-sheet pairs; the second to the eighteen ordered opposite-sheet pairs. The ninety-two next relations are the same-sheet Koszul triples, opposite-sheet multiples of same-sheet relations, same-sheet multiples of mixed relations, and opposite-sheet commutativity relations among mixed coefficients.

Exactness in the displayed degrees follows for arbitrary polynomial coefficients by the unique branch decomposition \(a+p_++p_-\). On a fixed sheet, internal relations are its polynomial Koszul relations; coefficients from the other sheet form the annihilator part. Repeating this decomposition on the relation coefficients gives exactly the four stated families of second relations. A free tail may be appended in higher degrees. Its formulas cannot enter the present mapping or homotopy equations because the target vanishes above homological degree four.

Let \(P\) denote this ideal resolution. A normalization resolution \(Q\) is obtained from

\[
Q_0=Rb_+\oplus Rb_-,\qquad Q_1=R^6,
\qquad Q_2=R^{24},\qquad Q_3=R^{92}.
\]

If \(i\) is positive, its degree-one generator maps to \(X_i b_-\); if \(i\) is negative, it maps to \(X_i b_+\). These are exactly the annihilator ideals of the two sheet modules. The remaining differentials are the ideal-resolution differentials, with the corresponding shift in indices.

A resolved inclusion \(j_P:P\to Q\) is

\[
j_P(a_i)=X_i b_{\operatorname{sheet}(i)},\qquad
j_P(P_n)=0\quad(n>0).
\]

It is a chain map. Internal pair relations cancel, and mixed products are zero in \(R\). Its augmentation is the actual inclusion of the conductor ideal into the normalization, not a section chosen on the conductor.

The checker verifies all displayed source squares, degrees, and the resolved inclusion. It also exports a signed cone resolving the doubled upper conductor. Its module in degree \(n\) is

\[
E_n=Q_{n-2}\oplus P_{n-3},
\qquad d_E(q,p)=(-d_Qq-j_Pp,d_Pp).
\]

Thus \(E\simeq(A\oplus A)[2]\). The signs are explicit and are checked; the equivalent conventional cone is obtained by alternating degree signs.

## 3. Complete mapping complexes

A homogeneous target coefficient on \([F,H,\varepsilon]\), for a source generator of occurrence weight \(m\), has occurrence exponent

\[
m+\mathbf1_F-\mathbf1_H-\varepsilon\mathbf1_{35}.
\]

It must be nonnegative and survive the mixed-sheet relations. Its regulator exponent is \(3-|H|\), which must also be nonnegative. For \(N\), it must have positive conductor order. These constraints determine every coefficient; there is no polynomial-degree search cutoff.

The full equations use \(\delta f=d f-(-1)^{|f|}f d\), where \(|f|\) is the map's homological degree. Degree-one homotopies therefore have differential \(d h+h d\).

The exact integer systems give:

| Domain and target | Degree-zero cochains | Closed degree-zero cochains | Degree-one cochains | Closed degree-one cochains | Degree-zero derived maps |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(P[3]\to N\) | 604 | 40 | 0 | 0 | 40 |
| \(P[3]\to K\) | 628 | 64 | 33 | 0 | 31 |
| \(Q[3]\to N\) | 0 | 0 | 0 | 0 | 0 |
| \(Q[3]\to K\) | 115 | 0 | 0 | 0 | 0 |

The first row independently reconstructs the rank-forty result by solving the generator equations and source relations simultaneously. The earlier implementation first solved the sixty generator-cycle coordinates; the new implementation includes those cycle equations in the matrix itself.

The 33 ambient homotopy boundaries are independent. All 64 ambient cocycles are generated by the forty conductor-valued cocycles together with these boundaries. Hence the inclusion gives a saturated surjection

\[
H^0\operatorname{RHom}(I[3],N)\longrightarrow
H^0\operatorname{RHom}(I[3],K)
\]

of ranks forty and thirty-one, with kernel rank nine.

The normalization row includes its unit images, all first source relations, and the equations on the next relations. It is not a strict-module-only computation. Its zero derived-map group rules out extending any of the thirty-one nonzero ambient ideal classes over the normalization sheets in this component.

## 4. Strict extensions and coherent source-diagram extensions

An extension of the filtered source diagram consists of

\[
f:I[3]\to N,\qquad g:\widetilde R[3]\to K,
\qquad \delta H=\iota f-gj,
\]

where \(H\) is a degree-one homotopy on a resolution of the ideal. The relevant mapping complex is

\[
\mathcal E=\operatorname{fib}\left(
\operatorname{RHom}(I[3],N)\oplus
\operatorname{RHom}(\widetilde R[3],K)
\longrightarrow\operatorname{RHom}(I[3],K)\right).
\]

A strict extension sets \(H=0\). The normalization map must be zero, so only \(f=0\) extends strictly.

For a coherent extension, \(g=0\) still, but \(\delta H=f\) is permitted. The complete simultaneous equation matrix has seventy-three unknowns: forty conductor-map coordinates and thirty-three ambient homotopy coordinates. Its rank is sixty-four; every pivot is a signed unit. Its solution lattice has rank nine, and the projection to the forty conductor maps is a saturated injection.

There are no degree-one homotopies between different extension solutions in this component. Such a homotopy would require a degree-one cochain into \(N\), one from the normalization into \(K\), or a degree-two cochain from the ideal into \(K\). All three spaces are zero. Consequently the nine-dimensional component lattice is discrete up to contractible higher mapping spaces. A compatible \(f\) has exactly one \(H\) in the chosen resolution model.

Every one of these \(H\) is supported only on source generator \(a_{35}\), since the separate occurrence partner is the only degree-four target available at a first-generator weight. Its coefficient contains no conductor factor. The homotopy preserves the complete endpoint and \(Q\) conditions, but leaves the conductor-valued target \(N\). This is precisely the extra datum retained by the source-filtration comparison.

## 5. A three-term coherent extension

Define the degree-four chain

\[
\begin{aligned}
U={}&[\{02,03,35\},\{02,03,35\},1]
+[\{02,25,35\},\{02,25,35\},1]\\
&-\beta[\{02,35\},\{02,35\},1].
\end{aligned}
\]

All three terms carry the separate occurrence partner. They are not endpoint states. Their full differential is a nine-term conductor-valued chain. The differential's long-coordinate terms cancel; the remaining coefficients have positive conductor order. The complete endpoint boundary and \(Q\)-projection are zero.

Let \(H(a_{35})=U\) and set every other value of \(H\) to zero. Set \(f=\delta H\). Then

\[
f(a_{35})=dU,\qquad f(a_i)=0\quad(i\ne35),
\]

\[
f(k_{13,35})=X_{13}U,\qquad
f(k_{15,35})=X_{15}U,\qquad
f(m_{n,35})=X_nU\quad(n\in\{02,04,24\}),
\]

and all other source values vanish. All five relation images are essential to the map. The checker verifies all ninety-two next equations, every coefficient, and the complete endpoint frame.

The map \(f\) is nonzero in \(\operatorname{RHom}(I[3],N)\), because that homogeneous Hom complex has no degree-one cochains. It becomes the displayed boundary in \(\operatorname{RHom}(I[3],K)\). Thus \((f,0,H)\) is a nonzero coherent filtered-source comparison, while it does not give a nonzero normalization-sheet map by itself.

For the source's signed scalar conductor element

\[
f_\sigma=X_{25}X_{13}+X_{14}X_{35}+X_{03}X_{15}
-X_{14}X_{02}-X_{25}X_{04}-X_{03}X_{24},
\]

this example satisfies

\[
f(f_\sigma)=X_{14}dU=d(X_{14}U).
\]

The primitive \(X_{14}U\) is outside the conductor-valued target. No occurrence or regulator factor has been inverted. The scalar symbol therefore retains a relative class together with its explicit ambient compatibility homotopy.

## 6. The genuine normalization obstruction

For any of the forty ideal maps, define a map on the doubled-conductor cone by

\[
\operatorname{Ob}_f(q,p)=f(p):E\to K.
\]

The cone differential makes this a chain map. It is the connecting obstruction for extending \(f\) across \(j\). The exact triangle identifies its class with an element of

\[
\operatorname{Hom}_{D(R)}((A\oplus A)[2],K).
\]

Since \(H^0\operatorname{RHom}(\widetilde R[3],K)=0\), the connecting map is injective on the rank-thirty-one ambient ideal-map group. The certificate exports all forty connecting cocycles and the rank-thirty-one coordinate readout. This identifies a rank-thirty-one submodule in the obstruction target; it does not assert that the entire target Hom group has rank thirty-one.

For a coherent extension, the source-cone primitive is \((q,p)\mapsto H(p)\), whose differential is exactly \(\operatorname{Ob}_f\). This is verified in every case. Thus the source-derived obstruction is zero exactly on the nine computed directions, not merely on a selected example.

A simple nonextendable example is the preceding strict negative-sheet map. Write

\[
L_{03}=[\{03,13,35\},\{03,13,35\},0]
-\beta[\{13,35\},\{13,35\},0],
\]

and set \(\Phi_-(a_i)=X_iL_{03}\) for negative-sheet generators, with all positive-sheet values and relation images zero. This is a valid map from the whole ideal. It remains nonzero in the ambient framed target: an ambient homotopy on \(a_{02}\) would require a degree-four coefficient of weight \(\epsilon_{02}-\epsilon_{35}\), which is not polynomial. Its normalization obstruction is therefore nonzero, and the exported quotient coordinates detect it directly.

The six relation-only maps also all survive the rank-thirty-one obstruction readout. Their inclusion is saturated and injective. Vanishing on the scalar element \(f_\sigma\) does not make their normalization obstruction vanish.

## 7. Symmetry and what remains selectable

The calculation uses the existing action \(r(v)=v+2\) and \(s(v)=2-v\), with the source's top-cell and native-mark signs. Reflection fixes the occurrence label \(35\); rotation transports it through \(35,15,13\). No one-step sheet-exchange symmetry is added to the fixed component.

The action preserves the nine-dimensional extension kernel. Exact integral matrices give invariant ranks thirteen, three, and ten in the forty/nine/thirty-one sequence. The invariant obstruction image has ten unit diagonal factors, so

\[
0\to\mathbb Z^3\to\mathbb Z^{13}\to\mathbb Z^{10}\to0
\]

has no finite-index cokernel. All three invariant coherent extensions are exported and checked as full chain maps and compatibility homotopies on all three occurrence-labelled targets.

The relation-only submodule has two invariant directions. Both are genuine normalization obstructions. Thus imposing this coherent source-filtration compatibility eliminates the two undetected invariant parameters of the previous scalar-symbol evaluation, rather than choosing values for them.

Evaluation on \(f_\sigma\) is injective on the nine coherent directions. It is consequently injective on their three invariant directions as well. The three families are distinguishable by their chain-valued scalar-symbol images and remain accompanied by their restriction homotopies.

This does not select a physical image of the scalar symbol. It gives a smaller, explicit source-compatible family, and the exact obstruction to putting any excluded candidate in that family. A geometric normalization–conductor/Gysin comparison must determine the remaining three coordinates and its compatibility homotopy. Matching scalar residues or discarding the doubled conductor would not do so.

## Reproduction

Run the standalone standard-library checker:

```bash
python branch_a_normalization_sheet_extension_obstructions_checker.py \
  --output branch_a_normalization_sheet_extension_obstructions_certificate.json
```

It reconstructs the source and target, all map and homotopy equations, the cone obstruction maps, the saturated integral sequences, and the transported symmetry. It does not read predecessor certificates or require a network connection or companion file. An isolated replay with a different Python hash seed reproduced the certificate byte-for-byte.

The checker reports 426,963 exact checks. The mathematical payload SHA-256 is

```text
1928ac438af7e5fbc7350934c9dad90412a1108197e7f60a2c788e6cda347d78
```

### Source provenance and conventions

Repository: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: normalization, conductor ideal, doubled upper conductor, and six-term scalar symbol.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, blob `b967151cb0ee822e2361b9334a4ab26082c12682`: signed radial/native differential, face supports, and symmetry.
- The previous `branch_a_normalization_ideal_descent_checker.py`: source resolution and frame conventions. Its rank-forty result is reconstructed from a new, unreduced map-equation system rather than assumed.
- Stacks Project Tags `0A8H`, `064B`, `014D`, and `0117`: Hom differentials, derived maps from projective resolutions, mapping cones, and connecting sequences.

The source's fixed-nonzero-regulator physical purity theorem remains separate. This calculation concerns its declared polynomial coefficient family and does not prove a new regulator-zero geometric realization.

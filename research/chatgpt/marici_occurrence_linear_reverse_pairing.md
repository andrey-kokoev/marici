# The occurrence-linear reverse pairing: an ideal-valued map and its support defect

Date: 2026-09-07  
Project: Marici, Branch B  
Input commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result

The cubical complementary-support construction admits an exact continuation that retains arbitrary polynomial occurrence coefficients. In the critical plus-branch/D03 excess channel, its reverse connecting pairing has image the ideal **(X2,X4)**, not the entire occurrence ring.

The earlier integer-valued pairing with value one was correct in its specified fully homogeneous slice. It does not extend to a polynomial-linear, occurrence-ring-valued derived trace on the full coefficient family with the same normalization. This is a concrete failure of the previously unproved promotion, not a contradiction of the slice calculation.

The new calculation constructs the actual polynomial-linear reverse map, both generating covectors, and the supported quotient measuring its failure to attain one. It also retains the complete endpoint complexes and their separate source frames. The necessary residual support is the actual noncrossing short pair x2,x4. It is distinct from the branch-normal support and from both integer-prime obstructions.

The statement is scoped to a trace linear over the occurrence polynomial ring with values in that ring, with the already specified normal and determinant frames. A supported-duality or coefficient-line-valued physical trace can have a different target. No equivalence with that physical functor, no new physical cell, and no reflection parity is asserted here.

## 2. Keep the occurrence family rather than one occurrence degree

Let

\[
A=\mathbb Z[X_0,X_1,X_2,X_3,X_4,X_5,X_{D03},X_{D14},X_{D25}],
\qquad R=A[u_a\mid a\in\mathscr D].
\]

In words: occurrences remain polynomial variables over the integers; the nine normal parameters are a separate family.

The target state indexed by H contained in a noncrossing face S has coefficient module

\[
R_{S,H}=R[u_a^{-1}:a\in S\setminus H].
\]

In words: normal inversion remains confined to the unmarked directions of that particular state. Occurrence variables are never inverted on this polynomial base.

The target differential is the original one:

\[
\begin{aligned}
d[S,H]={}&\sum_{a}(-1)^{\#\{s\in S:s<a\}}
 \frac{X_a}{u_a}[S\cup\{a\},H]\\
&+\sum_{h\in H}(-1)^{3-|S|+\operatorname{pos}_H(h)}[S,H\setminus\{h\}].
\end{aligned}
\]

In words: retain the radial occurrence factor and the unit normal-localization coefficient, together with their source signs. The code reconstructs these rules from the pinned source rather than modifying its pole domains [S1].

Fix only the normal degree. A nonzero homogeneous normal component of a target summand is then one free module over A. In that basis a radial coefficient is **X_a**, not one; a normal or source-Koszul coefficient is a signed unit after accounting for its normal degree. Arbitrarily high occurrence degrees are present. This is not a bounded polynomial truncation.

The inherited occurrence grading of the free generators is still recorded: a state supported on S has occurrence shift minus the sum of the degrees of the X_a in S. Suppressing those shifts in a matrix display does not discard them or authorize a division.

## 3. The actual source and supported branch comparison

Keep the complete source

\[
D=K_R(u_1,u_3,u_5)\otimes_R K_R(u_0,u_3),
\qquad \eta=h_3^+-h_3^{03}.
\]

In words: both copies of the common normal remain in the source; their difference is the independent excess class. These are the source's actual branch and pair ideals [S2].

After the previously constructed supported branch-purity operation, the residual source is K(u0,0). The dual determinant of the three odd branch normals and the shift by three remain part of the target. In particular the second residual generator has zero differential, not zero value.

Write

\[
\gamma=e_{u_{D03}}+e_{u_{D14}}+e_{u_{D25}},
\qquad
\lambda=\gamma-e_{u_0}-e_{u_1}-2e_{u_3}-e_{u_5}.
\]

In words: this is the same critical excess normal frame as before. The repeated source normal is counted twice. There is no occurrence-degree restriction in this continuation.

For a target support object T, let C_T be its derived source-Hom complex in this normal degree, retaining the full A-module structure. The Hom differential is the usual target differential minus the signed source differential [M1].

The reference-chart comparison from the complete 32-state source to the branch-purity model was checked over A, including its entire cone:

| Target | Raw source-Hom columns | Purity columns | Cone columns | Signed-unit cancellations |
|---|---:|---:|---:|---:|
| K | 220 | 44 | 264 | 132 |
| B | 213 | 37 | 250 | 125 |
| V | 18 | 2 | 20 | 10 |
| E | 202 | 42 | 244 | 122 |
| Q | 7 | 7 | 14 | 7 |
| B/V | 195 | 35 | 230 | 115 |

Every cone cancels completely. The comparison thus remains a quasi-isomorphism over the occurrence polynomial ring; it was not validated merely by agreement of ranks. Here V is the full two-endpoint support, B is the full short-boundary support, E=K/V, and Q=K/B.

All six transported branch/pair charts satisfy the polynomial differential equations with their original orientation signs. The code checks the transported matrices, not equivariance of an arbitrarily chosen contraction.

## 4. An exact polynomial deformation retraction

On every complex, cancel only differential entries equal to +1 or -1. Retain the projection, inclusion, and contracting homotopy, and verify all their equations over A. No X_a is used as a pivot.

For K and E the resulting core has four generators. After a signed reordering, it is

\[
C_K\simeq C_E\simeq
\left[
A\xrightarrow{(X_2,X_4)^T}A^2
\xrightarrow{(-X_4,X_2)}A
\right],
\]

in cohomological degrees two, three, and four.

In words: this is the actual weighted incidence of the empty face, the two remaining compatible short labels, and their edge. It is a Koszul complex on two independent occurrence coordinates, not an acyclic integer interval with all weights erased.

Let q,a2,a4,a24 be its ordered generators. Their inherited occurrence degrees are

\[
\deg q=0,\quad \deg a_2=-e_{X_2},\quad
\deg a_4=-e_{X_4},\quad
\deg a_{24}=-e_{X_2}-e_{X_4}.
\]

In words: multiplication by each displayed occurrence variable makes the differential homogeneous. The signs in the executable source basis differ by the stated signed basis change only.

The support maps reduce to the actual subcomplex and quotient:

\[
C_B\simeq C_{B/V}\simeq
\left[A^2\xrightarrow{(-X_4,X_2)}A\right],
\qquad C_Q\simeq A[-2],\qquad C_V\simeq0.
\]

In words: short support retains the two vertices and edge; the generic quotient retains the empty-face term; the entire endpoint comparison complex is contractible in this particular normal frame.

The reduction counts are 20 cancellations for K, 17 for B, 19 for E, one for V, three for Q, and 16 for B/V. The stored homotopy satisfies the exact identity on every original column, not only on cycles.

### The cohomology that one fully homogeneous slice does not see

Put

\[
I=(X_2,X_4)\subset A.
\]

In words: I is a proper codimension-two ideal of independent occurrence parameters.

Because X2,X4 form a regular sequence, the complete polynomial core has

\[
H^4(C_K)=H^4(C_E)=A/I,\qquad H^j(C_K)=H^j(C_E)=0\quad(j\ne4).
\]

In words: the full occurrence family contains an additional supported class. Its occurrence shift is that of a24. Regular Koszul exactness proves this for all coefficients [M2].

The short complex has

\[
H^3(C_B)=A[\beta],\qquad H^4(C_B)=A/I,
\qquad \beta=X_2a_2+X_4a_4.
\]

In words: the old transgression is still a free generator of the degree-three cohomology. However, its cycle representative is not a direct summand of the degree-three free module. Two coprime polynomial coordinates need not generate the unit ideal.

The original fully homogeneous occurrence-zero component has basis q, X2 a2, X4 a4, X2 X4 a24. Its matrices have coefficients one and it is acyclic. The supported class A/I has no occurrence-zero component in its inherited shift. Thus the previous integer-slice calculation and the new family calculation are compatible.

## 5. The reverse connecting pairing is exactly ideal-valued

Take the derived dual over the occurrence ring:

\[
C_T^{\vee_A}=\operatorname{RHom}_A(C_T,A).
\]

In words: dualize the finite free A-complex, rather than first extracting an occurrence degree and then taking its integer dual.

The reverse connecting homomorphism is represented, up to the fixed overall connecting sign, by

\[
A^2/A(-X_4,X_2)
\longrightarrow A,
\qquad [(a,b)]\longmapsto X_2a+X_4b.
\]

In words: the two covectors evaluate the two actual weighted short incidences. The quotient accounts for all cochain homotopies, not a selected representative.

The kernel of the row (X2,X4) is exactly A(-X4,X2). To see this directly, X2 a=-X4 b implies X2 divides b, since X2 and X4 are relatively prime polynomial variables. Write b=X2 c and then a=-X4 c. Therefore

\[
H^{-3}(C_B^{\vee_A})\cong I,
\qquad
\partial^{\vee_A}:I\hookrightarrow A
      =H^{-2}(C_Q^{\vee_A}).
\]

In words: the reverse connecting map is the inclusion of the proper ideal I. Its image is neither smaller nor larger.

Its cokernel is

\[
\operatorname{coker}\partial^{\vee_A}\cong A/I,
\qquad \overline1\ne0\in A/I.
\]

In words: the class of one is the exact obstruction to a global polynomial-linear reverse trace with unit generic value.

No choice of additional polynomial covectors or cochain homotopies can change this image ideal: they have all been included in the quotient above. Including the two endpoint comparison variables does not remove it because C_V has an explicit signed-unit contraction in this frame. This does not identify C_V in this frame with the separate nonzero endpoint residue frames.

The supported class has infinite additive order. Inverting two, three, six, or any nonzero integer does not change the fact that I is proper in the corresponding polynomial ring.

### Explicit rows before contraction

The two generating short covectors are minus the coefficient rows for the residual-pair top input mapping to the unmarked x2 and x4 facet states. Extend either covector by zero to the full complex. Its boundary is supported entirely on the actual generic chamber row, with respective coefficients X2 and X4.

Thus both generators are present in the original spatial kernel. The polynomial coefficient is the part that cannot be removed by a scalar normalization.

The old single-row covector on `[x2,D25; D25 marked]` illustrates the distinction particularly clearly. As an A-linear coefficient-row functional it evaluates the old nine-term obstruction to X2 X_D25. Extracting the coefficient of that monomial returns the integer one, but coefficient extraction is not A-linear: it sends X2 to one and sends one to zero. The occurrence degree cannot be frozen before testing coefficient-linearity.

## 6. The weighted spatial kernel and its diagonal

The underlying cubes from the preceding construction remain valid. Their polynomial-linear boundary is now

\[
\partial_A\square(H,S)=
\sum_{a\in S\setminus H}(-1)^{\operatorname{pos}(a)}
\left(\square(H\cup\{a\},S)-X_a\square(H,S\setminus\{a\})\right).
\]

In words: the upper face has unit coefficient and the lower face retains its actual occurrence coefficient. This equation is checked against the signed transpose on all 215 cells in the normal degree admitting every marked state. The same inequality-defined relative faces give the restrictions to other normal frames.

The numerical cubical diagonal therefore cannot simply be reused as a diagonal into one ordinary tensor product over A. Already for a single interval with

\[
\partial e=v_1-Xv_0
\]

the old formula gives

\[
\partial\Delta e-\Delta\partial e
=(1-X)v_0\otimes v_1.
\]

In words: its coefficient-free Serre diagonal fails the polynomial chain equation. This is not a failure of the correctly typed coefficient-line or sheafwise diagonal, which may use a different tensor target.

The obstruction is not just failure of that one formula. Write the most general degree-one image as

\[
\Delta e=A_0e\otimes v_0+A_1e\otimes v_1
          +B_0v_0\otimes e+B_1v_1\otimes e.
\]

In words: all four possible product edges are allowed, with arbitrary polynomial coefficients. Requiring both vertex images to remain group-like yields

\[
X(A_0+B_0)=X,\qquad A_1+B_1=1,
\qquad A_0=XB_1,\qquad B_0=XA_1.
\]

In words: these equations would imply X squared equals X in the polynomial ring, which is false. Hence no such polynomial-linear diagonal has both of those fixed vertex columns. The coefficient transport data of the physical cap are substantive additional structure.

This is a second local check on why the integer spatial realization was not already the requested ringed physical kernel. No claim is made against a cap construction with its genuine coefficient-system pairings and determinant lines.

## 7. The obstruction has a canonical supported representative

On the principal open set where X2 is invertible, a reverse trace is represented by (1/X2,0). Where X4 is invertible, it is represented by (0,1/X4). These are actual open restrictions, not allowed formulas over the original closed polynomial base.

Their difference is

\[
\left(\frac1{X_2},0\right)-\left(0,\frac1{X_4}\right)
=-\frac1{X_2X_4}(-X_4,X_2).
\]

In words: on the overlap the traces agree up to an explicit Koszul homotopy. They supply a derived unit trace away from the residual closed support, without choosing a global polynomial inverse.

The overlap coefficient determines the primitive local-cohomology class

\[
\left[\frac1{X_2X_4}\right]\in
A[(X_2X_4)^{-1}]/\bigl(A[X_2^{-1}]+A[X_4^{-1}]\bigr).
\]

In words: its two negative occurrence exponents prevent it from coming from either singly localized summand. This is the degree-two local-cohomology group of the residual ideal, computed by the extended Cech complex [M3].

With the ordered occurrence-conormal determinant retained, the corresponding regular-immersion class is

\[
\operatorname{Ext}^2_A(A/I,A)
\cong (A/I)\otimes\det(I/I^2)^\vee.
\]

In words: the failure to extend the unit trace is naturally a codimension-two occurrence-supported Gysin class. It is not an arbitrary chosen parity or an ordinary nullhomotopy.

This identifies a possible output of a correctly typed supported operation. It does not license appending a formal residue to the physical comparison. The prescribed source geometry must supply that occurrence-support operation and its relation to the already existing branch-normal Gysin class.

## 8. Endpoint frames, Rees parameters, and transports

The two branch endpoint residue channels were recomputed without freezing occurrence degree. Their underlying modules are free A-lines in the appropriate degrees, but the **prescribed source classes** carry their original principal occurrence factors. In the reference plus chart these are X1 X3 X5 times the endpoint generator, with the existing excess orientation sign. They are not units of A before the supplied principal-line pairing.

This preserves the distinction made in the earlier supported comparison: pairing with the dual of the supplied principal occurrence line is legitimate without an occurrence-ring inverse. It is not the same operation as trivializing the non-principal ideal (X2,X4). That ideal is not an invertible line at its codimension-two support, and its generators have no common polynomial factor that can be removed to make them unimodular.

Reflection exchanges the two branch frames. The six transported residual ideals are

\[
(X_2,X_4),\ (X_3,X_5),\ (X_0,X_4),\
(X_1,X_5),\ (X_0,X_2),\ (X_1,X_3).
\]

In words: each is the pair of short labels left outside the transported branch/pair normal sequence. All come from actual compatible short faces, and all remain proper ideals.

Tensoring the complete polynomial core and its support maps with the previously constructed independent Rees-supported coefficient operation preserves the factor X2 a+X4 b. All eight central Rees faces of that tensor differential were checked. The existing normal residue can turn an integer incidence evaluation into its branch Gysin value, but it does not turn the proper residual occurrence ideal into the unit ideal.

Under the stated independence of the occurrence coordinates from the supported coefficient factor, the possible supported values are therefore I times the prescribed branch Gysin class. They do not include the bare primitive Gysin class. An additional source identification that changes this independence or supplies the residual occurrence trace would need to be constructed explicitly, not inferred from numerical agreement.

The actual excess generator is retained throughout. No target normal multiple is substituted for it, and no claim that a bare excess cycle survives in the same target degree is added.

## 9. Consequence for the requested source-to-kernel construction

The continuation has produced a coefficient-natural reverse map and a complete obstruction to promoting it to a unit-valued trace over the original polynomial base. It has not produced the full normalization-sheet source morphism into a ringed supported-Verdier kernel.

The remaining issue is now specific: the source's cap or extraordinary comparison must explain the residual occurrence-support class and its determinant, while carrying the two endpoint connector cells. In particular it must distinguish the legitimate endpoint principal-line pairing from the non-principal residual pair ideal.

Repeating the integer degree-zero contraction would hide precisely this extra support. Replacing the raw source by a constant-differential or globally localized model is not used here. The result also does not contradict the previously computed native-normal exceptional resonance: that source-side issue is separate and is not assumed absent.

No physical reflection parity is assigned.

## 10. Reproduction, scope of checks, and sources

Run:

```sh
python check_marici_occurrence_linear_reverse_pairing.py \
  --output marici_occurrence_linear_reverse_pairing_certificate.json
```

The self-contained standard-library checker passes **22,304 exact assertions**. It verifies the original coefficient domains, polynomial differentials, complete signed-unit SDRs, six full-source purity cones in the reference chart, all six transported purity diagrams, both endpoint residue frames with their actual occurrence factors, the literal support maps, both reverse covectors, the 215 weighted cubes, principal-open comparison homotopies, and all eight Rees-face tensor differentials.

All occurrence polynomial degrees are covered by the symbolic polynomial identities and the regular-sequence proof, not sampled by a maximum degree. Normal degrees are the specified excess frame, its six transports, and the separate endpoint frames; no computation of every normal frame is claimed. The source purity comparison retains its full 32-state source. The number of assertions is not proof-assistant certification.

[S1] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, pinned blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`.

[S2] `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`, pinned blob `df8448271089910a90c8e641af5b8ae95f1472dd`.

Prior local inputs: `marici_cubical_supported_dual_kernel.md`, `marici_branch_purity_dual_transgression.md`, and `marici_rees_supported_residue_trace.md`. Their source-category, variance, determinant, and physical-parity qualifications remain in force.

[M1] Stacks Project, Hom complexes, tag `0A8H`: `https://stacks.math.columbia.edu/tag/0A8H`.

[M2] Stacks Project, The Koszul complex, tag `0621`: `https://stacks.math.columbia.edu/tag/0621`. Exactness in the particular two-variable case used here follows directly from the displayed polynomial divisibility argument.

[M3] Stacks Project, Local cohomology, tag `0952`: `https://stacks.math.columbia.edu/tag/0952`.

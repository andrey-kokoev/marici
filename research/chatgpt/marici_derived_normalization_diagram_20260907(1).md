# The complete derived normalization diagram: cancellation, filtration, and endpoints

Date label: 2026-09-07. Repository baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result and scope

The infinite auxiliary-normalization Tor terms found in the occurrence-preserving bridge do not obstruct comparison of the **total conductor kernel**. The conductor term has its own derived terms, and the actual conductor-difference map pairs the two sets by integral isomorphisms in every positive degree. I construct the comparison of complete kernels and an explicit contraction of its kernel.

This is not an equivalence of the normalization diagrams with their intermediate objects fixed. The contraction moves between the normalization and conductor rows. I compute its exact failure for the two-step row filtration, including the complete Rees comparison kernel. I also compute the different result for the relative normalization quotient and for the source's quotient-and-road endpoint pattern: their comparison retains a nonzero, unbounded fibre.

All these are coefficient-category statements. No independent geometric support-changing operation, native generic-Q source map, or endpoint connector 2-cell is inferred from them. The finite physical normal Tor-zero/Tor-one packet and the auxiliary base-change Tor groups computed here are different constructions.

## 1. Rings, degrees, and the two normalization rows

Let C be the retained polynomial/Laurent spectator ring. Set

\[
S=C[x_1,x_2,x_3,y_1,y_2,y_3],\qquad
U=S[a,b]/(ab),\qquad
B=S/(x_i y_j:1\le i,j\le3).
\]

In words: x and y are the existing positive and negative occurrence triples; a and b are the two auxiliary branch coordinates formerly denoted z-plus and z-minus. The coefficient map fixes all occurrences and kills a and b.

Write

\[
I_+=(x_1,x_2,x_3)B,\qquad I_-=(y_1,y_2,y_3)B,\qquad
I=I_+\oplus I_-,\qquad C=B/I,
\]

\[
N_U=U/(b)\oplus U/(a),\qquad N_B=B/I_-\oplus B/I_+.
\]

In words: the actual native normalization has two separate occurrence sheets. Its conductor is the spectator ring, not the full occurrence base S.

The source gives the two exact rows

\[
0\to U\to N_U\xrightarrow{\delta_U} S_{\mathrm{or}}\to0,
\qquad
0\to B\to N_B\xrightarrow{\delta_B} C_{\mathrm{or}}\to0.
\]

Both maps are the difference of the two conductor values. The subscript records the sign under sheet exchange. The relative base and the two conductor ideals are kept distinct. The normal-form decomposition of B proves the second row directly.

Every complex in this note is homologically graded: its differential lowers degree, and M[k] places a degree-zero module M in degree k. Thus the conductor kernel

\[
\mathcal K_U=[N_U\to S_{\mathrm{or}}],\qquad
\mathcal K_B=[N_B\to C_{\mathrm{or}}]
\]

has degrees zero and minus one. Its only homology is U or B in degree zero, respectively. The relative normalization cofiber is a different operation: it has the conductor quotient in degree zero.

## 2. Resolve both rows before base change

For the auxiliary positive branch U/(b), use a rank-one resolution with differential b in odd positive degree and a in even positive degree. For U/(a), exchange a and b. Exactness follows in every degree from

\[
\operatorname{Ann}_U(a)=(b),\qquad
\operatorname{Ann}_U(b)=(a).
\]

These identities hold coefficientwise: U is a free S-module on the constant and positive pure a- and b-powers. No exponent cutoff enters the proof.

Let M^U be the direct sum of those branch resolutions. Resolve the conductor S by L^U, with

\[
L^U_0=U,\qquad L^U_n=U^2\quad(n\ge1),
\]

\[
d_1=(a\ b),\qquad
 d_{2k}=\operatorname{diag}(b,a),\qquad
 d_{2k+1}=\operatorname{diag}(a,b)\quad(k\ge1).
\]

The kernel of the first differential is (b) in its first coordinate and (a) in its second: the a- and b-images have no common nonzero monomial. This proves exactness at degree one as well as in the periodic tail.

The conductor difference lifts to an actual map of resolutions

\[
c_0=(1\ -1),\qquad
c_n=J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\quad(n\ge1).
\]

In words: the positive branch maps to the b-coordinate and the negative branch maps to minus the a-coordinate. Direct multiplication with the displayed differentials proves the chain equation in both parities, including degree one. The matrix J has determinant one.

The fibre of this lifted difference is a bounded-below free resolution of the conductor kernel. It is therefore K-flat. Derived base change is computed by tensoring this resolution with B. This is the exact derived-tensor construction, not an ordinary replacement of every source module by its quotient [M1].

After base change, put

\[
M=B\otimes_U^L N_U,\qquad L=B\otimes_U^L S_{\mathrm{or}}.
\]

The explicit models have zero internal differential, since a and b act by zero:

\[
M_n=B^2\quad(n\ge0),\qquad
L_0=B_{\mathrm{or}},\quad L_n=B^2\quad(n\ge1).
\]

The difference map is still c-zero and J as above. Each individual derived normalization term has genuine higher Tor. The conductor has genuine higher Tor too; omitting it would change the total complex.

## 3. The complete conductor-kernel comparison

Let

\[
\mathcal T=\operatorname{fib}(c:M\to L).
\]

In the chosen model

\[
\mathcal T_n=M_n\oplus L_{n+1},\qquad
 d(m,\ell)=(0,c_n m).
\]

The degree-minus-one term is L-zero. In this notation the second component on the right belongs to degree n minus one. There are no internal differentials after base change.

Define the comparison to the native kernel by

\[
\alpha_M^0(f,g)=(f\bmod I_-,g\bmod I_+),\qquad
\alpha_L^0(h)=h\bmod I,
\]

and send all positive resolution degrees to zero. The normalization and conductor square commutes on every polynomial. Hence it defines a chain map

\[
\alpha:\mathcal T\longrightarrow\mathcal K_B.
\]

Its induced degree-zero map sends the diagonal copy of B to its actual two branch restrictions. This is the identity on the identified native ring B.

### Exact comparison kernel

Let D-M and D-L be the degreewise kernels of the two comparison maps. They have zero differential, with

\[
(D_M)_0=I_-\oplus I_+,\qquad (D_L)_0=I,
\]

\[
(D_M)_n=(D_L)_n=B^2\quad(n\ge1).
\]

On degree zero the difference map is

\[
\bar c_0(y,x)=y-x.
\]

Its inverse takes x+y to (y,-x), using the canonical splitting I=I-plus direct-sum I-minus. In positive degrees the inverse is J-inverse. These inverses are B-linear, including when B has its native opposite-sheet zero divisors.

Consequently

\[
\ker\alpha=\operatorname{fib}(\bar c:D_M\xrightarrow{\sim}D_L)
\]

is contractible. Explicitly,

\[
h(\ell_n)=\bar c_n^{-1}(\ell_n)\in(D_M)_n,\qquad h(m_n)=0,
\qquad dh+hd=1,\quad h^2=0.
\]

In words: a conductor defect is filled by its matching normalization defect in the next total degree. This uses no inverse polynomial coefficient and no averaging over sheets or roads. The identity proves the all-degree statement independently of the bounded executable tests.

We have constructed

\[
B\otimes_U^L\mathcal K_U\xrightarrow{\sim}\mathcal K_B.
\]

This does not contradict the preceding non-equivalence of the underived map from the U-complex to the B-complex. The domain is now derived base-changed to B. It also does not identify U and B as algebras.

### Two important limits of this conclusion

First, this is an equivalence of total complexes. The intermediate maps M to N-B and L to C are not equivalences.

Second, the kernel contraction is B-linear, but an ambient B-linear chain inverse of alpha has not been supplied or asserted. The degreewise surjection B to B-plus need not split over B. A contractible kernel alone does not turn a non-split short exact sequence of modules into a termwise split sequence. Derived inverses exist; their strict chain presentation can require resolutions [M2].

## 4. The defect retained by the row filtration

Give the conductor row filtration level zero and the normalization row level one. The conductor row is a subcomplex. The comparison preserves this filtration. Its kernel contraction does not: h takes a conductor term into the normalization row.

Both associated-graded comparison kernels are nonzero. Therefore alpha is not an equivalence in the filtered derived category defined by associated-graded quasi-isomorphisms. This assertion concerns this explicitly stated two-step row filtration. It does not assume that every native physical filtration is this filtration.

The comparison defect has a simple Rees model. Introduce a new bookkeeping parameter lambda, independent of every original occurrence and normal parameter. Under the standard increasing-filtration Rees convention its differential is

\[
d_\lambda(m,\ell)=(0,\lambda\bar c_n m).
\]

The same h satisfies

\[
d_\lambda h+h d_\lambda=\lambda\,1.
\]

Since multiplication by lambda is injective on a polynomial extension of any coefficient module, the complete Rees-kernel homology is

\[
H_{-1}=I\otimes_B B[\lambda]/(\lambda),\qquad
H_n=(B[\lambda]/(\lambda))^2\quad(n\ge0).
\]

All orientations and internal occurrence degrees are inherited. The total annihilator of this homology is exactly (lambda), since the positive-degree defect pairs contain free B coefficients. Specializing lambda to one yields the acyclic total kernel. Specializing the complex to zero retains both graded rows. One must specialize the complex, not merely specialize its homology and drop the accompanying Tor.

This is filtration-parameter torsion, not integer-prime torsion. The parameter lambda has not been identified with a geometric Rees time. In the two-row spectral sequence, the first differential is the actual invertible map bar-c in every degree; it cancels the defects after forgetting the filtration [M3]. It is not the separate endpoint d-three transgression constructed earlier.

Thus the infinite auxiliary Tor terms are neither independently added physical states nor freely discardable filtered data. Their role depends on which of the explicit source operations is being compared.

## 5. The relative normalization quotient has a different answer

The source also uses the relative normalization quotient in its endpoint construction. Form

\[
\mathcal R_U=\operatorname{cofib}(U\to N_U)\simeq S_{\mathrm{or}},\qquad
\mathcal R_B=\operatorname{cofib}(B\to N_B)\simeq C_{\mathrm{or}}.
\]

In words: the exact normalization rows identify these cofibers with their conductor quotients, placed in degree zero. This is not the kernel operation of Section 3.

The derived comparison is

\[
L=B\otimes_U^L\mathcal R_U\longrightarrow\mathcal R_B=C_{\mathrm{or}}.
\]

Its fibre is the explicit zero-differential complex

\[
\mathcal E_\infty=\operatorname{fib}(L\to C_{\mathrm{or}}),\qquad
H_0(\mathcal E_\infty)=I_{\mathrm{or}},\quad
H_n(\mathcal E_\infty)=B^2\quad(n\ge1).
\]

This same E-infinity is isomorphic to either intermediate defect D-M or D-L. It cancels between two rows in the total kernel; there is no second row to cancel it when only the quotient is retained.

### Unit tests and coefficient-linear sections are different

The element one of B maps to one of C. A test of the single scalar unit therefore passes.

A B-linear section of the whole quotient would be a different map. Any B-linear map from C to B sends one to an element annihilated by I. But

\[
\operatorname{Ann}_B(I)=0.
\]

For proof, write b=c+f-plus+f-minus in its unique normal form. Multiplying by a positive occurrence detects c and f-plus; multiplying by a negative occurrence then detects f-minus. Hence b is zero if I kills it. This argument is coefficientwise and needs no field extension.

Any proposed derived section also induces a section on degree-zero homology. The displayed annihilator calculation therefore rules it out. Extra higher maps cannot change that induced homology map [M4]. This excludes the specified coefficient-linear section, not a scalar representative or a support-changing map of different variance.

Over the smaller spectator ring C, normalized markings of L have a different, nonempty fibre. Translation by its constant unit identifies that fibre with the Dold-Kan marking space of E-infinity: components are I, and its positive homotopy groups are B-squared. This illustrates why the source ring of a marking problem must be specified. These are auxiliary-comparison homotopies, not an identification with the native physical moduli object.

## 6. Include the full quotient-and-road endpoint pattern

Entry 142 prescribes the conductor quotient and the complete oriented road resolution, with difference, cyclic boundary, and norm maps [S2]. To test the above comparison in that pattern, keep the entire road resolution rather than only its final augmentation.

Resolve every auxiliary conductor module by L-U, and both normalization sheets by M-U, before applying the occurrence quotient. The resulting bicomplex has commuting horizontal and vertical maps before totalization. The horizontal maps are exactly the source's conductor difference, normalization relation, road boundary, and norm. The standard total differential is the horizontal differential plus the signed vertical differential.

After base change the vertical differentials vanish. In auxiliary resolution degree zero the four-term row has ranks

\[
1\longrightarrow4\longrightarrow5\longrightarrow1
\]

and differential ranks one, three, one. In each positive auxiliary degree it has ranks

\[
2\longrightarrow6\longrightarrow8\longrightarrow2
\]

and differential ranks two, four, two. The latter row has no new node-relation summand: its sheet-to-conductor map is the invertible two-by-two matrix J. Each row retains the actual three-road resolution for every conductor coefficient.

The complete base-changed endpoint object and its native counterpart satisfy

\[
\mathbb P_{\mathrm{der}}\simeq L[1],\qquad
\mathbb P_{\mathrm{nat}}\simeq C_{\mathrm{or}}[1],
\qquad
\operatorname{fib}(\mathbb P_{\mathrm{der}}\to\mathbb P_{\mathrm{nat}})
\simeq\mathcal E_\infty[1].
\]

In words: including all road relations does not remove the auxiliary normalization base-change defect from this relative endpoint operation.

The comparison fibre has I in homological degree one and two copies of B in every degree at least two. The actual road augmentation gives primitive coefficient readouts for each row, with no division by two or three. All row homologies are computed by integral unit pivots and explicit primitive representatives in the checker.

This endpoint object is the source's **coefficient quotient-and-road pattern** applied to the specified rings. It is not asserted to be the native full 215-state geometric endpoint source. In particular, changing the conductor from S to C is part of this test, not a derivation that the physical generic leg must lie on C.

## 7. Equivariance, localization, and the full target differential

Reflection swaps the two normalization-resolution slots and exchanges a with b. On the conductor resolution it acts by minus one in degree zero and by minus the two-coordinate swap in positive degree, together with its action on coefficients. The matrix identity

\[
-J_{\mathrm{swap}}J=J J_{\mathrm{swap}}
\]

expresses compatibility of the positive-degree difference map. The ordered x/y labels are transported by the actual vertex permutations i to i-plus-two-r and i to one-minus-i-plus-two-r. The low-degree inverse (x+y) to (y,-x) also commutes with these actions. The full kernel contraction is therefore equivariant.

For road terms, use the source cyclic permutation r. Reflection on the road factor is the reversing permutation, on the tag factor it is minus r-inverse times that permutation, and on the norm factor it is minus one, tensored with the conductor orientation action. The checker verifies all six actions on every tested endpoint row. No equivariant splitting of the primitive road representative is claimed.

Every formula is natural under the allowed coefficient localizations. With the actual short-normal relation u-s=t-s X-s, inverting a short normal on one native sheet kills the opposite sheet and the conductor. Inverting opposing sheet occurrences gives the zero ring. The module decompositions and the kernel homotopy localize to these legitimate zero or nonzero modules; no inverse is evaluated at zero in a nonzero target.

The checker reconstructs all 215 loaded states and 522 covering incidences from the source differential. Their localization census remains 72 states with no short occurrence inverted, 64 on each separate punctured sheet, and 15 zero mixed-localization states. The equivalence of total scalar kernels can be tensored with this bounded-flat target complex. More generally, arbitrary tensors must be derived; the native two-term kernel presentation is not silently treated as termwise flat.

At chain level, h on the coefficient defect has degree plus one. For each actual target incidence, the two mixed terms in the tensor homotopy cancel with signs (-1) raised to q-plus-one and q. Thus the contraction is compatible with the actual target differential, including the normal-removal endpoint terms. It is not a comparison of scalar values alone.

The genuine seven-state Q class still has the same independent long-normal coefficients. Its chosen full-target lift still has eighteen nonzero connecting terms, and each fully marked endpoint retains its three normal-removal terms. The scalar-kernel comparison acts as the identity on the surviving B coefficient; it supplies no nullhomotopy for those existing target boundaries and no new endpoint connector.

This computation does not cancel the nine mixed quadratic classes in the previous algebra-map Tor cokernel. Those classes compare the different coefficient algebras U and B. The present cancellation occurs between two rows of a module complex after derived base change to B. Likewise it does not remove the intrinsic conductor Tor of the fourteen-channel source: applying the derived unit B to that source leaves the source unchanged.

## 8. Consequence for the next physical identification

There are now three precisely separated outcomes for the same explicit coefficient map:

* The derived total conductor kernel comparison is an equivalence.
* The comparison is not an equivalence with its normalization/conductor row filtration fixed; the full Rees defect is computed above.
* The relative normalization quotient and the corresponding complete endpoint coefficient pattern retain E-infinity and E-infinity shifted once, respectively.

A proposed physical comparison must specify which operation and which filtration it realizes. The nonzero homology of either individual normalization term is not a no-go theorem for the total kernel. Conversely, equivalence of the total kernel does not identify the relative endpoint quotient or its generic/endpoint maps.

The actual support-changing operation of the native source remains to be identified. Nothing here fixes a scalar endpoint value in place of a comparison map, adds a geometric filling cell, or promotes a formal filtration parameter to a physical normal.

## 9. Reproduction and evidence

Run:

```sh
python check_marici_derived_normalization_diagram_20260907.py \
  --output marici_derived_normalization_diagram_certificate_20260907.json
```

The default run checks 59,808 exact assertions. It verifies the free-resolution and cone equations before and after base change, the lifted conductor-difference map, its B-linearity, the complete comparison-kernel contraction, all labelled dihedral actions, the Rees homotopy, the four-term endpoint rows and primitive readouts, and compatibility with the source's loaded coefficient differential.

The executable checks an auxiliary degree window with additional incoming degrees. It does not claim that truncating the infinite complex gives the same terminal homology. The parity formulas, annihilator identities, and explicit inverse difference maps prove the results in every degree over arbitrary retained polynomial coefficients.

The preceding occurrence-preserving bridge checker was independently rerun and passed 81,667 assertions. Its report is saved separately. No repository file was modified. Neither checker is a proof-assistant formalization.

### Sources

[S1] `src/ledger/20260817-627 The Conductor Difference Complex Is the Universal Mixed-Variance Kernel.md`, internal entry 433, fetched at the pinned commit. It supplies the kernel operation, polynomial conductor difference, and orientation convention. Returned blob: `263ff4cdc1b2114cbdb99680db2e999dff41ce30`.

[S2] `src/ledger/20260815-142 Unsplit Conductor-Road Endpoint Pullback and the Spatial Realization Blocker.md`, fetched at the same commit. It supplies the distinct quotient/road operation and all four differential degrees. Returned blob: `992943c89edb9d6ae39650bf5cbde4f0497233f8`.

[S3] The local artifact `marici_occurrence_preserving_bridge_20260907.md` and its rerun checker supply the fixed rings, occurrence-preserving quotient, permitted PC coefficient localizations, and prior scope. The new checker reconstructs the relevant loaded differential independently.

[M1] Stacks Project, *Derived tensor product*, tag `06XY`: K-flat resolutions and exact derived tensor.

[M2] Stacks Project, *Cones and termwise split sequences*, tag `014D`; *Derived categories*, tag `05RR`.

[M3] Stacks Project, *Spectral sequences: filtered complexes*, tag `012K`: row filtration, associated graded, and its first connecting differential.

[M4] Stacks Project, *Hom complexes*, tag `0A8H`: the distinction between a derived morphism and its induced homology map.

# Complete corrected Morse source and the conductor-nullhomotopy fibre

## Result

The complete corrected Morse source admits two explicitly constructed endpoint-connecting maps to the conductor-nullhomotopy fibre, with the two endpoint coefficient lines retained. Each map is nonzero in the relative derived category and becomes nullhomotopic after projection to the eleven-state coefficient source. These are coefficient comparisons, not an identification of the physical spatial correspondence.

The calculation has two distinct conclusions about the generic roof:

1. The endpoint-connecting maps send its pure long-facet flag to zero. On the complete positive corrected roof, their positive component has matching cubic endpoint terms which cancel.
2. A different, top-based map sends every pure long-facet flag to the unit road cycle, but sends the lower endpoint roof flag to the same cycle. It is explicitly nullhomotopic in the fibre and does not preserve the required separation of the generic and lower support grades.

Thus passing to the conductor fibre resolves the earlier boundary-versus-cycle error and supplies genuine relative comparison classes. It does not, by itself, construct a unit-normalized physical Q comparison.

## 1. Coefficients, sources, and grading

Let the conductor coefficient ring be

\[
C=\mathbb Z[X_{03},X_{14},X_{25},
 t_{02},t_{04},t_{13},t_{15},t_{24},t_{35},
 u_{03},u_{14},u_{25}].
\]

Retain the alternating normalization algebra

\[
B=C[X_{02},X_{04},X_{13},X_{15},X_{24},X_{35}]
 /(X_iX_j:i\in\{13,15,35\},\ j\in\{02,04,24\}),
\]

\[
I=(X_{02},X_{04},X_{13},X_{15},X_{24},X_{35}),
\qquad \epsilon:B\longrightarrow C=B/I.
\]

The short-normal graph is \(u_i=t_iX_i\). The three long normal variables remain independent of their occurrence variables. The checker works polynomially; the identities also extend through the prescribed flat localizations at monodromy units. No occurrence or Rees parameter is inverted.

The source is reconstructed from the exact rules in
`research/voevodsky/check_d03_pabs_morse_pullback.rs`, pinned at commit
`d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

Blow up the noncrossing face complex of the labelled hexagon at \(\{03,13\}\). A face containing that center is replaced by the three exceptional faces obtained by retaining neither center member, retaining 03, or retaining 13. Blowdown replaces the exceptional symbol E by both 03 and 13.

This gives 51 expanded faces and 581 strict flags. A flag \(F_0<\cdots<F_k\) carries every normal subset \(H\subseteq\operatorname{old}(F_0)\). This is the pulled-back-normal source used by the Morse construction; it is not the different 245-state native-normal source.

The pulled-back complex has 1,169 generators. Tensor it with the separate occurrence Koszul factor

\[
K_{\mathrm{occ}}(X_{35})=[Bh_{\mathrm{occ}}\xrightarrow{X_{35}}Bp].
\]

Denote the resulting source by \(S\). Its 2,338 generators have ranks

\[
(51,354,824,803,294,12)
\]

in homological degrees zero through five.

Deleting the first vertex of a flag multiplies by the occurrence monomial for the new initial face divided by that for the old initial face. All other flag deletions have unit coefficients and simplicial signs. Circle deletion multiplies by its actual normal \(u_i\), with the tensor sign. The added occurrence factor has its own differential and tensor sign. The checker verifies the complete square-zero equation both before and after the mixed-sheet quotient.

Occurrence degree of a source basis state is minus the occurrence vector of its initial old face, plus \(\epsilon_{35}\) for the auxiliary occurrence-circle state. A native normal-circle mark adds its separate normal degree. Give \(t_i\) occurrence degree \(-\epsilon_i\) and normal degree \(\epsilon_i\), so \(t_iX_i\) has only normal degree. These assignments make every differential entry homogeneous.

## 2. The conductor-nullhomotopy fibre

Use the eleven-state complex \(J_B\) with the integer matrices of the Entry-436 checker:

\[
d_3=\begin{pmatrix}0\\1\\1\\1\end{pmatrix},\qquad
 d_2=\begin{pmatrix}
1&0&0&0\\1&0&0&0\\0&1&0&-1\\0&-1&1&0\\0&0&-1&1
\end{pmatrix},\qquad
 d_1=(1,-1,-1,-1,-1).
\]

Let

\[
z=(1,0,1,0,0)^T,\qquad r=(0,0,1,1,1),
\qquad d_1z=0,\quad rd_2=0,\quad rz=1.
\]

The fibre \(F=\operatorname{fib}(\epsilon r:J_B\to C[1])\) is represented by

\[
F_3=B,\quad F_2=B^4,\quad F_1=B^5,\quad F_0=B\oplus C,
\]

\[
d_{F,1}(v)=(d_1v,\epsilon(rv)),
\]

with higher differentials \(d_2,d_3\). In particular,

\[
d_Fz=(0,1).
\]

The same vector z is a cycle in \(J_B\), but is not a cycle in F.

An explicit integral deformation retract takes F to
\([B\xrightarrow{\epsilon}C]\) in degrees one and zero. Its degree-one projection is r, its degree-zero projection extracts C, and its inclusion sends the degree-one basis to z. The contracting homotopy is the previously specified integer contraction of J, extended by zero on the C coordinate. Therefore

\[
F\simeq I[1].
\]

These are ordinary coefficient complexes. Calling this fibre a physical source would additionally require the spatial and support-filtration comparison.

## 3. Endpoint-connecting maps on every source generator

Let

\[
v_+=\{13,15,35\},\qquad v_-=\{02,04,24\}.
\]

Define \(\lambda_\sigma:S_0\to B\) to extract the unmarked, single-vertex source state \([v_\sigma]\otimes p\), and to vanish on every other source basis vector. Its conductor reduction

\[
\bar\lambda_\sigma=\epsilon\lambda_\sigma:S\to C
\]

is a chain map. Indeed, every differential term entering that endpoint has either a nonempty short-occurrence monomial, a short-normal factor \(t_iX_i\), or the auxiliary occurrence factor \(X_{35}\). Each lies in I. Hence

\[
\lambda_\sigma d_S(S_1)\subset I,\qquad
\epsilon\lambda_\sigma d_S=0.
\]

Define

\[
(m_\sigma)_1(v)=z\lambda_\sigma(d_Sv),
\qquad (m_\sigma)_n=0\quad(n\ne1).
\]

Then

\[
d_Fm_\sigma=m_\sigma d_S.
\]

The degree-one equation uses \(d_F(zc)=(0,\epsilon c)\), which vanishes because \(c\in I\). The degree-two equation uses \(d_S^2=0\). All remaining equations are zero by degree.

To preserve internal grading, retain the endpoint generator lines \(L_\sigma\), with bases of occurrence degree

\[
\deg L_\sigma=-\sum_{i\in v_\sigma}\epsilon_i.
\]

The homogeneous maps are \(m_\sigma:S\to F\otimes L_\sigma\), and the paired target is

\[
F_\partial=(F\otimes L_+)\oplus(F\otimes L_-).
\]

These lines retain the endpoint labels and their grading. They are not identified by a scalar basis change. The physical endpoint swap and a support-changing Gysin identification are not inferred from retaining these labels.

Each map has exactly eleven nonzero source columns:

- seven flags \([G,v_\sigma]\otimes p\), one for each proper subface \(G\subset v_\sigma\), with coefficient \(\prod_{i\in v_\sigma\setminus G}X_i\);
- three endpoint single-circle states, with coefficients \(u_i=t_iX_i\);
- the endpoint auxiliary occurrence-circle state, with coefficient \(X_{35}\).

Every column multiplies the fixed vector z. The sparse certificate lists all columns and their source labels. Every higher normal state remains in S, although its image is zero; its chain equation is still checked.

## 4. These are nonzero relative classes

Since S is bounded free over B, applying its Hom complex to

\[
0\to I\to B\xrightarrow{\epsilon}C\to0
\]

gives a short exact sequence of Hom complexes and a connecting homomorphism.

The complete degree-zero calculation is

\[
H^0\operatorname{Hom}_B(S,C)=C\bar\lambda_+\oplus C\bar\lambda_-.
\]

Here is the all-polynomial proof. A degree-zero cochain is a coefficient on each of the 51 face vertices. A face containing a long diagonal has a circle relation involving its independent, nonzero-divisor long normal; its coefficient is zero. The same applies to an exceptional face because its pulled-back old face contains 03. If a remaining face is not maximal, choose a maximal coface. The flag equation expresses its coefficient as the occurrence product times the maximal coefficient. This is zero on the conductor unless the original face already is a maximal all-short face. Those faces are exactly \(v_+,v_-\). Their coefficients are unconstrained. The auxiliary occurrence factor becomes zero on the conductor and adds no degree-zero constraint.

No degree-zero B-valued cocycle has a nonzero conductor restriction at either endpoint. For a positive endpoint, its three normal equations require its coefficient to be annihilated by all \(t_iX_i\) for \(i\in v_+\). In the split normalization algebra, that coefficient lies in the opposite branch ideal, and therefore has zero conductor value. The negative endpoint is analogous. Including the separate \(X_{35}\) occurrence relation can strengthen these annihilator conditions but cannot give a nonzero conductor constant.

Thus the image of

\[
H^0\operatorname{Hom}_B(S,B)\to H^0\operatorname{Hom}_B(S,C)
\]

is zero. The connecting homomorphism embeds C^2 into \(H^1\operatorname{Hom}_B(S,I)\), equivalently into the indicated classes of maps to the shifted fibre. With the cohomological Hom convention \(\delta\lambda=-\lambda d_S\), our displayed positive map represents the negative of the connecting image of \(\bar\lambda_\sigma\). Its sign is fixed by the displayed formula; no positive residue is inferred.

Each class has exact annihilator I. For every \(c\in I\),

\[
H_c(v)=c\lambda_\sigma(v)z\quad(v\in S_0)
\]

is an actual F-valued nullhomotopy of \(c m_\sigma\). Its degree-zero boundary contribution vanishes because \(\epsilon(c)=0\). Conversely the injectivity of the connecting map shows that no nonzero coefficient of C annihilates either class.

This identifies an injected C^2 submodule, not the complete mapping-cohomology group. After restoring internal degrees and endpoint lines, the two displayed classes live in their respective labelled summands.

Projection to \(J_B\) makes \(m_\sigma\) nullhomotopic by \(z\lambda_\sigma\). The same cochain is not an F-valued primitive for \(m_\sigma\): its degree-zero boundary has the additional conductor component \(\bar\lambda_\sigma\). This is precisely the retained relative datum.

## 5. Derived conductor restriction and six normal directions

The lowest homology of the derived conductor restriction of F is

\[
H_1(C\otimes_B^LF)=I/I^2\cong C^6.
\]

The six endpoint single-circle states are cycles after conductor restriction. Their coefficient-extraction functionals annihilate every boundary of the full specialized S, so none is an artifact of omitting higher source states.

Their images on lowest derived homology are

\[
[m_\sigma(\ell_i)]
=t_i[X_i]z_\sigma,\qquad i\in v_\sigma.
\]

These are six independent directions over C, but the native-circle images carry their Rees factors. When all six \(t_i\) are specialized to zero, these six images vanish. There is no justification for replacing the factors by units.

The auxiliary occurrence-circle state at either endpoint has instead the image \([X_{35}]z_\sigma\). It belongs to the separate occurrence Koszul factor and must not be called the monodromy circle.

On the incoming one-occurrence flags, the first-symbol cochain sends the flag missing i to \([X_i]z_\sigma\). Those flag statements are cochain evaluations; these flags are not asserted to be cycles in the complete specialized source.

## 6. Evaluation on the actual corrected Morse chain

Retain the exact source identity

\[
dH_M=q_J-X_{35}\widetilde\xi,
\qquad
 d\widetilde\xi=X_{03}X_{02}[c]-X_{13}X_{15}[v_+],
\]

where \(c=\{03,02,35\}\). Tensoring with the occurrence factor gives

\[
\widehat h_M=H_M\otimes p-\widetilde\xi\otimes h_{\mathrm{occ}},
\]

\[
d\widehat h_M=\widehat q_J
=q_J\otimes p-(d\widetilde\xi)\otimes h_{\mathrm{occ}}.
\]

The endpoint map has

\[
m_+(\widetilde\xi\otimes p)=-X_{13}X_{15}z_+,
\]

\[
m_+(q_J\otimes p)
=m_+((d\widetilde\xi)\otimes h_{\mathrm{occ}})
=-X_{13}X_{15}X_{35}z_+.
\]

Therefore

\[
m_+(\widehat q_J)=0,\qquad m_+(\widehat h_M)=0.
\]

The negative endpoint component vanishes on all these positive-gallery chains. Its full map on the complete source remains nonzero, as established above.

No source boundary has been mapped to the nonzero homology generator of \(J_B\). The complete corrected boundary has not been deleted; its nonzero source vector is exported and its vanishing image is verified.

The nonzero raw-roof coefficient has conductor order exactly three. Its initial symbol is

\[
-[X_{13}X_{15}X_{35}]z_+
\in(I^3/I^4)\otimes L_+.
\]

It is nonzero in the positive polynomial branch. This is a product in the associated-graded algebra, not an unproved identification with an exterior Gysin orientation. A first-order conductor readout necessarily misses this particular raw-roof entry.

The pure long-facet flag \([\varnothing,\{03\}]\) maps to zero under both endpoint maps. The cubic contribution above comes from the retained endpoint roof correction, not from a newly constructed generic Q image.

## 7. A top-based control and its support failure

Let \(\lambda_\top\) extract the unmarked empty-face vertex. Define a homotopy

\[
h_\top(\varnothing)=-z
\]

and zero on other source states. Its boundary

\[
m_\top=d_Fh_\top+h_\top d_S
\]

is an explicit chain map \(S\to F\). Its 52 nonzero columns are all exported. It has

\[
m_\top[\varnothing,\{03\}]=z,
\qquad
m_\top[\varnothing,v_+]=z,
\qquad
m_\top(\varnothing)=(0,-1).
\]

The analogous unit holds for each of the other long-facet flags. Its extra auxiliary occurrence-circle column is retained as well.

This is an ordinary nullhomotopic map of the complete complexes. More importantly, it cannot serve as the required support-filtered comparison if the first flag is to have a nonzero Q-grade while the second is a lower endpoint correction: it sends both to the same vector. The full three-term q_J has image zero because its generic and endpoint parts cancel.

The endpoint maps and this top-based control must not be added while silently forgetting their different internal line degrees. They are separately defined, not a claimed affine family of physically graded maps.

## 8. General unit-road obstruction in this fibre model

The row r, composed with projection from F to J_B, is a chain map \(F\to B[1]\). For any B-linear degree-zero chain map \(m:S\to F\), the retained Morse equation therefore implies

\[
r m(q_J\otimes p)=X_{35}\,r m(\widetilde\xi\otimes p).
\]

In the unlocalized ring this cannot equal one. Reduction modulo \((X_{35})\) sends the right side to zero and preserves the unit on the left.

This statement concerns the total, ordinary road readout. It does not equate that readout with a physical Q-associated-grade map; constructing that filtered comparison is exactly the unresolved issue. It rules out demanding a unit total readout from the present fibre while retaining all of the displayed source differential.

## 9. Verification and physical scope

The standalone standard-library checker verifies 78,365 exact identities. It reconstructs all source states and differentials, verifies the source graph quotient and the fibre contraction, checks both endpoint maps on every column, verifies every conductor-ideal annihilating homotopy, retains all endpoint normal states, verifies both corrected Morse chains, and supplies the top-based negative control.

The matrix hash is

`bcc59e60abaf6ebb80e3f55bcc60194ecfa1e68c2cd860bc382c2ba90cdc2d74`.

The sparse certificate includes the complete 2,338-state basis, 7,413 nonzero source differential entries after normalization pullback, all endpoint and top-map columns, the first-symbol rows, and separate scope flags. The all-polynomial nonvanishing and annihilator statements use the proofs above, not a finite coefficient search.

Constructed: full relative coefficient maps, their nonzero classes, their actual endpoint normal values, and their exact Morse evaluations.

Not constructed: the physical support-changing correspondence, its endpoint-swap identification, a nonzero generic Q comparison compatible with all lower support terms, or the physical conductor–Morse class.

The next physical calculation must operate on the complete filtered source and distinguish the pure long-facet flag from the endpoint correction. Neither a unit readout on one isolated flag nor the existence of the nonzero relative endpoint classes proves that distinction.

## Sources

Marici commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: pulled-back coefficient normal states, weighted flag differential, separate occurrence Koszul correction.
- `research/voevodsky/check_d03_normalized_blowdown_counit.py`: seven Morse triangles, six gallery flags, three-term generic roof.
- `research/voevodsky/check_physical_derived_pullback_after_transform.py`: integer J matrices and the fixed road-readout vector. The present calculation uses these matrices, not the script's signature-based identification with a physical transform.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: alternating branch algebra and conductor quotient.
- `src/ledger/20260817-397 The Descended qJ Roof Is the Canonical D03 Yoneda Generator.md`: the stated generic flag and lower roof labels only. The claim there identifying the nested-filtration splice with a nonzero Yoneda class is not used.

Stacks Project: Tag 0A8H (Hom complexes), Tag 014D (cones and termwise split sequences), Tag 0117 (connecting homomorphism), Tag 0621 (Koszul construction and signs).

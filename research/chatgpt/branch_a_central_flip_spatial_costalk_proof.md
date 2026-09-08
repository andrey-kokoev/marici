# Branch A: central-flip spatial locality and explicit conductor costalk kernels

Date: 2026-09-07.

## Result and scope

This calculation applies the actual marked support to the previously computed conductor costalk. It constructs explicit local coefficient maps from the resolved conductor and their physical-reflection comparison homotopy. It does not construct the complete physical support-changing six-functor correspondence or identify the physical conductor–Morse class.

In occurrence-map degree zero and regulator-normal grade three:

* The marked two-edge D03 gallery has a rank-three local costalk, injected into the full rank-thirty-four costalk. Its entire conductor-unit image is zero in full target homology.
* The whole closed D03 facet has zero local costalk in this component. Adding that square to the marked gallery leaves the same rank-three zero-primary image.
* The opposite edge of the containing 35 pentagon has a rank-three local costalk and a primitive rank-one primary image. An explicit twelve-term resolved map realizes that primary.
* That map includes both the D03 and D25 endpoints of the opposite edge. Deleting its D25 component produces a nonzero chain defect.
* In the previous symmetry convention s(v)=2-v, the ten invariant zero-primary directions have a saturated rank-three locality sublattice. The physical D03 reflection f3(v)=3-v is a different operation: it exchanges the occurrence-35 and occurrence-04 complexes. Its local comparison is constructed separately, with an explicit homotopy and zero square defect.

The no-go statements apply to the specified source A[2], regulator degree, and closed-support coefficient subcomplexes. A different extraordinary source, determinant twist, shift, or relative-support target requires its own comparison. In particular, these results do not identify ordinary costalk primary evaluation with an independently defined physical residue.

## 1. Retained coefficient model and actual supports

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/(I_-I_+),
\]

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad
I=I_-\oplus I_+,\qquad A=R/I.
\]

These are the two normalization sheets and their conductor. The full target C_beta has 430 indexed states [F,H,e], where F is a noncrossing face, H is a subset of its native normal marks, and e records the separate occurrence-35 partner. Its homological degree is

\[
3-|F|+|H|+e.
\]

The radial coefficient is X_a, the native-circle coefficient is beta X_a, and the occurrence differential is X_35. The original scalar occurrences are not replaced by additional native factors.

Let V contain all 32 states over the two physical vertices {13,15,35} and {02,04,24}. Let B_short contain the 416 states whose faces contain a short diagonal. Q=C_beta/B_short is the actual fourteen-state quotient. Define

\[
K_n=\{c\in C_{\beta,n}:qc=0,\ vc=0,\ vdc=0\}.
\]

The last condition retains incoming endpoint terms. It is needed because projection onto the entire endpoint subcomplex is not itself a chain map.

For a genuine closed union S of faces, let C_beta(S) be its full native/occurrence-loaded subcomplex, and set

\[
K(S)=K\cap C_\beta(S).
\]

The checker verifies differential closure of every support before calculating its Hom complex. No mixed flags or normal states are omitted by an unverified projection.

The geometrically prescribed gallery is the union of the two closed edges {13,35} and {03,35}. Its vertices are

\[
v_+=\{13,15,35\},\quad
b=\{03,13,35\},\quad
c=\{02,03,35\}.
\]

Its support has 64 states after the separate occurrence correction. This is the actual gallery in ledger Entry 106. Entry 96 independently identifies c with the marked intersection W03 of the two coordinate edges {03,02} and {03,35} in the D03 factorization square.

## 2. Compute local costalks and their actual global images

The source is the free resolution P_A[2]. Its relevant ranks are 1,6,24,92 in homological degrees 2,3,4,5. Its unit p and first generators satisfy

\[
d e_a=X_a p.
\]

The next maps retain six within-sheet Koszul relations, eighteen ordered mixed-sheet relations, and all ninety-two next compatibility equations. These are reconstructed in the checker. Source resolution terms above degree five cannot contribute to degree-zero maps, their homotopies, or their chain equations because the target ends in degree four.

For a source generator with occurrence weight w, a legal entry into [F,H,e] has exponent vector

\[
w+\sum_{a\in F}\epsilon_a-\sum_{a\in H}\epsilon_a-e\epsilon_{35},
\]

and beta exponent 3-|H|. Negative exponents and monomials involving both sheets are excluded. The resulting integer systems are complete homogeneous components, not coefficient-degree cutoffs.

For each S, compute

\[
\mathcal H(S)=H_0\operatorname{Hom}_R(P_A[2],K(S))
\]

and the induced map into the full costalk. The homotopy quotient is included; source-relation components are not discarded. The complete results are:

| Closed support | States | Local costalk rank | Rank in global costalk | Global unit-image rank |
|---|---:|---:|---:|---:|
| Central-flip edge {13,35} | 40 | 3 | 3 | 0 |
| Marked two-edge D03 gallery | 64 | 3 | 3 | 0 |
| Gallery plus entire D03 square | 124 | 3 | 3 | 0 |
| Gallery and its old s-reflection | 112 | 6 | 6 | 0 |
| Entire D03 facet | 100 | 0 | 0 | 0 |
| Marked corner W03 | 16 | 0 | 0 | 0 |
| Opposite edge {02,35} | 40 | 3 | 3 | 1 |
| Entire 35 pentagon | 124 | 12 | 12 | 1 |
| Three-facet carrier F35 union F03 union F04 | 268 | 20 | 20 | 2 |

All nonzero invariant factors of the local-to-global and unit-image matrices are one. Thus these are saturated integral images. The certificate contains the entire local closed-map and boundary systems, local quotient bases, global coordinate maps, and reductions.

The geometric inference is limited but exact: a comparison represented by a map A[2] -> K(gallery) cannot have any nonzero primary class of the present global costalk. A log-expanded carrier whose comparison still factors through this same local target cannot change that conclusion. The calculation does not assert that every possible extraordinary correspondence has this source, shift, or coefficient realization.

The local systems at grade g and g+1 are identical up to multiplication by beta for g >= 3, since every state has at most three native marks. This is checked on the entire pentagon Hom differential in degrees -1,0,1,2. Local classes inject into the beta-torsion-free global costalk. The locality conclusion therefore persists after inverting beta and applying the previously established unit-normal frame changes. It is not an extension of a geometric purity theorem to beta=0.

## 3. Construct a nonzero local primary from the actual opposite edge

Let

\[
E=\{02,35\},\qquad
W_{03}=\{02,03,35\},\qquad
W_{25}=\{02,25,35\}.
\]

These are the edge opposite v+ in the containing 35 pentagon and its two actual endpoints. Put

\[
L_E=\beta[E,E,0]-[W_{03},W_{03},0]-[W_{25},W_{25},0].
\]

The coefficients are forced within these three marked states by cancelling the two long-normal terms in the complete differential. Choosing +beta on the ordered edge fixes the orientation; the two vertex coefficients are then -1. No value of a target residue is used to choose them.

The full boundary splits into its two normalization-sheet parts,

\[
dL_E=U_++U_-.
\]

Its positive part is

\[
\begin{aligned}
U_+={}&\beta^2X_{35}[\{02,35\},\{02\},0]\\
&-\beta X_{35}[\{02,03,35\},\{02,03\},0]\\
&-\beta X_{35}[\{02,25,35\},\{02,25\},0].
\end{aligned}
\]

The negative part is

\[
\begin{aligned}
U_-={}&-\beta^2X_{02}[\{02,35\},\{35\},0]\\
&-\beta X_{02}[\{02,03,35\},\{03,35\},0]\\
&-\beta X_{02}[\{02,25,35\},\{25,35\},0].
\end{aligned}
\]

Both parts are closed. This follows from the full signed differential and the cross-sheet product relations; it is also checked directly.

Define the resolved supported map

\[
\mathcal G_E^+(p)=U_+,\qquad
\mathcal G_E^+(e_a)=
\begin{cases}
X_aL_E,&a\in\{13,15,35\},\\
0,&a\in\{02,04,24\},
\end{cases}
\]

with zero values on the twenty-four relation generators. All ninety-two next equations hold. For a positive a, X_a U_-=0, so d(X_a L_E)=X_a U_+. For a negative a, X_a U_+=0. Same-sheet source relations cancel by commutativity, and mixed-sheet relations vanish.

The complete map has twelve polynomial terms. Every value has zero endpoint and Q components, and no incoming endpoint boundary. Its primary class is primitive and nonzero in the global target H_2. In the exported global costalk basis, the map is the sixth basis vector; its primary coordinate vector is (0,0,0,0,-1).

Repeating the same differential-derived construction on edges {04,13} and {15,24} gives three primitive primary images spanning the entire rank-three global counit image. Their coordinate matrix has three unit invariant factors. This identifies which actual local edges carry the three primary classes; it does not yet identify their residues with physical scalar units.

## 4. D03-only truncation has an explicit defect

Delete every target term containing 25 from the map above, retaining the edge and the W03 terms. Call this graded map G_cut. On the source unit,

\[
\delta\mathcal G_{\mathrm{cut}}(p)
=-\beta^2X_{25}X_{35}
[\{02,25,35\},\{02\},0]\ne0.
\]

The coefficient contains one long occurrence and one positive short occurrence, so it survives in the normalization ring. The defect is not an integer multiple introduced by normalization; its coefficient is -1.

The entire Hom differential of G_cut is exported, not only this detecting column. Its relation components also remain available for checking the failed truncation.

The all-D03 local costalk calculation in Section 2 rules out fixing this by another representative of the same current type supported solely on that facet. A relative endpoint selection or Gysin operation would have to introduce and type the additional comparison object explicitly. Deleting the companion channel is not such an operation.

## 5. Construct the physical reflection comparison on the correct target pair

The earlier rank-ten invariant kernel used the parity-preserving reflection

\[
s(v)=2-v\pmod6.
\]

The source's actual D03 physical reflection is

\[
f_3(v)=3-v\pmod6.
\]

It fixes D03, exchanges the two normalization sheets, and sends occurrence 35 to occurrence 04. It is a map between the correctly labelled corrected complexes C_beta,35 and C_beta,04, not an automorphism of the fixed occurrence-35 complex.

The checker includes all 430 chain equations for this map, all native-mark orientation signs, the occurrence differential, and the involution square. Source generators and relation bases are permuted with their actual exterior signs; the conductor unit is fixed in this coefficient convention. No additional Thom or polarity twist is silently inserted.

The edge E is sent to

\[
E'=\{04,13\},
\]

whose endpoints are {03,04,13} and {04,13,14}. The normal-mark orientation gives

\[
f_3L_E=-L_{E'}.
\]

Define the negative-sheet representative by

\[
\mathcal G_E^-(p)=-U_-,\qquad
\mathcal G_E^-(e_a)=
\begin{cases}
-X_aL_E,&a\in\{02,04,24\},\\
0,&a\in\{13,15,35\}.
\end{cases}
\]

Then

\[
f_3\mathcal G_E^+=\mathcal G_{E'}^-.
\]

The degree-one cochain H_E, defined by H_E(p)=L_E and zero on all other source generators, satisfies

\[
\delta H_E=\mathcal G_E^+-\mathcal G_E^-.
\]

Consequently the positive-sheet choices obey the physical-reflection comparison

\[
\mathcal G_{E'}^+-f_3\mathcal G_E^+=\delta H_{E'}.
\]

The square coherence is literal:

\[
f_3H_{E'}+H_E=0.
\]

Thus the reflected local coefficient kernels agree through an actual support-preserving comparison homotopy. They retain the D25 and D14 companion terms. This computation does not identify the coefficient source with the full geometrically framed reciprocal/Gysin source.

## 6. Read locality in the previous rank-ten invariant lattice

For the earlier s=2-v convention, construct the invariant costalk basis and take the saturated kernel of the counit. The certificate exports its 34-by-10 basis matrix.

The union of the marked gallery and its s-reflection has an invariant rank-three image. In the exported ten-coordinate basis its inclusion is

\[
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0\\
0&0&0\\
1&0&0\\
0&0&0\\
0&0&0\\
1&1&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

Its image is the direct summand spanned by the first, fifth, and eighth coordinate directions. The whole 35 pentagon gives exactly the same invariant zero-primary sublattice, with a different unimodular basis. Its nonzero local primary is odd under s in this source convention.

This reduces the old zero-primary locality problem from ten to three coordinates. It does not produce a normalized absolute kernel: all three have zero primary. Nor should the s-invariant counts be relabelled as a fixed-D03 f3 result; the correct physical reflection calculation is Section 5.

## 7. Consequence for the spatial construction

The marked gallery and even the gallery plus the whole D03 square cannot realize a nonzero primary of the present A[2] conductor-costalk problem. This is a complete derived-map calculation in those supports, including source relations and admissible target homotopies.

A concrete nonzero primary is realized by the opposite edge selected by the containing pentagon. Its explicit two-channel closure, its twelve-term supported map, and its physical-reflection comparison are now known. The D03 corner W03 is geometrically marked, but the current absolute cochain does not admit a D03-only truncation.

The remaining operation must be a source-defined relative/Gysin comparison at that marked corner, retaining the opposite-edge boundary data and its physical-reflection partner. Its source degree, reciprocal coefficient variance, and determinant lines must be specified before equating it with this coefficient map or extracting a physical residue. No coordinate of the physical Delta_J is assigned by this calculation.

## Reproduction and references

Run:

```sh
python branch_a_central_flip_spatial_costalk_checker.py --output branch_a_central_flip_spatial_costalk_certificate.json
```

The checker is standalone and reads no other files. It reconstructs the target differential and the relevant free source resolution. Its certificate includes complete local linear systems, homotopy quotient reductions, inclusions into the global basis, local primary matrices, the explicit edge maps, the channel-truncation defect, and the physical reflection homotopy.

Primary project inputs, pinned at commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61:

* `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`
* `src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md`
* `src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md`
* `src/ledger/20260814-140 Physical-Reflection Naturality of the D03 Edge Purity.md`
* `research/voevodsky/check_absolute_unlocalized_support_pc.rs`

Hom-complex signs and the cochain homotopy quotient: Stacks Project, Tag 0A8H. Projective resolutions computing derived maps: Tag 064B. The affine closed-immersion right adjoint and counit: Tag 0A74. These standard facts justify the coefficient mapping interpretation; they do not supply the missing physical spatial correspondence.

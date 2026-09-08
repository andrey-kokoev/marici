# Construction of the full marked logarithmic matrix

## 1. Exact scope

The requested physical map has a normalization-conductor source, geometric
support, relative dualizing shifts, and prescribed endpoint and Q homotopies.
The checked-in integration and signature scripts do not specify its full
source-to-target generator map.

Here we construct an independent, complete map on the **native logarithmic
blowdown source**. This fills the previously absent normal-marked right-leg
matrix, rather than relabelling the target's finite-to-Čech diagonal as the
physical connector. It retains the exceptional monodromy and every native
normal state. The remaining normalization/Gysin left leg is explicitly not
claimed.

## 2. Source and coefficient ring

Let D be the nine diagonals of the labelled hexagon. Put

\[
R=\mathbb Z[X_d,u_d:d\in D],\qquad q_d=1+u_d.
\]

All formulas hold after localizing at the monodromy units q_d. No u_d or X_d
is inverted in the source construction.

Set a=03 and b=13. Stellar-subdivide the edge {a,b} of the noncrossing
simplicial complex, introducing the exceptional ray E. Equivalently, remove
all faces containing {a,b} and insert

\[
\{E\}*\partial\{a,b\}*\operatorname{link}\{a,b\}.
\]

The resulting face counts are (1,10,24,16). Its native marked cells are
[\widetilde F,\widetilde H], with \widetilde H a subset of \widetilde F;
there are 245. Both normalization endpoint labels are unchanged by this
subdivision.

Define the old-face map by

\[
\pi\widetilde F=
\begin{cases}
\widetilde F,&E\notin\widetilde F,\\
(\widetilde F\setminus\{E\})\cup\{a,b\},&E\in\widetilde F.
\end{cases}
\]

The source occurrence label is m(\widetilde F)=\prod_{d\in\pi\widetilde F}X_d,
exactly the old-face loading used by the repository's normalized blowdown.
For a native radial incidence \widetilde F\subset\widetilde G, use the
polynomial quotient m(\widetilde G)/m(\widetilde F), not a separately chosen
coefficient. The exceptional normal is

\[
u_E=q_aq_b-1=u_a+u_b+u_au_b.
\]

The source differential adds a ray with the exterior incidence sign and the
occurrence quotient, or removes a mark with coefficient u_d, including u_E.
A normal removal has sign (-1)^{3-|\widetilde F|+\operatorname{pos}(d)}.
The source differential squares to zero on all 245 generators.

This is a specified native-normal coefficient model of the source geometry.
Its identification with a complete algebraic six-functor source is not an
assumption of the calculation.

## 3. Target

The finite target has 215 cells [F,H], H subset F, in homological degree
3-|F|+|H|. Its radial coefficients are X_d and its normal coefficients u_d.
The Čech target has coefficient module

\[
R[u_d^{-1}:d\in F\setminus H]
\]

on [F,H], radial coefficients X_d/u_d, and normal coefficients one.
The finite-to-Čech map is

\[
\Lambda[F,H]=\left(\prod_{d\in F\setminus H}u_d^{-1}\right)[F,H].
\]

Both endpoint packets remain until taking the final quotient. They have
sixteen generators in total. The quotient E has 199 generators, not 215.

## 4. Closed formula for every matrix entry

Order original rays lexicographically and place E last. Define the normal
exterior map L by

\[
L(e_d)=e_d\quad(d\ne E),\qquad L(e_E)=e_a+q_a e_b.
\]

Its normal chain equation is

\[
dL(e_E)=u_a+q_a u_b=u_E.
\]

Extend by exterior products with their ordinary signs. There is no normal
truncation. The opposite loop word gives q_b e_a+e_b; the difference is

\[
(e_a+q_a e_b)-(q_b e_a+e_b)=d(e_a\wedge e_b).
\]

This is a normal-chain homotopy, not a claim that both word representatives
are equal.

For E not in \widetilde F, put epsilon(\widetilde F)=1. For E in
\widetilde F and neither a nor b in \widetilde F, put epsilon=0. Otherwise
exactly one of a,b belongs to \widetilde F. Replace E in its ordered list by
the missing member of {a,b}, and let epsilon be the sign of sorting the
resulting old-face list.

The full finite matrix is

\[
K^{\rm fin}_{[F,H],[\widetilde F,\widetilde H]}
=\varepsilon(\widetilde F)
\,\mathbf1_{F=\pi\widetilde F}
\,[e_H]\bigl(\bigwedge L(e_{\widetilde H})\bigr).
\]

Here [e_H] denotes coefficient extraction in the exterior algebra. The full
Čech matrix is

\[
K^{\check C}_{[F,H],[\widetilde F,\widetilde H]}
=\left(\prod_{d\in F\setminus H}u_d^{-1}\right)
K^{\rm fin}_{[F,H],[\widetilde F,\widetilde H]}.
\]

Thus all entries are specified without solving for a desired output residue.
Ten entire source columns collapse. All 215 target rows occur. The Čech
matrix has 245 nonzero polynomial entries, comprising 260 monomials.

The full degree-block shapes, written target rows by source columns, are

\[
14\times16,\quad63\times72,\quad93\times106,\quad45\times51.
\]

After removing the source and target endpoint packets they become

\[
12\times14,\quad57\times66,\quad87\times100,\quad43\times49.
\]

## 5. Chain-level derivation and verification

The matrix was obtained independently from the loaded barycentric source,
not only guessed from the formula. The expanded face poset has 581 strict
flags. Loading the initial face by all native normal subsets gives 1,111
states in degrees (51,300,504,256).

On these flags, take the repository's normalized blowdown: replace E by
{a,b}, and set a flag to zero when its image is degenerate. Apply L to its
native normal states. First-vertex occurrence coefficients agree because
both are defined using the old-face label. This is a chain map on the full
normal-loaded bar complex, not merely on the three displayed Morse chains.

We constructed an integral, face-supported cellular approximation on every
old face. Its integer fillings are independently checked. Multiplying a
filling cell G by m(G)/m(F_0) introduces no occurrence inverse. The normal
operators commute with this comparison because every filling lies in a
coface of F_0, where all initial marks remain permitted.

Composing with the native cellular subdivision gives the closed formula in
Section 4. Although the intermediate approximation chooses integer
fillings, the resulting cellular matrix equals the explicit face-sign and
exterior-map formula on every source generator.

The verifier checks

\[
d_{\rm fin}K^{\rm fin}=K^{\rm fin}d_{\log},\qquad
 d_{\check C}K^{\check C}=K^{\check C}d_{\log},\qquad
 K^{\check C}=\Lambda K^{\rm fin}.
\]

It also checks every permitted target localization and all source and target
differential squares. These are exact polynomial identities, not tests at
selected coefficient values.

## 6. Endpoint and Q data

On all sixteen native endpoint states, K^fin is the unchanged endpoint
identification. On the seven native Q states it is the identity. After Čech
realization these become the corresponding finite-to-Čech maps, with the
specified lower localizations.

The endpoint connecting maps are extracted from the actual source and
target differentials. Their squares commute strictly for the native
cellular matrix. There is no target-endpoint component on a source
nonendpoint cell; the off-diagonal endpoint-comparison block is zero.
All connecting matrices are included in the JSON.

This is not the normalization-sheet swap matrix. The source here is the
native logarithmic carrier, not the pair of normalization sheets. Equating
these two endpoint statements would assume the missing left-leg map.

## 7. The five incoming rows are now numerical polynomials

The row order is

1. [{13},{13}];
2. [{04,13},{13}];
3. [{04,13},{04,13}];
4. [{13,35},{13}];
5. [{13,35},{13,35}].

Each row has exactly one nonzero native-source entry, on the identically
labelled source cell. Their coefficients are

\[
1,\quad u_{04}^{-1},\quad1,\quad u_{35}^{-1},\quad1.
\]

All other entries of those five rows are zero. In particular,

\[
\mathcal R_{03,13}K^{\check C}
[\{13,35\},\{13\}]
=
\frac{X_{03}}{u_{03}^2u_{13}u_{35}}
[\{03,13,35\},\varnothing].
\]

The complete radial composite has five nonzero source columns, and the
mixed T-composite has ten. The global identity

\[
d(HK)+(HK)d=TK+\mathcal RK
\]

is checked on every native source column. This evaluates the operation on
this fully constructed native carrier; it does not assign it a value on
the as-yet unspecified normalization-derived source map.

## 8. The exceptional kernel is not acyclic

The finite matrix is degreewise split surjective. A graded section is
explicit: lift unchanged faces identically; lift a face containing {a,b}
to the chart retaining b and use

\[
e_a\longmapsto e_E-q_a e_b,\qquad e_b\longmapsto e_b.
\]

All entries are polynomial. This gives a free kernel of ranks (2,9,13,6).
Ten unit cancellations give an explicit integral deformation retraction to
ranks (0,2,5,3).

Put

\[
P_{\rm link}=\left[
R^3\xrightarrow{\begin{pmatrix}
X_{04}&u_{04}&0\\X_{35}&0&u_{35}
\end{pmatrix}}R^2\right]
\]

in homological degrees one and zero. The remaining kernel is exactly

\[
\ker K^{\rm fin}\simeq K_R(u_E)\otimes_R P_{\rm link}[1].
\]

The factorization includes the indicated differential signs; its basis
identification and all maps are exported.

The kernel of d in P_link is free on

\[
(u_{04}u_{35},\ -X_{04}u_{35},\ -X_{35}u_{04}).
\]

Indeed the first equation forces u_04 to divide the first coordinate; the
second forces u_35 to divide it. The other two coordinates are then forced.
These divisibility arguments are unchanged by monodromy-unit localization.

Multiplication by u_E is injective on both homology groups of P_link. The
coefficients defining P_link are independent of u_a,u_b, and u_E has a
unit leading coefficient in those polynomial variables. Consequently

\[
H_2(\ker K^{\rm fin})\cong R/(u_E),
\]

\[
H_1(\ker K^{\rm fin})\cong
\operatorname{coker}(d_{P_{\rm link}})\otimes_R R/(u_E),
\qquad H_j(\ker K^{\rm fin})=0\ (j\ne1,2).
\]

The degree-two generator has an explicit primitive after multiplication
by u_E. Both are given in the reduced kernel and the original 245-state
source. This is monodromy-parameter torsion, not integer-prime torsion.

A separate detector specializes u_a=u_b=0, u_04=u_35=1 and all occurrence
coordinates to zero over Z[1/2]. It annihilates every degree-three source
boundary and reads the full exceptional cycle as one. This respects the
monodromy-unit localizations. It confirms that ordinary blowdown cannot be
promoted to a quasi-isomorphism on the unlocalized resonance family.

## 9. The actual remaining physical construction

The requested normalization-derived map would need an independently
constructed morphism from the normalization-conductor source into this
native logarithmic comparison, together with its relative trace and
conormal degree data. That morphism is not supplied by the matrix above.

The source's explicit unmarked q_J consists of barycentric one-simplices.
The native loaded-chain comparison maps it to homological degree one,
where the cellular Q quotient is zero. The verification reconstructs the
seven-triangle source Morse identity and its full target image and confirms
this zero Q projection. This is a grading obstruction to using the ordinary
bar pushforward as the physical q_J attachment. It does not apply to a
separately constructed extraordinary/Gysin comparison with the correct
source and shift.

In particular, the following claims are not made:

- that native log blowdown alone is the normalization-sheet transform;
- that an endpoint swap or residue signature determines the missing map;
- that the exceptional kernel can be discarded while preserving the required
  relative Thom trace;
- that the source's physical Q-homotopy, higher symmetries, or numerical
  amplitude has been computed.

The concrete advance is a full generator matrix, including native
exceptional monodromy and all incoming rows, plus an exact exceptional
kernel on which the missing relative trace must now be evaluated.

## 10. Source provenance

Pinned repository inputs:

- `research/voevodsky/check_d03_normalized_blowdown_counit.py`: old-face map,
  first-vertex occurrence loading, and seven-triangle Morse identity.
- `research/voevodsky/check_ringed_alexandrov_pc_target.py`: all finite target
  faces, loaded states, differentials, and legal localizations.
- `src/ledger/20260814-111 One-Sheet Rees-Cartier Symbol and the Missing Marked Conductor Lattice.md`:
  exceptional relation q_E=q_03 q_1 and separation from the x_3 conormal.
- `research/voevodsky/check_global_mixed_variance_transform.py` and
  `check_cellular_log_kernel_framed_identification.py`: signature checks;
  neither defines the remaining normalization-to-marked-carrier matrix.

The homological algebra uses the ordinary Koszul construction and the Hom
complex sign rule, as in Stacks Project tags 0621 and 0A8H. The chain maps,
integer fillings, kernel reduction, and nonzero detector in this package are
new explicit calculations; they are not attributed to those general lemmas.

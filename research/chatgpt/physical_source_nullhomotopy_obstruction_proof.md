# Source admissibility of the proposed conductor–Morse primitive

## Result and correction

The expression `P = -k_nu h_Morse` cannot be tested for framed admissibility on the Entry-436 source using the preceding comparison `a`. Its necessary equation `delta h_Morse = a` has no solution, even without support or filtration restrictions. The map `a` takes a nonzero homology generator to the conductor unit.

This is a correction to the preceding source identification, not a proof that every physical secondary invariant vanishes. The historical corrected Morse source and the Entry-436 derived-pullback source have different specified cycles: the first specified cycle is a boundary, while the second is not. No chain map can identify them as previously proposed.

The calculation also constructs:

- an integral deformation retract of the complete eleven-state Entry-436 complex;
- two explicit chain representatives of the derived normalization comparison and their homotopy;
- the correction required when composing that homotopy with the nonclosed cochain `k_nu`;
- the universal source fibre on which the comparison does have a nullhomotopy;
- its conductor ideal and the first two homology modules of its derived conductor restriction.

The new source fibre is an algebraic construction. No identification of it with the physical Morse source is assumed.

## 1. Source and coefficient conventions

Write `J_Z` for the eleven-state complex in the repository's Entry-436 checker. This notation deliberately distinguishes it from the source called `J` in the original secondary-class specification.

The homological differential lowers degree. The three matrices are

\[
d_3=\begin{pmatrix}0\\1\\1\\1\end{pmatrix},\qquad
 d_2=\begin{pmatrix}
1&0&0&0\\1&0&0&0\\0&1&0&-1\\0&-1&1&0\\0&0&-1&1
\end{pmatrix},\qquad
 d_1=\begin{pmatrix}1&-1&-1&-1&-1\end{pmatrix}.
\]

The degree-one ordered basis is `(A_+, A_-, r_0, r_1, r_2)`. Define

\[
z=(1,0,1,0,0)^T,\qquad r=(0,0,1,1,1).
\]

Then

\[
d_1z=0,\qquad rd_2=0,\qquad rz=1.
\]

Let `C` be the nonzero spectator coefficient ring, retaining any specified Rees, long-occurrence, and long-normal parameters. Use the source-defined split normalization algebra

\[
B_+=C[x_1,x_2,x_3],\qquad B_-=C[y_1,y_2,y_3],\qquad
B=B_+\times_C B_-=C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j).
\]

The variables `x_1,x_2,x_3` here stand for the three positive-sheet short occurrences; the `y_j` stand for the negative-sheet short occurrences. Set

\[
I=(x_1,x_2,x_3,y_1,y_2,y_3),\qquad \epsilon:B\longrightarrow C=B/I.
\]

The short-normal graph, when needed for the endpoint target, remains `u_i^+=t_i^+ x_i` and `u_j^-=t_j^- y_j`. The map of complexes computed below does not identify a long occurrence coordinate with a long monodromy parameter. Localizing factors that become one on the conductor, such as `1+t_i x_i`, does not change the conductor or the calculated first two Tor modules.

For the B-linear calculation use the free extension

\[
J_B=B\otimes_{\mathbb Z}J_{\mathbb Z},\qquad
 a_C:J_B\longrightarrow C[1],\qquad (a_C)_1=\epsilon\circ r.
\]

The target `C[1]` is in homological degree one. If instead the source is extended to `C` from the outset, the same row is a quasi-isomorphism `J_C -> C[1]`. The nonexistence argument below applies to both choices. These two coefficient choices must not be confused with a derived base change of the complete normalization diagram.

## 2. Integral deformation retract

Define a chain map `i:B[1] -> J_B` by `i(1)=z`. The map `r:J_B -> B[1]` is the road row. The following integer matrices raise homological degree by one:

\[
h_0=\begin{pmatrix}1\\0\\0\\0\\0\end{pmatrix},\qquad
h_1=\begin{pmatrix}
0&1&0&0&0\\
0&0&0&-1&-1\\
0&0&0&0&-1\\
0&0&0&0&0
\end{pmatrix},\qquad
h_2=\begin{pmatrix}0&0&0&1\end{pmatrix}.
\]

They satisfy

\[
dh+hd=1-ir,\qquad ri=1,\qquad h^2=0,\qquad hi=0,\qquad rh=0.
\]

These are integer identities on all eleven states. Consequently

\[
J_B\simeq B[1],\qquad H_1(a_C)=\epsilon:B\longrightarrow C.
\]

The map on homology is nonzero. Tensoring both sides with the same retained invertible orientation line or passive Cartier grade preserves this conclusion; it does not require evaluating either normal frame.

## 3. Obstruction to the proposed primitive

A nullhomotopy `h:J_B -> C[1]` has cochain degree minus one. Its only possible nonzero component is `h_0:J_0 -> C[1]_1`. Thus, for a coefficient `c` in `C`, its boundary in degree one is

\[
(\delta h)_1=c\,\epsilon d_1.
\]

Every such row evaluates to zero on `z`, whereas `a_C(z)=1`. Therefore

\[
\delta h=a_C
\]

has no solution. This classifies every possible cochain of the required degree; it is not a bounded search over coefficients.

The normalization sequence defines

\[
T=[B\xrightarrow{\nu}B_+\oplus B_-],\qquad
\rho:T\xrightarrow{\simeq}C.
\]

Here `T` occupies cohomological degrees minus one and zero. The previously defined derived comparison is `a = rho[1]^{-1} a_C`. If a nullhomotopy of `a` existed in any enhancement compatible with these ordinary complexes, composition with `rho[1]` would nullhomotope `a_C`. Hence the derived mapping-space path set from `a` to zero is empty:

\[
\operatorname{Path}_{\operatorname{Map}_{D_\infty(B)}(J_B,T[1])}(a,0)=\varnothing.
\]

A framing restriction can remove possible homotopies; it cannot create one contradicting the underlying homology map. This does not prove nonvanishing of the desired physical `Delta_J`: the proposed expression has not been constructed on this source.

### Corrected Morse boundary cannot map to `z`

The independent Morse construction provides

\[
\widehat h_M=H_M\otimes p-\widetilde\xi\otimes h_{\rm occ},\qquad
 d\widehat h_M=\widehat q_J
 =q_J\otimes p-(d\widetilde\xi)\otimes h_{\rm occ}.
\]

Suppose `m` were a degree-preserving chain map into `J_B` with `m(widehat q_J)=z`. Then

\[
z=d\,m(\widehat h_M),\qquad
1=rz=rd\,m(\widehat h_M)=0.
\]

Thus the proposed source-model identification is impossible. The same argument excludes mapping `widehat q_J` to any representative of the class of `z`. It does not exclude a support-changing construction that retains homotopy data rather than identifying these ordinary homology classes.

## 4. Explicit strict lifts of the derived comparison

For the free B-source `J_B`, no non-existent B-linear section `C -> B_+ + B_-` is needed. Define B-linear maps from `B` itself:

\[
\ell_+(b)=(b_+,0),\qquad \ell_-(b)=(0,-b_-).
\]

Then

\[
(\epsilon_+-\epsilon_-)\ell_\pm=\epsilon,\qquad
\ell_+-\ell_-=\nu.
\]

Both

\[
(a_\pm)_1=\ell_\pm r,\qquad (a_\pm)_n=0\quad(n\ne1)
\]

are chain maps `J_B -> T[1]`. The shift gives the differential `d_{T[1],2}=-nu`. Define the cochain `S` of degree minus one by

\[
S_1=-r:J_1\longrightarrow T[1]_2=B,
\]

and zero otherwise. Direct calculation gives

\[
\delta S=a_+-a_-.
\]

These strict representatives agree as derived morphisms and both have zero values on the two designated endpoint coordinates of `J_1`. They are lifts of the row construction, not newly proved physical source correspondences.

### Nonclosed postcomposition needs its homotopy correction

The earlier kernel construction has a degree-one cochain `k_nu` with `delta k_nu=e_nu`; it is not a closed derived morphism. On `T[1]_1=B_+ + B_-`, it is `-G`, where

\[
G(f_+,f_-)=f_+v_++f_-v_-,\qquad G\nu=v,
\qquad v(b)=b(v_++v_-).
\]

The actual compositions are

\[
H_+=k_\nu a_+=-v_+r,\qquad
H_-=k_\nu a_-=v_-r.
\]

They are closed in this strict model, since `e_nu a_+=e_nu a_-=0`. Their difference is

\[
H_+-H_-=e_\nu S=-(v_++v_-)r.
\]

The properly transported comparison is

\[
H_+-H_--e_\nu S=0.
\]

In particular the derived roof for `a` does not, on its own, define the nonclosed composite `k_nu a` independently of representative and comparison homotopy. This is a second precise correction to the preceding conclusion.

The difference need not be an ordinary boundary if the correction `e_nu S` is omitted. After the valid specialization `t_i^+=t_j^-=1`, the positive endpoint class is represented by `1/(x_1 x_2 x_3)` in the full unmarked target. Every incoming one-mark summand leaves one of the three variables unlocalized. The coefficient of `x_1^{-1} x_2^{-1} x_3^{-1}` therefore annihilates all endpoint boundaries and evaluates `v_+` to one. The negative endpoint has the analogous detector. If the units `1+x_i` are retained, use their expansions at the conductor; this detector is unchanged. Applying `r` to the source keeps the same unit detector on `H_+-H_-`.

This detects the failure of representative-independent nonclosed postcomposition. It is not a proposed physical secondary invariant.

## 5. The universal source on which nullhomotopy exists

The required relative source is determined, rather than guessed, by the homotopy fibre

\[
F=\operatorname{fib}(a_C:J_B\longrightarrow C[1]).
\]

Use coordinates

\[
F_3=B,\quad F_2=B^4,\quad F_1=B^5,\quad F_0=B\oplus C.
\]

Its differential from degree one is

\[
d_{F,1}(w)=\bigl(d_1w,\epsilon(rw)\bigr).
\]

The higher differentials are `d2,d3` from `J`. Projection `p:F -> J_B` has the canonical nullhomotopy

\[
s_F:F_0\longrightarrow C[1]_1,\qquad s_F(b,c)=c,
\qquad \delta s_F=a_Cp.
\]

The source primitive is not retained as a closed unit inside `F`:

\[
d_Fz=(0,1).
\]

### Exact reduction

There is an explicit deformation retract of `F` onto

\[
L=[B\xrightarrow{\epsilon}C]
\]

in homological degrees one and zero. The projection is `r` in degree one and projection onto `C` in degree zero. The inclusion is `z` in degree one and inclusion of the second summand in degree zero. Its homotopy is the preceding `h` on the `J` coordinates and zero on the added `C` coordinate. Every matrix is exported.

Since the kernel of `epsilon` is `I` and `epsilon` is surjective,

\[
F\simeq I[1].
\]

This source includes precisely the conductor-vanishing amplitudes at the level of its surviving homology. It is not the physical unit line. A map from a physical source into `F` must itself be constructed before identifying `F` as its realization.

The homotopy-fibre universal property is: a map `L' -> F` is a map `m:L' -> J_B` together with a specified nullhomotopy of `a_C m`. It does not impose the impossible condition `m(widehat q_J)=z`.

## 6. Derived restriction recovers conductor normal information

The coefficient module `C=B/I` is not flat over `B`. Hence termwise substitution in the displayed fibre complex is not a valid way to calculate its derived conductor restriction.

The derived restriction is

\[
C\otimes_B^L F\simeq(C\otimes_B^L I)[1].
\]

Its first two homological groups are

\[
H_1(C\otimes_B^L F)=I/I^2\cong C^6,
\]

\[
H_2(C\otimes_B^L F)=\operatorname{Tor}_1^B(C,I)
\cong\operatorname{Tor}_2^B(C,C)\cong C^{24}.
\]

Here is the complete justification for the second rank. A resolution of `C` starts with `B^6 -> B -> C`. The 24 first syzygies are

\[
x_i e_j^+-x_j e_i^+\ (i<j),\qquad
 y_i e_j^--y_j e_i^-\ (i<j),
\]

\[
y_j e_i^+,\qquad x_i e_j^-\quad(1\le i,j\le3).
\]

There are three syzygies within each branch and eighteen mixed ones. They generate all first relations: restrict an arbitrary relation to each polynomial sheet, apply the usual polynomial Koszul syzygies within that sheet, and subtract them. The remaining coefficients lie on the opposite sheet and are generated by the mixed syzygies.

All entries of this differential lie in `I`. There is no relation between these 24 columns with a nonzero conductor-constant coefficient. This can be checked in homogeneous degree two: the map from 36 variable-generator products to the twelve surviving quadratic monomials has these 24 columns as a saturated integral kernel basis. The checker constructs a unimodular completion. Therefore any next resolution differential also has entries in `I` in these components, and tensoring with `C` gives `Tor_2(C,C)=C^24`. Dimension shifting along `0 -> I -> B -> C -> 0` gives the stated group.

This uses an unbounded resolution only through the exact first syzygy statement; no assertion that the displayed truncation resolves every higher Tor group is made. Higher Tor groups have not been classified here.

In contrast, naively tensoring the non-flat two-term representative `L` term by term produces `[C -> C]`, which is contractible. That calculation loses the six first conormal directions and the twenty-four first relations just displayed.

## 7. Consequence for the physical task

The coefficient comparison `a_C` and its derived lift exist. The proposed use of that map as the boundary of a transported Morse homotopy is impossible. Consequently the expression `-k_nu h_Morse` has not become a candidate in the framed mapping complex.

The independent physical problem still concerns two trivializations of the **same composite**, not a nullhomotopy of a nonzero unit-valued source map. An admissible comparison must retain the actual corrected Morse source, the map from its entire boundary packet, and the homotopy identifying its composite with the conductor composite. None of those can be obtained by sending its exact corrected cycle to the Entry-436 primitive.

This result assigns no value to the physical `Delta_J`. It supplies an explicit exclusion of the last proposed identification, strict chain lifts for the valid coefficient map, and a universal relative source on which the nullhomotopy equation is well typed.

## Sources and replay

Repository: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

- `research/voevodsky/check_physical_derived_pullback_after_transform.py`: the eleven-state matrices and primitive row/cycle.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: the corrected Morse identity and the distinction between occurrence and monodromy.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the normalization algebra and exact sequence.
- Previously generated `conductor_kernel_homotopy/proof.md`: the cochain `k_nu`, the endpoint coefficient map `G`, and the condition `delta h=a` used in the proposed primitive.

General constructions: Stacks Project 0A8H (Hom differential and composition), 014D (cones), 00LY (Tor and long exact sequences), 06XP (derived Ext).

Replay with `python check.py` using Python 3.10 or newer. Only the standard library is required. The certificate counts 52 exact checks; mathematical completeness and scope are explained above. It does not claim a numerical check establishes a physical comparison.

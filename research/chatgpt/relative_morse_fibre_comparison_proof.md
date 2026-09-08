# Endpoint-derived relative Morse-to-conductor-fibre comparison

## Result

There is an explicit pair of coefficient-linear maps from the complete corrected Morse source to an endpoint-line-valued refinement of the conductor fibre. They arise from the conductor connecting morphism applied to the two labelled endpoint augmentations. Neither map is obtained by fitting a residue value.

The two maps give independent conductor-supported derived classes. On derived conductor restriction, the six native endpoint normal states map to the six corresponding conormal directions with their Rees factors retained.

The same calculation proves a limitation: no degree-preserving, coefficient-linear map from this Morse source to the proposed fibre can send the raw generic chain to a scalar conductor unit. For the constructed map, the raw generic chain has the exact coefficient `X13*X15*X35`, and the complete corrected Morse boundary maps to zero.

Thus the relative endpoint comparison is constructed. A fully physical comparison preserving an independently specified unit Q-roof is not constructed. The coefficient map into the conductor is not a substitute for the full Q/support diagram.

## 1. Coefficients, source, and conventions

Use homological degrees: differentials lower degree by one. A cochain of degree r lowers homological degree by r, and the Hom differential is

\[
\delta f=d f-(-1)^r f d.
\]

The coefficient base is the split normalization algebra

\[
B=\mathcal C[X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}]
 /(X_eX_o:e\in\{02,04,24\},\ o\in\{13,15,35\}).
\]

Here \(\mathcal C\) retains the three long occurrence variables, the three independent long-normal variables, and all six short Rees parameters. Put

\[
I=(X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}),\qquad
\epsilon:B\longrightarrow\mathcal C=B/I.
\]

The two labelled endpoints are

\[
V_+=\{13,15,35\},\qquad V_-=\{02,04,24\}.
\]

For each short diagonal d, impose the previously specified graph relation

\[
u_d=t_dX_d.
\]

The long normals remain independent. No occurrence, normal, Rees parameter, or integer is inverted in the construction. It remains valid after adjoining the monodromy units: the short factors \(1+t_dX_d\) reduce to one on the conductor.

The source is reconstructed from `check_d03_pabs_morse_pullback.rs` at commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`. It is the old-normal pullback on the stellar subdivision at `{03,13}`, not the different native-normal 245-state blowdown model.

A generator before the extra occurrence factor is

\[
(F_0<\cdots<F_k,H),\qquad H\subseteq\pi(F_0).
\]

The blowdown \(\pi\) replaces E by `{03,13}`. Deleting the initial flag vertex multiplies by the occurrence monomial of \(\pi(F_1)\setminus\pi(F_0)\); other simplicial faces have unit coefficient. Normal deletion carries \(u_d\) and the source's Koszul sign. There are 581 flags and 1,169 loaded generators.

Tensor this source with the separate occurrence complex

\[
K_{\rm occ}(X_{35})=[B h_{\rm occ}\xrightarrow{X_{35}}Bp].
\]

The complete source \(\widehat M\) has 2,338 generators, with homological degree ranks

\[
(51,354,824,803,294,12).
\]

All normal marks and both states of the occurrence factor are retained. At each endpoint there are eight native normal states and their eight occurrence partners, for 32 endpoint states in total. The occurrence generator is not identified with the native monodromy circle labelled 35.

## 2. The relative target and its endpoint coefficient lines

Retain the eleven-state Entry-436 coefficient complex \(J_B\), with

\[
d_1=(1,-1,-1,-1,-1),\qquad
r=(0,0,1,1,1),\qquad z=(1,0,1,0,0)^T.
\]

Its higher differential matrices are reproduced in the certificate. They satisfy

\[
d_1z=0,\qquad r d_2=0,\qquad rz=1.
\]

The previously constructed fibre is

\[
F=\operatorname{fib}(\epsilon r:J_B\longrightarrow\mathcal C[1]).
\]

In the chosen cone convention,

\[
F_3=B,\quad F_2=B^4,\quad F_1=B^5,\quad F_0=B\oplus\mathcal C,
\]

\[
d_{F,1}(w)=(d_1w,\epsilon(rw)).
\]

The map \(I[1]\to F\), \(b\mapsto bz\), is a quasi-isomorphism. One can use the integral contraction of \(J_B\) onto \(B[1]\) to retract F onto \([B\xrightarrow{\epsilon}\mathcal C]\) in degrees one and zero. Its surviving homology is I, in degree one.

Retaining occurrence gradings requires two different endpoint lines. Define free graded lines \(L_\pm=B\ell_\pm\) by

\[
\deg_X\ell_+=-\epsilon_{13}-\epsilon_{15}-\epsilon_{35},\qquad
\deg_X\ell_-=-\epsilon_{02}-\epsilon_{04}-\epsilon_{24}.
\]

These are the degrees of the two unmarked endpoint generators in the actual source. They are formal coefficient-line generators, not scalar reciprocals of the corresponding occurrence monomials.

The endpoint-line-valued refinement is

\[
F_\partial=(F\otimes L_+)\oplus(F\otimes L_-).
\]

This preserves the two labelled coefficient targets rather than identifying different occurrence degrees. It is not yet the full physical endpoint/Q correspondence. Discrete orientation and polarity lines can be tensored throughout without evaluation; no equality of a conormal line with a scalar has been used.

## 3. Endpoint augmentations and the complete matrix

Let \(E_\pm:\widehat M_0\to B\) be scalar coefficient extraction at the unmarked singleton vertex \(V_\pm\otimes p\), in its fixed endpoint basis. It is zero on the other degree-zero generators. Define

\[
e_\pm(c)=\epsilon(E_\pm(c))\ell_\pm,\qquad
e_\pm:\widehat M\longrightarrow\mathcal C\ell_\pm[0].
\]

These are chain maps. Every differential entering one of these endpoint generators carries a nonempty short occurrence monomial, a short normal \(t_dX_d\), or the occurrence factor \(X_{35}\), so its augmentation is zero.

This assertion uses the short-normal graph. If the short u-variables were kept independent while only the X-variables were set to zero, the endpoint normal column would have augmentation \(u_d\), not zero. The same endpoint augmentation would then not be a chain map.

Apply the connecting morphism of

\[
0\longrightarrow I L_\pm\longrightarrow B L_\pm
\longrightarrow\mathcal C L_\pm\longrightarrow0
\]

to \(e_\pm\). Since \(\widehat M\) is a bounded free B-complex, lifting \(e_\pm\) by \(E_\pm(-)\ell_\pm\) computes the connecting cocycle directly. Our Hom convention gives

\[
\lambda_\pm(c)=-E_\pm(dc)\ell_\pm,\qquad
\lambda_\pm:\widehat M_1\longrightarrow I L_\pm.
\]

Compose with \(I L_\pm[1]\to F\otimes L_\pm\):

\[
m_{\pm,1}(c)=-E_\pm(dc)\,z\otimes\ell_\pm,\qquad
m_{\pm,n}=0\quad(n\ne1).
\]

The entire paired matrix \(m_\partial=(m_+,m_-)\) is determined by the following rules. For either endpoint V and its line \(\ell_V\):

- On an unmarked two-vertex flag \((G<V)\otimes p\), with G a proper subset of V,
  \[
  m_V((G<V)\otimes p)
  =-\left(\prod_{d\in V\setminus G}X_d\right)z\otimes\ell_V.
  \]
- On a singleton endpoint with one native circle,
  \[
  m_V((V,\{d\})\otimes p)=-t_dX_dz\otimes\ell_V.
  \]
- On its separate occurrence partner,
  \[
  m_V((V,\varnothing)\otimes h_{\rm occ})=-X_{35}z\otimes\ell_V.
  \]
- All other columns are zero.

There are eleven nonzero source columns at each endpoint: seven incoming flags, three native normal states, and one occurrence partner. Since z has two nonzero coordinates, the full matrix has 22 nonzero source columns and 44 polynomial entries.

Every coefficient belongs to I. Thus

\[
d_Fm_\pm=0,\qquad m_\pm d=-zE_\pm d^2=0.
\]

The checker verifies the chain equation on all 2,338 columns, not only these 22. It also verifies the exact occurrence and Rees multidegrees of every matrix entry. The maps have conductor-filtration order at least one.

## 4. Nonzero relative classes and their annihilator

The new maps are not the previously rejected map sending a corrected Morse boundary to z. They are connecting classes with values in \(I[1]\).

They determine independent classes

\[
\mathcal C[m_+]\oplus\mathcal C[m_-]
\hookrightarrow
H^0\operatorname{RHom}_B(\widehat M,F_\partial).
\]

This is an injection of the displayed submodule, not a computation of the entire mapping group.

To prove nonvanishing, use the quasi-isomorphism \(I[1]\to F\). A nullhomotopy of a linear combination with constant conductor coefficient c would be an I-valued degree-zero endpoint coefficient b. At a positive endpoint normal d, its chain equation would require

\[
t_dX_db=-c\,t_dX_d.
\]

Restrict to the positive polynomial branch. There \(t_dX_d\) is a nonzero divisor, so \(b_+=-c\). But b belongs to I, and its conductor augmentation is zero. Therefore c=0. The negative endpoint has an independent argument on the negative polynomial branch. The argument survives all prescribed monodromy-unit localizations, whose conductor images are units.

Conversely, for any \(x\in I\), the I-valued cochain \(-xE_\pm\) is an explicit nullhomotopy of \(x m_\pm\). The verifier checks this on all source columns for the six ideal generators. Consequently

\[
\operatorname{Ann}_B[m_\pm]=I.
\]

Forgetting the fibre homotopy makes the maps exact. Let \(p_F:F\to J_B\). Then

\[
p_Fm_\pm=\delta(-zE_\pm).
\]

The same candidate primitive inside F has an extra degree-zero value

\[
d_F(-zE_\pm)=(0,-\epsilon E_\pm)
\]

on the endpoints. This is exactly why it does not nullhomotope the zero-framed lift. The lost datum is the original endpoint augmentation, not an unspecified physical constraint.

## 5. Exact evaluation on the corrected Morse chain

Use the repository's labels

\[
a=V_+,\qquad c=\{03,02,35\}.
\]

The source's weighted gallery satisfies

\[
d\widetilde\xi
=X_{03}X_{02}\,c-X_{13}X_{15}\,a,
\]

\[
dH_M=q_J-X_{35}\widetilde\xi,\qquad
dq_J=X_{35}d\widetilde\xi.
\]

After the normalization pullback, the mixed product \(X_{02}X_{35}\) vanishes, while the all-positive product does not. Put

\[
\Pi_+=X_{13}X_{15}X_{35}.
\]

The complete endpoint-derived matrix gives

\[
m_+(q_J\otimes p)=\Pi_+z\otimes\ell_+,\qquad
m_-(q_J\otimes p)=0.
\]

The separate endpoint correction has exactly the same image:

\[
m_+((d\widetilde\xi)\otimes h_{\rm occ})
=\Pi_+z\otimes\ell_+.
\]

Therefore

\[
\widehat h_M=H_M\otimes p-\widetilde\xi\otimes h_{\rm occ},\qquad
\widehat q_J=q_J\otimes p-(d\widetilde\xi)\otimes h_{\rm occ}
\]

satisfy

\[
d\widehat h_M=\widehat q_J,\qquad
m_\partial(\widehat h_M)=0,\qquad
m_\partial(\widehat q_J)=0.
\]

The chain equation is preserved. The corrected boundary is not assigned to the nonzero homology generator z.

The raw coefficient \(\Pi_+\) has conductor order exactly three. It has zero first and second conductor symbols and nonzero third symbol. It must not be replaced by 1 or identified with an unshifted first-normal unit. Its coefficient here is a boundary-construction output, not a new physical residue.

## 6. The six native normal directions have an actual derived image

Derived conductor restriction gives

\[
H_1(\mathcal C\otimes_B^L F)=I/I^2.
\]

In the refined target there is one such module with each endpoint line. These are not obtained by substituting into the nonflat term \(\mathcal C\) of the displayed fibre matrix.

The first free module of a resolution of I has basis \(E_d\), with differential \(E_d\mapsto X_d\). Lifting the displayed native endpoint normal columns gives

\[
e_d^\pm\longmapsto-t_dE_d\otimes\ell_\pm.
\]

Their compatibility on every two-normal endpoint state is checked using all 24 first syzygies of I: six within-sheet Koszul relations and eighteen mixed-sheet annihilator relations. This determines the induced degree-one conductor map

\[
H_1(\mathcal C\otimes_B^L m_\pm)(e_d^\pm)
=-t_d[X_d]\otimes\ell_\pm.
\]

The six native normal states survive as independent source classes after conductor restriction: every incoming and outgoing differential coefficient at each singleton endpoint vanishes. Their images occupy six independent rows of the line-valued target. The corresponding six-by-six minor is \(\prod_{d\in V_+\cup V_-}t_d\), a nonzero polynomial.

Thus the native-normal subspace map has generic rank six and retains its individual Rees factors. This is not a claim that setting a Rees parameter to zero leaves its image nonzero.

The extra occurrence states also remain. At either endpoint their induced value is

\[
h_{\rm occ}^\pm\longmapsto-[X_{35}]\otimes\ell_\pm.
\]

At the positive endpoint this produces the expected repeated-coordinate relation with its native 35-circle, but the two source generators have not been merged. No rank-one selector for all six directions has been derived.

## 7. Universal obstruction to unit scalar Q-normalization

Let \(n:\widehat M\to F\) be any degree-zero B-linear chain map, with any endpoint homotopies. The map \(r p_F:F\to B[1]\) is closed. Applying it to the actual Morse equation gives

\[
rp_Fn(q_J\otimes p)
=X_{35}\,rp_Fn(\widetilde\xi\otimes p).
\]

This is an equality of B-coefficients. Since \(\epsilon(X_{35})=0\),

\[
\epsilon\bigl(rp_Fn(q_J\otimes p)\bigr)=0.
\]

It cannot equal the conductor unit. The same argument holds componentwise with retained endpoint lines, or after any refinement that has a B-linear forgetful chain map to this fibre and uses that readout as its scalar Q-normalization.

This does not prove that a physical support-graded Q-roof vanishes. It proves that identifying that roof with the scalar readout \(\epsilon r\) is incompatible with this source's loaded Morse equation. A supported Gysin or other extraordinary comparison can change the relevant objects, degrees, and lines; such a comparison must be constructed rather than represented by a unit scalar substitution.

## 8. Verification and limits

The standalone checker reconstructs both differentials, the complete source, the endpoint augmentations, the 44-entry comparison, the exact corrected Morse chains, the endpoint-normal first-Tor lift equations, and every conductor-annihilator homotopy. The certificate includes all new matrix entries and the actual marked source labels.

It performs 40,106 exact checks. No parameter sampling, rational rank heuristics, omitted source columns, or inverted coefficient parameters are used. The polynomial-sheet regularity argument and the Tor interpretation above are proofs; their validity is not inferred from the number of checks.

The new result is an endpoint-derived relative comparison with explicit nontrivial coefficient classes. It is not the physical \(\Delta_J\), and it is not a completed unit-Q normalization-conductor correspondence. The formal fibre construction is no longer an unspecified map, but the physical Q/support comparison remains distinct.

## Sources

Repository input, all at commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

1. `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the split normalization algebra, sheet labels, and conductor ideal.
2. `research/voevodsky/check_d03_pabs_morse_pullback.rs`, blob `46624341c7956a8557249a54b117a88d43adfd62`: the complete old-normal flag differential, occurrence correction, and seven-triangle Morse identity.
3. `research/voevodsky/check_physical_derived_pullback_after_transform.py`, blob `7993b2b1bbdba03d05c3f443a45717d7b8efeec5`: the eleven-state coefficient matrices and road readout. Only those matrices are used; their signature assertions do not establish the missing physical source identification.

General mathematical conventions:

4. Stacks Project, Tag 0A8H, Hom complexes: https://stacks.math.columbia.edu/tag/0A8H
5. Stacks Project, Tag 014D, Cones and termwise split sequences: https://stacks.math.columbia.edu/tag/014D
6. Stacks Project, Tag 064B, maps from bounded-above projective complexes: https://stacks.math.columbia.edu/tag/064B
7. Stacks Project, Tag 00LY, Tor and its naturality: https://stacks.math.columbia.edu/tag/00LY

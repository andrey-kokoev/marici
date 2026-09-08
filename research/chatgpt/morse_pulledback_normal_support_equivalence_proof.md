# Complete pulled-back-normal Morse comparison and the actual support quotient

## Result and scope

There is an explicitly computed, polynomial chain-homotopy equivalence

\[
\mathsf R:\widehat M\longrightarrow C_{\mathrm{fin}}\otimes_AK_{\mathrm{occ}}(X_{35}),
\]

from the complete corrected Morse source with 2,338 generators to the full original cellular coefficient complex with its occurrence correction, with 430 generators. Its inverse and homotopy preserve both endpoint subcomplexes and the entire short-boundary subcomplex. No occurrence or normal coordinate is inverted.

This is a comparison of the **pulled-back-normal** source specified in the repository's Morse construction. Its intermediate cellular model has 255 states. It is not the previously studied 245-state **native-normal** logarithmic model, whose exceptional resonance kernel is a different calculation.

The actual generic support quotient has 786 source states and reduces to fourteen states, in degrees two through four. In particular, its degree-one homology is zero. The projection that retains only flags between the top and the three long facets is not a chain map on the complete source: it discards mixed triangles whose boundaries contain the retained generic edges with coefficient one.

This establishes the ordinary coefficient/source comparison and corrects the previously used generic-flag projection. It does not construct the extraordinary normalization-conductor comparison or determine the physical conductor–Morse invariant.

## 1. Coefficients and the complete source

Let \(\mathcal D\) be the nine diagonals of the labelled hexagon. Work first over

\[
A=\mathbb Z[X_d,u_d:d\in\mathcal D].
\]

The occurrence variables and the normal monodromy parameters are independent. The identities also hold after localizing at the monodromy units \(1+u_d\), without inverting \(u_d\) or \(X_d\).

Stellar-subdivide the noncrossing face complex at \(\{03,13\}\), introducing the exceptional label \(E\). The old-face map is

\[
\pi(F)=
\begin{cases}
F,&E\notin F,\\
(F\setminus\{E\})\cup\{03,13\},&E\in F.
\end{cases}
\]

There are 51 expanded faces and 581 strict flags. A source basis state is

\[
[F_0<\cdots<F_k;H],\qquad H\subseteq\pi(F_0),
\]

in homological degree \(k+|H|\). Its coefficient module is free over \(A\). The first flag deletion multiplies by

\[
\prod_{d\in\pi(F_1)\setminus\pi(F_0)}X_d.
\]

Every other flag deletion is a signed unit map. Removing the \(j\)-th normal mark has coefficient \((-1)^{k+j}u_d\), using zero-based positions. This is the full pulled-back normal model in `check_d03_pabs_morse_pullback.rs`.

There are 1,169 such basis states. Tensor with the independent occurrence complex

\[
K_{\mathrm{occ}}(X_{35})=[Ah_{\mathrm{occ}}\xrightarrow{X_{35}}Ap]
\]

in degrees one and zero. The complete corrected source \(\widehat M\) has ranks

\[
(51,354,824,803,294,12)
\]

in degrees zero through five. The checker verifies its full square-zero differential before any coefficient specialization.

## 2. Explicit reduction to the pulled-back cellular model

A unit cancellation removes a pair \(a,b\) with \(d(b)=\varepsilon a+v\), \(\varepsilon=\pm1\). If \(c_j\) is the \(a\)-coefficient of \(d(j)\), the reduced differential and maps on surviving generators are

\[
d'(j)=d(j)-\varepsilon c_jd(b),\qquad
p(a)=-\varepsilon v,\qquad p(b)=0,
\]

\[
i(j)=j-\varepsilon c_jb,\qquad h(a)=\varepsilon b.
\]

The displayed differential is restricted to the surviving coordinates. These maps satisfy

\[
pi=1,\qquad dh+hd=1-ip.
\]

The checker composes these exact contractions, rather than inferring an equivalence from ranks or from selected specializations.

In the first reduction, a pair may be cancelled only when its two flags have the same initial face and the same normal subset. There are 457 cancellations. The remaining 255 generators are naturally indexed by

\[
[F,H],\qquad H\subseteq\pi(F),
\]

in degree \(3-|F|+|H|\). Their ranks are

\[
(16,72,108,56,3).
\]

After a verified diagonal change of orientation signs, their differential has the expected form: add a ray with the signed old-face occurrence quotient, or remove an old normal with its normal parameter and the totalization sign.

The top orientation is fixed to agree with the original cellular convention. The remaining signs are determined by the incidence equations; every cycle in those equations is checked. No coefficient normalization is chosen from a desired residue.

The difference from the native 245-state model is essential. At an exceptional-only face, the pulled-back coefficient retains the independent old normals for both 03 and 13. A native exceptional normal, with monodromy \((1+u_{03})(1+u_{13})-1\), is not substituted for those two old normal directions in this construction.

## 3. The full pulled-back blowdown and its contractible kernel

The original finite target \(C_{\mathrm{fin}}\) has 215 generators \([F,H]\), \(H\subseteq F\), and ranks \((14,63,93,45)\). Its differential adds a diagonal with coefficient \(X_d\) or removes a normal with coefficient \(u_d\), with the prescribed signs.

The cellular blowdown has formula

\[
K[F,H]=
\begin{cases}
\varepsilon(F)[\pi(F),H],&|\pi(F)|=|F|,\\
0,&|\pi(F)|>|F|.
\end{cases}
\]

When \(E\in F\) and one center member is retained, replace \(E\) by the missing center member and use the sign of sorting that ordered list. On unchanged faces the sign is one. All marks are old normal marks, so the normal map is the identity on their labels.

The full equation \(dK=Kd\) is verified. The map is degreewise split surjective, and its kernel has ranks

\[
(2,9,15,11,3).
\]

All forty kernel generators contract through twenty unit cancellations. The checker exports the complete kernel differential and its contracting homotopy.

More explicitly, choose the exported graded section \(s_0\), kernel inclusion \(i_N\), and kernel projection \(p_N\). The attaching map is

\[
\delta=p_Nd s_0.
\]

For the computed kernel contraction \(h_N\), the corrected section and homotopy are

\[
s=s_0-i_Nh_N\delta,\qquad h_K=i_Nh_Np_N.
\]

They satisfy \(ds=sd\), \(Ks=1\), and \(dh_K+h_Kd=1-sK\). These formulas retain the exceptional attachment rather than deleting the kernel as a graded module.

Combining both reductions, then tensoring with the occurrence complex, gives matrices

\[
\mathsf R:\widehat M\to\widehat C,\qquad
\mathsf U:\widehat C\to\widehat M,\qquad
\mathsf G:\widehat M_n\to\widehat M_{n+1},
\]

where \(\widehat C=C_{\mathrm{fin}}\otimes K_{\mathrm{occ}}(X_{35})\), with

\[
\mathsf R\mathsf U=1,\qquad
d\mathsf G+\mathsf Gd=1-\mathsf U\mathsf R.
\]

The matrix \(\mathsf R\) is \(430\times2338\), with 1,426 nonzero polynomial entries. The inverse has 1,168 entries and the homotopy has 4,734 entries. Every chain equation and homotopy equation is checked on every basis generator.

## 4. Actual support filtration and endpoint frames

Let \(V_M\) be the direct sum of the two endpoint packets, including the occurrence factor. Let \(B_M\) consist of states whose initial old face contains a short diagonal. Since a flag is increasing, these are exactly the flags lying entirely in the short-boundary face subposet. The corresponding target subcomplexes are \(V_C\) and \(B_C\).

The support counts are

| Object | Corrected source | Corrected cellular target |
|---|---:|---:|
| Both endpoint packets | 32 | 32 |
| Complete short boundary | 1,552 | 416 |
| Full complex | 2,338 | 430 |
| Quotient by the short boundary | 786 | 14 |

All inclusions are actual subcomplex inclusions. The three matrices preserve the endpoint and short-boundary supports, and \(\mathsf G\) is zero on every endpoint state. Thus they induce chain-homotopy equivalences on the subcomplexes and the quotients.

In the fixed cell-orientation convention, an unmarked positive endpoint has sign \(+1\), and an unmarked negative endpoint has sign \(-1\); the same signs hold on all their normal and occurrence partners. These explicit orientation identifications are part of the exported matrix. They are not a claimed identification with the separate physical ray-to-sheet swap.

Every entry is homogeneous in the independent occurrence and normal grading. A source state has occurrence weight minus its initial old-face vector, normal weight its marked subset, and the separate occurrence partner adds \(\epsilon_{35}\). The corresponding target weights use its cellular face. The identities therefore preserve the Rees weights after \(u_s=t_sX_s\).

The same full equations were rechecked after adjoining the short Rees parameters, imposing \(u_s=t_sX_s\), and imposing the alternating normalization relations \(X_eX_o=0\). Since the original chain homotopies are polynomial identities, they survive this nonflat base change. No flatness assumption is used to replace a derived fibre by an ordinary fibre.

## 5. The omitted mixed flags invalidate the three-edge projection

Define the thin generic subcomplex by retaining only flags all of whose vertices are the top face or one of the three long facets. With normals and the occurrence factor it has twenty states. It includes into the full source, but projection onto it is not a chain map.

For example, let

\[
c=\{02,03,35\},\qquad
\sigma=[\varnothing,\{03\},c].
\]

The actual differential is

\[
d\sigma=X_{03}[\{03\},c]-[\varnothing,c]+[\varnothing,\{03\}].
\]

Deleting the two mixed flags while keeping the pure generic edge gives

\[
\pi_{\mathrm{thin}}(\sigma)=0,\qquad
\pi_{\mathrm{thin}}(d\sigma)=[\varnothing,\{03\}]\ne0.
\]

This is an exact unit-coefficient obstruction. The full checker finds 238 nonzero defect columns, not just this one example.

The edge itself is not a cycle in the actual source or its full short-boundary quotient:

\[
d[\varnothing,\{03\}]=X_{03}[\{03\}]-[\varnothing].
\]

Both vertices survive that quotient. Classifying \([\varnothing,v_+]\) as a lower endpoint-support chain merely because of its terminal vertex also fails: the flag has the top face as its initial coefficient support and geometrically crosses the interior.

Entry 397's edge-coordinate argument therefore cannot identify the homology of the actual quotient of the supplied loaded complexes. The ordinary support filtration requires the mixed flags and their boundaries to remain. This does not exclude an additional extraordinary or explicitly framed construction; it excludes using the thin projection as the chain map for that construction.

## 6. The correct finite Q packet is retained

Before the occurrence factor, the full 393-state quotient reduces to

\[
Q_3=A\langle T,h_{03},h_{14},h_{25}\rangle,
\qquad
Q_2=A\langle p_{03},p_{14},p_{25}\rangle,
\]

with

\[
M_Q=
\begin{pmatrix}
X_{03}&u_{03}&0&0\\
X_{14}&0&u_{14}&0\\
X_{25}&0&0&u_{25}
\end{pmatrix}.
\]

This is the original seven-state cellular Q packet. It is not acyclic. Its homology is

\[
H_2(Q)=\operatorname{coker}M_Q,\qquad
H_3(Q)=A\langle\Theta\rangle,
\]

where

\[
\Theta=u_{03}u_{14}u_{25}T
-X_{03}u_{14}u_{25}h_{03}
-X_{14}u_{03}u_{25}h_{14}
-X_{25}u_{03}u_{14}h_{25}.
\]

To prove the kernel formula, write a cycle as \(aT+\sum b_dh_d\). The equations \(X_da+u_db_d=0\), reduced modulo each independent \(u_d\), force \(u_d\mid a\). Thus their product divides \(a\), and each \(b_d\) is forced. This is an all-polynomial argument; the checker independently verifies the displayed cycle.

The three \(p_d\) lift to oriented eight-triangle relative cycles in the source quotient. Their representatives are exported. In particular, setting every occurrence and normal variable to zero annihilates every differential but preserves the unit coefficient of \(p_{03}\). This is a valid specialization, including after inversion of \(1+u_d\), and detects a nonzero class.

With the occurrence factor retained, the finite quotient has fourteen states:

\[
\widehat Q_4=A^4,\qquad
\widehat Q_3=A^7,\qquad
\widehat Q_2=A^3,
\]

\[
d_4=
\begin{pmatrix}-X_{35}I_4\\M_Q\end{pmatrix},
\qquad
d_3=(M_Q\mid X_{35}I_3).
\]

Hence \(H_1(\widehat Q)=0\). The degree-two and degree-three normal/support information has not been removed to obtain this vanishing. The full 786-state quotient is chain-homotopy equivalent to this fourteen-state complex.

## 7. Evaluation of the actual Morse chains

The repository supplies the seven-triangle \(H_M\), six-flag gallery \(\widetilde\xi\), and three-term roof \(q_J\), with

\[
dH_M=q_J-X_{35}\widetilde\xi.
\]

For the explicit cellular approximation constructed above, let

\[
\Gamma=X_{03}[\{03,35\},\varnothing]
+X_{13}[\{13,35\},\varnothing].
\]

Direct matrix evaluation gives

\[
\mathsf R(H_M)=0,\qquad
\mathsf R(\widetilde\xi)=\Gamma,\qquad
\mathsf R(q_J)=X_{35}\Gamma.
\]

Every output lies in the short-boundary subcomplex. The pure generic flag \([\varnothing,\{03\}]\) has zero image; this is compatible with its actual boundary and its degree.

The corrected chains remain

\[
\widehat h_M=H_M\otimes p-\widetilde\xi\otimes h_{\mathrm{occ}},
\]

\[
\widehat q_J=q_J\otimes p-(d\widetilde\xi)\otimes h_{\mathrm{occ}},
\qquad d\widehat h_M=\widehat q_J.
\]

Their cellular images are

\[
\mathsf R(\widehat h_M)=-\Gamma\otimes h_{\mathrm{occ}},
\]

\[
\mathsf R(\widehat q_J)
=X_{35}\Gamma\otimes p-d\Gamma\otimes h_{\mathrm{occ}}.
\]

The second is the boundary of the first, with the tensor sign determined by the degree-one gallery. Both vanish on projection to the actual Q quotient. Their nonzero lower-support terms remain in the full target.

These representatives depend on the stated cellular approximation. Their chain equations and support preservation are exact; no uniqueness in the fully framed physical category is asserted.

## 8. A same-complex secondary filling comparison

Let \(\bar q_J\) and \(\bar H_M\) denote the images in the full source short-boundary quotient, and let \(\mathsf G_Q\) be the induced source homotopy. Since their cellular projections vanish,

\[
H_{\mathrm{red}}=\mathsf G_Q(\bar q_J),\qquad
dH_{\mathrm{red}}=\bar q_J.
\]

The reduction-derived filler has eight triangle terms. The original Morse filler has seven. Their difference has an explicit six-tetrahedron primitive:

\[
L=\mathsf G_Q(\bar H_M),\qquad
\bar H_M-H_{\mathrm{red}}=dL.
\]

All three chains and their signs are exported. This compares two actual fillers in one coefficient complex. It does not relabel the reduction-derived filler as an independently physical conductor trivialization.

## 9. Consequence for the physical comparison

The actual corrected Morse complex and the complete cellular coefficient model are now related by a support-preserving chain-homotopy equivalence. This closes their ordinary source-model comparison, including the normal factors and the occurrence correction.

The distinguished three-edge projection cannot serve as the Q-boundary functor: it fails the chain equation on mixed triangles. A physical source/refinement must instead specify its comparison with the genuine endpoint/short-boundary/fourteen-state-Q diagram, including any additional chosen homotopies.

The calculation does not assign a value to

\[
\Delta_J=H_{\mathrm{cond}}-e_Fh_{\mathrm{Morse}}.
\]

It supplies an explicit ordinary support model and its complete contraction against which physical frame admissibility can be tested. No numerical equality of residues, frozen signature dictionary, or elimination of the native exceptional kernel is used to claim the missing physical identification.

## 10. Reproduction and provenance

Run

```
python morse_pulledback_normal_support_equivalence_checker.py --output .
```

The checker is self-contained and uses only the Python standard library. It produces `morse_pulledback_normal_support_equivalence_certificate.json`, containing the full source and target bases, all differentials, the comparison, its inverse, its homotopy, both support filtrations, the two reduction pivot lists, the complete pulled-back blowdown kernel, the genuine Q representatives, and the named Morse chains.

It verified 51,044 exact identities. A clean execution in a second directory reproduced the certificate byte-for-byte. The matrix-payload SHA-256 is

```
e23a0acfca927bf3fcb14bc3be7be367b3670464cea2bfbf750605e47f2ffeef
```

Pinned Marici provenance: commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: complete pulled-back normal source, weighted flag differential, and independent occurrence correction.
- `research/voevodsky/check_d03_normalized_blowdown_counit.py`: the actual seven Morse triangles, six gallery flags, and three-term roof.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: original finite target and legal target-only normal localizations.
- `src/ledger/20260817-397 The Descended qJ Roof Is the Canonical D03 Yoneda Generator.md`: the thin generic-edge projection being tested, not an assumption of its validity.

Standard background: Stacks Project Tags 010V and 0111 (complexes and their quotient homology sequence), 0119 (chain homotopies), 0194 (simplicial chain functor). The specific equivalences here are proved by the exported matrices, not inferred from those general results.

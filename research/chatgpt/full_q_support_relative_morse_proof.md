# Full Q-support refinement of the relative Morse comparison

## Result and scope

The endpoint-relative source can be constructed without replacing the generic Q-support quotient by a scalar conductor readout. On the complete loaded Morse model, the construction retains all endpoint normal states, all mixed flags, the separate occurrence-Koszul factor, and all coefficient gradings. The corrected Morse disk has an explicit lift to this source.

The full Q quotient is also computed, not inferred from the flags consisting only of the top cell and long facets. Before the extra occurrence factor it has 393 generators. An explicit integral chain contraction reduces it to the original seven-state cellular Q complex. With the occurrence factor retained the corresponding counts are 786 and 14.

The raw corrected generic roof has a unit coefficient on the flag `[top,D03]`, but is a boundary in this full quotient. Its seven-triangle primitive is recovered exactly by the constructed contraction. A projection which discards mixed flags is not a chain map; one actual triangle gives its unit defect.

These are results about the explicit coefficient/support complexes. They do not identify the physical conductor–Morse class, do not establish a raw extraordinary realization, and do not infer a physical nonzero class from a unit matrix coefficient.

## 1. Coefficient ring and complete source

Use homological degrees: the differential lowers degree by one. The ring is

\[
B=\mathcal C[X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}]
 /(X_eX_o:e\in\{02,04,24\},\ o\in\{13,15,35\}).
\]

Here \(\mathcal C\) contains the three long occurrence coordinates, the independent long-normal coordinates, and the six short Rees parameters. Set

\[
I=(X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}),\qquad
\epsilon:B\longrightarrow\mathcal C=B/I.
\]

Retain the prescribed short-normal graph

\[
u_d=t_dX_d.
\]

The calculation does not invert an occurrence, normal, Rees parameter, or integer. It remains valid after the usual monodromy-unit localizations.

The expanded face poset is the stellar subdivision at \(\{03,13\}\). Its blowdown replaces the exceptional ray \(E\) by that pair. A generator of the loaded flag complex is

\[
(F_0<\cdots<F_k,H),\qquad H\subseteq\pi(F_0).
\]

Deleting the initial vertex of a flag multiplies by the occurrence monomial of \(\pi(F_1)\setminus\pi(F_0)\). The other flag deletions have signed unit coefficients. Normal deletion has coefficient \(u_d\) and the usual total-complex sign. This is the differential supplied by `check_d03_pabs_morse_pullback.rs`.

There are 581 flags and 1,169 loaded generators before the additional occurrence factor. Keep that factor separately:

\[
\widehat M=M\otimes_B K_{\mathrm{occ}}(X_{35}),\qquad
dh_{\mathrm{occ}}=X_{35}p.
\]

The complete corrected complex has 2,338 generators, in homological degree ranks

\[
(51,354,824,803,294,12).
\]

The native normal with label 35 is not identified with \(h_{\mathrm{occ}}\).

## 2. The actual support flag

Let \(\widehat V\) be the direct sum of the two singleton endpoint packets at

\[
V_+=\{13,15,35\},\qquad V_-=\{02,04,24\}.
\]

There are sixteen corrected generators at each endpoint, including the occurrence partners.

A flag lies entirely on the short boundary exactly when its initial face does. Indeed, the face-label sets are increasing, so a short label in the initial face persists through the flag. Define \(\widehat B\) by this condition, including every allowed normal subset and occurrence partner.

The actual inclusions are

\[
\widehat V\subset\widehat B\subset\widehat M,
\]

with numbers of indexed generators

\[
32\subset1552\subset2338.
\]

The complete differential preserves both subcomplexes. The natural quotient is

\[
\widehat Q=\widehat M/\widehat B.
\]

It retains flags starting at the top or a long facet even when their later vertices lie on the short boundary. A segment from the top to an endpoint is not supported solely at that endpoint.

This support condition is essential. Classifying the entire flag by its last vertex and deleting all mixed flags does not define the same quotient.

## 3. Endpoint-relative refinement preserving the full Q quotient

Let \(L_\pm=B\ell_\pm\) retain the endpoint occurrence degrees

\[
\deg_X\ell_+=-\epsilon_{13}-\epsilon_{15}-\epsilon_{35},\qquad
\deg_X\ell_-=-\epsilon_{02}-\epsilon_{04}-\epsilon_{24}.
\]

Write

\[
D_\partial=\mathcal C\ell_+\oplus\mathcal C\ell_-.
\]

For the endpoint coefficient extractions \(E_\pm\) on degree-zero unmarked endpoint states, define

\[
e=(\epsilon E_+,\epsilon E_-):\widehat M\longrightarrow D_\partial[0].
\]

This is a chain map: every incoming endpoint coefficient has positive conductor order after \(u_d=t_dX_d\). With independent short normal variables the same assertion would fail, which is why the graph assumption remains explicit.

Define, using the stated cone convention,

\[
\mathcal R_M=\operatorname{fib}(e).
\]

In coordinates this retains every old term of \(\widehat M\) and adds two conductor modules in homological degree minus one. The only added differential columns are

\[
v_+\longmapsto c_+,\qquad v_-\longmapsto c_-.
\]

Coefficients on \(c_\pm\) are reduced by \(\epsilon\); these terms are \(\mathcal C\)-modules, not free \(B\)-modules.

Similarly define \(\mathcal R_B\) and \(\mathcal R_V\) by restricting the same augmentation to the short-boundary and endpoint subcomplexes. Then

\[
\mathcal R_V\subset\mathcal R_B\subset\mathcal R_M
\]

has numbers of indexed summands \(34,1554,2340\), and

\[
\mathcal R_M/\mathcal R_B=\widehat Q
\]

literally. The two new conductor summands occur in both numerator and denominator and cancel in the quotient. This is not a replacement of Q by \(\mathcal C[1]\).

The projection \(p:\mathcal R_M\to\widehat M\) is a chain map. The map taking \(c_\pm\) to the corresponding basis of \(D_\partial\), and all other generators to zero, supplies the universal homotopy of \(ep\).

There is no identity-over-\(\widehat M\) lift of the entire unmodified source to \(\mathcal R_M\): each endpoint unit is a cycle with nonzero image under \(e\). Such a lift would nullhomotope this nonzero augmentation. This is why the full source has been replaced by its fibre rather than silently supplied with an impossible section.

The construction is the homotopy fibre of actual maps of the support diagram. It has not been identified with the reciprocal physical source or with an extraordinary pull–push.

## 4. The corrected Morse disk lifts

The supplied chains satisfy

\[
dH_M=q_J-X_{35}\widetilde\xi,\qquad
dq_J=X_{35}d\widetilde\xi.
\]

Set

\[
\widehat h_M=H_M\otimes p-\widetilde\xi\otimes h_{\mathrm{occ}},
\]

\[
\widehat q_J=q_J\otimes p-(d\widetilde\xi)\otimes h_{\mathrm{occ}}.
\]

The full source differential gives

\[
d\widehat h_M=\widehat q_J,\qquad d\widehat q_J=0.
\]

Both chains have positive homological degree, so the new endpoint-augmentation differential adds no term to them. The two-generator disk with generators \(h,q\), in degrees two and one, and differential \(dh=q\), therefore maps to \(\mathcal R_M\) by these exact chains.

This is a lift of the corrected Morse disk. It is not a map sending an exact chain to the previously detected nonzero scalar homology generator.

The raw roof is

\[
q_J=-[\varnothing,V_+]+[\varnothing,\{03\}]
     +X_{03}[\{03\},c],\qquad c=\{03,02,35\}.
\]

All three terms survive the actual Q quotient. Their starting faces are the top or D03. The gallery and the occurrence endpoint correction are in \(\widehat B\). Consequently

\[
d\overline H_M=\overline q_J
\]

inside \(\widehat Q\), while the coefficient of \([\varnothing,\{03\}]\) remains \(+1\).

A unit coordinate in an exact chain is not a nonzero homology class.

## 5. An explicit unit defect of the truncated projection

Consider the actual unmarked triangle

\[
\sigma=[\varnothing,\{03\},c].
\]

Its loaded boundary is

\[
d\sigma=X_{03}[\{03\},c]-[\varnothing,c]+[\varnothing,\{03\}].
\]

Let \(r\) keep only flags all of whose vertices are the top or a long facet, deleting every mixed flag. Then

\[
r(\sigma)=0,\qquad r(d\sigma)=[\varnothing,\{03\}]\ne0.
\]

Thus \(rd\ne dr\). This failure has coefficient one, independent of coefficient specialization. It already occurs on one unmarked triangle before any conductor, normal, or Rees evaluation.

The retained pure subposet has seven geometric flags and ten loaded generators before the occurrence factor. It is a subcomplex, but the indicated coordinate projection onto it is not a chain map from the full relative quotient.

Entry 397's argument that no two-simplex can bound the D03 edge after keeping only the long-facet subposet cannot be used as the homology calculation of this loaded quotient. Entry 109's earlier seven-triangle relative-boundary equation is consistent with the full computation. This audit does not claim that every possible framed physical Q observable is the above quotient homology; it identifies exactly which proposed projection fails.

## 6. Complete integral reduction of Q

Before the extra occurrence factor the actual quotient has 342 flags and 393 loaded states, in ranks

\[
(4,77,192,120).
\]

The checker performs 193 elementary cancellations along signed unit differential entries. In each pair the initial face and the normal subset agree. The calculation tracks the complete projection, inclusion, and homotopy rather than only the reduced differential.

After fixing the top orientation, the result is

\[
Q_{\mathrm{cell}}:
B\langle T,h_{03},h_{14},h_{25}\rangle
\xrightarrow{
\begin{pmatrix}
X_{03}&u_{03}&0&0\\
X_{14}&0&u_{14}&0\\
X_{25}&0&0&u_{25}
\end{pmatrix}}
B\langle p_{03},p_{14},p_{25}\rangle
\]

in homological degrees three and two.

The exported maps satisfy

\[
p_Qi_Q=1,\qquad d h_Q+h_Qd=1-i_Qp_Q,
\]

as well as both chain-map equations. Every coefficient is polynomial. Every entry of the projection and homotopy preserves the full occurrence/Rees multidegree. No regularity inference or parameter sampling is used to establish the contraction.

Tensoring all three maps with the independent occurrence Koszul factor gives

\[
\widehat Q\simeq
Q_{\mathrm{cell}}\otimes K_{\mathrm{occ}}(X_{35}).
\]

The unreduced quotient has 786 states; the reduced quotient has 14, with ranks \(3,7,4\) in degrees two, three, and four. The tensor homotopy retains the standard sign on the occurrence differential. It is checked on all 786 columns.

Therefore

\[
H_n(\widehat Q)=0\qquad(n<2).
\]

In particular, the actual degree-one corrected roof cannot be a primitive nonzero Q-homology class in this model.

The Q object is not acyclic. Before tensoring the occurrence factor its top cycle is

\[
\theta=\left(\prod_{d\in\{03,14,25\}}u_d\right)T
 -\sum_{d\in\{03,14,25\}}
 X_d\left(\prod_{e\ne d}u_e\right)h_d.
\]

The independent long coordinates imply

\[
H_3(Q_{\mathrm{cell}})=B\langle\theta\rangle,
\]

and \(H_2\) is the displayed matrix's cokernel. For the top-kernel assertion, reduce each row modulo its \(u_d\). Since \(X_d\) remains a nonzero divisor modulo \(u_d\), the top coefficient is divisible by each of the three independent \(u_d\), hence by their product. The other coefficients are then forced. This proof remains valid over the mixed-sheet ring because the long variables remain independent polynomial variables.

These degree-two and degree-three classes are distinct from the single degree-one barycentric edge.

## 7. The selected contraction recovers the Morse primitive

Let \(\overline h_M\) and \(\overline q_J\) denote the images of the corrected Morse chains in the full quotient. The exact reduction gives

\[
p_Q(\overline h_M)=0,\qquad p_Q(\overline q_J)=0,
\]

\[
h_Q(\overline q_J)=\overline h_M,\qquad h_Q(\overline h_M)=0.
\]

The equality is termwise: both sides of the first homotopy identity contain the same seven triangles with their original coefficients. There is no residual difference between these two chosen Q-nullhomotopies. The contraction is an explicit selected algebraic one; no uniqueness under the full physical frame is inferred from it.

The certificate exports all seven terms, the contraction matrix, and its evaluation. This is not an identification of the conductor nullhomotopy with the Morse homotopy.

## 8. Effect on the earlier endpoint-derived comparisons

The preceding endpoint maps \(m_\pm:\widehat M\to F\otimes L_\pm\) were nonzero connecting classes before endpoint relativization. Pull them back through \(p:\mathcal R_M\to\widehat M\).

They now have explicit homotopies. On the unmarked old endpoint set

\[
P(v_\pm)=-z\otimes\ell_\pm,
\]

and on the new conductor comparison summand set

\[
P(c_\pm)=1
\]

in the conductor component of degree zero of the corresponding fibre target. All other columns vanish. The full equation is

\[
dP+Pd=m_\partial p.
\]

On an old endpoint, the two conductor contributions cancel; on an incoming endpoint flag the remaining term is precisely the old \(-zE_\pm d\) coefficient. This is verified on every source column.

This is a homotopy of the explicit underlying fibre complexes. It uses the new conductor-comparison summands. An additional physical frame that forbids changing those comparison components would require its own admissible mapping complex; no framed physical vanishing is inferred here.

## 9. Verification and consequence

The standalone checker uses only Python's standard library and performs 37,807 exact checks. It reconstructs the complete corrected source, both support subcomplexes, the relative fibre and projection, the corrected Morse lift, the failed pure-flag projection, every matrix of the Q contraction, the occurrence-tensored identities, and the endpoint homotopies.

The contraction proves low-degree vanishing for arbitrary coefficients in the displayed ring, not merely tested parameter values. The normal graph assumption is needed for the endpoint augmentation; the Q contraction itself uses only the independent long coordinates.

The receiving support diagram and corrected Morse lift are now explicit. A physical comparison must specify whether its based Q datum is the retained chain and its nullhomotopy, or a class in a different degree/category. The unsupported assertion that the isolated D03 edge is already a nonzero class of the full quotient cannot serve as its normalization condition.

No physical value for \(\Delta_J\) is assigned by this calculation.

## Provenance

Repository inputs are read at commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61` of `andrey-kokoev/marici`:

- `research/voevodsky/check_d03_pabs_morse_pullback.rs`, blob `46624341c7956a8557249a54b117a88d43adfd62`: loaded flag differential and occurrence correction.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the normalization coefficient algebra.
- `src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md`: the original relative Morse boundary equation.
- `src/ledger/20260817-397 The Descended qJ Roof Is the Canonical D03 Yoneda Generator.md`: the pure-long-facet projection claim tested here, not assumed as a theorem of the loaded quotient.

General conventions: Stacks Project, Tags 014D (cones and termwise split sequences), 0A8H (Hom complexes and composition signs). The new finite matrices and the one-triangle counterexample are computed directly in the accompanying checker.

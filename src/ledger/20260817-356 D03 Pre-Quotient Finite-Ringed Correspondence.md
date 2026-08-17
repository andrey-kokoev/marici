# D03 Pre-Quotient Finite-Ringed Correspondence

## Result

The full \(D03\) pre-quotient carrier has an actual correspondence in the
category of finite ringed spaces. It retains the Morse top, generic and
special lower terms, the occurrence Cartier ideal, the complete target
Cech diagram, and both repeated-normal Tor grades. The remaining gap is the
mixed-variance Beck--Chevalley comparison, not existence of the
pre-quotient space or its two projections.

Let \(X=(P_{K_6}^{\rm or})^{\rm op}\) be the ringed target of entry 352.
Let \(G_{03}\) be the barycentric face poset of the \(D03,x_1\) stellar
blowup used by the exact P_abs checker. Its blowdown

\[
b:G_{03}\longrightarrow P_{K_6}^{\rm or}
\]

replaces the exceptional ray by \(\{D03,x_1\}\). The checker proves that
\(b\) is order preserving on every comparable pair and that pulling back
the complete 215-state coefficient diagram along \(b\) has square-zero
weighted differential.

Let \(I_{\rm occ}\) be the oriented two-point finite ringed interval with
constant structure ring \(R\) and rank-one coefficient transition

\[
K_{\rm occ}(x_3)=
[R\langle h_3\rangle\xrightarrow{x_3}R\langle p\rangle].
\]

Define

\[
Z_{03}^{\rm pre}=G_{03}\times I_{\rm occ},
\qquad
q=b\circ\operatorname{pr}_{G},
\qquad
p=\operatorname{pr}_{I}.
\]

Give \(Z_{03}^{\rm pre}\) the pulled-back ring
\(\mathcal O_Z=q^{-1}\mathcal O_X\). Then \(q\) is a morphism of ringed
finite spaces by the identity map
\(q^{-1}\mathcal O_X\to\mathcal O_Z\). The interval has constant ring \(R\),
so the structural maps \(R\to\mathcal O_Z\) make \(p\) a ringed morphism.
Both underlying order maps are literal projections composed with the
proved order-preserving blowdown.

## Perfect pre-quotient kernel

On \(Z_{03}^{\rm pre}\), take

\[
\mathcal K_{03}^{\rm pre}
=q^*\mathcal L^{\check C}
\mathbin{\widehat\otimes}
p^*K_{\rm occ}(x_3)
\mathbin{\widehat\otimes}
D_3,
\]

where

\[
D_3=K(u_3^\vee)\otimes K(u_3)
\]

is the repeated-normal derived self-intersection. Its quotient and excess
maps retain the primitive \(\operatorname{Tor}_0\) and
\(\operatorname{Tor}_1\) lines, with
\(\eta_{3,\mathrm{mix}}=(-q_3,-1)\). The first factor pulls back the whole
target diagram, hence does not discard any Cech lower or overlap term.

On the seven-triangle subcarrier the pulled-back differential forces

\[
dH_{\rm Morse}=q_J-x_3\widetilde\xi.
\]

Totalizing with the occurrence interval gives the exact pre-quotient
identity

\[
d(H_{\rm Morse}p-\widetilde\xi h_3)
=q_Jp-d\widetilde\xi\,h_3.
\]

Thus \(H_{\rm Morse}\), \(q_J\), the special lower term
\(\widetilde\xi\), and the principal ideal \((x_3)\) coexist in one
unlocalized ringed kernel. No evaluation of \(x_3^\vee x_3\) is extended
illegally to the \(R\)-valued generic terms, and neither \(x_3\) nor a
support normal is inverted.

## Exact boundary

This proves d_central_flip_prequotient_correspondence in the finite-ringed
category. It does not prove that the generic localization and special
Cartier/Gysin restrictions are the two faces of one extraordinary
base-change transformation. In particular it does not yet construct:

1. the Beck--Chevalley cell comparing the \(q^!\) restriction with the
   occurrence-ideal Gysin boundary;
2. preservation and computation of \(q^!\mathcal L^{\check C}\) on the
   required perfect/constructible subcategory;
3. the relative dualizing orientation and proper trace; or
4. the PC-purity comparison.

The next obligation is therefore
d_central_flip_projection_beck_chevalley. Only after it is proved may
the pre-quotient projections be promoted to the assembled central-flip
span used in the trace formula.

## Evidence

The exact checker
research/voevodsky/check_d03_pabs_morse_pullback.rs verifies:

- the 215-state target and its square-zero differential;
- blowup face census \((1,10,24,16)\);
- barycentric census \((51,194,240,96)\);
- order preservation of blowdown;
- the complete pulled-back loaded differential and \(d^2=0\);
- the seven-triangle identity and occurrence-Koszul totalization above.

The Tor factor and its primitive two grades are independently verified by
research/voevodsky/check_d03_unlocalized_road_flag_aw.rs.

Delegation run run-79bc4c417fea49ff96dda946ac110f24 terminated without a
result and is not used as evidence.

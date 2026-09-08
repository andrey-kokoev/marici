# Homogeneous Morse Q-fillings and their short-boundary attachment

## Computed result

For the complete corrected Morse source and its actual short-boundary quotient, the homotopy classes of fillings of the fixed Q-roof form a rank-two integral torsor in the multidegree of the supplied Morse chain. Both independent changes are detected by the actual short-boundary connecting map. Once the entire lower attachment is fixed, only one homogeneous chain-homotopy class of fillings remains.

The calculation constructs the three Q-variation chains, their eight-term short-boundary attachments, and every projection, inclusion, and contracting homotopy used below. It does not construct the independent physical conductor homotopy, identify the physical conductor–Morse class, or assert that every componentwise homotopy is admissible in a stronger unprovided physical frame.

## 1. Coefficients, support, and grading

Use homological degrees throughout: the differential lowers degree by one. Let

\[
\mathscr D=\{02,03,04,13,14,15,24,25,35\},
\quad
\mathscr S_+=\{13,15,35\},
\quad
\mathscr S_-=\{02,04,24\},
\quad
\mathscr L=\{03,14,25\}.
\]

The coefficient ring for this calculation is the unlocalized polynomial normalization ring

\[
B=\mathbb Z[X_d\ (d\in\mathscr D),\ t_s\ (s\in\mathscr S_+\cup\mathscr S_-),\ u_l\ (l\in\mathscr L)]
 /(X_eX_o:e\in\mathscr S_-,\ o\in\mathscr S_+).
\]

The six short-normal graph relations are \(u_s=t_sX_s\). The three long normals remain independent. All eighteen displayed variables have their own fine degree. No occurrence, normal, Rees parameter, or integer is inverted. Localizations at inhomogeneous monodromy units are not used in the multigraded calculation.

The source is the complete expanded loaded flag complex with the independent occurrence-Koszul factor retained:

\[
\widehat M=M\otimes K_{\mathrm{occ}}(X_{35}),
\qquad dh_{\mathrm{occ}}=X_{35}p.
\]

A state has the form \(g=(F_0<\cdots<F_k,H,\epsilon)\), with \(H\subseteq\pi(F_0)\) and \(\epsilon\in\{0,1\}\). The blowdown \(\pi\) replaces the exceptional ray by \(\{03,13\}\). Its homological degree and coefficient weight are

\[
|g|=k+|H|+\epsilon,
\]

\[
\operatorname{wt}(g)
=-\sum_{d\in\pi(F_0)}\operatorname{wt}(X_d)
+\sum_{d\in H}\operatorname{wt}(u_d)
+\epsilon\operatorname{wt}(X_{35}).
\]

The differential deletes flag vertices with the supplied lcm occurrence coefficient on deletion of the first vertex; other flag deletions have signed unit coefficients. It also deletes normal marks using \(u_d\), and includes the separate occurrence differential. The checker reconstructs all 2,338 states and verifies their full polynomial differential before extracting any homogeneous component.

The support subcomplexes are the same actual objects as in the preceding calculation:

\[
\widehat V\subset\widehat B\subset\widehat M,
\qquad
\widehat Q=\widehat M/\widehat B.
\]

A flag is in \(\widehat B\) precisely when its initial face contains a short label after blowdown. Mixed flags beginning at the top or a long facet are retained in \(\widehat Q\). The state counts are \(32\subset1552\subset2338\), with 786 Q-states.

The physical endpoint-relative construction previously added two conductor modules in degree minus one. Their coefficient lines have weights \(-\sum_{d\in\mathscr S_\pm}\operatorname{wt}(X_d)\). They have zero multidegree-zero component: the required complementary monomials contain short occurrence variables, which vanish in the conductor ring. Thus the homogeneous computation below applies equally to that endpoint-augmentation fibre. This observation does not replace derived conductor restriction by termwise substitution.

## 2. The complete polynomial filling module

The supplied corrected pair satisfies

\[
\widehat h_M=H_M\otimes p-\widetilde\xi\otimes h_{\mathrm{occ}},
\qquad
\widehat q_J=q_J\otimes p-(d\widetilde\xi)\otimes h_{\mathrm{occ}},
\qquad
 d\widehat h_M=\widehat q_J.
\]

After passage to the full Q quotient, denote the pair by \((\bar h_M,\bar q_J)\). Both have fine weight zero. The question here concerns a second filling \(h\in\widehat Q_2\) of this SAME fixed degree-one chain, so that \(dh=\bar q_J\). Two fillings are homotopic relative to their fixed boundary when their difference is the differential of a degree-three chain.

Choosing \(\bar h_M\) as reference identifies this set of homotopy classes with a torsor under \(H_2(\widehat Q)\). This statement concerns maps from a homogeneous free probe, or equivalently a based disk and its fixed boundary; it is not an identification with the whole physical mapping complex \(R\operatorname{Hom}(J,F_0)\).

The previously established contraction reduces \(\widehat Q\) to

\[
Q_{\mathrm{cell}}\otimes K_{\mathrm{occ}}(X_{35}),
\]

where \(Q_{\mathrm{cell}}\) has four upper generators \((T,h_{03},h_{14},h_{25})\), three lower generators \((p_{03},p_{14},p_{25})\), and differential

\[
A_Q=
\begin{pmatrix}
X_{03}&u_{03}&0&0\\
X_{14}&0&u_{14}&0\\
X_{25}&0&0&u_{25}
\end{pmatrix}.
\]

The new calculation retains all fourteen states and checks the complete degree-three-to-degree-two matrix:

\[
A_{\widehat Q}=
\begin{pmatrix}
X_{03}&u_{03}&0&0&X_{35}&0&0\\
X_{14}&0&u_{14}&0&0&X_{35}&0\\
X_{25}&0&0&u_{25}&0&0&X_{35}
\end{pmatrix}.
\]

Consequently

\[
H_2(\widehat Q)=\operatorname{coker}_B A_{\widehat Q}.
\]

Equivalently it is generated by the three unmarked long-facet states with the relations \(u_lp_l=0\), \(X_{35}p_l=0\), and \(X_{03}p_{03}+X_{14}p_{14}+X_{25}p_{25}=0\). This is the full polynomial presentation; the smaller integral result below follows by taking its exact homogeneous component, not by replacing parameters by sampled values.

## 3. The entire homogeneous component of the Morse data

Write \(C_{(0)}\) for the fine-weight-zero component of a complex \(C\). For any free state \(g\), the coefficient of a weight-zero vector has uniquely forced exponent vector \(-\operatorname{wt}(g)\). The state contributes if and only if those exponents are nonnegative and the monomial survives the mixed-sheet ideal.

This test is exhaustive in arbitrary polynomial degree. It is not a cutoff. Native normal marks cannot occur in this component because their positive Rees or long-normal weight would require a forbidden inverse coefficient. The separate occurrence partner does contribute on appropriate faces and is retained.

The complete integer complexes are:

| Complex | Degree 0 | Degree 1 | Degree 2 | Degree 3 | Total |
|---|---:|---:|---:|---:|---:|
| \(\widehat M_{(0)}\) | 40 | 199 | 264 | 108 | 611 |
| \(\widehat B_{(0)}\) | 36 | 125 | 96 | 12 | 269 |
| \(\widehat Q_{(0)}\) | 4 | 74 | 168 | 96 | 342 |
| \(\widehat V_{(0)}\) | 2 | 1 | 0 | 0 | 3 |

Every resulting integer differential is checked against the full polynomial differential, including the cases where a mixed-sheet monomial becomes zero.

In the reduced Q model, the weight-zero lower generators are

\[
\lambda_{03}=X_{03}p_{03},\qquad
\lambda_{14}=X_{14}p_{14},\qquad
\lambda_{25}=X_{25}p_{25}.
\]

The only upper generator of the same weight is \(T\), with

\[
dT=\lambda_{03}+\lambda_{14}+\lambda_{25}.
\]

Thus

\[
H_2(\widehat Q)_{(0)}
\cong\mathbb Z^3/\mathbb Z(1,1,1)
\cong\mathbb Z^2.
\]

There is no higher homology in this homogeneous Q component. The space of homogeneous fillings of the fixed roof therefore has a discrete rank-two torsor of components and no higher homotopy groups. This is a statement in the chain-homotopy model of the specified free probe.

Using the explicit polynomial inclusion from the reduced Q complex, define

\[
\zeta_l=i_Q(\lambda_l),\qquad l\in\{03,14,25\}.
\]

Each \(\zeta_l\) is an eight-term polynomial degree-two cycle in the full quotient. None has an endpoint-state component. All fillings are, modulo homotopy,

\[
\bar h_M+c_{03}\zeta_{03}+c_{14}\zeta_{14}+c_{25}\zeta_{25},
\qquad c_l\in\mathbb Z.
\]

The two independent coordinates are \((c_{03}-c_{25},c_{14}-c_{25})\). The checker exports a readout for these coordinates and verifies that it annihilates every degree-three boundary in the full homogeneous quotient. It evaluates the three variation generators to \((1,0),(0,1),(-1,-1)\).

The chosen Morse reference has coordinates \((0,0)\). These coordinates are relative to that reference; they are not numerical values assigned to a physical conductor class.

## 4. Compute the actual attachment, not only the Q difference

Lift each \(\zeta_l\) to the same labelled chains in \(\widehat M_{(0)}\). Its boundary is a short-boundary cycle

\[
\beta_l=d_{\widehat M}\widetilde\zeta_l\in\widehat B_{1,(0)}.
\]

All three \(\beta_l\) have eight nonzero labelled terms. They are exported with their original occurrence coefficients. This is the connecting map of the actual short exact sequence

\[
0\longrightarrow\widehat B_{(0)}
\longrightarrow\widehat M_{(0)}
\longrightarrow\widehat Q_{(0)}\longrightarrow0.
\]

The checker performs signed-unit integral cancellations and tracks complete projection, inclusion, and homotopy matrices. The results are

\[
H_1(\widehat B)_{(0)}=\mathbb Z^5,
\qquad
H_1(\widehat M)_{(0)}=\mathbb Z^3,
\]

\[
H_n(\widehat M)_{(0)}=0\ (n\ne1),
\qquad
H_n(\widehat B)_{(0)}=0\ (n\ne1).
\]

There are 304 unit cancellations for \(\widehat M_{(0)}\), 132 for \(\widehat B_{(0)}\), 170 for \(\widehat Q_{(0)}\), and one for the endpoint component. The residual differentials are literally zero. Thus these results include integral saturation, not just rational ranks or checks modulo selected primes.

In the explicitly exported five-element short-boundary homology basis, the attachment columns \((\beta_{03},\beta_{14},\beta_{25})\) are

\[
D_{\partial}=
\begin{pmatrix}
-1&1&0\\
1&0&-1\\
1&0&-1\\
-1&1&0\\
0&-1&1
\end{pmatrix}.
\]

Its kernel on \(\mathbb Z^3\) is exactly the diagonal \(\mathbb Z(1,1,1)\). A maximal rank-two minor is \(-1\). Therefore its induced map on \(H_2(\widehat Q)_{(0)}\) is injective with primitive image.

The inclusion from short-boundary to full-source homology is

\[
A_{BM}=
\begin{pmatrix}
0&-1&1&0&0\\
-1&0&0&1&0\\
1&1&0&0&1
\end{pmatrix}.
\]

It satisfies \(A_{BM}D_{\partial}=0\). An explicit unimodular change of basis has first columns \(\beta_{03},\beta_{14}\) and last columns the three inherited full-source generators. Its determinant is \(-1\). In this basis the attachment and inclusion become

\[
D'_{\partial}=
\begin{pmatrix}
1&0&-1\\
0&1&-1\\
0&0&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
A'_{BM}=
\begin{pmatrix}
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}.
\]

This gives the exact split sequence of integral groups

\[
0\longrightarrow\mathbb Z^2
\xrightarrow{\partial}\mathbb Z^5
\longrightarrow\mathbb Z^3\longrightarrow0.
\]

The split displayed here is a calculated basis choice, not a claimed canonical physical splitting.

At chain level, the relation among all three attachments retains a 72-term lower-support chain. With \(\widetilde T\) the lift of the reduced top generator, put

\[
W_B=d\widetilde T-(\widetilde\zeta_{03}+\widetilde\zeta_{14}+\widetilde\zeta_{25}).
\]

Then \(W_B\in\widehat B_{2,(0)}\) and

\[
dW_B=-(\beta_{03}+\beta_{14}+\beta_{25}).
\]

Every term is retained in the certificate. The diagonal relation is therefore accompanied by its actual lower chain correction.

## 5. Exact criterion for preserving the lower attachment

A variation with coefficient vector \((c_{03},c_{14},c_{25})\) changes the lower attachment, in the adapted basis, by

\[
(c_{03}-c_{25},\ c_{14}-c_{25},\ 0,0,0).
\]

The short-boundary attachment class remains unchanged if and only if

\[
c_{03}=c_{14}=c_{25}.
\]

Exactly these variations are already zero in the Q-filling torsor. Thus no nontrivial homogeneous Q-filling class preserves the complete short-boundary attachment even at homology level.

There is a stronger statement when comparing actual full-source fillings. If \(h'\) is a homogeneous degree-two chain in \(\widehat M\) with exactly

\[
dh'=d\widehat h_M=\widehat q_J,
\]

then \(y=h'-\widehat h_M\) is a homogeneous degree-two cycle. Let \(H_M\) denote the exported integer contracting homotopy of \(\widehat M_{(0)}\), with a different symbol from the source's named Morse chain when implementing this formula. Since the residual homology projection has only degree one,

\[
d\bigl(H_M(y)\bigr)=y.
\]

This is an explicit universal primitive for any such difference. Moreover, the residual component has no homology above degree one, so the nonempty homogeneous space of full fillings is contractible in this ordinary chain-homotopy model.

The selected contraction also evaluates the actual corrected roof to the original corrected Morse chain exactly. It does not produce an independently defined conductor filling.

## 6. What this establishes for the conductor–Morse problem

The previously fixed roof has a fully computed comparison test. A proposed conductor realization in the same model can be compared with the Morse reference as follows:

1. project its degree-two Q-difference to the three \(\lambda_l\) coefficients;
2. extract \((c_{03}-c_{25},c_{14}-c_{25})\);
3. compare its actual short-boundary correction with the matrix \(D_{\partial}\).

A nonzero pair necessarily changes the short-boundary attachment. A zero pair gives the same Q-filling homotopy class. If the full corrected boundary is identical, the full-source contraction supplies the higher comparison explicitly.

These are comparisons of a fixed based disk/free probe. They do not establish that the physical \(H_{\mathrm{cond}}\in\operatorname{Hom}^1(J,F_0)\) is such a filling. That identification requires the independent source and support-changing maps specified by the physical problem. Nor does this calculation establish that the componentwise primitive is permitted by every stronger endpoint, reciprocal, support, or filtration frame. Those requirements must be checked on the actual transport, not inferred from ordinary homology.

The nonzero native first-jet/Gysin class previously denoted \(\tau\) is not assigned to the two-integer torsor here. Its source, target, and weight are different. No equality with the physical \(\Delta_J\) is claimed.

## 7. Reproducibility and sources

Run:

```sh
python morse_q_filling_torsor_and_attachment_checker.py
```

The checker is standalone and uses only Python's standard library. It reconstructs and checks the preceding 2,338-state source and full-Q contraction, then verifies 10,895 new exact identities. It replays 37,807 earlier identities. The mathematical conclusions use the explicit contractions and unimodular matrices, not the number of assertions.

Repository provenance is fixed to commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61` of `andrey-kokoev/marici`:

- `research/voevodsky/check_d03_pabs_morse_pullback.rs`, blob `46624341c7956a8557249a54b117a88d43adfd62`: the loaded flag differential, seven-triangle Morse chain, and separate occurrence correction.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the coefficient algebra and conductor quotient.
- `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`: the retained support flag and seven-state cellular Q target.
- `src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md`: the original requirement for independently constructed conductor and Morse homotopies in a common mapping category.

General conventions:

- Stacks Project, [Hom complexes, Tag 0A8H](https://stacks.math.columbia.edu/tag/0A8H): homotopies, cohomology of mapping complexes, and composition signs.
- Stacks Project, [connecting homomorphism, Tag 0117](https://stacks.math.columbia.edu/tag/0117): the long exact homology sequence of the actual support short exact sequence.
- Stacks Project, [cones and termwise split sequences, Tag 014D](https://stacks.math.columbia.edu/tag/014D): endpoint-augmentation fibres and the corresponding chain constructions.

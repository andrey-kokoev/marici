# Coherent diagonal observability is independent of seam transversality

## The missing sector

Let
\[
D:L_P\oplus L_A\to L_I,
\qquad
D(x_P,x_A)=r_Px_P-r_Ax_A.
\]
The gluing margin controls only disagreement modes:
\[
(\ker D)^\perp.
\]
Its kernel is the coherent pullback. Therefore perfect transversality does not imply that a final Green observer detects coherent joint states.

After quotienting authorized gauge, write
\[
H_{\mathrm{joint}}
=
H_{\mathrm{coh}}\oplus H_{\mathrm{dis}},
\qquad
H_{\mathrm{coh}}=\ker D/G_D.
\]
The orthogonal splitting is a Hilbert control; in the form or Krein setting it must be replaced by the corresponding reduced decomposition.

## Fourth margin

Let
\[
J_{\mathrm{Green}}:H_{\mathrm{joint}}\to Z_{\mathrm{Green}}
\]
be the complete final boundary observer. Define
\[
\delta_{\mathrm{diag}}
=
\inf_{\substack{z\in H_{\mathrm{coh}}\\\|z\|=1}}
\|J_{\mathrm{Green}}z\|.
\]
Completion faithfulness now requires four separately typed bounds:

1. \(\delta_P>0\): arithmetic realization;
2. \(\delta_A>0\): analytic/Mellin realization;
3. \(\delta_{\mathrm{glue}}>0\): stable correction of disagreement;
4. \(\delta_{\mathrm{diag}}>0\): observation of exactly coherent joint states.

No one of these margins implies another.

## Block audit

Relative to
\[
H_{\mathrm{joint}}=H_{\mathrm{coh}}\oplus H_{\mathrm{dis}},
\]
the Green Gram operator is
\[
B_{\mathrm{Green}}
=
J_{\mathrm{Green}}^*J_{\mathrm{Green}}
=
\begin{pmatrix}
B_{cc}&B_{cd}\\
B_{dc}&B_{dd}
\end{pmatrix}.
\]

The diagonal margin is the lower bound of \(B_{cc}\) after authorized gauge reduction. The gluing margin is governed by \(D^*D\) on \(H_{\mathrm{dis}}\). The mixed blocks encode conversion between coherent and disagreement modes and cannot be inferred from either diagonal block.

A total lower bound requires a Schur-complement estimate. If \(B_{dd}\) is coercive, then coherent control is governed by
\[
B_{cc}-B_{cd}B_{dd}^{-1}B_{dc}.
\]
Thus even positive \(B_{cc}\) can be cancelled by mixed coupling. The final Green theorem needs either a direct assembled coercivity bound or separate diagonal, disagreement, and mixed-block estimates.

## Minimal hostile: coherent escape

Take
\[
L_P=L_A=\mathbb C,\qquad r_P=r_A=I.
\]
Then
\[
D(x,y)=x-y,
\]
and the coherent diagonal is
\[
\ker D=\{(x,x)\}.
\]
Both component channels are isometric, and \(D\) has a fixed positive singular value on the anti-diagonal.

At cutoff \(X\), define
\[
J_{\mathrm{Green},X}(x,x)=\varepsilon_Xx,
\qquad
\varepsilon_X\to0.
\]
All arithmetic, analytic, and gluing margins remain fixed while
\[
\delta_{\mathrm{diag},X}=\varepsilon_X\to0.
\]
The coherent state becomes asymptotically invisible without any arithmetic-analytic mismatch.

## Converse hostile: disagreement escape

Let the Green observer be an isometry on the coherent diagonal while the two incidence images approach tangency. Then \(\delta_{\mathrm{diag}}=1\) but
\[
\delta_{\mathrm{glue}}\to0.
\]
A strong common-mode observer does not repair unstable seam correction.

## Birman–Schwinger interpretation

An eigenvalue-one collision can arise in different typed sectors:

- **disagreement collision:** an arithmetic-analytic mismatch is no longer dominated;
- **coherent collision:** an exactly matched joint state loses boundary-defect amplitude;
- **mixed collision:** coherent and disagreement components cancel through off-diagonal Green coupling.

Therefore the residual operator must be block-classified before its gap is identified with any one margin.

Let \(P_c\) and \(P_d\) be the coherent and disagreement projections. Audit
\[
R_{cc}=P_cRP_c,\quad
R_{dd}=P_dRP_d,\quad
R_{cd}=P_cRP_d,\quad
R_{dc}=P_dRP_c.
\]
Only a source-derived statement that \(R\) acts purely in the disagreement sector would identify the Birman–Schwinger gap with \(\delta_{\mathrm{glue}}\). Otherwise \(\delta_{\mathrm{diag}}\) and mixed control are indispensable.

## Interaction-net normal-form interface

The reported SCC finite registry supplies the correct domain invariant: typed normal-form classes with retained boundary interfaces. Determinant/Schur, quadratic, context, optics, and coherent-loop values are projections, not the class itself.

This matches the four-margin audit. A coarse optics projection may detect disagreement while forgetting a coherent boundary interface. The combined separating family should be used to define \(J_{\mathrm{Green}}\), with arithmetic-to-analytic incidence and moving-seam transport added as typed atoms and rewrite witnesses.

Equality of coarse projections must never identify enriched coherent states before the diagonal observer is tested.

## Revised completion theorem target

On each compact \(s\)-set and uniformly in cutoff:

1. arithmetic and analytic restricted limits realize their bounded-energy shadows;
2. \(D\) has a positive lower bound on disagreement modes;
3. \(J_{\mathrm{Green}}\) has a positive lower bound on coherent modes modulo gauge;
4. mixed Green blocks satisfy a Schur-complement bound;
5. the residual/Birman–Schwinger operator is sector-classified;
6. the assembled lower bound survives completion.

The first possible failure then has a precise type: component realization, seam transversality, coherent observation, or mixed cancellation.

## Next calculation

Construct finite-cutoff projections onto \(\ker D_X(s)\) and its reduced complement. Compute:

- the least positive singular value of \(D_X(s)\);
- the least singular value of \(J_{\mathrm{Green},X}(s)|_{\ker D_X(s)}\);
- the norm of the mixed Green block;
- the corresponding Schur-complement margin.

This four-block calculation determines whether the assembled Green residual controls disagreement modes, coherent modes, or both.

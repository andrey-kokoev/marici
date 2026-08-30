# Minimal cross-system pairing theorem for opposite logical charges

## Question

What is the smallest authorized interaction that can annihilate opposite Fredholm defects in two completed systems, and when is that interaction unique?

## Claim boundary

Let

\[
A_1:H_1\to K_1,\qquad A_2:H_2\to K_2
\]

be bounded Fredholm comparison operators. Assume the minimal opposite-charge case:

\[
\ker A_1=\operatorname{span}\{k\},\qquad
\operatorname{coker}A_1=0,
\]

\[
\ker A_2=0,\qquad
\operatorname{coker}A_2=\operatorname{span}\{[c]\}.
\]

Thus \(\operatorname{ind}A_1=+1\) and \(\operatorname{ind}A_2=-1\). Consider the triangular coupled system

\[
\mathcal A_C
=
\begin{pmatrix}
A_1&0\\
C&A_2
\end{pmatrix}
:H_1\oplus H_2\to K_1\oplus K_2.
\]

Let

\[
\bar C:\ker A_1\to\operatorname{coker}A_2
\]

be the induced defect map \(\bar C(k)=[Ck]\). Then

\[
\mathcal A_C\text{ is invertible}
\quad\Longleftrightarrow\quad
\bar C\ne0.
\]

The proof is exact. From \(A_1x_1=0\), a kernel vector has \(x_1=ak\). The second equation can be solved only if \(a[Ck]=0\) in the cokernel of \(A_2\). Nonzero \([Ck]\) forces \(a=0\), and injectivity of \(A_2\) then forces \(x_2=0\). Conversely, surjectivity of \(A_1\) solves the first output, and the free kernel coefficient \(a) supplies exactly the missing cokernel coordinate of the second output.

Thus one directed cross-arrow pairs the excess input mode of system 1 with the missing output mode of system 2. No second arrow is needed for algebraic invertibility.

### Minimality

The correction must have rank at least one because it must act nontrivially on the one-dimensional defect quotient. Rank one suffices. More generally, if the total kernel and cokernel have common finite dimension \(m\), a first-order finite-rank repair requires an isomorphism

\[
\bar T:\ker(A_1\oplus A_2)
\xrightarrow{\cong}
\operatorname{coker}(A_1\oplus A_2),
\]

so rank at least \(m\) is necessary and rank \(m\) is sufficient.

For a general perturbation, the exact criterion is invertibility of the Feshbach or Schur defect map after the invertible bulk complement has been eliminated. The leading map \(\Pi_{\mathrm{coker}}T|_{\ker}\) is the generic first-order term. If it vanishes, a higher-order path through bulk modes may still repair the defect, but that is a different, weaker mechanism and must be audited through the full Schur complement.

### Dagger completion

If the two-system realization must be self-adjoint or dagger-compatible, the one-way arrow is insufficient as a realization law. One then uses

\[
\mathcal D_C
=
\begin{pmatrix}
D_1&C^*\\
C&D_2
\end{pmatrix}.
\]

The reverse arrow is not a second independent datum; it is fixed by the dagger once \(C\) and the source/target metrics are fixed. This distinction matters:

- invertibility requires defect pairing;
- self-adjoint realizability additionally requires the authorized adjoint.

A fitted metric that is chosen merely to make the reverse arrow equal to \(C^*\) does not supply source authority.

### Symmetry selection rule

Let a symmetry group act on the defect spaces. An equivariant pairing exists only in the relevant intertwiner space:

\[
\bar C\in
\operatorname{Hom}_G(\ker A_1,\operatorname{coker}A_2).
\]

For one-dimensional Fourier characters, this space vanishes unless the characters match. With an antiunitary or bilinear pairing, the permitted target may instead carry the conjugate or dual character; that choice must come from the declared coefficient lens.

Therefore opposite scalar indices are insufficient. The defects must have compatible typed character. If their characters differ, annihilating them requires symmetry breaking or an additional carrier that supplies the character difference.

### Uniqueness and the residual torsor

When both defect spaces are one-dimensional and symmetry-compatible, all nonzero defect pairings differ by a scalar:

\[
\bar C(k)=\gamma[c],\qquad \gamma\ne0.
\]

Algebraic closure determines only that \(\gamma\) is nonzero. It does not determine magnitude, phase, sign, topology, or physical implementation.

The repair is unique only after source data fix:

- a generator or vacuum frame for the kernel line;
- a generator or orientation frame for the cokernel line;
- the normalization of their incidence;
- the dagger or reality law.

Without those data, admissible repairs form a \(\mathbb C^\times\) torsor, or a smaller \(\mathbb R^\times\), positive, or phase torsor after imposing reality and metric conditions.

### Conditioning

Let \(S_1\) be a bounded right inverse for \(A_1\) on its complement and let \(S_2\) be the inverse of \(A_2\) onto its closed range. Uniform invertibility of \(\mathcal A_C\) requires both bulk inverse bounds and a lower bound on the defect pairing:

\[
|\gamma_X|\ge\gamma_0>0.
\]

If \(\gamma_X\to0\), every finite coupled system may be invertible while the completed inverse norm diverges. This is the finite-index version of the tiny-tail conditioning obstruction.

Because the defect is finite-dimensional, a rank-one compact arrow can repair it. This does not contradict the compact-tail no-gap theorem: compact repair works only after essential approximate kernels have already been excluded.

### Interpretation for reciprocal tails

The two reciprocal systems should be audited for:

1. which one carries the excess kernel mode;
2. which one carries the missing boundary output;
3. the Fourier or sheet character of each defect;
4. whether a source-derived arrow maps the kernel generator to the cokernel generator;
5. whether its coefficient is uniformly nonzero through completion;
6. whether the dagger forces the reverse arrow.

If the modular tails merely provide two defect vectors but no incidence between them, the charge cancellation is only numerical. If theta/Tate transport supplies \(C\), the interaction converts the two defects into an invertible combined mate.

### Immediate prediction for the missing Green–Ward arrow

The reverse source incidence isolated by arrow deletion has exactly the required variance: it should map the Green-side hidden boundary mode into the Ward-side missing source port. In the unit-defect case, the entire topological problem reduces to one matrix coefficient

\[
\gamma_X
=
\langle c_X^*,R_Xk_X\rangle.
\]

The first finite gate is \(\gamma_X\ne0\). The completion gate is \(\inf_X|\gamma_X|>0\). Character mismatch forces \(\gamma_X=0\) before any analytic estimate.

## Disposition

The minimal two-system closure is a rank-one directed defect pairing, not an extra observable and not necessarily a symmetric pair of arrows. Opposite indices become genuinely cancellable only when a source-authorized intertwiner sends the kernel line of one system onto the cokernel line of the other.

This reduces the active search to a scalar-valued but pre-scalarization incidence coefficient \(\gamma_X\) defined on typed defect lines. Its nonvanishing decides finite closure; its uniform lower bound decides completion; its phase and normalization expose the remaining source-reference torsor. A dagger-compatible realization may then add the adjoint arrow without introducing a second free constructor.
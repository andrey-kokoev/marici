# Euler-weight compactness reduces to bounded Green-normalized unweighted synthesis

## Forced factorization

On the reduced Green support, factor the arithmetic synthesis by grade:
\[
U_s=S_sD_E,
\]
where \(S_s\) is the unweighted typed boundary synthesis and \(D_E\) is diagonal on prime-power labels:
\[
D_Ee_{p,k}=w_{p,k}e_{p,k},
\qquad
w_{p,k}=\frac1k p^{-k/2}.
\]

Let \(B_s^{\dagger/2}\) denote the inverse square-root geometry only on the authorized reduced Green support. Define
\[
A_s=B_s^{\dagger/2}S_s,
\qquad
T_s=B_s^{\dagger/2}U_s=A_sD_E.
\]

The decisive source estimate is
\[
\|A_s c\|_{\mathcal H_s^{\mathrm{red}}}
\le C_C\|c\|_{\ell^2(\mathcal I)}
\]
uniformly for \(s\) in each compact parameter set \(C\), with cutoff and Real compatibility. If this holds, compactness comes from the already forced Euler diagonal:
\[
D_E\ \text{compact}
\quad\Longrightarrow\quad
T_s=A_sD_E\ \text{compact},
\]
and hence
\[
K_s=T_sT_s^*
\]
is compact.

This converts the Fredholm gate from an abstract compact-embedding request into one explicit Green graph-norm domination inequality for unweighted synthesis.

## Why the Euler diagonal is compact

Along any enumeration escaping finite subsets of the prime-power label set,
\[
w_{p,k}\longrightarrow0.
\]
A diagonal operator on \(\ell^2\) is compact exactly when its diagonal entries vanish at infinity. Therefore \(D_E\) is compact.

At finite cutoff \(X\), let \(P_X\) retain finitely many labels. Then
\[
\|D_E(I-P_X)\|
=
\sup_{(p,k)\notin X}|w_{p,k}|
\longrightarrow0.
\]
If \(A_s\) is uniformly bounded on a compact parameter patch,
\[
\sup_{s\in C}\|T_s(I-P_X)\|
\le
C_C\|D_E(I-P_X)\|
\longrightarrow0.
\]
Thus the factorization gives uniform tail-operator norm decay, not merely columnwise decay.

## Exact grade ideals

For fixed grade \(k\), the diagonal singular values are
\[
w_{p,k}=k^{-1}p^{-k/2}.
\]
Its Schatten \(q\)-sum is
\[
\sum_p |w_{p,k}|^q
=
k^{-q}\sum_p p^{-kq/2}.
\]
The prime sum converges exactly when
\[
\frac{kq}{2}>1.
\]

Therefore:

- primitive grade \(k=1\):
  \[
  D_1\in\mathcal S_q\quad(q>2),
  \qquad
  D_1\notin\mathcal S_2;
  \]
- square grade \(k=2\):
  \[
  D_2\in\mathcal S_q\quad(q>1),
  \qquad
  D_2\in\mathcal S_2;
  \]
- connected grades \(k\ge3\):
  \[
  D_k\in\mathcal S_1.
  \]

These are the primitive, square, and connected ideals already demanded by the typed completion. The asymmetry is not a defect; it explains why low grades require relative determinant/counterterm treatment while the connected tail is trace class.

## What bounded multiplication preserves

If \(A_s\) is bounded, then
\[
A_sD_k\in\mathcal S_q
\]
whenever \(D_k\in\mathcal S_q\), with
\[
\|A_sD_k\|_{\mathcal S_q}
\le
\|A_s\|\|D_k\|_{\mathcal S_q}.
\]
Thus:

- primitive normalized synthesis is compact and lies in every \(\mathcal S_q\), \(q>2\), but not automatically Hilbert–Schmidt;
- square normalized synthesis is Hilbert–Schmidt;
- connected normalized synthesis is trace class.

No stronger ideal may be claimed unless \(A_s\) supplies additional smoothing.

## Mandatory column-decay hostile

Column norms tending to zero do not imply compactness for an arbitrary synthesis operator. Let
\[
H=\bigoplus_{n\ge1}\mathbb C^n
\]
and let \(P_n\) be the orthogonal projection onto the \(n\)-th block. Enumerate an orthonormal basis blockwise and define an operator whose columns within the \(n\)-th block each have norm \(n^{-1/2}\), but all map coherently onto a fixed unit vector for that block. Every individual column norm tends to zero, while each block operator has norm \(1\). The tail operator norm therefore does not vanish, so the operator is not compact.

Equivalently, vanishing images of basis vectors is necessary but not sufficient for compactness.

The accepted evidence must be one of:

1. a bounded-times-compact factorization \(T_s=A_sD_E\);
2. uniform finite-rank approximation;
3. direct uniform tail-operator norm decay.

A columnwise summability shadow alone is rejected.

## Source inequality in form language

The boundedness of \(A_s\) is equivalent to
\[
\|B_s^{\dagger/2}S_sc\|^2
\le
C_C^2\|c\|^2.
\]
Without writing a pseudoinverse on the unreduced space, the source-safe version is a dual Green-form estimate:
\[
|\langle S_sc,h\rangle|^2
\le
C_C^2\|c\|^2\,b_s[h,h]
\]
for every reduced test vector \(h\), uniformly for \(s\in C\).

This is the graph-norm domination theorem to prove from complete boundary incidence. It must include every typed channel before reduction:

- primitive current;
- square current;
- connected tail;
- seam and endpoint;
- archimedean reservoir;
- reciprocal sheet.

If any channel is omitted, boundedness of the projected synthesis does not authorize compactness of the complete RH pencil.

## Cutoff and reciprocal naturality

The factorization must commute with cutoff:
\[
\iota_{X,Y}S_{X,s}=S_{Y,s}j_{X,Y},
\qquad
j_{X,Y}D_{E,X}=D_{E,Y}j_{X,Y}.
\]
Real transport must satisfy the conjugate counterpart. These identities make compactness and Schatten classification source-natural rather than basis artifacts.

## Consequence for the obstruction tower

The Fredholm-discreteness gate now has a sharply divided status:

- **Euler compact factor:** proved formally from \(w_{p,k}\to0\);
- **grade Schatten thresholds:** proved by prime summability;
- **complete normalized unweighted synthesis bound:** missing source estimate.

Hence the first new analytic target is not another Euler sum. It is:

> prove uniform compact-local Green graph-norm domination of the complete unweighted boundary synthesis \(S_s\).

Once this holds after stable radical reduction, compactness of the normalized arithmetic action and finite algebraic multiplicity near \(1\) follow from the forced Euler factorization.

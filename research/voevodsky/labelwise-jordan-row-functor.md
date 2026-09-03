# Labelwise Jordan rows and the order of the two limits

## Question

Which finite-cutoff construction survives source refinement without imposing positivity too early?

## Claim boundary

The labelwise row construction preserves the exact finite quadratic form and cutoff provenance. Convergence, tail control, and the global contraction remain open.

## Nonfunctorial aggregate splitting

For self-adjoint labelled prime terms \(q_nJ_n\), taking positive and negative parts after forming

\[
T_N=\sum_{n\leq N}q_nJ_n
\]

is not compatible with cutoff extension. Spectral subspaces of \(T_N\) can rotate when the next term is added. In particular,

\[
(S+T)_+\neq S_++T_+
\]

in general.

The checker uses

\[
S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
T=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Since \((S+T)^2=2I\), the aggregate positive part differs exactly from the sum of labelwise positive parts.

## Functorial repair

Split each labelled term first:

\[
J_n=J_n^+-J_n^-.
\]

Define provenance-preserving rows

\[
A_N=\bigoplus_{n\leq N}\sqrt{q_n}(J_n^+)^{1/2},
\qquad
B_N=\bigoplus_{n\leq N}\sqrt{q_n}(J_n^-)^{1/2}.
\]

Then

\[
\sum_{n\leq N}q_n\langle f,J_nf\rangle
=
\|A_Nf\|^2-\|B_Nf\|^2,
\]

and \(N\to N+1\) appends coordinates rather than rotating earlier ones.

## Correct order of limits

Arithmetic cutoff \(N\) constructs the source. Observer packet \(I\) restricts positivity. They cannot be identified.

1. Complete labelled rows \(A_N,B_N\) with explicit tail control.
2. Combine endpoint, gamma, and prime rows into global \(A,B\).
3. Prove \(\ker A\subseteq\ker B\), defining \(C(Af)=Bf\).
4. Test \(\|C\|\leq1\) on every finite observer span \(V_I\).

Partial forms at fixed \(N\) need not be positive. Requiring a contraction at every arithmetic cutoff would assert more than completed positivity and can reject the intended cross-sector cancellation.

## Tail-margin gate

A mixed finite computation can certify a global observer packet only when the omitted tail is bounded below its smallest computed eigenvalue margin. A positive truncated eigenvalue without such a tail estimate is not stable evidence.

## Disposition

The opposed limits mean more than covariance versus contravariance: they prescribe a noncommuting order of operations. Preserve labelled source provenance through direct completion; apply Jordan/Douglas order structure only to the globally coupled object; then restrict to finite observer packets. Aggregate finite-cutoff spectral splitting destroys the transition maps needed for this passage.

## Verification

- `research/voevodsky/labelwise-jordan-row-functor-v1.json`
- `research/voevodsky/checkers/check_labelwise_jordan_row_functor.py`
- `research/voevodsky/results/labelwise_jordan_row_functor.json`

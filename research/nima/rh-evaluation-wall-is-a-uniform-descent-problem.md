# RH evaluation wall is a uniform descent problem

## Result

The bordered evaluation wall has an exact finite algebraic criterion.

Let \(M_X(z)\) encode all source-derived state equations together with the scalar Evans-zero condition at cutoff \(X\). Let \(R_X(z)\) be the full sum-carrier port. The wall lifts scalar zero to carrier zero exactly when

\[
\ker M_X(z)\subseteq\ker R_X(z).
\]

In finite dimensions, this is equivalent to a factorization

\[
R_X(z)=L_X(z)M_X(z).
\]

The factor \(L_X\) is the evaluation-wall certificate. It expresses the full carrier residual as a consequence of the typed bordered equations.

## Smallest hostile

Take

\[
M=(1,0),
\qquad
R=(0,1).
\]

The vector \((0,1)\) satisfies the scalar-zero equation but has nonzero carrier residual. This is the smallest unexplained defect state.

Graph positivity cannot repair it because the failure is one of incidence: the bordered equations simply do not observe the second carrier direction.

## Completion gate

Finite kernel inclusion is insufficient. For

\[
M_N=
\begin{pmatrix}
1&0\\
0&1/N
\end{pmatrix},
\qquad
R_N=I,
\]

every finite \(M_N\) is injective, hence the kernel condition holds. But any factorization \(R_N=L_NM_N\) has norm at least \(N\).

The evaluation lift disappears at completion.

Therefore the completed wall requires a cutoff-independent estimate

\[
\|R_Xv\|\le C\|M_Xv\|
\]

in the source-selected graph topology.

## Typed defect alternative

The carrier port need not vanish if the residual lands in a declared defect object \(D_X\). Then the correct condition is factorization through the pair

\[
(M_X,D_X).
\]

Every surviving null direction must receive an explicit type and a source law. Naming the entire unexplained kernel as a defect is not a repair.

## Categorical interpretation

The +1 wall is a descent morphism. It proves that the carrier-sum observation descends through the quotient imposed by the bordered source equations.

The finite factorization establishes algebraic descent. The uniform bound establishes continuous descent through completion.

This connects the RH frontier directly to Marici's distinction-preserving completion theorem: equality after scalar projection does not authorize an operator-valued lift unless the relevant kernel and continuity obligations are satisfied.

## DPC verdict

Candidate: positive graph plus scalar endpoint equation.

Verdict: rejected by the finite dimension obstruction.

Candidate: cutoffwise bordered injectivity.

Verdict: rejected by the collapsing singular-value family.

Surviving candidate: a source-derived bordered operator \(M_X\), sum-carrier port \(R_X\), and uniformly bounded factorization \(R_X=L_XM_X\), possibly with separately typed defect channels.

## Immediate calculation

For the first finite seam graph:

1. assemble the state, seam, primitive, square, archimedean, and scalar endpoint rows into \(M_X\);
2. compute a basis for \(\ker M_X\);
3. apply \(R_X\) to every basis vector;
4. classify every nonzero residual by a predeclared defect type;
5. compute the sharp factorization norm.

One unexplained residual closes the wall. Growing factorization norms close completion stability.

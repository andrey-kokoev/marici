# 2359 — One Soft Occurrence Produces a Maximal-Parabolic Coefficient Obstruction

## Question

Entries 2339 and 2347 identify tangent source closures on total-energy and
component-soft support.  Does tangent Gauss--Manin transport remain
contextually faithful on each retained closure?

For each supported closure, generate the associative algebra of its two
tangent connection matrices in the source-cyclic basis.  Do not use the
normal connection direction.

## Three irreducible supports

At the tested fibers over \(\mathbf F_{32003}\), three closures generate their
full matrix algebras:

\[
\begin{array}{c|c|c}
\text{support}&\text{module rank}&\dim\mathcal A\\ \hline
E_T=0&7&49=7^2\\
X_2=0&20&400=20^2\\
X_3=0&24&576=24^2.
\end{array}
\]

Thus any nonzero dual readout is cyclic on each of these tested tangent
systems.

## The \(X_1\)-soft obstruction

At \(X_1=0\), the rank-twenty closure instead generates

\[
\boxed{\dim\mathcal A_{X_1}=336<400.}
\]

This signature replicates at three fibers over \(\mathbf F_{32003}\) and at
one fiber over the independent prime \(\mathbf F_{31991}\).

The dimension alone is not used to infer a module.  Compute the radical of
the trace pairing

\[
(A,B)\longmapsto\operatorname{tr}(AB)
\]

on the generated algebra.  Exact reduction gives

\[
\dim\operatorname{rad}_{\rm tr}\mathcal A=64.
\]

The span of the images of those radical matrices is a sixteen-dimensional
subspace \(W_{16}\), and both tangent generators preserve it with zero
containment failures.  Since

\[
336=16^2+16\cdot4+4^2,
\]

the generated algebra is the full maximal parabolic for

\[
\boxed{
0\longrightarrow W_{16}
\longrightarrow M_{20}^{X_1\text{-soft}}
\longrightarrow Q_4
\longrightarrow0.
}
\]

This is the first supported coefficient obstruction in the present
interacting contextual-faithfulness audit.  It lies on an existing soft
Carrier divisor and therefore does not falsify H2 at carrier level.

## Physical recovery gate

For the full parabolic above, a dual covector is cyclic precisely when its
restriction to \(W_{16}\) is nonzero.  Covectors in

\[
W_{16}^{\perp}
\]

see only the four-dimensional quotient orbit.  Therefore generic
nonvanishing of the physical period is no longer sufficient.  The next exact
test is

\[
\boxed{
\lambda_{\rm BD}|_{W_{16}}\stackrel?\ne0.
}
\]

The source-normalized physical relative cycle must determine this pairing;
it may not be replaced by a convenient finite-field covector.

## Scope

The result concerns specialized tangent connection algebras.  It does not
construct the soft nearby-cycle object, integral lattice, or physical
pairing.  Entry 2354 shows that the corresponding occurrence-transported
soft source remains natural; the parabolic flag must be transported with it.

## Artifacts

- `research/benincasa/check_rank26_tangent_support_algebra.py`
- `research/benincasa/rank26-tangent-support-algebra.json`

Sequence claim: `seqclaim-3f78535562e34e85d5f10232`.

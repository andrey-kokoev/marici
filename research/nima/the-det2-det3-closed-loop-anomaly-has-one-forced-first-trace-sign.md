# The det2-det3 closed-loop anomaly has one forced first-trace sign

## Regularized determinant conventions

For a finite-rank operator \(T\), use

\[
\det_2(I+T)=\det(I+T)e^{-\operatorname{Tr}T}
\]

and

\[
\det_3(I+T)
=\det(I+T)
\exp\left(-\operatorname{Tr}T+
\frac12\operatorname{Tr}T^2\right).
\]

These formulas fix the anomaly signs; they are not adjustable normalizations.

## Bare Euler block

For the prime-loop operator \(L\), substitute \(T=-L\):

\[
\det_3(I-L)
=
\det(I-L)
\exp\left(
\operatorname{Tr}L+
\frac12\operatorname{Tr}L^2
\right).
\]

Hence

\[
\det(I-L)^{-1}
=
\exp\left(
\operatorname{Tr}L+
\frac12\operatorname{Tr}L^2
\right)
\det_3(I-L)^{-1}.
\]

The primitive and square Euler currents occur exactly once as the two removed
cumulants.  Connected grades occur in the order-three determinant.

## Relative closed-loop block

For the Schur return

\[
K_{\rm rel}=A_0^{-1}B^\dagger D_0^{-1}B,
\]

the finite-cutoff cone identity contains \(\det(I-K_{\rm rel})\).  Its
order-two representation is

\[
\det(I-K_{\rm rel})
=
\det_2(I-K_{\rm rel})
\exp\left(-\operatorname{Tr}K_{\rm rel}\right).
\]

Therefore the relative first-trace anomaly enters with a minus sign.

## Combined finite-cutoff section

After removing the open boundary factor \(\det D_0\), the normalized
closed-loop section is

\[
\begin{aligned}
\mathfrak D_X(s)
={}&
\exp\left(
\operatorname{Tr}L_X+
\frac12\operatorname{Tr}L_X^2
-\operatorname{Tr}K_{{\rm rel},X}
\right)\\
&\times
\det_3(I-L_X)^{-1}
\det_2(I-K_{{\rm rel},X}).
\end{aligned}
\]

This is the unique scalar expression compatible with both regularization
conventions and the Schur determinant.

## No-double-counting rule

The traces have different sources:

- \(\operatorname{Tr}L_X\) is the primitive open Euler current;
- \(\frac12\operatorname{Tr}L_X^2\) is the square open Euler current;
- \(\operatorname{Tr}K_{{\rm rel},X}\) is the first closed-loop excursion
  through incidence, boundary propagation, and return.

The relative trace may cancel a boundary contribution only through a proved
trace identity.  It must not be relabelled as another primitive or square
Euler term merely because both are scalar traces.

## Exact anomaly target

Let \(a_{\partial,X}(s)\) denote the logarithm of the independently constructed
boundary and archimedean determinant-line section.  The remaining finite
anomaly is

\[
\mathcal A_X(s)
=
\operatorname{Tr}L_X(s)
+
\frac12\operatorname{Tr}L_X(s)^2
-
\operatorname{Tr}K_{{\rm rel},X}(s)
+a_{\partial,X}(s).
\]

G4 requires a source calculation showing that \(\mathcal A_X\) converges to
the logarithm of a holomorphic nowhere-zero unit on the open strip.  A bounded
or reciprocal scalar is insufficient: periods around zeros must also vanish
so that the logarithm glues globally.

## Reciprocal check

Reciprocal covariance gives

\[
K_{{\rm rel},-}(s)
=
\mathscr R_EK_{{\rm rel},+}(1-s)\mathscr R_E^{-1}.
\]

Where the trace is defined,

\[
\operatorname{Tr}K_{{\rm rel},-}(s)
=
\operatorname{Tr}K_{{\rm rel},+}(1-s).
\]

Thus the forced negative anomaly is compatible with the reciprocal chart
gluing.  This establishes covariance, not cancellation.

## Disposition

The det2/det3 anomaly bookkeeping is now fixed without double counting.  The
remaining calculation is a concrete source trace identity for
\(\mathcal A_X\), followed by uniform ideal convergence and the global
zero-period test.  Until those are proved, the comparison factor is not known
to be a unit and no RH conclusion is authorized.

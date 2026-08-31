# The theta common mode lies in the closure of arithmetic incidence but only at diverging source cost

## Exact one-prime approximants

The centered primitive column is

\[
b_p
=
p^{-1/2}\Phi+r_p,
\qquad
r_p
=
-p^{-1/2}\Phi\mathbf1_{(\log p,\infty)}.
\]

For the finite-support source vector

\[
x^{(p)}=p^{1/2}e_p,
\]

one obtains the exact image

\[
B_\Sigma x^{(p)}
=
p^{1/2}b_p
=
\Phi\mathbf1_{[0,\log p]}.
\]

Theta superexponential decay gives

\[
\|B_\Sigma x^{(p)}-\Phi\|_{\mathcal H}
=
\|\Phi\mathbf1_{(\log p,\infty)}\|_{\mathcal H}
\longrightarrow0.
\]

Therefore

\[
\Phi
\in
\overline{\operatorname{ran}B_\Sigma}.
\]

In particular,

\[
\operatorname{dist}
\bigl(
\Phi,
\overline{\operatorname{ran}B_\Sigma}
\bigr)=0.
\]

A positive unweighted range angle is not merely unproved; it is false.

## Diverging arithmetic cost

The source norm of the approximant is

\[
\|x^{(p)}\|_U^2
=
p\log p.
\]

Hence the approximation reaches the theta common mode only at diverging
arithmetic energy. It does not produce a bounded source sequence converging to
an exact dark pair with a nonzero theta coordinate.

This separates two statements:

- history-space closure: \(\Phi\) is approximable by arithmetic incidence;
- energy-controlled cancellation: approximants remain bounded in the
  arithmetic complement norm.

Only the second is relevant to Schur coercivity.

## Correct weighted test

Let the arithmetic complement satisfy

\[
\operatorname{Re}Q_U\ge\delta_U I
\]

or the corresponding sign-definite imaginary-part estimate. Then

\[
\langle x,Q_Ux\rangle
\]

penalizes the sequence \(x^{(p)}\) at least proportionally to \(p\log p\).
The closure approximation therefore cannot erase the theta defect at bounded
complement energy.

The relevant comparison is the bounded transfer

\[
T_Q
=
Q_U^{-1/2}B_\Sigma^\dagger R_HV,
\]

not the unweighted distance from \(\Phi\) to
\(\overline{\operatorname{ran}B_\Sigma}\). The dressed scalar is controlled by

\[
F_\theta
=
V^\dagger R_HV-T_Q^\dagger T_Q
\]

in a positive chart, with the appropriate sign variant in the Nevanlinna
chart.

A strict theta defect requires an estimate comparing \(\|T_Q\|^2\) with the
bare theta Weyl value. It does not require closed range of \(B_\Sigma\).

## Consequences

1. The proposed positive range-angle gate is withdrawn.
2. Compactness or nonclosed range of the arithmetic incidence is compatible
   with a coercive Schur complement.
3. The strict Cayley law remains eligible precisely because it charges the
   large source norms needed to approximate \(\Phi\).
4. Finite-cutoff angle estimates must not be extrapolated uniformly: their
   constants necessarily degenerate along the one-prime approximants.
5. The prospective Xi zeros must arise from the dressed energy balance, not
   from failure of history-space object membership.

## Remaining quantitative gate

The source calculation now required is

\[
\left\|
Q_U^{-1/2}B_\Sigma^\dagger R_HV
\right\|^2
\]

relative to \(V^\dagger R_HV\), including seam boundary values and reciprocal
signs. Equality at the Xi divisor and strict inequality off it would supply
the intended one-dimensional defect crossing.

## Disposition

The theta forcing belongs to the closure of the centered arithmetic incidence
range, but only through source vectors whose norm diverges as
\((p\log p)^{1/2}\). The unweighted range-angle requirement is false and is
replaced by a complement-energy transfer estimate. The divisor identity and
seam boundary theorem remain open. No RH conclusion is authorized.

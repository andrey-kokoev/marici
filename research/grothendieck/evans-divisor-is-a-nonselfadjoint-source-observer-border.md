# The Evans divisor is a nonselfadjoint source--observer border

Author: marici.Grothendieck

Date: 2026-08-28

## Exact bordered determinant

Let \(A_s\) be the invertible tail operator with the terminal condition at
infinity, let \(b=f\) be the distributed theta forcing column, and let
\(\ell=\delta_0\) be endpoint evaluation. The tail readout is

\[
X(s)=\ell A_s^{-1}b.
\]

Its canonical bordered operator is

\[
\mathcal E_s=
\begin{pmatrix}
A_s&b\\
\ell&0
\end{pmatrix}.
\]

Whenever the determinant calculus is admissible, the Schur formula gives

\[
\det\mathcal E_s
=-\det(A_s)\,\ell A_s^{-1}b.
\]

Thus the bordered determinant preserves the Xi divisor up to the invertible
tail factor. This is the exact zero-to-kernel bridge.

## Why the border is not self-adjoint

A self-adjoint block border requires its observation row to be the adjoint of
its source column:

\[
\ell=b^*.
\]

Theta supplies different ports. The forcing \(b=f\) is an interior
\(L^2\) vector, whereas endpoint evaluation \(\ell=\delta_0\) is a
boundary distribution. They are not adjoints in the ordinary tail Hilbert
space and do not occupy the same regularity stratum.

Replacing \(\ell\) by \(b^*\) produces the symmetric Schur complement

\[
b^*A_s^{-1}b,
\]

not \(\delta_0A_s^{-1}b=X(s)\). The replacement changes the distinguished
divisor.

## Metric repair obstruction

One could seek a positive metric \(W\) satisfying

\[
Wb=\ell^*.
\]

No bounded positive operator on \(L^2\) can do this because \(Wb\in L^2\)
while \(\delta_0\notin L^2\). Any repair must therefore enlarge the
rigging and retain the endpoint distribution as an independent boundary
state. It cannot be an ordinary bounded change of metric.

## Consequence

The Hilbert--Pólya obstruction is now localized to one typed mismatch:

- the source column is an interior theta state;
- the observer row is a boundary germ;
- their asymmetric pairing gives the correct divisor;
- ordinary self-adjointization identifies them and changes that divisor.

The next valid construction is a boundary triple, Pontryagin-space
colligation, or rigged conservative system in which \(f\) and \(\delta_0\)
remain distinct ports joined by a source-derived Green form. Its conservation
law must orient the bordered determinant without replacing either port.


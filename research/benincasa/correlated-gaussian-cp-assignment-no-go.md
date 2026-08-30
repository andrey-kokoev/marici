# Correlated Gaussian CP-assignment no-go

An ordinary Gaussian channel from the observed mode to the observed-plus-partner pair acts on covariances by

\[
V\longmapsto XVX^T+Y.
\]

Preserving the observed mode, while making the partner covariance and cross-correlation input-independent, forces the assignment form

\[
X=\begin{pmatrix}I\\0\end{pmatrix},
\qquad
Y=\begin{pmatrix}0&cZ\\cZ&aI\end{pmatrix}.
\]

The Gaussian complete-positivity condition is

\[
Y+i(\Omega_{\rm out}-X\Omega_{\rm in}X^T)\succeq0.
\]

Its observed-(q)/partner-(q) principal submatrix is

\[
\begin{pmatrix}0&c\\c&a\end{pmatrix},
\]

whose determinant is (-c^2).  Therefore no such CP assignment exists for (c\ne0).

At (c=0), the test reduces to (aI+iJ\succeq0), with eigenvalues (a\pm1).  For (a\ge1) this is exactly the ordinary product assignment.

This does not deny positivity of the joint states on Entry 1639's compatibility domain.  It proves that this domain cannot be replaced by an ordinary state-independent Gaussian CP preparation map.  The required object must retain initial-correlation compatibility, as a process tensor, assignment relation, or equivalent supported coefficient object.

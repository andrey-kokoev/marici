# Fourth cumulant lives inside a positive moment matrix, not a positive ray

For a centered one-variable marginal, write

\[
\mu_{2r}=\langle q^{2r}\rangle,
\qquad
\kappa_4=\mu_4-3\mu_2^2.
\]

Physical positivity through degree eight is represented by the truncated
moment matrix

\[
M_4=
\begin{pmatrix}
1&\mu_2&\mu_4\\
\mu_2&\mu_4&\mu_6\\
\mu_4&\mu_6&\mu_8
\end{pmatrix}
\succeq0.
\]

At fixed variance \(\mu_2=1\), two exact physical distributions give opposite
fourth cumulants:

\[
q=\pm1\text{ with equal weights}
\quad\Rightarrow\quad
(\mu_4,\mu_6,\mu_8)=(1,1,1),
\quad\kappa_4=-2,
\]

and

\[
P(0)=\frac34,
\qquad
P(2)=P(-2)=\frac18
\]

gives

\[
(\mu_4,\mu_6,\mu_8)=(4,16,64),
\qquad
\kappa_4=1.
\]

Both moment matrices are positive semidefinite.  Thus physicality does not
select a sign for \(\kappa_4\); it constrains the coupled moment sequence.

This classical marginal is a necessary slice of the quantum state moment
cone.  The full phase-space problem additionally requires mixed \(q,p\)
moments and the canonical commutator/localizing constraints.

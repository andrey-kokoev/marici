# The stable even magnetic response has a fixed sign

The even-depth Schur correction contains the adjacent-endpoint response

\[
X=g(a-4)(m_++1)+(a+g-1)(m_+-g),
\qquad m_+=1-g+q-a.
\]

For even `q`, the stable region begins at

\[
a=q+4+2t,\qquad t\ge0.
\]

After this substitution, direct expansion gives

\[
\begin{aligned}
-X={}&g^2q+2g^2t+2g^2+2gqt+4gq+4gt^2+10gt+9g\\
&+2qt+3q+4t^2+12t+9.
\end{aligned}
\]

Every coefficient is strictly positive.  Therefore

\[
\boxed{X<0}
\]

for every stable even component.  The correction

\[
\frac{qg(g+3)}{X}
\]

has a fixed negative sign and no pole in the stable parameter domain.  Since
the complete even transfer character is already the positive polynomial

\[
qg(g+3)a^{\overline g}a^{\overline{g-1}}(a+g+q-1),
\]

the denominator is a removable chart normalization, not a spectral
singularity.

The stability boundary is essential.  The same raw endpoint response vanishes
in the prefix at

\[
(g,q,a)=(5,12,6),
\]

well before `a=q+4`.  Thus source inequalities, not a formal cancellation,
protect the stable transport.  Prefix response zeros must remain part of the
finite initialization atlas.

The coefficient-sign argument is symbolic for all `g>=2`, even `q>=2`, and
`t>=0`; bounded sweeps serve only as implementation cross-checks.

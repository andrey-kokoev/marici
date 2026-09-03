# Orientation fixes a unique formal cyclic converter

On the ordered `L` orbit `(g12,g23,g31)`, the literal vector is `(0,-1,-1)`
and the desired shadow is `(0,-1,1)`. There is a unique integral circulant
matrix sending the former to the latter:
\[
A=\begin{pmatrix}0&1&-1\\-1&0&1\\1&-1&0\end{pmatrix}.
\]
It is skew-symmetric, has rank two, annihilates constants, and maps into the
zero-sum ordered cocycles.

Thus the sign defect has a unique formal cyclic repair. It is not yet a source
chain map: `q_g12` is absent, marked-pair and occurrence axes are not identified,
and interpreting `A` as incidence requires the missing complement-labelling
morphism. The next test is an exact incidence factorization of `A`.

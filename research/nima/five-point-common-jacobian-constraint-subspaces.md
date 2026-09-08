# Five-point common-Jacobian constraint subspaces

## Question

Which rank-three affine constraints realize the classified common-Jacobian fans, and do conservation or positivity select the reference member?

## Claim boundary

The annihilator is derived from the two-parameter gradient family. No source map selects one member or its support constants.

With normalized facet gradients parameterized by `a,b`, the rank-three annihilator can be chosen as

\[
R(a,b)=
\begin{pmatrix}
1&-a&1&0&0\\
-u&-v&0&1&0\\
-b&1&0&0&1
\end{pmatrix},
\quad
u=\frac{1-b}{ab-1},\quad v=\frac{1-a}{ab-1}.
\]

Direct multiplication gives `R(a,b)V(a,b)=0`. For the reference member `a=b=0`, the affine constraints are

\[
a_0+a_2=k_2,\qquad a_0+a_1+a_3=k_3,
\qquad a_1+a_4=k_4.
\]

Using the verified universal map `b=C a`, these rows are non-coordinate linear combinations of the five `b_i`; this explains why fixing any coordinate triple failed.

The condition that `v2=-v0` and `v4=-v1` forces `a=b=0`, so two parallel facet pairs select the reference fan within this frame. That geometric condition is not supplied by conservation alone. Strict positivity also fails to select it: exact rational members `(a,b)=(1/4,1/3)` and `(-1/4,1/5)`, with all support constants one, retain five strict adjacent vertices and the same common Jacobian.

## Disposition

The required affine constraint subspaces are now explicit. Conservation rewrites them but does not choose one, and bounded positivity leaves nearby rivals. Selecting the reference slice requires a further source-derived constraint, such as an authorized positive-geometry construction or a proved geometric condition on parallel facets; support constants remain independent input.

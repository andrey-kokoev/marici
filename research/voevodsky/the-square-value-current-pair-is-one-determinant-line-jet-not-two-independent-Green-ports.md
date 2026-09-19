# The square value/current pair is one determinant-line jet, not two independent Green ports

The value/current distinction from the previous iteration is valid only at the
determinant-line jet level.  Prime-power cumulants are cyclic word lengths of
one primitive Euler loop; they cannot be adjoined as independent Hilbert
boundary channels.

For the square cumulant use the local section

\[
a_p(s)=\frac12p^{-2s}.
\]

At the centered point,

\[
a_p(1/2)=\frac12p^{-1}.
\]

Its logarithmic connection coordinate is not independent:

\[
-\partial_s a_p(s)=(\log p)p^{-2s},
\]

and therefore

\[
-\partial_s a_p(1/2)=(\log p)p^{-1}.
\]

Thus the two source-normalized coefficients are exactly the value and
connection of one square determinant-line section.  Their relation fixes the
factor `1/2`, logarithm, and derivative sign.

The correct `CG` requirement is consequently connection-preserving transport

\[
\alpha\circ\nabla_{\rm Euler}
=\nabla_{\rm Green}\circ\alpha
\]

on the square line, together with the analogous archimedean connection.  It is
not a map sending two freely chosen square coordinates into two independent
Green ports.  On the Green side, endpoint value and ordered current may appear
as separate observations, but their image must satisfy the source connection
relation above.

This removes the finite square-normalization ambiguity while respecting the
cyclic-source obstruction.  The remaining square gate is to prove that the
labelled adelic-to-Hardy correspondence intertwines this determinant
connection and its archimedean mate after reciprocal sewing.

# Many-many enlarged Green block collocation

Write the enlarged feature space as

$$
\mathscr X_G=\bigoplus_{r=1}^6X_r
$$

and the source metric as a Hermitian block operator

$$
G_{\rm src}=(G_{rs})_{r,s=1}^6,
\qquad
G_{sr}=G_{rs}^*.
$$

Let the lifted input and output ports be block columns

$$
B_G=(b_r)_r,
\qquad
C_G^*=(c_r)_r.
$$

The collocation equation

$$
G_{\rm src}B_G=C_G^*
$$

is equivalent to the six row equations

$$
\sum_{s=1}^6G_{rs}b_s=c_r,
\qquad 1\le r\le6.
$$

The diagonal blocks carry positive graph energies. Off-diagonal blocks carry the ordered Stokes/Wronskian, endpoint-tail, primitive-square, and reciprocal linking forms. They are retained before any Schur reduction.

For a finite packet, positivity is checked by Schur complements after the row equations are imposed. In the projective completion, every block must be jointly closable on the common analytic source core and compatible with cutoff restriction.

Status: enlarged block-collocation equations fixed; source values of the cross blocks remain to be assembled.

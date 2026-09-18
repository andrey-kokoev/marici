# Xi Rosenbrock pencil is not a fixed-endpoint Hopf module

The transverse pencil is

$$
\mathcal R_\Xi(z)(f_-,f_+,c)
=
\bigl((\partial_q-z)f_- -c\Phi_-,
(\partial_q-z)f_+ -c\Phi_+,
 f_-(0)-f_+(0)\bigr).
$$

Translation commutes with the differential expression:

$$
(\partial_q-z)S_af=S_a(\partial_q-z)f.
$$

It does not preserve the fixed endpoint row:

$$
E_0S_af=f(a),
$$

so

$$
(E_0\oplus-E_0)(S_af_-,S_af_+)
=f_-(a)-f_+(a),
$$

which is not generally `f_-(0)-f_+(0)`. Translation also sends the source columns to `S_a Phi_±`; these need not equal `Phi_±`.

Therefore the fixed-endpoint Rosenbrock pencil is not an `H_tr`-module morphism under bare translation. This failure does not affect its exact transfer

$$
E_\Xi(z)=\tau(z)=\Xi_{\rm centered}(z)
$$

or its multiplicity theorem.

A Hopf-compatible realization must enlarge the object index from one fixed endpoint to the translated endpoint/seam groupoid. Its naturality square has the form

$$
\mathcal R_{\Xi,a}(z)\,\rho(Q_a)
=
\rho_{\rm out}(Q_a)\,\mathcal R_{\Xi,0}(z),
$$

where `R_Xi,a` evaluates at `q=a` and carries the translated source columns. Equivalently, retain the full tail-plus-seam cut so endpoint movement is part of the target.

Thus the first missing six-port compatibility is now explicit: construct the moving-endpoint Xi pencil as a module over the translation action groupoid, then compare its source-selected conservative symmetrizer across those fibers.

Status: fixed-endpoint Hopf-module claim disproved; moving-endpoint/seam-equivariant replacement open.

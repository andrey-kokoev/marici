# 920 — Reflection Strictly Exchanges the Two Off-Diagonal Rees Lines

## Frozen comparison

Entry 919 globalizes the (y=s_{35}) off-diagonal line on

\[
E_y=\mathbf P(n_a,n_y,n_q)
\]

as

\[
\mathcal L_y
=
\mathbf Q\langle r_y\rangle
\otimes
\mathcal O_{E_y}(D_a-D_y).
\]

The source reflection

\[
\tau_{\rm off}=(23)
\]

fixes (a=s_{14}) and (q=s_{235}), and exchanges

\[
y=s_{35}
\longleftrightarrow
z=s_{25}.
\]

The comparison is made by transporting this frozen source object. No independent normalization is chosen for the (z)-line.

## Exceptional divisor transport

On homogeneous exceptional coordinates, reflection acts by

\[
[n_a:n_y:n_z:n_q]
\longmapsto
[n_a:n_z:n_y:n_q].
\]

Therefore

\[
\tau^*\!\left(\frac{n_a}{n_y}\right)
=
\frac{n_a}{n_z},
\]

and

\[
\tau(D_a-D_y)=D_a-D_z.
\]

Both divisors have degree zero. The (q)-component remains zero.

## Orientation audit

In the source-normalized transition, \(\tau_{\rm off}\) reverses both serialized variance bases:

\[
\chi_{\rm sparse}(\tau_{\rm off})=-1,
\qquad
\chi_{\rm dense}(\tau_{\rm off})=-1.
\]

It preserves the ordered residue orientation and the normal-line orientation. Hence

\[
\chi_{\rm total}(\tau_{\rm off})
=(-1)(-1)(+1)(+1)
=+1.
\]

The exact checker consequently finds no residual sign or rational unit:

\[
\boxed{
\tau^*\mathcal L_y=\mathcal L_z,
\qquad
\mathcal L_z
=
\mathbf Q\langle r_z\rangle
\otimes
\mathcal O_{E_z}(D_a-D_z).
}
\]

## Narrow conclusion

The two order-dependent off-diagonal flags are not separate fitted coefficient objects. They are a single source-labelled occurrence orbit. Reflection transports both the constant projective line and its Hecke divisor strictly:

\[
\boxed{
D_a-D_y
\xleftrightarrow{\ \tau\ }
D_a-D_z,
\qquad
\text{transition unit}=1.
}
\]

Thus the entire (y/z) asymmetry is occurrence labelling on the existing Rees carrier. It supplies neither a new carrier stratum nor an additional coefficient character.

## Scope and next falsifier

This proves pairwise reflection covariance. It does not yet assemble the diagonal (x)-flag and off-diagonal (y/z)-flags into one normal-crossing coefficient complex: the (x)-flag lives in first conormal grade, whereas the (y/z)-flags live on Rees exceptional lines.

The next test is to construct the smallest typed comparison between these two filtration types at their common deeper corner. A map may be proposed only if it is induced by the frozen marked-incidence differential or a Rees specialization map; rank matching alone is inadmissible.

# 2858 — The Soft Endpoint Stokes Object Is a Two-Port Cospan

## Source chain

The exceptional physical coordinate carries the oriented chain

\[
\Gamma_\xi=[-1,1],
\qquad
\partial\Gamma_\xi=[1]-[-1].
\]

The two endpoint ports are:

1. the ordinary coefficient-valued Cayley–Menger boundary at \(\xi=+1\);
2. the \(q_{g1}\)-residue Cayley–Menger corner at \(\xi=-1\).

In this ordered basis, the source boundary column is

\[
d_{\partial}=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]

## Relative totalization

Before totalization, the unmarked positive port has relative degree zero and the marked residue port has degree one. The residue-cone suspension shifts the marked port by \(-1\):

\[
\deg_{\rm tot}(E_+)=0,
\]

\[
\deg_{\rm tot}(E_-)=1-1=0.
\]

Thus the two ports occupy the same total boundary degree without identifying their coefficient lines.

The endpoint objects have no further ordinary boundary, so

\[
d_{\partial}^2=0.
\]

## Physical occurrence readout

Entry 2855 supplies the occurrence covector

\[
V_{\rm phys}=(1,0)
\]

on each endpoint packet. This is applied separately after the two boundary routes are formed.

## Structural conclusion

Stokes does not provide a morphism

\[
E_-\longrightarrow E_+.
\]

It provides a cospan

\[
E_+
\longleftarrow
\Gamma_\xi
\longrightarrow
E_-,
\]

or equivalently one boundary map into the direct sum

\[
\Gamma_\xi\longrightarrow E_+\oplus E_-.
\]

The common bulk parent fixes the relative shifts and orientation signs. It does not turn the two coefficient lines into one scalar.

Therefore the two-port description is the source-derived answer. A scalar endpoint sum requires an additional readout functional on \(E_+\oplus E_-\). Such a functional must come from an independently derived observable or relative cocycle; Stokes alone does not supply it.

## Falsifier

Search the frozen observable for a declared cocycle pairing with both totalized ports. If none exists, retire the scalar endpoint-combination hypothesis while retaining the cospan and both chamberwise endpoint values.

## Durable artifacts

- research/benincasa/check_soft_endpoint_stokes_cospan.py
- research/benincasa/soft-endpoint-stokes-cospan.json


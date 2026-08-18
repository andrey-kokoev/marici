# Entry 492 — The Gradient Homotopy Complex Does Not Supply the Conormal Cell

Entry 491 proposed recovering the even conormal cell as the degree-minus-one
fiber of the lifted carrier map into the two-term gradient complex of Entry
487.  The proposed identification is not well typed.

## Two different Koszul constructions

Entry 487 uses

\[
G_K=\left[\mathcal O^{\oplus2}
\xrightarrow{(K_a,K_b)}\mathcal O/(K)\right]
\]

to nullhomotope the residues of the complete exact operators.  Indeed

\[
H_p=(0,3m/2),\qquad H_q=(-3m/2,0)
\]

map to \(3mK_b/2\) and \(-3mK_a/2\).  This is the correct complex for the
gradient obstruction.

But its degree-minus-one kernel contains, for every coefficient \(f\),

\[
f(-K_b,K_a).
\]

Thus the unquotiented two-term kernel is a coefficient-sized gradient
syzygy module.  It cannot canonically equal the single principal conormal
line.

The conormal cell instead comes from the derived self-intersection of the
principal hypersurface.  If \(S\) is the ambient ring, \(R=S/(K)\), and
\(I=(K)\), tensoring the resolution

\[
[S\xrightarrow{K}S]
\]

with \(R\) gives

\[
[R\xrightarrow{0}R],
\qquad
H^{-1}\cong R\cong I/I^2.
\]

Therefore

\[
\boxed{
\text{gradient nullhomotopy data}\ne
\text{principal conormal data}.
}
\]

## Consequence

Entry 491's flatness result remains valid: the ordinary generic even source
is \((\mathbb Q[u]/(u^2))^{\oplus2}\).  What fails is only its proposed next
identification.  Taking the homotopy fiber against \(G_K\) without retaining
the hypersurface resolution would mix the universal gradient syzygies with
the desired Cartier relation.

The derived carrier comparison must therefore be a bicomplex (or an
equivalent iterated fiber) retaining both structures:

1. the principal complex \([S\xrightarrow K S]\), which supplies \(I/I^2\);
2. the gradient complex, which supplies the canonical homotopies of Entry
   487.

No additional carrier geometry is required; the correction is entirely in
the coefficient complex.

## Next gate

Construct the comparison as an iterated fiber: first lift ordinary carrier
reduction through the gradient homotopies, then base-change the resulting
map along the principal hypersurface resolution.  Test whether the even
fiber is exactly one copy of \(I/I^2\), with no residual gradient-syzygy
class.

The symbolic type check is
`research/voevodsky/check_soft_axis_gradient_vs_conormal.py`.

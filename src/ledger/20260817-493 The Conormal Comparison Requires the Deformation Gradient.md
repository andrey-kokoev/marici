# Entry 493 — The Conormal Comparison Requires the Deformation Gradient

Entry 492 separates the principal conormal resolution from the relative
gradient homotopy complex.  Joining them requires a chain-level Euler
certificate expressing the hypersurface equation through the chosen
gradient directions.

For the dual-number soft quartic

\[
K=a^4+ua^2(1-b^2),\qquad u^2=0,
\]

the full parameter-space derivatives satisfy the regular identity

\[
\boxed{K={a\over4}K_a+{u\over2}K_u.}
\]

Thus the principal differential factors canonically through the gradient
complex only when the deformation direction is retained.

## Failure of the frozen relative gradient

Entry 487 retains only \((K_a,K_b)\).  Removing the \(a\)-Euler part leaves

\[
K-{a\over4}K_a={u a^2\over2}(1-b^2).
\]

On the chart \(b\ne0\), this can be written as

\[
-{1-b^2\over4b}K_b,
\]

but the coefficient has a pole at \(b=0\).  This is not merely a bad choice
of certificate.  Restricting to \(b=0\), where \(K_b=0\), division by
\(K_a=4a^3+2ua\) would require

\[
A={a\over4}+{u\over8a}\pmod{u^2},
\]

which is not polynomial at the carrier.  Therefore

\[
K\notin(K_a,K_b)
\quad\text{regularly over the global frozen base,}
\]

even though a Laurent certificate exists on smaller charts.

## Consequence

The iterated comparison requested by Entry 492 cannot be formed globally
inside the frozen relative \((a,b)\)-gradient calculus.  The missing arrow is
exactly the deformation/Kodaira--Spencer direction \(K_u\).  This agrees
with Entry 488: the soft Gauss--Manin lift also becomes regular only after
the deformation direction is weighted logarithmically.

This is coefficient-complex information, not an instruction to add carrier
geometry.  The minimal comparison complex must retain

\[
(K_a,K_b,K_u)
\]

before taking the relative or nearby-cycle specialization.  Freezing \(u\)
too early destroys the global Euler bridge from the principal conormal cell
to the gradient homotopies.

## Next gate

Form the three-gradient Koszul comparison using the canonical vector
\((a/4,0,u/2)\).  Then specialize derivedly to \(u=0\) and determine whether
its even degree-minus-one fiber is exactly one copy of \(I/I^2\), while the
extra \(K_u\) direction becomes the expected Gauss--Manin/Kodaira--Spencer
class rather than a second conormal generator.

The symbolic certificate is checked by
`research/voevodsky/check_soft_axis_euler_comparison.py`.

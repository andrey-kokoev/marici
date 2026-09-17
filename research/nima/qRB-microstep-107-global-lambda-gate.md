# qRB microstep 107: global stabilization-parameter gate

A single scalar `lambda` stabilizes every regulator stage only if

$$
\lambda\sup_\alpha\|G_{\rm link}^{(\alpha)}\|\le1.
$$

If the linking norms are uniformly bounded, choose any strict value

$$
0<\lambda<\left(\sup_\alpha\|G_{\rm link}^{(\alpha)}\|\right)^{-1}.
$$

If they are unbounded, no nonzero global scalar stabilization exists; one must use a relative/projective family or regulator-dependent form stabilization.

The source record proves boundedness on the completed orbit for each declared linking operator, but does not yet provide a uniform bound across the full regulator family.

Status: global-lambda criterion isolated; uniform regulator norm remains open.

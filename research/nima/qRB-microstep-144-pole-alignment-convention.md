# qRB microstep 144: pole-alignment convention

When the shifted contour passes exactly through a digamma pole, define the continued integral by symmetric indentation. The pole contribution is then the Cauchy principal value plus one half of the oriented residue.

For a simple pole with residue `R`, the aligned prescription is

$$
\int_{\rm aligned}F
=\operatorname{PV}\int F
\pm\pi iR,
$$

with the sign determined by the contour orientation.

This convention makes the continued gamma channel the symmetric boundary value of the two adjacent analytic branches. It prevents an artificial jump caused solely by choosing one-sided indentation.

Status: pole-alignment convention fixed; a full source comparison must use this convention consistently in the gamma and endpoint channels.

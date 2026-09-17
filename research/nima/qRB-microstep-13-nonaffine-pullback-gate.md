# qRB microstep 13: non-affine pullback gate

For a source refinement map `\varphi`, the remaining observer test is

$$
\omega_{\sigma,t}\circ R_\varphi
\in
\overline{\operatorname{span}}\{\omega_{\sigma',t'}\text{ and endpoint jets}\}.
$$

It is not enough that `f\mapsto f\circ\varphi` preserves positivity or defines a formal pullback. We need:

1. `R_\varphi` maps the declared Schwartz core continuously into itself;
2. Gaussian pullbacks are either Gaussian mixtures or controlled Schwartz limits;
3. endpoint functionals remain projectively defined;
4. the pullback preserves the observer radical.

If these hold, refinement descends to the quotient. If not, the relative carrier may still exist, but the claimed qRB quotient functor is not defined for that refinement.

Status: exact gate isolated; no non-affine closure is claimed yet.

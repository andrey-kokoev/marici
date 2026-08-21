# Scalar Numerator Does Not Collapse the Asymmetric Kummer Character Support

Benincasa Entry 1273 proves that the exact degree-sixteen adjoint numerator
reduces on the physical Kummer cover to a nonzero scalar. This removes all
nontrivial numerator characters, but it does not remove the moving marked
denominator arrangement.

On the asymmetric physical slice the integrand is

\[
\Omega^{\rm asym}_{C_5}
=
\frac{C}{\prod_{a=1}^{26}q_a(X,y)},
\]

where every \(q_a\) is linear in the five Kummer sheet variables and the deck
group acts by

\[
y_i\mapsto\epsilon_i y_i.
\]

The exact Walsh--Hadamard audit evaluates the reciprocal denominator product
on all 32 sheets at two independent rational samples. Every transformed
coefficient is nonzero:

\[
\boxed{
\widehat\Omega_S\ne0
\quad\text{for all }S\subseteq\{1,\ldots,5\}.
}
\]

Therefore

\[
\boxed{
\operatorname{Supp}_{\widehat{C_2^5}}(\Omega^{\rm asym}_{C_5})
=
\widehat{C_2^5}.
}
\]

The typing is now exact:

- numerator coefficient class: trivial character only;
- complete rational integrand: all 32 characters;
- source of nontrivial characters: the 26 moving marked denominators.

Thus Entry 1273 simplifies the coefficient numerator without reducing the
Kummer local-system problem. The next twisted de Rham computation must retain
all 32 labelled character columns, organized into cyclic orbit blocks where
available. A rank reduction can arise only from exact cohomological relations
or the relative-cycle pairing, not from the scalar numerator itself.

Artifacts:

- `research/nima/check_asymmetric_constant_numerator_deck_support.py`
- `research/nima/results/asymmetric-constant-numerator-deck-support.json`

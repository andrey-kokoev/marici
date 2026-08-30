# The Two Erased Orientation Bits Live in Different Algebraic Layers

The exact Smith port contains two binary refinements, but they have different
support.

For \(A_\pm\), the entire relational Smith packet is identical. The first two
full Smith factors are also identical; only the terminal full factor changes.
Therefore the endpoint-orientation character \(\omega_A\) lives exclusively
in the full gauge extension.

For \(C_\pm\), both the terminal full factor and terminal relational factor
change. Therefore the ordered-tail character \(\omega_C\) survives relational
reduction.

The terminal full-to-relational ratios are exact squares:

\[
C_+:\ 28^2,
\qquad
C_-:\ 36^2.
\]

Writing \(\omega_C=\pm1\), both cases are governed by one affine conductor:

\[
\kappa_C(\omega_C)=4(8-\omega_C),
\qquad
\frac{s^{\mathrm{full}}_3(C_{\omega_C})}
     {s^{\mathrm{rel}}_2(C_{\omega_C})}
=\kappa_C(\omega_C)^2.
\]

Thus \(\kappa_C(+1)=28\) and \(\kappa_C(-1)=36\). Both conductors have
2-adic valuation two, so their squares have identical 2-adic depth even though
their odd units \(7\) and \(9\) differ.

Consequently the five-to-three 2-adic collapse forgets two differently typed
bits:

- one extension-only bit;
- one relational bit.

They cannot be represented as two copies of one homogeneous binary port.

Replay:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies seventy-four exact gates.

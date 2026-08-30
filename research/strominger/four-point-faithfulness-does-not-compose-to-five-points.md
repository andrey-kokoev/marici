# Four-Point Faithfulness Does Not Compose to Five Points

## Question

Does the faithful three-port packet for four marked zeros remain jointly
faithful when applied to every four-point marginal of a five-zero packet?

## Five-point Brunnian hostile

Push the fifth point around the peripheral loop

\[
\beta=[[[x_1,x_2],x_3],x_4]
\]

in the four-punctured sphere, where

\[
x_1x_2x_3x_4=1.
\]

After eliminating \(x_4\), the word is freely reduced and has length twenty
two in \(F_3=\langle x_1,x_2,x_3\rangle\). The Birman point-pushing
injection therefore gives a nontrivial class in the pure five-point mapping
class group.

Deleting any of the first four points kills one input of the nested
commutator, hence kills \(\beta\). Deleting the fifth point forgets the pushed
point and also kills \(\beta\). Thus every four-point deletion marginal is
trivial although the five-point class is nontrivial.

## Consequence

Even a faithful observation packet on every four-point face is not jointly
faithful on the five-point object. The missing information lies in the
intersection

\[
\bigcap_{i=1}^{5}\ker(d_i),
\]

the five-point Brunnian subgroup.

Therefore four-point closure does not compose upward. A new five-ary
coherence port is required; it must observe how the four-point faces are
jointly filled, not merely observe each face more accurately.

This is the first explicit higher-net obstruction predicted by the tower
programme.

## Verification

```powershell
uv run python research/strominger/checkers/five_point_brunnian_four_marginal_hostile_checks.py
```

## Sources

The construction uses the Birman point-pushing exact sequence. Its Brunnian
interpretation agrees with the deletion-kernel framework developed by
Stanford and with the spherical Brunnian analysis of Bardakov, Mikhailov,
Vershinin, and Wu.

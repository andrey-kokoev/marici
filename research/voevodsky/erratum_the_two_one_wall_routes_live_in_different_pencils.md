# Erratum: the two one-wall routes live in different pencils

## Correction

The wall-basis covector

\[
q_{v_{\rm alg}}(w_{101},w_{110})=(-1,+1)
\]

is source-derived and remains valid. However, the suggested direct marking

\[
(w_{101},w_{110})\stackrel?\longleftrightarrow
(\alpha_{13},\alpha_{14})
\]

is not merely unserialized; the two sides are geometrically typed in different pencils.

## Wall typing

The universal central two-wall packet uses

\[
l_1=b+x,
\qquad l_2=a+y.
\]

Before imposing \(E=0\), these are the two physical site walls

\[
W_1:b=y+z,
\qquad
W_2:a=x+z.
\]

Indeed, \(E=0\) gives \(y+z=-x\) and \(x+z=-y\).

Thus:

- \(w_{101}\) belongs to the \(b\)-adapted pencil;
- \(w_{110}\) belongs to the site-exchanged \(a\)-adapted pencil.

By contrast, \(\alpha_{13},\alpha_{14}\) are both defined inside the single fixed \(b/h\)-pencil from its four component differences.

## Central collision confirms the mismatch

In the fixed \(b\)-pencil, central specialization pairs

\[
q_1=q_4=-x,
\qquad q_2=q_3=x.
\]

Their half-sums are

\[
\frac{d_1+d_4}{2}=\alpha_{14},
\qquad
\frac{d_2+d_3}{2}=-\alpha_{14}.
\]

So the two collapsed \(b\)-wall supports carry only one primitive line, not the two-dimensional complement \(\langle\alpha_{13},\alpha_{14}\rangle\). The second one-wall route \(w_{110}\) enters from the different \(a\)-pencil.

## Exact role of the missing comparison

The remaining map is therefore precisely the site-exchange transport

\[
\text{the }a\text{-pencil wall route }w_{110}
\longrightarrow
\text{an integral route in the fixed }b\text{-pencil}.
\]

Once transported, the already-proved wall covector \((-1,+1)\) determines the fixed-pencil kernel. Without that map, neither

\[
\alpha_{13}+\alpha_{14}
\quad\text{nor}\quad
\alpha_{13}-\alpha_{14}
\]

is authorized as the physical kernel.

## Durable conclusion

The source data now determine both response rows on their natural domains:

1. the fixed-pencil normal jet gives the primitive \(e_6\) row;
2. the cross-pencil one-wall pair gives the primitive \(v_{\rm alg}\) row \((-1,+1)\).

The missing coherence comparison has one sharply isolated job: transport the second, site-exchanged wall route back to the fixed pyramid integrally and with orientation.

Verification:

- `research/voevodsky/checkers/check_cross_pencil_wall_typing.py`
- `research/voevodsky/results/cross_pencil_wall_typing.json`

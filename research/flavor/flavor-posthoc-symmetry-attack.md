# Post-hoc symmetry attack on the revised DPC (WP393)

## Target

Attack the revised claim that a one-dimensional intertwiner space explains a
unique flavor-response direction.

## Universal custom-symmetry construction

Let $v=(p,q)^T$ be any nonzero target direction in a calibrated real
two-dimensional response space. With the chosen Euclidean pairing, define the
orthogonal vector $n=(-q,p)^T$ and reflection

\[
S_v=\frac{vv^T-nn^T}{v^Tv}.
\]

Exact calculation gives

\[
S_v^2=I,\qquad S_vv=v,\qquad S_vn=-n.
\]

Therefore $S_v$ is a valid $Z_2$ representation and its fixed intertwiner
space from the trivial source line is exactly one-dimensional:

\[
\dim\operatorname{Hom}_{Z_2}(L,R)=1.
\]

This construction works for every nonzero $v$. The revised DPC's algebraic
condition can therefore be manufactured around any desired flavor ratio.

## Smallest hostile pair

The unrelated target rays $v_1=(1,2)^T$ and $v_2=(2,1)^T$ each possess a
custom reflection with a unique fixed line. Their reflections are different,
and the first reflection does not fix the second ray. Existence of some
symmetry with one-dimensional intertwiner space does not choose between them.

The construction also consumes a positive pairing to define $n$. If that
metric is inferred from the target or detector coordinates, the claimed
symmetry imports additional presentation authority.

## Explanatory diagnosis

The revised DPC becomes explanatory only if the following are frozen before
the target flavor relation is supplied:

- the physical origin and action of the symmetry;
- the response representation and its multiplicities;
- the positive pairing used to identify the protected complement;
- the source-to-physical16 embedding;
- the allowed RG and threshold commutant.

Merely exhibiting these objects after fitting the response direction is a
universal reconstruction recipe, not a source explanation. It predicts no
independent phenomenon.

## Disposition

WP393 does not refute a specific independently given symmetry theory. It
refutes the inference from existence of a suitable symmetry and
one-dimensional intertwiner to explanatory selection. For any target ray,
such a symmetry exists by construction.

The smallest exact falsifier is the pair $(1,2)$ and $(2,1)$ with their two
custom reflections. The required repair is temporal and causal: preregister
the symmetry, metric, and embedding from non-flavor source dynamics, and only
then expose the physical16 target for prediction.

Run `uv run --with sympy python
research/flavor/checkers/wp393_posthoc_symmetry_attack.py` to regenerate the
result.

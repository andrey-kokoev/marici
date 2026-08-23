# Strict-category audit of the finite self-modeling construction

## Category

Let \(\mathbf{TDG}\) be the finite category whose objects are typed dependency
graphs and whose morphisms preserve:

- node kind and level;
- directed incidence;
- edge kind and role.

No edge may be silently erased or have its role changed. This is intentionally
strict: it models the existing Marici discipline that transport does not
create authority or erase typing.

## Object action

For a graph \(X\), \(\mathsf U(X)\) adds, for every node \(x\),

- a meta-level model object \(m_x\);
- a meta-level readout record \(r_x\);
- edges \(m_x\xrightarrow{\rm models}x\) and
  \(r_x\xrightarrow{\rm classifies}m_x\).

The original graph is retained as an induced subgraph.

## Morphism action

For \(f:X\to Y\), define

\[
\mathsf U(f)(x)=f(x),\qquad
\mathsf U(f)(m_x)=m_{f(x)},\qquad
\mathsf U(f)(r_x)=r_{f(x)}.
\]

The companion checker verifies on a finite composable diagram that this
preserves every typed edge and satisfies

\[
\mathsf U(1_X)=1_{\mathsf U(X)},\qquad
\mathsf U(g\circ f)=\mathsf U(g)\circ\mathsf U(f).
\]

Thus the construction earns a bounded endofunctor result on
\(\mathbf{TDG}\).

## Negative result: no strict retraction

The canonical inclusion

\[
\eta_X:X\hookrightarrow\mathsf U(X)
\]

is a strict morphism. But an exhaustive finite search finds no strict
\(\pi_X:\mathsf U(X)\to X\) fixing \(X\). The new `models` and `classifies`
edges have no corresponding typed edges in the base object, so a total strict
graph morphism cannot erase them.

Therefore

\[
\boxed{\mathsf U\text{ is functorial in the tested strict category, but the
extension is not split there}.}
\]

Induced-subgraph truncation remains available as an external restriction
operation. Promoting it to a morphism would require a justified category of
partial maps, localization, or explicit erasure cells. None is adopted here.

## Consequence for the fixed-point conjecture

The absence of a strict retraction is not a defect to repair automatically.
It may be the first substantive residual of self-modeling: once a system
contains records of its own models, returning to the prior system loses typed
structure. Any fixed-point or final-coalgebra proposal must explain this
residue rather than discard it.


# Edge-12 inter-grade localization audit

## Frozen pair

Let (S) be a deletion set not containing edge (12). The correlator source
defines two independent summands

\[
\omega_S=T_S\psi_{G\setminus S},
\qquad
\omega_{S+12}=T_{S+12}\psi_{G\setminus(S\cup\{12\})}.
\]

Writing (y=y_{12}), the additional source operation in the second port is

\[
K_{12}f=rac1y,	au_{12}^*f,
\qquad
\tau_{12}:(x_1,x_2,x_3)mapsto(x_1+y,x_2+y,x_3).
\]

The functions on which (T_S) and (T_{S+12}) act belong to different graph
sectors. The source supplies no equality between them.

## Candidate 1: ordinary restriction

Ordinary restriction of (K_{12}f) to (y=0) is undefined because of its
simple pole. Multiplying by (y) first gives

\[
i^*(yK_{12}f)=f(x_1,x_2,x_3),
\]

but this is the boundary value of the same (f). It is not a map to or from
the independently supplied adjacent graph function.

## Candidate 2: residue/Gysin

The logarithmic residue is well typed for the external Kummer factor:

\[
\operatorname{Res}_{y=0}
\left(\frac{dy}{y}\,\tau_{12}^*f\right)=f|_{y=0}.
\]

Its target is the (y=0) boundary value of the translated sector. A Gysin
normal line and its orientation do not identify this target with
(mathcal M_S). Hence this constructs a boundary counit inside one sector,
not an edge-erasure morphism between sectors.

## Candidate 3: translated Kummer pullback

The operator (K_{12}=y^{-1}\tau_{12}^*) is horizontal after retaining its
forced logarithmic connection:

\[
(\partial_y+y^{-1})K_{12}
=K_{12}(\partial_{x_1}+\partial_{x_2}).
\]

It is therefore a legitimate source port. Its codomain is the common
correlator readout, not the adjacent graph module. Horizontality does not
change that variance.

## Verdict

All three candidates fail to construct

\[
\mathcal M_S\longrightarrow\mathcal M_{S\cup\{12\}}.
\]

Restriction fails on the pole, residue returns a same-sector boundary value,
and translated Kummer pullback is the already-known port into the common
readout. The edge-12 inter-grade morphism remains source-absent.

This is a typing failure, not a nonzero obstruction class. No mapping cone or
homotopy is authorized until an independent graph-sector comparison is
derived.

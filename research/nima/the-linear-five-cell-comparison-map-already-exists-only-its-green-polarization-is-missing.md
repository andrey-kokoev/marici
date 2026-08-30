# The linear five-cell comparison map already exists; only its Green polarization is missing

## Correction

The representation frontier stated at event 10166 was too broad. The source already supplies the linear comparison map before analytic multiplication.

For each prime \(p\), with \(L=\log p\), define

\[
J_p^{\mathrm{cell}}e_{p,1}=[W_L],
\qquad
J_p^{\mathrm{cell}}e_{p,2}=[W_{2L}].
\]

Then

\[
J_p^{\mathrm{cell}}(e_{p,2}-e_{p,1})
=
[W_{2L}-W_L],
\]

and the multiplication representation gives

\[
\operatorname{Mult}
\bigl(
J_p^{\mathrm{cell}}(e_{p,2}-e_{p,1})
\bigr)
=
M_{W_{2L}-W_L}.
\]

Thus finite location, grade, orientation, prime label, and the raw adjacent-window propagator are already intertwined.

## Linear versus quadratic authority

This linear map does not determine the coefficient Green form. If \(u=[W_L]\) and \(v=[W_{2L}]\), the multiplication representation fixes \(\pi(u)\) and \(\pi(v)\), but it does not by itself fix the polarized coefficient

\[
g_p^{\mathrm{cell}}(u,v).
\]

Different Hermitian forms on the same two feature vectors can have the same represented difference operator and different mixed Green blocks.

The missing theorem is therefore not construction of \(\Pi\) as a linear representation. It is construction of a source-polarized form for which the quadratic representation commutes with the Green boundary operation.

## Exact square

Let

\[
\Gamma_\pi(|u\rangle\langle v|)
=
\pi(u)^{*}\pi(v).
\]

The required identity is

\[
\Gamma_\pi(G_p^{\mathrm{cell}})
=
G_p^{\mathrm{analytic}}
\]

on a common form core, after wall splitting and radical descent.

Equivalently, each of the four endpoint matrix units must satisfy the source Green identity:

\[
\Gamma_\pi
\bigl(
|W_{jL}\rangle\langle W_{kL}|
\bigr),
\qquad
j,k\in\{1,2\}.
\]

The diagonal entries are controlled by the closed history norms. The off-diagonal entries carry the remaining polarization and orientation content.

## Relation to the five-cell observer

The exact endpoint columns and Wronskian traces prove finite observability only after this quadratic lift identifies their coefficient and analytic Green frames. Otherwise one can have:

- the correct linear trace matrix;
- the correct adjacent-window difference;
- the correct reciprocal action;
- but the wrong mixed Green current.

Therefore event 10166 should be read conditionally: the numerical frame is available, and the linear comparison map is available, but the Green-polarized representation is not yet source-authorized.

## Minimal theorem

The next proof packet needs only:

1. freeze the coefficient feature form on the four endpoint matrix units;
2. prove the multiplication identity on the rapid twisted core;
3. show both sides are continuous in the closed history graph norm;
4. prove radical compatibility;
5. prove reciprocal adjoint orientation of the off-diagonal entries;
6. assemble prime labels with cutoff-uniform form bounds.

The rapid twisted core theorem already removes the density and hidden-extension hostiles. The genuinely live datum is the source value of the mixed polarization.

## Hostile

Choose two coefficient forms with identical diagonal entries and identical energy on \(v-u\), but opposite imaginary off-diagonal entries. Their linear multiplication histories and scalar difference energies agree. Their reciprocal Green currents disagree.

This is exactly why the quadratic lift, not the linear map, is the irreducible gate.

## Frontier

The first Adams comparison arrow has reached its narrowest current form:

\[
\text{explicit coefficient window history}
\longrightarrow
\text{source-polarized four-entry Gram}
\longrightarrow
\text{quadratic multiplication identity}
\longrightarrow
\text{closed analytic Green boundary}.
\]

Only the middle two arrows remain unresolved locally.

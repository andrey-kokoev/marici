# Equivariant weighted moving-current completion of the eight-lattice

## Result

The terminal pro-horn is completed in a translation-equivariant weighted trace-class bundle over the center parameter `c in R`.

For an even weight

\[
w_{c,s}(t)=(1+(t-c)^2)^{-s},
\]

choose `s` beyond the polynomial divisor-counting and successor-growth threshold. The symmetry-completed divisor feature

\[
P_c^{(s)}=\sum_\rho
w_{c,s}(\operatorname{Re}\rho)
|e_{c,\rho}\rangle\langle e_{c,\rho}|
\]

is positive trace class. Finite divisor truncations converge in trace norm.

## Translation action

With `(U_a f)(t)=f(t-a)`, the centered moving port is

\[
E_{c,\gamma}f=(f(c+\gamma),f(c-\gamma)).
\]

It satisfies

\[
E_{c+a,\gamma}U_a=E_{c,\gamma},
\qquad
U_aP_c^{(s)}U_a^*=P_{c+a}^{(s)}.
\]

Thus the completion is covariant, not strictly invariant. Strict nonzero translation invariance is impossible in trace class.

## Face compatibility

The three relevant faces transform over the same base:

- `H134`: `E_(c,gamma)^* J_idx E_(c,gamma)`;
- `H124`: exact unitary transport of the finite-width physical representative;
- enlarged `H234`: translated moving-current pairing.

Their pullback equality is preserved by every `U_a`. The global atomic current converges in the strong Schwartz dual under polynomial divisor counting.

## Lattice coverage

Edgewise-subdivision functoriality restricts this one enriched parent pullback to all cells of `esd_7(Delta^3)`:

- 560 equivariant edge transfers;
- 784 equivariant face homotopies;
- 343 equivariant pullback modifications.

Shared faces have one record and are referenced identically by adjacent tetrahedra.

## Aggregate certificate

The aggregate executable certificate is:

- `research/voevodsky/checkers/check_esd7_equivariant_trace_class_completion.py`;
- `research/voevodsky/results/esd7_equivariant_trace_class_completion.json`.

It consumes the weighted trace-class, translation bundle, port intertwiner, three-face equivariance, global-current pullback, and explicit lattice-overlay certificates. Every dependency passes.

## Scope

Established:

1. weighted global trace class in every center fiber;
2. trace-norm convergence of finite divisor packets;
3. translation covariance;
4. strong-dual current convergence;
5. compatible analytical representations on every edge, face, and tetrahedron.

Not asserted:

1. a nonzero strictly translation-invariant trace-class operator;
2. unweighted global trace class;
3. all-path norm convergence of divergent common Hilbert rows.

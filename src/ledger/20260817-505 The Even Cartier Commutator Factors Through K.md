# Entry 505 — The Even Cartier Commutator Factors Through K

Benincasa Entry 504 proves that multiplication by \(a^2\) does not descend
to the naive complete exact cokernel.  The commutator can nevertheless be
computed exactly from the sector operators.

The \(p\)-operator differentiates only in \(b\), so

\[
[p,a^2]=0.
\]

The \(q\)-operator contains the term

\[
(\partial_a f)L_1^{e_a}L_2^{e_b}K.
\]

Leibniz therefore gives, in every sector and in both deck lattices,

\[
\boxed{
[q,a^2](f)=2afL_1^{e_a}L_2^{e_b}K.
}
\]

The whole commutator is divisible by the defining quartic \(K\).  Thus it
has a canonical candidate nullhomotopy in the principal hypersurface resolution

\[
[S\xrightarrow K S]
\]

with coefficient

\[
h(f)=2afL_1^{e_a}L_2^{e_b}.
\]

This factorization is not yet a nullhomotopy in the complete exact complex of
Entry 504.  That complex retains gradient/Kodaira--Spencer data, while Entry
492 proved that the gradient nullhomotopy complex and the principal conormal
complex are distinct.  A comparison map between those degrees must be derived,
not inferred from divisibility by \(K\).

## Consequence

The failure found in Entry 504 has now been localized to the principal
\(K\)-direction, but it is not yet removed.  Multiplication by \(a^2\) can
become a derived chain operation only if the coefficient \(h(f)\) lifts
through the retained gradient/Kodaira--Spencer complex compatibly with its
differential.

This identifies the unique candidate correction and rules out a fitted
syzygy.  It does not authorize adjoining a new principal cell to the frozen
target.

The result does not yet prove Entry 503's predicted reduced quotient.  The
corrected action must now be applied to the actual stable defect homology;
its homotopy component can contribute to the induced \(a^2\)-map.

## Next gate

Solve the lifting equation for \(h(f)\) in the retained gradient/Kodaira--Spencer
complex.  If such a compatible lift exists, build the corrected \(a^2\)-action
on the actual mapping cone and compute its induced map on \(H(C_D,u)\) across
\(D\to D+2\).  If no lift exists, Entry 502's even-incidence explanation fails
in its present form.

The all-sector identity is checked by
`research/voevodsky/check_soft_axis_a2_commutator_homotopy.py`.

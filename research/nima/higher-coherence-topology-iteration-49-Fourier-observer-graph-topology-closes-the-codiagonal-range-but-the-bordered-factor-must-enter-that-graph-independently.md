# Higher-coherence topology iteration 49: Fourier-observer graph topology closes the codiagonal range, but the bordered factor must enter that graph independently

## Candidate topology

For the common-history synthesis

\[
Tc(t)=\sum_\lambda a_\lambda
\left(c_\lambda^+\tau_{L_\lambda}\Phi(t)
+c_\lambda^-\tau_{-L_\lambda}\Phi(t)\right),
\]

the full Fourier transform gives

\[
\widehat{Tc}(\xi)=\widehat\Phi(\xi)F_c(\xi),
\]

where `F_c` is the Fourier transform of the discrete measure supported at the
distinct points `+-L_lambda`. Existing work proves that `T` is injective on the
projective source.

Equip the source-generated common-history range with the graph seminorms

\[
p_{K,m,\delta}(h)
=
\|h\|_{K,m}+q_\delta(\mathcal R_Fh),
\]

where `R_F` extracts the discrete Fourier measure and divides by the nonzero
coefficients `a_lambda`. This makes `T` a topological embedding with closed
range by construction.

## Why this is not automatically circular

The recovery formula is source-derived: it uses the known theta atom, Fourier
transform, and unique signed prime-power displacements. It does not use Xi
zeros or the desired Haar cancellation.

However, declaring the graph topology is useful only if all independently
constructed target sections, especially `H_border`, are continuous elements of
the same graph. Otherwise the topology has merely excluded the obstruction by
definition.

## Quantitative interpolation

The displacement gaps can shrink roughly exponentially in `L`:

\[
\log(n+1)-\log n\asymp e^{-L}.
\]

Isolating one atom therefore costs exponential resolution. A projective Köthe
scale can absorb any fixed exponential loss by shifting `delta`. This suggests
that coefficient recovery may be tame in the projective category even though
no Hilbert lower bound exists.

The harder issue is division by `widehat Phi` and analytic continuation across
its zeros. Algebraic uniqueness uses one open interval where `widehat Phi` is
nonzero, but continuation from that interval is not a stable operation in an
ordinary rapid-history topology. The graph observer must retain the complete
Fourier quotient, not only finitely many frequencies.

## Closed-range consequence

If `T` has a continuous Fourier recovery map in the analytic Silva/Köthe
category, then its image is strict and closed. The quotient inherits the
regular connection, and iteration 48 excludes Xi torsion. The implication is

\[
\tau[H_{\rm border}]=0
\Longrightarrow
[H_{\rm border}]=0
\Longrightarrow
R=\tau S.
\]

This is now a coherent multi-topology route: labelled Köthe recovery, analytic
Silva derivative bounds, and Fourier graph strictness.

## Remaining membership gate

One must prove independently that `H_border` lies in the domain of the full
Fourier recovery observer, with seminorm bounds uniform under prime cutoff and
spectral differentiation. The known statement

\[
\Delta_{\rm border}=\tau H_{\rm border}
\]

only places `tau H_border` in the scalar bordered target. It does not establish
that `H_border` has a discrete translated-theta Fourier quotient.

A hostile `H_border` may contain a common-history component outside the
source-generated translated-theta range. Then its cokernel class is exactly the
torsion detected earlier, and the recovery graph cannot be applied to it.

## Verdict for topology 49

Fourier-observer graph topology can make the codiagonal range strict without a
false Hilbert lower bound, and shrinking prime-power gaps appear compatible
with projective exponential seminorm loss. The decisive remaining test is
whether the independently computed `H_border` belongs to this observer graph.

The final topology to test is a hybrid graph topology adjoining the bordered
Green channel to the Fourier-recoverable theta range. The key question is
whether that pushout preserves strictness or necessarily adds a new Xi-torsion
generator.
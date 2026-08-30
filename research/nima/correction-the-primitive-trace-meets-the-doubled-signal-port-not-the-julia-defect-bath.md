# Correction: the primitive trace meets the doubled signal port, not the Julia defect bath

Event 10302 matched the reciprocal Julia defect pair to the two primitive
histories. The rank match is real, but it is the wrong coefficient interface.

For one prime, the Schur signal transfer is

\[
r_p(z)=p^{-1/2}e^{iz\log p}.
\]

The missing primitive determinant term is

\[
\operatorname{tr}S(z)
=
\sum_p r_p(z).
\]

Thus the primitive channel carries the signal coefficient

\[
a_p=p^{-1/2}.
\]

The Julia defect coupling instead has magnitude

\[
d_p=\sqrt{1-a_p^2}
=
\sqrt{1-p^{-1}}.
\]

These have opposite large-prime behavior:

\[
a_p\to0,
\qquad
d_p\to1.
\]

Therefore an isometric identification of the defect bath with the primitive
history would attach the wrong arithmetic normalization. It cannot represent
the missing \(\mathfrak S_1\) trace term.

## Correct passive typing

The conservative realization has three distinct roles:

1. signal input/output:
   carries \(r_p(z)\) and therefore the primitive trace coordinate;
2. internal delay state:
   carries the source translation by \(\log p\);
3. defect bath:
   witnesses passivity/unitarity of the attenuation but is not the primitive
   Euler trace.

The bath must retain prime labels to prevent cross-prime feedback, as proved
in event 10301. But it should not be sewn directly to the primitive wall.

## Correct local meeting

After reciprocal doubling, the signal carrier is

\[
\mathcal S_p^+\oplus\mathcal S_p^-.
\]

This rank-two signal pair is the correct source for the two twisted histories:

\[
J_p^{\mathrm{sig}}:
\mathcal S_p^+\oplus\mathcal S_p^-
\longrightarrow
\mathcal H_{p,-}\oplus\mathcal H_{p,+}.
\]

In parity coordinates,

\[
J_p^{\mathrm{sig}}
=
\operatorname{diag}(j_{p,+},j_{p,-}).
\]

Its source normalization must retain the factor \(p^{-1/2}\) on the signal
side. The causal Green identity must determine how that coefficient is
distributed across the even and odd history ports.

The defect bath remains in a separate commutative square proving that
\(J_p^{\mathrm{sig}}\) is compatible with the conservative dilation. It does
not supply the trace value.

## Revised architecture

The first local packet is

\[
\begin{array}{ccc}
\text{doubled signal}_p
&\longrightarrow&
\text{primitive histories}_p\\
\downarrow&&\downarrow\\
\text{Julia signal plus bath}_p
&\longrightarrow&
\text{wall-extended causal block}_p.
\end{array}
\]

The top arrow is the primitive trace incidence. The bottom arrow is the
passive compatibility extension. Conflating them replaces \(a_p\) by \(d_p\).

## Smallest hostile

Use the defect amplitude \(d_p\) as the wall incidence coefficient. The local
colligation is exactly unitary and both reciprocal history ports may be
nonzero. Yet the primitive scalar shadow becomes

\[
\sum_p\sqrt{1-p^{-1}}\,e^{iz\log p},
\]

not

\[
\sum_pp^{-1/2}e^{iz\log p}.
\]

This hostile passes passive realization and rank matching while failing the
Euler primitive coefficient at the first atom.

## Status repair

- Event 10301 remains valid: defect baths require prime labels and cannot be
  globally collapsed into two wall ports.
- Event 10302 is corrected: reciprocal doubling gives the right local rank,
  but the primitive histories meet the doubled signal ports, not the defect
  ports.
- The missing source theorem is now the signal-to-history Green/Stokes
  incidence together with its extension to the labelled conservative
  dilation.

No boundary pencil or downstream positivity is promoted.

# Common-singlet relative parity reference

## Bounded question

Can an already admitted source field realize WP631's odd reference without
adding a new fitted orientation or abandoning the connector messenger grammar?

## Existing reference candidate

WP489 replaces both explicit messenger masses by

\[
z_A\sigma\bar AA+z_B\sigma\bar BB
\]

and gives the real gauge singlet \(\sigma\) a nonzero source-selected magnitude.
Declare \(\sigma\) odd under the sector parity, while keeping \(Q\), \(H^u\),
\(u_R\), \(S\), and \(X\) even and \(H^d\) odd. Solving every entrance,
connector, exit, and singlet-mass parity equation gives a unique assignment:

| chain | \(A_L\) | \(A_R\) | \(B_L\) | \(B_R\) | terminal quark |
|---|---:|---:|---:|---:|---:|
| up | 1 | 0 | 0 | 1 | 0 |
| down | 0 | 1 | 1 | 0 | 1 |

All declared renormalizable route vertices and both singlet-generated masses
are even. The mixed entrance kinetic term and wrong-sector entrance vertices
remain odd.

## Why the common-source mass matters

Because left and right messenger parities alternate, a bare vectorlike mass
\(M\bar A_LA_R\) or \(M\bar B_LB_R\) is odd and forbidden. The construction
therefore exists specifically on WP489's common-singlet threshold domain. It
does not compose with the earlier explicit-mass grammar while retaining the
same parity.

The scalar source already depends on \(\sigma^2\), so its radial lift remains
even. The simultaneous sign reversal

\[
(H^d,\sigma)\longmapsto(-H^d,-\sigma)
\]

admits the relative class \(I_{d\sigma}=\operatorname{sgn}(H^d)\operatorname{sgn}(\sigma)\)
at the abstract orbit level. This instantiates WP631's categorical reference
with an existing source field rather than a new port.

## Authority boundary

This is a source-derived relative-reference candidate and a stronger
presentation rigidifier. It is not yet a physical selector. The sign of a real
singlet expectation value can disappear from low-energy amplitudes after
fermion rephasings, especially because the two messenger denominators carry
two powers of \(\sigma\). A descended relative observable must be derived from
the complete matched action rather than asserted from the abstract product.

If the parity is gauged, its chiral discrete-anomaly conditions and defect
spectrum must be computed. If it remains global, simultaneous sign-related
vacua and their wall history remain. Thus the next exact gate is whether any
matched `physical16` or threshold amplitude is odd in the relative class after
all legal messenger rephasings.

## Reproduction

Run:

    python research/flavor/checkers/wp632_common_singlet_relative_parity_reference.py

The generated result is
`research/flavor/results/wp632_common_singlet_relative_parity_reference.json`.


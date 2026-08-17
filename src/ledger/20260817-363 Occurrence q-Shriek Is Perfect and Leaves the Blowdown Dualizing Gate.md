# Occurrence q-Shriek Is Perfect and Leaves the Blowdown Dualizing Gate

## Result

Write the actual Entry-356 projection as

\[
q=b\circ\operatorname{pr}_G:
G_{03}\times I_{\rm occ}\longrightarrow X.
\]

Right adjoints compose in reverse order, so

\[
q^!=\operatorname{pr}_G^!\circ b^!,
\qquad
\omega_q=\operatorname{pr}_G^!(\omega_b),
\qquad
\omega_b:=b^!\mathcal O_X.
\]

For the oriented two-point finite interval
\(I_{\rm occ}=\{h<p\}\) with the pulled-back ring, direct image along
\(\operatorname{pr}_G\) is evaluation at the initial point \(h\).
The right adjoint to evaluation is the costandard extension

\[
\operatorname{pr}_G^!N=(N\longrightarrow0).
\]

Indeed a map from an arbitrary arrow \((M_h\to M_p)\) to
\((N\to0)\) is uniquely a map \(M_h\to N\).

## Finite-projective compression

The costandard arrow has the functorial resolution

\[
0\longrightarrow(0\longrightarrow N)
\longrightarrow(N\xrightarrow{1}N)
\longrightarrow(N\longrightarrow0)
\longrightarrow0.
\]

The first two terms are the two representable interval modules tensored
with \(N\). Therefore, if \(N\) is perfect on \(G_{03}\), then
\(\operatorname{pr}_G^!N\) is perfect on
\(G_{03}\times I_{\rm occ}\). Evaluation at \(h\) recovers \(N\),
so the occurrence factor also reflects this perfectness question.
Consequently

\[
\boxed{
\omega_q\text{ is perfect}
\iff
\omega_b=b^!\mathcal O_X\text{ is perfect}.
}
\]

Thus the occurrence interval is not the remaining obstruction. The exact
finite-projective calculation is now concentrated on the stellar/barycentric
blowdown \(b\).

## Entry-176 comparison

Entry 176 constructs a chain map

\[
\mathrm{cap}_{\rm norm}:
C_\bullet(I_{\rm occ}\times I_{\rm norm},
I_{\rm occ}\times\partial I_{\rm norm})
\longrightarrow C_{\bullet-1}(I_{\rm occ})
\]

inside an explicitly labelled local double-Rees exceptional model. This is
not an \(\mathcal O_Z\)-module representing the right adjoint to
\(Rq_*\). Consequently the literal equation

\[
\omega_q=\mathrm{cap}_{\rm norm}
\]

is ill-typed. A comparison first requires a support functor from that local
relative exceptional carrier into \(D(Z,\mathcal O_Z)\), followed by a
map to the blowdown factor \(\omega_b\). Entry 176 may still supply an
oriented exceptional correction after those constructions; it is not the
global dualizing complex as currently stated.

## Exact next gate

Compute \(\omega_b=b^!\mathcal O_X\) from the finite standard resolution
using the actual order-preserving blowdown. The required test is a bounded
finite-projective compression of that incidence module. Only after such a
compression exists is a supported comparison with Entry 176 meaningful.

The exact checker
research/voevodsky/check_d03_qbang_occurrence_factor.rs verifies the
interval adjunction, the length-one projective resolution, recovery at the
initial point, and the resulting status boundary.

Delegation runs run-256bb5b54dde486982ee977963902a05 and
run-afa385dbd37b47d59cfe38b883f487cf returned only sandbox-refusal records
and are not used as mathematical evidence.

# Flat DNC Log-Node Bockstein and the Toric Framing Gate

Date: 2026-08-15  
Status: scoped finite coefficient and Bockstein theorem proved. The oriented
line-valued DNC, integral nearby-cycle lattice, toric framing comparison, and
literal entry-131/143 support map remain unconstructed. No graph admission
is claimed.

## Flat logarithmic deformation

Let
\[
\mathcal D
=
\operatorname{Spec}
k[\lambda,X,u,t]/\bigl(u-(X+\lambda)t\bigr).
\]
The defining relation is monic in \(u\), so elimination gives
\[
k[\lambda,X,u,t]/\bigl(u-(X+\lambda)t\bigr)
\simeq k[\lambda,X,t].
\]
Hence the displayed coefficient family is polynomial, and therefore flat,
over \(k[\lambda]\). No occurrence or normal parameter is inverted.

At \(\lambda=0\), the family specializes to the Rees/log-node relation
\[
u=Xt.
\]
This is a coefficient deformation of the crossing. The checker does not
promote \(\lambda\) to an oriented geometric deformation line or construct a
nearby-cycle functor.

## The finite DNC Bockstein

Use the entry-131-shaped coefficient packet
\[
dg=Xp,
\qquad
dh=up,
\]
and define
\[
z=tg-h.
\]
Then
\[
dz=(Xt-u)p=-\lambda t\,p.
\]
Thus \(z\) becomes closed on the special fibre \(\lambda=0\). The bounded
special packet retains
\[
\operatorname{Tor}_0=\langle p\rangle,
\qquad
\operatorname{Tor}_1=\langle z\rangle,
\]
both of primitive rank one.

The connecting morphism for the principal deformation ideal
\((\lambda)\) is therefore
\[
\boxed{
\beta_\lambda([z])=-t\,p.
}
\]
This is the translated formal Bockstein supplied by the DNC coefficient
family. Its sign follows from the displayed differential; it is not fitted
from an endpoint value.

The output is still \(t\)-line-valued. The theorem does not identify
\(-tp\) with the literal entry-131 edge generator or with an entry-143
Boolean/costalk state.

## Global reducible-support gate

Away from the special fibre,
\[
u=(X+\lambda)t
\]
implies
\[
V(u)=V(t)\cup V(X+\lambda).
\]
The second component is genuine. For example,
\[
(\lambda,X,t)=(2,-2,1)
\]
has \(u=0\) but \(t\ne0\). Thus the DNC coefficient family does not globally
identify normal support \(V(u)\) with the selected branch \(V(t)\).

Recovering \(t\) from \(u\) requires
\[
t=\frac{u}{X+\lambda}.
\]
Such an inverse exists only after an explicitly named localization or formal
completion. After \(\lambda\) is inverted and one completes \(X\)-adically,
\[
\frac1{X+\lambda}
=
\lambda^{-1}
\sum_{j\ge0}(-X/\lambda)^j.
\]
Every polynomial truncation has a nonzero final remainder. Therefore this is
not a global polynomial inverse and cannot define the universal support map.

## Conditional toric framing gate

A possible toric chart may be presented with an additional relation
\[
Xt=su.
\]
This relation is not part of the checker and no repository theorem currently
identifies its parameter \(s\) with the DNC parameter \(\lambda\). Even if
such a chart is supplied, it does not globally turn
\[
\beta_\lambda([z])=-tp
\]
into a scalar class. On an \(X\)-chart,
\[
t=\frac{s\,u}{X}
\]
requires \(X^{-1}\); on a \(u\)-chart,
\[
s=\frac{Xt}{u}
\]
requires \(u^{-1}\). Both operations erase one of the supports that the
construction must retain.

Accordingly \(Xt=su\) is an acceptance gate for future geometry:

- specify the line bundles carrying \(s,t,X,u\);
- construct a transition identifying the DNC and toric deformation lines;
- retain the selected \(V(t)\) branch and the extra \(V(X+\lambda)\)
  component until a relative-support operation disposes of it;
- show that \(-tp\) maps to the entry-131 purity class without a forbidden
  scalar division.

No toric framing theorem is claimed here.

## The remaining spatial comparison

The minimal missing object is an oriented line-valued specialization
\[
\operatorname{Sp}_{X,u}^{\log}(\mathcal D)
\]
and a branch-selected excess comparison
\[
\operatorname{BC}^{!,\log}_{X,u}:
\operatorname{Sp}_{X,u}^{\log}(\mathcal D)
\longrightarrow
E_{v_+}^{\mathrm{BM},\check C}.
\]
It must carry the two special generators \((p,z)\), send the deformation
Bockstein \(-tp\) to the normalized entry-131 edge purity, and land in the
literal entry-143 \(u\)-Boolean endpoint packet. It must also record how the
extra component \(V(X+\lambda)\) is treated.

The flat family and Bockstein do not construct this map. They provide its
finite coefficient shadow and a falsifier for any proposed global
identification that silently divides by \(X+\lambda\), \(X\), or \(u\).

## Falsifiers and boundary

The positive coefficient theorem is falsified if elimination of \(u\) is not
polynomial, if the family is not flat over \(k[\lambda]\), if
\(d(tg-h)\ne-\lambda tp\), if either special Tor grade is absent, or if the
Bockstein sign differs from \(-tp\).

The global gate is falsified if \(V(u)\) lacks the extra
\(V(X+\lambda)\) component or if a finite polynomial inverse to
\(X+\lambda\) exists over the stated base.

A future logarithmic nearby-cycle/Beck--Chevalley construction would not
contradict the gate because it adds branch, orientation-line, and
relative-support data absent here.

Until that comparison, its polarity conjugate, the generic \(Q\) leg, and
both endpoint connector cells exist, the physical endpoint mapping fiber is
uninstantiated. Hence \(p_{\partial,Q}\), its parity, and its Bockstein remain
undefined.

## Provenance and validation

Exact certificate:

- research/voevodsky/check_d03_dnc_log_node_bockstein_gate.rs, SHA-256
  7a3665337c0ccb03b02badf2605aed51bffde120bb72635e18dbc7a24c401f65.

The checker is explicitly scoped to finite polynomial-algebra and two-term
Bockstein facts. It does not claim runtime construction of nearby cycles,
line-valued DNC geometry, or a spatial entry-131/143 comparison.

Relevant ledger inputs are entries 131, 143, 172, 186, 190, and 191.

## Next experiment

Construct the oriented deformation line and integral log nearby-cycle
lattice for \(\mathcal D\). Then build the branch-selected comparison to the
literal entry-143 endpoint packet and test that
\(\beta_\lambda([z])=-tp\) restricts to entry 131's edge purity. Treat any
\(Xt=su\) chart as additional line-bundle framing data, not a license to
invert \(X\) or \(u\).

## Outcome contract

~~~json
{
  "claim": "The family k[lambda,X,u,t]/(u-(X+lambda)t) is polynomial and flat over k[lambda]. In the packet dg=Xp, dh=up, the class z=tg-h satisfies dz=-lambda*t*p; at lambda=0 it gives primitive Tor0/Tor1 generators and Bockstein beta_lambda([z])=-t*p. Globally V(u)=V(t) union V(X+lambda), and recovering t requires a non-polynomial localization or formal completion.",
  "status": "proved_scoped_coefficient_with_global_gate",
  "scope": "finite DNC coefficient algebra and two-term Bockstein only; no oriented line-valued DNC, nearby-cycle functor, toric framing theorem, or literal entry131/143 comparison",
  "factorization": {
    "family": "u=(X+lambda)t",
    "elimination": "k[lambda,X,t]",
    "flat_over_lambda": true,
    "packet": "dg=Xp, dh=up",
    "special_generator": "z=tg-h",
    "differential": "dz=-lambda*t*p",
    "special_Tor0_Tor1": [1, 1],
    "Bockstein": "beta_lambda([z])=-t*p",
    "global_support": "V(u)=V(t) union V(X+lambda)",
    "formal_inverse": "t=u/(X+lambda) only after named localization/completion",
    "base_inversion": false,
    "toric_Xt_equals_su": "conditional framing gate, not checker-certified",
    "oriented_DNC_line": "unconstructed",
    "integral_nearby_cycles": "unconstructed",
    "entry131_purity_comparison": "unconstructed",
    "literal_entry143_comparison": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined"
  },
  "checker_sha256": "7a3665337c0ccb03b02badf2605aed51bffde120bb72635e18dbc7a24c401f65",
  "evidence_refs": [
    "research/voevodsky/check_d03_dnc_log_node_bockstein_gate.rs",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-172 Weighted Occurrence-Normal Graph and the Cartier Nearby-Cycle Gate.md",
    "src/ledger/20260815-186 Direct Affine-Node Endpoint Descent No-Go and the Extraordinary Trace Gate.md",
    "src/ledger/20260815-190 Rees-Line Cancellation and the Log Branch-Selected Beck-Chevalley Gate.md",
    "src/ledger/20260815-191 Nodal Component Perfectness No-Go and the Relative Exceptional BM Repair.md"
  ],
  "unconstructed": [
    "oriented line-valued DNC and integral nearby-cycle lattice",
    "branch-selected log excess Beck-Chevalley map",
    "comparison of -t*p with entry-131 edge purity",
    "literal entry-143 endpoint Boolean/costalk map",
    "toric framing transition for Xt=su",
    "polarity endpoint, generic Q leg, and endpoint connectors",
    "physical mapping fiber, p, parity, and Bockstein"
  ],
  "counterevidence": [
    "The extra component V(X+lambda) prevents global support identification.",
    "Every polynomial truncated inverse of X+lambda has a nonzero remainder.",
    "The coefficient Bockstein remains t-line-valued.",
    "The toric equation Xt=su alone requires forbidden chartwise divisions to identify the framing."
  ],
  "minimal_repair": "An oriented integral log-nearby-cycle specialization with branch selection, deformation-line framing, and a Beck-Chevalley map to literal entry143 restricting to entry131 purity.",
  "next_experiment": "Construct the oriented DNC/nearby-cycle lattice and literal endpoint comparison; use any Xt=su presentation only after its line-bundle framing and support behavior are proved."
}
~~~

# Energy--Ward Comparison and Global Time Orientation

## Record

Date: 2026-08-14

Status: conditional local/tree theorem with loop residual identified at graph-homology level. Full scalar first-jet/BRST chain map remains unconstructed.

## Claim

Let \(A\) be a connected cosmological region with partial-energy normal

\[
e_A=\mathcal E_A
\]

and resolved outgoing interface-energy sum

\[
s_A
=
\sum_{e\in\partial A}
(y_{e,+}+y_{e,-}).
\]

For one boundary interface, write simply

\[
s_A=y_++y_-.
\]

The scalar conversion normal is

\[
c=e_As_A.
\]

For the corresponding Yang--Mills Ward endpoints

\[
q=-Q,
\qquad
r=Q-p_A,
\]

the physical-polarization restriction satisfies

\[
\boxed{
[P(r)-P(q)]_{\rm phys}
=
e_As_A\,g_A
}
\]

for the induced physical metric \(g_A\).

Taking the associated grade along

\[
e_A=0
\]

gives

\[
\operatorname{gr}_{e_A}
[P(r)-P(q)]_{\rm phys}
=
s_Ag_A.
\]

Under physical diagonal specialization of one interface,

\[
y_+=y_-=y_A,
\]

this becomes

\[
\boxed{
2y_Ag_A.
}
\]

Thus the factor appearing in the cosmological energy residue is the same occurrence multiplicity already identified in the scalar Cut carrier.

At the coefficient-complex level there is a polynomial map

\[
K(e_As_A)
\longrightarrow
K(e_A).
\]

Its cofiber is supported on

\[
s_A=0.
\]

Therefore away from the soft locus,

\[
s_A\neq0,
\]

the mixed energy-to-Ward comparison is a quasi-isomorphism in the one-exit model.

For \(m\) exits, the total first-order jet is the weighted Koszul exit-location complex on

\[
s_1,\dots,s_m.
\]

For a tree region, this maps to the Ward transport simplex and is exact away from simultaneous soft support.

After blowing up the soft ideal, the residual boundary class is carried by the exceptional projective simplex rather than by a new generic cosmological gauge primitive.

For a graph with loops, the remaining transport ambiguity is graph homology:

\[
H_1(G).
\]

This is the pre-existing Ward/Brauer circuit sector.

Hence the generic comparison predicts

\[
\boxed{
\text{cosmological gauge obstruction}
=
\text{soft support}
+
H_1(G),
}
\]

with no additional tree-level generic class.

Time orientation obeys a parallel equalizer principle.

If one assigns a sign to every coarse regional square root independently, spurious local sign freedom appears.

After resolving interface roots and imposing tree compatibility, all regional signs are forced equal.

The deck group reduces to

\[
\boxed{\mathbb Z_2}
\]

acting globally.

Thus time orientation is a diagonal/equalizer datum under Cuts, not a tensor product of independent regional \(\mathbb Z_2\) choices.

## Evidence

The endpoint identity follows from

\[
P_{\mu\nu}(k)=k^2\eta_{\mu\nu}-k_\mu k_\nu
\]

and restriction to the physical transverse fiber, where the longitudinal terms vanish.

The scalar endpoint difference factors as

\[
r^2-q^2=e_As_A
\]

in the local partial-energy parameterization.

The map

\[
K(e_As_A)\to K(e_A)
\]

is multiplication by \(s_A\) in the appropriate degree, so its failure to be invertible is supported precisely at \(s_A=0\).

The multi-exit tree complex is Koszul and therefore exact for a regular nonzero exit tuple.

On loops, transport around a closed route leaves the standard cycle space

\[
\ker(\partial_{\rm graph})=H_1(G).
\]

The sign equalizer follows by propagating root compatibility across every edge of a connected tree.

This entry is a retrospective reconstruction without a standalone repository certificate.

## Boundary

The following remain unproved:

- an explicit scalar first-jet-to-BRST chain map realizing every step globally;
- compatibility with arbitrary nontransverse soft/circuit intersections;
- a canonical Ward-to-Brauer chain-level equivalence;
- the loop-integrated period statement.

The equality

\[
[P(r)-P(q)]_{\rm phys}=e_As_Ag_A
\]

is a physical-state-symbol statement. It is not yet the complete off-shell cohomological theorem.

The root \(\mathbb Z_2\) is distinct from previously encountered scalar polarity and contact-orientation lines. These should not be identified without an explicit comparison.

## Consequence

The mixed cosmology/YM test removes the need for a generic tree-level cosmological gauge primitive.

The remaining hostile test moves to nonseparating topology:

\[
\text{does energy loading create loop cohomology beyond }H_1(G)?
\]

The marked theta graph is the first test.

## Outcome contract

```json
{
  "claim": "At physical-state-symbol level, the partial-energy normal maps to the Ward endpoint difference as e_A s_A g_A; its associated grade is s_A g_A and becomes 2 y_A g_A on the physical occurrence diagonal. Tree multi-exit residuals are soft-supported, loop residuals reduce to H1(G), and resolved time-root compatibility leaves one global Z2.",
  "status": "conditional",
  "assumptions": [
    "Physical transverse polarization restriction is imposed.",
    "Generic statements are away from simultaneous soft support.",
    "The complete scalar first-jet/BRST chain realization is not yet constructed."
  ],
  "evidence_refs": [
    "retrospective mixed energy-Ward derivation",
    "occurrence-resolved Cut valuation",
    "Ward transport sequence"
  ],
  "factorization_test": {
    "one_exit": "passed analytically away from soft support",
    "multi_exit_tree": "passed at Koszul/transport level",
    "loop_residual": "identified with H1(G)",
    "time_sign_equalizer": "passed on connected trees",
    "full_BRST_chain_map": "open"
  },
  "counterevidence": [
    "Soft support survives and cannot be removed by generic localization arguments.",
    "Loop circuit homology survives as a genuine pre-existing sector."
  ],
  "next_experiment": "Freeze H1(G) plus soft support as the only admissible loop sectors and test a nonseparating marked theta cut for any additional cosmological obstruction."
}
```
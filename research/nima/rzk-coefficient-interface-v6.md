# Coefficient interface v6: boundary-framed comparison

## Implemented Rzk layer

`rzk/11-boundary-framed-comparison.rzk.md` is a standalone, axiom-free module
with 13 checked definitions. It represents the framed lift as

\[
\sum_{f:X}(r(f)=\theta).
\]

X and Y are supplied mapping spaces; r is their actual restriction. They are
not plain chain-module carriers. Required admissibility (support, filtration,
scalar ring, variance and group action) must already be included in these
spaces. The theorem does not construct derived mapping spaces from complexes.

For two framed maps (f,h), (g,k), it constructs a fibre path from an ambient
path p:f=g and a comparison ap(r,p) followed by k equals h. Conversely, it
extracts those two witnesses from every fibre path. In particular, an ambient
primitive f=zero gives a framed nullhomotopy only with the compatibility of
its induced boundary path and the independently prescribed h. A separate
obstruction eliminator quantifies over all compatible primitives. Frame
revision takes an explicit path between boundary objects.

No definition chooses the physical Q-homotopy, declares a nonzero frame to
have a zero object, or infers contractibility from existence of a primitive.

## Chain-model adapter required from the physical comparison

The incoming spatial Gysin packet must specify:

1. The full source and target diagrams and their mapping-space interpretation,
   with both endpoint packets, Q, scalar domains, degrees, and variance.
2. The actual restriction r and independently constructed boundary comparison
   theta; every connector must be a cochain/path, not merely its boundary.
3. The candidate f and its supplied Q/endpoint homotopy h. Any ambient primitive
   s must be admissible in that same diagram category.
4. The realization of the compatibility type above by the relative Hom model
   D(f,h)=(d f,r(f)-d h). In that model the secondary test is h-r(s), modulo
   restrictions of closed ambient homotopies and higher boundary boundaries.

The newer target calculation gives a prospective adapter fib(E -> Q + V[1])
~= B with B the full 208-generator support complex. It must not be replaced
by B/V. Its normalization-source secondary subgroup R/(Delta), its Rees
version R'/(Delta_t), and the nodal resolution remain mathematical packet
claims, not Rzk instances in this increment. The physical identification is
being constructed separately; the interface leaves its Q-homotopy open.

## Verification

Fresh headless check through the permitted PowerShell-file command path:

`pwsh -NoProfile -File research/nima/rzk/check-boundary-framed.ps1`

Passed, exit 0, `Everything is ok!`, all 13 definitions. The entire dependency
closure is this single file; it uses built-in identity elimination and no
sHoTT or other-owner module. Results with source/executable digests are in
`results/rzk-boundary-framed-typecheck.json`. Execution reference:
`structured_command_execution:e_39824_1788728420449761700_2`.

Persistent LSP feedback was attempted but reported this file unchecked due to
an error in its staged `02a-marici-boundary-interior-chain-map.rzk.md`
dependency. That is a limitation of that LSP session, not independent evidence
of an error in the authoritative other-owner source. No other-owner file was
changed. The standalone fresh closure above avoids that staged dependency.

Sources read: `research/chatgpt/framed-target-category/framed_target_category.md`,
`endpoint-boundary-restriction/endpoint_boundary_restriction.md`,
`actual-boundary-restriction/actual_boundary_restriction.md`, and
`normalization-framed-support/normalization_framed_support.md` under the same
ChatGPT directory. Their concrete checkers were not rerun for this increment.

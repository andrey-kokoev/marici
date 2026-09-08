# v19: physical six-point source comparison

**Next checkpoint:** [`rzk-coefficient-interface-v20.md`](rzk-coefficient-interface-v20.md)
checks the additive normalization-conductor exact sequence and records the
physical roof data without pretending to invert quasi-isomorphisms.

`rzk/30-physical-source-comparison.rzk.md` is the first checked coefficient map
originating in the physical six-point source. It defines the homological
complex J with ranks `(1,4,5,1)` from the displayed integral matrices in
`research/chatgpt/physical_source_comparison.md`.

Rzk checks:

- the full differential squares to zero on all finite integral chains;
- `z=(1,0,1,0,0)` is a cycle;
- the road augmentation `a_C=(0,0,1,1,1)` annihilates every differential;
- `a_C(z)=1`;
- both endpoint coordinates are killed strictly;
- after unpacking the chain relations as `r1=r2=r3`, primitive normalization
  forces all three road coefficients to equal one.

The generated source has 11 states, 16 signed arrows, and seven cancellation
shapes. A fresh 73-file headless closure passed in 30.11 seconds. Evidence:

- `results/30-physical-source-comparison.typecheck.json`
- `results/physical-source-generation.json`

The Rzk LSP was not used.

Scope remains strict: this checks `a_C:J -> C_cond[1]`. It does not invert the
quasi-isomorphism `rho:T -> C_cond`, construct the derived roof as a morphism in
a localized category, identify physical Q with the conductor line, or transport
the physical source into the native first-jet/local target.

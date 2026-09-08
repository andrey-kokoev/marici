# v16: supported residue detects the primitive tau class

**Next checkpoint:** [`rzk-coefficient-interface-v17.md`](rzk-coefficient-interface-v17.md)
constructs boundaries for every finite integral expression in the typed
augmentation ideal `(u,s,t)`.

`rzk/27-supported-local-residue.rzk.md` defines the constant-term residue on
the unique degree-one state of the 16-state supported local complex. It selects
exactly the `(u,s,t)=(0,0,0)` monomial coefficient.

Rzk proves:

- every differential column has zero residue;
- every boundary of an arbitrary finite integral polynomial expression has
  zero residue;
- the canonical tau atom has residue one;
- therefore an asserted setoid boundary for tau would imply
  `0_Z = 1_Z`.

The module passed a fresh 72-file headless closure in 32.58 seconds. Evidence:
`results/27-supported-local-residue.typecheck.json`. The Rzk LSP was not used.

This establishes the nonzero primitive top class by an internal coefficient
detector. It is the injective/nonboundary half of the reported
`H^1 = Z[u,s,t]/(u,s,t)<tau>` classification. The converse reduction—every
degree-one coefficient with zero constant residue is a boundary—still requires
a typed monomial-factor decomposition and is not claimed here.

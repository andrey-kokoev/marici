# Four-channel free-category bridge: final scope

`FourChannelBridge.agda` starts with four typed edge families OO, OR, RO and RR on two object sorts. These families provide a graph, **not** a composition law. Cubical Agda's free-category construction adds identities and composition. Its library universal property interprets paths in any category equipped with a graph map. The ordinary Yoneda theorem applies to this resulting free category; `NativeYoneda.Adapter` packages that interpretation through the native constructor interface.

The negative control is structural, not merely a counting argument. The XOR and OR categories have definitionally identical four channel families and identical selected units, yet disagree on the square of the `true` loop. `no-composition-recovery` rules out a channel-only decoder satisfying both compositions. `source-compositions-disagree` checks the incompatible evaluations of the *same* free path. `free-square-not-unit` shows that the free category has not secretly imposed the XOR relation: its OR interpretation separates that square from the unit.

**Boundary:** This is an exact theorem about a deliberately weak four-family signature. It is neither an identification of those families with the historical table-fibration four-step schedule nor a negative result about the eight-form/twelve-rule whole-package constructor. See `PRIOR-WORK.md` for the existing native table and closure equivalences. In particular, free category completion adds formal paths; it does not recover provenance, attachment witnesses, source composition or rule admission from four edge types.

Verification (fresh source and declared negative control):

```powershell
pwsh -NoProfile -File research/nima/checkers/check_four_channel_kernel.ps1
```

This command passed after the explicit square-evaluation regression was added. Receipt: `research/nima/results/four-channel-kernel.json`. No simplex-generation or S3-action claim follows.

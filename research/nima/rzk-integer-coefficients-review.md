# Review checkpoint: integer indexing, coefficient modules, derived Hom

**Subsequent update:** [v10](rzk-coefficient-interface-v10.md) closes the
assembled integer Hom square-zero gap described below, with a concrete
Z-squared target instance. The final 82-file closure passed in 27,975 ms.
The review below records the earlier checkpoint, not the latest gap list.

## Active objective and verified state

The active objective has three distinct parts. They must not be reported as
one completed realization.

| Part | Reviewed status |
|---|---|
| Integer indexing | Module 15 instantiates shifts, successor/source alignment, composition alignment, inverse shifts, parallel-path coherence and computed parity on canonical MariciInt. |
| Concrete coefficients | Module 16 constructs Z squared, its additive and scalar-action laws, d(a,b)=(b,0), H(a,b)=(0,a), and a concrete integer-indexed Hom boundary of H in every source degree. This is a pilot, not the physical polynomial modules. |
| Derived Hom | Not implemented. No K-projective replacement or localization comparison has been supplied; raw Hom is not being identified with RHom. |

Fresh source checks already completed before this runner review:

- `rzk/15-integer-hom-indexing.rzk.md`: 23 definitions and one parity datatype;
  60-file closure passed. Result: `results/15-integer-hom-indexing.typecheck.json`.
  Execution: `structured_command_execution:e_39824_1788732026318203500_25`.
- `rzk/16-integer-coefficient-complex.rzk.md`: 29 definitions; 81-file closure
  passed. Result: `results/16-integer-coefficient-complex.typecheck.json`.
  Execution: `structured_command_execution:e_39824_1788732231021862400_27`.

The arithmetic is reused read-only from Grothendieck's source, including global
addition associativity and integer identity-path uniqueness. Closure manifests
record every file digest. The closure scan found no literal #assume declarations in
these files; this does not authenticate upstream provenance or constitute a
complete assumption audit. The staged core uses section #variables, which
Rzk prints as #assume. The v10 closure separately inventories these parameters. The persistent
LSP attempt timed out and is not counted as successful verification.

## Definition and proof review

- Shift is i+n; composition has degree q+p. The source-successor square uses
  associativity and commutativity; the target-successor square uses
  associativity. Parallel transport choices agree by integer path uniqueness.
- Negative integers retain their signed normal forms. Parity uses magnitude,
  and its successor-flip theorem includes the negative-to-zero case. Degrees
  minus one and minus two are checked odd and even, respectively.
- In Z squared, d and H are additive and integer-linear; their squares vanish.
  The contraction is derived from the actual coordinate maps and integer
  unit laws. The final Hom-boundary theorem uses the actual parity-selected
  differential and discharges constant-family transports by identity induction.
- The remaining general theorem is NOT supplied by these checks: square-zero
  of the assembled integer-indexed differential for arbitrary admitted linear
  complexes, with all transport and module-law identifications discharged.
  The earlier operator-window square-zero results remain conditional until
  that instantiation is made.
- General graded Leibniz, a packaged DG category, concrete polynomial/stalk
  modules, and derived-Hom realization remain outstanding. The Z-squared
  contraction is not evidence for a physical support contraction or Gysin map.

## Why the verification workload grew

A read-only census of the actual manifests gives:

| Closure | Files | Source bytes | Declarations |
|---|---:|---:|---:|
| Integer indexing | 60 | 256,589 | 298 |
| Z-squared pilot | 81 | 332,608 | 366 |

These are whole-file transitive closures, not minimal declaration-level slices.
Even the indexing closure imports multiplication material because an arithmetic
file contains multiple theorems. The largest file is sHoTT `01-paths.rzk.md`
(59,280 bytes, 60 declarations). The initial 30-second arithmetic run timed out;
a bounded 120-second run passed. That does not establish the source of the
cost or justify repeated timeout increases. The next run should retain timing
and partial diagnostics; source review precedes another large closure.

## Runner defects found and repaired

1. Under ErrorActionPreference=Stop, Write-Error could bypass the intended
   timeout exit 124. The bounded child runner now returns normalized exit 124,
   retains the raw process exit and partial streams, and the wrapper exits
   without a terminating diagnostic in that path.
2. Previously source and executable digests were collected after the process.
   They could describe modified files rather than the verification inputs.
   The wrapper now records pre-run hashes and rejects exit-zero verification
   if the hashes differ or an input disappears at the post-run check (exit125).
   This comparison is not filesystem locking and cannot detect a transient
   change that is restored between checks.
3. The wrapper now records duration, validates manifest target and paths,
   rejects duplicate paths, and decodes both streams as UTF8.

Shared implementation: `rzk/bounded-process.ps1`. Tests:
`rzk/test-bounded-process.ps1`, using only its own child fixture, passed 22
controls for success, failure, timeout, partial Unicode diagnostics, duration,
input mutation/deletion and PowerShell syntax. Result:
`results/bounded-process-tests.json`; execution
`structured_command_execution:e_39824_1788732537335406300_31`.
No arithmetic closure was executed by those tests.

An end-to-end check of the repaired wrapper on the single-file module 11 also
passed with a five-second bound. Result:
`results/11-boundary-framed-comparison.typecheck.json`; execution
`structured_command_execution:e_39824_1788732585986777800_32`.
The 60/81-file closures were not rerun during this runner review; their Rzk
sources were unchanged.

The structured-command PowerShell parse-check tool itself emitted a malformed
ParseFile invocation with doubled quotes around the path. That error was in
the tool wrapper, not a parsed error in the target script. Direct Parser.ParseFile
calls in the test script checked all four PowerShell files successfully.

## Next bounded formal task

Instantiate the pre/post operator laws for the assembled integer Hom families,
including linearity and transport, rather than add another synthetic complex.
After that, define the exact resolution/model comparison needed for the intended
normalization source. The physical polynomial/stalk module construction and
Gysin Q-homotopy must remain explicit dependencies; neither is supplied by the
integer pilot.

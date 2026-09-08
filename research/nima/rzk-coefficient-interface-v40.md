# v40: fixed-beta D03 specialization and X35 summand

`rzk/51-d03-fixed-beta-specialization.rzk.md` records the changed chain-level
status after the source-prescribed graph `u03=lambda*X03`: the specialized
primary `Omega` is the boundary of `S`, while the retained comparison `Z` is a
cycle with primitive detector. Its first-normal symbol is represented by a
separate type, so it is not conflated with the now-zero ordinary supported-Hom
class.

`rzk/52-x35-strict-occurrence-summand.rzk.md` records the strict two-state
occurrence summand. Its upper state has differential `-X35*Z`; hence every
positive X35 multiple of the lower class is a boundary, while the exponent-zero
lower class has primitive coefficient one. The occurrence partner remains
distinct from the native 35-normal state.

Fresh closure checks passed:

- module 51: 71 files, 28.61 seconds;
- module 52: 71 files, 26.87 seconds.

Evidence is in the corresponding `results/51-*.typecheck.json` and
`results/52-*.typecheck.json` files.

Scope: Rzk checks the specialized exact/nonexact packet and monomial X35
summand. Exact identification of the 45-term `Z03=P35 Psi`, its two endpoint
components, complete Q projection, all-unit normal-frame conjugacy, and exact
annihilator over the singular full ring remain certificate-backed. No physical
conductor--Morse identification or Delta_J value is asserted.

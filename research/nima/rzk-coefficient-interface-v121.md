# v121: verified five-cutoff Smith laws

The integral checker now verifies family-level identities rather than merely
printing five Smith tables. For `D=4n`, `n=3,...,7`, it checks after L2
completion:

- invariant factors lie in `{1,2,14,42}`;
- unit count is `n(6n+5)`;
- pure-2 count is `n(2n-3)`;
- nonunit count and 2-primary exponent are `n(2n+1)`;
- 7-primary exponent is `4n=D`.

These assertions are exact consequences of the five computed integer Smith
forms. They expose a rigid finite-family pattern suitable for an eventual
symbolic induction, but are not themselves an all-degree theorem.

`rzk/149-soft-d1-five-cutoff-smith-laws.rzk.md` passes all eight declarations
without assumptions.

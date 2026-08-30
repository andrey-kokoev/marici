# The valuation shortcut fails, but translation period 729 also fails

## Proposed shortcut

A nonzero translation period for the contextual Smith sequence would make every valuation coordinate bounded. Therefore unbounded terminal Smith valuation would immediately prove that the future trace has no nonzero period.

## Hostile result

The first record-breaking snake valuations occur at

\[
(0,0),(8,1),(17,2),(71,3),(152,5).
\]

This resembles a Hensel branch. But the three representatives lifting (152) from modulus (243) to modulus (729) are

\[
152,quad395,quad638,
\]

with snake valuations

\[
5,quad4,quad4.
\]

None reaches valuation six. Thus the naive local Hensel-lift explanation terminates, and unboundedness is not established by that branch.

A sweep over (0\le n<729) finds no value larger than five.

## Periodicity result

Despite that failure, every proposed period (1\le p\le100) has an explicit witness on the same bounded window.

More sharply, period (729) fails:

\[
R(152)=(2,4,11),
\qquad
R(881)=(2,4,12).
\]

Equivalently, the snake valuation increases from five to six under translation by (729) at that grade.

This is structurally important. Low grades repeat after (729):

\[
R(0)=R(729),quad R(1)=R(730),quad R(2)=R(731),
\]

yet the translation fails deeper in the same observation sequence. Finite prefix agreement is therefore not a period certificate.

## Current classification

- The contextual trace is faithful on the tested bounded grade interval.
- Periods (1) through (100) and period (729) are falsified.
- The first apparent valuation-lift branch does not by itself prove unboundedness.
- No unbounded no-period theorem has yet been proved.

The next proof must use the exact integral recurrence to explain why a translation can preserve shallow Smith data while changing a deeper determinantal valuation. Another census is insufficient.

## Evidence

- Checker: `research/strominger/checkers/periodicity_shortcut_falsifier.py`
- Result: `research/strominger/results/periodicity_shortcut_falsifier.json`
- Sweep execution: `structured_command_execution:e_2512_1787935943550161100_33`
- Period-729 hostile: `structured_command_execution:e_2512_1787935975671451300_35`

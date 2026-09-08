# 1689 — Quotienting to the Reachable Image Cannot Detect a Relative Class

## Typing correction

Entry 1688 proposes removing the conserved kernel and replacing the padded
target by the reachable image. For

\[
F_{D,n}:P_{\le D}\longrightarrow P_{\le D+n},
\]

this produces

\[
\overline F_{D,n}:
P_{\le D}/\ker F_{D,n}
\longrightarrow
\operatorname{im}F_{D,n}.
\]

But the first isomorphism theorem gives, canonically,

\[
\boxed{
P_{\le D}/\ker F_{D,n}
\simeq
\operatorname{im}F_{D,n}.
}
\]

No rank computation is needed. The proposed reduced comparison is an
isomorphism by construction.

## Narrow result

\[
\boxed{
\text{quotienting to the reachable image cannot detect a stable relative coefficient class.}
}
\]

The conserved Hamiltonian powers found in Entry 1688 are genuine kernel data,
but once they are quotiented, defining the target to be the image removes every
cokernel tautologically.

Any legitimate relative defect requires an independently declared target
object—for example a source moment filtration, positivity completion, Cut
support, or boundary condition—not an image fitted after seeing the map.

## Evidence

- Entry 1688's typed finite maps and kernels;
- the first isomorphism theorem for linear maps.

## Next falsifier

Use the independently declared finite Hankel/moment filtration of Entries
1678--1680 as target. Determine which dynamically reachable moments satisfy its
positivity and consistency relations, and compute the comparison cone without
replacing the target by the image.
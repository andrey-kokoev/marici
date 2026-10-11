# Cycling through the three positions of one face

## Two different cycles must not be conflated

The stored proton selects a vector with the character omega=exp(2pi i/3) of X C X^-1, where X has columns (face centroid, first corner, second corner). This operator cycles the three columns of that SMALL triangle. It is not the rigid spatial rotation that fixes the whole face and takes AB to BC to CA.

Fresh exact tests distinguish the operators on all four source faces. Confusing them would incorrectly assign the proton's entire selected vector a single spatial rotation phase.

## Actual face-stabilizer transport

For an outward-oriented face ABC, the spatial 120-degree rotation R fixes its center F and cycles its corners. The three selected proton vectors are

    v_AB=F+omega A+omega^2 B,
    v_BC=F+omega B+omega^2 C,
    v_CA=F+omega C+omega^2 A.

They satisfy R v_AB=v_BC, R v_BC=v_CA, R v_CA=v_AB. Their sum is zero. Transporting each vector back to its own reference frame instead gives the same nonzero reference vector. Thus “combine the three” is ambiguous: ambient addition and frame-aligned coefficient comparison are different operations.

Let n be the outward normal and H=i[n]_cross. The selected vector is tangential but contains both circular polarizations. Its positive and negative polarization norm fractions are exactly 4/5 and 1/5. Under the spatial rotation these components acquire omega^-1 and omega respectively. The full selected vector is not an eigenvector of R; it moves between the three local placements.

The original geometry already exhibited the corresponding mean polarization 3/5 and variance 16/25. This audit recovers those weights in the actual one-face rotation comparison, rather than replacing the proton by a polarization-projected variant.

## Electron on the same oriented face

The stored face line is P=(I-n.sigma)/2. The continuous spin lift of the same outward 120-degree spatial rotation is

    U=I/2-i sqrt(3)(n.sigma)/2.

On the retained negative-polarization line,

    U P=exp(i*pi/3) P,
    U^3=-I.

The face placement returns after three steps, but the lifted spinor changes sign. Six steps return the lifted coefficient. The opposite lift of the same endpoint spatial rotation would change the one-step phase; the displayed choice retains the continuous rotation path and its full-turn sign.

## Common comparison table

| Operation | Original proton state | Electron face state |
|---|---|---|
| Advance one face-edge position by spatial rotation | Move to the next small-triangle vector; its two circular components pick opposite cube-root phases | Same face line, multiplied by exp(i*pi/3) |
| Three advances, a full spatial turn | Return exactly | Return with minus sign |
| Compare in transported local frames | One unchanged scalar amplitude per reference vector | Phase depends on whether the spin frame is transported; the lift still retains the full-turn history |
| Forget all frame/position labels and sum | The three ambient proton vectors cancel | Not a substitute for retained spinor transport |

There is a useful local relation: exp(i*pi/3)^2=omega. The electron line's squared rotation character matches the NEGATIVE circular component of the proton's vector. It does not equal the entire original proton state, whose other component has weight 4/5. Phase squaring alone neither creates the three centroid triangles nor supplies a whole-particle composition law.

## Disposition

The comparison does not support merely calling the electron an unfinished version of the proton. It identifies two specific differences: retained position/frame data and vector versus spinor transport. A possible nonlinear bridge should compare the spinor square with an explicitly selected circular vector channel, retain the complementary channel, and verify inter-face sewing. The prior `electron-charge-spin-frontier.md` already contains a quadratic Cartan-root construction; that work should be reused rather than reinvented.

## Verify

    uv run --with sympy python research/voevodsky/checkers/check_face_cycle_state_comparison.py

Results: `results/face_cycle_state_comparison.json`. All four source faces are checked exactly: corner rotation, small-triangle character equations, transported vectors, cancellation, polarization fractions, stored Pauli projectors and spinorial phases. No new particle identification or physical energy law is asserted.

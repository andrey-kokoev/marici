# v86: D35/D04 strict input gate

The native variance-mate report is unchanged and was already admitted at v85.

The D35 input-gate checker was rerun against `research/chatgpt`. It found 11 of
18 unconditional inputs available and 7 missing, and performed zero new spatial
chain calculations. The Branch-B framed-support audit independently returned
`decision_3_input_consumption_incomplete` with zero new mathematical assertions.

`rzk/112-d35-strict-input-gate.rzk.md` records that the D35/D04 spatial
comparison has not been tested. This is an input-access stop, not a mathematical
no-go. The formal strict pullback requires the component square-zero equations,
chain-map equations for `q` and `pi`, and action intertwining. Missing matrix,
frame, and action blocks are not replaced by zero.

The Rzk module passes a fresh check.

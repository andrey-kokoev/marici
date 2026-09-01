# Split minimal amplitude-system obstruction: WP1162

## Question

Can a split minimal \(9+9\) support-four carrier satisfy the amplitude system
and fixed-\(q\) target?

## DPC resolution

- **Problem:** solve the minimal amplitude-equality system after WP1161.
- **Conjecture:** a split minimal support-four carrier has a phase-compatible
  fixed-\(q\) interior point.
- **Rivals:** split minimal carrier witness; amplitude equality classes;
  fixed-\(q\) linear consistency; connected minimal carrier.
- **Risky consequences:** \(7\,200\) split minimal carriers, ten amplitude
  equality classes, rank-nine linear system, and fixed-\(q\) consistency.
- **Falsification attempt:** amplitude propagation reduces every split carrier
  to ten classes; the resulting fixed-\(q\) linear system is inconsistent for
  all \(7\,200\).
- **Residual:** \(43\,200\) connected minimal carriers, \(16\,200\) type
  \(10+10\) carriers, and \(1\,350\) type \(12+12\) carriers remain open.
- **Disposition:** reject all split minimal \(9+9\) carriers for fixed-\(q\)
  phase compatibility.

Checker: `research/flavor/checkers/wp1162_minimal_amplitude_system_no_go.py`

Result: `results/wp1162_split_minimal_amplitude_no_go.json`

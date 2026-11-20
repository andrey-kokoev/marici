"""Replay fixed codes on the first 20 addresses of five catalogue records in file order."""
from pathlib import Path
from pauli_realization_audit import decode_graph6
from ramsey_paired_interval_codec import run as pair
from ramsey_rolling_lookahead_codec import run

if __name__=='__main__':
    data=Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6'
    for number,line in enumerate(data.read_text().splitlines()[:5],1):
        rows=decode_graph6(line);M=[[(r>>j)&1 for j in range(20)] for r in rows[:20]]
        print(number, pair(M),run(M,False),run(M,True),flush=True)

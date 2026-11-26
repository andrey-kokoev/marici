"""Replay the (2,2) census from catalogues. Argument: executable compiled from ramsey_k33_22_first.cpp (C++17). Requires python-sat and igraph; use OS TEMP for the regenerable full placement tables. Output process must succeed before a later stage can consume its file."""
from ramsey_three_by_three_projections import marks
from ramsey_k33_22_deck import T,graphs
from pathlib import Path
import sys,subprocess,json
if __name__=='__main__':
 path=Path(__file__).resolve().parent;sig=T/'k22marks.txt';sig.write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(marks(57)) if len(r)==5));h=graphs();inp=''.join(' '.join(map(str,g))+'\n' for g in h)
 with (T/'k22sides.txt').open('w') as f:subprocess.run([sys.argv[1],str(sig)],input=inp,text=True,stdout=f,check=True)
 for s in ['deck','mutual','seam','seam_verify']:subprocess.run([sys.executable,str(path/f'ramsey_k33_22_{s}.py')],check=True)

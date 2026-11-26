"""Replay asymmetric (1,2) exclusion. Arguments: compiled ramsey_k33_12_first.cpp and compiled ramsey_k33_22_first.cpp (the latter now accepts an explicit base order). Needs catalogue files, python-sat and igraph. Large intermediates are regenerable in OS TEMP."""
from ramsey_three_by_three_projections import marks
from ramsey_k33_22_deck import T,graphs
from pathlib import Path
import sys,subprocess
if __name__=='__main__':
 path=Path(__file__).resolve().parent;tab=marks(57);f4=T/'k22marks.txt';f5=T/'k12marks.txt'
 for name,n in [(f4,4),(f5,5)]:name.write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(tab) if len(r)==1+n))
 with (T/'k12sides.txt').open('w') as f:subprocess.run([sys.argv[1],str(f5)],input=''.join(' '.join(map(str,h))+'\n' for h in graphs()),text=True,stdout=f,check=True)
 def call(s):subprocess.run([sys.executable,str(path/f'ramsey_k33_12_{s}.py')],check=True)
 call('deck')
 with (T/'k12graphs15.txt').open() as g,(T/'k12sides15.txt').open('w') as f:subprocess.run([sys.argv[2],str(f4),'15'],stdin=g,stdout=f,check=True)
 for s in ['mutual','seam','verify']:call(s)

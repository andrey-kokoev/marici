"""Regenerate the five-deletion census on the Google witness. python ... WORK_DIRECTORY [WORKERS]; requires Rust. Keep work directory for full per-core certificates. With 14 workers uses the archived ordering and shard names."""
from pathlib import Path
import itertools,concurrent.futures,subprocess,sys,os
K=Path(__file__).resolve().parent

def main():
 w=Path(sys.argv[1]).resolve();w.mkdir(parents=True,exist_ok=True);n=int(sys.argv[2]) if len(sys.argv)>2 else 14;exe=w/('all5probe.exe' if os.name=='nt' else 'all5probe');matrix=K.parents[1]/'grothendieck/r312_google_52.txt'
 subprocess.run(['rustc','-O','-C','target-cpu=native','--edition=2021',K/'ramsey312_four_deletion_probe.rs','-o',exe],check=True)
 fs=[(w/f'all5shard{i}').open('w') for i in range(n)]
 try:
    for i,d in enumerate(itertools.combinations(range(52),5)):print(*d,file=fs[(i//250)%n])
 finally:
    for f in fs:f.close()
 def part(i):
    with (w/f'all5run{i}.txt').open('wb') as out:subprocess.run([exe,matrix,w/f'all5shard{i}','--sweep'],stdout=out,check=True)
 with concurrent.futures.ThreadPoolExecutor(n) as ex:list(ex.map(part,range(n)))
 subprocess.run([sys.executable,K/'ramsey312_collect_five_sweep.py',*[w/f'all5run{i}.txt' for i in range(n)]],check=True)
if __name__=='__main__':main()

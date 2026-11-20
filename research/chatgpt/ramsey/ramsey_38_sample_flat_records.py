"""Fixed quantile sample (including endpoints), both five-bit collision geometries. Pass Rust checker executable path."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import gzip,sys,subprocess,os,hashlib

def main():
    data=Path(__file__).with_name('pauli-realization-catalogues').joinpath('r38_27.g6.gz').read_bytes();ls=gzip.decompress(data).splitlines();print('graph6 stream sha256',hashlib.sha256(gzip.decompress(data)).hexdigest(),'records',len(ls),flush=True)
    def test(i):
        l=ls[i];assert l[0]==90;b=''.join(f'{v-63:06b}' for v in l[1:]);a=[0]*27
        for y in range(27):
            for x in range(y):
                if b[y*(y-1)//2+x]=='1':a[y]|=1<<x;a[x]|=1<<y
        outputs=[]
        for three in [False,True]:
            env=dict(os.environ);env.pop('THREE_FLATS',None)
            if three:env['THREE_FLATS']='1'
            r=subprocess.run([sys.argv[1],'3','1','0'],input=' '.join(map(str,a)),text=True,capture_output=True,check=True,env=env).stdout.strip();outputs.append(r.replace('\n','; '))
            if 'layout' in r:break
            assert r.splitlines()==['exhausted 3','exhausted 1','exhausted 0']
        return (i+1,outputs)
    with ThreadPoolExecutor(8) as pool:
        for r in pool.map(test,[j*(len(ls)-1)//7 for j in range(8)]):print(*r,flush=True)
if __name__=='__main__':main()

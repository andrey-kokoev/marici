"""Exact, search-free transport of a newly repeated column through one fill."""
def mv(B,v):return tuple(sum(x*y for x,y in zip(row,v)) for row in B)
def transpose(B):return tuple(zip(*B))
def table(masks):return tuple(tuple(m>>i&1 for m in masks) for i in range(3))

def main():
    pre=table(range(1,8));post=table([1,2,7,4,5,6,7]);delta=tuple(tuple(b-a for a,b in zip(r,s)) for r,s in zip(pre,post))
    v=(0,0,1,0,0,0,-1);u=mv(delta,v);new=mv(transpose(post),u)
    assert mv(post,v)==(0,0,0) and mv(pre,v)==tuple(-x for x in u)
    assert u==(0,0,1) and new==post[2]
    print('before',mv(pre,v),'after',mv(post,v),'change',u,'transported support',[i for i,x in enumerate(new,1) if x])
    assert all(tuple(pre[i][j] for i in range(3))==tuple(post[i][j] for i in range(3))==tuple(int(i==k) for i in range(3)) for j,k in [(0,0),(1,1),(3,2)])

if __name__=='__main__':main()

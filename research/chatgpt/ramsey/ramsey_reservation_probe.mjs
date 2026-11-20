// Failed-color test for one side-exchange link orbit. Vertices 0..15 are host sites and 16..21 future sites. Return concrete monochromatic cliques forced after conditioning the pair-mask domains.
export function singleProbe(ids,domains,graph,N,A,table=false){
 function conflict(ds){const [S,R]=graph(ids,ds.map(d=>d.reduce((x,y)=>x&y,3))),[,P]=graph(ids,ds.map(d=>d.reduce((x,y)=>x|y,0)));
 for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)if((R[i]>>j&R[i]>>k&R[j]>>k)&1)return {color:'red',sites:[16+i,16+j,16+k]};
 for(let m=1;m<64;m++){let old=65535,sites=[],blue=true;for(let i=0;i<6;i++)if(m>>i&1){if(m&P[i]){blue=false;break}old&=~S[i];sites.push(16+i)}if(!blue||A[old]+sites.length<7)continue;while(sites.length<7){let b=old&-old,i=31-Math.clz32(b);old^=b;if(A[old&~N[i]]+1+sites.length>=7){sites.push(i);old&=~N[i]}}return {color:'blue',sites}}
 return null}
 if(table){let rows=[];for(const a of domains[0])for(const b of domains[1])for(const c of domains[2])rows.push({masks:[a,b,c],clique:conflict([[a],[b],[c]])});return rows}
 for(let p=0;p<3;p++)for(let bit of [1,2]){let no=domains[p].filter(v=>!(v&bit)),yes=domains[p].filter(v=>v&bit);if(!no.length||!yes.length)continue;let test=d=>conflict(domains.map((v,i)=>i===p?d:v));let whenBlue=test(no);if(!whenBlue)continue;let whenRed=test(yes);if(whenRed)return {pair:p,bit,whenBlue,whenRed}}
 return null
}

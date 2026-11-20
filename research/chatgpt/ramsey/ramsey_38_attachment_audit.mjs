// node ramsey_38_attachment_audit.mjs r38_27.g6.gz (McKay catalogue).
import fs from 'node:fs'; import {gunzipSync} from 'node:zlib';
const lines=gunzipSync(fs.readFileSync(process.argv[2])).toString('ascii').trimEnd().split(/\r?\n/);
let roots=[0,0,0,0],graphs=[0,0,0,0],examples={},first=[];
for(let g=0;g<lines.length;g++){
 const s=lines[g],a=new Int32Array(27);if(s.length!==60||s[0]!=='Z')throw Error('graph6');
 for(let j=1,k=0;j<27;j++)for(let i=0;i<j;i++,k++)if((s.charCodeAt(1+Math.floor(k/6))-63)>>(5-k%6)&1){a[i]|=1<<j;a[j]|=1<<i;}
 let flags=0;
 for(let v=0;v<27;v++){
  let seen=new Set(),pairs=true,hist=Array(8).fill(0),n=0;
  for(let u=0;u<27;u++)if(u!==v&&!(a[v]>>u&1)){
   let t=a[v]&a[u],b=t,c=0;while(b){b&=b-1;c++;}hist[c]++;pairs&&=c===2;seen.add(t);n++;
  }
  const type=+pairs+2*(seen.size===n);roots[type]++;flags|=1<<type;
  const rec={record:g+1,v,degree:26-n,hist,duplicateExcess:n-seen.size};if(g===0)first.push(rec);if(!examples[type])examples[type]=rec;
 }
 for(let t=0;t<4;t++)if(flags>>t&1)graphs[t]++;
}
console.log(JSON.stringify({records:lines.length,roots,graphs,examples,first},null,2));

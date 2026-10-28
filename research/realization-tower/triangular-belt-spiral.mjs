// Colour order on a triangular node array. Coordinates sum to side-1.
// Peel each perimeter and repeat on the inner triangle; this adds no links.
export function triangularBeltSpiral(side=6){
 if(![4,5,6].includes(side))throw Error('Supported triangular belt sides are four, five and six');
 const runs=[],points=[];let offset=0,n=side-1;
 function run(coords){if(!coords.length)return;const role=runs.length%2===0?'proton':'electron',index=runs.length;const entries=coords.map(p=>({coordinates:p.map(x=>x+offset),role,run:index,step:points.length+1}));for(const entry of entries){entry.step=points.length;points.push(entry);}runs.push({index,length:entries.length,role,steps:entries.map(e=>e.step)});}
 while(n>=0){
  run(Array.from({length:n+1},(_,j)=>[n-j,j,0]));
  run(Array.from({length:n},(_,j)=>[0,n-j-1,j+1]));
  run(Array.from({length:Math.max(0,n-1)},(_,j)=>[j+1,0,n-j-1]));
  offset++;n-=3;
 }
 return {runs,points};
}

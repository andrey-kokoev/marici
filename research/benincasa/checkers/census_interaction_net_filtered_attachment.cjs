#!/usr/bin/env node
"use strict";
const fs=require("fs");
const matrixLines=fs.readFileSync(process.argv[2],"utf8").split(/\r?\n/);
const labels=JSON.parse(fs.readFileSync(process.argv[3],"utf8")).labels;
function isTop(label){return label[0]===3 && label.slice(1,6).every(x=>x===2);}
let topColumns=0;
for(const label of labels) if(isTop(label)) topColumns++;
let topOnly=0,lowerOnly=0,mixed=0,empty=0;
const mixedWidths=[];
const lowerBlocks=new Map();
for(let i=1;i<matrixLines.length;i++){
 const line=matrixLines[i]; if(!line){empty++;continue;}
 let t=0,l=0;
 for(const entry of line.split(",")){
  const column=Number(entry.slice(0,entry.indexOf(":")));
  if(isTop(labels[column]))t++; else {
   l++;
   const label=labels[column], key=label[0]+":"+label.slice(1,6).join("");
   lowerBlocks.set(key,(lowerBlocks.get(key)||0)+1);
  }
 }
 if(t&&l){mixed++;mixedWidths.push([t,l]);}
 else if(t)topOnly++;
 else lowerOnly++;
}
const widthHistogram={};
for(const [t,l] of mixedWidths){const k=t+":"+l;widthHistogram[k]=(widthHistogram[k]||0)+1;}
process.stdout.write(JSON.stringify({
 schema:"marici.filtered-residual-attachment-census.v1",
 columns:labels.length,top_columns:topColumns,lower_columns:labels.length-topColumns,
 rows:matrixLines.length-2,top_only_rows:topOnly,lower_only_rows:lowerOnly,mixed_rows:mixed,
 mixed_width_histogram:Object.entries(widthHistogram).sort((a,b)=>b[1]-a[1]),
 lower_block_occurrences:Object.fromEntries([...lowerBlocks].sort((a,b)=>b[1]-a[1]))
},null,2)+"\n");

#!/bin/bash
for((j=0; j<21; j++))
do
  rm -rf $j
  mkdir $j
  cp umbrella.mdp  water.top equil_${j}.gro table.xvg $j
  cp sub.pbs $j 
  qsub -v num="$j" $j/sub.pbs
  sleep 1
done

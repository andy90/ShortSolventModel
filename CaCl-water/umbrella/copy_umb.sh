for ((i=0; i<21; i++))
do
  cp $i/pullx.xvg ./pullx_$i.xvg
  cp $i/pullf.xvg ./pullf_$i.xvg
  cp $i/md.tpr ./umbrella_$i.tpr
done

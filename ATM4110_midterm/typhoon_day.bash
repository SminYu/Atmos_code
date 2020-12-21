#!/bin/bash

#KOMPASU  100901-100903
typhoon=( "KOMPASU"  "20100901" "20100903"
#RUSA     020830-020901
	  "RUSA"     "20020830" "20020901"
#MAEMI    030912-030913
          "MAEMI"    "20030912" "20030913"
#MEGI     040817-040819
          "MEGI"     "20040817" "20040819" 
#NARI     070913-070918
          "NARI"     "20070913" "20070918"
#DIANMU   100810-100812
	  "DIANMU"   "20100810" "20100812"
#RAMMASUN 020704-020706
	  "RAMMASUN" "20020704" "20020706"
#EWINIAR  060709-060710
	  "EWINIAR"  "20060709" "20060710")

for n in `seq 0 7`;do
  name="${typhoon[((0+3*$n))]}"
  t1="${typhoon[((1+3*$n))]}"
  t2="${typhoon[((2+3*$n))]}"
  echo $n ${name} ${t1} ${t2}
  rm -f ./result/${name}_${t1}.txt ./result/"day"_${name}_*.png
  while [ $t1 -le $t2 ];do
    yy=${t1:0:4}
    mmdd=${t1:4:4}
    julian=`date -d "$t1" +%j`
    for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do
      lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
      lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
      echo "typhoon_pt.bash "${name}" "$t1","$j","$hh
      awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt | awk '{if (NR=='$julian') {print $0}}' | awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' >> ./result/${name}_${t1}.txt
    done
    ncl ./ncl/${name}_${mmdd}.ncl
    convert ./result/${name}${mmdd}.ps ./result/"day"_${name}_${mmdd}.png
    rm ./result/${name}${mmdd}.ps
    t1=`date -d "$t1 1days" +%Y%m%d`
  done
done



#!/bin/bash

#KOMPASU  100901-100903
typhoon=( "KOMPASU"  "2010090100" "2010090323"
#RUSA     020830-020901
	  "RUSA"     "2002083000" "2002090123"
#MAEMI    030912-030913
          "MAEMI"    "2003091200" "2003091323"
#MEGI     040817-040819
          "MEGI"     "2004081700" "2004081923" 
#NARI     070913-070918
          "NARI"     "2007091300" "2007091823"
#DIANMU   100810-100812
	  "DIANMU"   "2010081000" "2010081223"
#RAMMASUN 020704-020706
	  "RAMMASUN" "2002070400" "2002070623"
#EWINIAR  060709-060710
	  "EWINIAR"  "2006070900" "2006071023")
	  
for n in `seq 0 7`;do
  name="${typhoon[((0+3*$n))]}"
  t1="${typhoon[((1+3*$n))]}"
  t2="${typhoon[((2+3*$n))]}"
  echo $n ${name} ${t1} ${t2}
  rm -f ./result/"hour"_${name}_*.png
  while [ $t1 -le $t2 ];do
    yy=${t1:0:4}
    ymd=${t1:0:8}
    mm=${t1:4:2}
    dd=${t1:6:2}
    hh=${t1:8:2}
    julian=`date -d "$ymd" +%j`
    rm -f ${t1}_${name}_"pt".txt
    for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

      lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
      lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
      echo "typhoon_hour.bash "${name}" "$t1","$j","$hh
      awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt | awk '{if (NR=='$julian') {print $0}}' | awk '{printf '$j'", "'$lat'", "'$lon'", "; printf $'$((10#${hh}+10#1))'; printf ",\n"}' >> ./result/${t1}_${name}_"pt".txt	
    done
    ncl ./ncl/${name}_${mm}${dd}${hh}.ncl
    convert ./result/${name}${mm}${dd}${hh}.ps ./result/"hour"_${name}_${mm}${dd}${hh}.png
    rm -f ./result/${name}${mm}${dd}${hh}.ps
    t1=`date -d "$ymd $hh 1hours" +%Y%m%d%H`
  done
  convert -delay 20 -loop 0 ./result/"hour"_${name}_*.png ./result/${name}.gif
done


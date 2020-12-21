#!/bin/bash
 
rm -f ./result/11year.txt
rm -f ./result/summer.txt
rm -f ./result/winter.txt
 

#yearly sum
for i in `seq 2000 2010`;do
	rm -f "./result/${i}_year.txt"
        for j in `awk '{print $1}' ./KOREA_rain/$i/station${i}.dat`;do
        lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/$i/station${i}.dat)
        lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/$i/station${i}.dat)
        awk '$25 ~ /'$i'/ {for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./station_pt/${j}station_pt.txt >> ./result/${i}_year.txt
        done
done

 
#11year sum
for j in `awk '{print $1}' station_all.dat`;do
        lat=$(awk '/'^$j'/{print $2}' station_all.dat)
        lon=$(awk '/'^$j'/{print $3}' station_all.dat)
        awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum/11; printf ",\n"}' ./station_pt/"$j"station_pt.txt >> ./result/11year.txt
done

#season sum
for j in `awk '{print $1}' station_all.dat`;do
        lat=$(awk '$1 == '$j' {print $2}' station_all.dat)
        lon=$(awk '$1 == '$j' {print $3}' station_all.dat)
        awk '$25 ~ /,6/ || $25 ~ /,7/ || $25 ~ /,8/ {for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum/11; printf ",\n"}' ./station_pt/"$j"station_pt.txt >> ./result/summer.txt
        awk '($25 ~ /,1/ && $25 !~ /,10/ && $25 !~ /,11/) || $25 ~ /,12/ || $25 ~ /,2/ {for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum/11; printf ",\n"}' ./station_pt/"$j"station_pt.txt >> ./result/winter.txt
done
ncl ./ncl/summer.ncl
ncl ./ncl/winter.ncl
ncl ./ncl/11year.ncl
convert ./result/summer.ps ./result/summer.png
convert ./result/winter.ps ./result/winter.png
convert ./result/11year.ps ./result/11year.png
rm -f ./result/summer.ps
rm -f ./result/winter.ps
rm -f ./result/11year.ps
for y in `seq 2000 2010`;do
	ncl ./ncl/"${y}_year.ncl"
	convert ./result/${y}_year.ps ./result/${y}_year.png
	rm -f ./result/${y}_year.ps
done


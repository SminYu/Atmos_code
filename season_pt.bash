#!/bin/bash
 
rm -f ./result/summer_mean.txt
rm -f ./result/winter_mean.txt
 
#11yearr_avg for every months
for j in `awk '{print $1}' station_all.dat`;do
        lat=$(awk '$1 == '$j' {print $2}' station_all.dat)
        lon=$(awk '$1 == '$j' {print $3}' station_all.dat)
        awk '$25 ~ /,6/ || $25 ~ /,7/ || $25 ~ /,8/ {for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum/11; printf ",\n"}' ./station_pt/"$j"station_pt.txt >> ./result/summer_mean.txt
        awk '$25 ~ /,11/ || $25 ~ /,12/ || $25 ~ /,1/ && $25 !~ /,10/ {for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum/11; printf ",\n"}' ./station_pt/"$j"station_pt.txt >> ./result/winter_mean.txt
done


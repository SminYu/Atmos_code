#/bin/bash

rm -f ./station_pt/*station_pt.txt

for i in `seq 2000 2010`;do
    for m in `seq 1 12`;do
        for j in `awk '{print $1}' ./KOREA_rain/$i/station${i}.dat`;do
                if (( $i <= 2007 ));then
                        awk -F "|" '$2 == '$i' && $3 == '$m' {for (l=33;l<=56;l++) printf "%05d ", $l; printf "'$i','$m'"; printf "\n"}' ./station/"$j"station.txt >> ./station_pt/"$j"station_pt.txt
                elif (( $i == 2008));then
                        awk -F "|" '$2 == '$i' && $3 == '$m' {for (l=29;l<=52;l++) printf "%05d ", $l; printf "'$i','$m'"; printf "\n"}' ./station/"$j"station.txt >> ./station_pt/"$j"station_pt.txt
                elif (( $i == 2009 ));then
                        awk -F "," '$2 ~ /'$i'/ && $2-20090000 > '$m*100' && $2-20090100 < '$m*100' {for (l=3;l<=26;l++) printf "%05d ", 10*$l; printf "'$i','$m'"; printf "\n" }' ./station/"$j"station.txt >> ./station_pt/"$j"station_pt.txt
                else (( $i == 2010 ));
                        awk -F "," '$2 ~ /'$i'/ && $2-20100000 > '$m*100' && $2-20100100 < '$m*100' {for (l=3;l<=26;l++) printf "%05d ", $l; printf "'$i','$m'"; printf "\n" }' ./station/"$j"station.txt >> ./station_pt/"$j"station_pt.txt
                fi
        done
    done
done

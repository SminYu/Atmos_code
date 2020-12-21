#!/bin/bash
#223 is missing data

rm -f ./station/*

for i in `seq 2000 2010`;do
        for j in `awk '{print $1}' ./KOREA_rain/$i/station${i}.dat`;do
                grep '^'$j'' ./KOREA_rain/$i/"$i"sfc.txt >> ./station/"$j"station.txt
        done
done


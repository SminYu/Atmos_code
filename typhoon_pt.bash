#!/bin/bash

#KOMPASU 100901-100903

rm -f ./result/20*_KOMPASU_pt.txt
for i in `seq 20100901 20100903`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_KOMPASU_pt.txt

  done
done

#RUSA 020830-020901

rm -f ./result/20*_RUSA_pt.txt

t1=20020830
t2=20020901

while [ $t1 -le $t2 ];do

  yy=${t1:0:4}
  julian=`date -d "$t1" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$t1"_RUSA_pt.txt

  done
t1=`date -d "$t1 1days" +%Y%m%d`
done

#MAEMI 030912-030913

rm -f ./result/20*_MAEMI_pt.txt
for i in `seq 20030912 20030913`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_MAEMI_pt.txt

  done
done

#MEGI 040817-040819

rm -f ./result/20*_MEGI_pt.txt
for i in `seq 20040817 20040819`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_MEGI_pt.txt

  done
done

#NARI 070913-070918

rm -f ./result/20*_NARI_pt.txt
for i in `seq 20070913 20070918`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_NARI_pt.txt

  done
done

#RAMMASUN 020705-020706

rm -f ./result/20*_RAMMASUN_pt.txt
for i in `seq 20020705 20020706`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_RAMMASUN_pt.txt

  done
done

#EWINIAR 060709-060710

rm -f ./result/20*_EWINIAR_pt.txt
for i in `seq 20060709 20060710`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_EWINIAR_pt.txt

  done
done

#DIANMU 100810-100812

rm -f ./result/20*_DIANMU_pt.txt
for i in `seq 20100810 20100812`;do

  yy=${i:0:4}
  julian=`date -d "$i" +%j`

  for j in `awk '{print $1}' ./KOREA_rain/"$yy"/station"$yy".dat`;do

    lat=$(awk '/'^$j'/{print $2}' ./KOREA_rain/"$yy"/station"$yy".dat)
    lon=$(awk '/'^$j'/{print $3}' ./KOREA_rain/"$yy"/station"$yy".dat)
    awk '$25 ~ /'$yy'/{print $0}' ./station_pt/"$j"station_pt.txt > typhoon1.txt
    awk '{if (NR=='$julian') {print $0}}' ./typhoon1.txt > typhoon2.txt
    awk '{for (k=1;k<=24;k++) sum+=$k} END {printf '$j'", "'$lat'", "'$lon'", "; printf sum; printf ",\n"}' ./typhoon2.txt >> ./result/"$i"_DIANMU_pt.txt

  done
done


#ncl
for i in `seq 1 3`;do
	ncl RUSA${i}.ncl
	ncl MEGI${i}.ncl
	ncl KOMPASU${i}.ncl
	ncl DIANMU${i}.ncl
	convert ./result/RUSA${i}.ps ./result/RUSA${i}.jpg
	convert ./result/MEGI${i}.ps ./result/MEGI${i}.jpg
	convert ./result/KOMPASU${i}.ps ./result/KOMPASU${i}.jpg
	convert ./result/DIANMU${i}.ps ./result/DIANMU${i}.jpg
done
for i in `seq 1 2`;do
	ncl MAEMI${i}.ncl
	ncl RAMMASUN${i}.ncl
	ncl EWINIAR${i}.ncl
	convert ./result/MAEMI${i}.ps ./result/MAEMI${i}.jpg
	convert ./result/RAMMASUN${i}.ps ./result/RAMMASUN${i}.jpg
	convert ./result/EWINIAR${i}.ps ./result/EWINIAR${i}.jpg
done
for i in `seq 1 6`;do
	ncl NARI${i}.ncl
	convert ./result/NARI${i}.ps ./result/NARI${i}.jpg
done

#!/bin/bash

for i in `seq 2000 2010`;do
sed -e  "s/YYYY/${i}/g" ./ncl/year.ncl > ./ncl/${i}_year.ncl
done

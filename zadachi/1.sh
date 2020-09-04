
for type in $(cat z2)
do
	num=$(grep $type z1 | wc -l)
	echo $type $num
done



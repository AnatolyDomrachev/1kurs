file=is30
awk -F ':' '{print $1}' $file |sort -u | \
awk '{print "echo "$0 ":$(grep \""$0"\" "fil"|wc -l)"}' fil=$file |sh > tmp
max=$(cat tmp | awk -F ':' '{print $2}' | sort -n | tail -n 1)
cat tmp | awk -F ':' '{if($2==m) oc=5;else oc=4 ;print $1" "oc}' m=$max 
    


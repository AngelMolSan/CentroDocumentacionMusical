while IFS= read -r line
do
   wget -i "$line"
done < recursos.txt

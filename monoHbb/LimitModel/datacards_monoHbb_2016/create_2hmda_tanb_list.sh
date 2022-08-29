cat ../configs/points_2hdma.py | grep -v 'gg'  | grep '2HDMa' | sed "s/'//g" | sed "s/,//g" | sed ':a;N;$!ba;s/\n/ /g' | sed 's/_/-/g'


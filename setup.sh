g='\033[1;32m'
p='\033[1;35m'
r='\033[1;31m'
b='\033[1;34m'
w='\033[1;0m'
echo -e "$g [*] download ..."
echo -e "$w"
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install python3 -y
clear
mv payload /data/data/com.termux/files/usr/bin
cd /data/data/com.termux/files/usr/bin;chmod +x payload
echo -e "$r[*] Start PAYLOAD > $g payload"
cd $HOME
cd payload_termux
mv .payload.py $HOME
mv .rif.sh $HOME
cd $HOME
bash .rif.sh

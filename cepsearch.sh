r="\033[0;49;91m"                                            
g="\033[0;49;92m"
y="\033[0;49;93m"
b="\033[0;49;94m"                                            
p="\033[0;49;95m"                                             
b2="\033[0;49;96m"
d="\033[2;37m"
w="\033[0m"
echo -en "$r Digite o CEP: $g \033[m\033[m"
read -p "" cepp
wget https://viacep.com.br/ws/$cepp/json
sed -i 's/"//g' json ; sed -i 's/,//g' json ; sed -i 's/://g' json ; sed -i 's/{//g' json ; sed -i "s/}//g" json
echo -e $r" O CEP Selecionado: $g $cepp\033[m"
var=$(cat json | cut -d" " -f4-6)
logra=$(echo ${var:0} | cut -d" " -f2-4)
bairro=$(echo ${var:0} | cut -d" " -f5)
cidade=$(echo ${var:0} | cut -d" " -f6-8)
estado=$(echo ${var:0} | cut -d" " -f9)
ibge=$(echo ${var:0} | cut -d" " -f11)
ddd=$(echo ${var:0} | cut -d" " -f12)
siafi=$(echo ${var:0} | cut -d" " -f13)
echo -e "$r Logradouro: $g $logra\033[m"
echo -e "$r Bairro: $g $bairro\033[m"
echo -e "$r Cidade: $g $cidade\033[m"
echo -e "$r Estado: $g $estado\033[m"
echo -e "$r IBGE: $g $ibge\033[m"
echo -e "$r DDD: $g $ddd\033[m"
echo -e "$r Siafi: $g $siafi\033[m"
read -p ">Enter<"
rm json
#python johnny.py

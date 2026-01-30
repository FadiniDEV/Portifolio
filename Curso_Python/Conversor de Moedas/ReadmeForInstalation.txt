 Para instalação dos conteudos essenciais para o conversor funcionar,
você precisará do "Python 3" e precisará usar os seguintes comandos:

python -m pip install customtkinter
python -m pip install xmltodict
python -m pip install requests



 Se estiver no linux e estiver dando erro no pip install,
tente instalar o pip3 pelo comando:

sudo apt update
sudo apt install python3-pip

 Caso ainda estiver com problemas use o seguinte comando
para fazer a instalação utilizando o pip que ele irá forçar
uma instalação utilizando o pip:

sudo pip install xmltodict --break-system-packages

 Caso ainda esteja com algum erro no tkinter, siga esses
comandos:

sudo apt update
sudo apt install python3-tk
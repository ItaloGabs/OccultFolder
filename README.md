# OccultFolder
Mini programa para esconder pastas dos usuários local:

- Esconde com mini sistema de login
- Gerador de log de acesso mal sucedido
- Gera log de cada caminho de arquivo/pasta oculto

---

# Instrução:
1.SUBSTITUIR DENTRO DO IF O NOME 'ITARU' PARA O NOME DESEJADO, FAZER O MESMO PARA A SENHA:
	if valores['usuario'] == 'seunome' and valores['senha'] == 'suasenha':
	1.1.PARA GERAR O ARQUIVO .EXE COM AS ALTERAÇÕES FEITAS INSTALAR O PYINSTALLER E EXECUTAR A LINHA A SEGUIR:
		Pyinstaller --noconsole --icon='iconedesejado' caminhodapasta
			ex: Pyinstaller --noconsole --icon='C:\Users\user\Desktop\testepasta\iconedesejado' C:\Users\user\Desktop\testepasta\occultFolder.py
	Obs: pode alterar o nome do arquivo python para um desejado, que o mesmo vai gerar um .exe
2.TODOS OS LOGS DE TENTATIVA DE ACESSO MAL SUCEDIDA SERÃO GERADOS UM TXT DENTRO DA PASTA OCCULTFOLDER

3.OS CAMINHOS DAS PASTAS OCULTADAS TAMBEM SERÃO GERADAS PARA CASO PERCA O CAMINHO

4.CASO OCORRA DE NÃO OCULTAR INSERIR O CAMINHO DA PASTA ENTRE ASPAS: "CAMINHO"

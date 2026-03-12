import logging
from extracao import extrair_conteudo_html

logging.basicConfig(
    filename="server.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s no arquivo %(filename)s e função %(funcName)s na linha %(lineno)d: %(message)s",
)

logging.info("Mensagem de Informação")
logging.warning("Mensagem de Warning")
logging.error("Mensagem de Erro")

if __name__ == "__main__":
    resultado = extrair_conteudo_html("http://books.toscrape.com/", logging)
    print(resultado)
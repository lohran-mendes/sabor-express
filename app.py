from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida  
from modelo.cardapio.prato import Prato
from modelo.cardapio.sobremesa import Sobremesa
import os

def main():
    # restaurante_japones = Restaurante('japa food', 'japonesa')
    # restaurante_mexicano = Restaurante('mexican marmita', 'mexicana')
    restaurante_italiano = Restaurante('rei da pizza', 'italiana')
    # restaurante_mexicano.receber_avaliacao('lohran', 4)
    # restaurante_mexicano.receber_avaliacao('maria', 4)
    # restaurante_japones.receber_avaliacao('maria', 5)
    # restaurante_japones.receber_avaliacao('maria', 2)
    # Restaurante.listar_restaurantes()
    bebida_coca = Bebida('Coca Cola', 8.0, 'Grande')
    prato_lasanha = Prato('Lasanha', 20.0, 'Uma lasanha fresquinha')
    sobremesa_sorvete = Sobremesa('Sorvete', 15.0, 'Um sorvete com três bolas com sabores escolhidos')
    restaurante_italiano.adicionar_no_cardapio(bebida_coca)
    restaurante_italiano.adicionar_no_cardapio(prato_lasanha)
    restaurante_italiano.adicionar_no_cardapio(sobremesa_sorvete)
    bebida_coca.aplicar_desconto()
    sobremesa_sorvete.aplicar_desconto()
    # prato_lasanha.aplicar_desconto()
    restaurante_italiano.exibir_cardapio



if __name__ == '__main__':
    os.system('cls')
    main()
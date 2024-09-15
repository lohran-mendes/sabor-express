from modelo.restaurante import Restaurante
import os

def main():
    restaurante_japones = Restaurante('japa food', 'japonesa')
    restaurante_mexicano = Restaurante('mexican marmita', 'mexicana')
    restaurante_italiano = Restaurante('rei da pizza', 'italiana')
    restaurante_mexicano.alterar_estado()
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    os.system('cls')
    main()
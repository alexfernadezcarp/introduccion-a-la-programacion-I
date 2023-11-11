import menu
import negocio


selec=0


while selec !=9:
    menu.datos_menu()
    selec=int(input('ingrese una opcion '))
    if selec == 1:
        negocio.clientes_registrados()
    if selec == 2:
        negocio.registrar_productos()
    if selec == 3:
        negocio.compradores_finales()
    if selec == 4:
        negocio.ventas_clientes()
    if selec == 5:
        negocio.listar_clientes()
    if selec == 6:
        negocio.listar_productos()
    if selec == 7:
        negocio.buscar_ventas()
    if selec == 8:
        negocio.ordenamiento_productos()
    if selec == 9:
        negocio.salir()
    
                        
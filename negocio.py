#cargas de clientes
global nombre_cliente
nombre_cliente=[]
global codigo_cliente
codigo_cliente=[]
global cantidad_ventas_cliente
cantidad_ventas_cliente=[]

#productos
global nombre_producto
nombre_producto=[]
global codigo_producto
codigo_producto=[]
global precio_producto
precio_producto=[]
global cantidad_de_producto
cantidad_de_producto=[]
global ventas_registrada_x_producto
ventas_registrada_x_producto=[]

#compradores nuevos
global nombre_nuevos_cliente
nombre_nuevos_cliente=[]
global cantidad_productos_nuevos
cantidad_productos_nuevos=[]
global precio_compradores
precio_compradores=[]







def clientes_registrados():
    op=True
    while op:
        nombre=input('ingrese nombre de cliente ')
        codigo=int(input('ingrese codigo del cliente '))
        ventas=int(input('ingrese ventas realizadas del cliente '))
        nombre_cliente.append(nombre)
        codigo_cliente.append(codigo)
        cantidad_ventas_cliente.append(ventas)
        pregunta=int(input('deseas ingresar mas clientes? SI/1 NO/2 '))
        if pregunta == 2:
            print('Gracias por registrar ')
            op=False


def registrar_productos():
    op=True
    while op:
        nombre=input('ingrese el nombre del producto ')
        codigo=int(input('ingrese el codigo del producto '))
        precio=float(input('ingrese el precio del producto '))
        stock=int(input('ingrese el stock del producto '))
        nombre_producto.append(nombre)
        codigo_producto.append(codigo)
        precio_producto.append(precio)
        cantidad_de_producto.append(stock)
        pregunta=int(input('Deseas ingresar mas productos? SI/1 NO/2' ))
        if pregunta == 2:
            print('Gracias por registrar')
            op=False
        


def compradores_finales():
        print('***Productos en Stock***')
        print(nombre_producto)
        eleccion=input('ingrese el producto a comprar ')
        op=True
        while op:
            for i in range(len(nombre_producto)):
                if eleccion == nombre_producto[i]:
                   nombre=input('ingrese su nombre ')
                   nombre_nuevos_cliente.append(nombre) 
                   cantidad=int(input('ingrese la cantidad de productos a comprar '))
                   if cantidad <= cantidad_de_producto[i]:
                        cantidad_productos_nuevos.append(cantidad)
                        ventas_registrada_x_producto.append(cantidad)
                        precio_final= cantidad * precio_producto[i]
                        precio_compradores.append(precio_final)
                        stock= cantidad_de_producto[i] - cantidad
                        cantidad_de_producto[i]=stock
                        
                      
                        print('Comprar realizada con exitos ')
                        print('Total de la compra', precio_final)
                        pregunta=int(input('deseas seguir comprarndo? SI/1 NO/2 '))
                        if pregunta == 2:
                            print('Gracias por tu compra ')
                            op=False
                        
                        
                   else:
                      print('la compra no se puede realizar por que no ahi stock disponible ')
                      print('Ingrese nuevamente ')
                else:
                    print('producto no encontrado ')
                    print('vuelva a intentarlo nuevamente ')
           
            


                    
def ventas_clientes():
    op=True
    while op: 
        buscar=0
        buscar=int(input('ingrese el codigo del cliente: '))
        for i in range(len(codigo_cliente)):
            if buscar == codigo_cliente[i]:
                print('**cliente encontado con exito**')
                print('Nombre de cliente,',nombre_cliente[i],'codigo',codigo_cliente[i],'ventas registrda', cantidad_ventas_cliente[i])
                op=False
            else:
                print('cliente no encontrado')
                print('intente nuevamente') 
            
        
    compra=True
    while compra:
        print('***Productos en Stock***')
        print(nombre_producto)                        
        eleccion=input('ingrese el producto a comprar ')
        for i in range(len(nombre_producto)):
            if eleccion == nombre_producto[i]:
                cantidad=int(input('ingrese la cantidad de productos a comprar '))
                if cantidad <= cantidad_de_producto[i]:
                    if cantidad < 10:
                        des=int(input('ingrese descuento menor de 10 unidades: '))
                        precio=cantidad * precio_producto[i]
                        descuento= precio * des / 100
                        total1=precio - descuento
                        cantidad_ventas_cliente.append(total1)
                        stock= cantidad_de_producto[i] - cantidad
                        cantidad_de_producto[i]=stock
                        ventas_registrada_x_producto.append(cantidad)
                        print('total precio con descuento del 5% por ser cliente ', total1)
                        
                        
                    elif cantidad > 10:
                        des=int(input('la compra supera las 10 unidades por favor ingrese descuento: '))
                        precio=cantidad * precio_producto[i]
                        descuento= precio * des / 100
                        total=precio - descuento 
                        cantidad_ventas_cliente.append(total)
                        stock= cantidad_de_producto[i] - cantidad
                        cantidad_de_producto[i]=stock
                        ventas_registrada_x_producto.append(cantidad)
                        print('total precio con decuento del 10% por superar 10 productos ', total)
                        
                else:
                    print('stock no disponible el stock disponible es de, ', cantidad_de_producto[i])                    
            else:
                print('producto no encontrado')  
            
        pregunta=int(input('Desea seguir comprando? SI/1 NO/2'))
        if pregunta == 2:
            print('Gracias por tu compra ')
            compra=False              

def listar_clientes():
    print('**lista de cliente**')
    print(nombre_cliente)
    print('**lista de clientes finales**')
    print(nombre_nuevos_cliente)
    
      
      
    
    
    
    
def listar_productos():
    count=len(nombre_producto)
    for i in range(count):
        print('**lista de productos')
        print('Nonmbre',nombre_producto[i],'precio',precio_producto[i],'stock',cantidad_de_producto[i])
    
    
def buscar_ventas():
    op=True
    while op:
        buscar=0
        buscar=int(input('ingrese el codigo de cliente '))
        for i in range(len(nombre_cliente)):
            if buscar == nombre_cliente[i]:
                print('**cliente encontrado con exito**')
                print(nombre_cliente[i])
                print('sus ventas son: ', cantidad_ventas_cliente[i])
                pregunta=int(input('deseas realizar otra busqueda? SI/ 1 NO/2'))
                if pregunta == 2:
                    print('Gracias por tu busqueda')
                    op=False
                
            else:
                print('cliente no encontrado')
                print('intente nuevamente')


def ordenamiento_productos():
     count=len(ventas_registrada_x_producto)-1
     for i in range(0,count):
        for j in range(0,count):
            if ventas_registrada_x_producto[j] < ventas_registrada_x_producto[j+1]:
                num=ventas_registrada_x_producto[j]
                ventas_registrada_x_producto[j]=ventas_registrada_x_producto[j+1]
                ventas_registrada_x_producto[j+1]=num
                auxi=nombre_producto[j]
                nombre_producto[j]=nombre_producto[j+1]
                nombre_producto[j+1]=auxi
               
                
    
     print('lista ordenadas de mayor a menor')
     for j in range(count+1):
       print(nombre_producto[j],ventas_registrada_x_producto[j])

def salir():
    print('Gracias vuelva pronto')
    
      
        
        
    
            
            
            

   
    
                    
                                  
                            
    
                    
        
    
        
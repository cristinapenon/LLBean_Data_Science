
#Escribir un código en Python que imprima en pantalla lo siguiente:
#* 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14

#usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos.

var_1= '******'
var_2=3.1415962

#print('%.1s %.9s' % (var_1,var_2))
#print('%.2s %.8s' % (var_1,var_2))
print('%.1s %.9s, %.2s %.8s, %.3s %.7s, %.4s %.6s, %.5s %.5s, %.6s %.4s' % (var_1,var_2,var_1,var_2,var_1,var_2,var_1,var_2,var_1,var_2,var_1,var_2))
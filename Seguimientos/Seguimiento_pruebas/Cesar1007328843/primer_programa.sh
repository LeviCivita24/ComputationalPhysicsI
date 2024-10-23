#!/bin/bash
#echo Hola mundo
#v1="No Espacio" #Se crea un string como var
#v2=10 #Se crea una variable
#echo $v1 #Imprime variable
#echo $v2

#------Segunda Parte-------
#Leer valor 
#echo Ingresar Valor A #o echo -n
#read A #Lee el valor --> Realmente es donde se está ingresando
#echo El valor es: $A #Imprime la variable 
#for numero in {1..20..2}
#do 
#    #echo el valor es $numero
#    resultado=$(bc<<<"scale=2;($numero*$numero)")
#    echo $resultado 
#done 
num1=3
num2=4

if [[ $num1 -gt $num2 ]]
then 
     echo $num1 mayor que $num2
else 
    echo $num2 mayor que $num1
fi 


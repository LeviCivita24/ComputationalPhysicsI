#!/bin/bash

#i1=12 #Número a adivinar

# En general el programa funciona muy bien
# La idea de ingresar el número de intentos es muy buena, sin embargo, se debe 
# refactorizar el código para su respecto funcionamiento (ej: n=2)
# Se debe comentar el código para el entendimiento
# Se recomienda informar del rango para adivinar el número
#:)

i1=$(($RANDOM%20 + 1))
echo Ingrese el numero de intentos que quiere adivinar el numero
read n

for k in 1 2 3 4 .. n
do
echo ingrese un valor
read i2
    if [[ $i2 -ne $i1 ]];
    then
        while [ $i2 -ne $i1 ]
        do
        if [[ $i2 -gt $i1 ]];
        then
        echo El número a adivinar debe ser menor
        else
        echo El número a adivinar debe ser mayor
        fi 
        break
        done
    else 
        echo Ganaste. Los números son iguales!!
        break
    fi
echo intento $k
echo ------------******--------
done 

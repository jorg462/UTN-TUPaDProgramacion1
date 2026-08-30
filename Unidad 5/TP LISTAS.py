{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b2ba8cf2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "8\n",
      "12\n",
      "16\n",
      "20\n",
      "24\n",
      "28\n",
      "32\n",
      "36\n",
      "40\n",
      "44\n",
      "48\n",
      "52\n",
      "56\n",
      "60\n",
      "64\n",
      "68\n",
      "72\n",
      "76\n",
      "80\n",
      "84\n",
      "88\n",
      "92\n",
      "96\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 1\n",
    "lista= list(range(1,101))\n",
    "for i in lista:\n",
    "    if i%4==0:\n",
    "        print(i)\n",
    "\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c02317fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Ejercicio 2\n",
    "lista = [1,2,3,4,5]\n",
    "lista[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b798dedc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['RIVER PLATE']\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 3\n",
    "lista=[]\n",
    "lista.append(\"RIVER PLATE\")\n",
    "print(lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f1a0fcce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['perro', 'loro', 'conejo', 'oso']\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 4\n",
    "animales = [\"perro\", \"gato\", \"conejo\", \"pez\"]\n",
    "animales[1]= \"loro\"\n",
    "animales[3]= \"oso\"\n",
    "print(animales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2840c3a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8, 15, 3, 7]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 5\n",
    "numeros=[8,15,3,22,7]\n",
    "numeros.remove(max(numeros))\n",
    "print(numeros)\n",
    "# ESTE PROGRAMA BORRA EL NUMERO MAS GRANDE DE LA LISTA \"NUMEROS\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b02d6e3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 15]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Ejercicio 6\n",
    "lista= list(range(10,31,5))\n",
    "lista[0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7023aa27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sedan', 'corolla', 'cronos', 'gol']\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 7\n",
    "autos = [\"sedan\", \"polo\", \"suran\", \"gol\"]\n",
    "autos[1:3]=[\"corolla\", \"cronos\"]\n",
    "print(autos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8981e964",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20, 30]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 8\n",
    "doble=[]\n",
    "doble.append(5*2)\n",
    "doble.append(10*2)\n",
    "doble.append(15*2)\n",
    "print(doble)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0b4438a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['leche'], ['arroz', 'tallarines', 'salsa'], ['agua', 'jugo']]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 9\n",
    "compras = [[\"pan\", \"leche\"], [\"arroz\", \"fideos\", \"salsa\"],[\"agua\"]]\n",
    "compras[2].append(\"jugo\")\n",
    "compras[1][1]=\"tallarines\"\n",
    "compras[0].remove(\"pan\")\n",
    "print(compras)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "392b9e06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[15, True, [25.5, 57.9, 30.6], False]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 10\n",
    "lista_anidada = []\n",
    "\n",
    "lista_anidada.append(15)\n",
    "lista_anidada.append(True)\n",
    "lista_anidada.append([25.5, 57.9, 30.6]) \n",
    "lista_anidada.append(False)\n",
    "\n",
    "print(lista_anidada)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c79b867",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

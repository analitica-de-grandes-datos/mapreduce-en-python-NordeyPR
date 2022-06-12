#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = "A"
    total = 0
    #
    # cada linea de texto recibida se adiciona a la lista1
    #
    for line in sys.stdin:
        val = line[1]
        key = line[3].split(",")
        val = (val)
        print(key ,  val)
            #if key == curkey:
                #total.append(val)
                #print(total)
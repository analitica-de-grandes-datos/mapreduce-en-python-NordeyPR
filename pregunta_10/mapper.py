#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import pandas

if __name__ == "__main__":

   

    for line in sys.stdin:
        result = line.split()
        
        #result1 = result[0].split("\t")
        result = line.replace("\t" , ",")
        result1 = result.replace("\r" , "")
        result2 = result1.replace("\n" , "")
        result3 = result2.split(",")
        clave = int(result3[0])
        valor = sorted(result3[1:])
        clave = clave
        
        #print(valor , clave)
        
        
                
        #sys.stdout.write("{}".format(result))
        sys.stdout.write("{}\t{}\n".format(valor ,  clave))
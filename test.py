#single note.py, Simple note application



#modules
import sys

#main funtion
def main () -> int:
    #arguments by sys.arg
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[1] + sys.args[2])
    print(22+23)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)



    #return value

    return(0)
#main function definiton

if __name__ == '__main__':
    sys.exit(main())

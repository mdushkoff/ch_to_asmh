class Syntax(object):
    """
    This represents the syntax definitions
    relevant to compiling C header files into
    ARM Cortex M0+ assembly files.
    """
    
    __slots__ = ('keys','types')
    
    def __init__(self):
        """
        This initializes a Syntax object.
        """
        
        """
        This is the type data which is defined as such:
            [0] MEM - Memory Size
            [1] ST  - Structure
            [2] SYM - Symbol
            [3] OP  - Operator
            [4] COM - Comment
            [5] DEF - Defines
            [6] SP  - Special (user-defined)
        """
        self.types=['MEM','ST','SYM','OP','COM','DEF','SP']
        self.keys={'uint8_t':types[0],\
                   'uint16t':types[0],\
                   'uint32t':types[0],\
                   'struct':types[1],\
                   '(':types[2],\
                   ')':types[2],\
                   '{':types[2],\
                   '}':types[2],\
                   '[':types[2],\
                   ']':types[2],\
                   ',':types[2],\
                   ';':types[2],\
                   '&':types[3],\
                   '<<':types[3],\
                   '>>':types[3],\
                   '->':types[3],\
                   '*':types[3],\
                   '/*':types[4],\
                   '*/':types[4],\
                   '#define':types[5],\
                   'BASES':types[6]}

              

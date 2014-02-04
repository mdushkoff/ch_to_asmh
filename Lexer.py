class Lexer(object):
    """
    This represents the Lexical Dictionary
    object which can interpret C syntax
    and appropriately arrange it in order
    to be parsed by the parser.
    """
    
    __slots__ = ('keyword','data','formatkey')
    
    def __init__(self,keyword,data,formatkey):
        """
        This initializes a Lexer object with the following
        parameters:
            keyword - The keyword that was encountered
            data - The data relevant to the keyword
            formatkey - A String representing the formatting
        """
        
        # Initialize the inputted slots
        self.keyword=keyword
        self.data=data
        self.formatkey=formatkey


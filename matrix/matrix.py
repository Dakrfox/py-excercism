class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(number) for number in row.split()] for row in matrix_string.split('\n')]
        """
        asi se crea un doble for primero se hace split en donde tenga de separador \n asi genera varias string filas 
        row1 "1 2 3" row2"4 5 6" row3" 7 8 9"
        y en el otro for por cada row generado
        los divide y convierte en numeros [1 2 3][4 5 6][7 8 9]
        recordar que se encuentrar almacenados en self
        """
        self.columns = [list(tup) for tup in zip(*self.rows)]
        """
        este utiliza zip que no es mas que unir bajo un mismo index iterativo 
        [1 2 3] ['a' 'b' 'c'] =[(1,"a")(2,"b")(3, "c")]
        el asterisco es usado para referenciar a todos los rows de swlf.rows
        """
    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
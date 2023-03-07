import var


class TableClientes:

    '''
    Metodo que sirve para darle estilos a la tabla
    '''
    @staticmethod
    def set_row_color():
        """

        Funcion que cambia el color de las filas de la tabla de clientes
        :return:
        """
        var.ui.tabClientes.setStyleSheet(
            '''
            QTableView
            {   
                
                background-color: #E0E0E0;
                gridline-color:#E0E0E0;
                color: black;
                
            }
            QTableView::item 
            {   
                color: black;         
            }
            QTableView::item:hover
            {   
                color: black;
                background: #FFFFFF;            
            }
            QTableView::item:focus
            {   
                color: black;
                background-color: white;            
            }
            
            '''
        )

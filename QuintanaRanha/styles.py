import var


class TableClientes:

    @staticmethod
    def setRowColor():
        var.ui.tabClientes.setStyleSheet(
            '''
            QTableView
            {   
                background-color: grey;
                gridline-color:grey;
                color: salmon;
            }
            QTableView::item 
            {   
                color: white;         
            }
            QTableView::item:hover
            {   
                color: black;
                background: #ffffff;            
            }
            QTableView::item:focus
            {   
                color: black;
                background: #ffffff;            
            }
            '''
        )

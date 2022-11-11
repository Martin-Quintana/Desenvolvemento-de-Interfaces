import var


class TableClientes:

    @staticmethod
    def setRowColor():
        var.ui.tabClientes.setStyleSheet(
            '''
            QTableView
            {   
                background-color: #E0E0E0;
                gridline-color:#E0E0E0;
                color: salmon;
            }
            QTableView::item 
            {   
                color: black;         
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
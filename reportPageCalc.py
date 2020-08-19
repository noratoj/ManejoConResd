import xlwt

class reporthojaCalc:

    def __init__(self):
        self.wb=xlwt.Workbook()
        self.ws=self.wb.add_sheet("Listado de Vecinos")

        self.ws.write(0,0,"Listado de Vecinos")

        columns = ["Nro:",
                    "Nro de Cédula",
                    "Nombres",
                    "Apellidos",
                    "Edif",
                    "Piso",
                    "Apto"
        ]
        impri_col=0
        for column1 in columns:
            self.ws.write(1,impri_col,column1)
            impri_col+=1

    def addItemRep(self, registros):
        self.row_1=2
        for i in registros:
            self.ws.write(self.row_1, 0, self.row_1-1)
            self.ws.write(self.row_1, 1, i[1])
            self.ws.write(self.row_1, 2, i[2]+" "+i[3])
            self.ws.write(self.row_1, 3, i[4]+" "+i[5])
            self.ws.write(self.row_1, 4, i[29])
            self.ws.write(self.row_1, 5, i[15])
            self.ws.write(self.row_1, 6, i[28])
            self.row_1 = self.row_1 + 1


    def saveRep(self, nameRep):
        self.wb.save(nameRep)
        print("salvao")
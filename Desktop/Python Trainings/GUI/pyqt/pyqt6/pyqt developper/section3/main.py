
from PyQt6.QtWidgets import QMainWindow,QApplication ,QFileDialog,QMessageBox

import sys 
from PyQt6.QtPrintSupport import QPrinter , QPrintDialog  ,QPrintPreviewDialog
from PyQt6.QtGui import QFont
from notepad import Ui_MainWindow 
from PyQt6.QtCore import QFileInfo

class NotePadWindow(QMainWindow,Ui_MainWindow) : 
    def __init__(self) : 
        super().__init__() 
        self.setupUi(self)
        self.show() 
        self.actionSave.triggered.connect(self.save_file)
        self.filename = ''
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionExport_PDf.triggered.connect(self.preview_dialog)
        self.actionPreview.triggered.connect(self.export_pdf)
        self.actionQuit.triggered.connect(self.quit)

        
        self.textEdit.setFont(QFont("Times New Roman",14))
    def save_file(self) : 
        if self.filename != '' : 
            f= open(self.filename,'w')
            with f : 
                text = self.textEdit.toPlainText() 
                f.write(text)
                
        else : 

        
            filename = QFileDialog.getSaveFileName(self,'save the file')
            self.filename = filename[0]
            
            print(filename[0])
            if self.filename : 
                f= open(self.filename,'w')
                with f : 
                    text = self.textEdit.toPlainText() 
                    f.write(text)



    def maybe_save(self) :
        if not self.textEdit.document().isModified() : 
            return True 
        ret = QMessageBox.warning(self,'Application','The Document has been modified do you want to save the change ',
                                  QMessageBox.StandardButtons.Save | QMessageBox.StandardButtons.Discard|QMessageBox.StandardButtons.Cancel)


        if ret == QMessageBox.StandardButtons.Save :
            return self.save_file() 
        elif ret == QMessageBox.StandardButtons.Cancel : 
            return False 
        else : 
            return True 
    
    def file_new(self) : 
        if self.maybe_save() : 
            self.textEdit.clear()

    def open_file(self) : 
        fname= QFileDialog.getOpenFileName(self,"Open File")
        print(fname)
        if fname[0] : 
            self.filename = fname[0]
            f = open(fname[0],'r') 

            with f : 
                data = f.read() 
                self.textEdit.setText(data)

    def print_file(self) : 
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        
        dialog = QPrintDialog(printer) 
      

        if dialog.DialogCode.Accepted : 

            self.textEdit.print(printer)
            print('\n\n\n\n hello rachid how are uyou \n \n \n ')
            


    def preview_dialog(self) : 
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        prev_d = QPrintPreviewDialog(printer,self)
        prev_d.paintRequested.connect(self.print_preview)
        prev_d.exec() 
    
    def print_preview(self,printer) : 
        self.textEdit.print(printer)

    def export_pdf(self) : 
        fn,_ = QFileDialog.getSaveFileName(self,
                                           'Export PDF',
                                           "text",
                                           
                                           )
        
        if fn != "" : 

            if QFileInfo(fn).suffix() == "" : fn += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

    def quit(self) : 
        self.close() 











    


app = QApplication(sys.argv) 
Note = NotePadWindow() 

sys.exit(app.exec())


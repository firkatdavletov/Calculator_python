import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.groupInp = ttk.Entry(self)
        self.groupInp.grid(row='0', column='1', columnspan='1', sticky='w', padx='5', pady='5')
        self.groupLbl = ttk.Label(self, text='Группа')
        self.groupLbl.grid(row='0', column='0', padx='5', pady='0')

        self.categoryInp = ttk.Entry(self)
        self.categoryInp.grid(row='0', column='3', padx='5', pady='5')
        self.categoryLbl = ttk.Label(self, text='Категория')
        self.categoryLbl.grid(row='0', column='2', padx='5', pady='0')

        self.companyLbl = ttk.Label(self, text='Организация (предприятие)')
        self.companyLbl.grid(row='2', column='0', columnspan='1', sticky='w', padx='5', pady='5')
        self.companyInp = ttk.Entry(self)
        self.companyInp.grid(row='2', column='1', columnspan='1', sticky='w', padx='5', pady='5')

        self.ntb = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.ntb)
        self.tab2 = ttk.Frame(self.ntb)
        self.tab3 = ttk.Frame(self.ntb)
        self.ntb.add(self.tab1, text='Технологический нефтепродуктопровод')
        self.ntb.add(self.tab2, text='Отдельные трубопроводы')
        self.ntb.add(self.tab3, text='third')

        self.title1 = tk.Label(self.tab1)
        self.title1['text'] = '1. Технологический нефтепродуктопровод'
        self.title1.grid(row='0', column='0', columnspan='2', padx='5', pady='20')

        self.generalDataLbl = tk.Label(self.tab1, text='1.1 Общие данные')
        self.generalDataLbl.grid(row='1', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.regNumbLbl = tk.Label(self.tab1, text='Регистрационный номер')
        self.regNumbLbl.grid(row='2', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.regNumbInp = tk.Entry(self.tab1, width='10')
        self.regNumbInp.grid(row='2', column='1', columnspan='1', padx='5', pady='5')

        self.dateLbl = tk.Label(self.tab1, text='Дата')
        self.dateLbl.grid(row='2', column='2', columnspan='1', rowspan='2', ipadx='5', ipady='5', sticky='nw')
        self.dateDayInp = tk.Entry(self.tab1, width='10')
        self.dateDayInp.grid(row='2', column='3', columnspan='1', padx='5', pady='0', sticky='nw')
        self.dateMonthInp = tk.Entry(self.tab1, width='10')
        self.dateMonthInp.grid(row='2', column='4', columnspan='1', padx='5', pady='0', sticky='nw')
        self.dateYearInp = tk.Entry(self.tab1,width='10')
        self.dateYearInp.grid(row='2', column='5', columnspan='1', padx='5', pady='0', sticky='nw')
        self.dateDayLbl = tk.Label(self.tab1, text='день')
        self.dateDayLbl.grid(row='3', column='3', columnspan='1', padx='5', pady='0')
        self.dateMonthLbl = tk.Label(self.tab1, text='месяц')
        self.dateMonthLbl.grid(row='3', column='4', columnspan='1', padx='5', pady='0')
        self.dateYearLbl = tk.Label(self.tab1, text='год')
        self.dateYearLbl.grid(row='3', column='5', columnspan='1', padx='5', pady='0')

        self.causeOfMeasLbl = tk.Label(self.tab1, text='Основание для проведения измерений')
        self.causeOfMeasLbl.grid(row='5', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.causeOfMeasInp = tk.Entry(self.tab1, width='50')
        self.causeOfMeasInp.grid(row='5', column='1', columnspan='8', padx='5', pady='5', sticky='w')

        self.placeOfMeasLbl = tk.Label(self.tab1, text='Место проведения измерений')
        self.placeOfMeasLbl.grid(row='6', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.placeOfMeasInp = tk.Entry(self.tab1, width='50')
        self.placeOfMeasInp.grid(row='6', column='1', columnspan='8', padx='5', pady='5', sticky='w')

        self.innacOfMeasLbl = tk.Label(self.tab1, justify='left')
        self.innacOfMeasLbl['text'] = 'Погрешность определения вместимости\nтехнологического нефтепродуктопровода, %'
        self.innacOfMeasLbl.grid(row='7', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.innacOfMeasInp = tk.Entry(self.tab1, width='50')
        self.innacOfMeasInp.grid(row='7', column='1', columnspan='8', padx='5', pady='5', sticky='w')

        self.devicesLbl = tk.Label(self.tab1, justify='left')
        self.devicesLbl['text'] = 'Средства измерений'
        self.devicesLbl.grid(row='8', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.devicesInp = tk.Entry(self.tab1, width='50')
        self.devicesInp.grid(row='8', column='1', columnspan='8', padx='5', pady='5', sticky='w')

        self.condLbl = tk.Label(self.tab1, text='1.2 Условия проведения измерений')
        self.condLbl.grid(row='9', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.tempLbl = tk.Label(self.tab1, text='Температура воздуха, °С')
        self.tempLbl.grid(row='10', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.tempInp = tk.Entry(self.tab1, width='10')
        self.tempInp.grid(row='10', column='1', columnspan='1', padx='5', pady='5', sticky='w')

        self.speedWindLbl = tk.Label(self.tab1, text='Скорость ветра, м/с')
        self.speedWindLbl.grid(row='10', column='2', columnspan='2', padx='5', pady='5', sticky='w')
        self.speedWindInp = tk.Entry(self.tab1, width='10')
        self.speedWindInp.grid(row='10', column='4', columnspan='1', padx='5', pady='5', sticky='w')

        self.gazPollLbl = tk.Label(self.tab1, text='Загазованность, м³')
        self.gazPollLbl.grid(row='10', column='5', columnspan='2', padx='5', pady='5', sticky='w')
        self.gazPollInp = tk.Entry(self.tab1, width='10')
        self.gazPollInp.grid(row='10', column='7', columnspan='1', padx='5', pady='5', sticky='w')

        self.title2 = tk.Label(self.tab2, text='1. Отдельные трубопроводы')
        self.title2.grid(row='0', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.pipeLineNumbLbl = tk.Label(self.tab2, text='Номер отдельного трубопровода')
        self.pipeLineNumbLbl.grid(row='1', column='0', columnspan='1', padx='5', pady='5', sticky='w')
        self.pipeLineNumbInp = tk.Entry(self.tab2, width='10')
        self.pipeLineNumbInp.grid(row='1', column='1', columnspan='1', padx='5', pady='5', sticky='w')

        self.pipeLineBoundsLbl = tk.Label(self.tab2, text='Границы по номерам\nградуировочных точек', justify='left')
        self.pipeLineBoundsLbl.grid(row='1', column='2', columnspan='2', padx='5', pady='5', sticky='e')
        self.pipeLineBoundsInp = tk.Entry(self.tab2, width='10')
        self.pipeLineBoundsInp.grid(row='1', column='5', columnspan='1', padx='5', pady='5', sticky='w')

        self.addPipLineButt = tk.Button(self.tab2, text='Добавить трубопровод')
        self.addPipLineButt.grid(row='2', column='0')

        self.pipeLinesCanv = tk.Canvas(self.tab2, width='768', height='200')
        self.pipeLinesCanv.grid(row='3', column='0', columnspan='6')

        self.pipeLinesCanv.create_rectangle(10, 10, 768, 100)
        self.pipeLinesCanv.create_text(10, 10, text='Номер отдельного\nтрубопровода')

        self.ntb.grid(row='3', column='0', columnspan='4', padx='5', pady='5')


root = tk.Tk()
root.title('Расчет вместимости нефтепродуктопровода')
root.geometry('1024x768')
app = Application(master=root)

app.mainloop()
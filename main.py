import tkinter as tk
from tkinter import ttk
import json


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    pipeLineNumbInp = None
    pipeLineBoundsInp = None
    pipeLineY = 0
    pipeLinesArr = {}
    pipeLineStep = 0

    def write_to_json(self):
        with open('pipelines.json') as plr:
            pipes_obj = json.load(plr)
        new_pipe = {'numb': self.pipeLineNumbInp.get(), 'bounds': self.pipeLineBoundsInp.get()}
        pipes_obj.append(new_pipe)
        with open('pipelines.json', 'w') as pl:
            json.dump(pipes_obj, pl)

    def clear_json(self):
        with open('pipelines.json') as pld:
            pipes_obj = json.load(pld)
        pipes_obj.clear()
        with open('pipelines.json', 'w') as pl:
            json.dump(pipes_obj, pl)

    def write_canvas(self):
        with open('pipelines.json', 'r') as pl:
            data = json.load(pl)
            for i in data:
                y = self.pipeLineY * 25 + 58
                self.pipeLinesCanv.create_rectangle(10, y - 8, 850, y + 17, tag='text')
                self.pipeLinesCanv.create_line(160, y - 8, 160, y + 18, tag='text')
                self.pipeLinesCanv.create_text(12, y, text=i['numb'], anchor='w', tag='text')
                self.pipeLinesCanv.create_text(162, y, text=i['bounds'], anchor='w', tag='text')
                self.pipeLineY = self.pipeLineY + 1
            self.pipeLineY = 0

    def addComboPipe(self):
        with open('pipelines.json', 'r') as pl:
            data = json.load(pl)
            arr = []
            for i in data:
                arr.append(i['numb'])
        self.combo_pipes['values'] = arr

    def addPipeLine(self):
        self.write_to_json()

        self.pipeLinesCanv.delete('text')
        self.write_canvas()

        self.pipeLineNumbInp.delete(0, 'end')
        self.pipeLineBoundsInp.delete(0, 'end')

        self.addComboPipe()

    def delPipeLine(self):
        self.clear_json()
        self.pipeLinesCanv.delete('text')
        self.combo_pipes.delete(0, 'end')
        self.combo_pipes['values'] = []

    #Интерфейс-------------------------------------------------------------------------------------------------

    def create_widgets(self):

        #Данные пользователя---------------------------------------------------------------------------------------

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
        #Вкладки----------------------------------------------------------------------------------------------------
        self.ntb = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.ntb)
        self.tab2 = ttk.Frame(self.ntb)
        self.tab3 = ttk.Frame(self.ntb)
        self.tab4 = ttk.Frame(self.ntb)
        self.tab5 = ttk.Frame(self.ntb)
        self.tab6 = ttk.Frame(self.ntb)
        self.ntb.add(self.tab1, text='Общие данные')
        self.ntb.add(self.tab2, text='Отдельные трубопроводы')
        self.ntb.add(self.tab3, text='Параметры прямолинейной трубы')
        self.ntb.add(self.tab4, text='Параметры арматуры')
        self.ntb.add(self.tab5, text='Параметры фитинга')
        self.ntb.add(self.tab6, text='Вместимость оборудования')

        #Первая вкладка-----------------------------------------------------------------------------------------------

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

        #Вторая вкладка-----------------------------------------------------------------------------------------

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

        self.addPipeLineButt = tk.Button(self.tab2, text='Добавить трубопровод', command=self.addPipeLine)
        self.addPipeLineButt.grid(row='2', column='0')
        self.delPipeLineButt = tk.Button(self.tab2, text='Очистить список', command=self.delPipeLine)
        self.delPipeLineButt.grid(row='2', column='1')


        self.pipeLinesCanv = tk.Canvas(self.tab2, width='850', height='200')
        self.pipeLinesCanv.grid(row='3', column='0', columnspan='6')

        self.pipeLinesCanv.create_rectangle(10, 10, 850, 50)
        self.pipeLinesCanv.create_line(160, 10, 160, 50)
        self.pipeLinesCanv.create_text(20, 30, text='Номер отдельного\nтрубопровода', anchor='w')
        self.pipeLinesCanv.create_text(170, 20, text='Границы участка по номерам градуировочных точек', anchor='w')

        self.write_canvas()

        #Третья вкладка-----------------------------------------------------------------------------------------

        self.title3 = tk.Label(self.tab3, text='2. Параметры прямолинейной трубы')
        self.title3.grid(row='0', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.pipelinelbl = tk.Label(self.tab3, text='Номер участка трубопровода')
        self.pipelinelbl.grid(row='1', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.combo_pipes = ttk.Combobox(self.tab3)
        self.addComboPipe()
        self.combo_pipes.grid(row='1', column='1', columnspan='4', padx='5', pady='5', sticky='w')

        self.numb_meas_lbl = tk.Label(self.tab3, text='Номер измерения', justify='center')
        self.numb_meas_lbl.grid(row='2', column='1', columnspan='8', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_1 = tk.Label(self.tab3, text='1')
        self.numb_meas_lbl_2 = tk.Label(self.tab3, text='2')
        self.numb_meas_lbl_3 = tk.Label(self.tab3, text='3')
        self.numb_meas_lbl_4 = tk.Label(self.tab3, text='4')
        self.numb_meas_lbl_5 = tk.Label(self.tab3, text='5')
        self.numb_meas_lbl_6 = tk.Label(self.tab3, text='6')
        self.numb_meas_lbl_7 = tk.Label(self.tab3, text='7')
        self.numb_meas_lbl_8 = tk.Label(self.tab3, text='8')
        self.numb_meas_lbl_1.grid(row='3', column='1', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_2.grid(row='3', column='2', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_3.grid(row='3', column='3', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_4.grid(row='3', column='4', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_5.grid(row='3', column='5', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_6.grid(row='3', column='6', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_7.grid(row='3', column='7', columnspan='1', padx='5', pady='5', sticky='w')
        self.numb_meas_lbl_8.grid(row='3', column='8', columnspan='1', padx='5', pady='5', sticky='w')


        self.ext_diam_lbl = tk.Label(self.tab3, text='Диаметр наружный Dis, мм')
        self.ext_diam_lbl.grid(row='4', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.ext_diam_inp_1 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_2 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_3 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_4 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_5 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_6 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_7 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_8 = tk.Entry(self.tab3, width='5')
        self.ext_diam_inp_1.grid(row='4', column='1', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_2.grid(row='4', column='2', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_3.grid(row='4', column='3', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_4.grid(row='4', column='4', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_5.grid(row='4', column='5', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_6.grid(row='4', column='6', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_7.grid(row='4', column='7', columnspan='1', padx='5', pady='5', sticky='w')
        self.ext_diam_inp_8.grid(row='4', column='8', columnspan='1', padx='5', pady='5', sticky='w')

        self.circfer_lbl = tk.Label(self.tab3, text='Длина окружности Dis, мм')
        self.circfer_lbl.grid(row='5', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.circfer_inp_1 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_2 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_3 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_4 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_5 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_6 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_7 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_8 = tk.Entry(self.tab3, width='5')
        self.circfer_inp_1.grid(row='5', column='1', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_2.grid(row='5', column='2', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_3.grid(row='5', column='3', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_4.grid(row='5', column='4', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_5.grid(row='5', column='5', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_6.grid(row='5', column='6', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_7.grid(row='5', column='7', columnspan='1', padx='5', pady='5', sticky='w')
        self.circfer_inp_8.grid(row='5', column='8', columnspan='1', padx='5', pady='5', sticky='w')

        self.wall_thik_lbl = tk.Label(self.tab3, text='Толщина стенки, мм')
        self.wall_thik_lbl.grid(row='6', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.wall_thik_inp_1 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_2 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_3 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_4 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_5 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_6 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_7 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_8 = tk.Entry(self.tab3, width='5')
        self.wall_thik_inp_1.grid(row='6', column='1', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_2.grid(row='6', column='2', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_3.grid(row='6', column='3', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_4.grid(row='6', column='4', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_5.grid(row='6', column='5', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_6.grid(row='6', column='6', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_7.grid(row='6', column='7', columnspan='1', padx='5', pady='5', sticky='w')
        self.wall_thik_inp_8.grid(row='6', column='8', columnspan='1', padx='5', pady='5', sticky='w')

        self.length_lbl = tk.Label(self.tab3, text='Длина Lиз, мм')
        self.length_lbl.grid(row='7', column='0', columnspan='1', padx='5', pady='5', sticky='w')

        self.length_inp_1 = tk.Entry(self.tab3, width='5')
        self.length_inp_2 = tk.Entry(self.tab3, width='5')
        self.length_inp_3 = tk.Entry(self.tab3, width='5')
        self.length_inp_4 = tk.Entry(self.tab3, width='5')
        self.length_inp_5 = tk.Entry(self.tab3, width='5')
        self.length_inp_6 = tk.Entry(self.tab3, width='5')
        self.length_inp_7 = tk.Entry(self.tab3, width='5')
        self.length_inp_8 = tk.Entry(self.tab3, width='5')
        self.length_inp_1.grid(row='7', column='1', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_2.grid(row='7', column='2', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_3.grid(row='7', column='3', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_4.grid(row='7', column='4', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_5.grid(row='7', column='5', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_6.grid(row='7', column='6', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_7.grid(row='7', column='7', columnspan='1', padx='5', pady='5', sticky='w')
        self.length_inp_8.grid(row='7', column='8', columnspan='1', padx='5', pady='5', sticky='w')

        self.pipeParamCanv = tk.Canvas(self.tab3, width='850', height='200')
        self.pipeParamCanv.grid(row='10', column='0', columnspan='6')


        self.ntb.grid(row='3', column='0', columnspan='4', padx='5', pady='5')


root = tk.Tk()
root.title('Расчет вместимости нефтепродуктопровода')
root.geometry('1024x768')
app = Application(master=root)

app.mainloop()
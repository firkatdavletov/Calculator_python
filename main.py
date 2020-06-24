import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self)
        self.title["text"] = "ПРОТОКОЛ\nизмерений параметров технологического оборудования"
        self.title.pack(side="top")

        self.frame1 = tk.Frame(self)
        self.frame1.pack()

        self.group = tk.Label(self.frame1)
        self.group['text'] = 'Группа'
        self.group.pack(side='left', padx=30)

        self.inputGroup = tk.Entry(self.frame1)
        self.inputGroup.pack(side='left', padx=5, pady=5)


        self.inputCategory = tk.Entry(self.frame1)
        self.inputCategory.pack(side='right', padx=5, pady=5)

        self.category = tk.Label(self.frame1)
        self.category['text'] = 'Категория'
        self.category.pack(side='right', padx=30)

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        self.companyName = tk.Label(self.frame2)
        self.companyName['text'] = 'Организация (предприятие)'
        self.companyName.pack(side='left')

        self.inputCompanyName = tk.Entry(self.frame2)
        self.inputCompanyName.pack(side='right')

        self.subtitle1 = tk.Label(self)
        self.subtitle1['text'] = 'Б.1 Технологический нефтепродуктопровод'
        self.subtitle1.pack()

        self.frame3 = tk.LabelFrame(self)
        self.frame3['text'] = 'Б.1.1 - Общие данные'
        self.frame3.pack()

        self.registerNumber = tk.Frame(self.frame3)
        self.registerNumber.pack()

        self.registerNumberLbl = tk.Label(self.registerNumber)
        self.registerNumberLbl['text'] = 'Регистрационный номер:'
        self.registerNumberLbl.pack(side='left')

        self.date = tk.Frame(self.frame3)
        self.date.pack()

        self.dateLbl = tk.Label(self.date)
        self.dateLbl['text'] = 'Дата:'
        self.dateLbl.pack(side='left')

        self.day = tk.Frame(self.date)
        self.day.pack(side='left')

        self.dayInp = tk.Entry(self.day)
        self.dayInp.pack()

        self.dayLbl = tk.Label(self.day)
        self.dayLbl['text'] = 'день'
        self.dayLbl.pack()

        self.month = tk.Frame(self.date)
        self.month.pack(side='left')

        self.monthInp = tk.Entry(self.month)
        self.monthInp.pack()

        self.monthLbl = tk.Label(self.month)
        self.monthLbl['text'] = 'месяц'
        self.monthLbl.pack()

        self.year = tk.Frame(self.date)
        self.year.pack(side='left')

        self.yearInp = tk.Entry(self.year)
        self.yearInp.pack()

        self.yearLbl = tk.Label(self.year)
        self.yearLbl['text'] = 'год'
        self.yearLbl.pack()

        self.cause = tk.Frame(self.frame3)
        self.cause.pack()

        self.causeName = tk.Label(self.cause)
        self.causeName['text'] = 'Основание для проведения измерений'
        self.causeName.pack(side='left')

        self.causeTxt = tk.Text(self.cause, height=4)
        self.causeTxt.pack(side='left')

        self.place = tk.Frame(self.frame3)
        self.place.pack()

        self.placeName = tk.Label(self.place)
        self.placeName['text'] = 'Место проведения измерений'
        self.placeName.pack(side='left')

        self.placeTxt = tk.Text(self.place, height=4)
        self.placeTxt.pack(side='left')

        self.innacuracy = tk.Frame(self.frame3)
        self.innacuracy.pack()

        self.innacuracyName = tk.Label(self.innacuracy)
        self.innacuracyName['text'] = 'Погрешность определения вместимости технологического\nнефтепродуктопровода, %'
        self.innacuracyName.pack(side='left')

        self.innacuracyTxt = tk.Text(self.innacuracy, height=4)
        self.innacuracyTxt.pack(side='left')

        self.devices = tk.Frame(self.frame3)
        self.devices.pack()

        self.devicesName = tk.Label(self.devices)
        self.devicesName['text'] = 'Средства измерений'
        self.devicesName.pack(side='left')

        self.devicesTxt = tk.Text(self.devices, height=4)
        self.devicesTxt.pack(side='left')

        self.condOfMeas = tk.LabelFrame(self)
        self.condOfMeas['text'] = 'Б.1.2 - Условия проведения измерений'
        self.frame3.pack()

        self.temp = tk.Frame(self.condOfMeas)
        self.temp.pack()

        self.tempName = tk.Label(self.condOfMeas)
        self.tempName['text'] = 'Температура воздуха, &#8451 С'
        self.tempName.pack(side='left')








        self.registerNmberInp = tk.Entry(self.registerNumber)
        self.registerNmberInp.pack()



        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title('Расчет вместимости нефтепродуктопровода')
root.geometry('600x600')
app = Application(master=root)

app.mainloop()
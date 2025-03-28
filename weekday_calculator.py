#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Input in entry boxes of 'Year', 'Month' and 'Day"""
"""Month must be written as an integer between 1-12"""
"""Press "Calculate" button to return weekday of given date"""

"""Importing necessary modules"""
from time import*
from tkinter import*

class Calculator_UI():
    def __init__(self, master):
        """Initializes GUI window as well as entry boxes."""
        self.master = master
        self.months = ['January', 'january', 'February',
                       'february', 'March', 'march',
                       'April', 'april', 'May', 'may',
                       'June', 'june', 'July','july',
                       'August', 'august', 'September',
                       'september','October', 'october',
                       'November', 'november',
                       'December', 'december']
        master.title('Weekday Calculator')
        master.geometry('410x400')
        master.resizable(width = False, height = False)
        self.Label('Weekday Calculator', 18, 0)
        self.Label('This program determines the specific weekday'
                   ' for given dates \n'
                   '| Year (yyyy) | Month (mm) | Day (dd) |', 13, 1)
        entries = []
        name = ['Year:', 'Month:', 'Day:', 'Week:', 'Extra:']
        self.entries = []
        for i in range(1, 6):
            self.label = Label(root, padx = 9, text = name[i-1],
                         font = ('Avenir', 13, 'normal'))
            self.label.grid(row = i+1, sticky = W, padx = 1)
            self.display = Entry(root, width = 33)
            self.display.grid(row = i+1, column = 1, sticky = E)
            self.entries.append(self.display)
        for i in range(3, 5):
            self.entries[i].configure(state='readonly')
        self.Buttons()
        self.Label('Raymond Wang 2018 ®', 13, 11)

    def Label(self, sentence, size, num):
        """Initializes Labels."""
        self.Description = Label(root, text= sentence,
        font = ('Avenir', size, 'normal'))
        self.Description.grid(row = num, column = 0,
                         columnspan = 7, padx = 5, pady = 5)

    def Buttons(self):
        """Initializes buttons."""
        name = ['Calculate', 'Clear', 'Exit']
        command_name = [lambda:Input.calculate(self),
                        lambda:Input.clear(self),
                        root.destroy]
        for i in range(1, 4):
            self.Button = Button(root, text = name[i-1],
                          command = command_name[i-1],
                          font = ('Avenir', 15, 'normal'))
            self.Button.grid(row = i+7, column = 0, columnspan = 8,
                          padx = 10, pady = 5, sticky =  N+S+E+W)

class Input():
    """Evaluates whether input is correctly given
    and returns a specific message."""
    def clear(self):
        """Command of the Clear button.
        Clears each individual entry box"""
        for i in range(5): #Year, Month and Day
            self.entries[i].delete(0,END)
        for i in range(3, 5): #Week and Extra
            Input.clear_display(self, self.entries[i])
            self.entries[i].configure(state='readonly')

    def clear_display(self, func):
        """Clearing specific display before output."""
        func.configure(state='normal')
        func.delete(0,END)

    def calculate(self):
        """Main algorithm of the program.
        Returns input from each individual entry box.
        if inputs for year and month are correctly given,
        proceed to error handling for day
        of months.
        If otherwise, return error output."""
        year = (self.entries[0]).get()
        month = (self.entries[1]).get()
        day = (self.entries[2]).get()

        if year.isdigit():
            if year[0] == '0':
                if len(year) == 1:
                    Input.change_display(self, self.entries[4],
                    'Year 0 does not exist') #Error message in Extra-Display
                else:
                    Input.change_display(self, self.entries[4],
                    'Remove preceding zeros')
            elif month.isdigit():
                Input.month_digit(self, year, month, day)
            elif month in self.months:
                month = month.capitalize()
                month_to_int = {'January':1, 'February':2,
                'March':3, 'April':4,'May':5, 'June':6,
                'July':7, 'August':8, 'September':9,
                'October':10, 'November':11, 'December':12}
                Month = str(month_to_int[month])
                Input.month_digit(self, year, Month, day)
            elif month.isdigit() == False:
                Input.change_display(self, self.entries[4],
                'Enter month between 1-12 or month name')
        elif len(year) == 0 and len(month) == 0 and len(day) == 0:
            Input.change_display(self, self.entries[4], '')
        else:
            Input.change_display(self, self.entries[4], 'Error')

    def month_digit(self, year, month, day):
        """Error handling for zeros in month input."""
        if (month[0] == '0' and len(month) > 2 or
            day.isdigit() and day[0] == '0' and len(day) > 2):
            Input.change_display(self, self.entries[4],
            'Remove preceding zeros')
        else:
            Input.day_of_months(self, year, month, day.lstrip('0'))

    def day_of_months(self, year, month, day):
        """Error handling for day of months.
        If input is correctly given, proceed to output of message.
        If otherwise, return error message."""
        if month.isdigit() and int(month) < 13:
            if (int(month) in [1,3,5,7,8,10,12]):
                Input.condition(self, year, month, day, '31', '')
            elif (int(month) in [4,6,9,11]):
                Input.condition(self, year, month, day, '30', '')
            elif int(month) == 2:
                if (((int(year) % 4) == 0 and
                not (int(year) % 100) == 0)
                or (int(year) % 400) == 0):
                    if int(year) == 1712 and int(day) == 30:
                            """Easter Egg."""
                            Input.condition(self, year, month, day, '30','')
                            Input.special_case(self)
                    else:
                        Input.condition(self, year, month, day, '29',' ')
                else:
                    Input.condition(self, year, month, day, '28', '29')
        else:
            Input.change_display(self, self.entries[4],
            'Enter month between 1-12 or month name')

    def condition(self, year, month, day, lastday, leapday):
        """Error handling for day input."""
        try:
            if len(day) == 0 or int(day) > int(lastday):
                if int(month) == 2 and day == leapday:
                    Input.change_display(self, self.entries[4],
                    'Not a leap year')
                else:
                    Input.change_display(self, self.entries[4],
                    'Enter day between 1-' + lastday)
            elif int(day) <= int(lastday):
                Input.change_display(self, self.entries[3], #Weekday message
                Output.message(self, year, month, day))
        except:
            Input.change_display(self, self.entries[4],
            'Enter day between 1-' + lastday)

    def special_case(self):
        """Output for Easter Egg."""
        Input.clear_display(self, self.entries[4])
        self.entries[4].insert(INSERT, '1712/02/30 was a real date in Sweden')
        self.entries[4].configure(state='readonly')

    def change_display(self, func, text):
        """Clears output displays and inserts desired message."""
        for i in range(3, 5):
            Input.clear_display(self, self.entries[i])
        func.insert(INSERT, text)
        for i in range(3, 5):
            self.entries[i].configure(state='readonly')

class Output():
    def message(self, year, month, day):
        """Initially returns current date and compares it with given date,
        in order to determine specific output. Returns short message
        with desired weekday thereafter."""

        weekday = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
        a = int((14 - int(month))/12)
        y = int(year) - a
        m = int(month) + (12*a) -2
        d = (int(day) + y + int(y/4) - int(y/100) +
        int(y/400) + int((31*m)/12)) % 7
        x = weekday[d]
        name = Output.wordmonth(self, month)
        Day = Output.ordinal(self, day)
        weekday_txt = name + ' ' + Day + ', ' + year

        StrYear = int(strftime('%Y'))
        StrMonth = int(strftime('%m'))
        StrDay = int(strftime('%d'))
        DisplayTime = Output.JulianDN(self, year, month, day)
        CurrentDate = Output.JulianDN(self, StrYear, StrMonth, StrDay)

        if DisplayTime == CurrentDate:
            text = Output.final_output(self, '','Today is a ', x)
        elif DisplayTime == CurrentDate + 1:
            text = Output.final_output(self, '','Tomorrow will be a ', x)
        elif DisplayTime == CurrentDate - 1:
            text = Output.final_output(self, '','Yesterday was a ', x)
        elif DisplayTime > CurrentDate:
            text = Output.final_output(self, weekday_txt,' will be a ', x)
        elif DisplayTime < CurrentDate:
            text = Output.final_output(self, weekday_txt,' was a ', x)
        return text

    def final_output(self, date, text, day_of_week):
        """Determines final output message of given input date."""
        output = (date + text + day_of_week)
        return output

    def ordinal(self, day):
        """Returns specific ordinal suffix for given day number
        and attaches it to given day input as a string."""
        teen_numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        output = ['th','st', 'nd', 'rd', 'th', 'th',
                    'th', 'th', 'th', 'th', 'th']
        if int(day) in teen_numbers:
            return (day + 'th')
        else:
            return (day + output[int(day[-1])])

    def JulianDN(self, Y,M,D):
        """Calculates Julian Date Number for specific input date
        in order to subsequently determine when it occurs.
        and finally output."""
        a = int((14 - int(M))/12)
        y = int(Y) + 4800 - a
        m = int(M) + (12 * a) - 3
        JDN = (int(D) + int(((153 * m) + 2) /5) + (365 * y)
        + int(y/4) - int(y/100) + int(y/400) - 32045)
        return JDN

    def wordmonth(self, month):
        """Returns specific month name from given input of
        month number."""
        monthname = [word for word in self.months if word.istitle()]
        Month = int(month) -1
        return monthname[Month]

if __name__ == '__main__':
    """Callback."""
    root = Tk()
    Calculator_UI(root)
    root.mainloop()

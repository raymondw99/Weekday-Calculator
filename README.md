# Weekday Calculator 
This program calculates the weekday of every given date. Input in the entry boxes of 'Year', 'Month' and 'Day'. Month must be written as a number between 1-12. Press "Calculate" button to return weekday of the given date.

Implemented as a final project in [DD1331 Fundamentals of Programming](https://www.kth.se/student/kurser/kurs/DD1331?l=en). 
## Specifikation

### Inledning
Jag tänker skapa ett Pythonprogram som frågar efter årtal (yyyy), månad (mm) och dag (dd) och därefter, med hjälp av lämpliga formler räkna ut vilken veckodag detta datum infaller eller inföll på. Själva beräkningen ska göras i en funktion som tar år, månad och dag som parametrar. Formlerna ger såklart veckodagen som heltal, men funktionen bör returnera veckodag i klartext.

Programmet kommer köras som en GUI med inmatningsfält för år, månad, respektive dag samt fält för utmatning av veckodag. En av de största utmaningarna med detta projekt är först och främst att finna en lämplig formel för beräkningen, men även felhantering, då datum måste vara korrekt skrivna och inget annat än positiva heltal eller månadsnamnen får förekomma.

### Användarscenarier
Mata in årtal, månad och dag enligt formaten (yyyy), (mm)/månadsnamn, (dd). Om det inmatade datumet infaller med dagens datum kommer exempelvis följande skrivas ut:
```
Today is a Monday
```
Annars utmatas följande:
```
Yesterday was a Saturday
Tomorrow will be a thursday
```
I andra fall utmatas något av exempelvis nedanstående:
```
December 28th, 1999 was a Tuesday
June 21st, 2020 will be a Sunday
```
En anmärkning är att meningen som skrivs ut bör förhålla sig enligt korrekt engelsk ortografi. Ordningstalets suffix (Ordinal indicator) ska skrivas ut efter datumet om det inföll innan eller infaller efter dagens datum. I allmäna fall ska utmatningen förhålla enligt formatet [Month] [day+ suffix], [year] [was a/will be a] [weekday]. 

### Felhantering
Under inmatningen ska programmet först kontrollera om inmatningen av datum är korrekt. Därför bör nedanstående punkter tas i hänsyn.
* Existerar datum? T ex 30/2 och 12/13 existerar inte.
* Om blankt inmatas bör detta också kunna hanteras
* Månad och dag får ex. skrivas i formaten mm eller dd. Om onödigt många nollor föregår ska detta tas i hänsyn. 
  Liknande gäller för år    (yyyy). Ex. tillåts mm: 03 och dd: 01 (eller mm: 3, dd: 1) men inte mm: 004, dd: 0006.
* Innehåller det inmatade datumet annat än siffror (”o” istället för 0 etc)?

Hänsyn ska tas till eventuellt skottår, som definieras enligt: 
```
(årtal % 4 = 0) och (årtal % 4 ≠ 0) 
eller årtal % 400 = 0
```
När felaktig inmatning påträffas ska programmet kommentera felets art, dvs enligt vilka av de ovanstående punkterna som inmatningen inte förhåller.

# Kodskelett
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Input in entry boxes of 'Year', 'Month' and 'Day"""
"""Month must be written as an integer between 1-12"""
"""Press "Calculate" button to return weekday of given date"""

from time import*
from tkinter import*
    
class Calculator(object):
    """Class for GUI window"""
    def __init__(self, master):
        """Initializes GUI window and defines its specifications."""
        ...
        self.Title_and_Entry()
        self.Buttons()

    def Title_and_Entry(self):
        """Initializes text and entry boxes"""
        ...

    def Buttons(self):
        """Initializes buttons."""
        ...

class functions(object):
    """Functions and algorithms."""      
    def clear(self):
        """Command of the Clear button.
        Clears each individual entry box"""
        ...

    def clear_display(self, func):
        """Clearing specific display before output."""
        ...
        
    def calculate(self):
        """Main algorithm of the program.
        Returns input from each individual entry box.
        if inputs for year and month are correctly given,
        proceed to error handling for day 
        of months. If otherwise, return error output."""
        ...

    def output(self, year, month, day):
        """Error handling for day of months.
        If input is correctly given,proceed to output of message.
        If otherwise, return error message."""
        ...

    def change_display(self, func, text):
        """Clears output displays and inserts desired message."""
        ...
        
    def message(self, year, month, day):
        """Initially returns current date and compares it with given date,
        in order to determine specific output. Returns short message
        with desired weekday subsequently."""
        ...
    
    def final_output(self, date, text, day_of_week):
        """Determines final output message on given input date.""" 
        ...

    def ordinal(self, day):
        """Returns specific ordinal suffic for given day number
        and attaches it to given day input as a string."""
        ...

    def JulianDN(self, Y,M,D):
        """Calculates weekday integer from given date with
        the Julian Date Number algorithm.
        Returns value for further manipulation and output."""
        ...

    def wordmonth(self, month):
        """Returns specific month name from given input of 
        month number."""
        ...

if __name__ == '__main__':
    """Callback."""
    root = Tk()
    Calculator(root)
    root.mainloop

"""Deviation from framework as well as additional functions possible."""
```
# Programflöde 
Programmet börjar med att skapa ett GUI-fönster. Användaren matar sedan in år, månad och dag i respektive inmatningsfält. För att därefter få motta utskrift klickas knappen "Calculate". Meddelanden syns i "Weekday"-fältet.  Vid inkorrekt inmatning sker utskrift av felmeddelanden i det understa fältet. För att rensa utskrift eller inmatning klickas knappen "Clear". Om användaren i annat fall vill avsluta programmet klickas "Exit"-knappen.

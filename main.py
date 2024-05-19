from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
 
 
 
def show_selected_dates(calendar, event_text, selected_dates, events):
   event_text.delete(1.0, END)
 
 
   for selected_date in selected_dates:
       events_for_date = events.get(selected_date, [])
       event_text.insert(END, f"Events for {selected_date}:\n")
       for event in events_for_date:
           event_text.insert(END, f"- {event}\n")
 
 
 
def add_event(calendar, event_text, selected_dates, events, event_entry):
   event = event_entry.get()
 
 
   if not event:
       messagebox.showwarning("Empty Event", "Please enter an event.")
       return
 
 
   for selected_date in selected_dates:
       if selected_date not in events:
           events[selected_date] = []
       events[selected_date].append(event)
 
 
   # Update the displayed events
   show_selected_dates(calendar, event_text, selected_dates, events)
 
 
   # Clear the event entry
   event_entry.delete(0, END)
 
 
 
def select_date(calendar, selected_dates):
   selected_date = calendar.get_date()
   selected_dates.append(selected_date)
   messagebox.showinfo("Selected Date", f"You selected: {selected_date}")
 
 
 
def create_calendar(root):
   # Create a calendar with a specific date pattern
   calendar = Calendar(root, setmode="day", date_pattern='d/m/yy')
   calendar.pack(padx=15, pady=15)
   return calendar
 
 
 
def create_select_date_button(root, calendar, event_text, selected_dates, events):
   # Create a button to select the date
   select_date_button = Button(root, text="Select Date", command=lambda: select_date(calendar, selected_dates))
   select_date_button.pack(padx=15, pady=5)
 
 
   # Create an entry for adding events
   event_entry_label = Label(root, text="Add Event:")
   event_entry_label.pack(pady=5)
 
 
   event_entry = Entry(root, width=20)
   event_entry.pack(pady=5)
 
 
   # Create a button to add events
   add_event_button = Button(root, text="Add Event",
                             command=lambda: add_event(calendar, event_text, selected_dates, events, event_entry))
   add_event_button.pack(pady=15)
 
 
 
def create_event_text(root):
   # Create a Text widget to display events
   event_text = Text(root, height=8, width=30)
   event_text.pack(padx=15, pady=15)
   return event_text
 
 
 
def main():
   root = Tk()
   root.title("Improved Calendar App - The Pycodes ")
   root.geometry("400x530")
   root.configure(bg="lightblue")
 
 
   # Lists to store selected dates
   selected_dates = []
 
 
   # Dictionary to store events for each date
   events = {}
 
 
   calendar = create_calendar(root)
   event_text = create_event_text(root)
   create_select_date_button(root, calendar, event_text, selected_dates, events)
 
 
   root.mainloop()
 
 
if __name__ == "__main__":
   main()

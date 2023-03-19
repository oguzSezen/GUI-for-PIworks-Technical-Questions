import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import *  # tkinter libraries

ui = tk.Tk()
# ui.iconbitmap(icon directory)  #An Icon can be added
ui.title('User Interface')

ui.geometry("1300x700+350+200")  # Size of UI
ui.resizable(False, False)  # Can not resize
ui.state('normal')

# --------------------------------------TREEVIEW---------------------------------
style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview.Heading',  # These are the customizable setting for the headers
                background="#007CBA",
                foreground="White",
                rowheight=200,
                relief='flat'
                )
style.configure('Treeview',  # These are the customizable setting for the elements in the table
                background="silver",
                foreground="black",
                height=10,
                relief='groove',
                rowheight=45,
                )
style.map('Treeview', background=[('selected', "#56A7CF")])  # recolor the selected element(foreground white is default)

# CREATING THE TABLE
tree_frame = Frame(ui, height=5000)
tree_frame.pack(anchor=W, pady=100)

tree_scroll = Scrollbar(tree_frame)  # I added a scrollbar for better usability
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
tree_scroll.config(command=my_tree.yview)

# Formatting the columns
my_tree['columns'] = ("ID", "User Name", "Email", "Enabled")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=50)
my_tree.column("User Name", anchor=W, width=150)
my_tree.column("Email", anchor=W, width=300)
my_tree.column("Enabled", anchor=W, width=75)

# Creating Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("User Name", text="User Name", anchor=W)
my_tree.heading("Email", text="Email", anchor=W)
my_tree.heading("Enabled", text="Enabled", anchor=W)

# ------------------------------------WELCOME TAB--------------------------------

welcome: str = 'Welcome!\n\n\nYou can inspect the current users on the table on the left side.\n\nIn order to add a ' \
               'new user, please press the "+New User" button'
welcome_label = tk.Label(justify='left', text=welcome, font='Arial 10')
welcome_label.place(relx=0.75, rely=0.5, anchor="center")

#------------------------------ALREADY SAVED USERS -------------------------------

# This place can be connected to a database in order to fill the userlist tree from start.
# But the code needs some changes like making the counter start from the last persons ID number etc.
# Plus filling the table with values needs to be added on startup.

# ----------------------------------SAVE USER-------------------------------------

global userlist
onlyEnabled_userlist = []  # only enabled users
all_userlist = []  # all users

user_id_list = [0]


def save_user():
    if not (username_entry.get() and displayName_entry.get() and
            phone_entry.get() and email_entry.get() and user_roles_combobox.get()):  # Empty space error
        messagebox.showinfo(title='Error', message='Please fill all the boxes')

    elif not phone_entry.get().isdigit():  # Phone number error
        messagebox.showinfo(title='Error', message='Please use only numbers for phone number')

    elif not '@' in email_entry.get():  # Invalid mail error
        messagebox.showinfo(title='Error', message='Please write a valid email')

    # The errors can be extended

    else:

        if is_enabled.get() == 0:  # disabled users
            enabled = 0
        else:  # enabled users
            enabled = 1

        i = user_id_list[-1]  # i for counting ID list

        if enabled:
            temporary_list = [int(i + 1), username_entry.get(), displayName_entry.get(), phone_entry.get(),
                              email_entry.get(), user_roles_combobox.get(), bool(enabled)]
        # Up here we are getting the values from the boxes with only enabled users and putting them in a new empty list
            onlyEnabled_userlist.append(temporary_list)  # Now we add our empty list to the list with only enabled users
            user_id_list.append(i + 1)

        temporary_list = [int(i + 1), username_entry.get(), displayName_entry.get(), phone_entry.get(),
                          email_entry.get(), user_roles_combobox.get(), bool(enabled)]
        # Now we get the information of all users

        all_userlist.append(temporary_list)  # And put them in the list just like before
        user_id_list.append(i + 1)

        my_tree.insert(parent='', index='end', iid=i, text="",  # Inserting the values in the table/tree
                       values=(all_userlist[i][0], all_userlist[i][1], all_userlist[i][4], bool(enabled)))
        new_user()


# --------------------------------NEW USER INFORMATION---------------------------
x_pos = 700
y_pos = 180
y_space_between = 75   # Position constants


def new_user():
    # Save user button
    save_user_button = tk.Button(ui, text="Save User", fg='white', bg='#56A7CF', font='Arial 15',
                                 command=save_user)
    save_user_button.place(x=1120, y=30, width=150, height=40)

    # Clearing the first welcoming area
    welcome_label.destroy()

    # Listing the desired information
    newUser_label = tk.Label(text='New User', font='Arial 25 ', fg='#616C7B')
    newUser_label.place(x=675, y=100, width=150, height=40)

    global username_entry  # <-- Here we have the entry information
    username_entry = tk.Entry()
    username_entry.place(x=820, y=y_pos, width=420, height=30)  # <-- Here we create our box
    username_label = tk.Label(text='Username:')  # <-- Here we put the label for information box
    username_label.place(x=700, y=y_pos + 5)

    global displayName_entry
    displayName_entry = tk.Entry()
    displayName_entry.place(x=820, y=y_pos + y_space_between * 1, width=420, height=30)
    displayName_label = tk.Label(text='Display Name:')
    displayName_label.place(x=700, y=y_pos + y_space_between * 1 + 5)

    global phone_entry
    phone_entry = tk.Entry()
    phone_entry.place(x=820, y=y_pos + y_space_between * 2, width=420, height=30)
    phone_label = tk.Label(text='Phone:')
    phone_label.place(x=700, y=y_pos + y_space_between * 2 + 5)

    global email_entry
    email_entry = tk.Entry()
    email_entry.place(x=820, y=y_pos + y_space_between * 3, width=420, height=30)
    email_label = tk.Label(text='Email:')
    email_label.place(x=700, y=y_pos + y_space_between * 3 + 5)

    # User Roles Combobox  --- This one is a bit different. The box has multiple choices to select from.
    global user_role_string
    user_role_string = tk.StringVar()
    global user_roles_combobox
    user_roles_combobox = Combobox(values=('Guest', 'Admin', 'SuperAdmin'),
                                   textvariable=user_role_string, state="readonly")  # Read-only state is used
                                   # textvariable goes to the StringVar function and gives the string to the previously
                                   # used user_roles_combobox.get() function
    user_roles_combobox.place(x=820, y=y_pos + y_space_between * 4, width=420, height=30)
    user_roles_label = tk.Label(text='User Roles:')
    user_roles_label.place(x=700, y=y_pos + y_space_between * 4 + 5)

    # Enabled check box --- Again for being a checkbox this one is a little different too.
    global is_enabled
    is_enabled = tk.IntVar()
    is_enabled.set(0)  # Set to the false for the beginning

    global enabled_check
    enabled_check = tk.Checkbutton(variable=is_enabled)
    enabled_check.place(x=820, y=y_pos + y_space_between * 5)
    enabled_label = tk.Label(text='Enabled:')
    enabled_label.place(x=700, y=y_pos + y_space_between * 5 + 5)


# --------------------------------NEW USER BUTTON--------------------------------

new_user_button = tk.Button(text="+ New User", fg='white', bg='#007CBA', font='Arial 14 bold', command=new_user)
# Upon clicking this button new_user function is called
new_user_button.place(x=30, y=30, width=150, height=40)

# -----------------------------Check Button Images--------------------------------
checkbutton_off = PhotoImage(file="check button bos.png")
checkbutton_on = PhotoImage(file="check button.png")


# --------------------------HIDE DISABLED USER BUTTON-----------------------------
def disabled_users():
    for item in my_tree.get_children():  # First we clear the table
        my_tree.delete(item)

    for i in range(0, len(all_userlist)):
        if all_userlist[i][6]:  # all_userlist[i][6] denotes to the enabled value which is either true or false.
                                # If it is true, only the enabled users are being written on the table.
            my_tree.insert(parent='', index='end', iid=i, text="",
                           values=(all_userlist[i][0], all_userlist[i][1], all_userlist[i][4], all_userlist[i][6]))



def all_users():  # Same as disabled users, but this function doesn't consist the if statement, so it writes all users
                  # on the table
    for item in my_tree.get_children():
        my_tree.delete(item)

    for i in range(0, len(all_userlist)):
        my_tree.insert(parent='', index='end', iid=i, text="",
                       values=(all_userlist[i][0], all_userlist[i][1], all_userlist[i][4], all_userlist[i][6]))


State_on_off = 0  # Button is set to 0 for beginning


def on_off(event):
    global State_on_off
    if State_on_off == 1:
        checktest.config(image=checkbutton_off)  # Changes the image of the button
        State_on_off = 0  # Changing the state
        all_users()  # Calls for all_users function
    else:
        checktest.config(image=checkbutton_on)  # Changes the image
        State_on_off = 1  # Changing the state
        disabled_users()  # Calls the function for disabled users


chektestbox = IntVar()
checktest = Label(ui, image=checkbutton_off)
checktest.bind("<Button-1>", on_off)  # Clicking on the button triggers on_off function
checktest.place(x=240, y=37)  # Position of button

disabled_label = tk.Label(text='Hide Disabled Users', font='Arial 13')
disabled_label.place(x=265, y=37)

# -----------------------------Check Button Images--------------------------------
triangle_up = PhotoImage(file="triangle_up.png")
triangle_down = PhotoImage(file="triangle_down.png")


# ------------------------Sorting BUTTONS--------------------------------


def takeName(elem):
    # Getting the value from functions which is 0 for ID, 1 for Name, 4 for email, 6 for enabled or not
    global filter_element
    return elem[filter_element]  # returns the desired row for sorting


def sorting():
    all_userlist.sort(key=takeName, reverse=is_reversed)  # sorting the list of users according to the index taken
                                                          # from takeName function.
                   #If is_reversed = 1 comes from clicking the filter buttons, the sorting will be on the reverse order

    if State_on_off == 1:  # If "Hide Disabled Users" is checked
        disabled_users()   # Then only the disabled users information will be written

    for item in my_tree.get_children():
        my_tree.delete(item)  # clearing the table first...

    for i in range(0, len(all_userlist)):  # ...and the writing them on the table
        my_tree.insert(parent='', index='end', iid=i, text="",
                       values=(all_userlist[i][0], all_userlist[i][1], all_userlist[i][4], all_userlist[i][6]))


# ----- Sorting  by Name -----------------------

State_name = 0  # State of name filtering is first set to 0
is_reversed = 0  # State of reverse


def name_up(event):
    global State_name
    global filter_element
    global is_reversed
    filter_element = 1  # <-- goes to the filtering() and then to the takeName() in order to define the index for
                        # deciding which value to sort
    if State_name == 1:
        triangle_name.config(image=triangle_up)  # <-- Changes image
        State_name = 0  # <-- Changes state
        is_reversed = 1  # <-- Decides to reverse or not
        sorting()  # <-- Calls for the function

    else:
        triangle_name.config(image=triangle_down)
        State_name = 1
        is_reversed = 0
        sorting()


triangle_name = Label(ui, image=triangle_up)  # <-- Putting the image of filter button
triangle_name.bind("<Button-1>", name_up)  # <-- First value represents "Clicking on button", second calls for the
                                           # function)
triangle_name.place(x=160, y=106)  # <-- Position of button

# ----- Sorting  by ID -----------------------

State_id = 0


def id_up(event):
    global State_id
    global filter_element
    global is_reversed
    filter_element = 0
    if State_id == 1:
        triangle_id.config(image=triangle_up)
        State_id = 0
        is_reversed = 1
        sorting()

    else:
        triangle_id.config(image=triangle_down)
        State_id = 1
        is_reversed = 0
        sorting()


triangle_id = Label(ui, image=triangle_up)
triangle_id.bind("<Button-1>", id_up)
triangle_id.place(x=30, y=106)

# ----- Sorting  by email -----------------------

State_email = 0


def email_up(event):
    global State_email
    global filter_element
    global is_reversed
    filter_element = 4
    if State_email == 1:
        triangle_email.config(image=triangle_up)
        State_email = 0
        is_reversed = 1
        sorting()

    else:
        triangle_email.config(image=triangle_down)
        State_email = 1
        is_reversed = 0
        sorting()


triangle_email = Label(ui, image=triangle_up)
triangle_email.bind("<Button-1>", email_up)
triangle_email.place(x=470, y=106)

# ----- Sorting  by enabled -----------------------
State_enabled = 0


def enabled_up(event):
    global State_enabled
    global filter_element
    global is_reversed
    filter_element = 6
    if State_enabled == 1:
        triangle_enabled.config(image=triangle_up)
        State_enabled = 0
        is_reversed = 1
        sorting()

    else:
        triangle_enabled.config(image=triangle_down)
        State_enabled = 1
        is_reversed = 0
        sorting()


triangle_enabled = Label(ui, image=triangle_up)
triangle_enabled.bind("<Button-1>", enabled_up)
triangle_enabled.place(x=555, y=106)

ui.mainloop()

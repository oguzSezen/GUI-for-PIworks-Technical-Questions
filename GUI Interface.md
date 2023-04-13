# USER MANAGEMENT INTERFACE

We need to create a user management interface. The purposes of this table is to:
- Show general information about personels
- Enter in a new user
- Change existing users information 

* * * 
* * * 
## Logging in

Before everything, the user must log in to the system. In this way, according to the authority the user has, the functions which the user can be perform will be limited.

 >These limitations and roles are noted later in the document.

* * * 

## Table of Existing Users

After logging in, a table with general information about existing users should be displayed on the left side of the interface. The table needs to show four elements:
- user's `ID` number
- `User name`
- user's `Email` address
- if  the user is `Enabled` or not

This table can be in the form of an Microsoft Excel sheet. For this purpose, the required table is given below as: 


| ID | User name | Email | Enabled |
|--- |--- |--- |---
|1 | First user's username | email1@gmail.com | true (if enabled)
|2 | Second user's username | email2@itu.edu.tr | false (if **not** enabled)
*3,4,5...* | *username* | *.............@piworks.net* | *true or false*

**!!! IT IS IMPORTANT TO REFLECT THIS TABLE AS CLOSE AS POSSIBLE !!!**


## The functions on this table

### **1- Sorting**

For every column (in total 4), a sort button should be added in the headers of the table. The function of these buttons are to :
- sort the ID numbers in ascending order. (for `ID`)
- list user names and emails in alphabetical order. (for `User Name`, `Email`, plus this function can be used for `Enabled` since it also shows a word)
- separate true and false values

Furthermore, upon clicking one more time on this button, it should reverse the order of the first function. This cycle of re-pressing on the button should repeat.

### **2- Hiding disabled users**

Another function that is needed is to looking only for the enabled users. For this applicaton a checkbox labeled as `Hide Disabled User` is needed. 
By checking this box, the information about disabled users (users with enabled value "false") should disappear on the table.
In another words, only the enabled users will be shown.


### **3.1- Looking at user information**

Whenever the user clicks on an another user on the table, its existing information should be displayed on the right hand side of the screen. 

> Right side of the screen is descripted in the upcoming **Creating a New User** part. Required informations such as `username`, `phone number` etc. will stay the same for this part but only the header will change from `New User` to user's `username`. For example, if the user's user name is "AdminUser", after clicking on this user from the table, the header will be changed to "AdminUser".

### **3.2- Changing User Information**

Plus, the existing user's information can be changed and edited from the right side of the interface.

> Yet again, the save button in **Creating a New User** part can be utilised for this purpose too.


### **4- Deleting a user**

Whenever a user is right clicked from the table, a deleting option should appear. To avoid mistakes, a window prompt should appear asking if the user is sure to delete an user.


* * *
## Creating a New User

**There will be a `+New User` button on the upper left edge of the interface. This button will start upcoming functions.**

For the area from the middle to the right edge of the interface, there will be a place for entering in a new user. To indicate this part a header with "**New User**" can be placed.



In order to create and save a new user to the system, the user's information should be collected. 

>Additional Information! 
>>If the previous function of **Looking at user information** from **Table of Existing Users** is already in use, all of the checkboxes, entry boxes and comboboxes will be emptied out before using them.

### **The required informations are:**



1- **Username**

A simple entry box can be used.

2- **Display Name**

A simple entry box can be used.

3- **Phone Number**

A simple entry box can be used.

4- **Email address**

A simple entry box can be used.

5- **User Roles** User roles should be defined as:
 - `Guest`
 - `Admin`
 - `SuperAdmin`

In order to do this selection a combobox can be utilised.

6- **Enabled**

This selection should be a checbox. If the checkbox is marked, the new user's enabled value will be `true`; if it is unmarked, the value will be `false`.

### **Save Button**

Last things last, a button labeled as `Save User` should be added. 
The function of this button is saving and storing all of the written information into thedatabase so that it also appears in the table.

> After saving a user, an unoccupied ID number will be given to that user.

> This save button can also be used for **Changing User Information**, as stated before.

### **Error Prompts**

In order to check the validity of the given informations and prevent errors from happening, if a written information is not fitted for the given part, an error prompt should appear. Some of these scenarios are:

* For all information:
    - Username, phone number, email adress might be already used for an another user
    - An entry box may have been forgotten to fill

* `User name` and `Display Name`
    - Should be between 6 to 16 words

* `Phone` Number
    - Number of digits should be correct
    - The phone number should consist only of numbers

* `Email`
    - May not be a valid email adress
        - Checking if the mail has not "@" inside can be a easy way to evaluate
        - Or, not finishing with .com, .net etc.



* * *
## User Roles

Not every personel should have do what it desires. So the decision is to have 3 user roles.

### **1- SuperAdmin**
+ Have no limitations whatsoever.
    + Can look, edit, save, delete users.

### **2- Admin**
+ Can create a new user
+ Can look for the information of other users
+ Can edit an existing user's information but can't :
    - set the role of an user or itself to "SuperAdmin"
    - edit the information of a SuperAdmin
    - delete a SuperAdmin or another Admin

### **3- Guest**
+ Can look at other user's information but not:
    - the phone adress of an Admin or SuperAdmin

- Can **not** edit, save or delete users.
+ Can change their own display name, email, phone, enabled value.

* * *
* * *
## Design

### - Buttons

- "+New User" and "Save User" buttons should be HEX #007CBA <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAABcCAMAAADUMSJqAAAAA1BMVEUAfLoPRFGyAAAAH0lEQVRoge3BgQAAAADDoPlTX+EAVQEAAAAAAAAA8BohbAABVJpSrwAAAABJRU5ErkJggg=="  width="15" height="15">, with white text.


### - Table
- Header of the table should be HEX #007CBA <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAABcCAMAAADUMSJqAAAAA1BMVEUAfLoPRFGyAAAAH0lEQVRoge3BgQAAAADDoPlTX+EAVQEAAAAAAAAA8BohbAABVJpSrwAAAABJRU5ErkJggg=="  width="15" height="15">, with white text.
- To have better visibility, consequential rows should have different colours. Odd-numbered columns must have white background, and even-numbered columns must have HEX #B9D9E8 <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ508_ZQ4evq19ac0t1OfWQBWGhpVtUkN4Ez2Nf-ZEp&s"  width="15" height="15">, and black text.
- Whenever the function **Looking at user information** is at place, the selected row should be HEX #616C7B <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAADICAMAAAA9W+hXAAAAA1BMVEVhanu2qrdUAAAANElEQVR4nO3BMQEAAADCoPVP7WsIoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeAN1+AABVhDU2QAAAABJRU5ErkJggg=="  width="15" height="15">, and black text.

### - Checkboxes
[check button bos.png](https://github.com/oguzSezen/GUI-for-PIworks-Technical-Questions/blob/main/check%20button%20bos.png) <img src="https://github.com/oguzSezen/GUI-for-PIworks-Technical-Questions/blob/main/check%20button%20bos.png?raw=true"  width="15" height="15"> from [my github folder](https://github.com/oguzSezen/GUI-for-PIworks-Technical-Questions)  can be used for unchecked state and [check button.png](https://github.com/oguzSezen/GUI-for-PIworks-Technical-Questions/blob/main/check%20button.png) <img src="https://github.com/oguzSezen/GUI-for-PIworks-Technical-Questions/blob/main/check%20button.png?raw=true"  width="15" height="15"> can be used for checked state.







import tkinter as tk
import random

def createGUI():
    dictionary = {}

    def get_data():
        if dictionary:
            try:
                key = int(file_id.get())
                if key in dictionary:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, dictionary[key])
                else:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, "File was not found!")
            except ValueError:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Enter ID!")
        else:
            info.delete('1.0', tk.END)
            info.insert(tk.END, "Create new ID!")

    def create_id():
        name = file_id.get()
        id = random.randint(1, 10)
        while id in dictionary:
            id = random.randint(1, 10)
        dictionary[id] = name
        info.delete('1.0', tk.END)
        info.insert(tk.END, f"{name} get ID: {id}")

    def show_all():
        if dictionary:
            info.delete('1.0', tk.END)
            info.insert(tk.END, ', '.join(str(key) for key in dictionary))
        else:
            info.delete('1.0', tk.END)
            info.insert(tk.END, "Create new ID!")

    def delete_data():
        if dictionary:
            try:
                key = int(file_id.get())
                if key in dictionary:
                    del dictionary[key]
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, f"ID {key} deleted.")
                else:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, "File was not found!")
            except ValueError:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Enter ID!")
        else:
            info.delete('1.0', tk.END)
            info.insert(tk.END, "Create new ID!")

    def get_id():
        name = file_id.get()
        for key, value in dictionary.items():
            if value == name:
                info.delete('1.0', tk.END)
                info.insert(tk.END, f"ID: {key}")

    def rename_file():
        if dictionary:
            try:
                key = int(file_id.get())
                if key in dictionary:
                    new_name = int(file_id.get())
                    dictionary[key] = new_name
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, f"File name changed. New name: {new_name}")
                else:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, "File was not found!")
            except ValueError:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Enter ID!")
        else:
            info.delete('1.0', tk.END)
            info.insert(tk.END, "Create new ID!")

    def show_list():
        try:
            key = int(file_id.get())
            result = []
            while key > 0:
                if key % 10 in dictionary:
                    result.append(dictionary[key % 10])
                key //= 10
            info.delete('1.0', tk.END)
            info.insert(tk.END, str(result))
        except ValueError:
            info.delete('1.0', tk.END)
            info.insert(tk.END, "Incorrect ID!")

    canvas = tk.Tk()
    canvas.title("First Lab By Alex")
    canvas.geometry("1200x700")

    file_id = tk.Entry(canvas, font='Courier 20')
    file_id.place(x=40, y=20, width=300, height=60)

    get_but = tk.Button(canvas, font='Courier 16', text="User name by ID", command=get_data, foreground='blue')
    get_but.place(x=40, y=100, width=300, height=60)

    create_but = tk.Button(canvas, font='Courier 16', text="Create random ID", command=create_id, foreground='blue')
    create_but.place(x=40, y=180, width=300, height=60)

    showID_but = tk.Button(canvas, font='Courier 16', text="Show ID", command=show_all, foreground='blue')
    showID_but.place(x=40, y=260, width=300, height=60)

    userDelete_but = tk.Button(canvas, font='Courier 16', text="Delete User", command=delete_data,foreground='blue')
    userDelete_but.place(x=40, y=340, width=300, height=60)

    getID_but = tk.Button(canvas, font='Courier 16', text="Get Users ID", command=get_id, foreground='blue')
    getID_but.place(x=40, y=420, width=300, height=60)

    userRename_but = tk.Button(canvas, font='Courier 16', text="Rename ID", command=rename_file, foreground='blue')
    userRename_but.place(x=40, y=500, width=300, height=60)

    IDlist_but = tk.Button(canvas, font='Courier 16', text="List ID", command=show_list, foreground='blue')
    IDlist_but.place(x=40, y=580, width=300, height=60)

    info = tk.Text(canvas, font='14')
    info.place(x=380, y=20, width=740, height=620)

    canvas.mainloop()

if __name__ == "__main__":
    createGUI()

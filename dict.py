import pickle
import tkinter as tk
from tkinter import Scrollbar, Canvas

class Dictionary:
    def __init__(self):
        self.dictionary = self.loadDict()
        self.menu_window = None

    def loadDict(self):
        try:
            with open('dictionary.pkl', 'rb') as file:
                content = pickle.load(file)
        except FileNotFoundError:
            content = []

        contents = [content[i].replace('+', ':').replace('* ', '* Loại từ:').replace('=', '\t>> Example: ').replace('- ', '> Nghĩa: ') for i in range(len(content))]
        dictionary = {}
        for line in contents:
            if line.startswith('@'):
                values = ''
                try:
                    idx = line.find(' /')
                    key = line[1: idx]
                    values += f'Phiên âm:{line[idx:]}'
                except:
                    key = line[1:]
            else:
                values += line

            dictionary[key] = values

        return dictionary

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def create_menu(self):
        self.menu_window = tk.Tk()
        self.menu_window.title("Dictionary Menu")

        # Gọi hàm để đặt kích thước cửa sổ và vị trí ở trung tâm
        self.center_window(self.menu_window, 400, 200)

        menu_label = tk.Label(self.menu_window, text="Select an option:")
        menu_label.pack(pady=10)

        search_button = tk.Button(self.menu_window, text="Search a word", command=self.open_search)
        search_button.pack(pady=5)

        add_button = tk.Button(self.menu_window, text="Insert a new word", command=self.open_add)
        add_button.pack(pady=5)

        delete_button = tk.Button(self.menu_window, text="Delete a word", command=self.open_delete)
        delete_button.pack(pady=5)

        exit_button = tk.Button(self.menu_window, text="Exit", command=self.menu_window.destroy)
        exit_button.pack(pady=5)
        self.menu_window.mainloop()

    def open_search(self):
        self.menu_window.destroy()
        self.create_search_gui()

    def open_add(self):
        self.menu_window.destroy()
        self.create_add_gui()

    def open_delete(self):
        self.menu_window.destroy()
        self.create_delete_gui()

    def create_search_gui(self):
        self.root = tk.Tk()
        self.root.title("Dictionary App - Search")
        
        # Gọi hàm để đặt kích thước cửa sổ và vị trí ở trung tâm
        self.center_window(self.root, 800, 600)

        search_frame = tk.Frame(self.root)
        search_frame.pack(padx=20, pady=20)
        search_label = tk.Label(search_frame, text="Search a word:")
        search_label.pack(anchor='w', pady=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(fill='x', padx=5, pady=5)
        
        search_button = tk.Button(search_frame, text="Search", command=self.searchWord)
        search_button.pack()

        # Thêm nút "Back" cho giao diện con
        back_button = tk.Button(search_frame, text="Back to Menu", command=self.back_to_menu)
        back_button.pack(anchor='center', pady=5)

        self.result_label = tk.Label(self.root, text="", justify='left')
        self.result_label.pack()

        self.root.mainloop()

    def create_add_gui(self):
        self.root = tk.Tk()
        self.root.title("Dictionary App - Add")

        # Gọi hàm để đặt kích thước cửa sổ và vị trí ở trung tâm
        self.center_window(self.root, 400, 300)

        add_frame = tk.Frame(self.root)
        add_frame.pack(padx=20, pady=20)
        add_label = tk.Label(add_frame, text="Insert a new word:")
        add_label.pack(anchor='w', pady=5)
        self.new_word_entry = tk.Entry(add_frame)
        self.new_word_entry.pack(fill='x', padx=5, pady=5)
        meaning_label = tk.Label(add_frame, text="Translate to Vietnamese:")
        meaning_label.pack(anchor='w', pady=5)
        self.meaning_entry = tk.Entry(add_frame)
        self.meaning_entry.pack(fill='x', padx=5, pady=5)
        add_button = tk.Button(add_frame, text="Insert", command=self.addNewWords)
        add_button.pack()

        # Thêm nút "Back" cho giao diện con
        back_button = tk.Button(add_frame, text="Back to Menu", command=self.back_to_menu)
        back_button.pack(anchor='center', pady=5)

        self.result_label = tk.Label(self.root, text="", justify='left')
        self.result_label.pack()

        self.root.mainloop()

    def create_delete_gui(self):
        self.root = tk.Tk()
        self.root.title("Dictionary App - Delete")

        # Gọi hàm để đặt kích thước cửa sổ và vị trí ở trung tâm
        self.center_window(self.root, 400, 300)

        delete_frame = tk.Frame(self.root)
        delete_frame.pack(padx=20, pady=20)
        delete_label = tk.Label(delete_frame, text="Delete a word:")
        delete_label.pack(anchor='w', pady=5)
        self.delete_entry = tk.Entry(delete_frame)
        self.delete_entry.pack(fill='x', padx=5, pady=5)
        delete_button = tk.Button(delete_frame, text="Delete", command=self.deleteWord)
        delete_button.pack()

        # Thêm nút "Back" cho giao diện con
        back_button = tk.Button(delete_frame, text="Back to Menu", command=self.back_to_menu)
        back_button.pack(anchor='center', pady=5)

        self.result_label = tk.Label(self.root, text="", justify='left')
        self.result_label.pack()

        self.root.mainloop()

    # Tạo hàm quay lại menu
    def back_to_menu(self):
        self.root.destroy()
        self.create_menu()

    def searchWord(self):
        word = self.search_entry.get().lower()
        if word not in self.dictionary:
            self.result_label.config(text=f'{word} not found!')
        else:
            self.result_label.config(text=self.dictionary[word])

    def addNewWords(self):
        new_word = self.new_word_entry.get().lower()
        keys = self.dictionary.keys()
        if new_word in keys:
            self.result_label.config(text='This word already exists, please choose another word!')
        else:
            meaning = self.meaning_entry.get()
            self.dictionary[new_word] = meaning
            with open('dictionary.pkl', 'rb') as file:
                content = pickle.load(file)
            content.append(f'@{new_word}\n')
            content.append(f'- {meaning.strip()}\n')
            with open('dictionary.pkl', 'wb') as file:
                pickle.dump(content, file)
            self.result_label.config(text=f'New word: {new_word}\nMeaning: {meaning}\n')

    def deleteWord(self):
        word = self.delete_entry.get().lower()
        keys = self.dictionary.keys()
        if word not in keys:
            self.result_label.config(text='Not found, please choose another word!')
        else:
            with open('dictionary.pkl', 'rb') as file:
                content = pickle.load(file)

            for index, value in enumerate(content):
                if value.startswith(f'@{word}'):
                    idx1 = index
                    break

            for index, value in enumerate(content[idx1+1:]):
                if value.startswith('@'):
                    idx2 = index + idx1
                    break

            del content[idx1:idx2]
            with open('dictionary.pkl', 'wb') as file:
                pickle.dump(content, file)
            self.result_label.config(text=f'Deleted {word} successfully!')

    def menu(self):
        self.create_menu()

if __name__ == "__main__":
    Dictionary().menu()

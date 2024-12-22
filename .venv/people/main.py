import tkinter as tk
from tkinter import messagebox, filedialog
from database import Database
from person import Person


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер Людей")
        self.db = Database()


        self.bg_color = "#DBBCB4"
        self.button_color = "#CFA69D"
        self.text_color = "#9D7972"
        self.entry_bg = "#FAF3F7"
        self.result_bg = "#F8EEF5"


        self.root.configure(bg=self.bg_color)
        self.setup_ui()

    def setup_ui(self):

        title_label = tk.Label(
            self.root,
            text="Менеджер Людей",
            font=("Georgia", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack(pady=10)


        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(fill=tk.X, padx=20)


        left_frame = tk.Frame(input_frame, bg=self.bg_color)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        tk.Label(left_frame, text="Додати нову людину:", font=("Georgia", 14, "bold"),
                 bg=self.bg_color, fg=self.text_color).pack(pady=5)


        self.first_name_entry = self.create_label_entry(left_frame, "*Ім'я:")
        self.last_name_entry = self.create_label_entry(left_frame, "Прізвище:")
        self.middle_name_entry = self.create_label_entry(left_frame, "По-батькові:")
        self.birth_date_entry = self.create_label_entry(left_frame, "*Дата народження:")
        self.death_date_entry = self.create_label_entry(left_frame, "Дата смерті:")
        self.gender_entry = self.create_label_entry(left_frame, "Стать (m/f):")

        # Права частина - поле пошуку
        right_frame = tk.Frame(input_frame, bg=self.bg_color)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        tk.Label(right_frame, text="Пошук:", font=("Georgia", 14, "bold"),
                 bg=self.bg_color, fg=self.text_color).pack(pady=5)

        # Поле пошуку
        search_frame = tk.Frame(right_frame, bg=self.bg_color)
        search_frame.pack(fill=tk.X, pady=5)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Georgia", 12),
            bg=self.entry_bg,
            fg=self.text_color,
            relief=tk.FLAT
        )
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Кнопка пошуку
        search_button = tk.Button(
            search_frame,
            text="Шукати",
            command=self.search_people,
            font=("Georgia", 12),
            bg=self.button_color,
            fg="white",
            relief=tk.RAISED,
            borderwidth=2
        )
        search_button.pack(side=tk.LEFT, padx=5)


        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=10)

        self.create_button(button_frame, "Додати", self.add_person)
        self.create_button(button_frame, "Завантажити все", self.load_all)
        self.create_button(button_frame, "Завантажити з файлу", self.load_from_file)
        self.create_button(button_frame, "Вийти", self.exit_app)


        self.result_text = tk.Text(
            self.root,
            height=20,
            width=80,
            bg=self.result_bg,
            fg=self.text_color,
            font=("Georgia", 12),
            relief=tk.GROOVE,
            wrap=tk.WORD
        )
        self.result_text.pack(pady=10, padx=20)

    def create_label_entry(self, parent, label_text):
        frame = tk.Frame(parent, bg=self.bg_color)
        frame.pack(pady=5, fill=tk.X)

        label = tk.Label(
            frame,
            text=label_text,
            font=("Georgia", 12),
            bg=self.bg_color,
            fg=self.text_color,
            width=20,
            anchor='w'
        )
        label.pack(side=tk.LEFT)

        entry = tk.Entry(
            frame,
            font=("Georgia", 12),
            bg=self.entry_bg,
            fg=self.text_color,
            relief=tk.FLAT
        )
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        return entry

    def create_button(self, frame, text, command):
        button = tk.Button(
            frame,
            text=text,
            command=command,
            font=("Georgia", 12, "bold"),
            bg=self.button_color,
            fg="white",
            relief=tk.RAISED,
            borderwidth=2,
            padx=10,
            pady=5
        )
        button.pack(side=tk.LEFT, padx=5)

    def add_person(self):
        first_name = self.first_name_entry.get().strip()
        if not first_name:
            messagebox.showerror("Помилка", "Ім'я є обов'язковим полем!")
            return
        try:
            person = Person(
                first_name=first_name,
                last_name=self.last_name_entry.get(),
                middle_name=self.middle_name_entry.get(),
                birth_date=self.birth_date_entry.get(),
                death_date=self.death_date_entry.get() or None,
                gender=self.gender_entry.get()
            )
            self.db.add_person(person)
            messagebox.showinfo("Успіх", "Запис додано!")
            # Очистити поля після додавання
            for entry in [self.first_name_entry, self.last_name_entry, self.middle_name_entry,
                          self.birth_date_entry, self.death_date_entry, self.gender_entry]:
                entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Помилка", str(e))

    def search_people(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showinfo("Інформація", "Введіть текст для пошуку")
            return
        # Капитализируем первую букву поискового запроса
        query = query.capitalize()
        results = self.db.search_people(query)
        self.display_results(results)

    def load_all(self):
        results = self.db.load_all()
        self.display_results(results)

    def load_from_file(self):
        file_path = filedialog.askopenfilename(
            title="Оберіть файл бази даних",
            filetypes=[("SQLite Database", "*.db")]
        )
        if file_path:
            self.db.close()
            self.db = Database(file_path)
            messagebox.showinfo("Успіх", f"Базу даних завантажено: {file_path}")

    def display_results(self, people):
        self.result_text.delete(1.0, tk.END)
        if people:
            for person in people:
                if person:  # Перевірка на None
                    self.result_text.insert(tk.END, str(person) + "\n\n")
        else:
            self.result_text.insert(tk.END, "Записів не знайдено.")

    def exit_app(self):
        self.db.close()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()





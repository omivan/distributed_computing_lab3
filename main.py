import tkinter as tk
from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess  

def save_data():
    try:
        intervals = int(interval_entry.get())
        threads = int(threads_entry.get())
        
        result = subprocess.run(["./program", str(intervals), str(threads)], capture_output=True, text=True)
        
        if result.returncode == 0:
            output = result.stdout.splitlines()
            integral_result = output[0] 
            execution_time = output[1]  

            messagebox.showinfo("Успіх", f"{integral_result}\n{execution_time}")
        else:
            messagebox.showerror("Помилка", f"Програма завершилася з помилкою!\n{result.stderr}")
    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректні числа!")
    except FileNotFoundError:
        messagebox.showerror("Помилка", "Не знайдено C++ програму.")

def display_latex():
    fig, ax = plt.subplots(figsize=(3, 1))  
    ax.text(0.5, 0.5, r'$\int_0^{\frac{\pi}{2}} \sin(2t) \cos(3t) \,dt$', 
            fontsize=18, ha='center', va='center')  
    ax.axis('off')  
    canvas = FigureCanvasTkAgg(fig, master=integral_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

window = tk.Tk()
window.title("Інтегральне обчислення")

label_font = ("Arial", 18)
entry_font = ("Arial", 18)

window_width = 600
window_height = 650 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

integral_frame = tk.Frame(window)
integral_frame.pack(pady=20)

display_latex()

method_label = tk.Label(window, text="Метод середніх прямокутників", font=("Arial", 20, "bold"), bd=2)
method_label.pack(pady=20) 

interval_label = tk.Label(window, text="Кількість інтервалів:", font=label_font)
interval_label.pack(pady=20)  

interval_entry = tk.Entry(window, font=entry_font, width=10)
interval_entry.pack(pady=10)

threads_label = tk.Label(window, text="Кількість потоків:", font=label_font)
threads_label.pack(pady=10)

threads_entry = tk.Entry(window, font=entry_font, width=10)
threads_entry.pack(pady=10)

save_button = tk.Button(window, text="Запустити обчислення", font=label_font, command=save_data)
save_button.pack(pady=20)

window.mainloop()

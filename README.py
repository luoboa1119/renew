import tkinter as tk
import time

def start_timer():
    countdown(25 * 60)  # 25 minutes for focus

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=time_format)
        root.update()
        time.sleep(1)
        seconds -= 1

    timer_label.config(text="Time's up!")

# 创建主窗口
root = tk.Tk()
root.title("Focus Timer")

# 创建标签用于显示时间
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# 创建开始按钮
start_button = tk.Button(root, text="Start Focus", command=start_timer)
start_button.pack(pady=10)

# 运行主循环
root.mainloop()

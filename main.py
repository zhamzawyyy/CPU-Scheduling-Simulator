import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Process:
    def __init__(self, pid, burst_time, arrival_time=0, priority=0):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


class ModernScheduler(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPU Scheduler Pro - Professional Edition")
        self.geometry("1000x750")

        self.processes = []

        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)

        ctk.CTkLabel(self.sidebar, text="PROCESS INPUT", font=("Segoe UI", 22, "bold")).pack(pady=25)

        ctk.CTkLabel(self.sidebar, text="Burst Time (Required):", font=("Segoe UI", 12)).pack(pady=(10, 0), padx=20, anchor="w")
        self.in_burst = ctk.CTkEntry(self.sidebar, placeholder_text="e.g. 10", width=220)
        self.in_burst.pack(pady=5, padx=20)

        ctk.CTkLabel(self.sidebar, text="Arrival Time:", font=("Segoe UI", 12)).pack(pady=(10, 0), padx=20, anchor="w")
        self.in_arrival = ctk.CTkEntry(self.sidebar, placeholder_text="e.g. 0", width=220)
        self.in_arrival.insert(0, "0")
        self.in_arrival.pack(pady=5, padx=20)

        ctk.CTkLabel(self.sidebar, text="Priority (Lower = Higher):", font=("Segoe UI", 12)).pack(pady=(10, 0), padx=20, anchor="w")
        self.in_priority = ctk.CTkEntry(self.sidebar, placeholder_text="e.g. 1", width=220)
        self.in_priority.insert(0, "0")
        self.in_priority.pack(pady=5, padx=20)

        self.btn_add = ctk.CTkButton(self.sidebar, text="+ Add to Queue", fg_color="#2ecc71", hover_color="#27ae60",
                                     font=("Segoe UI", 14, "bold"), command=self.add_p)
        self.btn_add.pack(pady=30, padx=20)

        self.btn_reset = ctk.CTkButton(self.sidebar, text="Reset All Data", fg_color="#e74c3c", hover_color="#c0392b",
                                       command=self.reset)
        self.btn_reset.pack(pady=5, padx=20)

        self.main = ctk.CTkFrame(self, corner_radius=15)
        self.main.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.main, text="Simulation Settings", font=("Segoe UI", 18, "bold")).pack(pady=10)

        self.algo_box = ctk.CTkOptionMenu(self.main, values=["Round Robin", "SJF", "Priority Scheduling"], width=200)
        self.algo_box.pack(pady=10)

        ctk.CTkLabel(self.main, text="Time Quantum (for Round Robin only):").pack()
        self.q_entry = ctk.CTkEntry(self.main, width=100)
        self.q_entry.insert(0, "2")
        self.q_entry.pack(pady=5)

        self.btn_run = ctk.CTkButton(self.main, text="START EXECUTION", font=("Segoe UI", 16, "bold"),
                                     width=250, height=40, command=self.simulate)
        self.btn_run.pack(pady=20)

        self.txt = ctk.CTkTextbox(self.main, font=("Consolas", 14), border_width=2)
        self.txt.pack(pady=10, padx=20, fill="both", expand=True)

    def add_p(self):
        try:
            p_id = len(self.processes) + 1
            bt = int(self.in_burst.get())
            at = int(self.in_arrival.get())
            pr = int(self.in_priority.get())

            p = Process(p_id, bt, at, pr)
            self.processes.append(p)
            self.txt.insert("end", f"[+] Process P{p_id} Added: Burst={bt}, Arrival={at}, Priority={pr}\n")
            self.in_burst.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers in all fields!")

    def reset(self):
        self.processes = []
        self.txt.delete("1.0", "end")
        self.txt.insert("end", "System Reset. Ready for new input...\n")

    def simulate(self):
        if not self.processes:
            messagebox.showwarning("Empty Queue", "Please add at least one process first.")
            return

        algo = self.algo_box.get()
        try:
            q = int(self.q_entry.get())
        except:
            q = 2

        procs = [Process(p.pid, p.burst_time, p.arrival_time, p.priority) for p in self.processes]
        time, finished, ready_q, gantt = 0, [], [], []
        pending = sorted(procs, key=lambda x: x.arrival_time)

        while pending or ready_q:
            while pending and pending[0].arrival_time <= time:
                ready_q.append(pending.pop(0))

            if not ready_q:
                time = pending[0].arrival_time
                continue

            if algo == "SJF":
                ready_q.sort(key=lambda x: x.remaining_time)
            elif algo == "Priority Scheduling":
                ready_q.sort(key=lambda x: x.priority)

            p = ready_q.pop(0)

            run = min(p.remaining_time, q) if algo == "Round Robin" else p.remaining_time

            gantt.append(f"P{p.pid}")
            time += run
            p.remaining_time -= run

            while pending and pending[0].arrival_time <= time:
                ready_q.append(pending.pop(0))

            if p.remaining_time > 0:
                ready_q.append(p)
            else:
                p.completion_time = time
                p.turnaround_time = time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time
                finished.append(p)

        self.txt.delete("1.0", "end")
        header = f"{'Process':<10} | {'Arrival':<8} | {'Burst':<8} | {'Wait':<8} | {'Turnaround':<10}\n"
        self.txt.insert("end", header + "=" * 60 + "\n")

        total_wait = 0
        for p in sorted(finished, key=lambda x: x.pid):
            self.txt.insert(
                "end",
                f"P{p.pid:<9} | {p.arrival_time:<8} | {p.burst_time:<8} | {p.waiting_time:<8} | {p.turnaround_time:<10}\n"
            )
            total_wait += p.waiting_time

        self.txt.insert("end", "\n" + "-" * 60 + "\n")
        self.txt.insert("end", f"Average Waiting Time: {total_wait / len(finished):.2f}\n")
        self.txt.insert("end", f"\nGantt Chart Sequence:\n{' -> '.join(gantt)}\n")


if __name__ == "__main__":
    app = ModernScheduler()
    app.mainloop()

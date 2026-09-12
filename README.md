# ⚙️ CPU Scheduling Simulator

## 📌 Project Overview

CPU Scheduling Simulator is a Python-based desktop application that simulates different CPU scheduling algorithms.

The application allows users to add processes with burst time, arrival time, and priority, then simulate the scheduling process and calculate important performance metrics.

---

## 🚀 Features

* Add multiple processes to the scheduling queue.
* Set Burst Time for each process.
* Set Arrival Time for each process.
* Set Process Priority.
* Reset all process data.
* Calculate Waiting Time.
* Calculate Turnaround Time.
* Calculate Average Waiting Time.
* Display the execution sequence.

---

## 🧠 Scheduling Algorithms

### 🔄 Round Robin

Processes are executed using a configurable time quantum.

### ⚡ Shortest Job First (SJF)

The process with the shortest remaining execution time is selected first.

### 🎯 Priority Scheduling

Processes are executed based on their priority.

Lower priority values represent higher priority.

---

## 🛠️ Technologies Used

* Python
* CustomTkinter
* Tkinter

---

## 📂 Project Structure

```text
CPU-Scheduling-Simulator/
│
├── main.py
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CPU-Scheduling-Simulator.git
```

Navigate to the project folder:

```bash
cd CPU-Scheduling-Simulator
```

Install CustomTkinter:

```bash
pip install customtkinter
```

Run the application:

```bash
python main.py
```

---

## 📊 Output

After running a simulation, the application displays:

* Process ID
* Arrival Time
* Burst Time
* Waiting Time
* Turnaround Time
* Average Waiting Time
* Gantt Chart Execution Sequence

---

## 🎓 Concepts Demonstrated

This project demonstrates important Operating Systems concepts, including:

* CPU Scheduling
* Process Management
* Round Robin Scheduling
* Shortest Job First Scheduling
* Priority Scheduling
* Waiting Time Calculation
* Turnaround Time Calculation

---

## 👨‍💻 Author

**z.hamzawyyy**

Junior Data Scientist and Python developer interested in building practical projects and solving real-world problems with technology.

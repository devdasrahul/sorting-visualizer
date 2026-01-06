# 📊 Sorting Algorithm Visualizer

A clean, modern, and educational tool built with **Python** and **Pygame** to visualize how different sorting algorithms work in real-time. This project is designed to simplify complex **Data Structures & Algorithms (DSA)** concepts through interactive animation.

![Sorting Visualizer Demo](https://via.placeholder.com/800x450?text=Sorting+Visualizer+Demo+Placeholder)
*(Replace with actual screenshot)*

---

## 🚀 Features

- **Interactive Visualization**: Watch algorithms process data step-by-step with smooth animations.
- **7+ Supported Algorithms**: Covers basic (Bubble, Insertion) to advanced (Merge, Quick, Heap) algorithms.
- **Educational Overlay**:
  - Real-Time **Time & Space Complexity** dashboard.
  - Live **Comparison & Swap** counters to visualize efficiency.
- **Customizable**: Adjust array size and sorting speed on the fly.
- **Modern UI**: Dark theme, gradient bars, and color-coded status indicators (Compare, Swap, Sorted).

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Library**: Pygame (for 2D graphics and event handling)
- **Concepts**: Sorting Algorithms, Generators, Big-O Notation, Event-Driven Programming

---

## 🧠 Key DSA Concepts

This project allows users to visually verify theoretical concepts:
- **Divide and Conquer**: Visualized clearly in Merge Sort and Quick Sort.
- **Heap Data Structure**: See the heap building and extraction process in Heap Sort.
- **In-Place vs. Out-of-Place**: Visually distinguish algorithms that require extra space (like Merge Sort).
- **Time Complexity**: Observe why $O(n \log n)$ is significantly faster than $O(n^2)$ on large datasets.

---

## 📉 Time & Space Complexity

| Algorithm          | Best Case       | Average Case    | Worst Case      | Space Complexity |
|:-------------------|:----------------|:----------------|:----------------|:-----------------|
| **Bubble Sort**    | $O(n)$          | $O(n^2)$        | $O(n^2)$        | $O(1)$           |
| **Insertion Sort** | $O(n)$          | $O(n^2)$        | $O(n^2)$        | $O(1)$           |
| **Selection Sort** | $O(n^2)$        | $O(n^2)$        | $O(n^2)$        | $O(1)$           |
| **Merge Sort**     | $O(n \log n)$   | $O(n \log n)$   | $O(n \log n)$   | $O(n)$           |
| **Quick Sort**     | $O(n \log n)$   | $O(n \log n)$   | $O(n^2)$        | $O(\log n)$      |
| **Heap Sort**      | $O(n \log n)$   | $O(n \log n)$   | $O(n \log n)$   | $O(1)$           |
| **Counting Sort**  | $O(n+k)$        | $O(n+k)$        | $O(n+k)$        | $O(k)$           |

---

## 🎮 Controls

- **`SPACE`**: Start Sorting
- **`R`**: Reset Array
- **`Arrow Keys`**: Adjust Speed (↑/↓) and Size (←/→)
- **`A` / `D`**: Ascending / Descending Order

**Select Algorithm:**
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Counting Sort

---

## 🏃‍♂️ How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/sorting-visualizer.git
   cd sorting-visualizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python main.py
   ```

## 📸 Screenshots & Demos

### Video Demo
![Sorting Visualizer Video Placeholder](https://via.placeholder.com/800x450?text=Video+Demo+Coming+Soon)

### App Screenshots
![Main Interface](https://via.placeholder.com/800x450?text=Application+Screenshot+1)
![Sorting In Progress](https://via.placeholder.com/800x450?text=Application+Screenshot+2)

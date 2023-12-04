# main.py
import tkinter as tk
from gui import TvGUI
from television import Television


def main():
    """
    Main function to run the TV simulation.

    Creates an instance of Television and TvGUI, setting up the GUI window.
    """
    root = tk.Tk()
    root.title("TV Simulator")
    root.geometry("500x250")
    tv_instance = Television()
    TvGUI(root, tv_instance)
    root.mainloop()


if __name__ == "__main__":
    main()

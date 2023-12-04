# gui.py
import tkinter as tk
from television import Television


class TvGUI:
    """
    GUI class for the TV Simulator.

    Attributes:
    - master (tk.Tk): The main window.
    - tv (Television): The Television instance.

    Methods:
    - __init__(self, master, tv): Constructor to initialize the GUI.
    - create_widgets(self): Create widgets for the GUI.
    - toggle_power(self): Toggle the power state of the TV.
    - toggle_mute(self): Toggle the mute state of the TV.
    - channel_up(self): Increase the TV channel.
    - channel_down(self): Decrease the TV channel.
    - volume_up(self): Increase the TV volume.
    - volume_down(self): Decrease the TV volume.
    - update_screen(self): Update the screen label with current TV state.
    """
    def __init__(self, master, tv):
        """
        Constructor for TvGUI.

        Parameters:
        - master (tk.Tk): The main window.
        - tv (Television): The Television instance.
        """
        self.master = master
        self.master.title("TV Simulator")
        self.tv = tv
        self.create_widgets()

    def create_widgets(self):
        """
        Create widgets for the GUI.
        """
        # Screen label
        self.screen_label = tk.Label(self.master, text="TV Screen", font=("Helvetica", 16))
        self.screen_label.pack(side=tk.TOP, pady=10)

        # Power button
        self.power_button = tk.Button(self.master, text="Power", command=self.toggle_power)
        self.power_button.pack(side=tk.LEFT, padx=5)

        # Channel buttons
        self.channel_up_button = tk.Button(self.master, text="Channel Up", command=self.channel_up)
        self.channel_up_button.pack(side=tk.LEFT, padx=5)

        self.channel_down_button = tk.Button(self.master, text="Channel Down", command=self.channel_down)
        self.channel_down_button.pack(side=tk.LEFT, padx=5)

        # Volume buttons
        self.volume_up_button = tk.Button(self.master, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack(side=tk.LEFT, padx=5)

        self.volume_down_button = tk.Button(self.master, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack(side=tk.LEFT, padx=5)

        # Mute button
        self.mute_button = tk.Button(self.master, text="Mute", command=self.toggle_mute)
        self.mute_button.pack(side=tk.LEFT, padx=5)

        # Exit button
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy)
        self.exit_button.pack(side=tk.BOTTOM, pady=10)

    def toggle_power(self):
        """
        Toggle the power state of the TV.
        """
        self.tv.power()
        self.update_screen()

    def toggle_mute(self):
        """
        Toggle the mute state of the TV.
        """
        self.tv.mute()
        self.update_screen()

    def channel_up(self):
        self.tv.channel_up()
        self.update_screen()

    def channel_down(self):
        self.tv.channel_down()
        self.update_screen()

    def volume_up(self):
        self.tv.volume_up()
        self.update_screen()

    def volume_down(self):
        self.tv.volume_down()
        self.update_screen()

    def update_screen(self):
        """
        Update the screen label with the current TV state.
        """
        state = self.tv.get_state()
        power_status = "On" if state['power'] else 'Off'

        # Check if 'muted' key is present in the state dictionary
        mute_status = "Mute" if 'muted' in state and state['muted'] else "Unmute"

        volume_display = f"Volume: {'🔇' if 'muted' in state and state['muted'] else ''}{state['volume']}"
        screen_text = f"Power: {power_status} | Channel: {state['channel']} | {volume_display} | {mute_status}"
        self.screen_label.config(text=screen_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("TV Simulator")
    root.geometry("500x250")
    tv_instance = Television()
    app = TvGUI(root, tv_instance)
    root.mainloop()

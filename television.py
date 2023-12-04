# television.py

class Television:
    """
    Television class for simulating a TV.

    Attributes:
    - MIN_VOLUME (int): Minimum volume level (constant).
    - MAX_VOLUME (int): Maximum volume level (constant).
    - MIN_CHANNEL (int): Minimum channel number (constant).
    - MAX_CHANNEL (int): Maximum channel number (constant).
    - status (bool): Power status of the TV.
    - muted (bool): Mute status of the TV.
    - volume (int): Current volume level.
    - channel (int): Current channel number.

    Methods:
    - __init__(self): Constructor to initialize TV instance.
    - power(self): Toggle the power state of the TV.
    - mute(self): Toggle the mute state of the TV.
    - channel_up(self): Increase the TV channel.
    - channel_down(self): Decrease the TV channel.
    - volume_up(self): Increase the TV volume.
    - volume_down(self): Decrease the TV volume.
    - get_state(self): Return a dictionary with the current TV state.
    - __str__(self): Return a string representation of the TV state.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 20
    MIN_CHANNEL = 0
    MAX_CHANNEL = 20

    def __init__(self):
        """Initialize default instance variables."""
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
        self._screen = "TV Screen"

    def power(self):
        """Toggle the power status."""
        self._status = not self._status

    def mute(self):
        """Toggle the mute status."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """Increase the channel by 1, considering the maximum channel."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the channel by 1, considering the minimum channel."""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        """Increase the volume by 1, considering the maximum volume."""
        if self._status:
            self._muted = False
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        """Decrease the volume by 1, considering the minimum volume."""
        if self._status:
            self._muted = False
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def change_screen(self, new_screen):
        """Change the TV screen."""
        self._screen = new_screen

    def get_state(self):
        """Get the current state of the Television."""
        return {
            "power": self._status,
            "channel": self._channel,
            "volume": self._volume,
            "screen": self._screen
        }
    

class Television:
    """
    This class represents a television and has functionality  of power, mute, volume, and channels
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the television with default settings
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__mute_memory = 0 # This is used to store the volume when you mute the television


    def power(self)-> None:
        """
        This function will turn the television on and off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self)-> None:
        """
        This function  will mute the television
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__mute_memory
            else:
                self.__muted = True
                self.__mute_memory = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self)-> None:
        """
        This function moves the channel up by one if the channel is on max it will start over
        from the lowest number  the television
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self)-> None:
        """
        This function moves the channel down by one if the channel is on lowest number it will start over
        from the highest number the television
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self)-> None:
        """
        This function will turn the volume up by one volume can't be above MAX_VOLUME
        this will unmute the television
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__mute_memory
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self)-> None:
        """
        This function will turn the volume down by one volume can't be below MIN_VOLUME
        this will unmute the television
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__mute_memory
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self)-> str:
        """
        Returns a string of the television state
        """
        return f'Power- {self.__status}, Channel- {self.__channel},Volume- {self.__volume}.'

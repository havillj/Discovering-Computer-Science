"""
A bare bones Image class based on tkinter.
Requires Python 3.
   
Discovering Computer Science, Second Edition
Jessen Havill

Last updated: 05-12-2020
"""

import tkinter

_root = tkinter.Tk()
_root.withdraw()      # hide root window so no one can quit program until all windows have been closed
_numWindows = 0

def mainloop():
    _root.mainloop()
    
class Image:
    """A bare bones Image class based on tkinter."""
    
    def __init__(self, width = 300, height = 200, file = None, title = None):
        """Constructs a new Image object from a GIF file or a
           new empty image with the given width and height."""
           
        self._checkArgsConstructor(file, width, height, title)
        if file is not None:
            self._file = file
            self._image = tkinter.PhotoImage(file = self._file)
            self._width = self._image.width()
            self._height = self._image.height()
        else:
            self._file = None
            self._width = width
            self._height = height
            self._image = tkinter.PhotoImage(width = self._width, height = self._height)
            
        if title is not None:
            self._title = title
        else:
            self._title = 'Image'
        
    def width(self):
        """Returns the width of the image."""
        
        return self._width
         
    def height(self):
        """Returns the height of the image."""
        
        return self._height
        
    def get(self, x, y):
        """Returns the color (as a 3-tuple) at coordinates (x,y)."""
        
        self._checkCoordinates(x, y)
        color = self._image.get(x, y)
        if isinstance(color, str):
            color = color.split()
        return (int(color[0]), int(color[1]), int(color[2]))
        
    def set(self, x, y, color):
        """Sets the color (a 3-tuple or Tk color string) at coordinates (x,y)."""
        
        self._checkCoordinates(x, y)
        if not isinstance(color, str):
            color = self._tuple2hex(color)
        self._image.put(color, (x, y))
        
    def show(self):
        """Displays the image in a window and waits for it to be closed."""
        
        global _numWindows
        self._window = tkinter.Toplevel()
        _numWindows = _numWindows + 1
        self._window.title(self._title)
        self._window.protocol('WM_DELETE_WINDOW', self._quitWhenAllDone)
        label = tkinter.Label(self._window, image = self._image)
        label.grid()
        self._window.update()
        
    def save(self, fileName):
        if fileName[-4:] not in ('.gif', '.GIF'):
            fileName = fileName + '.gif'
        self._image.write(fileName, format='gif')
        
    def _quitWhenAllDone(self):
        global _numWindows
        _numWindows = _numWindows - 1
        self._window.destroy()
        if _numWindows == 0:
            _root.quit()
        
    def _checkArgsConstructor(self, file, width, height, title):
        if file is not None and not isinstance(file, str):
            raise TypeError('file name must be a string')
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if title is not None and not isinstance(title, str):
            raise TypeError('title must be a string')
            
    def _checkCoordinates(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('x and y must be integers')
        if (x < 0 or x >= self._width) or (y < 0 or y >= self._height):
            raise IndexError('coordinates are out of bounds (image is ' + str(self._width) + ' X ' + str(self._height) + ')')
            
    def _tuple2hex(self, color):
        if not isinstance(color, tuple) or len(color) > 3:
            raise TypeError('color must be a 3-element (red, green, blue) tuple')
            
        for i in range(3):
            if not isinstance(color[i], int) or color[i] < 0 or color[i] > 255:
                raise TypeError('color channel values must be integers between 0 and 255')

        return '#{0:02x}{1:02x}{2:02x}'.format(color[0], color[1], color[2])

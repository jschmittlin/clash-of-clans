import win32gui


class WindowInterface:
    def __init__(self, window_name: str = "Clash of Clans") -> None:
        self.window_name = window_name
        
        hwnd = win32gui.FindWindow(None, self.window_name)
        assert hwnd != 0, f"Window not found: {self.window_name}"
        
        wr = win32gui.GetWindowRect(hwnd)
        cr = win32gui.GetClientRect(hwnd)
        self.w_diff = wr[2] - wr[0] - cr[2] + cr[0]
        self.h_diff = wr[3] - wr[1] - cr[3] + cr[1]
        
        self.borders = (self.w_diff // 2, self.h_diff - self.w_diff // 2)
        self.x_origin_offset = - self.w_diff // 2
        self.y_origin_offset = 0
    
    def move_and_resize(
        self,
        x: int = 1,
        y: int = 0,
        w: int = 1335,
        h: int = 750,
    ) -> None:
        x += self.x_origin_offset
        y += self.y_origin_offset
        w += self.w_diff
        h += self.h_diff
        
        hwnd = win32gui.FindWindow(None, self.window_name)
        assert hwnd != 0, f"Window not found: {self.window_name}"
        
        win32gui.MoveWindow(hwnd, x, y, w, h, True)

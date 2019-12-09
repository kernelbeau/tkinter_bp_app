"""Create the base GUI.
"""
from tkinter import Tk, Menu, Frame, Label, \
    LabelFrame, PhotoImage
from tkinter.messagebox import askokcancel, showinfo
from webbrowser import open_new_tab

WIDTH = 960
HEIGHT = 540
ABOUT = "Version: 0.0.1\nDate: 2019"
BG = 'wheat'  # background color
HELP_PAGE = 'https://github.com/leeurbanek/tkinter_bp_app'
PROG_TITLE = "Blood Pressure Tracker"


class BaseGUI:
    """Build main pplication window, menu bar, and basic layout.
    Provide get_action_frame(), get_chart_frame(), get_stats_frame() method.
    """
    def __init__(self):
        self.root = Tk()
        self.root.bind_all('<F1>', self.show_help_contents)
        self.root.geometry(f"{str(WIDTH)}x{str(HEIGHT)}+0-0")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.minsize(800, 450)
        self.root.title(PROG_TITLE)

        self.build_main_menu()
        self.create_frame_layout()

    def build_main_menu(self):
        """Generic menu bar."""
        menu = Menu(self.root)

        # File dropdown menu
        file_menu = Menu(menu, tearoff=False)
        menu.add_cascade(
            label="File", underline=0, menu=file_menu
            )
        file_menu.add_command(
            label="Exit", underline=1, accelerator='alt+f4',
            command=lambda: self.root.destroy()
            )
        # Help dropdown menu
        help_menu = Menu(menu, tearoff=False)
        menu.add_cascade(
            label="Help", underline=0, menu=help_menu
            )
        help_menu.add_command(
            label="Contents", underline=0,
            command=self.show_help_contents
            )
        help_menu.add_command(
            label="About", underline=0,
            command=lambda: showinfo(
                title="About", message=PROG_TITLE, detail=ABOUT)
                )
        # end menu
        menu.config(bg=BG)
        self.root.config(menu=menu)

    def create_frame_layout(self):
        """Create basic grid for this app."""
        # create the main containers
        top_cont = Frame(
            self.root, bg=BG, padx=6,
            width=WIDTH, height=HEIGHT*(1/5)
            )
        btm_cont = Frame(
            self.root, bg=BG, padx=6, pady=6,
            width=WIDTH, height=HEIGHT*(4/5)
            )
        # layout the main containers
        top_cont.grid(row=0, sticky='ew')
        btm_cont.grid(row=1, sticky='nsew')
        top_cont.grid_rowconfigure(0, weight=1)
        top_cont.grid_columnconfigure(1, weight=1)

        # create the top frames
        logo_frame = Frame(
            top_cont, width=WIDTH*(1/4), height=HEIGHT*(1/5)
            )
        logo_img = PhotoImage(file='img/bp_cuff.gif')
        logo = Label(logo_frame, bg=BG, image=logo_img)
        logo.image = logo_img
        logo.grid(
            row=0, column=0, ipadx=6, ipady=6, sticky='nsew')
        self.action_frame = Frame(
            top_cont, bg='magenta', width=WIDTH*(3/4), height=HEIGHT*(1/5)
            )
        # layout the top frames
        logo_frame.grid(row=0, column=0, sticky='nsew')
        self.action_frame.grid(row=0, column=1, sticky='nsew')

        # create the bottom frames
        btm_cont.grid_rowconfigure(0, weight=1)
        btm_cont.grid_columnconfigure(0, weight=1)
        self.chart_frame = Frame(
            btm_cont, bg=BG,
            width=WIDTH*(2/3), height=HEIGHT*(4/5)
            )
        self.stats_frame = LabelFrame(
            btm_cont, bg=BG, text=' Stats ', padx=6,
            width=WIDTH*(1/3), height=HEIGHT*(4/5)
            )
        # layout the bottom frames
        self.chart_frame.pack(
            expand=True, fill='both', side='left')
        self.stats_frame.pack(
            fill='both', side='right')

    def get_action_frame(self):
        return self.action_frame

    def get_chart_frame(self):
        return self.chart_frame

    def get_stats_frame(self):
        return self.stats_frame

    def show_help_contents(self, event=None):
        """Open tkinter message box."""
        if askokcancel(
            title="Online Documentation",
            message="Do you want to read the help manual online?",
            detail="Click 'OK' to go to the documentation site "
                    "where the help pages are maintained."
                    ):
            open_new_tab(HELP_PAGE)

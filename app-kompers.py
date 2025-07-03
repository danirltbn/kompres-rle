import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from pathlib import Path
from PIL import Image, ImageTk
import numpy as np
import json
from datetime import datetime
import platform
import subprocess
from tkinter import PhotoImage

class ThemeManager:
    def __init__(self):
        self.themes = {
            'dark': {
                'name': 'Midnight',
                'bg': '#1a1a2e',
                'fg': '#e6e6e6',
                'secondary_bg': '#16213e',
                'accent': '#0f3460',
                'button_bg': '#16213e',
                'button_fg': '#ffffff',
                'button_active': '#1f4068',
                'primary': '#e94560',
                'success': '#4CAF50',
                'info': '#00b4d8',
                'warning': '#ff9f1c',
                'danger': '#ff2d75',
                'text_bg': '#1f4068',
                'text_fg': '#f8f8f8',
                'border': '#2d4263',
                'canvas_bg': '#1f4068',
                'highlight': '#e94560',
                'font': ('Segoe UI', 10),
                'heading_font': ('Segoe UI', 12, 'bold'),
                'title_font': ('Segoe UI', 14, 'bold'),
                'icons': {
                    'file': '📄',
                    'image': '🖼️',
                    'folder': '📂',
                    'save': '💾',
                    'compress': '🗜️',
                    'preview': '👁️',
                    'analysis': '📊',
                    'theme': '🎨',
                    'success': '✅',
                    'error': '❌',
                    'info': 'ℹ️',
                    'help': '❓'
                }
            },
            'light': {
                'name': 'Solar',
                'bg': '#f8f9fa',
                'fg': '#212529',
                'secondary_bg': '#e9ecef',
                'accent': '#dee2e6',
                'button_bg': '#e9ecef',
                'button_fg': '#212529',
                'button_active': '#ced4da',
                'primary': '#4361ee',
                'success': '#4CAF50',
                'info': '#4895ef',
                'warning': '#f77f00',
                'danger': '#f72585',
                'text_bg': '#ffffff',
                'text_fg': '#212529',
                'border': '#adb5bd',
                'canvas_bg': '#ffffff',
                'highlight': '#4361ee',
                'font': ('Segoe UI', 10),
                'heading_font': ('Segoe UI', 12, 'bold'),
                'title_font': ('Segoe UI', 14, 'bold'),
                'icons': {
                    'file': '📄',
                    'image': '🖼️',
                    'folder': '📂',
                    'save': '💾',
                    'compress': '🗜️',
                    'preview': '👁️',
                    'analysis': '📊',
                    'theme': '🎨',
                    'success': '✅',
                    'error': '❌',
                    'info': 'ℹ️',
                    'help': '❓'
                }
            },
            'blue': {
                'name': 'Ocean',
                'bg': '#03045e',
                'fg': '#caf0f8',
                'secondary_bg': '#023e8a',
                'accent': '#0077b6',
                'button_bg': '#023e8a',
                'button_fg': '#ffffff',
                'button_active': '#0096c7',
                'primary': '#00b4d8',
                'success': '#4CAF50',
                'info': '#48cae4',
                'warning': '#ff9e00',
                'danger': '#ff5a5f',
                'text_bg': '#0077b6',
                'text_fg': '#ffffff',
                'border': '#0096c7',
                'canvas_bg': '#0077b6',
                'highlight': '#00b4d8',
                'font': ('Segoe UI', 10),
                'heading_font': ('Segoe UI', 12, 'bold'),
                'title_font': ('Segoe UI', 14, 'bold'),
                'icons': {
                    'file': '📄',
                    'image': '🖼️',
                    'folder': '📂',
                    'save': '💾',
                    'compress': '🗜️',
                    'preview': '👁️',
                    'analysis': '📊',
                    'theme': '🎨',
                    'success': '✅',
                    'error': '❌',
                    'info': 'ℹ️',
                    'help': '❓'
                }
            },
            'forest': {
                'name': 'Forest',
                'bg': '#1b4332',
                'fg': '#d8f3dc',
                'secondary_bg': '#2d6a4f',
                'accent': '#40916c',
                'button_bg': '#2d6a4f',
                'button_fg': '#ffffff',
                'button_active': '#52b788',
                'primary': '#b7e4c7',
                'success': '#4CAF50',
                'info': '#95d5b2',
                'warning': '#f48c06',
                'danger': '#e5383b',
                'text_bg': '#40916c',
                'text_fg': '#ffffff',
                'border': '#52b788',
                'canvas_bg': '#40916c',
                'highlight': '#b7e4c7',
                'font': ('Segoe UI', 10),
                'heading_font': ('Segoe UI', 12, 'bold'),
                'title_font': ('Segoe UI', 14, 'bold'),
                'icons': {
                    'file': '📄',
                    'image': '🖼️',
                    'folder': '📂',
                    'save': '💾',
                    'compress': '🗜️',
                    'preview': '👁️',
                    'analysis': '📊',
                    'theme': '🎨',
                    'success': '✅',
                    'error': '❌',
                    'info': 'ℹ️',
                    'help': '❓'
                }
            },
            'sunset': {
                'name': 'Sunset',
                'bg': '#3a0ca3',
                'fg': '#f8edeb',
                'secondary_bg': '#7209b7',
                'accent': '#f72585',
                'button_bg': '#7209b7',
                'button_fg': '#ffffff',
                'button_active': '#b5179e',
                'primary': '#f72585',
                'success': '#4CAF50',
                'info': '#4895ef',
                'warning': '#f77f00',
                'danger': '#d00000',
                'text_bg': '#560bad',
                'text_fg': '#ffffff',
                'border': '#b5179e',
                'canvas_bg': '#560bad',
                'highlight': '#f72585',
                'font': ('Segoe UI', 10),
                'heading_font': ('Segoe UI', 12, 'bold'),
                'title_font': ('Segoe UI', 14, 'bold'),
                'icons': {
                    'file': '📄',
                    'image': '🖼️',
                    'folder': '📂',
                    'save': '💾',
                    'compress': '🗜️',
                    'preview': '👁️',
                    'analysis': '📊',
                    'theme': '🎨',
                    'success': '✅',
                    'error': '❌',
                    'info': 'ℹ️',
                    'help': '❓'
                }
            }
        }
        
        # Load saved theme or default to system preference
        self.current_theme = self.load_theme() or self.detect_system_theme()
    
    def detect_system_theme(self):
        """Detect system theme preference"""
        try:
            system = platform.system()
            if system == "Windows":
                import winreg
                registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                key = winreg.OpenKey(registry, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize")
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                winreg.CloseKey(key)
                return 'light' if value == 1 else 'dark'
            elif system == "Darwin":
                cmd = 'defaults read -g AppleInterfaceStyle'
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output, _ = process.communicate()
                return 'light' if b'Light' in output else 'dark'
            elif system == "Linux":
                try:
                    cmd = 'gsettings get org.gnome.desktop.interface gtk-theme'
                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    output, _ = process.communicate()
                    return 'light' if b'light' in output.lower() else 'dark'
                except:
                    return 'dark'
        except:
            return 'dark'
    
    def get_theme(self, theme_name=None):
        """Get theme by name or current theme"""
        if theme_name is None:
            theme_name = self.current_theme
        return self.themes.get(theme_name, self.themes['dark'])
    
    def load_theme(self):
        """Load saved theme from config file"""
        try:
            config_path = os.path.join(os.path.expanduser('~'), '.file_converter_theme.json')
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    return config.get('theme')
        except:
            pass
        return None
    
    def save_theme(self, theme_name):
        """Save theme preference to config file"""
        try:
            config_path = os.path.join(os.path.expanduser('~'), '.file_converter_theme.json')
            with open(config_path, 'w') as f:
                json.dump({'theme': theme_name}, f)
            return True
        except:
            return False
    
    def set_theme(self, theme_name):
        """Set current theme"""
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.save_theme(theme_name)
            return True
        return False
    
    def get_theme_names(self):
        """Get available theme names"""
        return list(self.themes.keys())

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter - KTM Asli")
        self.root.geometry("1200x800")  # Diperbesar untuk menampung panel bantuan
        
        # Initialize theme manager
        self.theme_manager = ThemeManager()
        self.current_theme = self.theme_manager.get_theme()
        
        # Variables
        self.selected_files = []
        self.original_image = None
        self.processed_image = None
        self.compression_data = {}
        self.themed_widgets = []
        self.help_shown = False
        
        # Set window icon
        self.set_window_icon()
        
        self.setup_ui()
        self.apply_theme()
    
    def set_window_icon(self):
        """Set window icon based on theme"""
        try:
            # Simple example icon in Base64 format
            icon_data = """
                R0lGODlhEAAQAIUAAPwCBISChCQmJGRmZJSWlLS2tNTS1PT29Pz+/AQGBIyKjJSWlLS2tNTS
                1PT29Pz6/OTi5Nza3NTS1Ozm7Ozm9OTi7Nza5NTS3OTm7Ozm9PTy9Pz+/Pz6/AAAAAAAAAAA
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkKAC0AAAAAEAAQAAAGhMCW
                cEgsGo9IJACwTDqfUKhUOaVardisdsvter/gsHhMLpvP6LR6zW673/C4fE6v2+/4vH7P7/v/
                gIGCg4SFhoeIiYqLjI2Oj5CRkpOUlZaXmJmam5ydnp+goaKjpKWmp6ipqqusra6vsLGys7S1
                tre4ubq7vL2+v8DBwsPExcbHyMnKy8zNzs8QADs=
            """
            self.icon = PhotoImage(data=icon_data)
            self.root.tk.call('wm', 'iconphoto', self.root._w, self.icon)
        except:
            pass
    
    def setup_ui(self):
        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # Theme menu with icons
        theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        for theme_name in self.theme_manager.get_theme_names():
            theme_data = self.theme_manager.get_theme(theme_name)
            theme_menu.add_command(
                label=f"{theme_data['icons']['theme']} {theme_data['name']}",
                command=lambda name=theme_name: self.change_theme(name)
            )
        self.menu_bar.add_cascade(label=f"{self.current_theme['icons']['theme']} Tema", menu=theme_menu)
        
        # Create main container
        main_container = tk.Frame(self.root)
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        self.add_themed_widget(main_container, 'frame')
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill='both', expand=True, side='left')
        self.add_themed_widget(self.notebook, 'notebook')
        
        # Main processing tab
        self.main_frame = tk.Frame(self.notebook)
        self.notebook.add(self.main_frame, text=f"{self.current_theme['icons']['compress']} Kompresi File")
        self.add_themed_widget(self.main_frame, 'frame')
        
        # Image preview tab
        self.preview_frame = tk.Frame(self.notebook)
        self.notebook.add(self.preview_frame, text=f"{self.current_theme['icons']['preview']} Preview Gambar")
        self.add_themed_widget(self.preview_frame, 'frame')
        
        # Data analysis tab
        self.analysis_frame = tk.Frame(self.notebook)
        self.notebook.add(self.analysis_frame, text=f"{self.current_theme['icons']['analysis']} Analisis Data")
        self.add_themed_widget(self.analysis_frame, 'frame')
        
        # Setup help panel (akan muncul di sebelah kanan notebook)
        self.setup_help_panel(main_container)
        
        # Setup tabs content
        self.setup_main_tab(self.main_frame)
        self.setup_preview_tab(self.preview_frame)
        self.setup_analysis_tab(self.analysis_frame)
    
    def setup_help_panel(self, parent):
        """Setup the help panel on the right side"""
        # Frame untuk penjelasan RLE (awalnya tersembunyi)
        self.help_panel = tk.Frame(parent, width=300)
        self.add_themed_widget(self.help_panel, 'frame')
        self.help_panel.pack_propagate(False)  # Mempertahankan lebar
        self.help_panel.pack(side='right', fill='y', padx=10, pady=10)
        
        # Konten panel bantuan
        help_title = tk.Label(
            self.help_panel,
            text=f"{self.current_theme['icons']['help']} Tentang Kompresi RLE",
            font=self.current_theme['title_font']
        )
        self.add_themed_widget(help_title, 'label', title=True)
        help_title.pack(pady=10)
        
        help_text = tk.Text(
            self.help_panel,
            wrap=tk.WORD,
            font=self.current_theme['font'],
            height=30,
            padx=10,
            pady=10
        )
        self.add_themed_widget(help_text, 'text')
        
        # Isi penjelasan RLE
        rle_explanation = """
Run-Length Encoding (RLE) adalah metode kompresi sederhana yang 
bekerja dengan mengganti urutan data yang sama (run) dengan 
satu nilai data dan jumlah kemunculannya.

🔹 Cara Kerja RLE:
1. Gambar diubah ke mode hitam-putih (binary)
2. Setiap baris gambar dipindai pixel per pixel
3. Urutan pixel dengan warna sama dikompresi
   Contoh: "black:5 | white:10 | black:3"

🔹 Contoh Kompresi:
Data asli:  A A A A B B B C C D D D D
Hasil RLE: 4A 3B 2C 4D

🔹 Keuntungan RLE:
- Sederhana dan cepat diproses
- Efektif untuk gambar dengan area warna solid
- Tidak kehilangan kualitas (lossless compression)
- Mudah diimplementasikan

🔹 Keterbatasan:
- Kurang efektif untuk gambar kompleks/bertekstur
- Rasio kompresi tidak setinggi metode lain
- Tidak optimal untuk gambar dengan banyak perubahan warna

🔹 Penggunaan dalam Aplikasi Ini:
1. Pilih file gambar (JPG/PNG/BMP)
2. Klik tombol 'Kompres'
3. Gambar akan dikonversi ke hitam-putih
4. Dilakukan kompresi RLE per baris
5. Hasil kompresi ditampilkan dalam format teks
6. Rasio kompresi dihitung dan ditampilkan

Tips:
- Untuk hasil terbaik, gunakan gambar dengan area warna solid
- Gambar KTM biasanya cocok untuk kompresi RLE
- Hasil kompresi bisa disimpan sebagai file teks atau JSON
"""
        help_text.insert(tk.END, rle_explanation)
        help_text.config(state='disabled')
        help_text.pack(fill='both', expand=True)
    
    def add_themed_widget(self, widget, widget_type, **kwargs):
        """Add widget to themed widgets list"""
        self.themed_widgets.append({
            'widget': widget,
            'type': widget_type,
            **kwargs
        })
    
    def change_theme(self, theme_name):
        """Change application theme"""
        if self.theme_manager.set_theme(theme_name):
            self.current_theme = self.theme_manager.get_theme()
            self.apply_theme()
    
    def apply_theme(self):
        """Apply current theme to all widgets"""
        theme = self.current_theme
        
        # Configure root
        self.root.configure(bg=theme['bg'])
        
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Set default font
        default_font = theme['font']
        style.configure('.', font=default_font)
        
        # Notebook style
        style.configure('TNotebook', background=theme['secondary_bg'])
        style.configure('TNotebook.Tab', 
                      background=theme['secondary_bg'],
                      foreground=theme['fg'],
                      padding=[10, 5],
                      font=theme['heading_font'])
        style.map('TNotebook.Tab',
                background=[('selected', theme['accent'])],
                foreground=[('selected', theme['fg'])])
        
        # Treeview style
        style.configure('Treeview',
                      background=theme['text_bg'],
                      foreground=theme['text_fg'],
                      fieldbackground=theme['text_bg'],
                      borderwidth=1)
        style.configure('Treeview.Heading',
                      background=theme['secondary_bg'],
                      foreground=theme['fg'],
                      font=theme['heading_font'])
        
        # Scrollbar style
        style.configure('Vertical.TScrollbar',
                      background=theme['secondary_bg'],
                      troughcolor=theme['bg'],
                      bordercolor=theme['border'],
                      arrowcolor=theme['fg'])
        
        # Apply to all themed widgets
        for widget_info in self.themed_widgets:
            widget = widget_info['widget']
            widget_type = widget_info['type']
            
            try:
                if widget_type == 'frame':
                    widget.configure(bg=theme['bg'])
                elif widget_type == 'label':
                    if widget_info.get('title', False):
                        widget.configure(bg=theme['bg'], fg=theme['fg'], font=theme['title_font'])
                    elif widget_info.get('heading', False):
                        widget.configure(bg=theme['bg'], fg=theme['fg'], font=theme['heading_font'])
                    else:
                        widget.configure(bg=theme['bg'], fg=theme['fg'], font=theme['font'])
                elif widget_type == 'button':
                    if widget_info.get('primary', False):
                        widget.configure(
                            bg=theme['primary'],
                            fg=theme['button_fg'],
                            activebackground=theme['button_active'],
                            font=theme['font']
                        )
                    elif widget_info.get('success', False):
                        widget.configure(
                            bg=theme['success'],
                            fg=theme['button_fg'],
                            activebackground=theme['button_active'],
                            font=theme['font']
                        )
                    elif widget_info.get('info', False):
                        widget.configure(
                            bg=theme['info'],
                            fg=theme['button_fg'],
                            activebackground=theme['button_active'],
                            font=theme['font']
                        )
                    else:
                        widget.configure(
                            bg=theme['button_bg'],
                            fg=theme['button_fg'],
                            activebackground=theme['button_active'],
                            font=theme['font']
                        )
                elif widget_type == 'listbox':
                    widget.configure(
                        bg=theme['text_bg'],
                        fg=theme['text_fg'],
                        selectbackground=theme['accent'],
                        selectforeground=theme['fg'],
                        font=theme['font']
                    )
                elif widget_type == 'text':
                    widget.configure(
                        bg=theme['text_bg'],
                        fg=theme['text_fg'],
                        insertbackground=theme['fg'],
                        font=theme['font']
                    )
                elif widget_type == 'canvas':
                    widget.configure(
                        bg=theme['canvas_bg'],
                        highlightbackground=theme['border']
                    )
                elif widget_type == 'labelframe':
                    widget.configure(
                        bg=theme['secondary_bg'],
                        fg=theme['fg'],
                        font=theme['heading_font']
                    )
                elif widget_type == 'notebook':
                    pass  # Already configured via ttk style
            except tk.TclError:
                continue
    
    def setup_main_tab(self, parent):
        # Title
        title_frame = tk.Frame(parent)
        self.add_themed_widget(title_frame, 'frame')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text=f"{self.current_theme['icons']['compress']} Kompresi Citra KTM Menggunakan Metode Run-Length Encoding (RLE)", 
            font=self.current_theme['title_font']
        )
        self.add_themed_widget(title_label, 'label', title=True)
        title_label.pack()
        
        # Help button
        help_btn = tk.Button(
            title_frame,
            text=f" {self.current_theme['icons']['help']} Bantuan",
            font=self.current_theme['font'],
            command=lambda: self.notebook.select(self.notebook.index(self.main_frame)),
            cursor='hand2'
        )
        self.add_themed_widget(help_btn, 'button', info=True)
        help_btn.pack(pady=10)
        
        # Main container
        main_container = tk.Frame(parent)
        self.add_themed_widget(main_container, 'frame')
        main_container.pack(expand=True, fill='both', padx=40, pady=20)
        
        # File selection section
        file_frame = tk.LabelFrame(
            main_container, 
            text=f"{self.current_theme['icons']['folder']} Pilih File", 
            font=self.current_theme['heading_font']
        )
        self.add_themed_widget(file_frame, 'labelframe')
        file_frame.pack(fill='x', pady=(0, 20))
        
        self.select_btn = tk.Button(
            file_frame,
            text=f" {self.current_theme['icons']['folder']} Ambil Gambar",
            font=self.current_theme['font'],
            padx=20,
            pady=10,
            command=self.select_files,
            cursor='hand2'
        )
        self.add_themed_widget(self.select_btn, 'button', success=True)
        self.select_btn.pack(pady=15)
        
        # File list
        self.file_listbox = tk.Listbox(
            file_frame,
            height=3,
            font=self.current_theme['font']
        )
        self.add_themed_widget(self.file_listbox, 'listbox')
        self.file_listbox.pack(fill='x', padx=10, pady=(0, 15))
        
        # Process button
        self.process_btn = tk.Button(
            main_container,
            text=f" {self.current_theme['icons']['compress']} Kompres {self.current_theme['icons']['help']}",
            font=self.current_theme['heading_font'],
            padx=30,
            pady=15,
            command=self.process_files,
            cursor='hand2'
        )
        self.add_themed_widget(self.process_btn, 'button', primary=True)
        self.process_btn.pack(pady=20)
        
        # Output section
        output_frame = tk.LabelFrame(
            main_container,
            text=f"{self.current_theme['icons']['file']} Hasil Kompres",
            font=self.current_theme['heading_font']
        )
        self.add_themed_widget(output_frame, 'labelframe')
        output_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # Text area with scrollbar
        text_frame = tk.Frame(output_frame)
        self.add_themed_widget(text_frame, 'frame')
        text_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.output_text = tk.Text(
            text_frame,
            font=self.current_theme['font'],
            wrap=tk.WORD
        )
        self.add_themed_widget(self.output_text, 'text')
        
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Save buttons frame
        save_frame = tk.Frame(main_container)
        self.add_themed_widget(save_frame, 'frame')
        save_frame.pack(pady=10)
        
        self.save_txt_btn = tk.Button(
            save_frame,
            text=f" {self.current_theme['icons']['save']} Simpan sebagai File .txt",
            font=self.current_theme['font'],
            padx=20,
            pady=10,
            command=self.save_output,
            cursor='hand2'
        )
        self.add_themed_widget(self.save_txt_btn, 'button', info=True)
        self.save_txt_btn.pack(side='left', padx=5)
        
        self.save_json_btn = tk.Button(
            save_frame,
            text=f" {self.current_theme['icons']['save']} Simpan Data JSON",
            font=self.current_theme['font'],
            padx=20,
            pady=10,
            command=self.save_json_data,
            cursor='hand2'
        )
        self.add_themed_widget(self.save_json_btn, 'button', primary=True)
        self.save_json_btn.pack(side='left', padx=5)
    
    def setup_preview_tab(self, parent):
        # Title
        preview_title = tk.Label(
            parent,
            text=f"{self.current_theme['icons']['preview']} Preview Gambar Sebelum dan Sesudah Kompresi",
            font=self.current_theme['title_font']
        )
        self.add_themed_widget(preview_title, 'label', title=True)
        preview_title.pack(pady=20)
        
        # Images container
        images_frame = tk.Frame(parent)
        self.add_themed_widget(images_frame, 'frame')
        images_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Original image frame
        original_frame = tk.LabelFrame(
            images_frame,
            text=f"{self.current_theme['icons']['image']} Gambar Asli",
            font=self.current_theme['heading_font']
        )
        self.add_themed_widget(original_frame, 'labelframe')
        original_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        self.original_canvas = tk.Canvas(
            original_frame,
            highlightthickness=0,
            width=400,
            height=300
        )
        self.add_themed_widget(self.original_canvas, 'canvas')
        self.original_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Processed image frame
        processed_frame = tk.LabelFrame(
            images_frame,
            text=f"{self.current_theme['icons']['image']} Gambar Setelah Kompresi",
            font=self.current_theme['heading_font']
        )
        self.add_themed_widget(processed_frame, 'labelframe')
        processed_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        self.processed_canvas = tk.Canvas(
            processed_frame,
            highlightthickness=0,
            width=400,
            height=300
        )
        self.add_themed_widget(self.processed_canvas, 'canvas')
        self.processed_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Image info frame
        info_frame = tk.Frame(parent)
        self.add_themed_widget(info_frame, 'frame')
        info_frame.pack(fill='x', padx=20, pady=10)
        
        self.image_info_text = tk.Text(
            info_frame,
            height=4,
            font=self.current_theme['font'],
            wrap=tk.WORD
        )
        self.add_themed_widget(self.image_info_text, 'text')
        self.image_info_text.pack(fill='x')
    
    def setup_analysis_tab(self, parent):
        # Title
        analysis_title = tk.Label(
            parent,
            text=f"{self.current_theme['icons']['analysis']} Analisis Data Kompresi",
            font=self.current_theme['title_font']
        )
        self.add_themed_widget(analysis_title, 'label', title=True)
        analysis_title.pack(pady=20)
        
        # Statistics frame
        stats_frame = tk.LabelFrame(
            parent,
            text=f"{self.current_theme['icons']['info']} Statistik Kompresi",
            font=self.current_theme['heading_font']
        )
        self.add_themed_widget(stats_frame, 'labelframe')
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        self.stats_text = tk.Text(
            stats_frame,
            height=10,
            font=self.current_theme['font'],
            wrap=tk.WORD
        )
        self.add_themed_widget(self.stats_text, 'text')
        self.stats_text.pack(fill='x', padx=10, pady=10)
        
        # Comparison table frame
        table_frame = tk.LabelFrame(
            parent,
            text=f"{self.current_theme['icons']['analysis']} Perbandingan Data",
            font=self.current_theme['heading_font']
        )
        self.add_themed_widget(table_frame, 'labelframe')
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Treeview for comparison data
        columns = ('Metric', 'Original', 'Compressed', 'Ratio')
        self.comparison_tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.comparison_tree.heading(col, text=col)
            self.comparison_tree.column(col, width=150)
        
        self.comparison_tree.pack(fill='both', expand=True, padx=10, pady=10)
    
    def select_files(self):
        """Select files for processing"""
        filetypes = [
            ('Image files', '*.png *.jpg *.jpeg *.bmp *.gif *.tiff'),
            ('All files', '*.*')
        ]
        
        files = filedialog.askopenfilenames(
            title="Pilih file untuk dikonversi",
            filetypes=filetypes
        )
        
        if files:
            self.selected_files = list(files)
            self.update_file_list()
            if len(files) > 0:
                self.load_image_preview(files[0])
    
    def update_file_list(self):
        """Update the file listbox"""
        self.file_listbox.delete(0, tk.END)
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            self.file_listbox.insert(tk.END, f"{self.current_theme['icons']['file']} {filename}")
    
    def load_image_preview(self, file_path):
        """Load and display image preview"""
        try:
            # Load original image
            self.original_image = Image.open(file_path)
            
            # Resize for display
            display_size = (300, 300)
            original_display = self.original_image.copy()
            original_display.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.original_photo = ImageTk.PhotoImage(original_display)
            
            # Display on canvas
            self.display_original_image(original_display)
            
            # Update image info
            self.update_image_info()
            
        except Exception as e:
            messagebox.showerror("Error", f"{self.current_theme['icons']['error']} Gagal memuat gambar: {str(e)}")
    
    def display_original_image(self, image):
        """Display original image on canvas"""
        try:
            self.original_canvas.delete("all")
            canvas_width = self.original_canvas.winfo_width() or 400
            canvas_height = self.original_canvas.winfo_height() or 300
            
            # Center the image
            x = max(0, (canvas_width - image.width) // 2)
            y = max(0, (canvas_height - image.height) // 2)
            
            self.original_canvas.create_image(x, y, anchor='nw', image=self.original_photo)
            
        except Exception as e:
            print(f"Error displaying original image: {str(e)}")
    
    def update_image_info(self):
        """Update image information display"""
        if self.original_image:
            info = f"{self.current_theme['icons']['info']} Informasi Gambar:\n"
            info += f"Resolusi: {self.original_image.size[0]} x {self.original_image.size[1]}\n"
            info += f"Mode: {self.original_image.mode}\n"
            info += f"Format: {self.original_image.format if self.original_image.format else 'Unknown'}\n"
            
            # Get file size safely
            try:
                if hasattr(self.original_image, 'filename') and self.original_image.filename:
                    file_size = os.path.getsize(self.original_image.filename)
                elif self.selected_files:
                    file_size = os.path.getsize(self.selected_files[0])
                else:
                    file_size = 0
                    
                if file_size > 0:
                    info += f"Ukuran File: {file_size:,} bytes ({file_size/1024:.2f} KB)\n"
            except (OSError, AttributeError):
                info += "Ukuran File: Tidak dapat diakses\n"
            
            self.image_info_text.delete(1.0, tk.END)
            self.image_info_text.insert(1.0, info)
    
    def process_files(self):
        """Process the selected files"""
        if not self.selected_files:
            messagebox.showwarning("Peringatan", f"{self.current_theme['icons']['warning']} Silakan pilih file terlebih dahulu!")
            return
        
        self.output_text.delete(1.0, tk.END)
        
        try:
            result = ""
            self.compression_data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'files': []
            }
            
            for i, file_path in enumerate(self.selected_files):
                filename = os.path.basename(file_path)
                result += f"=== File {i+1}: {filename} ===\n\n"
                
                # Get original file info
                original_size = os.path.getsize(file_path)
                
                # Convert to RLE
                converted_data, processed_img = self.convert_to_rle(file_path)
                result += f"RLE Encoding (Hitam-Putih):\n{converted_data}\n\n"
                
                # Calculate compression ratio
                compressed_size = len(converted_data)
                compression_ratio = original_size / compressed_size if compressed_size > 0 else 0
                
                result += f"Informasi Kompresi:\n"
                result += f"Ukuran asli: {original_size:,} bytes\n"
                result += f"Ukuran terkompresi: {compressed_size:,} bytes\n"
                result += f"Rasio kompresi: {compression_ratio:.2f}\n\n"
                
                # Store compression data
                file_data = {
                    'filename': filename,
                    'original_size': original_size,
                    'compressed_size': len(converted_data),
                    'compression_ratio': compression_ratio,
                    'method': 'RLE',
                    'compressed_data': converted_data
                }
                self.compression_data['files'].append(file_data)
                
                # Update processed image preview
                if i == 0 and processed_img:
                    self.show_processed_image(processed_img)
                
                result += "-" * 50 + "\n\n"
            
            self.output_text.insert(1.0, result)
            self.update_analysis_tab()
            messagebox.showinfo("Sukses", f"{self.current_theme['icons']['success']} Berhasil memproses {len(self.selected_files)} file!")
            
        except Exception as e:
            messagebox.showerror("Error", f"{self.current_theme['icons']['error']} Terjadi kesalahan: {str(e)}")
    
    def convert_to_rle(self, file_path):
        """Convert image to RLE format"""
        try:
            # Load image and convert to binary
            image = Image.open(file_path)
            # Convert to grayscale first
            gray_image = image.convert('L')
            # Convert to binary (black and white)
            binary_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
            
            # Convert to numpy array for RLE processing
            img_array = np.array(binary_image)
            
            # Perform RLE encoding
            rle_data = []
            for row in img_array:
                # Flatten row and perform RLE
                flat_row = row.flatten()
                rle_row = self.encode_rle(flat_row)
                rle_data.append(rle_row)
            
            # Format RLE data
            rle_string = "\n".join([f"Row {i+1}: {row}" for i, row in enumerate(rle_data[:10])])  # Show first 10 rows
            if len(rle_data) > 10:
                rle_string += f"\n... ({len(rle_data)-10} more rows)"
            
            return rle_string, binary_image
            
        except Exception as e:
            return f"Error in RLE conversion: {str(e)}", None
    
    def encode_rle(self, data):
        """Encode data using Run-Length Encoding"""
        if len(data) == 0:
            return ""
        
        encoded = []
        current_value = data[0]
        count = 1
        
        for i in range(1, len(data)):
            if data[i] == current_value:
                count += 1
            else:
                color = "black" if current_value == 0 else "white"
                encoded.append(f"{color}:{count}")
                current_value = data[i]
                count = 1
        
        # Add the last run
        color = "black" if current_value == 0 else "white"
        encoded.append(f"{color}:{count}")
        
        return " | ".join(encoded)
    
    def show_processed_image(self, processed_img):
        """Display processed image on canvas"""
        try:
            # Resize for display
            display_size = (300, 300)
            processed_display = processed_img.copy()
            processed_display.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.processed_photo = ImageTk.PhotoImage(processed_display)
            
            # Display on canvas
            self.display_processed_image(processed_display)
            
        except Exception as e:
            print(f"Error displaying processed image: {str(e)}")
    
    def display_processed_image(self, image):
        """Display processed image on canvas"""
        try:
            self.processed_canvas.delete("all")
            canvas_width = self.processed_canvas.winfo_width() or 400
            canvas_height = self.processed_canvas.winfo_height() or 300
            
            # Center the image
            x = max(0, (canvas_width - image.width) // 2)
            y = max(0, (canvas_height - image.height) // 2)
            
            self.processed_canvas.create_image(x, y, anchor='nw', image=self.processed_photo)
            
        except Exception as e:
            print(f"Error displaying processed image: {str(e)}")
    
    def update_analysis_tab(self):
        """Update analysis tab with compression statistics"""
        if not self.compression_data or not self.compression_data['files']:
            return
        
        # Update statistics text
        stats = f"{self.current_theme['icons']['analysis']} STATISTIK KOMPRESI\n"
        stats += "=" * 50 + "\n\n"
        
        total_original = sum(f['original_size'] for f in self.compression_data['files'])
        total_compressed = sum(f['compressed_size'] for f in self.compression_data['files'])
        avg_ratio = sum(f['compression_ratio'] for f in self.compression_data['files']) / len(self.compression_data['files'])
        
        stats += f"Total file diproses: {len(self.compression_data['files'])}\n"
        stats += f"Total ukuran asli: {total_original:,} bytes ({total_original/1024:.2f} KB)\n"
        stats += f"Total ukuran terkompresi: {total_compressed:,} bytes ({total_compressed/1024:.2f} KB)\n"
        stats += f"Penghematan: {total_original - total_compressed:,} bytes ({((total_original - total_compressed)/total_original*100):.2f}%)\n"
        stats += f"Rata-rata rasio kompresi: {avg_ratio:.2f}\n\n"
        
        stats += "DETAIL PER FILE:\n"
        stats += "-" * 30 + "\n"
        for file_data in self.compression_data['files']:
            stats += f"File: {file_data['filename']}\n"
            stats += f"  Method: {file_data['method']}\n"
            stats += f"  Ukuran asli: {file_data['original_size']:,} bytes\n"
            stats += f"  Ukuran terkompresi: {file_data['compressed_size']:,} bytes\n"
            stats += f"  Rasio: {file_data['compression_ratio']:.2f}\n"
            stats += f"  Penghematan: {((file_data['original_size'] - file_data['compressed_size'])/file_data['original_size']*100):.2f}%\n\n"
        
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(1.0, stats)
        
        # Update comparison table
        for item in self.comparison_tree.get_children():
            self.comparison_tree.delete(item)
        
        for file_data in self.compression_data['files']:
            self.comparison_tree.insert('', 'end', values=(
                file_data['filename'],
                f"{file_data['original_size']:,} bytes",
                f"{file_data['compressed_size']:,} bytes",
                f"{file_data['compression_ratio']:.2f}"
            ))
    
    def save_output(self):
        """Save output to text file"""
        content = self.output_text.get(1.0, tk.END).strip()
        
        if not content:
            messagebox.showwarning("Peringatan", f"{self.current_theme['icons']['warning']} Tidak ada konten untuk disimpan!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Simpan hasil konversi",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                messagebox.showinfo("Sukses", f"{self.current_theme['icons']['success']} File berhasil disimpan: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"{self.current_theme['icons']['error']} Gagal menyimpan file: {str(e)}")
    
    def save_json_data(self):
        """Save compression data to JSON file"""
        if not self.compression_data:
            messagebox.showwarning("Peringatan", f"{self.current_theme['icons']['warning']} Tidak ada data kompresi untuk disimpan!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Simpan data kompresi",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(self.compression_data, file, indent=2, ensure_ascii=False)
                messagebox.showinfo("Sukses", f"{self.current_theme['icons']['success']} Data JSON berhasil disimpan: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"{self.current_theme['icons']['error']} Gagal menyimpan data JSON: {str(e)}")

def main():
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import rumps
import pyperclip
from typing import Optional
from color_parser import Color
from date_parser import DateManager
from text_analyzer import TextAnalyzer
from line_parser import LineParser
from hash_generator import HashGenerator


class ClipboardManager(rumps.App):
    def __init__(self):
        super().__init__("📋")
        self.last_clipboard = ""
        self.current_color: Optional[Color] = None
        self.current_date: Optional[DateManager] = None
        self.menu = []
        self.setup_menu()

    def setup_menu(self):
        """Setup the main menu"""
        self.setup_text_analyzer()
        self.setup_line_transform()
        self.setup_text_tranform()
        self.setup_developer_menu()
        self.setup_color_menu()
        self.setup_date_menu()

        self.menu = [
            self.word_count_disp,
            self.char_count_disp,
            self.text_stats_menu,
            None,  # Separator
            self.line_menu,
            self.text_menu,
            self.developer_menu,
            self.color_menu,
            self.fake_color_menu,  # Placeholder since rumps doesn't support greyed out menu items
            self.date_menu,
            self.fake_date_menu,
            None,  # Separator
            rumps.MenuItem("Clear Clipboard", callback=self.clear_clipboard),
        ]

    def setup_line_transform(self):
        """Setup line transformation menu"""
        self.line_menu = rumps.MenuItem("Line Transformations")
        menus = [
            "Remove Duplicates",
            "Strip Empty Lines",
            "Sort Lines",
            "To List",
            "To CSV",
        ]
        for menu in menus:
            self.line_menu.add(rumps.MenuItem(menu, callback=self._transform_line))

    def setup_text_analyzer(self):
        """Setup text analysis menu"""
        self.word_count_disp = rumps.MenuItem("Words: 0")
        self.char_count_disp = rumps.MenuItem("Characters: 0")
        self.text_stats_menu = rumps.MenuItem("More Stats")
        self.text_stats_menu.add(None)
        self.text_analyzer = TextAnalyzer()

    def setup_text_tranform(self):
        """Setup text transformation menu"""
        self.text_menu = rumps.MenuItem("Text Transformations")
        menus = ["UPPERCASE", "lowercase", "camelCase", "snake_case", "Title Case"]
        for menu in menus:
            self.text_menu.add(rumps.MenuItem(menu, callback=self._transform_text))

    def setup_developer_menu(self):
        """Setup developer tools menu"""
        self.developer_menu = rumps.MenuItem("Developer Tools")

        options = ["MD5 Hash", "SHA1 Hash", "SHA256 Hash"]
        for op in options:
            self.developer_menu.add(rumps.MenuItem(op, callback=self._copy_hash))

    def setup_color_menu(self):
        """Setup color conversion menu"""
        self.color_menu = rumps.MenuItem("Color Conversions")
        self.color_preview = rumps.MenuItem("Current Color: None")
        self.color_menu.add(self.color_preview)
        self.color_menu.add(None)  # Separator
        self.fake_color_menu = self.dummy_menu("Color Conversions")
        self.fake_color_menu.hide()

        options = ["Copy as HEX", "Copy as RGB", "Copy as HSL"]
        for op in options:
            self.color_menu.add(rumps.MenuItem(op, callback=self._copy_color))

    def setup_date_menu(self):
        """Setup date conversion menu"""
        self.date_menu = rumps.MenuItem("Date Conversions")
        self.date_preview = rumps.MenuItem("Current Date: None")
        self.date_menu.add(self.date_preview)
        self.date_menu.add(None)  # Separator
        self.fake_date_menu = self.dummy_menu("Date Conversions")
        self.fake_date_menu.hide()

        options = [
            "Copy as ISO (YYYY-MM-DD)",
            "Copy as US (MM/DD/YYYY)",
            "Copy as European (DD/MM/YYYY)",
            "Copy as Long (Month DD, YYYY)",
            "Copy as Short (Mon DD, YYYY)",
        ]

        for op in options:
            self.date_menu.add(rumps.MenuItem(op, callback=self._copy_date))

    def dummy_menu(self, lable: str) -> rumps.MenuItem:
        """Create a dummy menu item
        This is used as a placeholder for rumps menu items that are disabled
        """
        menu = rumps.MenuItem(lable)
        menu.add(None)
        menu.set_callback(None)
        return menu

    def update_text_analysis(self):
        """Update text analysis menu items"""
        text = self.last_clipboard
        self.word_count_disp.title = (
            f"Word Count: {self.text_analyzer.count_words(text)}"
        )

        char_counts = self.text_analyzer.count_chars(text)
        self.char_count_disp.title = f"Character Count: {char_counts['total']}"

        self.text_stats_menu.clear()
        stats = [
            f"Characters (no spaces): {char_counts['no_spaces']}",
            f"Characters (no whitespace): {char_counts['no_whitespace']}",
            f"Lines: {self.text_analyzer.line_count(text)}",
            f"Paragraphs: {self.text_analyzer.count_paragraphs(text)}",
            f"Sentences: {self.text_analyzer.count_sentences(text)}",
            f"Read Time: {self.text_analyzer.read_time(text)}",
        ]
        self.text_stats_menu.update(stats)

    def set_color_menu_state(self, enabled: bool):
        """Enable or disable color menu items"""
        if not enabled:
            self.color_menu.hide()
            self.fake_color_menu.show()
            return

        self.color_preview.title = f"Current Color: {self.last_clipboard}"
        self.color_menu.show()
        self.fake_color_menu.hide()

    def set_date_menu_state(self, enabled: bool):
        """Enable or disable date menu items"""
        if not enabled:
            self.date_menu.hide()
            self.fake_date_menu.show()
            return

        self.date_preview.title = f"Current Date: {self.last_clipboard}"
        self.date_menu.show()
        self.fake_date_menu.hide()

    @rumps.timer(1)
    def check_clipboard(self, _):
        """Monitor clipboard for changes and update available options"""
        current = pyperclip.paste()
        if current != self.last_clipboard:
            self.last_clipboard = current
            self.update_menus_visibility()
            self.update_text_analysis()

    def update_menus_visibility(self):
        """Update menu states based on clipboard content"""
        text = self.last_clipboard.strip()

        self.current_color = Color.from_string(text)
        self.set_color_menu_state(self.current_color is not None)

        self.current_date = DateManager.from_string(text)
        self.set_date_menu_state(self.current_date is not None)

    def _transform_text(self, sender):
        """
        Handle text transformation options
        Method should only be called as a callback for text menu items.
        """
        text = self.last_clipboard

        formats = {
            "UPPERCASE": text.upper,
            "lowercase": text.lower,
            "camelCase": lambda: " ".join(word.capitalize() for word in text.split()),
            "snake_case": lambda: "_".join(text.split()),
            "Title Case": text.title,
        }

        text = formats[sender.title]()
        pyperclip.copy(text)

    def _transform_line(self, sender):
        """
        Handle line transformation options
        Method should only be called as a callback for line menu items.
        """
        text = self.last_clipboard

        formats = {
            "Remove Duplicates": LineParser.remove_duplicates,
            "Strip Empty Lines": LineParser.strip_empty_lines,
            "Sort Lines": LineParser.sort_lines,
            "To List": LineParser.to_list,
            "To CSV": LineParser.to_csv,
        }

        text = formats[sender.title](text)
        pyperclip.copy(text)

    def _copy_hash(self, sender):
        """
        Handle hash generation
        Method should only be called as a callback for hash menu items.
        """
        text = self.last_clipboard
        if not text:
            return

        hash_gen = HashGenerator(text)
        formats = {
            "MD5 Hash": hash_gen.get_md5,
            "SHA1 Hash": hash_gen.get_sha1,
            "SHA256 Hash": hash_gen.get_sha256,
        }

        hash = formats[sender.title]()
        pyperclip.copy(hash)

    def _copy_color(self, sender):
        """
        Handle color conversion and copying
        Method should only be called as a callback for color menu items.
        """
        if not self.current_color:
            return

        formats = {
            "Copy as HEX": self.current_color.to_hex,
            "Copy as RGB": self.current_color.to_rgb,
            "Copy as HSL": self.current_color.to_hsl,
        }

        color = formats[sender.title]()
        pyperclip.copy(color)

    def _copy_date(self, sender):
        """
        Handle date conversions.
        Method should only be called as a callback for date menu items.
        """
        if not self.current_date:
            return

        formats = {
            "Copy as ISO (YYYY-MM-DD)": self.current_date.to_iso,
            "Copy as US (MM/DD/YYYY)": self.current_date.to_us,
            "Copy as European (DD/MM/YYYY)": self.current_date.to_european,
            "Copy as Long (Month DD, YYYY)": self.current_date.to_long,
            "Copy as Short (Mon DD, YYYY)": self.current_date.to_short,
        }

        date = formats[sender.title]()
        pyperclip.copy(date)

    def clear_clipboard(self, _):
        """Clear the clipboard"""
        pyperclip.copy("")

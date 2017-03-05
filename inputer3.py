import sublime
import sublime_plugin
import subprocess
import os


class inputer3Command(sublime_plugin.TextCommand):
    def run(self, edit):
        # 选中区域
        sel = self.view.sel()
        # 文本输入
        text_output = os.popen("zenity --entry --title='inputer3' --width='0' --height='0'  ").read().strip()
        if text_output:
            for region in sel:
                if region.size() == 0:
                    # 插入
                    self.view.insert(edit, region.end(), text_output)
                else:
                    # 替换
                    self.view.replace(edit, region, text_output)
"""
纯电动汽车驱动传动系统实训台 - 详细电路原理演示
启动脚本：使用 pywebview 创建原生桌面窗口
"""
import webview
import os
import sys

def get_html_path():
    """获取HTML文件的绝对路径"""
    if getattr(sys, 'frozen', False):
        # PyInstaller 打包后的路径
        base_path = sys._MEIPASS
    else:
        # 开发环境路径
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    html_file = os.path.join(base_path, 'ev_powertrain_demo.html')
    if not os.path.exists(html_file):
        print(f"错误：找不到 {html_file}")
        sys.exit(1)
    return html_file

class Api:
    """暴露给 JavaScript 的 Python API"""
    def __init__(self):
        self.window = None

    def get_platform(self):
        """返回当前平台信息"""
        return sys.platform

    def minimize(self):
        """最小化窗口"""
        if self.window:
            self.window.minimize()

    def toggle_fullscreen(self):
        """切换全屏"""
        if self.window:
            self.window.toggle_fullscreen()

    def close_app(self):
        """关闭应用"""
        if self.window:
            self.window.destroy()

def main():
    html_path = get_html_path()
    api = Api()

    # 创建窗口
    window = webview.create_window(
        title='纯电动汽车驱动传动系统实训台 - 详细电路原理演示',
        url=html_path,
        width=1400,
        height=900,
        min_size=(800, 600),
        resizable=True,
        text_select=True,
        zoomable=False,  # 由程序内部处理缩放
        frameless=False,
        easy_drag=False,
    )
    api.window = window

    # 启动窗口（阻塞直到关闭）
    webview.start(debug=False, http_server=False)

if __name__ == '__main__':
    main()

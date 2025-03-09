#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
构建脚本 - 将RPGTranslationAssistant编译为独立的Windows可执行程序
无需Python环境即可运行
"""

import os
import sys
import subprocess
import shutil
import argparse
import platform

def check_dependencies():
    """检查并安装必要的依赖"""
    print("检查并安装必要的依赖...")
    
    # 安装PyInstaller（如果尚未安装）
    try:
        import PyInstaller
        print("PyInstaller已安装。")
    except ImportError:
        print("正在安装PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller安装完成。")

def build_executable(output_name="RPGTranslationAssistant", onefile=False, add_data=None, icon=None):
    """构建可执行文件"""
    print(f"开始构建{'单文件' if onefile else '多文件'}可执行程序...")
    
    # 检测操作系统
    is_windows = platform.system() == "Windows"
    path_sep = ";" if is_windows else ":"
    
    # 基本命令
    cmd = [
        sys.executable,  # 使用当前Python解释器路径
        "-m", "PyInstaller",  # 以模块方式调用PyInstaller
        "--name", output_name,
        "--noconfirm",  # 不询问确认
        "--clean",      # 清理临时文件
    ]
    
    # 是否打包成单个文件
    if onefile:
        cmd.append("--onefile")
    else:
        cmd.append("--onedir")
    
    # 添加Windows子系统标志（无控制台窗口）
    cmd.append("--windowed")
    
    # 添加图标（如果提供）
    if icon and os.path.exists(icon):
        cmd.extend(["--icon", icon])
    
    # 添加数据文件（作为目录复制）
    if add_data:
        for src, dst in add_data:
            if os.path.exists(src):
                # 使用正确的路径分隔符
                cmd.extend(["--add-data", f"{src}{path_sep}{dst}"])
                print(f"添加资源目录: {src} -> {dst}")
            else:
                print(f"警告: 找不到数据目录: {src}")
    
    # 添加主脚本
    cmd.append("RPGTranslationAssistant.py")
    
    # 运行PyInstaller
    print("执行命令:", " ".join(cmd))
    try:
        subprocess.check_call(cmd)
        
        # 如果是多文件模式，检查文件夹是否已正确复制
        if not onefile:
            dist_dir = os.path.join("dist", output_name)
            
            # 检查并复制资源文件夹
            required_folders = ["RPGRewriter", "EasyRPG", "RTPCollection"]
            for folder in required_folders:
                src_folder = folder
                dst_folder = os.path.join(dist_dir, folder)
                
                if not os.path.exists(dst_folder) and os.path.exists(src_folder):
                    print(f"手动复制资源文件夹: {src_folder} -> {dst_folder}")
                    shutil.copytree(src_folder, dst_folder)
            
            # 确保Works文件夹存在
            works_dir = os.path.join(dist_dir, "Works")
            if not os.path.exists(works_dir):
                print(f"创建Works文件夹: {works_dir}")
                os.makedirs(works_dir)
                
        print(f"构建完成! 可执行文件位于 'dist/{output_name}{'' if onefile else '/'}'")
    except FileNotFoundError:
        print("错误: 无法找到PyInstaller。")
        print("诊断信息:")
        print(f"Python路径: {sys.executable}")
        print(f"系统PATH: {os.environ.get('PATH', '')}")
        print("尝试运行: pip show pyinstaller")
        subprocess.run([sys.executable, "-m", "pip", "show", "pyinstaller"])
        raise
    except subprocess.CalledProcessError as e:
        print(f"错误: PyInstaller返回错误代码 {e.returncode}")
        raise

def main():
    parser = argparse.ArgumentParser(description="构建RPGTranslationAssistant的Windows可执行程序")
    parser.add_argument("--name", default="RPGTranslationAssistant", help="输出文件名")
    parser.add_argument("--onefile", action="store_true", help="使用单文件模式（默认为多文件）")
    parser.add_argument("--icon", default=None, help="应用程序图标路径")
    args = parser.parse_args()
    
    # 检查依赖
    check_dependencies()
    
    # 定义要包含的数据目录
    data_dirs = [
        ("RPGRewriter", "RPGRewriter"),
        ("EasyRPG", "EasyRPG"),
        ("RTPCollection", "RTPCollection"),
        ("Works", "Works")
    ]
    
    # 构建可执行文件
    build_executable(
        output_name=args.name, 
        onefile=args.onefile,  # 默认多文件模式
        add_data=data_dirs,
        icon=args.icon
    )
    
    # 显示后续步骤
    print("\n======= 构建完成 =======")
    if args.onefile:
        print(f"可执行文件已创建: dist/{args.name}.exe")
    else:
        print(f"可执行文件及资源已创建: dist/{args.name}/")
        print("请确保分发时包含整个文件夹")
    
    print("\n注意事项:")
    print("1. 确保您的RTP文件(.zip)已放入RTPCollection文件夹")
    print("2. 确保RPGRewriter文件夹包含RPGRewriter.exe和相关文件")
    print("3. 首次运行程序可能需要稍长时间启动")
    print("========================\n")

if __name__ == "__main__":
    main() 
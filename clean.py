# -*- coding:utf-8 -*-
"""
clean module.
"""

#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import os
import shutil
from pathlib import Path


def main():
    """
    删除构建过程中生成的临时文件和目录。
    """

    # 定义要删除的目录列表
    directories_to_clean = ["build", "dist"]

    # 移除指定的目录
    for directory in directories_to_clean:
        if os.path.exists(directory):
            print(f"Removing {directory}")
            shutil.rmtree(directory)

    # 移除 .egg-info 文件夹
    for item in Path('.').glob('*/*.egg-info'):
        if item.is_dir():
            print(f"Removing {item}")
            shutil.rmtree(item)

    # 移除 .spec 文件
    for file in os.listdir('.'):
        if file.endswith('.spec'):
            spec_file_path = os.path.join('.', file)
            try:
                os.remove(spec_file_path)
                print(f"Successfully removed file: {spec_file_path}")
            except Exception as e:
                print(f"Failed to remove file {spec_file_path}: {e}")

    # 移除 .log 文件
    for file in os.listdir('.'):
        if file.endswith('.log'):
            spec_file_path = os.path.join('.', file)
            try:
                os.remove(spec_file_path)
                print(f"Successfully removed file: {spec_file_path}")
            except Exception as e:
                print(f"Failed to remove file {spec_file_path}: {e}")

    print("Clean operation completed.")


if __name__ == "__main__":
    main()

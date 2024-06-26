#参考 https://juejin.cn/post/7053009657371033630, https://zhuanlan.zhihu.com/p/527321393
#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    # Groot_tool_helper_v1.whl

    name='Groot_tool_helper',  # 必填，项目的名字，用户根据这个名字安装，pip install SpiderKeeper-new
    version='1.0.0',  # 必填，项目的版本，建议遵循语义化版本规范
    long_description=long_description,  # 项目的详细说明，通常读取 README.md 文件的内容
    long_description_content_type='text/markdown',  # 描述的格式，可选的值： text/plain, text/x-rst, and text/markdown
    author_email='2390189571@qq.com',  # 作者的有效邮箱地址
    url='https://github.com/tornadoboys/Groot_tool_helper/tree/master',  # 项目的源码地址
    license='MIT',
    include_package_data=True,
    package_data= {
        'src' : ["resources/"]
    },

    install_requires=[
        'tqdm>=4.0',  # 指定tqdm的最低版本号
        # 在这里添加其他依赖包
    ],

    packages=find_packages(),  # 必填，指定打包的目录，默认是当前目录，如果是其他目录比如 src, 可以使用 find_packages(where='src')
    # 分类器通过对项目进行分类，帮助用户找到项目
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires=">=3.8"
)

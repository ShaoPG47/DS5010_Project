from setuptools import setup, find_packages

DESCRIPTION = "A Python library for data manipulation and visualization"
ver = '0.0.1'
setup(
    name='muncher',
    author='Anqi Guo, Zhenan Zhuang, Zuoming Zhang, Pengli Shao',
    author_email='guoanqi57@gmail.com, z28964713@gmail.com, zhuang.zu@northeastern.edu, shao.pe@northeastern.edu',
    version= ver,
    description = DESCRIPTION,
    packages=find_packages(),
    install_requires=['csv', 'json', 'xml', 'sqliter3','time','random'],
    keywords=['python', 'data manipulation', 'data visualization','importing and exporting data','merge data sets'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Data analytics',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows'
    ]
)

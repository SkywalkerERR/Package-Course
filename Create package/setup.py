#Сначала мы импортируем модуль setuptools, содержащий удобные методы настройки упаковки.

#1. В вызове функции setup() большинство параметров очень простые и не требуют пояснений. Рассмотрим основные моменты:
#name. Имя дистрибутива пакета, которое на pypi.org должно быть уникальным.
#Хороший способ обеспечить эту уникальность — присоединить к имени пакета имя пользователя в PyPI.

#2. long_description. Из файла README.md обычно устанавливается подробное описание.
# Для его корректного отображения вы указываете, что это файл Markdown, задавая параметр long_description_content_type.

#3. packages. Перечень пакетов, подлежащих публикации в пакете дистрибутива.
# Поскольку мы публикуем только один пакет test_package, то в списке значится именно его имя.
# Однако если вы планируете опубликовать все пакеты директории, то для удобства их извлечения используйте setuptools.find_packages().

#4. python_requires. Указывает необходимую для пакета версию Python.

import setuptools

with open('README.md') as file:
    read_me_discription = file.read()

setuptools.setup(
    name='test-package-username',
    version='0.1',
    author='Apex',
    author_email='my_email',
    description='This is a test package.',
    long_description=read_me_discription,
    long_description_content_type='text/markdown',
    url='package_github_page',
    packages=['test_package'],
    classifilers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
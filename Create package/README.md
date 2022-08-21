Это тестовый пакет, представляющий собой часть обучающего руководства Meduim. 

**Текст жирным шрифтом** 

*Текст, выделенный курсивом* 

setup.py sdist bdist_wheel - **Дистрибуция пакета** \
twine upload --repository testpypi dist/* - **Загрузкаа пакета** \
pip install -i https://test.pypi.org/simple/ test-package-username==0.1.1 - **Импорт пакет**
## Лицензия 
Лицензия MIT
# coordinate_distribution
Проект для исследования аккустической эмиссии в горных породах. Строит распределение энергии
(локальных напряжений или других параметров) по координате, делает аппроксимацию полученной зависимости.
Вычисляет некоторые энергетические и статистические параметры эксперимента.
Структура входного файла: Time X  E (или другой параметр, распределения которого будут анализироваться)

## Имена переменных в файлах статистики:
*Interval_end_time* -- Конец временного интервала (время последнего события в выборке, состоящей из фиксированнного числа событий)

*Gauss_expected_value* -- мат.ожидание распределения Гаусса энергии по координате

*Raw_data_argmax* -- координата MAX значения Esum в выборке

*FWHM_(FULL_width)* -- ширина колокола Гауссова распределения на полувысоте

*Esum_Gauss* -- суммарная энергия в распределении Гаусса

*Esum_raw* -- MAX значение Esum 

*Emax_raw* -- MAX значение E 

*Emax_coord_raw* -- координата события с MAX значением E
 
